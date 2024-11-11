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
    apariciones: int = 0

    #Integracion de split()
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

    for clave in palabras:
       if clave == palabra:
           apariciones += 1

    return apariciones

#print("Cantidad de apariciones:", cantidad_de_apariciones("Practica 8\ejercicios21.3.txt", "aa"))

def clonar_sin_comentarios(nombre_archivo: str):
    archivo = open(nombre_archivo, "r+")
    contenido = archivo.readlines()

    for linea in contenido:
        palabras = linea.split()

        if palabras[0][0] == "#":
            pass
        else:
            archivo.write(linea)
    
    archivo.close()

# clonar_sin_comentarios("Practica 8\ejercicio22.txt")

def invertir_lineas(nombre_archivo: str):
    archivo = open(nombre_archivo, "r+")
    contenido = archivo.readlines()

    for i in range(len(contenido) - 1, -1, -1):
        if i == len(contenido) - 1:
            archivo.write(contenido[i]+"\n")
        else:
            archivo.write(contenido[i])
    
    archivo.close()

# invertir_lineas("Practica 8\ejercicio23.txt")

def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "r+")
    archivo.write(frase)
    archivo.close()

# agregar_frase_al_final("Practica 8\ejercicio23.txt", "test")

def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()

    archivo = open(nombre_archivo, "w")
    archivo.write(frase + "\n" + contenido)
    archivo.close()

# agregar_frase_al_principio("Practica 8/ejercicio23.txt", "test")