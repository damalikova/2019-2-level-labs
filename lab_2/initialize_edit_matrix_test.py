# pylint: skip-file
"""
Checks the second lab. Part about the matrix initialization
"""

import unittest

from lab_2 import main


class InitializeEditMatrixTest(unittest.TestCase):
    """
    Tests matrix initialization
    """

    def test_matrix_initialization_ideal(self):
        """
        Ideal scenario
        """
        # arrange
        add_weight = 1
        remove_weight = 2
        edit_matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]
        expected_matrix = [[0, 1, 2, 3, 4, 5],
                           [2, 0, 0, 0, 0, 0],
                           [4, 0, 0, 0, 0, 0],
                           [6, 0, 0, 0, 0, 0],
                           [8, 0, 0, 0, 0, 0]]
        # act
        actual_matrix = main.initialize_edit_matrix(tuple(edit_matrix), add_weight, remove_weight)
        # assert
        self.assertListEqual(expected_matrix, actual_matrix)

    def test_matrix_initialization_empty(self):
        """
        Empty matrix
        """
        # arrange
        add_weight = 1
        remove_weight = 2
        edit_matrix = []
        expected_matrix = []
        # act
        actual_matrix = main.initialize_edit_matrix(tuple(edit_matrix), add_weight, remove_weight)
        # assert
        self.assertListEqual(expected_matrix, actual_matrix)

    def test_matrix_initialization_empty_elements(self):
        """
        Empty matrix
        """
        # arrange
        add_weight = 1
        remove_weight = 2
        edit_matrix = [[],[],[]]
        # act
        actual_matrix = main.initialize_edit_matrix(tuple(edit_matrix), add_weight, remove_weight)
        # assert
        self.assertListEqual(edit_matrix, actual_matrix)

    def test_matrix_initialization_wrong_params(self):
        """
        Wrong type parameters
        """
        # arrange
        add_weight = 'a'
        remove_weight = []
        edit_matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]
        # act
        actual_matrix = main.initialize_edit_matrix(tuple(edit_matrix), add_weight, remove_weight)
        # assert
        self.assertListEqual(edit_matrix, actual_matrix)

    def test_matrix_initialization_none_params(self):
        """
        None parameters
        """
        # arrange
        add_weight = None
        remove_weight = None
        edit_matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]
        # act
        actual_matrix = main.initialize_edit_matrix(tuple(edit_matrix), add_weight, remove_weight)
        # assert
        self.assertListEqual(edit_matrix, actual_matrix)
