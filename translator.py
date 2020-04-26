# need 'pip install googletrans'
# note we are using googletrans now
from googletrans import Translator


def translateText(language, text):
    translator = Translator()
    # split up text to not exceed maximum length for translate
    textSplit = text.split('.')
    translatedSentences = []
    for sentence in textSplit:
        if len(sentence) > 0:
            try:
                # language should be in google's abbreviated form
                translated = translator.translate(sentence, dest=language) 
                translatedSentences.append(translated.text)
            except:
                continue
    
    translatedText = ""
    for sentence in translatedSentences:
        if len(sentence) > 0:
            translatedText = translatedText + sentence + ". "

    return translatedText

# print(translateText("fr", "Hello, I like to eat apple pie. Do you know him? I like to watch movies everyday."))