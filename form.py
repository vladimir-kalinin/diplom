import sys
import time

from PyQt5 import QtCore, QtGui

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from gui_form import Ui_MainWindow
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

        self.pushButton.clicked.connect(self.onButtonClick)

    @pyqtSlot()
    def onButtonClick(self):
        func_str = self.textEdit_func.toPlainText()
        args = ["x"]
        l_bound = [
            int('-' + e) for e in self.textEdit_borders.toPlainText().split(' ')]
        r_bound = [
            int(e) for e in self.textEdit_borders.toPlainText().split(' ')]
        step_num = int(self.textEdit_N.toPlainText())
        self.solver.set(func_str, args, l_bound, r_bound, step_num)
        self.fig = self.solver.plot()
        self.komponovka = QVBoxLayout(self.widget)
        self.canvas = MyMplCanvas(self.fig)
        self.komponovka.addWidget(self.canvas)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
    # sys.exit(app.exec_)


main()
