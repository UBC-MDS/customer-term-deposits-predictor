# Predicting Customer Term Deposits

- **Contributors/Authors:** Elshaday Yoseph, Meagan Gardner, Mu Ha, Shell Ou

## Project Summary

This project investigates whether a machine learning model can predict if a bank customer will subscribe to a term deposit account. A term deposit is a low-risk investment option where customers lock in a fixed sum of money for a specific period at an agreed interest rate, making it an attractive choice for risk-averse individuals. The analysis is based on data from a Portuguese banking institution collected during phone marketing campaigns.

Key objectives include:
1. **Optimizing Marketing Campaigns**: By identifying customers most likely to subscribe, banks can target campaigns more effectively, saving time and resources.
2. **Understanding Customer Behavior**: Insights from the analysis reveal key patterns in customer demographics, financial attributes, and their interaction history with the bank.

### Analysis Process:
1. **Data Preprocessing**: The dataset includes 45,211 records with 17 features such as age, job, balance, and contact history. Missing values were handled, and irrelevant columns were removed (e.g., `poutcome` and `duration`) to avoid data leakage and noise.
2. **Exploratory Data Analysis (EDA)**: Visualizations such as count plots and box plots were used to understand the relationships between features (e.g., job type, account balance) and term deposit subscriptions.
3. **Modeling**: A logistic regression model was developed with feature scaling to handle imbalanced data. The target variable was encoded as binary (1 for subscription, 0 for non-subscription).
4. **Evaluation**: Metrics such as precision, recall, F1-score, and AUC were used to assess model performance. 

### Key Findings:
- The target variable is highly imbalanced, with only 11.7% of customers subscribing to term deposits.
- The logistic regression model achieved:
  - Macro-average recall: **0.68**
  - AUC score: **0.75**
- The model performs well in identifying non-subscribers but struggles with precision for subscribers (23%). This indicates potential for improvement, especially in reducing false positives to optimize marketing efforts.

### Recommendations:
1. Explore advanced machine learning techniques like Random Forests or Gradient Boosting to improve precision and recall for minority classes.
2. Incorporate additional features such as transaction history, customer engagement metrics, or economic indicators to enhance predictive power.
3. Conduct further research on the economic context (e.g., interest rates) to better understand external factors affecting subscription behavior.

This analysis provides actionable insights to banks, allowing them to design more focused marketing strategies and build stronger relationships with customers by aligning products with their preferences.

## Report
The final report can be found [here](https://ubc-mds.github.io/customer-term-deposits-predictor/)

## How to Run the Data Analysis

1. **Set Up the Environment**:
   - Ensure you have Python 3.8 or higher installed.
   - Install dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Alternatively, create a Conda environment:
     ```bash
     conda env create -f environment.yml
     conda activate customer-term-deposits
     ```

2. **Run the Analysis**:
   - Launch Jupyter Lab:
     ```bash
     jupyter lab
     ```
   - Open `notebooks/analysis.ipynb` and execute the cells to run the full analysis pipeline.

3. **Preprocessed Data**:
   - Preprocessed datasets (`X_train_scaled`, `X_test_scaled`, `y_train`, `y_test`) are available in the `data/processed/` folder.

## Dependencies

The analysis requires the following packages:
- Python 3.8+
- pandas 1.5+
- numpy 1.23+
- seaborn 0.12+
- matplotlib 3.6+
- scikit-learn 1.5+
- Jupyter Lab 4.0+

For detailed versions, refer to:
- [`environment.yml`](environment.yml)

## License

This project is licensed under the MIT License. For detailed information, see the [`LICENSE`](LICENSE) file.
