import random

import nltk
import numpy
import requests
from nltk.stem import SnowballStemmer
import pickle
from keras.models import load_model
import os
from main import settings


class ChatBot:
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

    # Stemmer: classe do NLTK que deixa as palavras na sua forma radical.
    STEMMER = SnowballStemmer("portuguese")

    VERIFY = False

    # Carregando os arrays que foram convertidos para pkl.
    classesPKL = pickle.load(
        open(settings.BASE_DIR.__str__() + r"\api\chatbot\classes.pkl", "rb"))

    wordsPKL = pickle.load(
        open(settings.BASE_DIR.__str__() + r"\api\chatbot\words.pkl", "rb"))

    # Carregando o model da I.A
    model = load_model(
        settings.BASE_DIR.__str__() + r'\api\chatbot\chatbot_model.keras')

    # Caracteres que vão ser ignorados
    IGNORE_LETTERS = [".", ';', '/', '?', '!', '"\"', ",", "...", "-", "(", ")", "-", "'", "_", "[", "]", "{",
                      "}",
                      "¡!"]

    def get_json(self, url):
        try:
            intents = requests.get(url).json()
            intents = intents[0]["json_palavras"]['intents']
            return intents

        except requests.exceptions.JSONDecodeError:
            print("ERRO: rode a api primeiro")

    # Função Tokenize (separar todas as palavras de uma palavra num array).
    def tokenize(self, sentence):
        # for char in self.IGNORE_LETTERS:
        #     for word in sentence:
        #         for latter in word:
        #             if latter == char:
        #                 sentence = sentence.replace(char, " ")

        tokenized_sentence = nltk.word_tokenize(sentence)
        return tokenized_sentence

    # Função Stem (pegar todas as palavras "tokenizadas" e deixar no infinitivo, pra facilitar na hora de transformar em
    # um input pra I.A).
    def stem(self, sentence):
        tokenized_sentence = self.tokenize(sentence)

        print(tokenized_sentence)
        stemmed_words = [self.STEMMER.stem(w.lower()) for w in tokenized_sentence if w not in self.IGNORE_LETTERS]
        self.wordsPKL = [self.STEMMER.stem(word) for word in self.wordsPKL if word not in self.IGNORE_LETTERS]
        return stemmed_words

    # Função Bag Of Words(Pegar todas as palavras que foram passadas pela função Stem, comparar com cada palavra em
    # nossa base de palavras e se caso ela corresponda retorna um array de zeros representando as posições das palavras
    # da base de dados e onde a palavra corresponder o valor fica 1 EX: ['bom', 'dia'] = [0 0 1 0 0 1]).
    def bow(self, sentence, words):
        sentence_words = self.stem(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1

        if 1 in bag:
            self.VERIFY = True

        if self.VERIFY:
            print("input aceito")
            return numpy.array(bag)

        else:
            print("input invalido")
            return numpy.array(bag)

    # Função Predict Class (Pega o array de zeros e uns gerado na função Bag of Words e utiliza como input para a I.A,
    # a mesma realiza um calculo muito doido e retorna um numero mais a probabilidade de acerto, esse número é utilizado
    # para acessar uma posição no nosso array de classes/tags (classes.pkl), assim apontando a que familia aquela
    # pergunta pertence EX: {"intents": grettings, 'probability': 0.9999})
    def predict_class(self, sentence):
        bag_of_words = self.bow(sentence, self.wordsPKL)
        res = self.model.predict(numpy.array([bag_of_words]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            if self.VERIFY:
                return_list.insert(0, {"intents": self.classesPKL[r[0]], 'probability': str(r[1])})
                self.VERIFY = False
            elif len(return_list) == 0:
                for i in self.classesPKL:
                    if i == "error":
                        requests.post("http://127.0.0.1:8000/perguntas_futuras/", data={"pergunta": sentence})
                        return_list.insert(0, {"intents": i, 'probability': str(r[1])})
                        print(return_list)

            else:
                for i in self.classesPKL:
                    if i == "error":
                        requests.post("http://127.0.0.1:8000/perguntas_futuras/", data={"pergunta": sentence})
                        return_list.insert(0, {"intents": i, 'probability': str(r[1])})
                        print(return_list)
        return return_list


# Função Get Response (pega a tag que a I.A retorna + json das palavras, percorre o json, encontra as respostas
# ralcionadas pela tag que a I.A retornou e dá um post com a resposta na API de resposta.)
def get_response(intents_list, intents_json):
    result = ""
    tag = intents_list[0]['intents']
    list_of_intents = intents_json

    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            try:
                requests.post('http://127.0.0.1:8000/respostas/', data={'resposta': str(result)})
            except Exception:
                print("deu ruim")
            break

    return result
