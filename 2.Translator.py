from numpy import unique
import pandas as pdv

from google_trans_new import google_translator
data = pdv.read_csv("Colours.csv")
print(data)

trans= google_translator()
translations ={}

for item in data.columns:
    unique = data[item].unique()
    for element in unique:
        translations[element]=trans.translate(element)

print(translations.items())

# or

for i in translations.items():
    print(i)

#  	TO TRANSLATE IN CERTAIN LANGUAGE 

for item in data.columns:
    unique = data[item].unique()
    for element in unique:
        translations[element]=trans.translate(element,lang_tgt='de')

print(translations.items())

