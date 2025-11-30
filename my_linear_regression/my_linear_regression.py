import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def h(x, theta):
    result = np.dot(x, theta)
    return result.reshape(-1, 1)

def mean_squared_error(y_pred, y_label):
    n = len(y_label)
    error = 0
    for y_hat, y in zip(y_pred, y_label):
        error += (y_hat - y) ** 2
    return (1 / n) * error

# ------------------------------------------------------------
# Bias column function
# ------------------------------------------------------------
def bias_column(X):
    X = np.array(X)
    return np.hstack([np.ones((X.shape[0], 1)), X])

# ------------------------------------------------------------
# Least Squares using Normal Equation
# ------------------------------------------------------------
class LeastSquaresRegression:
    def __init__(self):
        self.theta_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        # Normal Equation: θ = (XᵀX)⁻¹ Xᵀy
        self.theta_ = np.linalg.inv(X.T @ X) @ (X.T @ y)

    def predict(self, X):
        return X @ self.theta_

# ------------------------------------------------------------
# Generate data
# ------------------------------------------------------------
X = 4 * np.random.rand(100, 1)
y = 10 + 2 * X + np.random.randn(100, 1)

plt.scatter(X, y)
plt.title("Generated Data")
plt.show()

# ------------------------------------------------------------
# Prepare data (add bias)
# ------------------------------------------------------------
X_new = bias_column(X)

# ------------------------------------------------------------
# Fit model
# ------------------------------------------------------------
model = LeastSquaresRegression()
model.fit(X_new, y)

print("Theta (b, a):")
print(model.theta_)

# ------------------------------------------------------------
# Predictions + plot
# ------------------------------------------------------------
y_pred = model.predict(X_new)

def my_plot(X, y, y_pred):
    plt.scatter(X, y, label="Original Data")
    plt.plot(X, y_pred, color="red", label="Model Prediction")
    plt.legend()
    plt.title("Least Squares Regression")
    plt.show()

my_plot(X, y, y_pred)

# ------------------------------------------------------------
# Gradient Descent Optimizer
# ------------------------------------------------------------
class GradientDescentOptimizer:
    def __init__(self, f, fprime, start, learning_rate=0.1):
        self.f_ = f
        self.fprime_ = fprime
        self.current_ = np.array(start, dtype=float).ravel()
        self.learning_rate_ = learning_rate
        self.history_ = [self.current_.copy()]

    def step(self):
        # Gandalf's f_prime expects column vectors
        x_in = self.current_.reshape(-1, 1)

        # Compute gradient
        grad = np.asarray(self.fprime_(x_in), dtype=float).ravel()

        # Keep only needed components
        grad = grad[:len(self.current_)]

        # Gradient descent step
        self.current_ = self.current_ - self.learning_rate_ * grad

        self.history_.append(self.current_.copy())


    # def step(self):
    #     grad = np.asarray(self.fprime_(self.current_), dtype=float).ravel()

    #     if len(grad) > len(self.current_):
    #         grad = grad[:len(self.current_)]
    #     elif len(grad) < len(self.current_):
    #         grad = np.pad(grad, (0, len(self.current_) - len(grad)))

    #     self.current_ = self.current_ - self.learning_rate_ * grad
    #     self.history_.append(self.current_.copy())

    def optimize(self, iterations=100):
        for _ in range(iterations):
            self.step()

    def getCurrentValue(self):
        return self.current_

    def print_result(self):
        print("Best theta found:", self.current_)
        print("f(theta) =", self.f_(self.current_))
        print("f'(theta) =", self.fprime_(self.current_))
# ------------------------------------------------------------
# Define f and f'
# ------------------------------------------------------------
def f(x):
    x = np.asarray(x, dtype=float).ravel()
    c = np.array([2, 6], dtype=float)
    diff = x - c
    return 3 + diff @ diff

def fprime(x):
    x = np.asarray(x, dtype=float).ravel()
    c = np.array([2, 6], dtype=float)
    return 2 * (x - c)

# ------------------------------------------------------------
# Run gradient descent
# ------------------------------------------------------------
start = np.random.normal(size=(2,))
gd = GradientDescentOptimizer(f, fprime, start, learning_rate=0.2)
gd.optimize(20)
gd.print_result()

# ------------------------------------------------------------
# Plot 3D function + gradient path
# ------------------------------------------------------------
x_vals = np.linspace(-2, 6, 100)
y_vals = np.linspace(0, 12, 100)
Xg, Yg = np.meshgrid(x_vals, y_vals)
Zg = 3 + (Xg - 2)**2 + (Yg - 6)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Xg, Yg, Zg, cmap="viridis", alpha=0.6)

# gradient path
hist = np.array(gd.history_)
Z_hist = [f(p) for p in hist]
ax.plot(hist[:,0], hist[:,1], Z_hist, color="red", linewidth=3)

ax.set_title("Gradient Descent Path")
plt.show()
