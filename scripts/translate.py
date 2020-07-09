from googletrans import Translator

def translate(text):
    translator = Translator()
    return translator.translate(text, src='pl', dest='en').text


Chcę żeby wykrył język tekstu i przetłumaczył na język angielski


print(translate("Bossak znwou pijany. Świadkowie mówią, że był widziany z Trzaskowskim i Dudą w warszawskim klubie nocnym."))
