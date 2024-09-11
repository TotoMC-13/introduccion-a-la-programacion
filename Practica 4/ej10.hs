f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = f1(n-1) + 2^n

f2 :: Integer -> Integer -> Integer
f2 n q | n == 1 = q^n
       | otherwise = f2(n-1) q + q^n

f3 :: Integer -> Integer -> Integer
f3 n q | n == 0 = 0
       | n == 1 = q
       | otherwise = g(2*n) q
       where
       g :: Integer -> Integer -> Integer
       g n q | n == 1 = q
             | otherwise = g(n-1) q + q^n