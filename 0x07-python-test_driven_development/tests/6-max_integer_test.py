#!/usr/bin/python3

"""

A module that tests a function from 6-max_integer called max_integer.

"""





import unittest

from importlib import import_module



max_integer = import_module('6-max_integer', '..').max_integer



class Test_max_integer(unittest.TestCase):

        """
         a class that ineherits TestCase class for testing.
        """

        def test_max_integer(self):
            """
            the method tests max_integer function
            """
            self.assertEqual(max_integer([1, 2, 3, 4]), 4)
            self.assertEqual(max_integer([]), None)
            self.assertEqual(max_integer([-1, 3, 43, -97, 50, 13]), 50)
            self.assertEqual(max_integer([5, 12, -12, 12, -12]), 12)


if __name__ == "__main__":
    unittest.main()
