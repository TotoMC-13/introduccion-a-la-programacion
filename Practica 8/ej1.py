from queue import LifoQueue as Pila
from random import randint

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    numeros: Pila[int] = Pila()
    cant_numeros: int = 0

    while cant_numeros < cantidad + 1:
        cant_numeros += 1
        numeros.put(randint(desde,hasta))
    
    return numeros

def cantidad_elementos(p: Pila[int]) -> int:
    cantidad: int = 0
    nueva_pila: Pila[int] = Pila()

    while not p.empty():
        elem = p.get()
        nueva_pila.put(elem)
        cantidad += 1

    while not nueva_pila.empty():
        p.put(nueva_pila.get())

    return cantidad

def buscar_el_maximo(p: int) -> int:
    numeros: list[int] = []
    nueva_pila: Pila[int] = Pila()

    while not p.empty():
        elem = p.get()
        nueva_pila.put(elem)
        numeros.append(elem)

    while not nueva_pila.empty():
        p.put(nueva_pila.get())

    return maximo_elem(numeros)

def maximo_elem(numeros: list) -> int:
    maximo_numero: int = numeros[0]
    
    for i in numeros:
        if i > maximo_numero:
            maximo_numero = i

    return maximo_numero

def buscar_nota_maxima(p: Pila[tuple[str,int]]) -> tuple[str,int]:
    numeros: list[int] = []
    nueva_pila: Pila[int] = Pila()

    while not p.empty():
        elem = p.get()
        nueva_pila.put(elem)
        numeros.append(elem)

    while not nueva_pila.empty():
        p.put(nueva_pila.get())

    return maximo_elem(numeros)

def esta_bien_balanceada(s: str) -> bool:
    balance: int = 0

    for i in s:
        if i == "(":
            balance += 1
        elif i == ")":
            balance -= 1
        
        if balance < 0:
            return False

    return balance == 0 
    
def evaluar_expresion(expresion: str) -> float:
    numeros: Pila[int] = Pila()
    operadores: Pila[str] = Pila()
    numeros_str: str = "1234567890"
    operadores_str: list[str] = ["+","-","*","/"]

    for i in expresion[::-1]:
        if i in numeros_str:
            numeros.put(int(i))
        elif i in operadores_str:
            operadores.put(i)

    while cantidad_elementos(numeros) > 1:
        numero_uno = numeros.get()
        numero_dos = numeros.get()
        operador = operadores.get()

        if operador == "+":
            numeros.put(numero_uno + numero_dos)
        elif operador == "-":
            numeros.put(numero_uno - numero_dos)
        elif operador == "*":
            numeros.put(numero_uno * numero_dos)
        elif operador == "/":
            numeros.put(numero_uno / numero_dos)

    return numeros.get()

def intercalar(p1: Pila, p2: Pila) -> Pila: # Me da una inmensa paja chequear si esta bien.
    intercalada: Pila = Pila()

    while not(p1.empty()) and not(p2.empty()):
        intercalada.put(p1.get())
        intercalada.put(p2.get())
    
    invertir_pila(intercalada)

    return intercalada

def invertir_pila(p: Pila) -> Pila:
    aux: Pila = Pila()
    
    while not p.empty():
        aux.put(p.get())
    
    while not aux.empty():
        p.put(aux.get())
    
    return p

