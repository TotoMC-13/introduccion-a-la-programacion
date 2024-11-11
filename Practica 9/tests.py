import unittest
from funciones import *

class Ej1Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max(1, 2), 2, "x menor que y")

    def test_2(self):
        self.assertEqual(max(4, 1), 4, "x mayor que y")

class Ej2Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min(1, 2), 1, "x menor que y")

    def test_2(self):
        self.assertEqual(min(4, -2), -2, "x mayor que y")


class Ej9Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sumar(3,-2), 1, "y negativo")

    def test_2(self):
        self.assertEqual(sumar(3,1), 4, "y positivo")

if __name__ == '__main__':
    unittest.main(verbosity=2)
