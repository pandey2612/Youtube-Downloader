from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pytube import Playlist
from pytube import YouTube
AudioPlaylistDownload , _ = loadUiType('AudioPlaylistDownload.ui')

class DownloadAudioPlaylistWidget(QMainWindow , AudioPlaylistDownload):
    Links=""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()
        self.HandleUI_Changes()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Global(self , Link):
        self.Links = Link
        print(self.Links)   
        print('yes1')

    def HandleUI_Changes(self): 
        self.lineEdit.setText(self.Links)
        self.lineEdit.setDisabled(True)
        self.HandelButtons()

    def HandelButtons(self):
        self.pushButton_2.clicked.connect(self.DownloadAudioPlaylist)

    def DownloadList(self):
        AudioPlaylist = Playlist(self.Links)
        PlaylistLink = AudioPlaylist.parse_links()
        AudioLink  = []
        for item in PlaylistLink:
            AudioLink.append( (YouTube("https://www.youtube.com" + item).title ,"https://www.youtube.com" + item)   )
        print(AudioLink)
        if AudioLink:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row , form in enumerate(AudioLink):
                for column , item in enumerate(form):
                    self.tableWidget.setItem(row , column , QTableWidgetItem(item))
                    column += 1
                self.tableWidget.insertRow(self.tableWidget.rowCount())

    def DownloadAudioPlaylist(self):
        self.close()
        