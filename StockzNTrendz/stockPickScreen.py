from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql
import re
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
        print("Data from first window:" + username)
        global globalUser 
        globalUser = username
    def setupUi(self, pickerWindow, username):
        pickerWindow.setObjectName("pickerWindow")
        pickerWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(pickerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stockList = QtWidgets.QListWidget(self.centralwidget)
        self.stockList.setGeometry(QtCore.QRect(190, 120, 290, 121))
        self.stockList.setObjectName("stockList")
        retrievalQuery = "SELECT STOCK1, STOCK2, STOCK3 FROM holdings WHERE ID = '"+username+"'"
        cursor.execute(retrievalQuery)
        items = cursor.fetchall()
        itemString = "".join(map(str, items))
        itemStringRe = re.sub(r'[()]', '', itemString).replace("'","").replace(" ","")
        #itemStringList = list(map(str, itemStringRe[0].split(',')))
        itemStringList = itemStringRe.split(',')
        print(itemStringList)
        for item in itemStringList:
            self.stockList.addItem(item)
        #for item in items: this adds the entire tuple...
            #print(item)
            #self.stockList.addItem(str(item))
        
        self.stockListLabel = QtWidgets.QLabel(self.centralwidget)
        self.stockListLabel.setGeometry(QtCore.QRect(190, 70, 420, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.stockListLabel.setFont(font)
        self.stockListLabel.setObjectName("stockListLabel")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(190, 260, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
        #input field for adding new stocks
        self.stockInputField = QtWidgets.QLineEdit(self.centralwidget)
        self.stockInputField.setGeometry(QtCore.QRect(290, 450, 80, 20))
        self.stockInputField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.stockInputField.setObjectName("stockInputField")
        #Submit button for stock input field
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(280, 490, 100, 51))
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
    def retranslateUi(self, pickerWindow):
        _translate = QtCore.QCoreApplication.translate
        pickerWindow.setWindowTitle(_translate("pickerWindow", "Stock Picks"))
        self.stockListLabel.setText(_translate("pickerWindow", "Your Current List of Stocks:"))
        self.viewButton.setText(_translate("pickerWindow", "View"))
        self.submitButton.setText(_translate("pickerWindow", "Submit"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pickerWindow = QtWidgets.QMainWindow()
    ui = Ui_pickerWindow()
    ui.setupUi(pickerWindow)
    pickerWindow.show()
    sys.exit(app.exec_())
