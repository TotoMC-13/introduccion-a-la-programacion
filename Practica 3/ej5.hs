type Terna = (Int, Int, Int)

todosMenores :: Terna -> Bool
todosMenores (t1, t2, t3) = (f t1 > g t1) && (f t2 > g t2) && (f t2 > g t2)

f :: Int -> Int
f n | n <= 7 = n^2
    | n > 7 = 2*n - 1

g :: Int -> Int
g n | mod n 2 == 0 = div n 2
    | otherwise = 3*n + 1