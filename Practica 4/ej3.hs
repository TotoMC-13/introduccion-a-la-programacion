esDivisible :: Integer -> Integer -> Bool
esDivisible x y | y == 0 = False
                | x == 0 = True
                | x < 0 = False
                | otherwise = esDivisible (x - y) y