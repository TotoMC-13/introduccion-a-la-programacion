# {"pedro": [10, 12, 9, 28]} -> {"pedro": (4, 14.75)}
# {nombre: [tiempos]} -> {nombre: (len(tiempos), promedio)}
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}

    for jugador in registro:
        tiempos = registro[jugador]

        if not pertenece(res, jugador):
            res[jugador] = (len(tiempos), promedio(tiempos))
    
    return res

def promedio(numeros: list[int | float]) -> float:
    return sumar_todos(numeros) / len(numeros)

def sumar_todos(numeros: list[int | float]) -> int | float:
    suma: int | float = 0

    for i in numeros:
        suma += i

    return suma

# No declare los tipos porque la voy a reutilizar para otros ejercicios.
def pertenece(elementos, elemento) -> bool:
    for i in elementos:
        if i == elemento:
            return True
        
    return False

# print(promedio_de_salidas({"pedro": [10, 12, 9, 28], "juan": [5, 5, 5, 5, 5]}))

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    indice: int = 0
    indice_menor_tiempo: int = 0
    menor_tiempo: int = tiempos_salas[0]

    for tiempo in tiempos_salas:
        if tiempo < menor_tiempo:
            menor_tiempo = tiempo
            indice_menor_tiempo = indice
        indice += 1
    
    return indice_menor_tiempo

# print(tiempo_mas_rapido([1,2,3,4,5,6]))

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    indice: int = 0
    inicio: int = 0
    final: int = 0
    secuencias: list[tuple[int, int, int]] = []

    for tiempo in tiempos:
        if tiempo < 1 or tiempo > 60:
            final = indice - 1
            secuencias.append((inicio, final, final - inicio + 1))
            inicio = indice + 1
        
        indice += 1

    if not (tiempo < 1 or tiempo > 60):
        final = indice - 1
        secuencias.append((inicio, final, final - inicio + 1))

    tupla_ganadora: tuple[int, int, int] = mayor_z_tupla(secuencias)

    return (tupla_ganadora[0], tupla_ganadora[1])

def mayor_z_tupla(tuplas: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    mayor_z: int = tuplas[0][2]
    res: tuple[int, int, int] = tuplas[0]

    for tupla in tuplas:
        if tupla[2] > mayor_z:
            res = tupla
            mayor_z = tupla[2]

    return res

# print(racha_mas_larga([0, 5, 7, 61, 2, 3, 4, 61, 1, 2, 3]))

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    indice: int = 0
    indices: list[int] = []

    for sala in amigos_por_salas:
        if sala[0] == sala[1] == sala[3] == 0  and sala[2] != 0:
            indices.append(indice)
        
        indice += 1

    return indices

# print(escape_en_solitario([[2,4,0,1], [0,0,1,0], [8,4,60,5], [0,0,14,0]]))