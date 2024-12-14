PHONY: all clean

all: data/raw/bank-full.csv data/processed/preprocessed_data.csv data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv results/tables/summary_statistics.csv results/figures/target_variable_distribution.png results/figures/balance_distribution.png results/models/logistic_regression_model.pkl scaler.pkl results/figures/feature_densities_by_class.png results/figures/feature_densities_by_class.png results/figures/facet_grid_plot.png results/figures/Confusion_Matrix.png results/figures/ROC_curve.png results/figures/PR_curve.png analysis/customer-term-deposits-predictor.html

#download and extract data
data/raw/bank-full.csv: scripts/download_customer_data.py 
	python scripts/download_customer_data.py \
		--url https://archive.ics.uci.edu/static/public/222/bank+marketing.zip \
    	--download_zip_file1 data/raw/bank+marketing.zip \
    	--zip_path data/raw/bank_marketing \
		--file_path data/raw/ \
		--zip_file_name bank.zip

# Clean the data
data/processed/cleaned_data.csv: scripts/clean_data.py data/raw/bank-full.csv
	python scripts/clean_data.py \
	    --input_path data/raw/bank-full.csv \
	    --output_path data/processed/cleaned_data.csv

# Preprocess the data
data/processed/preprocessed_data.csv: scripts/preprocess_data.py data/processed/cleaned_data.csv
	python scripts/preprocess_data.py \
		--input_path data/processed/cleaned_data.csv \
	    --output_path data/processed/preprocessed_data.csv

# Split the data
data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv: scripts/split_data.py data/processed/preprocessed_data.csv
	python scripts/split_data.py \
	    --input_path data/processed/preprocessed_data.csv \
	    --output_path data/processed/ \
	    --testing_size 0.3

# Perform exploratory data analysis (EDA)
results/tables/metrics.csv results/tables/summary_statistics.csv results/figures/target_variable_distribution.png results/figures/balance_distribution.png: scripts/eda.py data/processed/X_train.csv data/processed/y_train.csv
	python scripts/eda.py \
	    --train_x_path data/processed/X_train.csv \
	    --train_y_path data/processed/y_train.csv \
	    --figures_dir results/figures \
	    --tables_dir results/tables

# Train logistic regression model
results/models/logistic_regression_model.pkl scaler.pkl results/figures/feature_densities_by_class.png results/figures/feature_densities_by_class.png results/figures/facet_grid_plot.png: scripts/fit_logistic_regression.py data/processed/X_train.csv data/processed/y_train.csv
	python scripts/fit_logistic_regression.py \
	    --x-training-data data/processed/X_train.csv \
	    --y-training-data data/processed/y_train.csv \
	    --pipeline-to results/models \
	    --plot-to results/figures \
	    --seed 123

# Evaluate the model
results/figures/Confusion_Matrix.png results/figures/ROC_curve.png results/figures/PR_curve.png: scripts/evaluate.py data/processed/X_test.csv data/processed/y_test.csv
	python scripts/evaluate.py \
	    --x-test-data data/processed/X_test.csv \
	    --y-test-data data/processed/y_test.csv \
	    --plot-to results/figures

# Render the analysis document
analysis/customer-term-deposits-predictor.html: analysis/customer-term-deposits-predictor.qmd
	quarto render analysis/customer-term-deposits-predictor.qmd --to html

clean:
	rm -f data/raw/bank-full.csv \
		data/processed/preprocessed_data.csv \
		data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv \
		results/models/* \
		results/figures/* \
		results/tables/* \
        analysis/customer-term-deposits-predictor.html	
