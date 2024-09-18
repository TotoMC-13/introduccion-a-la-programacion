-- 3
maximo :: (Ord t) => [t] -> t
maximo (x:[]) = x
maximo (x:y:xs)
        | x > y = maximo (x:xs)
        | otherwise = maximo(y:xs)