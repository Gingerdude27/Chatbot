#Importieren von Bibliotheken
import random
import json
import pickle #serialization von Objekten ?
import numpy as np #vereinfacht handling von Arrays ?
import nltk #Spracherkennungstool
from nltk.stem import WordNetLemmatizer #Bricht Worte auf den Wortstamm herunter
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

#Worte Herunterbrechen
lemmatizer = WordNetLemmatizer

intents = json.loads(open('tags.json').read())

words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',', ':'] #Buchstaben die ignoriert werden

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])