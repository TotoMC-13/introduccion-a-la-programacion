def imprimir_saludo(nombre: str):
    print("Hola", nombre)

def raiz_cuadrada_de(numero: int) -> int:
    return numero**(1/2)

def farenheit_a_celsius(temp_far: int) -> int:
    return ((temp_far - 32) * 5) / 9

def imprimir_dos_veces(estribillo: str) -> str:
    estribillo = f"{estribillo}\n"
    return estribillo*2

def es_multiplo_de(n: int, m:int) -> bool:
    return n % m == 0

def es_par(numero: int) -> bool:
    return numero % 2 == 0

# Alternativa:
# def es_par(numero: int) -> bool:
#     return es_multiplo_de(numero, 2)

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return (comensales*min_cant_de_porciones) / 8