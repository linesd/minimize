from minimize import minimize
from rosenbrock import rosenbrock
import numpy as np
import matplotlib.pyplot as plt

# minimize rosenbrock
length = 1000
for j in range(2, 25):
    for k in range(10):
        min = np.ones((j, 1))
        X = np.random.normal(loc=0.0, scale=5.0, size=(j,1)) # random intialisation
        x, con, i = minimize(rosenbrock, X, length, verbose=False)

        if np.all(np.round(x, 7) == min):
            print("SUCCESS for %i-D trial number %i after %i linesearches" % (j,k,i))
        else:
            print("FAILED to find min for %i-D trial number %i after %i linesearches" % (j,k,i))
            print("x: ", x.T)
            y = np.arange(con.shape[0])
            plt.figure(1)
            plt.plot(y, con[:,0])

plt.yscale('log')
plt.show()