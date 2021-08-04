import tkinter as tk
from module.MenuBar import Menubar
from module.Footer import Footer
from module.Router import Router
from tkinter import messagebox as ms
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.iconbitmap('src/image/icon.ico')
        self.title('Student Face Recognition ')
        self.width = 1200
        self.height = 670
        self.geometry(
            "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2), self.winfo_screenheight() // 2 - (self.height // 2)))   
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        container = tk.Frame(self)

        self.Router = Router(self,container)
        self.Goto('About_view')

        self.Menubar = Menubar(self,container)
        self.Menubar.pack(side='top',fill='x')

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Footer = Footer(self)
        self.Footer.pack(side='bottom' ,fill='x')

        self.Menubar.update_clock()

    
    def Goto(self,Frame):
        self.Router.GoTo(Frame)

    def on_closing(self):
        if ms.askyesno("ปิดโปรแกรม", "คุณต้องการที่จะปิดโปรแกรมหรือไม่"):
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()