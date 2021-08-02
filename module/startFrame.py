import tkinter as tk
from PIL import Image,ImageTk
class startFrame(tk.Frame):

    def __init__(self,windows, container) -> None:
        tk.Frame.__init__(self,container)
        
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=2)
        
        width = 100
        height = 100

        image = Image.open("./src/image/logo.png")
        image = image.resize((648,222), Image.ANTIALIAS)
        image =  ImageTk.PhotoImage(image)

        self.logo = tk.Label(self,image=image)
        self.logo.image =image
        self.logo.grid(column=0,columnspan=2,row=0,pady=20)

        iconDeep = Image.open("./src/image/detection.png")
        iconDeep = iconDeep.resize((width,height), Image.ANTIALIAS)
        iconDeep =  ImageTk.PhotoImage(iconDeep)

        recognition = Image.open("./src/image/recognition.png")
        recognition = recognition.resize((width,height), Image.ANTIALIAS)
        recognition =  ImageTk.PhotoImage(recognition)


        self.btnDeep = tk.Button(self,command= lambda : windows.Goto('FaceDetection_view'), text=' Face detection',relief='flat',compound=tk.LEFT,font=('mitr','20'),image = iconDeep)
        self.btnDeep.image = iconDeep
        self.btnDeep.bind("<Enter>", self.on_enter)
        self.btnDeep.bind("<Leave>", self.on_leave)
        self.btnDeep.grid(column=0,row=1,pady=50)

        self.btnRecog = tk.Button(self,command= lambda : windows.Goto('FaceRecognition_view'),text=' Face recognition ',relief='flat',compound=tk.LEFT,font=('mitr','20'),image = recognition)
        self.btnRecog.image = recognition
        self.btnRecog.bind("<Enter>", self.on_enter)
        self.btnRecog.bind("<Leave>", self.on_leave)
        self.btnRecog.grid(column=1,row=1,pady=50)
    
    def on_enter(e,widget):
        widget.widget['background'] = '#dbdbdb'

    def on_leave(e,widget):
        widget.widget['background'] = 'white'



