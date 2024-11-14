def agregar_producto(inventario: dict[str, dict[str, float ,int]], nombre: str, precio: float, cantidad: int):
    stockInfo:dict[str, float | int] = inventario[nombre]
    stockInfo["precio"] = precio
    stockInfo["cantidad"] = cantidad

stock: dict[str, dict[str, float | int]] = {} 

agregar_producto(stock, "manzana", 10.99, 12)
print(stock)