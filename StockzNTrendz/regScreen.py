
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="akrbanj",
    passwd="akrbanj19!",
    database="smadb"
)

cursor = db.cursor()

query = "SELECT * from users"
cursor.execute(query)
records = cursor.fetchall()
print(records)

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(802, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(100, 40, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
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
        self.userField_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userField_2.setObjectName("userField_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 70, 40))
        self.pushButton.setObjectName("pushButton")
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 18))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)
        
        #Line where we connect loginCLicked function to button click
        self.pushButton.clicked.connect(self.regClicked)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Stockz N Trendz Registration"))
        self.label.setText(_translate("MainWindow", "Enter your Username Here:"))
        self.label_2.setText(_translate("MainWindow", "Enter your Password Here:"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        
    def regClicked(self, text):
	    userVar = ""
	    passVar = ""
	    
	    #here, we get the inputted username and pass and commit to the db
	    userVar = self.userField.text()
	    passVar = self.userField_2.text()
	    
	    query = ("SELECT id FROM users WHERE users.username = '"+userVar+"'")
	    cursor.execute(query)
	    result = cursor.fetchone()
	    #print(result) using this to test
	    if(result == None):
		    query2 = "INSERT INTO users (username, password) VALUES (%s, %s)"
		    holdingsquery="INSERT INTO holdings (ID, STOCK1, STOCK2, STOCK3) VALUES (%s, %s, %s, %s)"
		    values = (userVar, passVar)
		    holdingsVals = (userVar, "AAPL", "GOOGL", "MSFT")
		    cursor.execute(query2, values)
		    cursor.execute(holdingsquery, holdingsVals)
		    db.commit()
		    print("You are now registered!")
	    else:
		    print("ERROR: Account already exists!")
	    
	    
		    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec_())
