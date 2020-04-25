from afinn import Afinn
af = Afinn()

# returns an array with [total sentiment of text, average sentiment of each word, description of the numerical value for avg sentiment]
# note that for Afinn, sentiment values range from -3 to 3 for each word
def analyzeSentiment(text):
    # Afinn data analyzes text
    totalSentiment = af.score(text)

    # find the average sentiment value per word
    wordList = text.split()
    avgWordSentiment = totalSentiment / len(wordList)

    # create text description of the average sentiment value
    sentimentDescription = "neutral"
    if avgWordSentiment > 0.2:
        sentimentDescription = "positive"
    elif avgWordSentiment < -0.2:
        sentimentDescription = "negative"

    # return array
    return [totalSentiment, avgWordSentiment, sentimentDescription]