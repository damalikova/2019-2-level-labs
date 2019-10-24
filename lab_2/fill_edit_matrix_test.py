# pylint: skip-file
"""
Checks the second lab. Part about the matrix filling
"""

import unittest
from unittest.mock import patch

from lab_2 import main


class FillEditMatrixTest(unittest.TestCase):
    """
    Tests matrix filling out
    """

    def test_matrix_filling_ideal(self):
        """
        Ideal scenario
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0]
        ]
        add_weight = 1
        remove_weight = 1
        substitute_weight = 2
        original_word = 'length'
        target_word = 'kitchen'
        expected_res = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [2, 3, 4, 5, 6, 7, 6, 7],
            [3, 4, 5, 6, 7, 8, 7, 6],
            [4, 5, 6, 7, 8, 9, 8, 7],
            [5, 6, 7, 6, 7, 8, 9, 8],
            [6, 7, 8, 7, 8, 7, 8, 9]
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    @patch('lab_2.main.minimum_value')
    def test_matrix_filling_ideal_minimum_function_called(self, minimum_func):
        """
        Ideal scenario, munimum_value function called
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0]
        ]
        add_weight = 1
        remove_weight = 1
        substitute_weight = 2
        original_word = 'length'
        target_word = 'kitchen'
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertTrue(minimum_func.called)

    def test_matrix_filling_ideal_again(self):
        """
        Ideal scenario #2
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 3, 4, 5, 6],
            [4, 5, 6, 7, 8],
            [6, 7, 8, 9, 10]
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_ideal_with_free_sub(self):
        """
        Ideal scenario, substitution is free
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 0
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 0, 1, 2, 3],
            [4, 2, 0, 1, 2],
            [6, 4, 2, 0, 1]
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_same_words(self):
        """
        Ideal scenario, same words
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3],
            [2, 0, 0, 0],
            [4, 0, 0, 0],
            [6, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'cat'
        expected_res = [
            [0, 1, 2, 3],
            [2, 0, 1, 2],
            [4, 2, 0, 1],
            [6, 4, 2, 0]
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_empty(self):
        """
        Empty matrix
        """
        # arrange
        edit_matrix = []
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'doge'
        expected_res = []
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_empty_content(self):
        """
        Matrix with empty fields
        """
        # arrange
        edit_matrix = [[], [], []]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [[], [], []]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_wrong_add_weight(self):
        """
        Wrong type parameters
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 'a'
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_wrong_remove_weight(self):
        """
        Wrong type parameters
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = None
        substitute_weight = 3
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_wrong_sub_weight(self):
        """
        Wrong type parameters
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = []
        original_word = 'cat'
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_none_original_word(self):
        """
        Wrong type parameters
        """
        # arrange
        edit_matrix = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = None
        target_word = 'doge'
        expected_res = [
            [0, 1, 2, 3, 4],
            [2, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0],
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_filling_empty_target_word(self):
        """
        Wrong type parameters
        """
        # arrange
        edit_matrix = [
            [0],
            [2],
            [4],
            [6],
        ]
        add_weight = 1
        remove_weight = 2
        substitute_weight = 3
        original_word = 'cat'
        target_word = ''
        expected_res = [
            [0],
            [2],
            [4],
            [6],
        ]
        # act
        actual_res = main.fill_edit_matrix(tuple(edit_matrix), add_weight, remove_weight, substitute_weight,
                                           original_word, target_word)
        # assert
        self.assertListEqual(expected_res, actual_res)
