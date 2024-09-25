module SolucionT1 where

-- No tiene tuplas repetidas ni tuplas con ambas componentes iguales
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x1,x2):xs)
    | ambosComponentesIguales ((x1,x2):xs) == True || existenDuplicados ((x1,x2):xs) == True = False
    | otherwise = True

existenDuplicados:: [(String, String)] -> Bool
existenDuplicados [] = False
existenDuplicados ((x1,x2):xs)
    | estaEn (x1,x2) xs == True = True
    | otherwise = existenDuplicados xs

-- Me dice si una tupla esta contenida en una lista de tuplas
estaEn :: (String, String) -> [(String, String)] -> Bool
estaEn _ [] = False
estaEn (x1,x2) ((y1,y2):ys)
    | (x1 == y1 && x2 == y2) || (x1 == y2 && x2 == y1) = True
    | otherwise = estaEn (x1,x2) ys

--Me dice si existe una tupla con ambos componentes iguales en una lista de tuplas
ambosComponentesIguales :: [(String, String)] -> Bool
ambosComponentesIguales [] = False
ambosComponentesIguales ((x1,x2):xs)
    | x1 == x2 = True
    | otherwise = ambosComponentesIguales xs

personas :: [(String, String)] -> [String]
personas [] = []
personas ((x1,x2):xs) = estaIncluido x1 xs ++ estaIncluido x2 xs ++ personas xs

estaIncluido :: String -> [(String, String)] -> [String]
estaIncluido x [] = [x]
estaIncluido x ((y1,y2):ys)
    | x == y1 || x == y2 = []
    | otherwise = estaIncluido x ys

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe x ((y1,y2):ys)
    | x == y1 = [y2] ++ amigosDe x ys 
    | x == y2 = [y1] ++ amigosDe x ys
    | otherwise = amigosDe x ys

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = []
personaConMasAmigos ((x1,x2):xs)
    | 

longitudLista :: [String] -> Integer
longitudLista [] = 0
longitudLista [x] = 1 
longitudLista (x:xs) = 1 + longitudLista xs

cuantosAmigos :: String -> [String] -> (String, Integer)
cuantosAmigos x [] = (x, 0)
cuantosAmigos x y = (x, longitudLista y)

tuplaComponenteYMasAlto :: [(String, Integer)] -> (String, Integer)
tuplaComponenteYMasAlto [(x1,x2)] = (x1,x2)
tuplaComponenteYMasAlto ((x1,x2):(y1,y2):xs)
    | x2 > y2 = tuplaComponenteYMasAlto ((x1,x2) : xs)
    | x2 < y2 = tuplaComponenteYMasAlto ((y1,y2) : xs)
    | x2 == y2 = tuplaComponenteYMasAlto ((x1,x2) : xs)
