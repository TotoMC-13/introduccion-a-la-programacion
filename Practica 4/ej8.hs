sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = sumaDigitos(div n 10) + mod n 10