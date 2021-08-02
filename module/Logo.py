import tkinter as tk
from PIL import Image,ImageTk
class Logo(tk.Frame):
    def __init__(self,windows,container = None) :
        tk.Frame.__init__(self,windows)
        self.configure(bg='red')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        

        image = Image.open("./src/image/logo.png")
        image = image.resize((453,155), Image.ANTIALIAS)
        image =  ImageTk.PhotoImage(image)

        self.logo = tk.Label(self,image=image,bg='green')
        self.logo.image =image
        self.logo.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.iconbitmap('src/image/icon.ico')
        self.title('School')
        self.width = 1000
        self.height = 600
        self.geometry(
            "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2), self.winfo_screenheight() // 2 - (self.height // 2)))   
        self.Logo = Logo(self)
        self.Logo.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
        