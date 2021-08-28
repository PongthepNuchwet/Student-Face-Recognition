import pymongo
class Mongo_attendant:
    def __init__(self) -> None:
    
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["StudentFaceRecognition"]
        self.mycol = self.mydb["attendants"]

    def getLen(self,id):
        return len([a for a in self.mycol.find({'studentId':str(id)})])

    def find_all(self,date):
        return [a for a in self.mycol.find({'date':str(date)})]

    def find_ID(self,studentId):
        return [a for a in self.mycol.find({'studentId':str(studentId)})]

    def view(self):
        return [a for a in self.mycol.find()]

    def add(self,data):
        status = self.mycol.insert_one(data)
        return status.acknowledged
    

