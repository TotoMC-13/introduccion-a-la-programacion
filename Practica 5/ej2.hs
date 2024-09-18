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