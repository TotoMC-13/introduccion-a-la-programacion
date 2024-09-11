sumaPotencias :: Integer ->Integer ->Integer -> Integer
sumaPotencias q n m | n == 0 = 0
                    | otherwise = sumaPotenciasM q n m + sumaPotencias q (n-1) m

sumaPotenciasM :: Integer -> Integer -> Integer -> Integer
sumaPotenciasM q n m | m == 0 = 0
                     | otherwise = sumaPotenciasM q n (m-1) + q^(n*m)