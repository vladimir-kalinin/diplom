from Equation import Expression
import numpy as np
import random


# R()
def haract(x1, x2, z1, z2, m):
    return m*(x2 - x1) + (z2 - z1)**2/(m*(x2 - x1)) - 2*(z2 + z1)


# d()
def x_new(x1, x2, z1, z2, m):
    return 0.5*(x2 + x1) - (z2 - z1)/(2*m)


class Solver:
    def __init__(self):
        self.delta = 0.001
        self.epsilon = 0.001
        self.step = 0.1
        self.r = 2

    def set(self, func_str, l_bound, r_bound, step_num, epsilon, r):
        self.func_str = func_str
        self.args = []
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.step_num = step_num
        self.epsilon = epsilon
        self.r = r

        self.func = Expression(func_str, self.args)
        random.seed(73)

    def plot(self, ax):
        print("func_str ", self.func_str)
        print("args ", self.args)
        print("l_bound ", self.l_bound)
        print("r_bound ", self.r_bound)
        print("step_num ", self.step_num)

        if (len(self.args) == 1):
            X = [self.l_bound[0], self.r_bound[0]]
            Z = [self.func(self.l_bound[0]), self.func(self.r_bound[0])]
            z_min = min(Z)
            R = [1]
            r_max = R[0]
            i_max = 0

            m = 0

            for iteration in range(self.step_num):
                M = 0
                for i in range(len(X)-1):
                    if abs(Z[i+1] - Z[i])/(X[i+1] - X[i]) > M:
                        M = abs(Z[i+1] - Z[i])/(X[i+1] - X[i])
                if M > 0:
                    m = self.r*M
                else:
                    m = 1
                x = x_new(X[i_max], X[i_max + 1], Z[i_max], Z[i_max + 1], m)
                X.insert(i_max + 1, x)
                Z.insert(i_max + 1, self.func(X[i_max + 1]))
                if Z[i_max] < z_min:
                    z_min = Z[i_max]
                R.pop(i_max)
                R.insert(i_max, haract(X[i_max], X[i_max + 1], Z[i_max], Z[i_max + 1], m))
                R.insert(i_max + 1, haract(X[i_max + 1], X[i_max + 2], Z[i_max + 1], Z[i_max + 2], m))
                r_max = max(R)
                i_max = R.index(r_max)

                print('X =', X)
                print('Z =', Z)
                print('R =', R)

            # plot algorithm steps
            ax.plot(X, Z, marker='o', color='r', ls='')

            # plot test func
            x = np.linspace(self.l_bound[0], self.r_bound[0], 1000)
            y = [self.func(i) for i in x]
            ax.plot(x, y)
