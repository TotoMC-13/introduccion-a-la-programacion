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