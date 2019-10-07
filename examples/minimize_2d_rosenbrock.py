from optimizer.minimize import minimize
from functions.rosenbrock import rosenbrock
from utils.plots import plot_2d_function_convergence
import numpy as np

# minimize rosenbrock
length = 100
X = np.array([-1, 0]).reshape(-1,1)
solution, convergence, i = minimize(rosenbrock, X, length, verbose=True)
print("Minimum of %.2f at [%.2f %.2f] after %i linesearches" % (convergence[0,-1], solution[0], solution[1], i))

# Get rosenbrock data
X = np.arange(-1.1, 1.2, 0.05)
Y = np.arange(-0.5, 1.2, 0.05)
X, Y = np.meshgrid(X, Y)
XY = np.hstack((X.reshape(-1, 1), Y.reshape(-1, 1)))
N = XY.shape[0]; n,m = X.shape
Z = np.zeros((N,))
for i, xy in enumerate(XY):
    Z[i], _ = rosenbrock(xy)
Z = Z.reshape(n, m)

# plot function and convergence
path = "../doc/imgs/convergence.png"
plot_2d_function_convergence(X=X, Y=Y, Z=Z, convergence=convergence, path=path)
