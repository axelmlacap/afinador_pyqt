# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'afinador.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 470)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.diff_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.diff_bar.setGeometry(QtCore.QRect(40, 190, 341, 81))
        self.diff_bar.setProperty("value", 24)
        self.diff_bar.setObjectName("diff_bar")
        self.ref_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ref_input.setGeometry(QtCore.QRect(110, 330, 201, 22))
        self.ref_input.setStyleSheet("color: gray")
        self.ref_input.setObjectName("ref_input")
        self.ref_label = QtWidgets.QLabel(self.centralwidget)
        self.ref_label.setGeometry(QtCore.QRect(20, 330, 81, 16))
        self.ref_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.ref_label.setObjectName("ref_label")
        self.ref_units = QtWidgets.QLabel(self.centralwidget)
        self.ref_units.setGeometry(QtCore.QRect(320, 330, 41, 16))
        self.ref_units.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ref_units.setObjectName("ref_units")
        self.tol_input = QtWidgets.QLineEdit(self.centralwidget)
        self.tol_input.setGeometry(QtCore.QRect(110, 360, 201, 22))
        self.tol_input.setObjectName("tol_input")
        self.tol_units = QtWidgets.QLabel(self.centralwidget)
        self.tol_units.setGeometry(QtCore.QRect(320, 360, 41, 16))
        self.tol_units.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.tol_units.setObjectName("tol_units")
        self.tol_label = QtWidgets.QLabel(self.centralwidget)
        self.tol_label.setGeometry(QtCore.QRect(20, 360, 81, 16))
        self.tol_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.tol_label.setObjectName("tol_label")
        self.upd_button = QtWidgets.QPushButton(self.centralwidget)
        self.upd_button.setGeometry(QtCore.QRect(160, 402, 81, 31))
        self.upd_button.setObjectName("upd_button")
        self.tuned_label = QtWidgets.QLabel(self.centralwidget)
        self.tuned_label.setGeometry(QtCore.QRect(160, 290, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tuned_label.setFont(font)
        self.tuned_label.setStyleSheet("color: gray")
        self.tuned_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tuned_label.setObjectName("tuned_label")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(330, 400, 51, 31))
        self.stop_button.setObjectName("stop_button")
        self.diff_label = QtWidgets.QLabel(self.centralwidget)
        self.diff_label.setGeometry(QtCore.QRect(0, 30, 401, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(50)
        font.setKerning(True)
        self.diff_label.setFont(font)
        self.diff_label.setAutoFillBackground(False)
        self.diff_label.setStyleSheet("background: #FFFFFF")
        self.diff_label.setAlignment(QtCore.Qt.AlignCenter)
        self.diff_label.setObjectName("diff_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
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
        self.ref_label.setText(_translate("MainWindow", "Reference:"))
        self.ref_units.setText(_translate("MainWindow", "Hz"))
        self.tol_units.setText(_translate("MainWindow", "Hz"))
        self.tol_label.setText(_translate("MainWindow", "Tolerance:"))
        self.upd_button.setText(_translate("MainWindow", "Update"))
        self.tuned_label.setText(_translate("MainWindow", "Tuned"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.diff_label.setText(_translate("MainWindow", "0 Hz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

