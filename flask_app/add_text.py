from sentiment_analysis import vader_sentiment
import text_to_ner as ner
import save_data as sd
import google_search as gs
import pandas as pd


df = pd.read_csv('trump.csv')
df_text = df['text']

for i in df_text:
    text = i
    sentiment = vader_sentiment(text) # SA
    
    text_item = {
            'input' : text,
            'sentiment' : sentiment
            }

    result_ner = ner.text_ner(text)
    if len(result_ner) != 0:
        result_ner_v = [x[1] for x in result_ner]
        result_ner_k = [x[0] for x in result_ner]

        search_result_list = []

        for i in range(0, len(result_ner_v)):
            search_result = gs.google_search(result_ner_v[i])
            
            ner_item = {
                'query' : result_ner_v[i],
                'entity' : result_ner_k[i]
            }

            search_result_merge = {**ner_item, **search_result}
            search_result_list.append(search_result_merge)
        
    else:
        search_result_list = [{
            'query' : "None",
            'entity' : "None"
        }]

    output = [{**text_item, **search_result_list[0]}]
    sd.save_data_mongodb(output)

