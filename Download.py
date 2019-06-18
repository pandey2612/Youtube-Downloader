from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
Download , _ = loadUiType('Download.ui')
  
class DownloadWidget(QMainWindow , Download):
    Links =""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()
        self.HandleUI_Changes()
        self.DownloadParameters()
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def Global(self , Link):
        self.Links = Link
        print(self.Links)   

    def HandleUI_Changes(self): 
        print(self.Links)
        self.lineEdit.setText(self.Links)
        self.lineEdit.setDisabled(True)

    def DownloadParameters(self):
        if "playlist" in self.Links:
            self.comboBox_3.setCurrentIndex(2)
            self.comboBox_3.setDisabled(True)
        else:
            self.comboBox_3.setCurrentIndex(1)
            self.comboBox_3.setDisabled(True)
        List = []
        with open('Preferences.txt','r') as Preferences:
            for i in Preferences:
                List.append(i)   
            Preferences.close()
            if List[1][17:-1] == "Ask Every Time":
                self.comboBox_2.setCurrentIndex(0)
            elif List[1][17:-1] == "144p":
                self.comboBox_2.setCurrentIndex(1)
            elif List[1][17:-1] ==  "240p":
                self.comboBox_2.setCurrentIndex(2)
            elif List[1][17:-1] ==  "480p":
                self.comboBox_2.setCurrentIndex(3)
            elif List[1][17:-1] ==  "720p":
                self.comboBox_2.setCurrentIndex(4)    
            elif List[1][17:-1] == "1080p":
                self.comboBox_2.setCurrentIndex(5)
            elif List[1][17:-1] == "1440p":
                self.comboBox_2.setCurrentIndex(6)
            elif List[1][17:-1] == "2160p":
                self.comboBox_2.setCurrentIndex(7)

