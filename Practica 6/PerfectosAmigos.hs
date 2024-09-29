-- Ej 9
divisoresPropios :: Integer -> [Integer]
divisoresPropios n  = divisoresDesde n 1

divisoresDesde :: Integer -> Integer -> [Integer]
divisoresDesde n m
    | n <= m = [n]
    | mod n m == 0 = m : divisoresDesde n (m+1)
    | otherwise = divisoresDesde n (m+1)

-- Ej 10
sonAmigos :: Integer -> Integer -> Bool
sonAmigos n m = sumarLista (divisoresPropios n) - n == m && sumarLista (divisoresPropios m) - m == n

sumarLista :: [Integer] -> Integer
sumarLista [] = 0
sumarLista [x] = x
sumarLista (x:y:xs) = x + y + sumarLista xs

-- Ej 11
losPrimerosNPerfectos :: Integer -> [Integer]
losPrimerosNPerfectos n = nCantidadDePerfectos n 0 0

nCantidadDePerfectos :: Integer -> Integer -> Integer -> [Integer]
nCantidadDePerfectos cantidad numeroActual contador
    | cantidad == contador = []
    | esPerfecto numeroActual = numeroActual : nCantidadDePerfectos cantidad (numeroActual + 1) (contador + 1)
    | otherwise = nCantidadDePerfectos cantidad (numeroActual + 1) contador

esPerfecto :: Integer -> Bool
esPerfecto 0 = False
esPerfecto n = n == sumarLista (divisoresPropios n) - n

estaEn :: (Eq t) => t -> [t] -> Bool
estaEn _ [] = False
estaEn n (x:xs)
    | n == x = True
    | otherwise = estaEn n xs

-- Ej 12
listaDeAmigos  :: [Integer] -> [(Integer, Integer)]
listaDeAmigos [] = []
listaDeAmigos (x:xs)
    | cualEsAmigoDe x xs /= 0 = (x, cualEsAmigoDe x xs) : listaDeAmigos  xs
    | otherwise = listaDeAmigos  xs

cualEsAmigoDe :: Integer -> [Integer] -> Integer
cualEsAmigoDe _ [] = 0
cualEsAmigoDe n (x:xs)
    | sonAmigos n x = x
    | otherwise = cualEsAmigoDe n xs