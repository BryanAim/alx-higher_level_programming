#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_work(self):
        """Normal output"""
        a_list = [1, 2, 3]
        self.assertEqual(3, max_integer(a_list))

    def test_work2(self):
        """Normal output"""
        a_list = [3, 4, 5, 6]
        self.assertEqual(6, max_integer(a_list))

    def test_empty(self):
        """empty case"""
        self.assertEqual(None, max_integer([]))

    def test_empty2(self):
        """empty case"""
        self.assertEqual(None, max_integer())

    def test_1list(self):
        """Normal output"""
        a_list = [1]
        self.assertEqual(1, max_integer(a_list))

    def test_none(self):
        """none"""
        self.assertRaises(TypeError, max_integer([]))

    def test_none2(self):
        """none v2"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negative(self):
        """negative"""
        a_list_n = [-1, -2, -3]
        self.assertEqual(-1, max_integer(a_list_n))

if __name__ == '__main__':
        unittest.main()
