from Equation import Expression
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D


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

# print('Enter x')
# x = int(input())
# print('Enter y')
# y = int(input())
# print(fn(x, y))

l_bound = []
r_bound = []
for i in range(args_num):
    print('Enter left bound', i)
    l_bound.append(float(input()))
    print('Enter right bound', i)
    r_bound.append(float(input()))
 

print('Enter number of algorithm steps')
n = int(input())


if (args_num == 1):
    x = np.linspace(l_bound[0], r_bound[0], 1000)
    y = [func(i) for i in x]
    plt.plot(x, y)

    min_x = l_bound[0]
    min_y = func(l_bound[0])
    x_rand_list = [random.uniform(l_bound[0], r_bound[0]) for i in range(n)]
    x_rand_list = sorted(x_rand_list)
    y_rand_list = []
    for x_rand in x_rand_list:
        y_rand = func(x_rand)
        if (y_rand < min_y):
            min_y = y_rand
            min_x = x_rand
        y_rand_list.append(y_rand)

    print('min(f(x)) = ', min_y)
    print('argmin(f(x)) = ', min_x)

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

    min_x = l_bound[0]
    min_y = l_bound[1]
    min_z = func(min_x, min_y)
    x_rand_list = [random.uniform(l_bound[0], r_bound[0]) for i in range(n)]
    x_rand_list = sorted(x_rand_list)
    y_rand_list = [random.uniform(l_bound[1], r_bound[1]) for i in range(n)]
    y_rand_list = sorted(y_rand_list)
    z_rand_list = []
    for x_rand, y_rand in zip(x_rand_list, y_rand_list):
        z_rand = func(x_rand, y_rand)
        if (z_rand < min_z):
            min_z = z_rand
            min_x = x_rand
            min_y = y_rand
        z_rand_list.append(z_rand)

    print('min(f(x, y)) = ', min_z)
    print('argmin(f(x,y)) = (', min_x, min_y, ')')

    ax.plot(x_rand_list, y_rand_list, z_rand_list, marker='o', color='r', ls='')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
