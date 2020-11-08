from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql
from stockPickScreen import Ui_pickerWindow
import pandas as pd
import pandas_datareader as web
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pyEX as p
from datetime import datetime as date

db = mysql.connect(
    host="localhost",
    user="akrbanj",
    passwd="akrbanj19!",
    database="smadb"
)
cursor = db.cursor()

class Ui_MainWindow2(object):
    def openPickWindow(self, MainWindow2):
        MainWindow2 = self.centralwidget
        self.window = QtWidgets.QMainWindow()
        self.username = self.userField.text()
        self.ui = Ui_pickerWindow(self.username)
        self.ui.setupUi(self.window, self.username)
        MainWindow2.hide()
        self.window.show()
	    
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(802, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(140, 40, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.userField = QtWidgets.QLineEdit(self.centralwidget)
        self.userField.setGeometry(QtCore.QRect(200, 170, 113, 20))
        self.userField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userField.setObjectName("userField")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 150, 200, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 200, 200, 16))
        self.label_2.setObjectName("label_2")
        self.userField_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.userField_2.setGeometry(QtCore.QRect(200, 220, 113, 20))
        self.userField_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userField_2.setObjectName("userField_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 56, 40))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 18))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)
        
        #Line where we connect loginCLicked function to button click
        self.pushButton.clicked.connect(self.loginClicked)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Stockz N Trendz"))
        self.label.setText(_translate("MainWindow", "Enter your Username Here:"))
        self.label_2.setText(_translate("MainWindow", "Enter your Password Here:"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
    def loginClicked(self, text):
	    userVar = ""
	    passVar = ""
	    
	    userVar = self.userField.text()
	    passVar = self.userField_2.text()
	    #Here we check to see if this combo exists in db
	    query = ("SELECT id FROM users WHERE users.username = '"+userVar+"' AND users.password = '"+passVar+"'")
	    cursor.execute(query)
	    result = cursor.fetchone()
	    self.pushButton.clicked.connect(self.openPickWindow)
	    #print(result) using this to test
	    if(result != None):
			#we want to create a new page where the user has a table of their 3 stocks.
		    self.openPickWindow(self.centralwidget)
	    else:
		    print("ERROR: Account does not exist. You need to register first!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
