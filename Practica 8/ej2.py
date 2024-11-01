from queue import Queue as Cola
from random import randint

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    res: Cola[int] = Cola()
    
    for _ in range(cantidad):
        res.put(randint(desde,hasta))
    
    return res

def cantidad_elementos(c: Cola) -> int:
    contador: int = 0
    c_aux: Cola = Cola()

    while not(c.empty):
        c_aux.put(c.get())
        contador += 1
    
    while not(c_aux.empty):
        c.put(c_aux.get())
    
    return contador

def buscar_el_maximo(numeros: Cola[int]) -> int:
    c_aux: Cola = Cola()
    elem = numeros.get()
    mayor_numero: int = elem
    c_aux.put(elem)
    
    while not(numeros.empty()):
        numero = numeros.get()
        c_aux.put(numero)

        if mayor_numero == 0 or mayor_numero <= numero:
            mayor_numero = numero

    while not(c_aux.empty()):
        numeros.put(c_aux.get())

    return mayor_numero

def nota_minima(notas: Cola[tuple[str,int]]) -> int:
    c_aux: Cola = Cola()
    elem = notas.get()
    nota_minima: int = elem[1]
    c_aux.put(elem)
    
    while not(notas.empty()):
        numero = notas.get()
        c_aux.put(numero)

        if nota_minima < numero[1]:
            nota_minima = numero[1]

    while not(c_aux.empty()):
        notas.put(c_aux.get())

    return nota_minima

# Hacer ejercicio 12, me da muchisima paja.
# def intercalar(c1: Cola, c2: Cola) -> Cola:

def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = []
    secuencia: Cola[int]  = Cola()

    for i in range(1,100):
        numero = randint(1,99)
        while numero in numeros:
            numero = randint(1,99)
        
        numeros.append(numero)
        secuencia.put(numero)
        
    return secuencia

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    carton_aux: list[int] = []
    jugadas_necesarias: int = 0

    for i in carton:
        carton_aux.append(i)

    while not bolillero.empty():
        if len(carton_aux) == 0:
            return jugadas_necesarias

        elem = bolillero.get()
        bolillero.put(elem)
        jugadas_necesarias += 1

        if elem in carton_aux:
            carton_aux.remove(elem)

# args: Cola[tuple[prioridad,nombre,especialidad medica]]
# devuelve la cantidad de pacientes que tienen prioridad en el rango [1,3]
def n_pacientes_urgentes(pacientes: Cola[tuple[int,str,str]]) -> int:
    pacientes_aux: Cola[tuple[int,str,str]] = Cola()
    pacientes_con_prioridad: int = 0

    while not pacientes.empty():
        paciente = pacientes.get()
        pacientes_aux.put(paciente)

        if  1 <= paciente[0] <= 3:
            pacientes_con_prioridad += 1
    
    while not pacientes_aux.empty():
        pacientes.put(pacientes_aux.get())

    return pacientes_con_prioridad

#Cola[tuple[nombre y apellido, dni, tipo de cuenta (preferencial o no), prioridad]]
def atencion_a_clientes(clientes : Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    clientes_con_prioridad: list[tuple[str, int, bool, bool]] = []
    clientes_preferenciales: list[tuple[str, int, bool, bool]] = []
    clientes_restantes: list[tuple[str, int, bool, bool]] = []
    clientes_aux: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_clientes: Cola[tuple[str, int, bool, bool]] = Cola()

    while not clientes.empty():
        cliente: tuple[str, int, bool, bool] = clientes.get()
        clientes_aux.put(cliente)

        if cliente[3] == True:
            clientes_con_prioridad.append(cliente)
        elif cliente[2] == True:
            clientes_preferenciales.append(cliente)
        else:
            clientes_restantes.append(cliente)

    while not clientes_aux.empty():
        clientes.put(clientes_aux.get())

    for cliente in clientes_con_prioridad:
        cola_clientes.put(cliente)

    for cliente in clientes_preferenciales:
        cola_clientes.put(cliente)

    for cliente in clientes_restantes:
        cola_clientes.put(cliente)
    
    return cola_clientes