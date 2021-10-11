from flask import Flask, render_template, request
from werkzeug.utils import header_property
from werkzeug.datastructures import ImmutableMultiDict
from sentiment_analysis import vader_sentiment
import text_to_ner as ner

import save_data as sd

import google_search as gs

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html'), 200

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form
        result = result.to_dict(flat=False)
        text = result['data'][0]
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

        return render_template("result.html", text = text, output = output, sentiment=sentiment)
    # elif request.method == 'GET':
    #      result = request.args.get('char1')
    #     return render_template('submit_test.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
