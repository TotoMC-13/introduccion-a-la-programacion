from queue import LifoQueue as Cola

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urgentes_copia: Cola[int] = Cola()
    postergables_copia: Cola[int] = Cola()
    res: Cola[int] = Cola()

    while not urgentes.empty():
        paciente = urgentes.get()
        urgentes_copia.put(paciente)
    
    while not postergables.empty():
        paciente = postergables.get()
        postergables_copia.put(paciente)

    while not urgentes_copia.empty():
        urgente = urgentes_copia.get()
        postergable = postergables_copia.get()

        res.put(urgente)
        res.put(postergable)
        urgentes.put(urgente)
        postergables.put(postergable)
    
    return res

# # Crear las colas de ejemplo
# urgentes = Cola()
# postergables = Cola()

# # Agregar elementos a las colas
# for paciente in [10, 20, 30]:
#     urgentes.put(paciente)

# for paciente in [40, 50, 60]:
#     postergables.put(paciente)

# print(orden_de_atencion(urgentes, postergables).queue)

def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    desvio: str = "me desvío siempre"
    sigo: str = "me la banco y no me desvío"
    res: dict[str, int] = {}

    for jugador in estrategias:
        puntaje: int = 0

        for enemigo in estrategias:
            estrategia_jugador: str = estrategias[jugador]
            estrategia_enemigo: str = estrategias[enemigo]

            if not jugador == enemigo:
                if estrategia_jugador == estrategia_enemigo == sigo:
                    puntaje -= 5
                elif estrategia_jugador == estrategia_enemigo == desvio:
                    puntaje -= 10
                elif estrategia_jugador == desvio != estrategia_enemigo:
                    puntaje -= 15
                elif estrategia_jugador == sigo != estrategia_enemigo:
                    puntaje += 10

        res[jugador] = puntaje
    
    return res

# estrategias = {
#     "Juan": "me desvío siempre",
#     "Ana": "me la banco y no me desvío",
#     "Luis": "me desvío siempre",
#     "Sofía": "me la banco y no me desvío"
# }

# print(torneo_de_gallinas(estrategias))

def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    gano_x: bool = False
    gano_o: bool = False
    tablero_transpuesto: list[list[str]] = transponer(tablero)

    for fila in tablero_transpuesto:
        if tres_consecutivos(fila) == "X":
            gano_x = True
        elif tres_consecutivos(fila) == "O":
            gano_o = True
    
    if gano_x == gano_o == True:
        return 3
    elif gano_x:
        return 1
    elif gano_x == gano_o == False:
        return 0

def tres_consecutivos(elementos: list[str]) -> str: # Devuelve None si es falso, devuelve el elemento si es verdadero.
    cantidad_seguidos: int = 1
    elemento_actual: str = elementos[0]

    for i in range(len(elementos) - 1):
        if elementos[i] == elementos[i + 1]:
            cantidad_seguidos += 1
            if cantidad_seguidos == 3:
                return elemento_actual
        else:
            elemento_actual = elementos[i + 1]
            cantidad_seguidos = 1
    
    return None

def transponer(matriz: list[list[str]]) -> list[list[str]]:
    matriz_resultado: list[list[str]] = []

    for i in range(len(matriz[0])):
        matriz_resultado.append(columna(matriz, i))
    
    return matriz_resultado

def columna(matriz: list[list[str]], n: int) -> list[str]:
    columna: list[str] = []

    for fila in matriz:
        columna.append(fila[n])

    return columna

# tablero = [
#     ["X", "O", " ", " ", " "],
#     ["X", "O", " ", " ", " "],
#     ["X", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " "],
#     [" ", " ", " ", " ", " "]
# ]

# print(quien_gano_el_tateti_facilito(tablero))

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    texto_recortado: str = texto
    cantidad_palindromos: int = 0
    
    while len(texto_recortado) > 0:
        nuevo_texto: str = ""
        i = 0

        if es_palindromo(texto_recortado):
            cantidad_palindromos += 1
        
        for _ in range(len(texto_recortado) - 1):
            i += 1
            nuevo_texto += texto_recortado[i]

        texto_recortado = nuevo_texto

    return cantidad_palindromos

def es_palindromo(palabra: str) -> bool:
    inversa: str = ""

    for letra in palabra:
        inversa = letra + inversa

    return palabra == inversa

# def probar_casos_de_prueba():
#     casos = [
#         ("Diego", 1),
#         ("ana", 2),
#         ("radar", 2),
#         ("abc", 1),
#         ("level", 2),
#         ("aabbaa", 3),
#     ]

#     for texto, esperado in casos:
#         resultado = cuantos_sufijos_son_palindromos(texto)
#         print(f"Texto: {texto} -> Resultado: {resultado} (Esperado: {esperado})")

# probar_casos_de_prueba()
