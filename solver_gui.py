import sys
import time

from PyQt5 import QtCore, QtGui

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from gui import Ui_MainWindow
from solver import Solver


class MyMplCanvas(FigureCanvas):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.solver = Solver()
        self.added = False

        self.pushButton.clicked.connect(self.onButtonClick)

    @pyqtSlot()
    def onButtonClick(self):
        func_str = self.textEdit_func.toPlainText()
        args = []
        for i in range(50):  # expect that arg number will be less then 50
            if not (func_str.find('x' + str(i)) == -1):
                args.append('x' + str(i))
        borders = self.textEdit_borders.toPlainText().split(' ')
        print('borders = ', borders)
        l_bound = []
        r_bound = []
        for border in borders:
            tmp = border[1:-1].split(',')
            print('tmp = ', tmp)
            l_bound.append(int(tmp[0]))
            r_bound.append(int(tmp[1]))

        # l_bound = [int('-' + e) for e in self.textEdit_borders.toPlainText().split(' ')]
        # r_bound = [int(e) for e in self.textEdit_borders.toPlainText().split(' ')]
        step_num = int(self.textEdit_n.toPlainText())
        epsilon = float(self.textEdit_eps.toPlainText())
        self.solver.set(func_str, args, l_bound, r_bound, step_num, epsilon)
        self.fig = self.solver.plot()
        self.canvas = MyMplCanvas(self.fig)
        if not self.added:
            self.komponovka = QVBoxLayout(self.widget)
            self.komponovka.addWidget(self.canvas)
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.komponovka.addWidget(self.toolbar)
            self.added = True
        else:
            self.fig.canvas.draw()
            # self.komponovka.update()
            # self.komponovka.widget() = QWidget(self.canvas)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
    # sys.exit(app.exec_)


main()
