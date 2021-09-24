import os
from pymongo import MongoClient
from module.Staticmethod_controller import StaticMD
class Terminal:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def success(self,t):
        print(f"{self.OKGREEN} {t} {self.ENDC}")
    
    def err(self,t):
        print(f"{self.FAIL} {t} {self.ENDC}")

terminal = Terminal()

def dbConnect():
    try:
        conn = MongoClient(StaticMD.mongodb())
        conn.server_info()
        terminal.success("Connection Successfull")
    except :
        terminal.err("Cannot connect to the MongoDB.")

# Libary
print("\t\tLibrary\t\t")
try :
    import tkinter
    terminal.success("[1]\ttkinter\t\t\tfound")
except :
    terminal.err("[1]\ttkinter\t\t\tnot found")

try :
    import PIL
    terminal.success("[2]\tPIL\t\t\tfound")
except :
    terminal.err("[2]\tPIL\t\t\tnot found")

try :
    import cv2
    terminal.success("[3]\tcv2\t\t\tfound")
except :
    terminal.err("[3]\tcv2\t\t\tnot found")

try :
    import threading
    terminal.success("[4]\tthreading\t\tfound")
except :
    terminal.err("[4]\tthreading\t\tnot found")

try :
    import datetime
    terminal.success("[5]\tdatetime\t\tfound")
except :
    terminal.err("[5]\tdatetime\t\tnot found")

try :
    import playsound
    terminal.success("[6]\tplaysound\t\tfound")
except :
    terminal.err("[6]\tplaysound\t\tnot found")

try :
    import requests
    terminal.success("[7]\trequests\t\tfound")
except :
    terminal.err("[7]\trequests\t\tnot found")

try :
    import pymongo
    terminal.success("[8]\tpymongo\t\t\tfound")
except :
    terminal.err("[8]\tpymongo\t\t\tnot found")
 
try :
    import numpy
    terminal.success("[9]\tnumpy\t\t\tfound")
except :
    terminal.err("[9]\tnumpy\t\t\tnot found")

print("\t\tMongodb\t\t")
dbConnect()