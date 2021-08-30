import os
from PIL import Image
from module.Staticmethod_controller import StaticMD 
from module.DataStudent_controller import DataStudent_controller
from tkinter import messagebox as ms
import threading
import cv2
import numpy as np

class TrainImages_controller:
    def __init__(self,windows,Frame,Frame1) -> None:
        StaticMD.check_haarcascadefile(windows)
        StaticMD.checkFolder('src/dataset/')
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        faces, ids = self.getImagesAndLabels()
        try:  
            recognizer.train(faces, np.array(ids))
        except:
            ms.showwarning(title='คำเตือน', message='กรุณาถ่ายรูปก่อนบันทึก')
            return
        recognizer.save("src/dataset\Trainner.yml")
        res = "บันทึกข้อมูลสำเร็จ"
        self.Frame = Frame
        self.Frame.labelStatus.configure(text=res,fg='#00ab11',font=('mitr',16))
        self.Frame.btnTakeImages.configure(state='normal')
        self.Frame.entryID.delete(0, 'end')
        self.Frame.entryName.delete(0, 'end')
        self.Frame.entryClass.delete(0, 'end')
        self.Frame.text1.configure(fg='#ffbf00')
        self.Frame.text2.configure(fg='#ffbf00')
        self.Frame.text3.configure(fg='#ffbf00')

        self.controller = DataStudent_controller(Frame1)
        self.controller.get_student()

        threading.Timer(5.0,self.resetLabelStatus).start()
    
    def resetLabelStatus(self):
        self.Frame.labelStatus.configure(text='',fg='#00ab11',font=(1))


    def getImagesAndLabels(self,path = 'src/Train'):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        Ids = []

        for imagePath in imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split(".")[0])
            faces.append(imageNp)
            Ids.append(ID)

        return faces, Ids
