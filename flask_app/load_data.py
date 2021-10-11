"""
Part_3

NoSQL 데이터 가져오기 (Github API - User octokit repos)

Part_2 에서 입력한 데이터에서 중복되지 않는 repo 의 name 을 가져와서 set 형태로 저장합니다.
- User octokit repos 데이터가 저장될 리스트의 변수명은 names 로 지정해주세요
- 여러분의 행동에 따라 repo 의 중복된 이름이 MongoDB 에 있을 수도 있고, 유일한 이름만 있을 수도 있습니다.
- 코드에 적혀있는 대로 콜렉션 이름은 변경하지 말아주세요!

# 클라우드 데이터베이스는 테스트에 시간이 걸릴 수 있습니다. 기다려주세요.
"""
from pymongo import MongoClient
import pandas as pd

HOST = 'cluster0.mc7y8.mongodb.net'
USER = 'yujin71'
PASSWORD = '5dk7dl1flsK'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'text_analysis'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
아래 pass 와 주석을 지우고, 코드를 작성하세요
set 자료형인 names 변수에 octokit의 repo 이름이 저장되도록 작성해주세요
"""

client = MongoClient(MONGO_URI)

DATABASE = 'myFirstDatabase'
database = client[DATABASE]

collection = database[COLLECTION_NAME]

cursor = collection.find()
mongo_docs = list(cursor)

docs = pd.DataFrame(columns=[])

for num, doc in enumerate( mongo_docs ):
    doc["_id"] = str(doc["_id"])
    doc_id = doc["_id"]
    series_obj = pd.Series( doc, name=doc_id )
    docs = docs.append(series_obj)

docs.to_csv("object_output.csv", ",") 

# cursor_query = collection.find({}, {'query':1})
# cursor_entity = collection.find({}, {'entity':1})
# cursor_input = collection.find({}, {'input':1})
# cursor_sentiment = collection.find({}, {'sentiment':1})
# cursor_wiki_0 = collection.find({}, {'wiki_0':1})

# def cursor_merge(cursor, name):
#     item = []
#     for i in cursor:
#         item.append(i[name])
#         return item

# query = cursor_merge(cursor_query, 'query')
# entity = cursor_merge(cursor_entity, 'entity')
# input_text = cursor_merge(cursor_input, 'input')
# sentiment = cursor_merge(cursor_sentiment, 'sentiment')
# wiki = cursor_merge(cursor_wiki_0, 'wiki_0')

# df = pd.DataFrame(list(zip(*[input_text,sentiment,query,entity,wiki])), columns=['input_text','sentiment','query','entity','wiki'])
# df.to_csv('output_from_db.csv', index=False)


# print(cursor_merge(cursor_query, 'query'))
# print(cursor_merge(cursor_entity, 'entity'))
# print(cursor_merge(cursor_input, 'input'))
# print(cursor_merge(cursor_sentiment, 'sentiment'))
# print(cursor_merge(cursor_wiki_0, 'wiki_0'))



# cursor = collection.find({},{"name":1})

# def Part_3_answer():
#     names = []
#     for i in cursor:
#         names.append(i['name'])
    
#     return set(names)
