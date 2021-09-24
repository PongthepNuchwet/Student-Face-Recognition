import pymongo
from module.Staticmethod_controller import StaticMD


class Mongo_attendant:
    def __init__(self) -> None:

        self.myclient = pymongo.MongoClient(StaticMD.mongodb())
        self.mydb = self.myclient["StudentFaceRecognition"]
        self.mycol = self.mydb["attendants"]

    def getLen(self, id):
        return len([a for a in self.mycol.find({'studentId': str(id)})])

    def find_all(self, date):
        return [a for a in self.mycol.find({'date': str(date)})]

    def find_ID(self, studentId):
        return [a for a in self.mycol.find({'studentId': str(studentId)})]

    def view(self):
        return [a for a in self.mycol.find()]

    def add(self, data):
        status = self.mycol.insert_one(data)
        return status.acknowledged

    def delete(self, id):
        myquery = {"studentId": str(id)}
        status = self.mycol.delete_one(myquery)
        return status
