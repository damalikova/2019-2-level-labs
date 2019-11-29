"""
Labour work #3
 ThreeGram tests
"""

import unittest

import math

from lab_3.main import NGramTrie


class ThreeGramTest(unittest.TestCase):
    """check NGramTrie class functionality on Three-Grams - all tests should pass for 8 score or above"""

    def test_three_gram_trie_check_creation(self):
        ngram = NGramTrie(3)
        self.assertEqual(ngram.size, 3)
        self.assertEqual(ngram.gram_frequencies, {})
        self.assertEqual(ngram.gram_log_probabilities, {})

    # bi gram tests
    def test_three_gram_fill_from_sentence_ideal(self):
        ngram = NGramTrie(3)
        sentence = (1, 2, 3, 4, 5)
        ngram.fill_from_sentence(sentence)
        expected_res = {(1, 2, 3): 1, (2, 3, 4): 1, (3, 4, 5): 1}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_three_gram_fill_from_sentence_duplcicates_ideal(self):
        ngram = NGramTrie(3)
        sentence = (1, 2, 1, 2, 1, 2)
        ngram.fill_from_sentence(sentence)
        expected_res = {(1, 2, 1): 2, (2, 1, 2): 2}
        self.assertEqual(ngram.gram_frequencies, expected_res)

    def test_three_gram_calculate_log_probabilities_ideal(self):
        ngram = NGramTrie(3)
        ngram.gram_frequencies = {(1, 2, 3): 10, (1, 2, 4): 2, (2, 1, 3): 2}
        first_prob = math.log(10 / 12)
        second_prob = math.log(2 / 12)
        ngram.calculate_log_probabilities()
        self.assertEqual(ngram.gram_log_probabilities[(1, 2, 3)], first_prob)
        self.assertEqual(ngram.gram_log_probabilities[(1, 2, 4)], second_prob)

    def test_three_gram_calculate_log_probabilities_one_three_gram(self):
        ngram = NGramTrie(3)
        ngram.gram_frequencies = {(1, 2, 3): 10}
        ngram.calculate_log_probabilities()
        self.assertEqual(ngram.gram_log_probabilities[(1, 2, 3)], 0.0)

    def test_three_gram_predict_next_sentence_simple_ideal(self):
        ngram = NGramTrie(3)
        ngram.gram_log_probabilities = {(1, 2, 3): -0.18, (1, 2, 4): -1.79}
        actual_res = ngram.predict_next_sentence((1, 2))
        expected_res = [1, 2, 3]
        self.assertEqual(actual_res, expected_res)

    def test_three_gram_predict_next_sentence_more_words_ideal(self):
        ngram = NGramTrie(3)
        ngram.gram_log_probabilities = {(1, 2, 3): -0.18, (1, 2, 4): -0.78, (1, 3, 4): -1.79, (2, 3, 4): -1,
                                        (2, 3, 5): -0.5, (2, 4, 5): -2, (3, 4, 6): -0.1, (3, 5, 6): -1.8}
        actual_res = ngram.predict_next_sentence((1, 2))
        expected_res = [1, 2, 3, 5, 6]
        self.assertEqual(actual_res, expected_res)

    def test_three_gram_predict_next_sentence_wrong_size(self):
        ngram = NGramTrie(3)
        actual_res = ngram.predict_next_sentence((1, 2, 3))
        expected_res = []
        self.assertEqual(actual_res, expected_res)

    def test_three_gram_predict_next_sentence_no_match(self):
        ngram = NGramTrie(3)
        ngram.gram_log_probabilities = {(4, 2, 1): -0.18, (4, 3, 5): -1.79}
        actual_res = ngram.predict_next_sentence((1, 2))
        expected_res = [1, 2]
        self.assertEqual(actual_res, expected_res)
