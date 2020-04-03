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
        MainWindow.resize(1224, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 0, 921, 711))
        self.widget.setObjectName("widget")
        self.textEdit_r = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_r.setGeometry(QtCore.QRect(30, 380, 231, 31))
        self.textEdit_r.setObjectName("textEdit_r")
        self.textEdit_n = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_n.setGeometry(QtCore.QRect(30, 340, 231, 31))
        self.textEdit_n.setObjectName("textEdit_n")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 21, 31))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 380, 31, 31))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 51, 31))
        self.label.setObjectName("label")
        self.textEdit_eps = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_eps.setGeometry(QtCore.QRect(60, 300, 201, 31))
        self.textEdit_eps.setObjectName("textEdit_eps")
        self.textEdit_borders = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_borders.setGeometry(QtCore.QRect(60, 170, 201, 31))
        self.textEdit_borders.setObjectName("textEdit_borders")
        self.textEdit_func = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_func.setGeometry(QtCore.QRect(100, 40, 181, 31))
        self.textEdit_func.setObjectName("textEdit_func")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 51, 31))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 260, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 530, 261, 81))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 630, 261, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 610, 261, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 51, 31))
        self.label_6.setObjectName("label_6")
        self.checkBox_from_text = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_from_text.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.checkBox_from_text.setObjectName("checkBox_from_text")
        self.checkBox_from_dll = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_from_dll.setGeometry(QtCore.QRect(10, 90, 181, 21))
        self.checkBox_from_dll.setObjectName("checkBox_from_dll")
        self.spinBox_func_number = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_func_number.setGeometry(QtCore.QRect(110, 120, 42, 22))
        self.spinBox_func_number.setObjectName("spinBox_func_number")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 81, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 21))
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
        self.textEdit_r.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "f(x1 ...  xn) ="))
        self.label_2.setText(_translate("MainWindow", "N ="))
        self.label_5.setText(_translate("MainWindow", "r ="))
        self.label.setText(_translate("MainWindow", "epsilon ="))
        self.label_4.setText(_translate("MainWindow", "Границы:"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label_6.setText(_translate("MainWindow", "Method:"))
        self.checkBox_from_text.setText(_translate("MainWindow", "Ввести вручную"))
        self.checkBox_from_dll.setText(_translate("MainWindow", "Выбрать из тестовых функций"))
        self.label_7.setText(_translate("MainWindow", "Функция номер"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

