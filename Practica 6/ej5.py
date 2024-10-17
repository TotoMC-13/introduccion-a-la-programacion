def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        numero = numero * 2

    return numero

def doble_mult_3_o_triple_mult_9(numero: int) -> int:
    if numero % 9 == 0:
        numero = numero * 3
    elif numero % 3 == 0:
        numero = numero * 2
    
    return numero

def lindo_nombre(nombre: str) -> str:
    texto: str

    if len(nombre) >= 5:
        (texto) = "Tu nombre tiene muchas letras!"
    else:
        texto = "Tu nombre tiene menos de 5 caracteres."

    return texto

def el_rango(numero: int):
    if numero < 5:
        print("Menor a 5")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

def apto_jubilacion(sexo: str, edad: int):
    if edad < 18 or (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65):
        print("Andá de vacaciones.")
    else:
        print("Te toca trabajar.")