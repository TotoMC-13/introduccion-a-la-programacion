import numpy as np

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

def es_matriz(matriz: list[list[int]]) -> bool:
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return False

    for i in range(len(matriz)-1):
        if len(matriz[i]) != len(matriz[i+1]):
            return False
    
    return True

def filas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    filas: list[bool] = []

    for fila in matriz:
        if not ordenados(fila):
            filas.append(False)
        else:
            filas.append(True)
        
    return filas
    
def ordenados(numeros: list) -> bool:
    anterior: int = numeros[0]

    for i in numeros:
        if i < anterior:
            return False
        anterior = i

    return True

def columna(matriz: list[list[int]], n_columna: int):
    columna: list[int] = []

    for fila in matriz:
        columna.append(fila[n_columna])
    
    return columna

def matriz_transpuesta(matriz: list[list[int]]) -> list[list[int]]:
    matriz_resultado: list[list[int]] = []
    
    for i in range(len(matriz[0])):
        matriz_resultado.append(columna(matriz, i))
    
    return matriz_resultado

def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    return filas_ordenadas(matriz_transpuesta(matriz))

def transponer(matriz: list[list[int]]) -> list[list[int]]:
    return matriz_transpuesta(matriz)

def quien_gana_tateti(tablero: list[list[str]]) -> int:  # 0 si gana O, 1 si gana X, 2 si es empate.
    matrices: list[list[list[str]]] = [tablero, matriz_transpuesta(tablero)]

    for matriz in matrices:
        for fila in matriz:
            if todos_iguales(fila) and fila[0] != "":
                return quien_gana(fila[0])

        if matriz == tablero:
            if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != "":
                return quien_gana(matriz[0][0])
            elif matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != "":
                return quien_gana(matriz[0][2])

    return 2

def quien_gana(ganador: str) -> int:
    if ganador == "O":
        return 0
    elif ganador == "X":
        return 1

def todos_iguales(numeros: list[int]) -> bool:
    for i in range(len(numeros)-1):
        if numeros[i] != numeros[i+1]:
            return False
        
    return True

def mul_matriz_aleatoria_n_veces(dimension: int, potencia: int) -> list[list[float]]:
    matriz = np.random.random((dimension, dimension)).tolist()
    print(matriz)

    while potencia > 0:
        potencia -= 1
        matriz = multiplicar_matrices(matriz, matriz)
    
    return matriz

def multiplicar_matrices(matriz_a: list[list[float]], matriz_b: list[list[float]]) -> list[list[float]]:
    resultado: list[list[float]] = []
    
    for i in range(len(matriz_a)):
        nueva_fila = []
        for j in range(len(matriz_b[0])):
            suma = 0
            for k in range(len(matriz_b)):
                suma += matriz_a[i][k] * matriz_b[k][j]
            nueva_fila.append(suma)
        resultado.append(nueva_fila)

    return resultado