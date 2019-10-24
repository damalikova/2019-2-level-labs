# pylint: skip-file
"""
Checks the second lab. Part about the matrix generation
"""

import unittest

from lab_2 import main


class GenerateEditMatrixTest(unittest.TestCase):
    """
    Tests matrix generation
    """

    def test_matrix_creation_ideal(self):
        """
        Ideal scenario
        """
        # arrange
        num_rows = 5
        num_columns = 6
        expected_res = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]]
        # act
        actual_res = main.generate_edit_matrix(num_rows, num_columns)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_creation_empty(self):
        """
        Empty matrix
        """
        # arrange
        num_rows = 0
        num_columns = 0
        expected_res = []
        # act
        actual_res = main.generate_edit_matrix(num_rows, num_columns)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_creation_wrong_params(self):
        """
        Wrong type parameters
        """
        # arrange
        num_rows = 'a'
        num_columns = []
        expected_res = []
        # act
        actual_res = main.generate_edit_matrix(num_rows, num_columns)
        # assert
        self.assertListEqual(expected_res, actual_res)

    def test_matrix_creation_none_params(self):
        """
        None parameters
        """
        # arrange
        num_rows = None
        num_columns = None
        expected_res = []
        # act
        actual_res = main.generate_edit_matrix(num_rows, num_columns)
        # assert
        self.assertListEqual(expected_res, actual_res)
