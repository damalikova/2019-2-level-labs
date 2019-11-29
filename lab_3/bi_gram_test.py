"""
Labour work #3
 BiGram tests
"""

import unittest

import math

from lab_3.main import NGramTrie


class BiGramTest(unittest.TestCase):
    """check NGramTrie class functionality on BiGrams - all tests should pass for 6,7 score"""

    def test_ngram_trie_check_creation(self):
        ngram = NGramTrie(2)
        self.assertEqual(ngram.size, 2)
        self.assertEqual(ngram.gram_frequencies, {})
        self.assertEqual(ngram.gram_log_probabilities, {})

    # bi gram tests
    def test_fill_from_sentence_ideal(self):
        ngram = NGramTrie(2)
        sentence = (1, 2, 3, 4, 5)
        ngram.fill_from_sentence(sentence)
        expected_res = {(1, 2): 1, (2, 3): 1, (3, 4): 1, (4, 5): 1}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_fill_from_sentence_duplcicates_ideal(self):
        ngram = NGramTrie(2)
        sentence = (1, 2, 1, 2, 1, 2)
        ngram.fill_from_sentence(sentence)
        expected_res = {(1, 2): 3, (2, 1): 2}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_fill_from_sentence_empty(self):
        ngram = NGramTrie(2)
        sentence = ()
        ngram.fill_from_sentence(sentence)
        expected_res = {}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_fill_from_sentence_none(self):
        ngram = NGramTrie(2)
        sentence = None
        res = ngram.fill_from_sentence(sentence)
        print(res)
        expected_res = {}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_fill_from_sentence_not_tuple(self):
        ngram = NGramTrie(2)
        sentence = [1, 2, 3, 4, 5]
        ngram.fill_from_sentence(sentence)
        expected_res = {}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_calculate_log_probabilities_ideal(self):
        ngram = NGramTrie(2)
        ngram.gram_frequencies = {(1, 2): 10, (1, 3): 2, (2, 5): 5}
        first_prob = math.log(10 / 12)
        second_prob = math.log(2 / 12)
        ngram.calculate_log_probabilities()
        self.assertEqual(ngram.gram_log_probabilities[(1, 2)], first_prob)
        self.assertEqual(ngram.gram_log_probabilities[(1, 3)], second_prob)

    def test_calculate_log_probabilities_one_bi_gram(self):
        ngram = NGramTrie(2)
        ngram.gram_frequencies = {(1, 2): 10}
        ngram.calculate_log_probabilities()
        self.assertEqual(ngram.gram_log_probabilities[(1, 2)], 0.0)

    def test_calculate_log_probabilities_empty(self):
        ngram = NGramTrie(2)
        ngram.gram_frequencies = {}
        ngram.calculate_log_probabilities()
        self.assertEqual(ngram.gram_log_probabilities, {})

    def test_predict_next_sentence_simple_ideal(self):
        ngram = NGramTrie(2)
        ngram.gram_log_probabilities = {(1, 2): -0.18, (1, 3): -1.79}
        actual_res = ngram.predict_next_sentence((1,))
        expected_res = [1, 2]
        self.assertEqual(actual_res, expected_res)

    def test_predict_next_sentence_more_words_ideal(self):
        ngram = NGramTrie(2)
        ngram.gram_log_probabilities = {(1, 2): -0.18, (1, 3): -1.79, (2, 3): -1, (2, 4): -2, (3, 4): -0.1,
                                        (3, 5): -1.8}
        actual_res = ngram.predict_next_sentence((1,))
        expected_res = [1, 2, 3, 4]
        self.assertEqual(actual_res, expected_res)

    def test_predict_next_sentence_wrong_size(self):
        ngram = NGramTrie(2)
        actual_res = ngram.predict_next_sentence((1, 2))
        expected_res = []
        self.assertEqual(actual_res, expected_res)

    def test_predict_next_sentence_none(self):
        ngram = NGramTrie(2)
        actual_res = ngram.predict_next_sentence(None)
        expected_res = []
        self.assertEqual(actual_res, expected_res)

    def test_predict_next_sentence_not_a_tuple(self):
        ngram = NGramTrie(2)
        actual_res = ngram.predict_next_sentence([1])
        expected_res = []
        self.assertEqual(actual_res, expected_res)

    def test_predict_next_sentence_no_match(self):
        ngram = NGramTrie(2)
        ngram.gram_log_probabilities = {(4, 2): -0.18, (4, 3): -1.79}
        actual_res = ngram.predict_next_sentence((1,))
        expected_res = [1]
        self.assertEqual(actual_res, expected_res)
