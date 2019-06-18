from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pytube import Playlist
from pytube import YouTube

VideoPlaylistDownload , _ = loadUiType('VideoPlaylistDownload.ui')

class DownloadVideoPlaylistWidget(QMainWindow , VideoPlaylistDownload):
    Links =""
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
        self.pushButton_2.clicked.connect(self.DownloadVideoPlaylist)

    def DownloadList(self):
        VideoPlaylist = Playlist(self.Links)
        PlaylistLink = VideoPlaylist.parse_links()
        VideosLink  = []
        for item in PlaylistLink:
            VideosLink.append( (YouTube("https://www.youtube.com" + item).title ,"https://www.youtube.com" + item)   )
        print(VideosLink)
        if VideosLink:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row , form in enumerate(VideosLink):
                for column , item in enumerate(form):
                    self.tableWidget.setItem(row , column , QTableWidgetItem(item))
                    column += 1
                self.tableWidget.insertRow(self.tableWidget.rowCount())
        Videos = YouTube("https://www.youtube.com" + PlaylistLink[0])
        Dict={}
        List=[]
        Dict["144p"] = [1,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='144p').all()]]
        Dict["240p"] = [2,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='240p').all()]]
        Dict["360p"] = [3,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='360p').all()]]
        Dict["480p"] = [4,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='480p').all()]]
        Dict["720p"] = [5,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='720p').all()]]
        Dict["1080p"] = [6,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='1080p').all()]]
        Dict["1440p"] = [7,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='1440p').all()]]
        Dict["2160p"] = [8,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='2160p').all()]]
        self.comboBox_2.clear()
        with open('Preferences.txt','r') as Preferences:
            for i in Preferences:
                List.append(i)   
            Preferences.close()
        if List[1][17:-1] == "Ask Every Time":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("Select Resolution")
            for resolutions ,values in Dict.items():
                if values[1]:
                    self.comboBox_2.addItem(resolutions)
        else:
            count = Dict[List[1][17:-1]][0]
            print(count)
            flag = False
            while(count > 0):
                for resolutions , values in Dict.items():
                    if values[1]:
                        if count == values[0]:
                            self.Resolution = resolutions
                            flag=True
                            break
                count-=1
                if flag:
                    break                     
            self.comboBox_2.clear()
            self.comboBox_2.addItem("Select Resolution")
            for resolutions ,values in Dict.items():
                if values[1]:
                    self.comboBox_2.addItem(resolutions)
            print(self.Resolution)
            if self.Resolution == "144p":
                self.comboBox_2.setCurrentIndex(1)
            elif self.Resolution ==  "240p":
                self.comboBox_2.setCurrentIndex(2)
            elif self.Resolution ==  "360p":
                self.comboBox_2.setCurrentIndex(3)
            elif self.Resolution ==  "480p":
                self.comboBox_2.setCurrentIndex(4)    
            elif self.Resolution == "720p":
                self.comboBox_2.setCurrentIndex(5)
            elif self.Resolution == "1080p":
                self.comboBox_2.setCurrentIndex(6)
            elif self.Resolution == "1440p":
                self.comboBox_2.setCurrentIndex(7)  
            elif self.Resolution == "2160p":
                self.comboBox_2.setCurrentIndex(8)    
    
    def DownloadVideoPlaylist(self):
        self.close()