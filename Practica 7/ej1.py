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

def tres_vocales(palabra: str) -> bool:
    vocales = ["a","e","i","o","u"]

    for i in palabra:
        if i in vocales:
            vocales.remove(i)

    if len(vocales) <= 2:
        return True
    else:
        return False

def pos_seq_larga(numeros: list[int]) -> int:
    tuplas: list[tuple[int,int]] = longitud_secuencias(numeros)
    sec_mas_larga: tuple[int,int] = tuplas[0]

    for i in range(len(tuplas)):
        if sec_mas_larga[1] < tuplas[i][1]:
            sec_mas_larga = tuplas[i]
    
    return sec_mas_larga[0]

def longitud_secuencias(numeros: list[int]) -> list[tuple[int,int]]: #tuple[pos_inicio, longitud]
    tuplas: list[tuple[int,int]] = []
    long_sec: int = 1
    pos_inicial: int = 0

    for i in range(len(numeros)-1):
        if numeros[i] == numeros[i+1]:
            long_sec += 1
        else:
            tuplas.append((pos_inicial,long_sec))
            long_sec = 1
            pos_inicial = i+1
    
    tuplas.append((pos_inicial,long_sec))

    return tuplas

def cant_digitos_impares(numeros: list[int]) -> int:
    impares: int = 0

    for numero in numeros:
        while numero > 0:
            if numero % 2 != 0:
                impares += 1
            numero = numero // 10
    
    return impares