import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import click

@click.command()
@click.option('--train_x_path', type=str, help='Path to the training features.')
@click.option('--train_y_path', type=str, help='Path to the training labels.')
@click.option('--figures_dir', type=str, help='Directory to save figures.')
@click.option('--tables_dir', type=str, help='Directory to save tables.')
def eda(train_x_path, train_y_path, figures_dir, tables_dir):
    # Load training data
    X_train = pd.read_csv(train_x_path)
    y_train = pd.read_csv(train_y_path)

    # Merge for EDA
    data = pd.concat([X_train, y_train], axis=1)

    # Create directories if they don't exist
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)

    # Save summary statistics to a CSV
    summary_stats = data.describe()
    summary_stats.to_csv(os.path.join(tables_dir, 'summary_statistics.csv'), index=True)

    # Distribution of target variable
    sns.countplot(x='y', data=data)
    plt.title('Distribution of Target Variable')
    plt.savefig(os.path.join(figures_dir, 'target_variable_distribution.png'))
    plt.close()

    # Boxplot for balance vs subscription status
    sns.boxplot(x='y', y='balance', data=data)
    plt.title('Balance Distribution by Subscription Status')
    plt.savefig(os.path.join(figures_dir, 'balance_distribution.png'))
    plt.close()

    print("EDA completed. Figures and tables saved.")

if __name__ == '__main__':
    eda()
