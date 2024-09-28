type Fila = [Integer]
type Tablero = [Fila]
type Posicion = (Integer, Integer)
type Camino = [Posicion]

-- Ej 5
maximo :: Tablero -> Integer
maximo x = maximoLista (volcarFilas x)

maximoLista :: [Integer] -> Integer
maximoLista [x] = x
maximoLista (x:y:xs)
    | x >= y = maximoLista (x:xs)
    | otherwise = maximoLista (y:xs )

volcarFilas :: Tablero -> [Integer]
volcarFilas [] = []
volcarFilas (x:xs) = x ++ volcarFilas xs

-- Ej 6

masRepetido :: (Eq t) => [t] -> t
masRepetido _ [x] = x
masRepetido x (y:ys)
    | 

contarApariciones :: (Eq t) => t -> [t] -> Integer
contarApariciones _ [] = 0
contarApariciones x (y:ys)
    | x == y = 1 + contarApariciones x ys
    | otherwise = contarApariciones x ys

sacarRepetidos :: (Eq t) => [t] -> [t]
sacarRepetidos [x] = [x]
sacarRepetidos (x:xs)
    | estaEn x xs = sacarRepetidos xs
    | otherwise = x : sacarRepetidos xs

estaEn :: (Eq t) => t -> [t] -> Bool
estaEn _ [] = False
estaEn x (y:ys)
    | x == y = True
    | otherwise = estaEn x ys