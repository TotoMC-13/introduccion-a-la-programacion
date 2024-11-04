def contar_lineas(nombre_archivo: str) -> int:
    contador: int = 0
    archivo = open(nombre_archivo, "r")

    for i in archivo.readlines():
        contador += 1

    archivo.close()

    return contador

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    archivo = open(nombre_archivo, "r")
    existe_palabra: bool = False

    for linea in archivo.readlines():
        if palabra in linea:
            existe_palabra = True

    archivo.close()

    return existe_palabra

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readlines()
    palabras: list[str] = []
    nueva_palabra: str = ""
    contador: dict = {}

    for linea in contenido:
        for letra in linea:
            if letra != " " and letra != "\n" and linea:
                nueva_palabra += letra
            elif linea != "\n":
                palabras.append(nueva_palabra)
                nueva_palabra = ""
    
    archivo.close()

    if nueva_palabra:
        palabras.append(nueva_palabra)
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    max_palabra: str = ""
    max_apariciones: int = 0

    for clave in contador:
        valor_actual: int = contador[clave]

        if valor_actual > max_apariciones:
            max_apariciones = valor_actual
            

    return contador

print(cantidad_de_apariciones("/home/Estudiante/Documentos/introduccion-a-la-programacion/Practica 8/ejercicios21-27.txt", "a"))