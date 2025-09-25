# fraud-detection-risk-analysis
Fraud detection &amp; risk governance project using Python, SQL, and data analysis
# Fraud Detection Risk Analysis
A credit card fraud detection project using machine learning in Python. Includes data preprocessing, model training, evaluation, and visualization of results.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Project Overview

This project detects fraudulent credit card transactions using machine learning.  
It demonstrates skills in data preprocessing, feature analysis, model building, evaluation, and visualization.  

*Key skills:* Python, pandas, scikit-learn, matplotlib/seaborn, data analysis.

## Dataset

The project uses the Kaggle Credit Card Fraud Detection dataset:  
[https://www.kaggle.com/mlg-ulb/creditcardfraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)  

*Note:* The dataset is *not included* in this repository due to size.  
Place creditcard.csv inside the data/ folder to run the project.

## Project Structure

fraud-detection-risk-analysis/ ├─ src/               # Python scripts for preprocessing, model training, evaluation ├─ notebooks/         # Jupyter notebooks for EDA and visualization ├─ results/           # fraud_analysis_summary.md and plots ├─ data/              # Dataset folder (ignored in GitHub) ├─ README.md          # Project overview and instructions ├─ requirements.txt   # Python dependencies └─ LICENSE            # MIT License

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Swazk/fraud-detection-risk-analysis.git
cd fraud-detection-risk-analysis

2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

Usage

Run the main script to train the model and generate results:

python src/run_model.py

Results will be saved in the results/ folder:

fraud_analysis_summary.md → summary of model performance

Plots → confusion matrix, ROC curve, feature importance
Usage

Run the main script to train the model and generate results:

python src/run_model.py

Results will be saved in the results/ folder:

fraud_analysis_summary.md → summary of model performance

Plots → confusion matrix, ROC curve, feature importance

Results

Model Accuracy: 99.9%

Precision, Recall, F1-score for fraud detection

Visualizations: confusion matrix, ROC curve, feature importance

License

This project is licensed under the MIT License - see the LICENSE file for details
