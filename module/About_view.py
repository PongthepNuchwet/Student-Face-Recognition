import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image,ImageTk

class About_view(tk.Frame):

    def __str__(self) -> str:
        return 'About'

    def __init__(self, windows,container):
        tk.Frame.__init__(self,container)


        self.H1 = ("mitr",28)
        self.H2 = ("kanit",20,'bold')
        self.H2Color = '#d62825'
        self.bg = '#323232'
        self.H3 = ("kanit",16)
        
        self.FrameA = tk.Frame(self)
        self.FrameA.pack()
        self.FrameB = tk.Frame(self,bg=self.bg)
        self.FrameB.pack(fill='both',expand=True)

        self.FrameB.columnconfigure(0, weight=1)
        self.FrameB.columnconfigure(1, weight=1)
        self.FrameB.columnconfigure(2, weight=1)
        self.FrameB.columnconfigure(3, weight=1)
        self.FrameB.columnconfigure(4, weight=1)

        label0 = tk.Label(self.FrameA, text="ABOUT", font=self.H1)
        label0.pack()

        label01 = tk.Label(self.FrameA,font=('kanit',14),text='Student face recognition เป็นระบบลงเวลามาโรงเรียนของนักเรียน\nและแจ้งเตือนไปยังโทรศัพท์มือถือของผู้ปกครอง ผ่านโปรแกรมไลน์ ( LINE Application )').pack()
        label02 = tk.Label(self.FrameB,font=self.H1,text='REFERENCE',fg='white',bg=self.bg).grid(columnspan=5, row=2,sticky='we')

        sFrame1 = Frame(self.FrameB)
        sFrame2 = Frame(self.FrameB)
        


        self.separator1 = ttk.Separator(sFrame1, orient='vertical')
        self.separator2 = ttk.Separator(sFrame2, orient='vertical')

        # tk.Label(sFrame2,text='5555').pack(fill='y',side='top')

        labelFrame1 = tk.Frame(self.FrameB,bg=self.bg)
        labelFrame1.columnconfigure(0, weight=1)
        labelFrame1.columnconfigure(1, weight=1)


        label1 = tk.Label(labelFrame1, text="Library", font=self.H2 ,fg=self.H2Color,bg=self.bg)
        label1.grid(columnspan=2, row=0, padx=5, pady=5)
        label2_1 = tk.Label(labelFrame1, text="- tkinter", font=self.H3,fg='white',bg=self.bg)
        label2_1.grid(column=0, row=1, padx=5, pady=5,sticky='w')
        label2_2 = tk.Label(labelFrame1, text="- csv", font=self.H3,fg='white',bg=self.bg)
        label2_2.grid(column=1, row=1, padx=5, pady=5,sticky='w')
        label3_1 = tk.Label(labelFrame1, text="- os", font=self.H3,fg='white',bg=self.bg)
        label3_1.grid(column=0, row=2, padx=5, pady=5,sticky='w')
        label3_2 = tk.Label(labelFrame1, text="- PIL", font=self.H3,fg='white',bg=self.bg)
        label3_2.grid(column=1, row=2, padx=5, pady=5,sticky='w')
        label4_1 = tk.Label(labelFrame1, text="- cv2", font=self.H3,fg='white',bg=self.bg)
        label4_1.grid(column=0, row=3, padx=5, pady=5,sticky='w')
        label4_2 = tk.Label(labelFrame1, text="- threading", font=self.H3,fg='white',bg=self.bg)
        label4_2.grid(column=1, row=3, padx=5, pady=5,sticky='w')
        label5_1 = tk.Label(labelFrame1, text="- pandas", font=self.H3,fg='white',bg=self.bg)
        label5_1.grid(column=0, row=4, padx=5, pady=5,sticky='w')
        label5_2 = tk.Label(labelFrame1, text="- detetime", font=self.H3,fg='white',bg=self.bg)
        label5_2.grid(column=1, row=4, padx=5, pady=5,sticky='w')
        label6_1 = tk.Label(labelFrame1, text="- playsound", font=self.H3,fg='white',bg=self.bg)
        label6_1.grid(column=0, row=5, padx=5, pady=5,sticky='w')
        label6_2 = tk.Label(labelFrame1, text="- requests", font=self.H3,fg='white',bg=self.bg)
        label6_2.grid(column=1, row=5, padx=5, pady=5,sticky='w')
        label7_1 = tk.Label(labelFrame1, text="- numpy", font=self.H3,fg='white',bg=self.bg)
        label7_1.grid(column=0, row=6, padx=5, pady=5,sticky='w')
        

        labelFrame2 = tk.Frame(self.FrameB,bg=self.bg)

        label8 = tk.Label(labelFrame2, text="Image", font=self.H2,fg=self.H2Color,bg=self.bg)
        label8.pack()
        label9_1 = tk.Label(labelFrame2, text="www.flaticon.com", font=self.H3,fg='white',bg=self.bg)
        label9_1.pack()
        label9_2 = tk.Label(labelFrame2, text="www.freepik.com", font=self.H3,fg='white',bg=self.bg)
        label9_2.pack()
        label88 = tk.Label(labelFrame2, text="Sound", font=self.H2,fg=self.H2Color,bg=self.bg)
        label88.pack(pady=10)
        label9_11 = tk.Label(labelFrame2, text="www.mixkit.co", font=self.H3,fg='white',bg=self.bg).pack()

        Github = Image.open("./src/image/github.png")
        Github = Github.resize((100,100), Image.ANTIALIAS)
        Github =  ImageTk.PhotoImage(Github)

        label12 = tk.Label(labelFrame2, text="Sound code", font=self.H2,fg=self.H2Color,bg=self.bg)
        label12.pack()
        label13 = tk.Label(labelFrame2,compound=tk.LEFT,justify='left',image=Github, text="  https://github.com/PongthepNuchwet/\n  Student-Face-Recognition", font=self.H3,fg='white',bg=self.bg)
        label13.image = Github
        label13.pack()
        

        labelFrame3 = tk.Frame(self.FrameB,bg=self.bg)



        label10 = tk.Label(labelFrame3, text="Developer", font=self.H2,fg=self.H2Color,bg=self.bg)
        label10.pack()

        p1 = Image.open("./src/image/p01.png")
        p1 = p1.resize((100,100), Image.ANTIALIAS)
        p1 =  ImageTk.PhotoImage(p1)

        p2 = Image.open("./src/image/p03.png")
        p2 = p2.resize((100,100), Image.ANTIALIAS)
        p2 =  ImageTk.PhotoImage(p2)

        p3 = Image.open("./src/image/p02.png")
        p3 = p3.resize((100,100), Image.ANTIALIAS)
        p3 =  ImageTk.PhotoImage(p3)

        self.LabelP02 = tk.Label(labelFrame3,justify='left',text=' Pongsagul Boonrub\n 6310301003@cdti.ac.th',compound=tk.LEFT,image=p2)
        self.LabelP02.configure(bg=self.bg,font=('kanit',16),fg='white')
        self.LabelP02.image = p2
        self.LabelP02.pack(ipadx=20,ipady=10)

        self.LabelP01 = tk.Label(labelFrame3,justify='left',text=' Pongthep Nuchwet\n 6310301004@cdti.ac.th',compound=tk.LEFT,image=p1)
        self.LabelP01.configure(bg=self.bg,font=('kanit',16),fg='white')
        self.LabelP01.image = p1
        self.LabelP01.pack(ipadx=20,ipady=10)

        

        self.LabelP03 = tk.Label(labelFrame3,justify='left',text=' Pakkamat Limjitsomboon\n 6310301036@cdti.ac.th',compound=tk.LEFT,image=p3)
        self.LabelP03.configure(bg=self.bg,font=('kanit',16),fg='white')
        self.LabelP03.image = p3
        self.LabelP03.pack(ipadx=20,ipady=10)

        sFrame1.grid(column=1,row=3,sticky='ns')
        sFrame2.grid(column=3,row=3,sticky='ns')
        self.separator1.pack(fill='y',expand=True)
        self.separator2.pack(fill='y',expand=True)
        labelFrame1.grid(column=0, row=3,sticky='n')
        labelFrame2.grid(column=2, row=3,sticky='n')
        labelFrame3.grid(column=4, row=3,sticky='n')