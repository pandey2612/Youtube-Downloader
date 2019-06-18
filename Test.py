from pytube import *
import os
import subprocess
import glob
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
"""
playlist = Playlist('https://www.youtube.com/playlist?list=PLflqtq8EOGALCJj-I8M7_dtrPh7_ZieDz')
h = playlist.parse_links()
VideoLink=[]
for item in h:
    Link=("https://www.youtube.com" + item)    
    print(Link)
    Videos = YouTube(Link)
    print(Videos.title)
    Dict={}
    Dict["144p"] = [1,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='144p').all()]]
    Dict["240p"] = [2,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='240p').all()]]
    Dict["360p"] = [3,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='360p').all()]]
    Dict["480p"] = [4,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='480p').all()]]
    Dict["720p"] = [5,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='720p').all()]]
    Dict["1080p"] = [6,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='1080p').all()]]
    Dict["1440p"] = [7,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='1440p').all()]]
    Dict["2160p"] = [8,[stream.itag for stream in Videos.streams.filter(file_extension='webm',res='2160p').all()]]
    print(list(Dict.values()))
    print(list(Dict.values())[0][0] )
    print(list(Dict.keys()))
    print(Dict["1080p"][0])
    n=6

    for resolution, values in Dict.items():
        if values[1]:
            print(resolution)

    flag = False
    while n>0:
        for resolution, values in Dict.items():
            if values[1]:
                if n == values[0]:
                    print(resolution)
                    flag = True
                    break     
        n-=1   
        if flag:
            break       

global File_Size

a= [stream.itag for stream in Videos.streams.filter(mime_type="audio/webm").order_by('abr').all()]
File_Size = Videos.streams.get_by_itag(a[len(a) - 1]).filesize

if a:
    Videos.streams.get_by_itag(a[len(a) - 1]).download(filename='A')
File_Size += Videos.streams.filter(file_extension='mp4',res='1080p').first().filesize

A = [stream.itag for stream in Videos.streams.filter(file_extension='mp4',res='1080p').all()]
B = [stream for stream in Videos.streams.filter(file_extension='mp4',res='480p').all()]
C = [stream for stream in Videos.streams.filter(file_extension='mp4',res='720p').all()]
D = [stream for stream in Videos.streams.filter(file_extension='mp4',res='360p').all()]

if A:
    Videos.streams.get_by_itag(A[len(A) - 1 ]).download(filename = 'A')   

cmd = 'ffmpeg -y -i '+'A.'+ 'webm' + ' -r 30 -i '+ 'A.'+ 'mp4' +  ' -filter:a aresample=async=1 -c:a flac -c:v copy ' + 'c.' + 'mkv'
subprocess.call(cmd, shell=True)                                     # "Muxing Done
print('Muxing Done')


for filename in os.listdir("."):
    if filename.startswith("c"):
        os.rename(filename , Videos.streams.first().default_filename[:-4] +'.mkv')

for filename in os.listdir("."):    
    if filename.startswith("A"):
        os.remove(filename)

print(Videos.thumbnail_url)



New_Path = '/root/Downloads/Youtube'
if os.path.isdir(New_Path) :
    print("Directory ALready present")
else:
    os.mkdir(New_Path)


with open('Preferences.txt','w') as Preferences:
    Preferences.write("Audio Format:.m4a\n")
    Preferences.write("Video Resolution:1080p\n")
    Preferences.write("Video Format:.mp4\n")
Preferences.close()

with open('Preferences.txt','r') as Preferences:
    List= []
    for i in Preferences:
        List.append(i)
for i in range(0,len(List)):
    print(List[i][13:-1])
Preferences.close()     

if os.path.isfile("Preference.txt"):
    print("Yes")
else:
    File = open("Preference.txt" , "w")
    File.write("Audio Format:Default Audio Format\n")
    File.write("Video Resolution:Ask Every Time\n")
    File.write("Video Format:Default Video Format")
    File.close()    

PathFile = open('Path.txt')
Path = PathFile.readline()    
if "/root/Downloads/Youtube Video Downloader" in Path:
    print("Yes")
else:
    PathFile = open('Path.txt','w')
    PathFile.write("/root/Downloads/Youtube Video Downloader")
    PathFile.close()



playlist = Playlist('https://www.youtube.com/playlist?list=PLflqtq8EOGAJJDNAct-tz9X8C6-MSljjB')
h = playlist.populate_video_urls()
for item in h:
    print(item)



db = sqlite3.connect('Youtube.db')
cur =db.cursor()

cur.execute('''SELECT UserEmail FROM Users''')
Data = cur.fetchall()
db.commit()
print(Data)
print(type(Data[0][0]))

Check , _ = loadUiType('Check.ui')

class Check(QMainWindow ,Check):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Download()

    def Download(self):
        playlist = Playlist('https://www.youtube.com/playlist?list=PLflqtq8EOGALCJj-I8M7_dtrPh7_ZieDz')
        h = playlist.parse_links()
        VideoLink=[]
        for item in h:
            Link=("https://www.youtube.com" + item)
            Videos = YouTube(Link)
            
            VideoLink.append( (Link , Videos.title) )
        
        if VideoLink:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row, form in enumerate(VideoLink):
                for col , item in enumerate(form):
                    self.tableWidget.setItem(row , col ,QTableWidgetItem(item))
                    col += 1
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            
            
def main():
    app = QApplication(sys.argv)
    window = Check()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()

"""
Videos = YouTube('https://www.youtube.com/watch?v=_nDiPVoPN8E&list=RDI5wHdUT2a_s&index=24')


File_Size = Videos.streams.filter(file_extension='mp4',res='1080p').first().filesize
print(File_Size)
"""
if a:
    Videos.streams.get_by_itag(a[len(a) - 1]).download(filename='A')
File_Size += Videos.streams.filter(file_extension='mp4',res='1080p').first().filesize

A = [stream.itag for stream in Videos.streams.filter(file_extension='mp4',res='1080p').all()]
B = [stream for stream in Videos.streams.filter(file_extension='mp4',res='480p').all()]
C = [stream for stream in Videos.streams.filter(file_extension='mp4',res='720p').all()]
D = [stream for stream in Videos.streams.filter(file_extension='mp4',res='360p').all()]
print(File_Size)
if A:
    #Videos.streams.get_by_itag(A[len(A) - 1 ]).download(filename = 'A')
    pass

"""    