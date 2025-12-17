# Welcome to Drive Me Crazy
***

## Task
Accurately predicting short-term traffic flow / trip durations in urban networks using heterogeneous data sources
 (PeMS04, PeMS07, PeMS08, NYC Taxi). 
 The core challenges are: heterogeneity across datasets, missing/noisy sensor data, 
 temporal and spatial dependencies across long horizons, and the effect of propagation delays 
 (how congestion or events spread across the network).


## Description
This project implements and evaluates two classes of approaches:

1. Traditional models (baselines) Linear Regression and Random Forest trained on engineered features (distance, hour, weekday, month, is_weekend, passenger_count), plus propagation-derived features (avg/max delay, propagation_delay_ratio). These are robust, interpretable, and computationally efficient.

2. Propagation Delay-Aware Dynamic Long-Range Transformer (PDFormer) A Transformer-based architecture that:
   Embeds discrete propagation delays and adds them to token representations.
   Uses Transformer encoder layers with causal masking to capture long-range temporal dependencies.
   Trained with sliding window sequences (e.g., 24 timesteps) and evaluated with MAE and RMSE.

Methodology highlights
Data integration from PeMS and NYC Taxi sources.
Feature engineering: Haversine distance, temporal features, graph-derived centrality/degree.
Shortest-path computations for propagation delay estimation (sampled for performance).
Uniform training/evaluation protocol for fair comparison.
Looker Studio dashboard for interactive visualization of predictions and metrics.

## Installation
pip install -r requirements.txt to run all dependencies
Install PyTorch according to your environment (CPU/GPU) from https://pytorch.org.
- For large graph computations, consider running on a machine with sufficient RAM.

## Usage
Place the raw datasets in the root directory
data/
  PEMS04.csv
  PEMS07.csv
  PEMS08.csv
  NYC_taxi.csv


Run the analysis and baselines
Open the Jupyter notebook `drive_me_crazy_tradi.ipynb` and run all cells:
- It executes `dataset_analysis.ipynb` to load and preprocess datasets.
- Produces baseline training, evaluation (MAE, RMSE), and feature importance.
- Saves `cleaned_dataset.csv', predictions & metrics to the same folder as your `train.csv` files.

jupyter notebook  then open the notebook UI and run all notebooks

```
./Drive_Me_Crazy Project
```

### The Core Team
Tamambang NJ FRU DUNA

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
