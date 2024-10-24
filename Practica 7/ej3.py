from random import randint

def estudiantes() -> list[str]:
    nombre: str = ""
    nombres: list[str] = []

    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre == "listo" or nombre == "":
            break
        nombres.append(nombre)

    return nombres

def historial_sube() -> list[tuple[str, int]]:
    historial: list[tuple[str, int]] = []
    while True:
        accion: str = input("Ingrese la accion: ")
        if accion == "X":
            break
        elif accion != "C" and accion != "D":
            print("Accion invalida")
            continue

        monto: int = int(input("Ingrese el monto: "))

        historial.append((accion, monto))
    
    return historial

def jugar_siete_y_medio() -> list[int]: # S = sacar carta, P = plantarse.
    historial_cartas: list[int] = []
    suma_total: float = 0
    carta_actual: int

    while True:
        print(f"Suma total: {suma_total}")
        if suma_total > 7.5:
            print("Te pasaste de 7.5, fin del juego.")
            break
        
        eleccion: str = input("Desea sacar otra carta (S) o plantarse (P): ")

        if eleccion == "P":
            break
        elif eleccion == "S":
            carta_actual = randint(1,12)
            while carta_actual == 8 or carta_actual == 9:
                carta_actual = randint(1,12)
            historial_cartas.append(carta_actual)
            if carta_actual in range(10,13):
                suma_total += 0.5
            else:
                suma_total += carta_actual

        print(f"Carta obtenida: {carta_actual}")

    print(f"Suma final: {suma_total}")
    return historial_cartas

def password_gen() -> str:
    password: str = input("Ingrese su nuevo password: ")

    if len(password) > 8 and tiene_minus(password) and tiene_mayus(password) and tiene_num(password):
        return "verde"
    elif len(password) < 5:
        return "roja"
    else:
        return "amarilla"

def tiene_minus(password:  str) -> bool:
    minus: str = "abcdefghijklmnopqrstuvwxyz"

    for i in password:
        if i in minus:
            return True
        
    return False

def tiene_mayus(password:  str) -> bool:
    mayus: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in password:
        if i in mayus:
            return True
        
    return False

def tiene_num(password:  str) -> bool:
    numeros: str = "0123456789"

    for i in password:
        if i in numeros:
            return True
        
    return False