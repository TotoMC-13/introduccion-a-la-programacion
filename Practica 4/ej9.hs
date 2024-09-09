esCapicua :: Integer -> Bool
esCapicua n | n < 10 = True
            | otherwise = div n 10^(cantDigitos n-1) == mod (div n 10^(cantDigitos n - (cantDigitos n -1))) 10


cantDigitos :: Integer -> Integer
cantDigitos n | n >= 0 && n < 10 = 1
              | otherwise = cantDigitos(div n 10) + 1