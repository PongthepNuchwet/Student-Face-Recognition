import tkinter as tk
from tkinter import ttk

class SaveImage_view(tk.Toplevel):

    def __init__(self,width):
        super().__init__()

        self.width = width
        self.height = 500
        self.geometry(
            "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2), self.winfo_screenheight() // 2 - (self.height // 2)))   
        self.resizable(False,False)
        self.title('Save Image')

        self.ms = tk.Label(self,font= ('mitr',18),text='ระบบกำลังบันทึกรูปภาพ (0/50) | 0%')
        self.ms.pack(fill='x')
        self.ms2 = tk.Label(self,font= ('mitr',12),text='กรุณาขยับใบหน้า ซ้านขวาอย่างช้าๆ')
        self.ms2.pack(fill='x')

        self.progressbar = ttk.Progressbar(
            self,
            orient='horizontal',
            mode='determinate',
            length=100
        )
        self.progressbar.pack(fill = 'x',padx=10,pady=10)


        self.display = tk.Label(self)
        self.display.pack()

    def updateprogress(self,n,l):
        tmp = (n*100) // l
        self.progressbar['value'] = tmp
        self.ms.configure(text=f"ระบบกำลังบันทึกรูปภาพ ({n}/50) | {tmp}%")




        
