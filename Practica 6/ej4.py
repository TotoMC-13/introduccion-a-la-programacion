def peso(altura: int) -> int:
    peso_del_pino: int

    if altura <= 300:
        peso_del_pino = altura*3
    else:
        peso_del_pino = altura*2

    return peso_del_pino

def es_peso_util(peso_del_pino: int) -> bool:
    return peso_del_pino >= 400 and peso_del_pino <= 1000

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso(altura))