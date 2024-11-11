import unittest
from funciones import *

class Ej1Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max(1,2), 2, "x menor que y")

    def test_2(self):
        self.assertEqual(max(4,1), 4, "x mayor que y")

class Ej2Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min(1,2), 1, "x menor que y")

    def test_2(self):
        self.assertEqual(min(4,-2), -2, "x mayor que y")

class Ej3y4Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sumar_alternativa(1,2), 3, "sumar 1 + 2")

    def test_2(self):
        self.assertEqual(restar(1,2), -1, "restar 2 - 1")

class Ej5Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(signo(-20), -1)
        
    def test_2(self):
        self.assertEqual(signo(20), 1)

class Ej6Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fabs(-10), 10, "Modulo de -10")
    
    # def test_2(self):
    #     self.assertEqual(fabs(20), 20, "Modulo de 20")

class Ej7Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fabs_dos(-10), 10, "Modulo de -10")
    
    def test_2(self):
        self.assertEqual(fabs_dos(20), 20, "Modulo de 20")

class Ej8Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mult10(10), 100, "10 x 10")
    
    # def test_2(self):
    #     self.assertEqual(mult10(-5), -25, "(-5) x 10")

class Ej9Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sumar(3,-2), 1, "y negativo")

    def test_2(self):
        self.assertEqual(sumar(3,1), 4, "y positivo")

class Ej10Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mcd(2,3), 1)
    
    def test_2(self):
        self.assertEqual(mcd(5,0), 5)

class Ej11Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(triangle(2,0,4), 4, "Un angulo menor o igual a 0")
    
    def test_2(self):
        self.assertEqual(triangle(2,2,4), 4,"(a + b < c) & (a + c > b) & (b + c > a)")

    def test_3(self):
        self.assertEqual(triangle(2,2,2), 1, "Todos iguales (a == b == c)")

    def test_4(self):
        self.assertEqual(triangle(3,4,3), 2, "(a != b) & (b != c) & (a == c)")

    def test_5(self):
        self.assertEqual(triangle(5,4,6), 3, "Ninguno es igual a alguno (a != b != c)")

class Ej12Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(multByAbs(2,-5), 10, "2 por -5")
    
    # def test_2(self):
    #     self.assertEqual(multByAbs(2,3), 6, "2 por 3")

class Ej13Tests(unittest.TestCase):
    def test_1(self):
        secuencia = [1,2,3]
        
        vaciarSecuencia(secuencia)

        self.assertEqual(secuencia, [0,0,0])

class Ej14Tests(unittest.TestCase):
    numeros: list[int] = [2,4,6,8,10]

    def test_1(self):
        self.assertEqual(existeElemento(self.numeros,1), False)
    
    def test_2(self):
        self.assertEqual(existeElemento(self.numeros,2), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)