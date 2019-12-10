"""
Labour work #3
 Building an own N-gram model
"""

from math import log

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:

    def __init__(self):
        self.storage = dict()

    def put(self, word: str) -> int:

        if not word or not isinstance(word, str):
            return 0

        id_number = len(self.storage)

        if not self.storage:
            id_number = 1
            self.storage[word] = id_number
            return id_number

        if not self.storage.get(word):
            id_number += 1
            self.storage[word] = id_number
        return self.storage.get(word)

    def get_id_of(self, word: str) -> int:

        for key, value in self.storage.items():
            if word is key:
                return value

        return -1

    def get_original_by(self, id_number: int) -> str:

        for key, value in self.storage.items():
            if id_number is value:
                return key

        return 'UNK'

    def from_corpus(self, corpus: tuple):

        storage_instance = WordStorage

        if not corpus or corpus is None or not isinstance(corpus, tuple):
            return storage_instance

        for word in list(corpus):
            storage_instance.put(self, word)

        return storage_instance


class NGramTrie:

    def __init__(self, n):

        self.size = n
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()
        self.predicted_sentence = []

    def fill_from_sentence(self, sentence: tuple) -> str:

        if not isinstance(sentence, tuple):
            return 'ERROR'

        right = self.size

        for i, _el in enumerate(sentence):
            n_gram = sentence[i:right]

            if len(n_gram) is self.size and n_gram not in self.gram_frequencies:
                self.gram_frequencies[n_gram] = 1

            elif n_gram in self.gram_frequencies:
                self.gram_frequencies[n_gram] += 1

            right += 1

        return 'OK'

    def calculate_log_probabilities(self):

        for n_gram in self.gram_frequencies:

            part_to_find = n_gram[:self.size - 1]
            n_gram_frequency = self.gram_frequencies[n_gram]
            n_grams_frequency = 0

            for n_grams in self.gram_frequencies:

                part_to_compare = n_grams[:self.size - 1]

                if part_to_compare == part_to_find:
                    n_grams_frequency += self.gram_frequencies[n_grams]

            probability = n_gram_frequency / n_grams_frequency
            self.gram_log_probabilities[n_gram] = log(probability)

    def predict_next_sentence(self, prefix: tuple) -> list:

        if not isinstance(prefix, tuple) or len(prefix) is not self.size - 1:
            return []

        list_of_prob = []

        for n_gram in self.gram_log_probabilities:

            part_to_compare = n_gram[:self.size - 1]

            if part_to_compare == prefix:
                list_of_prob.append(self.gram_log_probabilities[n_gram])

        if not list_of_prob:
            return [x for x in prefix]

        predicted_prob = max(list_of_prob)

        for key in self.gram_log_probabilities:

            if predicted_prob is self.gram_log_probabilities[key]:
                for element in key:
                    if element not in self.predicted_sentence:
                        self.predicted_sentence.append(element)

                new_prefix = key[1:]
                self.predict_next_sentence(new_prefix)

        return self.predicted_sentence


def encode(storage_instance, corpus) -> list:

    encoded_text = []

    for sentence in corpus:

        encoded_sentence = []

        for word in sentence:
            encoded_word = storage_instance.get_id_of(word)
            encoded_sentence.append(encoded_word)

        encoded_text.append(encoded_sentence)

    return encoded_text


def split_by_sentence(text: str) -> list:

    corpus = []

    if not text or ' ' not in text or not isinstance(text, str):
        return corpus

    splitters = '.!?'

    if ' \n ' in text:
        text = text.replace(' \n ', ' ')

    for element in text:
        if not element.isalpha() and element not in splitters and element != ' ':
            text = text.replace(element, '')

    for ind, sym in enumerate(text):
        if sym.isupper() and text[ind - 1] == ' ' and text[ind - 2] in splitters:
            text = text.replace(text[ind - 2], '%')

    for symbol in text:
        if symbol in splitters:
            text = text.replace(symbol, '')

    text_as_list = text.lower().split('%')

    for sentence in text_as_list:
        new_sentence = ('<s> ' + sentence + ' </s>').split()
        corpus.append(new_sentence)

    return corpus
