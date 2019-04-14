from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D


delta = 0.001
epsilon = 0.001
step = 0.1


def grad(x, foo):
    result = []
    for i in range(len(x)):
        x_l = x.copy()
        x_r = x.copy()
        x_l[i] = x_l[i] - delta
        x_r[i] = x_r[i] + delta
        result.append((foo(*x_r) - foo(*x_l)) / (2 * delta))
    print('result = ', result)
    return result


print('Enter function')
func_str = input()
print('Enter number of args')
args_num = int(input())
args = []
for i in range(args_num):
    print('Enter argument #', i)
    args.append(input())

func = Expression(func_str, args)
print(func)

l_bound = []
r_bound = []
for i in range(args_num):
    print('Enter left bound', i)
    l_bound.append(float(input()))
    print('Enter right bound', i)
    r_bound.append(float(input()))


print('Enter number of algorithm steps')
step_num = int(input())

# SEED
random.seed(72)


if (args_num == 1):
    x = np.linspace(l_bound[0], r_bound[0], 1000)
    y = [func(i) for i in x]
    plt.plot(x, y)

    x_rand_list = []
    y_rand_list = []
    x_rand_list.append(random.uniform(l_bound[0], r_bound[0]))
    y_rand_list.append(func(x_rand_list[0]))

    for i in range(step_num):
        grad_x = grad([x_rand_list[i]], func)[0]
        print('x = ', x_rand_list[i], 'grad = ', grad_x)
        curr_step = step
        new_x = x_rand_list[i] - grad_x * curr_step
        if (func(new_x) > y_rand_list[i]):
            curr_step = curr_step / 2
            new_x = x_rand_list[i] + grad_x * curr_step
        x_rand_list.append(new_x)
        y_rand_list.append(func(new_x))
        if ((y_rand_list[i] - y_rand_list[i + 1]) < epsilon):
            break

    print('min(f(x)) = ')
    print('argmin(f(x)) = ')

    plt.plot(x_rand_list, y_rand_list, marker='o', color='r', ls='')

    plt.show()

if (args_num == 2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(l_bound[0], r_bound[0], 0.05)
    y = np.arange(l_bound[1], r_bound[1], 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array([func(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z, alpha=0.5)
    ax.contour(X, Y, Z)
    # ax.plot_wireframe(X, Y, Z, alpha=0.5)

    x_rand_list = [random.uniform(l_bound[0], r_bound[0])]
    y_rand_list = [random.uniform(l_bound[1], r_bound[1])]
    z_rand_list = [func(x_rand_list[0], y_rand_list[0])]
    for i in range(step_num):
        grad_x = grad([x_rand_list[i], y_rand_list[i]], func)[0]
        grad_y = grad([x_rand_list[i], y_rand_list[i]], func)[1]

        curr_step = step
        new_x = x_rand_list[i] - grad_x * curr_step
        new_y = y_rand_list[i] - grad_y * curr_step
        if (func(new_x, new_y) > z_rand_list[i]):
            curr_step = curr_step / 2
            new_x = x_rand_list[i] - grad_x * curr_step
            new_y = y_rand_list[i] - grad_y * curr_step
        if (new_x < l_bound[0] or new_x > r_bound[0]):
            break
        if (new_y < l_bound[1] or new_y > r_bound[1]):
            break
        x_rand_list.append(new_x)
        y_rand_list.append(new_y)
        z_rand_list.append(func(new_x, new_y))
        if ((z_rand_list[i] - z_rand_list[i + 1]) < epsilon):
            break

    ax.plot(x_rand_list, y_rand_list, z_rand_list,
            marker='o', color='r', ls='')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
