import pandas as pd
import spacy

sp = spacy.load('en_core_web_sm', disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

def text_ner(text):
    text = [text]
    for sent in text:
        sent = ''.join(sent)
        sent = sp(sent)
        
        ner_list_keys = []
        ner_list_values = []            

        for entity in sent.ents:
            if entity.label_ == "PERSON":
                ner_list_keys.append(entity.label_)
                ner_list_values.append(entity.text)
            elif entity.label_ == "ORG":
                ner_list_keys.append(entity.label_)
                ner_list_values.append(entity.text)           
            elif entity.label_ == "NORP":
                ner_list_keys.append(entity.label_)
                ner_list_values.append(entity.text)
            else:
                None
    output = list(zip(ner_list_keys, ner_list_values))
    return output


# if __name__ == "__main__":
#     text = "Apple and Amazon are looking at buying U.K. startup for $1 billion"
# #    print([x[1] for x in text_ner(text)])
#     print(text_ner(text))
