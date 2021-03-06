import tkinter as tk
from PIL import Image, ImageTk
import threading

from module.TakeImages_controller import TakeImages_controller
from module.TrainImages_controller import TrainImages_controller
from module.DataStudent_controller import DataStudent_controller


class Frame1(tk.LabelFrame):
    def __init__(self, windows, container):
        tk.LabelFrame.__init__(self, container)
        self.configure(text='ข้อมูล', font=('mitr', 16), fg='#40bcff')
        self.controller = DataStudent_controller(self)
        threading.Thread(target=self.controller.get_student).start()
        # self.controller.get_student()


class Frame2(tk.LabelFrame):
    def __init__(self, windows, container, Frame1):
        tk.LabelFrame.__init__(self, container)
        self.configure(text='เพื่มข้อมูล', font=('mitr', 16), fg='#40bcff')

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)

        font = ('mitr', 14)
        self.labelID = tk.Label(
            self, text='Student ID :', font=font, fg='#40bcff')
        self.labelID.grid(column=0, row=0, sticky='e',
                          padx=5, pady=5, ipadx=10, ipady=10)

        self.entryIDText = tk.StringVar()
        self.entryIDText.trace_add('write', self.EntryChange)
        self.entryID = tk.Entry(self, font=font, relief='flat',
                                bg='#40bcff', fg='#ffffff', textvariable=self.entryIDText)
        self.entryID.grid(column=1, row=0, sticky='w',
                          padx=5, pady=5, ipadx=5, ipady=5)

        self.labelName = tk.Label(self, text='Name :', font=font, fg='#40bcff')
        self.labelName.grid(column=0, row=1, sticky='e',
                            padx=5, pady=5, ipadx=10, ipady=10)

        self.entryNameText = tk.StringVar(name='1111')
        self.entryNameText.trace_add('write', self.EntryChange)
        self.entryName = tk.Entry(self, font=font, relief='flat',
                                  bg='#40bcff', fg='#ffffff', textvariable=self.entryNameText)
        self.entryName.grid(column=1, row=1, sticky='w',
                            padx=5, pady=5, ipadx=5, ipady=5)

        self.labelClass = tk.Label(
            self, text='Class :', font=font, fg='#40bcff')
        self.labelClass.grid(column=0, row=2, sticky='e',
                             padx=5, pady=5, ipadx=10, ipady=10)

        self.entryClassText = tk.StringVar()
        self.entryClassText.trace_add('write', self.EntryChange)
        self.entryClass = tk.Entry(self, font=font, relief='flat',
                                   bg='#40bcff', fg='#ffffff', textvariable=self.entryClassText)
        self.entryClass.grid(column=1, row=2, sticky='w',
                             padx=5, pady=5, ipadx=5, ipady=5)

        self.msFrame = tk.Frame(self)
        self.msFrame.grid(column=0, columnspan=2, row=3, pady=10, sticky='we')

        self.text1 = tk.Label(
            self.msFrame, text='[ 1 ] กรอกข้อมูลให้ครบ', font=('mitr', 14), fg='#ffbf00')
        self.text1.pack()
        self.text2 = tk.Label(
            self.msFrame, text='[ 2 ] คลิกที่ปุ่มถ่ายรูป', font=('mitr', 14), fg='#ffbf00')
        self.text2.pack()
        self.text3 = tk.Label(
            self.msFrame, text='[ 3 ] คลิกปุ่มบันทึก', font=('mitr', 14), fg='#ffbf00')
        self.text3.pack()

        self.labelStatus = tk.Label(self.msFrame)
        self.labelStatus.pack()

        width = 50
        height = 50
        iconWebcam = Image.open("./src/image/camera.png")
        iconWebcam = iconWebcam.resize((width, height), Image.ANTIALIAS)
        iconWebcam = ImageTk.PhotoImage(iconWebcam)

        icondisk = Image.open("./src/image/disk.png")
        icondisk = icondisk.resize((width, height), Image.ANTIALIAS)
        icondisk = ImageTk.PhotoImage(icondisk)

        fontbtn = ('mitr', 20)

        self.btnTakeImages = tk.Button(self, command=lambda: TakeImages_controller(
            self), compound=tk.LEFT, text=' ถ่ายรูป ', image=iconWebcam, font=fontbtn, relief='flat', bg="#4f4f4f", fg='#ffffff')
        self.btnTakeImages.image = iconWebcam
        self.btnTakeImages.grid(column=0, columnspan=2,
                                row=4, ipadx=20, pady=10)

        self.btnSave = tk.Button(self, command=lambda: TrainImages_controller(windows, self, Frame1), compound=tk.LEFT,
                                 text=' บันทึก ', image=icondisk, font=fontbtn, relief='flat', bg="#4f4f4f", fg='#ffffff')
        self.btnSave.image = icondisk
        self.btnSave.grid(column=0, columnspan=2, row=5, ipadx=20, pady=10)

    def EntryChange(self, *args):
        TakeImages_controller.EntryChange(self)


class Register_view(tk.Frame):

    def __init__(self, windows, container):
        tk.Frame.__init__(self, container)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.Frame1 = Frame1(windows=windows, container=self)
        self.Frame1.grid(column=0, row=0, sticky='nsew', padx=5, ipady=5)
        self.Frame2 = Frame2(
            windows=windows, container=self, Frame1=self.Frame1)
        self.Frame2.grid(column=1, row=0, padx=5, sticky='nsew')

    def EntryChange(self, *args):
        TakeImages_controller.EntryChange(self)
