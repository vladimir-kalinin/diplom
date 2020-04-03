import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from Equation import Expression
from ctypes import *
from gui import Ui_MainWindow
from solver_har import Solver


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
        self.checkBox_from_text.stateChanged.connect(self.on_from_text)
        self.checkBox_from_dll.stateChanged.connect(self.on_from_dll)
        self.args = []

        # defaults
        self.textEdit_func.setText('x**2 + y**2')
        self.textEdit_n.setText('10')
        self.textEdit_eps.setText('0.1')
        self.textEdit_borders.setText('(0,1) (0,1)')
        self.comboBox.addItems(["perebor", "loman", "AGP"])
        self.checkBox_from_text.setCheckState(QtCore.Qt.Checked)
    
    def on_from_text(self, state):
        if state == QtCore.Qt.Checked:
            self.checkBox_from_dll.setCheckState(QtCore.Qt.Unchecked)

    def on_from_dll(self, state):
        if state == QtCore.Qt.Checked:
            self.checkBox_from_text.setCheckState(QtCore.Qt.Unchecked)

    @pyqtSlot()
    def onButtonClick(self):
        if (self.checkBox_from_text.isChecked()):
            func_str = self.textEdit_func.toPlainText()
            self.func = Expression(func_str, self.args)
        else:
            lib = cdll.LoadLibrary('random_func.dll')
            lib.random_func.argtypes = [c_double, c_double]
            lib.random_func.restype = c_double
            lib.getcoord.argtype = c_int
            lib.getcoord.restype = c_double
            lib.set_random(self.spinBox_func_number.value() + 1)
            self.func = lib.random_func
            self.args = ['x', 'y']

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
        # delta = float(self.textEdit_delta.toPlainText())
        r = float(self.textEdit_r.toPlainText())

        self.solver = Solver()
        self.solver.set(self.func, self.args, l_bound, r_bound, step_num, epsilon, r,
                        self.comboBox.currentText(), self.textBrowser, self.progressBar)

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
        self.solver.plot(ax)
        self.progressBar.setValue(100)
        if self.checkBox_from_dll.isChecked():
            answer = str(lib.getcoord(self.spinBox_func_number.value()*2))
            answer += ', '
            answer += str(lib.getcoord(self.spinBox_func_number.value()*2 + 1))
            self.textBrowser.append('answer = ' + answer)

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
