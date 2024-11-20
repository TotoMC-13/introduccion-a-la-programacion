from math import floor

def filtrar_codigos_primos(codigos_barras: list[int]) -> list[int]:
    res: list[int] = []
    
    for numero in codigos_barras:
        if es_primo(sumar_todos(ultimos_3_digitos(numero))):
            res.append(numero)

    return res

def es_primo(numero: int) -> bool:
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def ultimos_3_digitos(numero: int) -> list[int]:
    res: list[int] = []

    for _ in range(0,3):
        res.append(floor(numero % 10))
        numero = numero / 10

    return res

def sumar_todos(numeros: list[int | float]) -> int | float:
    suma: int | float = 0

    for i in numeros:
        suma += i

    return suma

# print(filtrar_codigos_primos([1234, 5678, 9123, 3456, 7890, 2345, 6789, 4567, 8910, 1235]))

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    stocks_pasados: dict[str, list[int]]  = {} # {"manzana": [minimo stock, maximo stock]}
    res: dict[str, tuple[int, int]] = {}

    for producto in stock_cambios:
        nombre: str = producto[0]
        stock_actual: int = producto[1]

        if nombre in stocks_pasados:
            minimo_pasado: int = stocks_pasados[nombre][0]
            maximo_pasado: int = stocks_pasados[nombre][1]
            
            if stock_actual < minimo_pasado:
                stocks_pasados[nombre][0] = stock_actual
            elif stock_actual > maximo_pasado:
                stocks_pasados[nombre][1] = stock_actual
        else:
            stocks_pasados[nombre] = [stock_actual, stock_actual]
    
    for producto in stocks_pasados:
        stock_minimo = stocks_pasados[producto][0]
        stock_maximo = stocks_pasados[producto][1]

        res[producto] = (stock_minimo, stock_maximo)

    return res

# print(stock_productos([
#     ("manzana", 1), 
#     ("manzana", 10), 
#     ("manzana", 9), 
#     ("manzana", 11),
#     ("banana", 5),
#     ("banana", 3),
#     ("banana", 8),
#     ("banana", 2),
#     ("pera", 12),
#     ("pera", 15),
#     ("pera", 10),
#     ("pera", 18),
#     ("naranja", 7),
#     ("naranja", 6),
#     ("naranja", 9),
#     ("naranja", 5)
# ]))

def responsable_por_turno(grilla: list[list[str]]) -> list[tuple[bool, bool]]:
    horarios_primera_mitad: list[str] = [] # De 9 a 12
    horarios_segunda_mitad: list[str] = [] # De 14 a 17
    grilla_transpuesta: list[list[str]] = matriz_transpuesta(grilla)
    res: list[tuple[bool, bool]] = []

    for horarios in grilla_transpuesta:
        horarios_primera_mitad = []
        horarios_segunda_mitad = []

        for i in range(0,4):
            horarios_primera_mitad.append(horarios.pop(0))

        for i in range(0,4):
            horarios_segunda_mitad.append(horarios.pop(0))
    
        res.append((todos_iguales(horarios_primera_mitad), todos_iguales(horarios_segunda_mitad)))

    return res

def matriz_transpuesta(matriz: list[list[str]]) -> list[list[str]]:
    matriz_resultado: list[list[str]] = []
    
    for i in range(len(matriz[0])):  # Cambiar len(matriz) por len(matriz[0])
        matriz_resultado.append(columna(matriz, i))
    
    return matriz_resultado

def columna(matriz: list[list[str]], n_columna: int) -> list[str]:
    columna: list[str] = []

    for fila in matriz:
        columna.append(fila[n_columna])
    
    return columna

def todos_iguales(elementos: list[str]) -> bool:
    primer_elemento: str = elementos[0]

    for i in range(1, len(elementos)):
        if elementos[i] != primer_elemento:
            return False
    
    return True

# grilla_horaria = [
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 9 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 10 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 11 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 12 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"],  # 2 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"],  # 3 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"],  # 4 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"]   # 5 PM
# ]

# grilla_horaria_prueba = [
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 9 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 10 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 11 AM
#     ["Juan", "Ana", "Laura", "Juan", "Pedro", "Ana", "Laura"],   # 12 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"],  # 2 PM
#     ["Pedro", "Luis", "Juan", "Carlos", "Pedro", "Luis", "Juan"], # 3 PM - Diferente responsable en jueves
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"],  # 4 PM
#     ["Pedro", "Luis", "Juan", "Luis", "Pedro", "Luis", "Juan"]   # 5 PM
# ]


# print(responsable_por_turno(grilla_horaria_prueba))

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    inicio: int = 0
    final : int = 0
    indice: int = 0
    secuencias: list[tuple[int, int, int]] = [] # [(inicio, fin, longitud)]

    for tipo in tipos_pacientes_atendidos:
        if tipo != "perro" and tipo != "gato":
            final = indice - 1
            secuencias.append((inicio, final, final - inicio + 1))
            inicio = indice + 1
        
        indice += 1
        
    if tipo == "gato" or tipo == "perro":
        final = indice - 1
        secuencias.append((inicio, final, final - inicio + 1))

    return mayor_z_tupla(secuencias)

def mayor_z_tupla(tuplas: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    mayor_z: int = tuplas[0][2]
    res: tuple[int, int, int] = tuplas[0]

    for tupla in tuplas:
        if tupla[2] > mayor_z:
            res = tupla
            mayor_z = tupla[2]

    return res

    # print(subsecuencia_mas_larga(["perro", "pajaro", "gato", "perro", "pajaro","perro","gato","gato"]))