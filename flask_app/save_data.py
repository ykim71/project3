"""
MONGODB SETUP
"""
from pymongo import MongoClient

HOST = 'cluster0.mc7y8.mongodb.net'
USER = 'yujin71'
PASSWORD = '5dk7dl1flsK'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'text_analysis'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

DATABASE = 'myFirstDatabase'
database = client[DATABASE]

collection = database[COLLECTION_NAME]

def save_data_mongodb(data):
    return collection.insert_many(data)


# pulled_data = [{'output_0': {'title': 'Steve Israel | Department of Government Cornell Arts ...', 'link': 'https://government.cornell.edu/steve-israel', 'text': 'Former Congressman Steve Israel left Capitol Hill – unindicted and undefeated – to pursue a career as a writer. In addition to writing two critically\xa0...'}, 'output_1': {'title': 'Steve Israel - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Steve_Israel', 'text': 'Steven J. Israel (born May 30, 1958) is an American politician who served as a U.S. Representative from New York from 2001 to 2017.\nIn office January 3, 2015 – January 3, 2017: In ...\nPolitical party: Democratic\nEducation: George Washington University (\u200eBA\u200e)\u200e\nSpouse(s): Marlene Budd (m. 2003; div. 20...\n\u200eU.S. House of Representatives · \u200eTenure · \u200ePolicy positions · \u200eGun issues'}, 'output_2': {'title': 'Steve Israel (American football) - Wikipedia', 'link': 'https://en.wikipedia.org/wiki/Steve_Israel_(American_football)', 'text': 'He played in the NFL for the Los Angeles Rams, the San Francisco 49ers, the New England Patriots, the New Orleans Saints, and the Carolina Panthers. After ten\xa0...'}, 'output_3': {'title': 'Steve Israel - Ballotpedia', 'link': 'https://ballotpedia.org/Steve_Israel', 'text': "Steve Israel (b. May 30, 1958, in Brooklyn, N.Y.) is a former Democratic member of the United States House of Representatives representing New York's 3rd\xa0...\nSupporting: Hillary Clinton\nStatus: Superdelegate"}, 'output_4': {'title': 'About | Steve Israel', 'link': 'https://repsteveisrael.com/about/', 'text': 'Steve Israel was a Member of Congress from New York for sixteen years. He was elected in 2000 and retired in 2017, having served in the House Democratic\xa0...'}, 'output_5': {'title': 'Steve Israel | Congress.gov', 'link': 'https://www.congress.gov/member/steve-israel/I000057', 'text': 'Results 1 - 100 of 3637 — Sponsored legislation by Steve Israel, the Representative from New York - in Congress from 2015 through 2017.\nHouse: New York, District 3 113th-114th (2013...'}, 'output_6': {'title': 'Steve Israel | Institute of Politics', 'link': 'https://politics.uchicago.edu/fellows-program/fellow/steve-israel', 'text': 'Former Congressman Steve Israel (D-NY) is a Distinguished Writer-In-Residence at Long Island University in New York and published two critically acclaimed\xa0...'}, 'output_7': {'title': 'Steve Israel - Michael Best Strategies', 'link': 'https://michaelbeststrategies.com/about/steve-israel/', 'text': 'Steve is a former U.S. Congressman who represented the North Shore of Long Island and parts of Queens for 16 years (2001-2017). He served as Chairman of the\xa0...'}, 'wiki_0': {'text': 'Steven Douglas Israel (born March 16, 1969)[1] is a former American football cornerback. Israel grew up in Lawnside, New Jersey and played high school football at Haddon Heights High School.[1][2]'}, 'wiki_1': {'text': " Steven J. Israel (born May 30, 1958) is an American politician who served as a U.S. Representative from New York from 2001 to 2017. A member of the Democratic Party, he was elected in New York's 2nd congressional district until 2013 and New York's 3rd congressional district until his retirement from Congress.[1]"}}]
# collection.insert_many(pulled_data)




