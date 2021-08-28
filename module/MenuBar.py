import tkinter as tk
from PIL import Image,ImageTk
import datetime

class Menubar(tk.Frame):
    def __init__(self,windows,container) :
        tk.Frame.__init__(self,windows)
        self.windows = windows
        self.configure(bg='#dbdbdb')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        width = 35
        height = 35

        homeIcon = Image.open("./src/image/home.png")
        homeIcon = homeIcon.resize((width,height), Image.ANTIALIAS)
        homeIcon =  ImageTk.PhotoImage(homeIcon)

        detIcon = Image.open("./src/image/register.png")
        detIcon = detIcon.resize((width,height), Image.ANTIALIAS)
        detIcon =  ImageTk.PhotoImage(detIcon)

        recIcon = Image.open("./src/image/recognition.png")
        recIcon = recIcon.resize((width,height), Image.ANTIALIAS)
        recIcon =  ImageTk.PhotoImage(recIcon)

        aboutIcon = Image.open("./src/image/about.png")
        aboutIcon = aboutIcon.resize((width,height), Image.ANTIALIAS)
        aboutIcon =  ImageTk.PhotoImage(aboutIcon)

        closeIcon = Image.open("./src/image/close.png")
        closeIcon = closeIcon.resize((width,height), Image.ANTIALIAS)
        closeIcon =  ImageTk.PhotoImage(closeIcon)

        timeIcon = Image.open("./src/image/time.png")
        timeIcon = timeIcon.resize((30,30), Image.ANTIALIAS)
        timeIcon =  ImageTk.PhotoImage(timeIcon)

        calendarIcon = Image.open("./src/image/calendar.png")
        calendarIcon = calendarIcon.resize((30,30), Image.ANTIALIAS)
        calendarIcon =  ImageTk.PhotoImage(calendarIcon)

        self.btn1 = tk.Button(self,text=' Home',image=homeIcon,command = lambda:  self.windows.Goto('startFrame'))
        self.btn1.image = homeIcon 
        
        self.btn2 = tk.Button(self,text=' Register',image=detIcon,command = lambda: self.windows.Goto('FaceDetection_view'))
        self.btn2.image = detIcon 
        
        self.btn3 = tk.Button(self,text=' Face Recognition',image=recIcon,command =  lambda: self.windows.Goto('FaceRecognition_view'))
        self.btn3.image = recIcon 

        self.btn4 = tk.Button(self,text=' About',image=aboutIcon,command = lambda:  self.windows.Goto('About_view'))
        self.btn4.image = aboutIcon 

        self.btn5 = tk.Button(self,text=' Exit',image=closeIcon,command=self.windows.on_closing)
        self.btn5.image = closeIcon

         

        for widget in self.winfo_children():
            widget.config(relief="flat", bg="#9e9e9e", fg="white", font=(
                'mitr', 12),compound=tk.LEFT)
            widget.pack(side='left',ipadx=10)
            widget.bind("<Enter>", self.on_enter)
            widget.bind("<Leave>", self.on_leave)

        self.LabelTime = tk.Label(self,text=' 17:32',compound=tk.LEFT,image=timeIcon)
        self.LabelTime.configure(bg='#dbdbdb',font=('RobotoMono',10,'bold'))
        self.LabelTime.image = timeIcon
        self.LabelTime.pack(side='right')

        self.Labelcalendar = tk.Label(self,text=' 25/7/564',compound=tk.LEFT,image=calendarIcon)
        self.Labelcalendar.configure(bg='#dbdbdb',font=('RobotoMono',10,'bold'))
        self.Labelcalendar.image = calendarIcon
        self.Labelcalendar.pack(side='right')

        
    
    def on_enter(e,widget):
        widget.widget['background'] = '#808080'

    def on_leave(e,widget):
        widget.widget['background'] = '#9e9e9e'

    def update_clock(self):

        now = datetime.datetime.now()
        time = now.strftime(" %H:%M:%S")
        date = now.strftime(" %d/%m/%Y")
       
        self.LabelTime.configure(text= time)
        self.Labelcalendar.configure(text= date)
        
        self.windows.after(100, self.update_clock)



# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.iconbitmap('src/image/icon.ico')
#         self.title('School')
#         self.width = 1000
#         self.height = 600
#         self.geometry(
#             "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2), self.winfo_screenheight() // 2 - (self.height // 2)))   
#         self.Menubar = Menubar(self)
#         self.Menubar.pack(side='top',fill='x')

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
        