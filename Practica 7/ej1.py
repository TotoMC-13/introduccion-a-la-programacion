def pertenece(x, lista: list) -> bool:
    for i in lista:
        if i == x:
            return True
    
    return False

def pertenece2(x, lista: list) -> bool:
    return x in lista

def pertenece3(x, lista: list) -> bool:
    i: int = 0

    while i < len(lista):
        if x == lista[i]:
            return True
        
        i += 1
    
    return False

def divide_a_todos(x: int, numeros: list) -> bool:
    for i in numeros:
        if i % x != 0:
            return False
    
    return True

def suma_total(numeros: list) -> int:
    suma: int = 0
    
    for i in numeros:
        suma = suma + i
    
    return suma

def maximo(numeros: list) -> int:
    maximo_numero: int = numeros[0]
    
    for i in numeros:
        if i > maximo_numero:
            maximo_numero = i

    return maximo_numero

def minimo(numeros: list) -> int:
    minimo_numero: int = numeros[0]
    
    for i in numeros:
        if i < minimo_numero:
            minimo_numero = i

    return minimo_numero

def ordenados(numeros: list) -> bool:
    anterior: int = numeros[0]

    for i in numeros:
        if i < anterior:
            return False
        anterior = i

    return True

def pos_maximo(numeros: list) -> int:
    maximo_numero: int = numeros[0]
    posicion: int = -1
    posicion_maximo: int = 0
    
    for i in numeros:
        posicion += 1

        if i > maximo_numero:
            maximo_numero = i
            posicion_maximo = posicion

    return posicion_maximo

def pos_minimo(numeros: list) -> int:
    minimo_numero: int = numeros[0]
    posicion: int = -1
    posicion_minimo: int = 0
    
    for i in numeros:
        posicion += 1

        if i < minimo_numero:
            minimo_numero = i
            posicion_minimo = posicion

    return posicion_minimo

def palabra_7_o_mas(palabras: list) -> bool:
    for i in palabras:
        if len(i) >= 7:
            return True
    
    return False

def es_palindromo(palabra: str) -> bool:
    return palabra == palabra[::-1]

def tres_seguidos(numeros: list) -> bool:
    longitud = len(numeros)
    
    for i in range(longitud):

        if i <= longitud - 3 and numeros[i] == numeros[i + 1] == numeros[i + 2]:
            return True

        if i >= 2 and numeros[i] == numeros[i - 1] == numeros[i - 2]:
            return True
            
    return False
