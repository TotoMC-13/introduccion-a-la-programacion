-- 5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:xs) 
        | elem == x = xs
        | otherwise = x : quitar elem xs