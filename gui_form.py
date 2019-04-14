# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 460, 81, 81))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_func = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_func.setGeometry(QtCore.QRect(110, 460, 441, 31))
        self.textEdit_func.setObjectName("textEdit_func")
        self.textEdit_borders = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_borders.setGeometry(QtCore.QRect(110, 510, 441, 31))
        self.textEdit_borders.setObjectName("textEdit_borders")
        self.textEdit_eps = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_eps.setGeometry(QtCore.QRect(600, 460, 71, 31))
        self.textEdit_eps.setObjectName("textEdit_eps")
        self.textEdit_N = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_N.setGeometry(QtCore.QRect(600, 510, 71, 31))
        self.textEdit_N.setObjectName("textEdit_N")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 741, 411))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

