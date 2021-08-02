import os
from tkinter import messagebox as ms
class StaticMD:

    @staticmethod
    def checkFolder(path):
        print(f"[Debug] checkFolder {path}")
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            print(f"Create a {path} folder")
            os.mkdir(dir)
    
    @staticmethod
    def check_haarcascadefile(window):
        print("[Debug] check_haarcascadefile")
        exists = os.path.isfile("src/haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            ms.showerror(title='Error', message='ไม่พบไฟล์ haarcascade_frontalface_default.xml')
            window.destroy()
