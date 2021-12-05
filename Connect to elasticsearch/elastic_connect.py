
# import requests module
import json
import pymongo
import requests
from requests.auth import HTTPBasicAuth


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NLP_project"]
mycol = mydb["elasticsearch"]

def get_json(url, user, password):
    # Making a get request
    response = requests.get(f'{url}',
                auth = HTTPBasicAuth(f'{user}', f'{password}'))
    
    return json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)

json_answer = get_json(
    "https://es1.mediaquantum.eu/streamua/streamua/_search?pretty=true&q=domain:*.il",
    "elastic",
    "changeme")
    
json_answer = json.loads(json_answer)
json_answer = json_answer['hits']['hits'] # Ask slava what does max_score and total stand for in hits 


for document in json_answer: # Document keys : ['_id', '_index', '_score', '_source', '_type']
    # Id and source are the only keys that make sense.
    mycol.insert_one({
        "id": document['_id'],
        "title": document['_source']['title'],
        "url": document['_source']['url'],
        "date": document['_source']['insertdate'],
        "text": document['_source']['text']})
    

