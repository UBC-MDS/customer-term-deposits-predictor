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

> Ensure Docker Desktop is running on your desktop.

1. **Clone this github repository**

2. **Open Docker**:
   - In your command line, navigate to the root of this project directory and enter the following command:
    ``` 
    docker-compose up
    ```
    - Note: this command may take a few minutes to run.
    - Once the command is finished running, look for a URL that starts with "http://127.0.0.1:8888/lab?token=". Copy and paste
      this URL into your browser. 

3. **Run the Analysis in Docker**:
   - Ensure you are connected to the term-deposit-predictor environment in the Jupyter Lab container:
     <img src="jupyter-environment-check.png">
   - If you are not in the environment, from the dropdown options under Start Preferred Kernel select
     `Python [conda env:term-deposit-predictor]*`
   - Navigate to the analysis folder and open the `customer-term-deposits-predictor.ipynb` notebook
   - Under the "Kernel" menu select "Restart Kernel and Run all Cells..."
     
4. **Shutting down Docker**
   - To close out of the container, exit out of the browser and return back to your terminal.
   - In the terminal where you launched the container, enter `Cntrl` + `C` on your keyboard
   - Then type `docker-compose rm`
   - Type `y` and hit enter to remove the container

## Dependencies

The analysis requires the following packages:
- Python 3.8+
- pandas 1.5+
- numpy 1.23+
- seaborn 0.12+
- matplotlib 3.6+
- Jupyter Lab 4.0+

For detailed versions, refer to:
- [`environment.yml`](environment.yml)

## License

This project is licensed under the MIT License. For detailed information, see the [`LICENSE`](LICENSE) file.
