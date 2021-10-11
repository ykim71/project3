from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(text):
    text = [text]
    for sentence in text:
        vs = analyzer.polarity_scores(sentence)
        result = vs['compound']

        return result

#        return "{:-<65} {}".format(sentence, str(vs))

# if __name__ == "__main__":
#     text = "i hate Trump"
#     print(vader_sentiment(text))