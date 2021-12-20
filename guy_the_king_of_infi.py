import pymongo
import requests 
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NLP_project"]
mycol = mydb["elasticsearch"]

bad_types = [
    "CONJUNCTION",
    "NUMBER",
    "QUESTION_WORD",
    "PRONOUN",
    "PREPOSITION"]



for doc in mycol.find():
    request = {
     'token': '6B94f8CrQg3Vd2l',
     'readable': False,
     'paragraph':  f'{doc["text"]}'
    }
    result = requests.post('https://hebrew-nlp.co.il/service/Morphology/Analyze', json=request).json()

    new_para = ''

    for sentence in result:
        
        for word in sentence:
            
            best_option = word[0]

            print()

            if best_option['partOfSpeech'] in bad_types:
                pass
            else:
                new_para += (' ')
                new_para += (best_option["baseWord"])
    
    print(new_para)