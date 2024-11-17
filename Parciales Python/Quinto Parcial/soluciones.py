def ind_nesima_aparicion(s: list[int], n: int, elem: int) -> int:
    cant_apariciones: int = 0
    indice: int = 0

    for elemento in s:
        if elemento == elem:
            cant_apariciones += 1
        
        if cant_apariciones == n:
            return indice
        
        indice += 1

    if cant_apariciones < n:
        return -1
    
# print(ind_nesima_aparicion([1,2,3,1,3], 2, 1))

def mezclar(s1: list[int], s2: list[int]) -> list[int]:
    res: list[int] = []

    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])

    return res

# print(mezclar([1,3,5], [2,4,6]))

def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str, list[str]]) -> dict[str, list[str]]:
    res: dict[str, list[int]] = {}

    for caballo in caballos:
        res[caballo] = [0]*len(caballos)

    for carrera in carreras:
        posiciones: list[str] = carreras[carrera]
        indice: int = 0

        for caballo in posiciones:
            res[caballo][indice] += 1
            indice += 1

    return res

caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
                 "carrera2":["petisa", "mister", "linda", "luck"]}

# print(frecuencia_posiciones_por_caballo(caballos, carreras))

def matriz_capicua(matriz: list[list[int]]) -> bool:
    for fila in matriz:
        if not es_capicua(fila):
            return False
        
    return True

def es_capicua(lista: list[int]) -> bool:
    reversa: list[int] = []

    for elemento in lista:
        reversa = [elemento] + reversa
    
    return reversa == lista

# # Casos de prueba
# matrices = [
#     [[1, 2, 3, 2, 1], [4, 5, 5, 4], [6, 7, 6]],  # Todas las filas son capicúa
#     [[1, 2, 3], [4, 4, 4], [5, 6, 5]],          # Una fila no es capicúa (la primera)
#     [[1, 2, 1], [3, 3, 3], [7, 8, 9]],          # Una fila no es capicúa (la última)
#     [[1, 1, 1, 1], [2, 2], [3, 3, 3]],          # Todas las filas son capicúa (listas homogéneas)
#     [[1]],                                      # Una matriz de una fila y un elemento (siempre capicúa)
#     []                                          # Matriz vacía (considerada capicúa)
# ]

# for matriz in matrices:
#     print(f"Matriz: {matriz} => ¿Es capicúa?: {matriz_capicua(matriz)}")