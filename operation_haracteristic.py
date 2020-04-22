from solver_har import Solver
from ctypes import *
import numpy as np
import matplotlib.pyplot as plt

r = 2
epsilon_begin = 0.005
epsilon_end = 0.1
epsilon_number = 20
delta = 0.02

lib = cdll.LoadLibrary('random_func.dll')
lib.random_func.argtypes = [c_double, c_double]
lib.random_func.restype = c_double
lib.getcoord.argtype = c_int
lib.getcoord.restype = c_double
args = ['x', 'y']
l_bound = [0, 0]
r_bound = [1, 1]


step_num = 1000000000
solver = Solver()
P = []
K = []
for epsilon in np.geomspace(epsilon_begin, epsilon_end, epsilon_number):
    solved_count = 0
    total_steps = 0
    for i in range(1, 101):
        lib.set_random(i)
        func = lib.random_func

        solver.set(func, args, l_bound, r_bound, step_num, epsilon, r, "loman", None, None)
        x_accurate = lib.getcoord((i-1)*2)
        y_accurate = lib.getcoord((i-1)*2 + 1)

        z_min, x_min, result = solver.solve(l_bound, r_bound, [])
        x_min.reverse()
        accuracy = np.sqrt((x_accurate - x_min[0])**2 + (y_accurate - x_min[1])**2)

        # print('epsilon = ', epsilon)
        # print('z_min = ', z_min)
        # print('x_min = ', x_min)
        # print('steps = ', solver.step_num_total - solver.step_num)
        # print('accuracy = ', accuracy, '\n\n')

        if accuracy < delta:
            solved_count += 1
        total_steps += solver.step_num_total - solver.step_num
    
    p = solved_count/100
    k = total_steps/100
    print('epsilon = ', epsilon)
    print('p = ', p)
    print('k = ', k)
    P.append(p)
    K.append(k)

# plt.semilogy(K, P, 'bo')
plt.plot(K, P, 'bo')
plt.xlabel('K')
plt.ylabel('P')
plt.show()
