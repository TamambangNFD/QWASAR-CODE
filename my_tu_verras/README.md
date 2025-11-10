# Welcome to My Tu Verras
***

## Task
The task is to analyze the **Boston Housing dataset** and build a **linear regression model**.  
The challenge lies in:
- Cleaning and preparing the dataset (handling missing values, renaming columns).  
- Exploring correlations between features and the target variable (e.g., number of rooms vs. median house value).  
- Visualizing relationships between attributes (histograms, scatter matrices).  
- Building a regression model to predict housing prices. 

## Description
I solved the problem by:
- Loading & Cleaning Data: Handled missing values using median imputation for multiple columns.  
- Exploratory Data Analysis (EDA): Printed dataset summary, created histograms, correlation matrices, and scatter plots to visualize relationships.  
- Correlation Analysis: Computed Pearson correlation matrix to identify the most influential features.  
- Modeling: Used `scikit-learn`’s `LinearRegression` to train a model with `RM` (average number of rooms) as a predictor for `MEDV` (median value of homes).  
- Prediction: Implemented a function to make predictions using the trained model.  

## Installation
Download the csv file that was given into the main workig directory on jupyter 
The project requires the following; pandas, numpy, matplotlib, seaborn, scikit-learn
Ensure the dataset file (boston.csv) is placed in the project folder.

## Usage
Prints dataset summary, histograms, correlations, and scatter plots. to Train a linear regression model., and for Expected Results, You will see that RM (average number of rooms) has the strongest positive correlation with housing prices (MEDV). 
Predictions give an estimated house price based on input features.
```
./my_tu_verras project
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
