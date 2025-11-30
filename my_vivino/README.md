# Welcome to My Vivino
***

## Task
The goal of this project is to analyze and visualize wine sales data from multiple vendors and regions.
The main challenge was to clean the dataset, extract insights (like most sold wines, price trends, and sales per region), and then predict which wine is likely to sell best in the following year using a simple regression model.


## Description
The project loads raw wine data from a CSV file, cleans it, and performs several key operations:
Generates summary statistics for prices and years.
Visualizes top-selling wines, vendor performance, regional distributions, and price rankings.
Builds scatter plots to show relationships between regions, years, and sales.
Trains a simple Linear Regression model using scikit-learn to predict future best-selling wines based on past data.
Saves cleaned data and visualizations (.png files) for reporting and presentation.
The solution uses Pandas for data handling, Matplotlib for visualization, and Scikit-learn for prediction.


## Installation
Intstall the necessary libraries which are needed 

## Usage
Run the code on jupyter platform
Place your wine dataset (wineddrop.csv) in the project directory.
Run the main script to clean data, generate statistics, and create plots:
The script will:
Clean the dataset and save it as wineddrop_clean.csv
Generate visualizations such as:
top_10_wines.png
top20_products_per_vendor.png
wines_per_region.png
top10_seller_vs_region_scatter.png and more 

Train and test a regression model to predict future best-selling wines.
Predictions can be visualized in scatter plots and optionally exported as .csv or .png for reporting.

```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
