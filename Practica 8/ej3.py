def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readline()
    palabras: list[str] = []
    nueva_palabra: str = ""
    contador: dict = {}

    for letra in contenido:
        if letra != " ":
            nueva_palabra += letra
        else:
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

# agrupar_por_longitud("Practica 8\ejercicio16.txt")

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

