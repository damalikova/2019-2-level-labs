# pylint: skip-file
"""
Checks the second lab. Part about the distance finding
"""

import unittest
from unittest.mock import patch

from lab_2 import main


class FindDistanceTest(unittest.TestCase):
    """
    Tests distance finding
    """

    def test_find_distance_ideal(self):
        """
        Ideal scenario
        """
        # arrange
        original_word = 'cat'
        target_word = 'doge'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = 10
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_ideal_again(self):
        """
        Ideal scenario # 2
        """
        # arrange
        original_word = 'length'
        target_word = 'kitchen'
        add_weight = 1
        remove_weight = 1
        substitute_weight = 2
        expected_result = 9
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_empty_target_word(self):
        """
        Empty target word
        """
        # arrange
        original_word = 'cat'
        target_word = ''
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = 6
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_same_words(self):
        """
        Same target word
        """
        # arrange
        original_word = 'cat'
        target_word = 'cat'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = 0
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_empty_original_words(self):
        """
        Empty original word
        """
        # arrange
        original_word = ''
        target_word = 'cat'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = 3
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_same_length_words(self):
        """
        Same length word with different letters
        """
        # arrange
        original_word = 'dog'
        target_word = 'cat'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = 9
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_wrong_original_word(self):
        """
        Wrong original word type
        """
        # arrange
        original_word = 1
        target_word = 'cat'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = -1
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_wrong_target_word(self):
        """
        Wrong target word type
        """
        # arrange
        original_word = 'cat'
        target_word = []
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        expected_result = -1
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_wrong_add_weight(self):
        """
        Wrong add weight type
        """
        # arrange
        original_word = 'cat'
        target_word = 'doge'
        add_weight = 'q'
        remove_weight = 2
        substitute_weight = 3
        expected_result = -1
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_wrong_remove_weight(self):
        """
        Wrong remove weight type
        """
        # arrange
        original_word = 'cat'
        target_word = 'doge'
        add_weight = 1
        remove_weight = []
        substitute_weight = 3
        expected_result = -1
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    def test_find_distance_wrong_substitute_weight(self):
        """
        Wrong substitute weight type
        """
        # arrange
        original_word = 'cat'
        target_word = 'doge'
        add_weight = 1
        remove_weight = 2
        substitute_weight = None
        expected_result = -1
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertEqual(expected_result, actual_distance)

    @patch('lab_2.main.generate_edit_matrix')
    @patch('lab_2.main.initialize_edit_matrix')
    @patch('lab_2.main.fill_edit_matrix')
    def test_find_distance_all_functions_called(self, generate_func, edit_func, find_func):
        """
        All needed functions are called
        """
        # arrange
        original_word = 'dog'
        target_word = 'cat'
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        # act
        actual_distance = main.find_distance(original_word, target_word, add_weight, remove_weight, substitute_weight)
        # assert
        self.assertTrue(generate_func.called)
        self.assertTrue(edit_func.called)
        self.assertTrue(find_func.called)
