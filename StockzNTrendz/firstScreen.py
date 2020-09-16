# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstScreen.ui'
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
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(150, 70, 600, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(340, 180, 71, 31))
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(340, 230, 71, 31))
        self.loginButton.setObjectName("loginButton")
        self.websiteLink = QtWidgets.QLabel(self.centralwidget)
        self.websiteLink.setGeometry(QtCore.QRect(30, 381, 190, 21))
        self.websiteLink.setOpenExternalLinks(True)
        self.websiteLink.setObjectName("websiteLink")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
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
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome to Stockz N Trendz!"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.websiteLink.setText('''<a href='http://stackoverflow.com'>Click Here For More Info</a>''')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
