module Ej2 where

-- 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) 
                | n == x = True
                | otherwise = pertenece n xs

-- 2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales xs
                      | otherwise = False

-- 3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs

-- 5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:xs) 
        | elem == x = xs
        | otherwise = x : quitar elem xs

-- 6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) 
                | n /= x = x : quitarTodos n xs
                | n == x = quitarTodos n xs

-- 7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
        | pertenece x xs = eliminarRepetidos xs
        | otherwise =  x : eliminarRepetidos xs

-- 8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos x y = sonIguales (eliminarRepetidos x) (eliminarRepetidos y)

sonIguales :: (Eq t) => [t] -> [t] -> Bool
sonIguales [] [] = True
sonIguales _ [] = False
sonIguales [] _ = False
sonIguales (x:xs) (y:ys)
        | x:xs == y:ys = True
        | pertenece x (y:ys) = sonIguales xs (quitar x (y:ys))
        | otherwise = False

-- 9
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua x = x == reverso x 
        where
        reverso :: [t] -> [t]
        reverso [] = []
        reverso [x] = [x]
        reverso (x:xs) = reverso xs ++ [x]