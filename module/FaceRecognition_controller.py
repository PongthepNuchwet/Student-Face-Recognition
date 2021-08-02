import tkinter as tk
from PIL import Image, ImageTk
from module.Staticmethod_controller import StaticMD 
from module.FaceRecognition_model import FaceRecognition_model
from module.LineNotify import LineNotify
from tkinter import messagebox as ms
import cv2
import threading
import os
import pandas as pd
import datetime
from playsound import playsound

class FaceRecognition_controller:
    def __init__(self,windows,Frame):
        self.Frame = Frame
        self.windows = windows

        self.LineNotify = LineNotify()

        self.recognizer =cv2.face.LBPHFaceRecognizer_create()
        harcascadePath = "src/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(harcascadePath);

        self.sound = './src/sound/notification.wav'
        self.statusC = False

        self.webcam = None
        self.font = None
        self.df = None
        self.After = None

        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y")

        threading.Thread(target=self.Attendance,args=(date,False)).start()
        
        
    def disableBtn(self):
        self.windows.Menubar.btn1["state"] = "disabled"
        self.windows.Menubar.btn2["state"] = "disabled"
        self.windows.Menubar.btn3["state"] = "disabled"
        self.windows.Menubar.btn4["state"] = "disabled"
        self.windows.Menubar.btn5["state"] = "disabled"

    def unDisableBtn(self):
        self.windows.Menubar.btn1["state"] = "normal"
        self.windows.Menubar.btn2["state"] = "normal"
        self.windows.Menubar.btn3["state"] = "normal"
        self.windows.Menubar.btn4["state"] = "normal"
        self.windows.Menubar.btn5["state"] = "normal"


    def Start(self):


        print("[Debug] Start")
        self.statusC = True

        StaticMD.check_haarcascadefile
        StaticMD.checkFolder('src/Student/')
        StaticMD.checkFolder('src/Attendance/')

        exists = os.path.isfile("src/dataset\Trainner.yml")
        if exists :
            print("[Debug] พบไฟล์ Trainner.yml")
            self.recognizer.read("src/dataset\Trainner.yml")
        else:
            print("[Debug] ไม่พบไฟล์ Trainner.yml")
            ms.showerror('คำเตือน','กรุณาบันทึกข้อมูลก่อนเริ่มการทำงาน')
            return
        
        self.webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        exists2 = os.path.isfile("src/Student/data.csv")
        if exists2:
            print("[Debug] พบไฟล์ data.csv")
            self.df = pd.read_csv("src/Student/data.csv")
        else:
            print("[Debug] ไม่พบไฟล์ data.csv")
            ms.showerror('คำเตือน','กรุณาบันทึกข้อมูลก่อนเริ่มการทำงาน')
            self.webcam.release()
            cv2.destroyAllWindows()

        threading.Thread(target=self.disableBtn).start()
        self.Run()
        

    def Stop(self):
        print("[Debug] Stop")
        if self.webcam != None :
            self.statusC = False
            self.Frame.Frame1.resetDisplay()
            self.windows.after_cancel(self.After)
            self.webcam.release()
            cv2.destroyAllWindows()
            self.unDisableBtn()
        
            self.Frame.Frame1.resetDisplay()
        else:
            ms.showwarning('คำเตือน','กรุณาคลิกปุ่ม Start ก่อน')


    def UpdateDisplay(self,RGBimage,name = None,x = None,y = None,w = None,h = None):
        
        print("[Debug] UpdateDisplay")
        if x != None :
            cv2.rectangle(RGBimage,(x,y),(x+w,y+h),(0, 255, 0),2)
            cv2.putText(RGBimage, str(name), (x, y + h), self.font, 1, (0, 251, 255), 2)
        current_image = Image.fromarray(RGBimage)  
        imgtk = ImageTk.PhotoImage(image=current_image) 
        if self.statusC :
            self.Frame.Frame1.video.configure(image=imgtk)
            self.Frame.Frame1.video.image = imgtk 


    def saveData(self,frame,id,name,clas,date,time,time2,x,y,w,h):

        StaticMD.checkFolder('src/Attendance/image/')
        status = FaceRecognition_model.ChackData(str(id),date)
        
        if status != True:
            url = f"src\Attendance\image\T{time2}.jpg"
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2.imwrite(url,frame)
            attendance = [id,'',url,'',name,'',clas,'',date,'',time]
            FaceRecognition_model.AddCsvAttendanceData(date,attendance)
            threading.Thread(target=self.LineNotify.Post(url,f'{name} มาถึงโรงเรียนแล้ว'))
            self.Attendance(date,True)
        


    def Attendance(self,date,sound):
        data = FaceRecognition_model.GetCsvAttendanceData(date)
        if data != '':
            self.Frame.Frame2.clearAttendance()
            for i in data :
                self.Frame.Frame2.creatwidget(i['image'],i['Name'],i['Id'],i['Class'],i['Date'],i['Time'])
                if sound :
                    playsound(self.sound)


    def Run(self):
        print("[Debug] Run")
        ret, frame = self.webcam.read()
        GRAYImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        RGBimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        faces = self.faceCascade.detectMultiScale(GRAYImage, 1.2, 5)
        name = None
        x,y,w,h = None,None,None,None
        for (x, y, w, h) in faces:
            print("[Debug] พบใบหน้า")
            serial, conf = self.recognizer.predict(GRAYImage[y:y + h, x:x + w])
            if (conf < 50): 
                print("[Debug] ใบหน้าเหมือน")

                now = datetime.datetime.now()
                time = now.strftime("%H:%M:%S")
                time2 = now.strftime("%H-%M-%S-%f")
                date = now.strftime("%d-%m-%Y")

                id = self.df.loc[self.df['SERIAL NO.'] == serial]['ID'].values
                id = str(id)
                id = id[1:-1]

                name = self.df.loc[self.df['SERIAL NO.'] == serial]['NAME'].values
                name = str(name)
                name = name[1:-1]

                clas = self.df.loc[self.df['SERIAL NO.'] == serial]['CLASS'].values
                clas = str(clas)
                clas = clas[1:-1]

                # cv2.imwrite(f'src/{name}.{time}.jpg',frame[y:y + h, x:x + w])

                CreatFrame = threading.Thread(target=self.saveData,args=(frame,id,name,clas,date,time,time2,x,y,w,h) )
                CreatFrame.start()
            else:
                Id = 'Unknown'
                name = 'Unknown'
        updatedisplay = threading.Thread(target=self.UpdateDisplay,args=(RGBimage,name,x,y,w,h))
        updatedisplay.start()

        self.After = self.windows.after(30,self.Run)

