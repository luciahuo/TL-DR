# need 'pip install translate'
from translate import Translator


def translateText(language, text):
    translator = Translator(to_lang=language)
    translatedText = translator.translate(text)
    return translatedText

# print(translateText("Latin", "Hello, I like to eat apple pie. Do you know him? I like to watch movies everyday."))