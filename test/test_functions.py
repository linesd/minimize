import sys
sys.path.append("..")
import numpy as np
from optimizer.minimize import minimize
from functions.rosenbrock import rosenbrock
from optimizer.check_grad import check_grad
from functions.rosenbrock_with_args import rosenbrock_with_args

def test_minimize():
    # constant solutions
    SOL = np.array([[1.], [1.]])
    CON = 0.00
    I = 20

    # minimize rosenbrock
    length = 100
    X = np.array([0, 0]).reshape(-1,1)
    solution, convergence, i = minimize(rosenbrock, X, length, verbose=True, concise=True)

    # tests
    assert np.all(np.round(solution, 6) == SOL)
    assert np.round(convergence, 2) == CON
    assert i == I

def test_check_grad():
    np.random.seed(0)
    X = np.random.normal(0, 1, size=(3,1))
    vec1, d1 = check_grad(rosenbrock, X, 1e-5)
    vec2, d2 = check_grad(rosenbrock_with_args, X, 1e-5, args=(100, 400))

    assert np.all(np.round(vec1[:,0], 5) == np.round(vec1[:,1], 5))
    assert np.all(np.round(vec2[:,0], 5) == np.round(vec2[:,1], 5))