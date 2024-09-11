menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | m == n = n
                      | mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)