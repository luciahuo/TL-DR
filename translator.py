# need 'pip install googletrans'
# note we are using googletrans now
from googletrans import Translator
import sys
import re


def translateText(language, text):
    translator = Translator()
    # split up text to not exceed maximum length for translate
    text = re.sub("[^a-zA-Z0-9\s\.\!\?]", "", text)
    textSplit = text.split('.')
    textSplit2 = []
    # cut up text into more reasonable chunks
    for sentence in textSplit:
        if len(textSplit2) > 0 and len(textSplit2[-1]) < 600:
            textSplit2[-1] = textSplit2[-1] + ". " + sentence
        else:
            textSplit2.append(sentence)
    translatedSentences = []
    isGoogleTranDown = False
    for sentence in textSplit2:
        if len(sentence) > 0:
            try:
                # language should be in google's abbreviated form
                translated = translator.translate(sentence, dest=language) 
                translatedSentences.append(translated.text)
            except:
                # if google translate returns a non JSON object then that means it is blocking the program for some reason
                isGoogleTranDown = True
                continue
    
    
    translatedText = ""
    for sentence in translatedSentences:
        if len(sentence) > 0:
            translatedText = translatedText + sentence + ". "

    if isGoogleTranDown:
        translatedText = translateText + "\nGoogle Translate has some trouble translated this article. Could be down right now.\n Please wait a little while and try again later."

    return translatedText
# print(translateText("French", "Hello, I like to eat apple pie. Do you know him? I like to watch movies everyday."))