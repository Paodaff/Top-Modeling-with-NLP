# import requests module
import json
import pymongo
import requests
from utils import *
from bs4 import BeautifulSoup, Tag
from requests.auth import HTTPBasicAuth



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["NLP_project"]
mycol = mydb["elasticsearch"]


def get_json(url: str, user: str, password: str):
    # Making a get request
    response = requests.get(f'{url}',
                            auth=HTTPBasicAuth(f'{user}', f'{password}'))

    return json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)


json_answer = get_json(
    "https://es1.mediaquantum.eu/streamua/streamua/_search?pretty=true&q=domain:*.il&sort=timestamp%3Adesc&size=2000",
    "elastic",
    "changeme")

json_answer = json.loads(json_answer)
json_answer = json_answer['hits']['hits']

count = 0

for document in json_answer:  # Document keys : ['_id', '_index', '_score', '_source', '_type']
    # Id and source are the only keys that make sense.

    # declarations
    html = document['_source']['text']
    irrelevantSitesNames = ["yaaraflowers", "bum", "tusa",
                            "love", "date", "b-zoog", "lov",
                            "makirim", "click4", "email",
                            "atraf", "soulmate", "soul"]

    # Relevancy check
    checkURL = [x for x in irrelevantSitesNames if (x in document['_source']['url'])]
    checkTitle = (document['_source']['title'] != "")

    # creation of needed elements
    abstract = find_abstract(html)
    body = find_body(html)
    summary = find_summary(html)

    if not checkURL and checkTitle and abstract and summary and body:
        mycol.insert_one({
                    "id": document['_id'],
                    "title": document['_source']['title'],
                    "url": document['_source']['url'],
                    "date": document['_source']['date'],
                    "abstract": abstract,
                    "body": body,
                    "summary": summary
        })
