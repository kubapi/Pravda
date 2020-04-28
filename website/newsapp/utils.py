#Grouping (Used in breaking elements when row ends in bootstrap)
def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

#Translation (Used for triplet extraction in editor)
from googletrans import Translator
def translate(l):
    translator = Translator()
    list = []
    for element in l:
        list.append(translator.translate(element,src='pl', dest='en').text)
    return list
