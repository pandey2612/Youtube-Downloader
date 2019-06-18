from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import sqlite3
import re
from cryptography.fernet import Fernet
from Youtube import DownloadDashboard
import os
from pytube import *

LogIN , _ = loadUiType('LogIN.ui')


Key =b'orHzoGOLuivudX_Obkc3C-WGOzFXlPG1vkglGF3qwk4='
CipherSuite = Fernet(Key)

class LogIN(QMainWindow ,LogIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()   
        self.HandleUI_Changes()
    
    def HandleUI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_3.setDisabled(True)
        self.HandleButtons()

    def HandleButtons(self):
        self.pushButton_3.clicked.connect(self.LogIN_Button)
        self.pushButton_4.clicked.connect(self.Register_Button)
        self.pushButton_2.clicked.connect(self.Register)
        self.pushButton.clicked.connect(self.LogIN)

    def LogIN_Button(self):
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(False)

    def Register_Button(self):
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(True)    

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def LogIN(self):
        UserName = self.lineEdit.text()
        Password = self.lineEdit_2.text()
        self.db = sqlite3.connect('Youtube.db')
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT UserEmail FROM Users WHERE UserName = ?''',[(UserName)])
        Data = self.cur.fetchall()
        if len(Data) >0:
            self.lineEdit.setText('')
            if Password =="":
                self.label.setText('Password Field Not be Empty')
                self.label.setStyleSheet('color:red')
            else:
                self.cur.execute('''SELECT UserPassword FROM Users WHERE UserName = ?''',[(UserName)])
                Data = self.cur.fetchall()
                if Password == CipherSuite.decrypt(Data[0][0]).decode('utf-8'):
                    self.label.setText('')
                    self.statusBar().showMessage('Logged In')
                    self.lineEdit_2.setText('')
                    self.window2 = DownloadDashboard()
                    self.close()
                    self.window2.show()
                    
        elif UserName=='':
            self.label.setText('Username Field Not be Empty')
            self.label.setStyleSheet('color:red')
        else:
            self.label.setText('Username Not Registered')
            self.label.setStyleSheet('color:red')

    def Register(self):
        self.db = sqlite3.connect('Youtube.db')
        self.cur  = self.db.cursor()

        Username = self.lineEdit_3.text()
        Email = self.lineEdit_5.text()
        Password = self.lineEdit_7.text()
        ConfirmPassword = self.lineEdit_8.text()
        Mobile_No = self.lineEdit_4.text()

        if Username =='':
            self.UserName_Label.setText('Username Field not be Empty')
            self.UserName_Label.setStyleSheet('color:red')
        elif len(Username) < 5:
            self.UserName_Label.setText('Username Too Short')
            self.UserName_Label.setStyleSheet('color:red')
        else:
            self.cur.execute('''SELECT * FROM Users WHERE UserName= ?''',[(Username)])
            Data =self.cur.fetchall()
            if len(Data)>0:
                self.UserName_Label.setText('Username already exist')
                self.UserName_Label.setStyleSheet('color:red')
            else:
                self.UserName_Label.setText('')
                if Email == '':
                    self.Email_Label.setText('Email Field not be Empty')
                    self.Email_Label.setStyleSheet('color:red')
                else:
                    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', Email) == None :
                        self.Email_Label.setText('Invalid Email Address')
                        self.Email_Label.setStyleSheet('color:red')
                    else:

                        self.cur.execute('''SELECT * FROM Users WHERE UserEmail = ?''',[(Email)])
                        Data = self.cur.fetchall()
                        if len(Data)>0:
                            self.Email_Label.setText('Email Already Registered')
                            self.Email_Label.setStyleSheet('color:red')
                        else:
                            self.Email_Label.setText('')
                            if Mobile_No=='':
                                self.MobileNo_Label.setText('Mobile Number Field not be Empty')
                                self.MobileNo_Label.setStyleSheet('color:red')
                            elif len(Mobile_No) !=10:
                                self.MobileNo_Label.setText('Mobile Number not valid')
                                self.MobileNo_Label.setStyleSheet('color:red')
                            else:
                                self.cur.execute('''SELECT * FROM Users WHERE MobileNumber= ?''',[(Mobile_No)])
                                Data =self.cur.fetchall()
                                if len(Data)>0:
                                    self.MobileNo_Label.setText('Mobile Number Already Registered')
                                    self.MobileNo_Label.setStyleSheet('color:red')
                                else:
                                    if Mobile_No.isnumeric()==False:
                                        self.MobileNo_Label.setText('Mobile Number Not Valid')
                                        self.MobileNo_Label.setStyleSheet('color:red')
                                    else:
                                        self.MobileNo_Label.setText('')
                                        Mobile_No=int(Mobile_No)
                                        if len(Password)<8:
                                            self.Password_Label1.setText("Password Will be 8-12 Character Long")
                                            self.Password_Label1.setStyleSheet('color: red')
                                        elif len(Password)>12:
                                            self.Password_Label1.setText("Password Will be 8-12 Character Long")
                                            self.Password_Label1.setStyleSheet('color: red')
                                        else:

                                            if Password != ConfirmPassword:
                                                self.Password_Label1.setText('')
                                                self.Password_Label2.setText("Password and Confirm Password does'nt Match ")
                                                self.Password_Label2.setStyleSheet('color: red')
                                            else:
                                                self.Password_Label2.setText("")
                                                Password=CipherSuite.encrypt(bytes(Password,'utf-8'))
                                                self.cur.execute('''INSERT INTO Users (UserName , UserEmail , UserPassword , MobileNumber) VALUES (?,?,?,?)''',(Username ,Email ,Password , Mobile_No,))
                                                self.db.commit()
                                                self.statusBar().showMessage('User Registered')

                                                self.lineEdit_3.setText('')
                                                self.lineEdit_5.setText('')
                                                self.lineEdit_7.setText('')
                                                self.lineEdit_8.setText('')
                                                self.lineEdit_4.setText('')
                                                
def main():
    app = QApplication(sys.argv)
    window = LogIN()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
