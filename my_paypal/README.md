# Welcome to My Paypal
***

## Task
The goal of this project is to detect fraudulent credit card transactions using machine learning.
The main challenge lies in the extreme class imbalance of the dataset: fraudulent transactions represent 
less than 0.2% of all transactions. Traditional accuracy metrics are misleading in this context, 
making fraud detection both a technical and business-critical problem. The objective is to correctly identify 
fraudulent transactions while minimizing the number of legitimate transactions that are incorrectly blocked.

## Description
This project builds a fraud detection system using supervised machine learning.
The dataset contains anonymized credit card transactions with numerical features obtained through PCA, along 
with transaction time and amount. The solution follows these steps:
Data loading and validation
Exploratory data analysis to understand class imbalance and patterns
Handling imbalance using SMOTE (Synthetic Minority Oversampling Technique)
Training and evaluating multiple models
Selecting the best-performing model based on Area Under the Precision Recall Curve (AUPRC)
Preparing production-ready code and artifacts for deployment
The final model balances fraud detection performance and customer experience, focusing on recall and precision rather than raw accuracy.

## Installation
Install dependencies:
pip install -r requirements.txt

## Usage
Run the Jupyter notebook:

jupyter notebook my_paypal.ipynb

Execute all cells to:
Load and preprocess the dataset
Train the fraud detection model
Evaluate performance using Precision Recall metrics
Save the trained model for production use
The saved model can be used by the DevOps team for:
Batch fraud detection
Real-time transaction scoring
Integration into an API or transaction processing pipeline


```
./my_paypal Project
```

### The Core Team
Tamambang Nji Fru Duna

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
