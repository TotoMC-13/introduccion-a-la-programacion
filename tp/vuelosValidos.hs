module Solucion where

type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]

-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool
vuelosValidos _ = 

vueloValido :: Vuelo  -> Bool
vueloValido (dest1, dest2, duracion) | dest1 == dest2 = False
                                     | otherwise = duracion > 0 