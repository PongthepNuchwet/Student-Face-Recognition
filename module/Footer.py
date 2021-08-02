import tkinter as tk

class Footer(tk.Frame):
    def __init__(self,windows,container = None) :
        tk.Frame.__init__(self,windows)
        self.configure(bg='#9e9e9e')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.t1 = tk.Label(self,text = '[ Developed by ]',bg="#787878")
        self.t2 = tk.Label(self,bg='#9e9e9e',text = '[ 1 ] Pongthep Nuchwet [ 2 ] Pongsagul Boonrub [ 3 ] Pakkamat Limjitsomboon  \t@2021')


        for widget in self.winfo_children():
            widget.config( fg="white", font=(
                'mitr', 8),compound=tk.LEFT)
            widget.pack(side='left',ipadx=10)
    



# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.iconbitmap('src/image/icon.ico')
#         self.title('School')
#         self.width = 1000
#         self.height = 600
#         self.geometry(
#             "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2), self.winfo_screenheight() // 2 - (self.height // 2)))   
#         self.Footer = Footer(self)
#         self.Footer.pack(side='bottom' ,fill='x')

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
        