def pertenece(x, lista: list) -> bool:
    for i in lista:
        if i == x:
            return True
    
    return False

def pertenece2(x, lista: list) -> bool:
    return x in lista

def pertenece3(x, lista: list) -> bool:
    i: int = 0

    while i < len(lista):
        if x == lista[i]:
            return True
        
        i += 1
    
    return False