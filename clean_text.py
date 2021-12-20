import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NLP_project"]
mycol = mydb["elasticsearch"]
list = ["<br />", "<br >", ".", ",", ":"]

for doc in mycol.find():
    for word in list:
        doc["text"] = doc["text"].replace(word, "")

    myquery = {"id" : doc["id"]}
    newVal = {"$set": {"text": doc["text"]}}

    mycol.update_one(myquery,newVal)
