-- 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) 
                | n == x = True
                | otherwise = pertenece n xs

-- 5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:xs) 
        | elem == x = xs
        | otherwise = x : quitar elem xs