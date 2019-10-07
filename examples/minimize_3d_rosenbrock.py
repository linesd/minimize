from optimizer.minimize import minimize
from functions.rosenbrock import rosenbrock
import numpy as np

length = 1000
X = np.array([0,0,0]).reshape(-1,1)
solution, con, i = minimize(rosenbrock, X, length, verbose=True, concise=True)
print("Minimum of %.2f at [%.2f %.2f %.2f] after %i linesearches" % (con, solution[0], solution[1], solution[2], i))
