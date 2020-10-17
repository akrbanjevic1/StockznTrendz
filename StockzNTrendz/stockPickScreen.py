from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql

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
    def __init__(self,username):
	    print("Data from first window:" + username)
	    #Note to self: next step is to display the records on the list as individual entries.
	    retrievalQuery = "SELECT STOCK1, STOCK2, STOCK3 FROM holdings WHERE ID = '"+username+"'"
	    cursor.execute(retrievalQuery)
	    results = cursor.fetchall()
	    print(results)
    def setupUi(self, pickerWindow):
        pickerWindow.setObjectName("pickerWindow")
        pickerWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(pickerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stockList = QtWidgets.QListWidget(self.centralwidget)
        self.stockList.setGeometry(QtCore.QRect(190, 120, 290, 121))
        self.stockList.setObjectName("stockList")
        self.stockListLabel = QtWidgets.QLabel(self.centralwidget)
        self.stockListLabel.setGeometry(QtCore.QRect(190, 70, 420, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.stockListLabel.setFont(font)
        self.stockListLabel.setObjectName("stockListLabel")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(380, 260, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.changeButton.setFont(font)
        self.changeButton.setObjectName("changeButton")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(190, 260, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
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

    def retranslateUi(self, pickerWindow):
        _translate = QtCore.QCoreApplication.translate
        pickerWindow.setWindowTitle(_translate("pickerWindow", "Stock Picks"))
        self.stockListLabel.setText(_translate("pickerWindow", "Your Current List of Stocks:"))
        self.changeButton.setText(_translate("pickerWindow", "Change"))
        self.viewButton.setText(_translate("pickerWindow", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pickerWindow = QtWidgets.QMainWindow()
    ui = Ui_pickerWindow()
    ui.setupUi(pickerWindow)
    pickerWindow.show()
    sys.exit(app.exec_())
