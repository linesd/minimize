from minimize import minimize
from rosenbrock import rosenbrock
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# minimize rosenbrock
length = 100
X = np.array([-1, 0]).reshape(-1,1)
x, convergence, i = minimize(rosenbrock, X, length)

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

# plot data
fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection='3d')

ax.view_init(elev=45., azim=45)
ax.plot(convergence[:,1], convergence[:,2], convergence[:,0], '-r*', markersize=12)
ax.scatter(1, 1, 0, s=100)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis',
                edgecolor='none', alpha=0.3, antialiased=False)
ax.set_xlabel('$X_{1}$', fontsize=20)
ax.set_ylabel('$X_{2}$', fontsize=20)
ax.set_zlabel('$f(\mathbf{X})$', fontsize=20)
plt.savefig('../img/convergence.png', dpi=200)

plt.show()
