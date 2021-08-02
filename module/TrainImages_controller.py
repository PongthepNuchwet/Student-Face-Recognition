import os
from PIL import Image
from module.Staticmethod_controller import StaticMD 
from module.GetDataInCSV import GetDataInCSV
from tkinter import messagebox as ms
import cv2
import numpy as np
import gc

class TrainImages_controller:
    def __init__(self,windows,Frame,Frame1) -> None:
        StaticMD.check_haarcascadefile(windows)
        StaticMD.checkFolder('src/dataset/')
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        faces, ID = self.getImagesAndLabels()
        try:  
            recognizer.train(faces, np.array(ID))
        except:
            ms.showwarning(title='คำเตือน', message='กรุณาถ่ายรูปก่อนบันทึก')
            return
        recognizer.save("src/dataset\Trainner.yml")
        GetDataInCSV(Frame1)
        res = "บันทึกข้อมูลสำเร็จ"
        Frame.labelStatus.configure(text=res,fg='#00ab11',font=('mitr',16))
        Frame.btnTakeImages.configure(state='normal')
        Frame.entryID.delete(0, 'end')
        Frame.entryName.delete(0, 'end')
        Frame.entryClass.delete(0, 'end')
        Frame.text1.configure(fg='#ffbf00')
        Frame.text2.configure(fg='#ffbf00')
        Frame.text3.configure(fg='#ffbf00')

    def getImagesAndLabels(self,path = 'src/Train'):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        Ids = []

        for imagePath in imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(imageNp)
            Ids.append(ID)

        return faces, Ids