from googletrans import Translator

def translate(text):
    translator = Translator()
    return translator.translate(text, dest='en').text
