from module.mongo_student import Mongo_student
from module.mongo_attendant import Mongo_attendant
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox as ms


class DataStudent_controller:
    def __init__(self, Frame) -> None:
        self.Mongo_student = Mongo_student()
        self.Mongo_attendant = Mongo_attendant()
        self.Frame = Frame
        self.count = 1

        self.deleteIcon = Image.open("./src/image/remove.png")
        self.deleteIcon = self.deleteIcon.resize((30, 30), Image.ANTIALIAS)
        self.deleteIcon = ImageTk.PhotoImage(self.deleteIcon)

    def get_student(self):
        self.clear()
        data = self.Mongo_student.getAlldata()
        self.Create_Frame(data)

    def Remove(self, id):
        if ms.askyesno("ยืนยัน", "คุณต้องการที่จะลบข้อมูลหรือไม่"):
            status = self.Mongo_student.delete(id)
            if status.acknowledged:
                self.KillFile(id,'src/Train')
                status = self.Mongo_attendant.delete(id)
                if status.acknowledged :
                    self.KillFile(id,'src/Attendance')
                    self.get_student()
            else:
                ms.showerror("ไม่สามารถลบข้อมูลได้")

    def KillFile(self, id,path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            ID = int(os.path.split(imagePath)[-1].split(".")[0])
            if str(ID) == str(id):
                if os.path.exists(imagePath):
                    os.remove(imagePath)
                else:
                    print("The file does not exist")
    

    def Create_Frame(self, data):
        if len(data) != 0:
            for data in data:
                row = tk.Frame(self.Frame, bg='#40bcff')
                tk.Label(row, font=(
                    'mitr', 12), text=f"{self.count}. Student ID : {data['id']}\tName : {data['name']}\tClass : {data['classs']}", bg='#40bcff').pack(side='left')
                btn = tk.Button(row, text=' Remove', image=self.deleteIcon,
                                command=lambda: self.Remove(data['id']))
                btn.image = self.deleteIcon
                btn.config(relief="flat", bg="#4f4f4f", fg="white",
                           font=('mitr', 12), compound=tk.LEFT)
                btn.pack(side='right')
                row.pack(fill='x', pady=5)
                self.count += 1
        else:
            row = tk.Frame(self.Frame)
            label = tk.Label(row, text="ไม่พบข้อมูล",
                             font=('kanit', 16)).pack()
            row.pack(fill='x', pady=5)

    def clear(self):
        for child in self.Frame.winfo_children():
            child.destroy()
