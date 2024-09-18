longitud :: (Eq t) => [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo(xs)

principio :: [t] -> t
principio (x:xs) = x

reverso :: [t] -> [t]
reverso [] = []
reverso (x:[]) = [x]
reverso (x:xs) = reverso xs ++ [x]