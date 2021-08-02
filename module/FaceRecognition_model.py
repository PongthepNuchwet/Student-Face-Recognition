import os
import csv
import datetime
# from module.Staticmethod_controller import StaticMD 
class FaceRecognition_model:
    def __init__(self) -> None:
        pass

    @staticmethod
    def AddCsvAttendanceData(date,attendance):
        print("[Debug] save data")
        col_names = ['Id','','image','','Name','','Class','','Date', '', 'Time']
        exists = os.path.isfile("src/Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("src/Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("src/Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()

    @staticmethod
    def ChackData(lid,date):
        
        status = False

        exist = os.path.isfile(f'src/Attendance/Attendance_{date}.csv')
        if exist :
            with open(f'src/Attendance/Attendance_{date}.csv', newline='') as csvfile:
                spamreader = csv.DictReader(csvfile)
                for row in spamreader:
                    if row['Id'] == lid :
                        status = True
            csvfile.close()
        print("[Debug] chek data",status)
        return status

    @staticmethod
    def GetCsvAttendanceData(date):

        spamreader = ''
        data = []
        exist = os.path.isfile(f'src/Attendance/Attendance_{date}.csv')
        if exist :
            with open(f'src/Attendance/Attendance_{date}.csv', newline='') as csvfile:
                spamreader = csv.DictReader(csvfile)
                for i in spamreader :
                    data.append(i)
                
        print("[Debug] GetCsvAttendanceData")
        return data
