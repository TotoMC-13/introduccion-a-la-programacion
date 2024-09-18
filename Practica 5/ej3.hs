-- 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

-- 2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:[]) = True
todosIguales (x:y:xs) | x == y = todosIguales(xs)
                      | otherwise = False

-- 3
maximo :: (Ord t) => [t] -> t
maximo (x:[]) = x
maximo (x:y:xs)
        | x > y = maximo (x:xs)
        | otherwise = maximo(y:xs)