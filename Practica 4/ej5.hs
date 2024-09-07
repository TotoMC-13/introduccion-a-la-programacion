medioFact :: Integer ->Integer
medioFact n | n <= 0 = 1
            | otherwise = medioFact(n - 2) * n