from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D


class Solver:
    def __init__(self):
        self.delta = 0.001
        self.epsilon = 0.001
        self.step = 0.1

    def grad(self, x, foo):
        result = []
        for i in range(len(x)):
            x_l = x.copy()
            x_r = x.copy()
            x_l[i] = x_l[i] - self.delta
            x_r[i] = x_r[i] + self.delta
            result.append((foo(*x_r) - foo(*x_l)) / (2 * self.delta))
        print('result = ', result)
        return result

    def set(self, func_str, args, l_bound, r_bound, step_num):
        self.func_str = func_str
        self.args = args
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.step_num = step_num

        self.func = Expression(func_str, args)
        random.seed(73)

    def plot(self):
        print("func_str ", self.func_str)
        print("args ", self.args)
        print("l_bound ", self.l_bound)
        print("r_bound ", self.r_bound)
        print("step_num ", self.step_num)

        if (len(self.args) == 1):
            fig = plt.figure()
            x = np.linspace(self.l_bound[0], self.r_bound[0], 1000)
            y = [self.func(i) for i in x]

            ax = fig.add_subplot(111)
            ax.plot(x, y)

            x_rand_list = []
            y_rand_list = []
            x_rand_list.append(random.uniform(
                self.l_bound[0], self.r_bound[0]))
            y_rand_list.append(self.func(x_rand_list[0]))

            for i in range(self.step_num):
                grad_x = self.grad([x_rand_list[i]], self.func)[0]
                print('x = ', x_rand_list[i], 'grad = ', grad_x)
                curr_step = self.step
                new_x = x_rand_list[i] - grad_x * curr_step
                if (self.func(new_x) > y_rand_list[i]):
                    curr_step = curr_step / 2
                    new_x = x_rand_list[i] + grad_x * curr_step
                x_rand_list.append(new_x)
                y_rand_list.append(self.func(new_x))
                if ((y_rand_list[i] - y_rand_list[i + 1]) < self.epsilon):
                    break

            print('x = ', x_rand_list)
            print('y = ', y_rand_list)

            ax.plot(x_rand_list, y_rand_list, marker='o', color='r', ls='')
            # plt.show()

            # fig, axes = plt.subplots(nrows=1, ncols=1)
            return fig

        if (len(self.args) == 2):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            x = np.arange(self.l_bound[0], self.r_bound[0], 0.05)
            y = np.arange(self.l_bound[1], self.r_bound[1], 0.05)
            X, Y = np.meshgrid(x, y)
            zs = np.array([self.func(x, y)
                           for x, y in zip(np.ravel(X), np.ravel(Y))])
            Z = zs.reshape(X.shape)

            ax.plot_surface(X, Y, Z, alpha=0.5)
            ax.contour(X, Y, Z)
            # ax.plot_wireframe(X, Y, Z, alpha=0.5)

            x_rand_list = [random.uniform(self.l_bound[0], self.r_bound[0])]
            y_rand_list = [random.uniform(self.l_bound[1], self.r_bound[1])]
            z_rand_list = [self.func(x_rand_list[0], y_rand_list[0])]
            for i in range(self.step_num):
                grad_x = self.grad(
                    [x_rand_list[i], y_rand_list[i]], self.func)[0]
                grad_y = self.grad(
                    [x_rand_list[i], y_rand_list[i]], self.func)[1]

                curr_step = self.step
                new_x = x_rand_list[i] - grad_x * curr_step
                new_y = y_rand_list[i] - grad_y * curr_step
                if (self.func(new_x, new_y) > z_rand_list[i]):
                    curr_step = curr_step / 2
                    new_x = x_rand_list[i] - grad_x * curr_step
                    new_y = y_rand_list[i] - grad_y * curr_step
                if (new_x < self.l_bound[0] or new_x > self.r_bound[0]):
                    break
                if (new_y < self.l_bound[1] or new_y > self.r_bound[1]):
                    break
                x_rand_list.append(new_x)
                y_rand_list.append(new_y)
                z_rand_list.append(self.func(new_x, new_y))
                if ((z_rand_list[i] - z_rand_list[i + 1]) < self.epsilon):
                    break

            ax.plot(x_rand_list, y_rand_list, z_rand_list,
                    marker='o', color='r', ls='')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
            # plt.show()

            return fig
