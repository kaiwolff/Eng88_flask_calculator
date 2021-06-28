import unittest

import calc_functions as calc_functions

class CalcTest(unittest.TestCase):
    #inheriting TestCase class from unittest


    def test_add(self): # naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter recognises it as a testcase.
        self.assertEqual(calc_functions.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(calc_functions.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(calc_functions.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(calc_functions.divide(2, 4), 0.5)
