#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 99]), 99)
        self.assertEqual(max_integer([99, 2, 3, 4, 5]), 99)
        self.assertEqual(max_integer([-99, -5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 7, 9, 3, 5, 2]), 9)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, 0]), 0)
        self.assertEqual(max_integer([]), None)
        self.assertTrue(len(max_integer.__doc__), 1)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1.5, 2.7, 2.9]), 2.9)
        self.assertRaises(TypeError, max_integer, [None, 3, 5])
        self.assertRaises(TypeError, max_integer, [None, None, None])
        self.assertRaises(TypeError, max_integer, [1, 3, 5, "Hola"])
        self.assertRaises(TypeError, max_integer, [2, 4, 6j])
        self.assertRaises(TypeError, max_integer, {2, 4, 6})
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertRaises(TypeError, max_integer, [1, [2, 4], 3])
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertRaises(TypeError, max_integer, [2j, 3, 5])
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 4, 1]), 4)


if __name__ == '__main__':
    unittest.main()
