import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D


from gui import Ui_MainWindow
from solver_kushner import Solver as Solver_kushner
from solver_loman import Solver as Solver_loman
from solver_agp import Solver as Solver_agp


class MyMplCanvas(FigureCanvas):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.added = False
        self.pushButton.clicked.connect(self.onButtonClick)

        # defaults
        self.textEdit_func.setText('x**2')
        self.textEdit_n.setText('10')
        self.textEdit_eps.setText('0.1')
        self.textEdit_borders.setText('(-3,7)')
        self.comboBox.addItems(["kushner", "loman", "AGP"])

    @pyqtSlot()
    def onButtonClick(self):
        func_str = self.textEdit_func.toPlainText()
        # args = []
        # for i in range(50):  # expect that arg number will be less then 50
        #     if not (func_str.find('x' + str(i)) == -1):
        #         args.append('x' + str(i))
        borders = self.textEdit_borders.toPlainText().split(' ')
        print('borders = ', borders)
        l_bound = []
        r_bound = []
        for border in borders:
            tmp = border[1:-1].split(',')
            print('tmp = ', tmp)
            l_bound.append(int(tmp[0]))
            r_bound.append(int(tmp[1]))
        step_num = int(self.textEdit_n.toPlainText())
        epsilon = float(self.textEdit_eps.toPlainText())
        delta = float(self.textEdit_delta.toPlainText())
        r = float(self.textEdit_r.toPlainText())

        if self.comboBox.currentText() == "kushner":
            self.solver = Solver_kushner()
            self.solver.set(func_str, l_bound, r_bound, step_num, epsilon, delta)
        if self.comboBox.currentText() == "loman":
            self.solver = Solver_loman()
            self.solver.set(func_str, l_bound, r_bound, step_num, epsilon, r)
        if self.comboBox.currentText() == "AGP":
            self.solver = Solver_agp()
            self.solver.set(func_str, l_bound, r_bound, step_num, epsilon, r)

        if not self.added:
            self.fig = plt.figure()
            self.axes = self.fig.gca()
            self.canvas = MyMplCanvas(self.fig)
        else:
            self.axes.clear()
            self.fig.clear()
        if len(l_bound) == 1:
            ax = self.fig.add_subplot(111)
        else:
            ax = self.fig.add_subplot(111, projection='3d')

        # self.progressBar.setValue(0)
        self.solver.plot(ax, self.textBrowser, self.progressBar)
        self.progressBar.setValue(100)

        ax.grid()
        if not self.added:
            self.komponovka = QVBoxLayout(self.widget)
            self.komponovka.addWidget(self.canvas)
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.komponovka.addWidget(self.toolbar)
            self.added = True
        else:
            self.fig.canvas.draw()


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
    # sys.exit(app.exec_)


main()
