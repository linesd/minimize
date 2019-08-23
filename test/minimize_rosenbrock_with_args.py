from minimize import minimize
from test.rosenbrock_with_args import rosenbrock_with_args
import numpy as np

length = 1000
X = np.array([0,0,0]).reshape(-1,1)
x, con, i = minimize(rosenbrock_with_args, X, length, args=(100,400), reduction=None, verbose=True)

print("Minimum at [%f %f %f] after %i linesearches" % (x[0],x[1],x[2],i))