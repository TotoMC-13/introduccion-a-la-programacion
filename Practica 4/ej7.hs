iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantDigitos(n)-i))) 10
                 

cantDigitos :: Integer -> Integer
cantDigitos n | n >= 0 && n < 10 = 1
              | otherwise = cantDigitos(div n 10) + 1