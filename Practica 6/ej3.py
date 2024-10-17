def alguno_es_cero(n: int, m:int) -> bool:
    return n == 0 or m == 0

def ambos_son_cero(n:int, m:int) -> bool:
    return n == 0 and m == 0

def es_nombre_largo(n:str) -> bool:
    return n >= 3 and n <= 8 

def es_bisiesto(n:int) -> bool:
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)