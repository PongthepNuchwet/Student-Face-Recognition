from PIL import Image, ImageTk
from module.Staticmethod_controller import StaticMD
from module.LineNotify import LineNotify
from module.mongo_attendant import Mongo_attendant
from module.mongo_student import Mongo_student
from tkinter import messagebox as ms
import cv2
import threading
import os
import datetime
from playsound import playsound


class FaceRecognition_controller:
    def __init__(self, windows, Frame):
        self.Frame = Frame
        self.windows = windows

        self.n = 0
        self.tmp = []

        self.LineNotify = LineNotify()
        self.Mongo_attendant = Mongo_attendant()
        self.Mongo_student = Mongo_student()

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        harcascadePath = "src/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(harcascadePath)

        self.sound = './src/sound/notification.wav'
        self.statusC = False

        self.webcam = None
        self.font = None
        self.df = None
        self.After = None

        now = datetime.datetime.now()
        self.date = now.strftime("%d-%m-%Y")

        threading.Thread(target=self.Attendance, args=('0')).start()

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

    def save_attendance(self, id, name, classs, date, time, time2, image):
        StaticMD.checkFolder('src/Attendance/')
        status = self.Mongo_attendant.getLen(id)

        if status < 1:
            url = f"src\Attendance\{id}.{time2}.jpg"
            cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
            cv2.imwrite(url, image)
            data = {
                'studentId': str(id),
                'name': str(name),
                'classs': str(classs),
                'date': str(date),
                'time': str(time),
                'image': str(url)
            }
            self.Mongo_attendant.add(data)
            self.LineNotify.Post(
                url, f'{str(name)} มาถึงโรงเรียนแล้ว \n วันที่ {str(date)} เวลา {str(time)}')
            self.Attendance('1')

    def find_student(self, id):
        return self.Mongo_student.find_all(id)

    def Run(self):
        ret, frame = self.webcam.read()
        GRAYImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        RGBimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        faces = self.faceCascade.detectMultiScale(GRAYImage, 1.2, 5)
        name = None
        x, y, w, h = None, None, None, None
        for (x, y, w, h) in faces:
            studenID, conf = self.recognizer.predict(
                GRAYImage[y:y + h, x:x + w])
            if (conf < 50):
                now = datetime.datetime.now()
                time = now.strftime("%H:%M:%S")
                time2 = now.strftime("%H-%M-%S-%f")
                date = now.strftime("%d-%m-%Y")
                data = self.find_student(str(studenID))

                if len(data) > 0 and data[0]['id'] not in self.tmp:
                    self.tmp.append(data[0]['id'])
                    threading.Thread(target=self.save_attendance, args=(
                        data[0]['id'], data[0]['name'], data[0]['classs'], date, time, time2, frame)).start()

            else:
                name = 'Unknown'
        updatedisplay = threading.Thread(
            target=self.UpdateDisplay, args=(RGBimage, name, x, y, w, h))
        updatedisplay.start()
        self.After = self.windows.after(30, self.Run)

    def Start(self):
        self.statusC = True

        StaticMD.check_haarcascadefile
        StaticMD.checkFolder('src/Attendance/')

        exists = os.path.isfile("src/model\Trainner.yml")
        if exists:
            count = len(self.Mongo_student.getAlldata())
            if count > 0:
                self.recognizer.read("src/model\Trainner.yml")
                self.webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                self.font = cv2.FONT_HERSHEY_SIMPLEX
                threading.Thread(target=self.disableBtn).start()
                self.Run()
            else:
                ms.showwarning('คำเตือน', 'กรุณาบันทึกข้อมูลก่อนเริ่มการทำงาน')
        else:
            ms.showerror('คำเตือน', 'กรุณาบันทึกข้อมูลก่อนเริ่มการทำงาน')

    def Stop(self):

        if self.webcam != None:
            self.statusC = False
            self.Frame.Frame1.resetDisplay()
            self.windows.after_cancel(self.After)
            self.webcam.release()
            cv2.destroyAllWindows()
            self.unDisableBtn()

            self.Frame.Frame1.resetDisplay()
        else:
            ms.showwarning('คำเตือน', 'กรุณาคลิกปุ่ม Start ก่อน')

    def UpdateDisplay(self, RGBimage, name=None, x=None, y=None, w=None, h=None):

        if x != None:
            cv2.rectangle(RGBimage, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(RGBimage, str(name), (x, y + h),
                        self.font, 1, (0, 251, 255), 2)
        current_image = Image.fromarray(RGBimage)
        imgtk = ImageTk.PhotoImage(image=current_image)
        if self.statusC:
            self.Frame.Frame1.video.configure(image=imgtk)
            self.Frame.Frame1.video.image = imgtk

    def Attendance(self, sound):
        data = self.Mongo_attendant.find_all(self.date)
        self.Frame.Frame2.clearAttendance()
        if len(data) != 0:
            for i in data:
                self.Frame.Frame2.creatwidget(
                    i['image'], i['name'], i['studentId'], i['classs'], i['date'], i['time'])
                if sound == '1':
                    playsound(self.sound)
        else:
            self.Frame.Frame2.notFound()
