# 1
def max (x: int , y: int) -> int:
    result: int = 0
    if x < y:
        result = y
    else:
        result = x
    return result

# 2
def min (x: int , y: int) -> int:
    result: int = 0
    if x > y:
        result = y
    else:
        result = x
    return result

# 9
def sumar ( x : int , y : int ) -> int :
    sumando : int = 0
    abs_y : int = 0
    if y < 0:
        sumando = -1
        abs_y = -y
    else:
        sumando = 1
        abs_y = y
    result : int = x
    count : int = 0
    while ( count < abs_y ):
        result = result + sumando
        count = count + 1
    return result