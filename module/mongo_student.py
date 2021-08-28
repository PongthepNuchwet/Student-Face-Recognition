import pymongo
class Mongo_student:
    def __init__(self) -> None:
    
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["StudentFaceRecognition"]
        self.mycol = self.mydb["studentdetails"]

    def find(self,id):
        return len([a for a in self.mycol.find({'id':str(id)})])

    def find_all(self,id):
        return [a for a in self.mycol.find({'id':str(id)})]

    def view(self):
        return [a for a in self.mycol.find()]

    def delete(self,id):
        myquery = {"id": str(id) }
        status = self.mycol.delete_one(myquery)
        return status

    def add(self,data):
        status = self.mycol.insert_one(data)
        return status.acknowledged
