from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql
import re
import pandas as pd
import pandas_datareader as web
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pyEX as p
from datetime import datetime as date
from datetime import timedelta

db = mysql.connect(
    host="localhost",
    user="akrbanj",
    passwd="akrbanj19!",
    database="smadb"
)

cursor = db.cursor()
class Ui_pickerWindow(object):
#the init is used for testing that the username really did get passed to
#this window!
    globalUser = ""
    def __init__(self,username):
        #print("Data from first window:" + username) used to test data transmission
        global globalUser
        globalUser = username
    def setupUi(self, pickerWindow, username):
        pickerWindow.setObjectName("pickerWindow")
        pickerWindow.resize(800, 600)
        pickerWindow.setStyleSheet("background-color: #245DA3;")
        self.centralwidget = QtWidgets.QWidget(pickerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 800, 50))
        self.stockList = QtWidgets.QListWidget(self.centralwidget)
        self.stockList.setGeometry(QtCore.QRect(190, 130, 290, 101))
        self.stockList.setObjectName("stockList")
        self.stockList.setStyleSheet("background-color: white;")
        font2 = QtGui.QFont("Impact")
        font2.setPointSize(15)
        retrievalQuery = "SELECT STOCK1, STOCK2, STOCK3 FROM holdings WHERE ID = '"+username+"'"
        cursor.execute(retrievalQuery)
        items = cursor.fetchall()
        itemString = "".join(map(str, items))
        itemStringRe = re.sub(r'[()]', '', itemString).replace("'","").replace(" ","")
        #itemStringList = list(map(str, itemStringRe[0].split(',')))
        itemStringList = itemStringRe.split(',')
        #print(itemStringList)
        for item in itemStringList:
            self.stockList.addItem(item)
        #for item in items: this adds the entire tuple...
            #print(item)
            #self.stockList.addItem(str(item))
        
        self.stockListLabel = QtWidgets.QLabel(self.centralwidget)
        self.stockListLabel.setGeometry(QtCore.QRect(150, 70, 420, 50))
        self.stockListLabel.setStyleSheet("background-color: #05302b; color: #6DDEAB; border: 3px solid black;")
        self.changeLabel = QtWidgets.QLabel(self.centralwidget)
        self.changeLabel.setGeometry(QtCore.QRect(160, 440, 500, 50))
        self.recLabel = QtWidgets.QLabel(self.centralwidget)
        self.recLabel.setGeometry(QtCore.QRect(190,310,280,40))
        self.headerLabel.setFont(font2)
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setStyleSheet("background-color: #05302b; color: #6DDEAB;")
        self.recStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.recStatusLabel.setGeometry(QtCore.QRect(300,360,80,100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font2 = QtGui.QFont()
        font2.setPointSize(7)
        font2.setBold(True)
        font2.setWeight(50)
        font3 = QtGui.QFont("Impact")
        font3.setPointSize(13)
        font3.setWeight(75)
        self.stockListLabel.setFont(font)
        self.stockListLabel.setObjectName("stockListLabel")
        self.recLabel.setFont(font)
        self.recLabel.setObjectName("recLabel")
        self.recLabel.setStyleSheet("background-color: #05302b; color: #6DDEAB; border: 3px solid black;")
        self.changeLabel.setFont(font2)
        self.changeLabel.setObjectName("changeLabel")
        self.changeLabel.setStyleSheet("color: white;")
        self.recStatusLabel.setFont(font3)
        self.recStatusLabel.setObjectName("rectStatusLabel")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(280, 250, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
        self.viewButton.clicked.connect(self.viewClicked)
        self.viewButton.setStyleSheet("color: #05302b; background-color: #27c4b2; font:bold;")
        #input field for adding new stocks
        self.stockInputField = QtWidgets.QLineEdit(self.centralwidget)
        self.stockInputField.setGeometry(QtCore.QRect(290, 490, 80, 20))
        self.stockInputField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.stockInputField.setObjectName("stockInputField")
        self.stockInputField.setStyleSheet("background-color: white;")
        #Submit button for stock input field
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(280, 520, 100, 51))
        self.submitButton.setStyleSheet("color: #05302b; background-color: #27c4b2; font:bold;")
        #connecting submit button to function for taking text from line
        self.submitButton.clicked.connect(self.submitClicked)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        pickerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pickerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        pickerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pickerWindow)
        self.statusbar.setObjectName("statusbar")
        pickerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(pickerWindow)
        QtCore.QMetaObject.connectSlotsByName(pickerWindow)
    def submitClicked(self, text):
        newStock = self.stockInputField.text()
        #using a loop to make list of existing stocks.
        selectedItem = self.stockList.selectedItems()
        itemIndex = 0
        for item in selectedItem:
            itemIndex = self.stockList.row(item)
            #print(itemIndex) testing of index
            item.setText(newStock)
        #next, write a query to update the column's value with new val
        updateQuery = "UPDATE holdings SET STOCK" +str(itemIndex+1)+"='"+str(newStock)+"'"+" WHERE ID='"+str(globalUser)+"'"
        cursor.execute(updateQuery)
        db.commit()
        self.stockInputField.setText("")
    def retranslateUi(self, pickerWindow):
        _translate = QtCore.QCoreApplication.translate
        pickerWindow.setWindowTitle(_translate("pickerWindow", "Stock Picks"))
        self.stockListLabel.setText(_translate("pickerWindow", "Your Current List of Stocks:"))
        self.changeLabel.setText(_translate("pickerWindow", "Tip: To CHANGE a stock: Highlight a stock, type new one (in field below) and click Submit"))
        self.recLabel.setText(_translate("pickerWindow", "Recommendation:"))
        self.viewButton.setText(_translate("pickerWindow", "View"))
        self.submitButton.setText(_translate("pickerWindow", "Submit"))
        self.headerLabel.setText(_translate("pickerWindow", "SMATrendz"))
    def viewClicked(self):
        stockPick = self.stockList.selectedItems()
        ticker = ""
        for selectedStock in stockPick:
            ticker = selectedStock.text()
        todaysDate = pd.to_datetime('today').date()
        end = dt.datetime.now()
        start = end - timedelta(days=250)
        #print(end)
        
        df = web.DataReader(ticker, 'yahoo', start, end)
        df['SMA50'] = df['Adj Close'].rolling(5).mean()
        df['SMA200'] = df['Adj Close'].rolling(10).mean()
        
        #plot testing
        plt.figure(figsize=(15,5))
        plt.plot(df['SMA50'], label='SMA for 50 days')
        plt.plot(df['SMA200'], label='SMA for 200 days')
        plt.title('Simple Moving Averages of 50 and 200 for ' + ticker)
        plt.legend()
        plt.show()
        
        #here we get the last row and last column first, then get the SMA value
        SMA200Frame = df.iloc[-1:,[-1]]
        SMA200 = SMA200Frame['SMA200'].values[0]
        SMA50Frame = df.iloc[-1:,[-2]]
        SMA50 = SMA50Frame['SMA50'].values[0]
        #print(SMA50) testing the SMA values
        #print(SMA200)
        #here, we want to make a decision based on the math...
        if(SMA50 > SMA200):
            self.recStatusLabel.setStyleSheet("color: #00FF7F;")
            self.recStatusLabel.setText("BUY")
        elif(SMA50 <= SMA200):
            self.recStatusLabel.setStyleSheet("color: Red;")
            self.recStatusLabel.setText("HOLD")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pickerWindow = QtWidgets.QMainWindow()
    ui = Ui_pickerWindow()
    ui.setupUi(pickerWindow)
    pickerWindow.show()
    sys.exit(app.exec_())
