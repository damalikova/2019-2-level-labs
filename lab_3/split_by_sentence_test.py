"""
Labour work #3
SplitBySentence tests
"""

import unittest

from lab_3.main import split_by_sentence


class SplitBySentenceTest(unittest.TestCase):
    """Check splitting by sentences of given text"""

    def test_ideal_splitting(self):
        """Ideal case"""
        test_text = 'Mar#y wa$nted, to swim! However, she was afraid of sharks.'
        expected_res = [
            [
                "<s>", "mary", "wanted", "to", "swim", "</s>"
            ],
            [
                "<s>", "however", "she", "was", "afraid", "of", "sharks", "</s>"
            ]
        ]

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)

    def test_empty_text_splitting(self):
        """empty text case"""
        test_text = ''
        expected_res = []

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)

    def test_none_text_splitting(self):
        """none text case"""
        test_text = None
        expected_res = []

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)

    def test_dirty_text_splitting(self):
        """dirty text case"""
        test_text = '!@#$%^&*('
        expected_res = []

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)

    def test_multiline_text_splitting(self):
        """dirty text case"""
        test_text = "Mar#y wa$nted, to swim! \n However, she  \n was afraid of sharks. \n Wasn't she?"

        expected_res = [
            [
                "<s>", "mary", "wanted", "to", "swim", "</s>"
            ],
            [
                "<s>", "however", "she", "was", "afraid", "of", "sharks", "</s>"
            ],
            [
                "<s>", "wasnt", "she", "</s>"
            ]
        ]

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)

    def test_not_a_sentence_text_splitting(self):
        """Not completed"""
        test_text = 'Mary'

        expected_res = []

        actual_res = split_by_sentence(test_text)
        self.assertEqual(actual_res, expected_res)
