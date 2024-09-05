f1 :: Int -> Int
f1 = abs

f2 :: Int -> Int -> Int
f2 x y | abs x > abs y = abs x
       | abs x < abs y = abs y

f3 :: Int -> Int -> Int -> Int
f3 x y z | x > y && x > z = x
         | y > x && y > z = y
         | z > x && z > y = z

f4 :: Int -> Int -> Bool
f4 x y = x == 0 || y == 0

f5 :: Int -> Int -> Bool
f5 x y | x == 0 || y == 0 = True
       | otherwise = False

f6 :: Int -> Int -> Bool
f6 x y = x == 0 && y == 0

f7 :: Int -> Int -> Bool
f7 0 0 = True
f7 _ _ = False

-- Intervalos: (−∞, 3],(3, 7] y (7, ∞)

f8 :: Int -> Int -> Bool
f8 x y | x <= 3 && y <= 3 = True
       | x > 3 && x <= 7 && y > 3 && y <= 7 = True
       | x > 7  && y > 7 = True
       | otherwise = False

f9 :: Int -> Int -> Int -> Int
f9 x y z | x == y && y == z = x
         | x == y = x + z
         | x == z = x + y
         | y == z = x + y
         | otherwise = x + y + z

f10 :: Int -> Int -> Bool
f10 x y = x `mod` y == 0 

f11 :: Int -> Int
f11 x = x `mod` 10

f12 :: Int -> Int
f12 x = (x `div` 10) `mod` 10