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
masRepetido :: Tablero -> Integer
masRepetido x = tuplaMayorY (generarTuplas (sacarRepetidos (volcarFilas x)) (volcarFilas x))

tuplaMayorY :: (Eq t) => [(t, Integer)] -> t
tuplaMayorY [(x1,x2)] = x1
tuplaMayorY ((x1,x2):(y1,y2):xs)
    | x2 >= y2 = tuplaMayorY((x1,x2):xs)
    | otherwise = tuplaMayorY((y1,y2):xs)

generarTuplas :: (Eq t) => [t] ->[t] -> [(t, Integer)]
generarTuplas [] _ = []
generarTuplas (x:xs) y = (x, contarApariciones x y) : generarTuplas xs y

tuplaApariciones :: (Eq t) => t -> [t] -> (t, Integer)
tuplaApariciones x [] = (x, 0)
tuplaApariciones x (y:ys) = (x,contarApariciones x (y:ys)) 

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

-- Ej 7
valoresDeCamino :: Tablero -> Camino -> [Integer]
valoresDeCamino _ [] = []
valoresDeCamino (x:xs) ((y1,y2):ys) = elemPosN y2 (elemPosN y1 (x:xs)) : valoresDeCamino (x:xs) ys

elemPosN :: (Eq t) => Integer -> [t] -> t
elemPosN 0 (y:ys) = y
elemPosN x (y:ys) = x > 0 = elemPosN (x-1) ys

-- Ej 8
esCaminoFibo :: [Integer] -> Integer -> Bool
esCaminoFibo [x] y = x == fibonacci y
esCaminoFibo (x:xs) y = x == fibonacci y && esCaminoFibo xs (y+1)

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)