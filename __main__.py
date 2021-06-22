import subprocess
import os
import multiprocessing as mp
import pyautogui as py
import time
import datetime
import pdb
def pid_extractor(app): #returns a list of pid
    try:
        x= subprocess.check_output(["pidof "+app],shell=True)
        x = x.decode()
        x = x.split()
        return x
    except:
        print("Error")
def returnTime():
    TIME = datetime.datetime.now
    hour = TIME().hour
    minute = TIME().minute
    return hour,minute

class Zoom():
    def __init__(self):
        pass
    def start(self):
        self.instance = mp.Process(target=subprocess.call,args=("zoom",))
        self.instance.start()
    def stop(self):
        try:
            pid_zoom = pid_extractor("zoom")
            if pid_zoom==None:
                return
        except:
            print("Zoom already closed.")
            return
        if pid_zoom[0]=="256":
            return
        try:
            os.system("kill " + pid_zoom[0])
        except:
            print("Already closed.")
    def searchUntilPops(self,x):
        y=None
        while y==None:
            try:
                y = py.locateCenterOnScreen(x)
                py.click(x)
                print(y)
                break
            except:
                pass
    def joinClass(self,ID,password):
        HomeJoinButton = "HomeJoinButton.png"
        EnterMeetingColumn = "EnterMeetingColumn.png"
        IDJoinButton = "IDJoinButton.png"
        PassMeetingPasswordColumn = "PassMeetingPasswordColumn.png"
        PassJoinMeeting  = "PassJoinMeeting.png"
        JoinWithComputerAudio = "JoinWithComputerAudio.png"

        self.searchUntilPops(HomeJoinButton)
        self.searchUntilPops(EnterMeetingColumn)
        py.typewrite(ID, interval=0.1)
        time.sleep(3)
        self.searchUntilPops(IDJoinButton)
        self.searchUntilPops(PassMeetingPasswordColumn)
        py.typewrite(password,interval=0.1)
        time.sleep(3)
        self.searchUntilPops(PassJoinMeeting)
zoom = Zoom()



def joinClassAtSchduledTime(hour,minute,classs):
    h,m = returnTime()
    if hour==h and minute==m:
        zoom.start()
        zoom.joinClass(classs[0],classs[1])
        while True:
            h,m = returnTime()
            if datetime.timedelta(minutes=2)<=(datetime.timedelta(minutes=m)-datetime.timedelta(minutes=minute)):
                zoom.stop()
                break
while True:
    joinClassAtSchduledTime(12,00,classes["maths"])
    joinClassAtSchduledTime(11,00,classes['chemistry'])