import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.67.56:27017/")
mydb = myclient["test"]
mycol = mydb["test"]
mycol.insert_one({'id':28745})