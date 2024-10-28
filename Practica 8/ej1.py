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

