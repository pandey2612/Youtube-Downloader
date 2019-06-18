from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import re
from VideoDownload import DownloadVideoWidget
from AudioDownload import DownloadAudioWidget
from VideoPlaylistDownload import DownloadVideoPlaylistWidget
from AudioPlaylistDownload import DownloadAudioPlaylistWidget
import os
from pytube import *
Youtube  , _ = loadUiType('Youtube.ui')


class DownloadDashboard(QMainWindow , Youtube):
    
    AudioFormat="Default Audio Format"
    VideoResolution= "Ask Every Time"
    VideoFormat="Default Video Format"

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
    
    def HandleUI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_2.setCurrentIndex(0)
        self.HandelButtons()
        self.pushButton_7.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.tabWidget_3.tabBar().setVisible(False)
        self.tabWidget_3.setCurrentIndex(0)
        self.pushButton_8.setDisabled(True)
        self.Path()

    def HandelButtons(self):
        self.pushButton_7.clicked.connect(self.HomePage)
        self.pushButton_5.clicked.connect(self.Preferences)
        self.pushButton_6.clicked.connect(self.Information)
        self.pushButton_3.clicked.connect(self.Downloading)
        self.pushButton_4.clicked.connect(self.Downloaded)
        self.pushButton_8.clicked.connect(self.Audio)
        self.pushButton_9.clicked.connect(self.Video)
        self.pushButton_10.clicked.connect(self.Path)
        self.pushButton_2.clicked.connect(self.VideoLinkValidation)
        self.pushButton_12.clicked.connect(self.AudioLinkValidation)
        self.pushButton_11.clicked.connect(self.ChangePath)
        self.pushButton_13.clicked.connect(self.SavePath)
        self.pushButton_14.clicked.connect(self.SaveAudioPreferences)
        self.pushButton_15.clicked.connect(self.SaveVideoPreferences)

    def HomePage(self):
        self.tabWidget.setCurrentIndex(0) 
        self.pushButton_7.setDisabled(True)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)  

    def Preferences(self):
        self.tabWidget.setCurrentIndex(1) 
        self.pushButton_7.setDisabled(False)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(False)
        self.pushButton_8.setDisabled(True)
        self.tabWidget_3.setCurrentIndex(0)
        self.pushButton_10.setDisabled(False)
        List= []
        if os.path.isfile("Preferences.txt"):
            with open('Preferences.txt','r') as Preferences:
                for i in Preferences:
                    List.append(i)   
            Preferences.close()
            if List[0][13:-1] == "Default Audio Format":
                self.comboBox_2.setCurrentIndex(0)
            elif List[0][13:-1] == "Audio.mp3":
                self.comboBox_2.setCurrentIndex(1)
            elif List[0][13:-1] ==  "Audio.mp4":
                self.comboBox_2.setCurrentIndex(2)
            elif List[0][13:-1] ==  "Audio.m4a":
                self.comboBox_2.setCurrentIndex(3)
            elif List[0][13:-1] == "Audio.webm":
                self.comboBox_2.setCurrentIndex(4)

            if List[1][17:-1] == "Ask Every Time":
                self.comboBox_4.setCurrentIndex(0)
            elif List[1][17:-1] == "144p":
                self.comboBox_4.setCurrentIndex(1)
            elif List[1][17:-1] ==  "240p":
                self.comboBox_4.setCurrentIndex(2)
            elif List[1][17:-1] ==  "360p":
                self.comboBox_4.setCurrentIndex(3)
            elif List[1][17:-1] ==  "480p":
                self.comboBox_4.setCurrentIndex(4)    
            elif List[1][17:-1] == "720p":
                self.comboBox_4.setCurrentIndex(5)
            elif List[1][17:-1] == "1080p":
                self.comboBox_4.setCurrentIndex(6)
            elif List[1][17:-1] == "1440p":
                self.comboBox_4.setCurrentIndex(7)
            else:
                self.comboBox_4.setCurrentIndex(8)

            if List[2][13:-1] == "Default Video Format":
                self.comboBox_3.setCurrentIndex(0)
            elif List[2][13:-1] == "Video.mp4":
                self.comboBox_3.setCurrentIndex(1)
            elif List[2][13:-1] ==  "Video.avi":
                self.comboBox_3.setCurrentIndex(2)
            elif List[2][13:-1] ==  "Video.mkv":
                self.comboBox_3.setCurrentIndex(3)
            elif List[2][13:-1] == "Video.webm":
                self.comboBox_3.setCurrentIndex(4)
        else :
            File = open("Preferences.txt" , "w")
            File.write("Audio Format:Default Audio Format\n")
            File.write("Video Resolution:Ask Every Time\n")
            File.write("Video Format:Default Video Format")
            File.close()
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(0)


    def Information(self):
        self.tabWidget.setCurrentIndex(2) 
        self.pushButton_7.setDisabled(False)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(True)           
    
    def Downloading(self):
        self.tabWidget_2.setCurrentIndex(0)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(False)
        self.lineEdit.setDisabled(False)
        

    def Downloaded(self):
        self.tabWidget_2.setCurrentIndex(1)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(True)
        self.lineEdit.setDisabled(True)

    def Audio(self):
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(False)
        self.pushButton_10.setDisabled(False)
        self.tabWidget_3.setCurrentIndex(0)

    def Video(self):
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(True)
        self.pushButton_10.setDisabled(False)
        self.tabWidget_3.setCurrentIndex(1)

    def Path(self):
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(False)
        self.pushButton_10.setDisabled(True)
        self.tabWidget_3.setCurrentIndex(2)  
        self.lineEdit_2.setDisabled(True)

    def CleanLink(self):
        self.lineEdit.setText("")
        
        
        PathFile = open('Path.txt')
        Path = PathFile.readline()    
        if "/root/Downloads/Youtube Video Downloader" in Path:
            print("Yes")
        else:
            PathFile = open('Path.txt','w')
            PathFile.write("/root/Downloads/Youtube Video Downloader")
            PathFile.close()
    
        self.lineEdit_2.setText(Path)
        PathFile.close()
    

    def ChangePath(self):
        self.lineEdit_2.setDisabled(False)
        
        
    def SavePath(self):
        New_Path = self.lineEdit_2.text()
        if os.path.isdir(New_Path) :
            print("Directory ALready present")
        else:
            os.mkdir(New_Path)
            PathFile = open('Path.txt','w')
            PathFile.write(New_Path)
            PathFile.close()
        self.lineEdit_2.setDisabled(True) 

    
    def SaveAudioPreferences(self):
        A = self.comboBox_2.currentIndex()
        List= []
        if os.path.isfile("Preferences.txt"):
            with open('Preferences.txt','r') as Preferences:
                for i in Preferences:
                    List.append(i)   
            Preferences.close()
        
        if A==0 :
            self.AudioFormat = "Default Audio Format"
        elif A==1:
            self.AudioFormat = "Audio.mp3"
        elif A==2:
            self.AudioFormat = "Audio.mp4"
        elif A==3:
            self.AudioFormat = "Audio.m4a"
        else :
            self.AudioFormat = "Audio.webm"

        with open('Preferences.txt','w') as Preferences:
            Preferences.write("Audio Format:"+self.AudioFormat+"\n")
            Preferences.write(List[1][:-1]+"\n")
            Preferences.write(List[2][:-1]+"\n")
        Preferences.close()


    def SaveVideoPreferences(self):
        V = self.comboBox_4.currentIndex()
        v = self.comboBox_3.currentIndex()
        List= []
        if os.path.isfile("Preferences.txt"):
            with open('Preferences.txt','r') as Preferences:
                for i in Preferences:
                    List.append(i)   
            Preferences.close()

        if V==0:
            self.VideoResolution = "Ask Every Time"
        elif V==1:
            self.VideoResolution = "144p"
        elif V==2:
            self.VideoResolution = "240p"
        elif V==3:
            self.VideoResolution = "360p"
        elif V==4 :
            self.VideoResolution = "480p"
        elif V==5 :
            self.VideoResolution = "720p"  
        elif V==6 :
            self.VideoResolution = "1080p" 
        elif V==7 :
            self.VideoResolution = "1440p"         
        else:
            self.VideoResolution = "2160p"
        
        if v==0:
            self.VideoFormat = "Default Video Format"
        elif v==1:
            self.VideoFormat = "Video.mp4"
        elif v==2:
            self.VideoFormat = "Video.avi"
        elif v==3:
            self.VideoFormat = "Video.mkv"
        else :
            self.VideoFormat = "Video.webm"

        with open('Preferences.txt','w') as Preferences:
            Preferences.write(List[0][:-1]+"\n")
            Preferences.write("Video Resolution:"+self.VideoResolution+"\n")
            Preferences.write("Video Format:"+self.VideoFormat+"\n")
        Preferences.close()
        

    def VideoLinkValidation(self):

        Link = self.lineEdit.text()
        if re.match('^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$' , Link) == None :
            if QMessageBox.warning(self,'Error' , 'Invalid URL' , QMessageBox.Ok ) == QMessageBox.Ok:
                self.lineEdit.setText('')
        elif "playlist" in Link:
            self.statusBar().showMessage('Link Found')       
            self.window5 = DownloadVideoPlaylistWidget()
            self.window5.Global(Link)
            self.window5.HandleUI_Changes()
            self.window5.DownloadList()
            self.setDisabled(True)
            self.window5.show()

        else:    
            self.statusBar().showMessage('Link Found')       
            self.window3 = DownloadVideoWidget()
            self.window3.Global(Link)
            self.window3.HandleUI_Changes()
            self.window3.DownloadParameters()
            self.window3.show()

    def AudioLinkValidation(self):
        Link = self.lineEdit.text()
        if re.match('^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$' , Link) == None :
            if QMessageBox.warning(self,'Error' , 'Invalid URL' , QMessageBox.Ok ) == QMessageBox.Ok:
                self.lineEdit.setText('')
        
        elif "playlist" in Link:
            self.statusBar().showMessage('Link Found')       
            self.window6 = DownloadAudioPlaylistWidget()
            self.window6.Global(Link)
            self.window6.HandleUI_Changes()
            self.window6.DownloadList()
            self.window6.show()
        else:
            self.statusBar().showMessage('Link Found')       
            self.window4 = DownloadAudioWidget()
            self.window4.Global(Link)
            self.window4.HandleUI_Changes()
            self.window4.DownloadParameters()
            self.window4.show()        
            


            
            