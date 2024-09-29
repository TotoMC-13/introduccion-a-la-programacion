module SegundoParcial where

type Formulas = [(String,String)]
type Votos = [Integer]

-- Ej 1
votosEnBlanco :: Formulas -> Votos -> Integer -> Integer
votosEnBlanco _ votos votosTotales = votosTotales - sumarLista votos  

sumarLista :: [Integer] -> Integer
sumarLista [] = 0
sumarLista (x:xs) = x + sumarLista xs

-- Ej 2
formulasValidas :: Formulas -> Bool
formulasValidas [] = True
formulasValidas formulas = not (hayRepetidos (aplanarTuplas formulas))

aplanarTuplas :: (Eq t) => [(t,t)] -> [t]
aplanarTuplas [(x1,x2)] = [x1,x2]
aplanarTuplas ((x1,x2):xs) = x1 : x2 : aplanarTuplas xs

estaEn :: (Eq t) => t -> [t] -> Bool
estaEn _ [] = False
estaEn x (y:ys)
    | x == y = True
    | otherwise = estaEn x ys

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs)
    | estaEn x xs = True
    | otherwise = hayRepetidos xs 

-- Ej 3
porcentajeDeVotos :: String -> Formulas -> Votos -> Float
porcentajeDeVotos presidente formulas votos = division ((votosDeFormula presidente formulas votos) * 100) (sumarLista votos)

posFormula :: String -> Formulas -> Integer
posFormula _ [x] = 0
posFormula presidente ((x1,x2):xs)
    | presidente == x1 = 0
    | otherwise = (posFormula presidente xs) + 1

elemPosN :: (Eq t) => Integer -> [t] -> t
elemPosN 0 (y:ys) = y
elemPosN x (y:ys) | x > 0 = elemPosN (x-1) ys

votosDeFormula :: String -> Formulas -> Votos -> Integer
votosDeFormula presidente formulas votos = elemPosN (posFormula presidente formulas) votos

division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

-- Ej 4
proximoPresidente :: Formulas -> Votos -> String
proximoPresidente [(x1,x2)] _ = x1
proximoPresidente ((x1,x2):(x3,x4):xs) (y1:y2:ys)
    | votosDeFormula x1 ((x1,x2):(x3,x4):xs) (y1:y2:ys) >= votosDeFormula x3 ((x1,x2):(x3,x4):xs) (y1:y2:ys) = proximoPresidente ((x1,x2):xs) (y1:ys)
    | otherwise = proximoPresidente ((x3,x4):xs) (y2:ys)