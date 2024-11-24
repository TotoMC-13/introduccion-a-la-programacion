from queue import Queue as Cola

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res: Cola[int] = Cola()
    urgentes_aux: Cola[int] = Cola()
    postergables_aux: Cola[int] = Cola()

    while not urgentes.empty(): # Como la longitud de urgentes = postergables puedo hacer esto.
        urgentes_aux.put(urgentes.get())
        postergables_aux.put(postergables.get())

    while not urgentes_aux.empty():
        paciente_urgente: int = urgentes_aux.get()
        paciente_postergable: int = postergables_aux.get()

        res.put(paciente_urgente)
        res.put(paciente_postergable)
        urgentes.put(paciente_urgente)
        postergables.put(paciente_postergable)

    return res

# # Crear las colas de ejemplo
# urgentes = Cola()
# postergables = Cola()

# # Agregar elementos a las colas
# for paciente in [1, 3, 5]:
#     urgentes.put(paciente)

# for paciente in [2, 4, 6]:
#     postergables.put(paciente)

# print(orden_de_atencion(urgentes, postergables).queue)

def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    cantidad_infectados: dict[str, int] = {}
    porcentaje_infectados: dict[str, float] = {}
    res: dict[str, float] = {}

    for paciente in registros:
        enfermedad = paciente[1]
        if pertenece(cantidad_infectados, enfermedad):
            cantidad_infectados[enfermedad] += 1
        else:
            cantidad_infectados[enfermedad] = 1
        
    for enfermedad in cantidad_infectados:
        cantidad: int = cantidad_infectados[enfermedad]
        porcentaje_infectados[enfermedad] = cantidad / len(registros)

    for enfermedad in porcentaje_infectados:
        porcentaje: float = porcentaje_infectados[enfermedad]

        if pertenece(infecciosas, enfermedad) and porcentaje >= umbral:
            res[enfermedad] = porcentaje
    
    return res


# Funcion polimorfica, por eso no tiene definido el tipo de dato.
def pertenece(elementos, elemento) -> bool:
    for elem in elementos:
        if elem == elemento:
            return True
        
    return False

# registros = [(111,"sifilis"),(222,"sifilis"),(333,"neumonia"),(444,"sifilis"),(555,"neumonia"),(666,"lolero")]
# infecciosas = ["sifilis", "neumonia", "lolero"]
# umbral = 0.3
# print(alarma_epidemiologica(registros, infecciosas, umbral))
# registros1 = [(111,"sifilis"),(222,"sifilis"),(333,"sifilis"),(444,"lolero"),(555,"gripe"),(666,"gripe"),(777,"neumonia"),(888,"neumonia"),(999,"gripe")]
# infecciosas1 = ["sifilis", "neumonia", "lolero"]
# umbral1 = 0.3
# print(alarma_epidemiologica(registros1, infecciosas1, umbral1))

def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    horas_trabajadas: dict[int, int] = {}
    mas_horas_trabajadas: int = 0
    empleados_del_mes: list[int] = []

    for empleado in horas:
        horas_totales: int = sumar_todo(horas[empleado])

        if horas_totales > mas_horas_trabajadas:
            mas_horas_trabajadas = horas_totales

        horas_trabajadas[empleado] = horas_totales

    for empleado in horas_trabajadas:
        horas_totales: int = horas_trabajadas[empleado]

        if horas_totales >= mas_horas_trabajadas:
            empleados_del_mes.append(empleado)

    return empleados_del_mes

def sumar_todo(numeros: list[int]) -> int:
    suma:int = 0

    for numero in numeros:
        suma += numero
    
    return suma

# h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
# print(empleados_del_mes(h1)) #["333"]
# h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
# print(empleados_del_mes(h2)) #["333","444"]
# h3 = {"111": [1, 2, 3], "444": [6,7,8], "222": [2, 3, 4], "333": [4,5,6]}
# print(empleados_del_mes(h3)) #["444"]
# h4 = {"111": [1, 2, 3], "444": [6,7,8], "222": [8,9,10], "333": [4,5,6], "444": [8,9,10], "555": [6,7,8]}
# print(empleados_del_mes(h4)) #["222","444"] o ["444","222"] (en los asegura no se habla del orden)

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    cantidad_total_de_camas: int = len(camas_por_piso[0])
    res: list[float] = []

    for piso in camas_por_piso:
        camas_ocupadas: int = 0
        
        for cama in piso:
            if cama == True:
                camas_ocupadas += 1
    
        res.append((camas_ocupadas / cantidad_total_de_camas) * 100)
    
    return res

# cp1 = [[True, True, False],
#        [False, True, True]]
# print(nivel_de_ocupacion(cp1))
# cp2 = [[True, True, False, True],
#        [False, True, True, True],
#        [False, False, False, True]]
# print(nivel_de_ocupacion(cp2))
# cp3 = [[True, True, False, True],
#        [False, True, True, True],
#        [False, False, False, True],
#        [False, False, False, False]]
# print(nivel_de_ocupacion(cp3))
