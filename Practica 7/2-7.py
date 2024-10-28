from random import randint

def matriz_cuadrada_random(dimension: int, min: int = 0, max: int = 20) -> list[list[int]]: # Args: min y max son los minimos y maximos valores que puede tener la matriz. Defaults: min = 0, max = 20.
    matriz: list[list[int]] = []
    columna: list[int] = []
    dimension_actual: int = 0
    longitud_columna: int = 0

    while dimension_actual < dimension:
        while longitud_columna < dimension:
            columna.append(randint(min,max))
            longitud_columna += 1
        
        matriz.append(columna)
        longitud_columna = 0
        columna = []
        dimension_actual += 1
    
    return matriz

def elevar_matriz(matriz: list[list[int]]) -> list[list[int]]:
    matriz_res: list[list[int]] = []
    nueva_fila: list[int] = []
    nuevo_numero: int = 0

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for k in range(len(matriz)):
                nuevo_numero += (matriz[i][k]*matriz[k][j])
            nueva_fila.append(nuevo_numero)
            nuevo_numero = 0
        matriz_res.append(nueva_fila)
        nueva_fila = []
        
    return matriz_res

print(elevar_matriz([[3,2,2],[0,5,3],[3,4,5]]))