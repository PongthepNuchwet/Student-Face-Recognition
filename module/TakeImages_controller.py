import tkinter as tk
from PIL import Image, ImageTk
from module.Staticmethod_controller import StaticMD 
from module.SaveImage_view import SaveImage_view
from module.FaceDetection_model import FaceDetection_model
from tkinter import messagebox as ms
import cv2
import threading


class TakeImages_controller:
    def __init__(self,Frame):
        self.Frame = Frame
        StaticMD.check_haarcascadefile
        self.harcascadePath = "src/haarcascade_frontalface_default.xml"
        StaticMD.checkFolder('src/Train/')
        StaticMD.checkFolder('src/Student/')
        self.status = False
        
        self.columns = ['SERIAL NO.','', 'ID', '', 'NAME','','CLASS']
        
        self.num = FaceDetection_model.CsvStudentData(0,self.columns)

        self.ID = self.Frame.entryIDText.get()
        self.name = self.Frame.entryNameText.get()
        self.clas = self.Frame.entryClassText.get()

        status = self.checkData()

        if status['status'] :
            self.webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            self.detector = cv2.CascadeClassifier(self.harcascadePath)
            self.width = int(self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.count = 0
            self.limit = 50

            self.saveImage = SaveImage_view(self.width)
            self.new = self.New()


            self.status = True

        else:
            ms.showwarning('คำเตือน',status['text'])

    @staticmethod
    def EntryChange(Frame):
        if Frame.entryIDText.get() != '' and Frame.entryNameText.get() != '' and Frame.entryClassText.get() != '' :
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

    def UpdateDisplay(self,RGBimage,x,y,w,h):
        if self.count <= self.limit :
            newIm = cv2.rectangle(RGBimage,(x,y),(x+w,y+h),(0, 255, 0),2)
            current_image = Image.fromarray(newIm)  
            imgtk = ImageTk.PhotoImage(image=current_image) 

            self.saveImage.display.configure(image=imgtk)
            self.saveImage.display.image = imgtk 

            del newIm
            del current_image
            del imgtk
    
    def Imwrite(self,GRAYImage,x,y,w,h):
        cv2.imwrite(f'src/Train/{self.name}.{str(self.num)}.{self.ID}.{str(self.count)}.jpg',GRAYImage[y:y + h, x:x + w])
        self.count += 1

    def New(self):
        ok, frame = self.webcam.read()  
        if ok:
            RGBimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            GRAYImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(GRAYImage, 1.05, 5)
            for (x,y,w,h) in faces :
                pass

                updatedisplay = threading.Thread(target=self.UpdateDisplay,args=(RGBimage,x,y,w,h))
                updatedisplay.start()

                imwrite = threading.Thread(target=self.Imwrite,args=(GRAYImage,x,y,w,h))
                imwrite.start()

        self.saveImage.updateprogress(self.count,self.limit)

        del ok
        del frame
        del RGBimage
        del GRAYImage
        del faces
        
        if self.count > self.limit :

            self.changColorLabel()
            self.disabledBtn()
            self.webcam.release()
            cv2.destroyAllWindows()
            self.saveImage.destroy()
            
            self.row  = [self.num,'',self.ID, '',self.name,'',self.clas]
            FaceDetection_model.AddCsvStudentData(self.row)
        else:
            self.saveImage.after(30, self.New)

        
    def video_loop(self):
        ok, frame = self.webcam.read()  
        if ok:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            faces = self.detector.detectMultiScale(cv2image, 1.05, 5)
            for (x,y,w,h) in faces :
                newIm = cv2.rectangle(cv2image,(x,y),(x+w,y+h),(0, 255, 0),2)

                self.current_image = Image.fromarray(newIm)  
                imgtk = ImageTk.PhotoImage(image=self.current_image) 
                self.saveImage.display.configure(image=imgtk)
                self.saveImage.display.image = imgtk 
        self.saveImage.updateprogress(self.count,self.limit)
        if self.count > self.limit :
            self.changColorLabel()
            self.disabledBtn()
            self.webcam.release()
            cv2.destroyAllWindows()
            self.saveImage.destroy()
        else:
            self.saveImage.after(30, self.video_loop)  

    def detectorSave(self):

        while(True):
            ret,img = self.webcam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, 1.05, 5)
            for (x,y,w,h) in faces :
                cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),2)
                self.count += 1
                cv2.imwrite(f'src/Train/{self.name}.{str(self.num)}.{self.ID}.{str(self.count)}.jpg',gray[y:y + h, x:x + w])
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif self.count > self.limit:
                break

        self.row  = [self.num,'',self.ID, '',self.name,'',self.clas]
        FaceDetection_model.AddCsvStudentData(self.row)

    def checkData(self):
        status = True 
        text = ''
        if self.ID == '' or self.name == '' or self.clas == '':
            status = False
            text = 'กรุณากรอกข้อมูลให้ครบ'
        elif not self.ID.isnumeric():
            status = False
            text = 'รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น'
        elif not self.name.isalpha() :
            status = False
            text = 'ชื่อต้องเป็นตัวอักษรเท่านั้น'
        return {'status':status,'text':text}