def ultima_aparicion(s: list[int], e: int) -> int:
    index: int = 0
    res: int = 0

    for elemento in s:
        if e == elemento:
            res = index
        
        index += 1

    return res

# # Casos de prueba
# casos = [
#     ([1, 2, 3, 4, 2, 5], 2),  # El 2 aparece por última vez en el índice 4
#     ([7, 8, 9, 10, 9], 9),    # El 9 aparece por última vez en el índice 4
#     ([5, 5, 5, 5], 5),        # El 5 aparece por última vez en el índice 3
#     ([1, 2, 3], 4),           # El 4 no está en la lista, devuelve 0 (según tu lógica actual)
#     ([], 3),                  # Lista vacía, devuelve 0
#     ([1, 2, 3, 2, 4], 6)      # El 6 no está en la lista, devuelve 0
# ]

# # Ejecutar pruebas
# for s, e in casos:
#     print(f"Lista: {s}, Elemento: {e} => Última aparición: {ultima_aparicion(s, e)}")

def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    res: list[int] = []

    for i in s:
        if not pertenece(t, i):
            res.append(i)
    
    for i in t:
        if not pertenece(s, i):
            res.append(i)
    
    return res

def pertenece(elementos: list[int], elemento: int) -> bool:
    for i in elementos:
        if i == elemento:
            return True
        
    return False

# # Casos de prueba
# casos = [
#     ([1, 2, 3], [3, 4, 5]),     # Elementos exclusivos: [1, 2, 4, 5]
#     ([1, 2, 2, 3], [3, 3, 4]),  # Elementos exclusivos: [1, 2, 2, 4]
#     ([], [1, 2, 3]),            # Elementos exclusivos: [1, 2, 3]
#     ([1, 2, 3], []),            # Elementos exclusivos: [1, 2, 3]
#     ([1, 2, 3], [1, 2, 3]),     # Elementos exclusivos: []
#     ([7, 8, 9], [10, 11, 7]),   # Elementos exclusivos: [8, 9, 10, 11]
#     ([1, 2, 3, 4], [4, 3, 2, 1]) # Elementos exclusivos: []
# ]

# # Ejecutar pruebas
# for s, t in casos:
#     print(f"Lista S: {s}, Lista T: {t} => Elementos exclusivos: {elementos_exclusivos(s, t)}")

def contar_traducciones_iguales(ing: dict[str, str], ale: dict[str, str]) -> int:
    res: list[str] = []
    palabras_aleman: list[str] = []

    for palabra in ale:
        palabras_aleman.append(ale[palabra])

    for i in ing:
        if pertenece(palabras_aleman, ing[i]):
            res.append(ing[i])

    return len(res)


# diccionario_ing = {'hola': 'hello', 'gato': 'cat', 'perro': 'dog'}
# diccionario_ale = {'hola': 'hello', 'gato': 'Katze', 'perro': 'hund'}

# resultado = contar_traducciones_iguales(diccionario_ing, diccionario_ale)
# print(resultado)  # Debería imprimir 1, ya que "hola" tiene la misma traducción en ambos idiomas

def convertir_a_diccionario(lista: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}

    for numero in lista:
        if pertenece(res, numero):
            res[numero] += 1
        else:
            res[numero] = 1
    
    return res

# print(convertir_a_diccionario([1,2,3,2,1,1]))
