import re
from afinn import Afinn
af = Afinn()

# returns an array with [total sentiment of text, average sentiment of each word, description of the numerical value for avg sentiment]
# note that for Afinn, sentiment values range from -3 to 3 for each word
def analyzeSentiment(text):
    # clean the text to only include lowercase alphanumeric characters and whitespace
    cleanText = text
    cleanText = cleanText.lower()
    cleanText= re.sub("[^a-zA-Z0-9\s]", "", cleanText)

    # Afinn data analyzes text
    totalSentiment = af.score(cleanText)

    # find the average sentiment value per word
    wordList = cleanText.split()
    avgWordSentiment = totalSentiment / len(wordList)

    # create text description of the average sentiment value
    sentimentDescription = "neutral"
    if avgWordSentiment > 0.05:
        sentimentDescription = "positive"
    elif avgWordSentiment < -0.05:
        sentimentDescription = "negative"

    # return array
    return [totalSentiment, avgWordSentiment, sentimentDescription]


# this function returns array of [original sentence, cleaned version's total sentiment]
def getSentencesSentiment(text):
    # replace sentence ending puncuation with .
    sentenceText = text
    sentenceText = re.sub("[\.\!\?]+", ".", sentenceText)
    # split sentences into list
    sentenceList = sentenceText.split(".")

    # clean sentences and perform sentiment analysis
    sentenceSentiments = []
    for sentence in sentenceList:
        # clean sentence
        sentenceClean = sentence.lower()
        sentenceClean = re.sub("[^a-zA-Z0-9\s]", "", sentenceClean)
        # only add to analysis if the sentence is of length greater than 0
        if (len(sentence) > 0):
            sentenceSentiments.append([sentence, af.score(sentenceClean)])
    
    return sentenceSentiments