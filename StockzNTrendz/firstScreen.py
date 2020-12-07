from PyQt5 import QtCore, QtGui, QtWidgets
from stockPickScreen import *
from StockzNTrendz import Ui_MainWindow2
from regScreen import Ui_MainWindow3
class Ui_MainWindow(object):
    
    def openWindow(self):
	    self.window = QtWidgets.QMainWindow()
	    self.ui = Ui_MainWindow2()
	    self.ui.setupUi(self.window)
	    MainWindow.hide()
	    self.window.show()

    def openRegWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
	
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("background-color: #245DA3;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(165, 110, 450, 51))
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font2 = QtGui.QFont("Impact")
        font2.setPointSize(15)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setStyleSheet("background-color: #05302b; color: #6DDEAB; border: 3px solid black;")
        self.headerLabel.setFont(font2)
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setStyleSheet("background-color: #05302b; color: #6DDEAB;")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(260, 260, 71, 31))
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setStyleSheet("color: #05302b; background-color: #27c4b2; font:bold")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(420, 260, 71, 31))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setStyleSheet("color: #05302b; background-color: #27c4b2; font:bold;")
        #Here, we are having the log-in button open the log in screen
        self.loginButton.clicked.connect(self.openWindow)
        #Here we have the register button open the register screen
        self.registerButton.clicked.connect(self.openRegWindow)
        self.websiteLink = QtWidgets.QLabel(self.centralwidget)
        self.websiteLink.setGeometry(QtCore.QRect(30, 381, 190, 21))
        self.websiteLink.setOpenExternalLinks(True)
        self.websiteLink.setObjectName("websiteLink")
        self.websiteLink.setStyleSheet("color: red;")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome to SMATrendz!"))
        self.headerLabel.setText(_translate("MainWindow", "SMATrendz"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.websiteLink.setText('''<a href='https://akrbanjevic1.github.io/StockznTrendz/' style='color:red;'>Click Here For More Info</a>''')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
