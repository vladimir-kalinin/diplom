from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D


def func(x):
    return x**2


def haract(x1, x2):
    return x2 - x1


def x_new(x1, x2):
    return (x1 + x2)/2


a = 0.
b = 1.
N = 10

x = [a, b]
y = [func(a), func(b)]
R = [haract(a, b)]
r_max = R[0]
i_max = 0

for iteration in range(N):
    x.insert(i_max + 1, x_new(x[i_max], x[i_max + 1]))
    R.pop(i_max)
    R.insert(i_max, haract(x[i_max], x[i_max+1]))
    R.insert(i_max + 1, haract(x[i_max+1], x[i_max+2]))
    r_max = 0
    i_max = 0
    for i in range(len(R)):
        if R[i] > r_max:
            r_max = R[i]
            i_max = i
    print('x =', x)
    print('R =', R)
