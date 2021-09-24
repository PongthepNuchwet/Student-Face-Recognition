from tkinter import messagebox as ms
from module.Router import Router
from module.Footer import Footer
from module.MenuBar import Menubar
import threading
import tkinter as tk
import time
t0 = time.time()


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

        self.container = tk.Frame(self)

        self.Menubar = Menubar(self, self.container)
        self.Menubar.pack(side='top', fill='x')

        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.Footer = Footer(self)
        self.Footer.pack(side='bottom', fill='x')

        threading.Thread(target=self.Menubar.update_clock).start()

        self.Router = Router(self, self.container)
        self.Goto('startFrame')

    def Goto(self, Frame):
        self.Router.GoTo(Frame)

    def on_closing(self):
        if ms.askyesno("ปิดโปรแกรม", "คุณต้องการที่จะปิดโปรแกรมหรือไม่"):
            self.destroy()


if __name__ == "__main__":
    app = App()
    t1 = time.time()
    print(t1-t0)
    app.mainloop()
