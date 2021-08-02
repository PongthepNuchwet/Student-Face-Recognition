import os
import csv
from module.Staticmethod_controller import StaticMD 
class FaceDetection_model:
    def __init__(self) -> None:
        pass

    @staticmethod
    def CsvStudentData(num = 0,columns = ['SERIAL NO.','', 'ID', '', 'NAME','','CLASS']):
        StaticMD.checkFolder('src/Student/')
        exist = os.path.isfile('src/Student/data.csv')
        if exist :
            with open('src/Student/data.csv','r') as data :
                reader = csv.reader(data)
                for i in reader:
                    num += 1
            num = num //2
            data.close
        else:
            with open('src/Student/data.csv','a+') as data:
                writer = csv.writer(data)
                writer.writerow(columns)
                num = 1
            data.close
        return num

    @staticmethod
    def AddCsvStudentData(row):
        StaticMD.checkFolder('src/Student/')
        with open('src/Student/data.csv','a+') as data:
            writer =  csv.writer(data)
            writer.writerow(row)
        data.close()