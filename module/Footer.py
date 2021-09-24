import tkinter as tk


class Footer(tk.Frame):
    def __init__(self, windows, container=None):
        tk.Frame.__init__(self, windows)
        self.configure(bg='#9e9e9e')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.t1 = tk.Label(self, text='[ Developed by ]', bg="#787878")
        self.t2 = tk.Label(
            self, bg='#9e9e9e', text='[ 1 ] Pongthep Nuchwet [ 2 ] Pongsagul Boonrub [ 3 ] Pakkamat Limjitsomboon  \t@2021')

        for widget in self.winfo_children():
            widget.config(fg="white", font=(
                'mitr', 8), compound=tk.LEFT)
            widget.pack(side='left', ipadx=10)
