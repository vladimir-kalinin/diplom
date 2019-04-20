# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_func = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_func.setGeometry(QtCore.QRect(100, 630, 501, 31))
        self.textEdit_func.setObjectName("textEdit_func")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 670, 261, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 901, 621))
        self.widget.setObjectName("widget")
        self.textEdit_n = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_n.setGeometry(QtCore.QRect(800, 630, 41, 31))
        self.textEdit_n.setObjectName("textEdit_n")
        self.textEdit_eps = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_eps.setGeometry(QtCore.QRect(710, 630, 41, 31))
        self.textEdit_eps.setObjectName("textEdit_eps")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 630, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(780, 630, 21, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 630, 71, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_borders = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_borders.setGeometry(QtCore.QRect(100, 670, 501, 31))
        self.textEdit_borders.setObjectName("textEdit_borders")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 670, 51, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "epsilon ="))
        self.label_2.setText(_translate("MainWindow", "N ="))
        self.label_3.setText(_translate("MainWindow", "f(x1 ...  xn) ="))
        self.label_4.setText(_translate("MainWindow", "borders:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

