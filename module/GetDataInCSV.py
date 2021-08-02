import csv
from module.FaceDetection_model import FaceDetection_model

class GetDataInCSV:
    def __init__(self,container) -> None:

        FaceDetection_model.CsvStudentData()
        container.tree.delete(*container.tree.get_children())
        with open('src/Student/data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')

            sortedlist = sorted(reader, key=lambda row: row['SERIAL NO.'], reverse=True)
            for row in sortedlist:

                serial = row['SERIAL NO.']
                id = row['ID']
                Name = row['NAME']
                cla = row['CLASS']
                container.tree.insert("", 0, values=(serial, id, Name,cla))