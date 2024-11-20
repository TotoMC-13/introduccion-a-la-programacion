def ceros_en_posiciones_pares(numeros: list[int]) -> list[int]:
    for i in range(len(numeros)):
        if i % 2 == 0:
            numeros[i] = 0
    return numeros

def ceros_en_posiciones_pares2(numeros: list[int]) -> list[int]:
    numeros_con_ceros: list[int] = []
    
    for i in range(len(numeros)):
        if i % 2 == 0:
            numeros_con_ceros.append(0)
        else:
            numeros_con_ceros.append(numeros[i])
    
    return numeros_con_ceros

def sin_vocales(palabra: str) -> str:
    vocales:str = "aeiou"
    nueva_palabra:str = ""

    for i in palabra:
        if i not in vocales:
            nueva_palabra += i
    
    return nueva_palabra

def reemplazar_vocales(palabra: str) -> str:
    vocales:str = "aeiou"
    nueva_palabra:str = ""

    for i in palabra:
        if i not in vocales:
            nueva_palabra += i
        else:
            nueva_palabra += " "
    
    return nueva_palabra

def dar_vuelta(palabra: str) -> str:
    palabra_invertida: str = ""
    for i in palabra:
        palabra_invertida = i + palabra_invertida
    return palabra_invertida

def eliminar_repetidos(palabra: str) -> str:
    nueva_palabra: str = ""

    for i in palabra:
        if i not in nueva_palabra:
            nueva_palabra += i

    return nueva_palabra

def resultadoMateria(notas: list[int]) -> int:
    for i in notas:
        if i < 4:
            return 3
    
    if promedio(notas) >= 7:
        return 1
    elif promedio(notas) >= 4:
        return 2
    else:
        return 3

def promedio(notas: list[int]) -> float:
    suma: int = 0
    
    for i in notas:
        suma += i

    return suma / len(notas)

def movimientos_cuenta(movimientos: list[tuple[str,int]]) -> int:
    balance: int = 0

    for movimiento in movimientos:
        if movimiento[0] == "R":
            balance -= movimiento[1]
        elif movimiento[0] == "I":
            balance += movimiento[1]
    
    return balance