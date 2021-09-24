import os
data = {}

# Libary
try :
    import tkinter
    print("[1]\ttkinter\t\t\tfound")
except :
    print("[1]\ttkinter\t\t\tnot found")
    data['tkinter'] = 'python -m pip install tk'

try :
    import PIL
    print("[2]\tPIL\t\t\tfound")
except :
    print("[2]\tPIL\t\t\tnot found")
    data['PIL'] = 'python -m pip install tk'

try :
    import cv2
    print("[3]\tcv2\t\t\tfound")
except :
    print("[3]\tcv2\t\t\tnot found")
    data['cv2'] = 'python -m pip install tk'

try :
    import threading
    print("[4]\tthreading\t\tfound")
except :
    print("[4]\tthreading\tnot found")
    data['threading'] = 'python -m pip install tk'

try :
    import datetime
    print("[5]\tdatetime\t\tfound")
except :
    print("[5]\tdatetime\tnot found")
    data['datetime'] = 'python -m pip install tk'

try :
    import playsound
    print("[6]\tplaysound\t\tfound")
except :
    print("[6]\tplaysound\tnot found")
    data['playsound'] = 'python -m pip install tk'

try :
    import requests
    print("[7]\trequests\t\tfound")
except :
    print("[7]\trequests\tnot found")
    data['requests'] = 'python -m pip install tk'

try :
    import pymongo
    print("[8]\tpymongo\t\t\tfound")
except :
    print("[8]\tpymongo\tnot found")
    data['pymongo'] = 'python -m pip install tk'

try :
    import numpy
    print("[9]\tnumpy\t\t\tfound")
except :
    print("[9]\tnumpy\tnot found")
    data['numpy'] = 'python -m pip install tk'

print(data)