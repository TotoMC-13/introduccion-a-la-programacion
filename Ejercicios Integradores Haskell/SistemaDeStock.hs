module Ejercicios where

type Productos = [String]
type Stock = [(String, Integer)]
type ValorStock = [(String, Float)]

type

-- Ej 1

generarStock :: Productos -> Stock
generarStock [] = []
generarStock x = generarTuplas (eliminarRepetidos x) x

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) 
        | n == x = True
        | otherwise = pertenece n xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
        | pertenece x xs = eliminarRepetidos xs
        | otherwise = x : eliminarRepetidos xs

contarRepeticiones :: (Eq t) => t -> [t] -> Integer
contarRepeticiones _ [] = 0
contarRepeticiones x (y:ys)
        | x == y = 1 + contarRepeticiones x ys
        | otherwise = contarRepeticiones x ys

generarTuplas :: Productos -> Productos -> Stock
generarTuplas [] _ = []
generarTuplas _ [] = []
generarTuplas (x:xs) y = (x, contarRepeticiones x y) : generarTuplas xs y

-- Ej 2
stockDeProducto :: Stock -> String -> Integer
stockDeProducto [] _ = 0
stockDeProducto ((x1,x2):xs) prod
        | x1 == prod = x2
        | otherwise = stockDeProducto xs prod

-- Ej 3
dineroEnStock :: Stock -> ValorStock -> Float
dineroEnStock [] _ = 0
dineroEnStock ((x1,x2):xs) y =  (fromInteger x2) * (encontarPrecio x1 y) + dineroEnStock xs y

encontarPrecio :: String -> ValorStock -> Float
encontarPrecio [] _ = 0
encontarPrecio x1 ((y1,y2):ys)
        | x1 == y1 = y2
        | otherwise = encontarPrecio x1 ys

-- Ej 4
aplicarOferta :: Stock -> ValorStock -> ValorStock
aplicarOferta [] _ = []
aplicarOferta ((x1,x2):xs) y
        | x2 <= 10 = (x1,encontarPrecio x1 y) : aplicarOferta xs y
        | x2 > 10 = (x1,(encontarPrecio x1 y) * 80 / 100) : aplicarOferta xs y

-- Ej 5
