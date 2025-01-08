# Stochastic gradient descent algorithm with python and numpy
# This is a basic implementation of the algorithm that starts with an arbitrary point, start, 
# iteratively moves it toward the minimum, and returns a point that is hopefully at or near the minimum

# %%
import numpy as np

def gradient_descent(gradient, start, learn_rate, n_iter = 50, tolerance=1e-6):
    vector = start
    for _ in range(n_iter):
        gradient_ = gradient(vector)
        diff = - learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        print(diff," - " ,vector, " - ", gradient_)
        vector += diff
    return vector

# %%
gd = gradient_descent(gradient=lambda v:2 * v, start=10, learn_rate=0.2)
print(gd)
# %%
