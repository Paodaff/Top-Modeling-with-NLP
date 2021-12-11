import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NLP_project"]
mycol = mydb["elasticsearch"]

for doc in mycol.find():
    doc["text"] = doc["text"].replace("<br />", "")
    doc["text"] = doc["text"].replace("<br >", "")
    print(doc["text"])
