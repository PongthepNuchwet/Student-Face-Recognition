# Student-Face-Recognition
![This is an image](./src/image/logo.png)
### Student face recognition เป็นระบบลงเวลามาเรียนของนักเรียนและแจ้งเตือนไปยังโทรศัพท์มือถือของผู้ปกครอง ผ่านโปรแกรมไลน์ ( Line Application)
> ระบบนี้พัฒนาด้วยภาษา Python และได้ใช้ Tkinter เป็น GUI
# Contents
- [วิธีติดตั้งโปรแกรม]()
## วิธีติดตั้งโปรแกรม
### Step 1
ติดตั้ง Library ดังต่อไปนี้
- tkinter
- PIL
- cv2
- threading
- datetime
- playsound
- requests
- pymongo
- numpy


### Step 2
ดาวน์โหลดและติดตั้ง MongoDB [Download](https://www.mongodb.com/try/download/community).

### Step 3 
#### ตั้งค่าโปรแกรมในไฟล์ Staticmethod_controller.py
> ./module/Staticmethod_controller.py
##### 1. กำหนด ที่อยู่ของ MongoDB ของคุณ
```
def mongodb(): return "<MongoDB hosts and ports>"
```
###### ตัวอย่าง
```
def mongodb(): return "mongodb://localhost:27017/"
```
##### 2. กำหนด Line token ของคุณ [สร้าง Line Token](https://notify-bot.line.me)
```
def lineToken(): return '<Your Line token>'
```
###### ตัวอย่าง
```
def lineToken(): return 'ABCDTGJWhQeqJSv1lE7cdacDItH8IwIpOmILZ4r1Lqk'
```

### Step 4
ทดสอบโดยการ Run ไฟล์ status.py
> status.py

##### status.py จะตรวจสอบว่า Libary ที่ใช้ในโปรแกรมถูกติดตั้งหมดหรือยัง และสามารถเชื่อมต่อกับ MongoDB ได้ใหม ถ้าขึ้นสีเขียวหมด เราก็สามารถรันโปรแกรมของเราได้

## วิธีการเปิดโปรแกรม
### Run ไฟล์ main.py เพื่อเปิดโปรแกรม

## Developer
1. Pongthep Nuchwet 
2. Pongsagul Boonrub 
3. Pakkamat Limjitsomboon
