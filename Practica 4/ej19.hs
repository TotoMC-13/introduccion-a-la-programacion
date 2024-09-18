esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n m | mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)

sumaPrimerosNPrimos :: Integer -> Integer
sumaPrimerosNPrimos m | m == 0 = 0
                      | m == 1 = 0
                      | esPrimo m = sumaPrimerosNPrimos (m-1) + m
                      | otherwise = sumaPrimerosNPrimos (m-1)

-- esSumaInicialPrimosDesde :: Integer -> Integer
-- esSumaInicialPrimosDesde n m | 