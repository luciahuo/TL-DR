from afinn import Afinn
af = Afinn()


def analyzeSentiment(text):
    totalSentiment = af.score(text)
    wordList = text.split()
    avgWordSentiment = totalSentiment / len(wordList)

    sentimentText = "neutral"
    if avgWordSentiment > 0.2:
        sentimentText = "positive"
    elif avgWordSentiment < -0.2:
        sentimentText = "negative"
    return [totalSentiment, sentimentText, avgWordSentiment]