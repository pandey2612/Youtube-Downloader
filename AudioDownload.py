from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pytube import YouTube

AudioDownload , _ = loadUiType('AudioDownload.ui')

class DownloadAudioWidget(QMainWindow , AudioDownload):
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
        self.HandelButtons()
    
    def HandelButtons(self):
        self.pushButton_2.clicked.connect(self.DownloadAudio)
    def DownloadParameters(self):
        if self.Links:
            print("Yes")
            print(self.Links)
            self.label.setText(YouTube(self.Links).title)

    def DownloadAudio(self):
        self.close()