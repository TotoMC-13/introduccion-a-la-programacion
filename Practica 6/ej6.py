def uno_al_diez() -> int:
    i: int = 0

    while i < 10:
        i += 1
        print(i)

def pares_diez_al_cuarenta() -> int:
    i: int = 10

    while i <= 40:
        print(i)
        i += 2

def imprimir_eco_diez_veces() -> str:
    i: int = 0

    while i < 10:
        i += 1
        print("eco")

def cuenta_regresiva(segundos: int) -> str:
    while segundos != 0:
        print(segundos)
        segundos -= 1
    
    print("Despegue")

def viaje_en_el_tiempo(partida: int, llegada: int) -> str:
    while partida > llegada:
        partida -= 1
        print(f"Viajo un año al pasado, estamos en el año: {partida}")

def monitoreo_viaje(partida: int) -> str:
        objetivo = -384

        while (partida > objetivo) and abs((abs(objetivo) - abs(partida))) > abs((abs(objetivo) - (abs(partida) - 20))):
                partida -= 20
                print(f"Viajo un año al pasado, estamos en el año: {partida}")
        
        print(f"Llegamos al año mas cercano: {partida}")

monitoreo_viaje(2000)