from PIL import Image, ImageTk
from module.Staticmethod_controller import StaticMD
from module.SaveImage_view import SaveImage_view
from module.mongo_student import Mongo_student
from tkinter import messagebox as ms
import cv2
import threading


class TakeImages_controller:
    def __init__(self, Frame):

        self.Frame = Frame
        self.ID = self.Frame.entryIDText.get()
        self.name = self.Frame.entryNameText.get()
        self.clas = self.Frame.entryClassText.get()

        self.db = Mongo_student()
        length = self.db.findById(self.ID)

        if length == 0:
            StaticMD.check_haarcascadefile
            self.harcascadePath = "src/haarcascade_frontalface_default.xml"
            StaticMD.checkFolder('src/Train/')
            StaticMD.checkFolder('src/Student/')
            self.status = False
            status = self.checkData()
            if status['status']:
                self.db.add({
                    'id': str(self.ID),
                    'name': str(self.name),
                    'classs': str(self.clas)
                })
                self.webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                self.detector = cv2.CascadeClassifier(self.harcascadePath)
                self.width = int(self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.height = self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
                self.count = 0
                self.limit = StaticMD.numberOfPhotoShoots()
                self.saveImage = SaveImage_view(self.width)
                self.Run()
                self.status = True

            else:
                ms.showwarning('คำเตือน', status['text'])
        else:
            ms.showwarning('คำเตือน', 'มีรหัสนักเรียนอยู่ในฐานข้อมูลอยู่แล้ว')

    @staticmethod
    def EntryChange(Frame):
        if Frame.entryIDText.get() != '' and Frame.entryNameText.get() != '' and Frame.entryClassText.get() != '':
            Frame.text1.configure(fg='#00ab11')
        else:
            Frame.text1.configure(fg='#ffbf00')

    def changColorLabel(self):
        self.Frame.text2.configure(fg="#00ab11")

    def disabledBtn(self):
        self.Frame.btnTakeImages.configure(state='disabled')

    def saveImageFn(self):
        self.saveImage = SaveImage_view(self.width)
        self.video_loop()

    def UpdateDisplay(self, RGBimage, x, y, w, h):
        if self.count <= self.limit:
            if x != None:
                cv2.rectangle(RGBimage, (x, y), (x+w, y+h), (0, 255, 0), 2)
            current_image = Image.fromarray(RGBimage)
            imgtk = ImageTk.PhotoImage(image=current_image)
            self.saveImage.display.configure(image=imgtk)
            self.saveImage.display.image = imgtk

    def Imwrite(self, GRAYImage, x, y, w, h):
        cv2.imwrite(
            f'src/Train/{self.ID}.{str(self.count)}.jpg', GRAYImage[y:y + h, x:x + w])
        self.count += 1

    def Run(self):
        ok, frame = self.webcam.read()
        if ok:

            RGBimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            GRAYImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(GRAYImage, 1.05, 5)
            x, y, w, h = None, None, None, None

            for (x, y, w, h) in faces:
                imwrite = threading.Thread(
                    target=self.Imwrite, args=(GRAYImage, x, y, w, h))
                imwrite.start()

            updatedisplay = threading.Thread(
                target=self.UpdateDisplay, args=(RGBimage, x, y, w, h))
            updatedisplay.start()

        self.saveImage.updateprogress(self.count, self.limit)

        if self.count > self.limit:

            self.changColorLabel()
            self.disabledBtn()
            self.webcam.release()
            cv2.destroyAllWindows()
            self.saveImage.destroy()

        else:
            self.saveImage.after(30, self.Run)

    def checkData(self):
        status = True
        text = ''
        if self.ID == '' or self.name == '' or self.clas == '':
            status = False
            text = 'กรุณากรอกข้อมูลให้ครบ'
        elif not self.ID.isnumeric():
            status = False
            text = 'รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น'
        return {'status': status, 'text': text}
