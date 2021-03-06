from optimizer.minimize import minimize
from functions.rosenbrock import rosenbrock
import numpy as np

length = -1000
X = np.array([0,0,0]).reshape(-1,1)
x, con, i = minimize(rosenbrock, X, length, verbose=True)

print("Minimum at [%f %f %f] after %i function evaluations" % (x[0],x[1],x[2],i))
