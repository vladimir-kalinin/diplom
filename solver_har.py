import numpy as np


def haract_perebor(x1, x2, z1, z2, m):
    return x2 - x1


def x_new_perebor(x1, x2, z1, z2, m):
    return (x1 + x2)/2

def haract_loman(x1, x2, z1, z2, m):
    return 0.5*m*(x2 - x1) - (z2 + z1)/2


def x_new_loman(x1, x2, z1, z2, m):
    return 0.5*(x2 + x1) - (z2 - z1)/(2*m)


def haract_agp(x1, x2, z1, z2, m):
    return m*(x2 - x1) + (z2 - z1)**2/(m*(x2 - x1)) - 2*(z2 + z1)


def x_new_agp(x1, x2, z1, z2, m):
    return 0.5*(x2 + x1) - (z2 - z1)/(2*m)


class Solver:
    def set(self, func, args, l_bound, r_bound, step_num, epsilon, r, method, textBrowser, progressBar):
        # print('func = ', func)
        # print('l_bound = ', l_bound)
        # print('r_bound = ', r_bound)
        # print('args = ', args)
        self.args = args
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.step_num = step_num
        self.epsilon = epsilon
        self.r = r
        self.func = func
        self.dimensions = len(self.args)
        self.textBrowser = textBrowser
        self.progressBar = progressBar
        if method == "perebor":
            self.haract = haract_perebor
            self.x_new = x_new_perebor
        if method == "loman":
            self.haract = haract_loman
            self.x_new = x_new_loman
        if method == "AGP":
            self.haract = haract_agp
            self.x_new = x_new_agp
        self.answer = []

    def solve(self, l_bound, r_bound, fixed_args):
        # print('solve(', fixed_args, ')')
        X = [l_bound[0], r_bound[0]]
        internal_results = []
        Z =[]
        X_min = []
        if len(fixed_args) == self.dimensions - 1:
            Z = [self.func(*fixed_args, l_bound[0]), self.func(*fixed_args, r_bound[0])]
        else:
            min_z, min_x, prev_results = self.solve(l_bound[1:], r_bound[1:], fixed_args + [l_bound[0]])
            Z.append(min_z)
            X_min.append(min_x)
            internal_results.append(prev_results)
            min_z, min_x, prev_results = self.solve(l_bound[1:], r_bound[1:], fixed_args + [r_bound[0]])
            Z.append(min_z)
            X_min.append(min_x)
            internal_results.append(prev_results)
        z_min = min(Z)
        R = [1]
        r_max = R[0]
        i_max = 0 # index of interval with max R
        m = 0

        for iteration in range(self.step_num):
            if len(fixed_args) == 0:
                self.progressBar.setValue(int(iteration*100/self.step_num))

            # calculate m
            M = 0
            for i in range(len(X)-1):
                if abs(Z[i+1] - Z[i])/(X[i+1] - X[i]) > M:
                    M = abs(Z[i+1] - Z[i])/(X[i+1] - X[i])
            if M > 0:
                m = self.r*M
            else:
                m = 1

            # calculate R
            r_max = 0
            i_max = 0
            R.clear()
            for i in range(len(X)-1):
                R.append(self.haract(X[i], X[i + 1], Z[i], Z[i + 1], m))
                if R[i] > r_max:
                    r_max = R[i]
                    i_max = i

            # epsilon check
            if (X[i_max + 1] - X[i_max]) < self.epsilon:
                break

            # calculate new x, z
            x = self.x_new(X[i_max], X[i_max + 1], Z[i_max], Z[i_max + 1], m)
            X.insert(i_max + 1, x)
            if len(fixed_args) == self.dimensions - 1:
                Z.insert(i_max + 1, self.func(*fixed_args, X[i_max + 1]))
                # X_min.insert(i_max + 1, [x])
            else:
                min_z, min_x, prev_results = self.solve(l_bound[1:], r_bound[1:], fixed_args + [X[i_max + 1]])
                Z.insert(i_max + 1, min_z)
                X_min.insert(i_max + 1, min_x)
                internal_results.insert(i_max + 1, prev_results)
            if Z[i_max + 1] < z_min:
                z_min = Z[i_max + 1]

        i_min = Z.index(z_min)
        if (len(X_min) > 0):
            tmp = X_min[i_min]
        else:
            tmp = []
        tmp.append(X[i_min])
        return Z[i_min], tmp, [X, Z, internal_results]


    def plot(self, ax):
        if self.dimensions == 1:
            z_min, x_min, result = self.solve(self.l_bound, self.r_bound, [])
            X = result[0]
            Z = result[1]
            output = 'z_min = ' + str(z_min) + '\n'
            x_min.reverse()
            output += 'x_min = ' + str(x_min) + '\n'
            self.textBrowser.setText(output)

            # plot algorithm steps
            ax.plot(X, Z, marker='.', color='r', ls='')

            # plot test func
            x = np.linspace(self.l_bound[0], self.r_bound[0], 1000)
            y = [self.func(i) for i in x]
            ax.plot(x, y)
        if self.dimensions == 2:
            z_min, x_min, result = self.solve(self.l_bound, self.r_bound, [])
            output = 'z_min = ' + str(z_min) + '\n'
            x_min.reverse()
            output += 'x_min = ' + str(x_min) + '\n'
            if len(self.answer):
                accuracy = np.sqrt((self.answer[0] - x_min[0])**2 + (self.answer[1] - x_min[1])**2)
                output += 'accuracy = ' + str(accuracy) + '\n'
            self.textBrowser.setText(output)

            x_list = []
            y_list = []
            z_list = []
            for x, args in zip(result[0], result[2]):
                for y, z in zip(args[0], args[1]):
                    x_list.append(x)
                    y_list.append(y)
                    z_list.append(z)
            # plot algorithm steps
            ax.plot(x_list, y_list, marker='.', color='r', ls='')

            # plot test func
            x = np.linspace(self.l_bound[0], self.r_bound[0], 30)
            y = np.linspace(self.l_bound[1], self.r_bound[1], 30)
            X, Y = np.meshgrid(x, y)
            zs = np.array([self.func(x, y)
                        for x, y in zip(np.ravel(X), np.ravel(Y))])
            Z = zs.reshape(X.shape)

            ax.plot_surface(X, Y, Z, alpha=0.5)
            ax.contour(X, Y, Z, zdir='z', offset=0)
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        if self.dimensions > 2:
            z_min, x_min, result = self.solve(self.l_bound, self.r_bound, [])
            output = 'z_min = ' + str(z_min) + '\n'
            x_min.reverse()
            output += 'x_min = ' + str(x_min) + '\n'
            self.textBrowser.setText(output)
            x_list = []
            y_list = []
            z_list = []
            for x, args in zip(result[0], result[2]):
                for y, args2 in zip(args[0], args[2]):
                    for z in args2[0]:
                        x_list.append(x)
                        y_list.append(y)
                        z_list.append(z)
            # plot algorithm steps
            ax.plot(x_list, y_list, z_list, marker='.', color='r', ls='')
