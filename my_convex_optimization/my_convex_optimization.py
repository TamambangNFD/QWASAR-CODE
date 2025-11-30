import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# ------------------------------------------------------------
# 1. Plotting a function
# ------------------------------------------------------------
def print_a_function(function, x_values):
    """
    Plot the function over the given x-values.
    """
    y_values = [function(x) for x in x_values]
    plt.plot(x_values, y_values, label="f(x)")
    plt.grid()
    plt.legend()
    plt.show()


# ------------------------------------------------------------
# 2. Bisection Method (Root Finding)
# ------------------------------------------------------------
def find_root_bisection(function, interval_start, interval_end, precision=0.001):
    """
    Find a root of 'function' on [interval_start, interval_end] using bisection.
    """
    while (interval_end - interval_start) / 2 > precision:
        midpoint = (interval_start + interval_end) / 2
        f_mid = function(midpoint)

        if f_mid == 0:
            return midpoint

        if function(interval_start) * f_mid < 0:
            interval_end = midpoint
        else:
            interval_start = midpoint

    return (interval_start + interval_end) / 2


# ------------------------------------------------------------
# 3. Newton–Raphson Method (Root Finding)
# ------------------------------------------------------------
def find_root_newton_raphson(function, derivative, initial_guess=0, precision=0.001, max_iterations=1000):
    """
    Find a root using the Newton–Raphson method.
    """
    current_x = initial_guess

    for _ in range(max_iterations):
        slope = derivative(current_x)

        if slope == 0:
            raise ValueError("Derivative is zero → Newton method cannot continue.")

        correction_step = function(current_x) / slope
        new_x = current_x - correction_step

        if abs(correction_step) < precision:
            return new_x

        current_x = new_x

    raise ValueError("Newton–Raphson did not converge")

# ------------------------------------------------------------
# 4. Gradient Descent (Function Minimization)
# ------------------------------------------------------------
def gradient_descent(function, derivative, initial_x, learning_rate=0.1, precision=0.001, max_iterations=10000):
    """
    Minimize 'function' using gradient descent.
    """
    current_x = initial_x

    for _ in range(max_iterations):
        gradient_value = derivative(current_x)
        new_x = current_x - learning_rate * gradient_value

        if abs(derivative(new_x)) < precision:
            return new_x

        current_x = new_x

    raise ValueError("Gradient descent did not converge")


# ------------------------------------------------------------
# 5. Linear Programming (Simplex Method)
# ------------------------------------------------------------
def solve_linear_problem(constraint_matrix, constraint_bounds, objective_vector):
    """
    Solve the linear problem:
        minimize   objective_vector · x
        subject to constraint_matrix x <= constraint_bounds
    using SciPy's linprog.
    """
    result = linprog(objective_vector, A_ub=constraint_matrix, b_ub=constraint_bounds, method="highs")
    return result.fun, result.x
