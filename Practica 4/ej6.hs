todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimoDigito n  ==  ultimoDigito(sacarUltimoDigito n) && todosDigitosIguales(sacarUltimoDigito n)
                      where ultimoDigito n = n `mod` 10 
                            sacarUltimoDigito n = n `div` 10