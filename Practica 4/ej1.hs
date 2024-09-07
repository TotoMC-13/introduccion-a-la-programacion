{- 
0 si n = 0
1 si n = 1
fib(n - 1) + fib(n - 2) en otro caso 
-}

fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n - 1) + fibonacci(n - 2)