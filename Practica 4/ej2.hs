parteEntera :: Float -> Integer
parteEntera n | (0 <= n && n < 1) || (-1 <= n && n < 0) = 0
              | n >= 1 = 1 + parteEntera (n - 1)
              | otherwise = parteEntera (n + 1) - 1