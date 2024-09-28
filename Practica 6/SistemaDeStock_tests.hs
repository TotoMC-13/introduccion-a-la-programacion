import Ejercicios
import Test.HUnit
import Data.List (sort)

run = runTestTT tests4

tests1 = TestList [
    "Caso base []" ~: sort (generarStock []) ~?= sort [],
    "Caso un elemento" ~: sort (generarStock ["banana"]) ~?= [("banana", 1)],
    "Caso varios elementos" ~: sort (generarStock ["banana", "manzana", "pera", "banana", "banana", "kiwi", "manzana", "kiwi"]) 
                              ~?= sort [("banana", 3), ("manzana", 2), ("pera", 1), ("kiwi", 2)],
    "Caso todos iguales" ~: sort (generarStock ["manzana", "manzana", "manzana"]) ~?= [("manzana", 3)],
    "Caso mayúsculas y minúsculas" ~: sort (generarStock ["Banana", "banana", "BANANA"]) ~?= sort ([("Banana", 1), ("banana", 1), ("BANANA", 1)]),
    "Caso lista con string vacío" ~: sort (generarStock ["", "banana", ""]) ~?= [("", 2), ("banana", 1)],
    "Caso muchos elementos" ~: length (generarStock (replicate 1000 "manzana")) ~?= 1
    ]

tests2 = TestList [
    "Caso base: lista vacía" ~: stockDeProducto [] "banana" ~?= 0,
    "Caso un producto, existe" ~: stockDeProducto [("banana", 10)] "banana" ~?= 10,
    "Caso un producto, no existe" ~: stockDeProducto [("banana", 10)] "manzana" ~?= 0,
    "Caso varios productos, existe" ~: stockDeProducto [("manzana", 5), ("banana", 3), ("kiwi", 7)] "banana" ~?= 3,
    "Caso varios productos, no existe" ~: stockDeProducto [("manzana", 5), ("banana", 3), ("kiwi", 7)] "pera" ~?= 0,
    "Caso todos diferentes cantidades" ~: stockDeProducto [("pera", 4), ("pera", 4)] "pera" ~?= 4
    ]

tests3 = TestList [
    "Caso un producto en stock" ~: dineroEnStock [("banana", 5)] [("banana", 2.5)] ~?= 12.5,
    "Caso varios productos en stock" ~: dineroEnStock 
        [("banana", 5), ("manzana", 3), ("kiwi", 2)] 
        [("banana", 2.0), ("manzana", 3.0), ("kiwi", 4.0)] ~?= 27.0,
    "Caso productos en diferente orden" ~: dineroEnStock 
        [("kiwi", 2), ("banana", 5)] 
        [("banana", 2.5), ("kiwi", 3.0)] ~?= 18.5
    ]

tests4 = TestList [
    -- Caso base: stock vacío
    "Caso base: stock vacío" ~: aplicarOferta [] [("banana", 2.5)] ~?= [],

    -- Caso con un solo producto con cantidad menor o igual a 10 y precio definido
    "Caso con un solo producto con cantidad menor o igual a 10" ~: 
        aplicarOferta [("banana", 5)] [("banana", 2.5)] ~?= [("banana", 2.5)],  -- Sin descuento

    -- Caso con un solo producto con cantidad mayor a 10 y precio definido
    "Caso con un solo producto con cantidad mayor a 10" ~: 
        aplicarOferta [("banana", 15)] [("banana", 2.5)] ~?= [("banana", 2.0)],  -- Descuento aplicado

    -- Caso con varios productos, todos con cantidades menores o iguales a 10
    "Caso con varios productos, todos con cantidades menores o iguales a 10" ~: 
        aplicarOferta [("banana", 5), ("manzana", 3), ("kiwi", 2)] 
                      [("banana", 2.0), ("manzana", 3.0), ("kiwi", 4.0)] 
        ~?= [("banana", 2.0), ("manzana", 3.0), ("kiwi", 4.0)],  -- Sin descuento aplicado

    -- Caso todos los productos con cantidades mayores a 10 y precios definidos
    "Caso todos productos mayores a 10" ~: 
        aplicarOferta [("banana", 11), ("manzana", 15)] 
                      [("banana", 2.5), ("manzana", 3.0)] 
        ~?= [("banana", 2.0), ("manzana", 2.4)],  -- Descuento aplicado en ambos

    -- Caso mezcla de productos con cantidades menores y mayores a 10
    "Caso mezcla de productos" ~: 
        aplicarOferta [("banana", 5), ("manzana", 10), ("kiwi", 15)] 
                      [("banana", 2.0), ("manzana", 3.0), ("kiwi", 4.0)] 
        ~?= [("banana", 2.0), ("manzana", 3.0), ("kiwi", 3.2)]  -- Sin descuento en banana y manzana

    -- Caso con precios y cantidades definidos sin repeticiones
    , "Caso precios y cantidades únicos" ~: 
        aplicarOferta [("banana", 2), ("manzana", 8), ("kiwi", 12)] 
                      [("banana", 5.0), ("manzana", 2.5), ("kiwi", 3.0)] 
        ~?= [("banana", 5.0), ("manzana", 2.5), ("kiwi", 2.4)]  -- Descuento aplicado en manzana
    ]