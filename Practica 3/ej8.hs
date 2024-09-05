comparar :: Int -> Int -> Int
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x =  mod x 10 + mod (div x 10) 10