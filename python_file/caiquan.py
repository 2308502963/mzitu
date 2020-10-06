# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caiquan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shitou = QtWidgets.QPushButton(self.centralwidget)
        self.shitou.setGeometry(QtCore.QRect(130, 80, 93, 28))
        self.shitou.setObjectName("shitou")
        self.jiandao = QtWidgets.QPushButton(self.centralwidget)
        self.jiandao.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.jiandao.setObjectName("jiandao")
        self.bu = QtWidgets.QPushButton(self.centralwidget)
        self.bu.setGeometry(QtCore.QRect(440, 80, 93, 28))
        self.bu.setObjectName("bu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.shitou.setText(_translate("MainWindow", "1(石头)"))
        self.jiandao.setText(_translate("MainWindow", "2（剪刀）"))
        self.bu.setText(_translate("MainWindow", "3（布）"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
