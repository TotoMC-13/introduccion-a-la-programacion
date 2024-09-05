type Punto2D = (Float, Float)


prodIntR2 :: Punto2D -> Punto2D -> Float
prodIntR2 (v1, v2) (w1, w2) = v1 * w1 + v2 * w2

todoMenor :: Punto2D -> Punto2D -> Bool
todoMenor (v1, v2) (w1, w2) = (v1 < w1) && (v2 < w2)

-- Calculo ||v - w|| = √(v1-w1)^2 + (v2-w2)^2

distanciaPuntos :: Punto2D -> Punto2D -> Float
distanciaPuntos (v1, v2) (w1, w2) = sqrt((v1 - w1)^2 + (v2 - w2)^2)

sumaTerna :: (Float, Float, Float) -> Float
sumaTerna (v1, v2, v3) = v1 + v2 + v3

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a,b,c) k | mod a k == 0 && mod b k == 0 && mod c k == 0 = a + b + c
                             | mod a k == 0 && mod b k == 0 = a + b
                             | mod a k == 0 && mod c k == 0 = a + c
                             | mod b k == 0 && mod c k == 0 = b + c
                             | mod a k == 0 = a
                             | mod b k == 0 = b
                             | mod c k == 0 = c
                             | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a, b, c) | mod a 2 == 0 = a
                       | mod b 2 == 0 = b
                       | mod c 2 == 0 = c

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b)-> (b, a)
invertir (a, b) = (b, a)
