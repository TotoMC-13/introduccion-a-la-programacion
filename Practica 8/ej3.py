from queue import LifoQueue as Pila

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readlines()
    palabras: list[str] = []
    nueva_palabra: str = ""
    contador: dict = {}

    for linea in contenido:
        for letra in linea:
            if letra != " " and letra != "\n":
                nueva_palabra += letra
            elif linea != "\n":
                palabras.append(nueva_palabra)
                nueva_palabra = ""
    
    if nueva_palabra:
        palabras.append(nueva_palabra)
    
    for palabra in palabras:
        if len(palabra) in contador:
            contador[len(palabra)] += 1
        else:
            contador[len(palabra)] = 1

    archivo.close()

    return contador

#print(agrupar_por_longitud("Practica 8\ejercicios21.3.txt"))

# list[tuple[nombre,nota_examen]] -> []
def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
    notas_estudiantes: dict[str,list[int]] = {}
    promedios_estudiantes: dict[str,float] = {}

    for estudiante in notas:
        if estudiante[0] in notas_estudiantes:
            notas_estudiantes[estudiante[0]].append(estudiante[1])
        else:
            notas_estudiantes[estudiante[0]] = [estudiante[1]]
    
    for estudiante, notas in notas_estudiantes.items():
        promedios_estudiantes[estudiante] =  sumar_todo(notas) / len(notas)

    return promedios_estudiantes

def sumar_todo(numeros: list[int]) -> int:
    suma = 0

    for numero in numeros:
        suma += numero

    return suma

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readlines()
    palabras: dict[str, int] = {}
    nueva_palabra: str = ""
    repeticiones_max: int = 0
    mas_repetida: str

    for linea in contenido:
        for letra in linea:
            if letra != " " and letra != "\n":
                nueva_palabra += letra
            elif letra != "\n":
                if nueva_palabra not in palabras:
                    palabras[nueva_palabra] = 1
                else:
                    palabras[nueva_palabra] += 1
                nueva_palabra = ""
    
    archivo.close()

    if nueva_palabra and nueva_palabra not in palabras:
        palabras[nueva_palabra] = 1
    elif nueva_palabra:
        palabras[nueva_palabra] += 1
    
    for palabra in palabras:
        if palabras[palabra] > repeticiones_max:
            repeticiones_max = palabras[palabra]
            mas_repetida = palabra

    return mas_repetida

print(la_palabra_mas_frecuente("Practica 8\ejercicio21.3.txt"))

historial: dict[str, Pila[str]] = {}

def visitar_sitio(usuario: str, sitio: str) -> dict[str, Pila[str]]:
    global historial
    sitios_visitados: Pila[str] = Pila()

    if usuario in historial:
        historial[usuario].put(sitio)
    else:
        historial[usuario] = sitios_visitados
        sitios_visitados.put(sitio)

def navegar_atras(usuario: str) -> dict[str, Pila[str]]:
    global historial

    sitio_actual = historial[usuario].get()
    sitio_anterior = historial[usuario].get()

    historial[usuario].put(sitio_anterior)
    historial[usuario].put(sitio_actual)
    historial[usuario].put(sitio_anterior)

inventario: dict[str, dict[str, float | int]] = {}

def agregar_producto(inventario: dict[str, dict[str, float | int]], nombre: str, precio: float, cantidad: int):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def actualizar_stock(inventario: dict[str, dict[str, float | int]], nombre: str, cantidad):
    inventario[nombre]["cantidad"] += cantidad

def actualizar_precios(inventario: dict[str, dict[str, float | int]], nombre: str, precio: int):
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario: dict[str, dict[str, float | int]]) -> float:
    valor_inventario: float = 0

    for producto in inventario:
        valor_inventario += inventario[producto]["cantidad"] * inventario[producto]["precio"]
    
    return valor_inventario

# inventario = {}
# agregar_producto(inventario, "Camisa", 20.0, 50)
# agregar_producto(inventario, "Pantalon", 30.0, 30)
# actualizar_stock(inventario, "Camisa", 10)
# valor_total = calcular_valor_inventario(inventario)
# print("Valor total del inventario:", valor_total) # Deber ́ıa imprimir 2100.0