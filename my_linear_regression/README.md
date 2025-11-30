# Welcome to My Linear Regression
***

## Task
Implement a compact, educational linear regression example in Python that demonstrates both the closed-form ordinary least squares (Normal Equation) solution and an iterative optimization approach (gradient descent) for simple parameter estimation. The challenge is to keep the code small and readable while providing clear visualizations of the data, fitted line, and an optimization path.

## Description
This repository contains a single script, `my_linear_regression.py`, which:
- generates synthetic linear data with noise;
- fits a linear model using the Normal Equation (closed-form least squares);
- includes a small gradient descent optimizer and demonstrates its path on a 2D quadratic surface (toy example);
- produces plots showing the generated data, the least-squares fit, and the gradient descent path on a 3D surface.

The implementation is intended for learning and experimentation rather than production use. The code is deliberately explicit and easy to modify to try different learning rates, starting points, or data noise levels.

## Installation
This project requires Python 3.8 or newer and the following Python packages:

```
pip install numpy matplotlib
```

Optionally create and activate a virtual environment before installing:

Windows (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy matplotlib
```

## Usage
Run the script from the project directory:

```
python my_linear_regression.py
```

When you run it, you will see three visual outputs:
- a scatter plot of the generated data;
- the fitted least-squares regression line plotted over the data;
- a 3D surface illustrating a simple quadratic objective and the gradient descent path.

You can edit `my_linear_regression.py` to change dataset size, noise level, learning rate, or the number of gradient descent iterations for experiments.

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
