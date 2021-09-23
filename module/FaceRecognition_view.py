import tkinter as tk
from tkinter import ttk
from module.TrainImages_controller import TrainImages_controller
from module.FaceRecognition_controller import FaceRecognition_controller
from PIL import Image,ImageTk




class Frame1(tk.Frame):
    def __init__(self, windows,container):
        tk.Frame.__init__(self,container)
        self.configure(bg='#dbdbdb')
        
        self.displayIcon = Image.open("./src/image/btn.png")
        self.displayIcon = self.displayIcon.resize((640,480), Image.ANTIALIAS)
        self.displayIcon =  ImageTk.PhotoImage(self.displayIcon)

        self.cameraIcon = Image.open("./src/image/camera.png")
        self.cameraIcon = self.cameraIcon.resize((40,40), Image.ANTIALIAS)
        self.cameraIcon =  ImageTk.PhotoImage(self.cameraIcon)

        self.titleFrame = tk.Frame(self)
        self.titleFrame.configure(bg='#40bcff')
        self.titleFrame.pack(fill='x',expand=True)

        self.fbottom = tk.Frame(self.titleFrame)
        self.fbottom.configure(bg='#40bcff')
        self.fbottom.pack(side='bottom')

        self.labelTitle = tk.Label(self.fbottom,text=' Web Came',compound=tk.LEFT,image=self.cameraIcon)
        self.labelTitle.configure(bg='#40bcff',fg="white",font=('mitr',12))
        self.labelTitle.image = self.cameraIcon
        self.labelTitle.pack()
        

        self.video = tk.Label(self,image=self.displayIcon)
        self.video.image = self.displayIcon
        self.video.pack()

        self.bottomFrame = tk.Frame(self)
        self.bottomFrame.configure(bg='#40bcff')
        self.bottomFrame.pack(fill='x',expand=True)

        self.menu = tk.Frame(self.bottomFrame)
        self.menu.configure(bg='#40bcff')
        self.menu.pack(side='bottom')
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_columnconfigure(1, weight=1)

        width = 30
        height = 30

        playIcon = Image.open("./src/image/play.png")
        playIcon = playIcon.resize((width,height), Image.ANTIALIAS)
        playIcon =  ImageTk.PhotoImage(playIcon)

        stopIcon = Image.open("./src/image/stop.png")
        stopIcon = stopIcon.resize((width,height), Image.ANTIALIAS)
        stopIcon =  ImageTk.PhotoImage(stopIcon)

        self.btnStart = tk.Button(self.menu,text=" Start",image=playIcon, command= lambda : container.Start())
        self.btnStart.config(relief="flat", bg="#40bcff", fg="white", font=(
                'mitr', 10),compound=tk.LEFT)
        self.btnStart.image = playIcon
        self.btnStart.bind("<Enter>", self.on_enter)
        self.btnStart.bind("<Leave>", self.on_leave)
        
        
        self.btnStop = tk.Button(self.menu,text=" Stop",image=stopIcon, command= lambda : container.Stop())
        self.btnStop.config(relief="flat", bg="#40bcff", fg="white", font=(
                'mitr', 10),compound=tk.LEFT)
        self.btnStop.image = stopIcon
        self.btnStop.bind("<Enter>", self.on_enter)
        self.btnStop.bind("<Leave>", self.on_leave)

        self.btnStart.grid(column=0,row=0,sticky='e',ipady=5,ipadx=5)
        self.btnStop.grid(column=1,row=0,sticky='w',ipady=5,ipadx=5)


    def resetDisplay(self):
        self.video.configure(image=self.displayIcon)
        self.video.image = self.displayIcon


    def on_enter(e,widget):
        widget.widget['background'] = '#19adfc'

    def on_leave(e,widget):
        widget.widget['background'] = '#40bcff'

    



class Frame2(tk.Frame):
    def __init__(self, windows,container):
        tk.LabelFrame.__init__(self,container)
        # self.configure(text='เพื่มข้อมูล',font= ('mitr',12),fg='#40bcff')
        self.cardIcon = Image.open("./src/image/card.png")
        self.cardIcon = self.cardIcon.resize((40,40), Image.ANTIALIAS)
        self.cardIcon =  ImageTk.PhotoImage(self.cardIcon)

        self.titleFrame = tk.Frame(self)
        self.titleFrame.configure(bg='#40bcff')
        self.titleFrame.pack(fill='x',side='top')

        self.fbottom = tk.Frame(self.titleFrame)
        self.fbottom.configure(bg='#40bcff')
        self.fbottom.pack(side='bottom')

        self.labelTitle = tk.Label(self.fbottom,text=' Attendance',compound=tk.LEFT,image=self.cardIcon)
        self.labelTitle.configure(bg='#40bcff',fg="white",font=('mitr',12))
        self.labelTitle.image = self.cardIcon
        self.labelTitle.pack()

        mycanvas = tk.Canvas(self)
        mycanvas.pack(side='left',fill='both',expand=True)

        yScroreBar = ttk.Scrollbar(self,orient='vertical',command= mycanvas.yview)
        yScroreBar.pack(side='right',fill='y')

        mycanvas.configure(yscrollcommand=yScroreBar.set)

        mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion= mycanvas.bbox('all')))

        self.myFrame = tk.Frame(mycanvas)
        mycanvas.create_window((0,0),window=self.myFrame,anchor='nw')
        

        # self.creatwidget('./src/image/demo.png','Pongthep Nuchwet','6310301004','6/7','26/7/2564','18:00')
      
       
    def clearAttendance(self):
        widget = self.myFrame.winfo_children()
        for i in widget :
            i.destroy()
    
    def notFound(self):
        row =  tk.Frame(self.myFrame)
        label = tk.Label(row,text="\t\t\tไม่พบข้อมูล",font=('kanit',12)).pack()
        row.pack(fill='x',pady=5)


    def creatwidget(self,img,name,id,clas,date,time):
        current_image = Image.open(img)
        current_image = current_image.resize((160,120),Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image=current_image) 
        self.widget = tk.Label(self.myFrame,image=image,compound=tk.LEFT ,text=f'   Name : {name}\n   Studen id : {id} Class : {clas}\n   Date : {date} Time : {time}')
 
        self.widget.configure(font=('kanit',12),justify='left',bg='#d1d1d1',fg='#000000')
        self.widget.image = image
        self.widget.pack(fill='x',pady=5 ,side='top',ipadx=5,ipady=5)

    def loadImage(self,url):
        width = 100 
        height = 100
        iconWebcam = Image.open(url)
        iconWebcam = iconWebcam.resize((width,height), Image.ANTIALIAS)
        iconWebcam =  ImageTk.PhotoImage(iconWebcam)
        return iconWebcam
        

class FaceRecognition_view(tk.Frame):

    def __init__(self, windows,container):

        tk.Frame.__init__(self,container)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)



        self.Frame1 = Frame1(windows,self)
        self.Frame1.grid(column=0,row=0,padx=5,pady=5,sticky='nsew')

        self.Frame2 = Frame2(windows,self)
        self.Frame2.grid(column=1,row=0,padx=5,pady=5,sticky='nsew')

        self.control = FaceRecognition_controller(windows,self)

    def Start(self):
        self.control.Start()

    def Stop(self):
        self.control.Stop()

    
