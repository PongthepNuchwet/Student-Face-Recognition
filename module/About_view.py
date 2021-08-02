import tkinter as tk

class About_view(tk.Frame):

    def __init__(self, windows,container):
        tk.Frame.__init__(self,container)

        label = tk.Label(self,text='About_view')
        label.pack()