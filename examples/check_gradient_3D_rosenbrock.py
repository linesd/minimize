import numpy as np
from optimizer.check_grad import check_grad
from functions.rosenbrock import rosenbrock
from functions.rosenbrock_with_args import rosenbrock_with_args

# set random seed
np.random.seed(0)

# random initialisation of X
X = np.random.normal(0, 1, size=(3, 1))

# check gradients for rosenbrock and rosenbrock with arguments
vec1, d1 = check_grad(rosenbrock, X, 1e-5)
vec2, d2 = check_grad(rosenbrock_with_args, X, 1e-5, args=(100, 400))

# check results are the same (first and second columns should match)
print("Derivatives vs finite difference for the rosenbrock function: ")
print(vec1)
print("Derivatives vs finite difference for the rosenbrock with arguments function: ")
print(vec1)