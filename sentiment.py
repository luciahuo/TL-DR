from afinn import Afinn
af = Afinn()


def analyzeSentiment(text):
    score = af.score(text)
    sentimentText = "neutral"
    if score > 0.5:
        sentimentText = "positive"
    elif score < 0.5:
        sentimentText = "negative"

    return [score, sentimentText]