# need 'pip install translate'
from translate import Translator


def translateText(language, text):
    translator = Translator(to_lang=language)
    translatedText = translator.translate(text)
    return translatedText