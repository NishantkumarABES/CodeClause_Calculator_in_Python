
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.expression=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 80, 81, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.insert("9"))
        
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 80, 81, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda: self.insert("8"))

        
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(160, 80, 81, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda: self.insert("7"))

        
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(80, 120, 81, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda: self.insert("5"))

        
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 120, 81, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda: self.insert("6"))
        
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(160, 120, 81, 41))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda: self.insert("4"))
        
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(80, 160, 81, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(lambda: self.insert("2"))

        
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(0, 160, 81, 41))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(lambda: self.insert("3"))
        
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(160, 160, 81, 41))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(lambda: self.insert("1"))
        
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(80, 200, 81, 41))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(lambda: self.insert("0"))

        
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(0, 200, 81, 41))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 200, 81, 41))
        self.pushButton_24.setObjectName("pushButton_24")
        
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(240, 200, 81, 41))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(self.evaluate)
        
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(240, 120, 81, 41))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(lambda: self.insert("-"))
        
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(240, 80, 81, 41))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(lambda: self.insert("*"))
        
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(240, 160, 81, 41))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(lambda: self.insert("+"))
        
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(240, 40, 81, 41))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(lambda: self.insert("/"))
        
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(80, 40, 81, 41))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(self.clear)
        
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 40, 81, 41))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.clicked.connect(self.square)
        
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(160, 40, 81, 41))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(self.erase)

        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 21))
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
        self.pushButton_13.setText(_translate("MainWindow", "9"))
        self.pushButton_14.setText(_translate("MainWindow", "8"))
        self.pushButton_15.setText(_translate("MainWindow", "7"))
        self.pushButton_16.setText(_translate("MainWindow", "5"))
        self.pushButton_17.setText(_translate("MainWindow", "6"))
        self.pushButton_18.setText(_translate("MainWindow", "4"))
        self.pushButton_19.setText(_translate("MainWindow", "2"))
        self.pushButton_20.setText(_translate("MainWindow", "3"))
        self.pushButton_21.setText(_translate("MainWindow", "1"))
        self.pushButton_22.setText(_translate("MainWindow", "0"))
        self.pushButton_24.setText(_translate("MainWindow", "."))
        self.pushButton_25.setText(_translate("MainWindow", "="))
        self.pushButton_26.setText(_translate("MainWindow", "-"))
        self.pushButton_27.setText(_translate("MainWindow", "*"))
        self.pushButton_28.setText(_translate("MainWindow", "+"))
        self.pushButton_29.setText(_translate("MainWindow", "/"))
        self.pushButton_30.setText(_translate("MainWindow", "C"))
        self.pushButton_31.setText(_translate("MainWindow", "X^2"))
        self.pushButton_32.setText(_translate("MainWindow", "E"))
        
    
    def insert(self,value):
        self.expression=self.expression+value
        self.label.setText(self.expression)
        
    def evaluate(self):
        info=self.label.text()
        try:
            result=eval(info)
            self.label.setText(str(result))
        except:
            self.label.setText("Invalid")
        self.expression=""
        
    def clear(self):
        self.label.setText("")
        self.expression=""
        
    def erase(self):
        self.expression=self.expression[:-1]
        self.label.setText(self.expression)
        
    def square(self):
        info=self.label.text()
        result=int(info)**2
        self.label.setText(str(result))
        self.expression=str(result)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
