sumaImpares :: Int -> Int
sumaImpares n | n == 1 = 1
              | otherwise = (n * 2 - 1) + sumaImpares(n - 1)