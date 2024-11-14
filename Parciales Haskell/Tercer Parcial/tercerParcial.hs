module TercerParcial where

type Registro = [(String,[Integer])]
type Alumno = String

-- Ej 1
-- Alumno tiene que tener mas de n materias aprobada.
aproboMasDeNMAterias :: Registro -> Alumno -> Integer -> Bool
aproboMasDeNMAterias registro nombre n = n < (cuantosNumerosMayoresAN 3 (notasAlumno nombre registro))


-- Caso base para evitar recursiones infinitas.
buscarTupla :: Alumno -> Registro -> (String,[Integer])
buscarTupla _ [] = ("",[]) 
buscarTupla nombre ((nombreRegistro,notasRegistro):xs)
    | nombre == nombreRegistro = (nombreRegistro,notasRegistro)
    | otherwise = buscarTupla nombre xs

cuantosNumerosMayoresAN :: Integer -> [Integer] -> Integer
cuantosNumerosMayoresAN _ [] = 0
cuantosNumerosMayoresAN x (y:ys)
    | x < y = 1 + cuantosNumerosMayoresAN x ys
    | otherwise = cuantosNumerosMayoresAN x ys

componenteY :: (x,y) -> y
componenteY (x,y) = y

notasAlumno :: Alumno -> Registro -> [Integer]
notasAlumno _ [] = []
notasAlumno nombre (x:xs) = componenteY (buscarTupla nombre (x:xs))

-- Ej 2
-- Promedio 8.0 y no tiene notas menores a 4.
buenosAlumnos :: Registro -> [Alumno]
buenosAlumnos [] = []
buenosAlumnos ((nombreRegistro,notasRegistro):xs)
    | promedioAlumno nombreRegistro ((nombreRegistro,notasRegistro):xs) >= 8.0 && noTieneAplazos nombreRegistro notasRegistro = nombreRegistro : buenosAlumnos xs
    | otherwise = buenosAlumnos xs

noTieneAplazos :: Alumno -> [Integer] -> Bool
noTieneAplazos _ [] = True
noTieneAplazos alumno (x:xs)
    | x >= 4 && noTieneAplazos alumno xs = True
    | otherwise = False

promedioAlumno :: Alumno -> Registro -> Float
promedioAlumno _ [] = 0
promedioAlumno alumno registro = promedio (notasAlumno alumno registro)

promedio :: [Integer] -> Float
promedio [] = 0
promedio x = fromInteger (sumarLista x) / fromInteger (cantidadElementos x)

sumarLista :: [Integer] -> Integer
sumarLista [] = 0
sumarLista (x:xs) = x + sumarLista xs

cantidadElementos :: (Eq t) => [t] -> Integer
cantidadElementos [] = 0
cantidadElementos (x:xs) = 1 + cantidadElementos xs

-- Ej 3
mejorPromedio :: Registro -> Alumno
mejorPromedio x = xDeTuplaMayorY (todosLosPromedios x) 

xDeTuplaMayorY :: [(Alumno, Float)] -> Alumno
xDeTuplaMayorY [(x,y)] = x
xDeTuplaMayorY ((x1,x2):(y1,y2):xs)
    | x2 >= y2 = xDeTuplaMayorY ((x1,x2):xs)
    | otherwise = xDeTuplaMayorY ((y1,y2):xs)

todosLosPromedios :: Registro -> [(Alumno, Float)]
todosLosPromedios [] = []
todosLosPromedios ((nombreRegistro,notasRegistro):xs) = (nombreRegistro, promedioAlumno nombreRegistro ((nombreRegistro,notasRegistro):xs)) : todosLosPromedios xs

-- Ej 4
--  si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera -1)
-- alumno pertenece al conjunto de buenosAlumnos(registro) 
-- promedio de notas de finales de alumno está a menos (estrictamente) de 1 punto del mejorPromedio(registro)
seGraduoConHonores :: Registro -> Integer -> Alumno -> Bool
seGraduoConHonores registro cantidadMaterias alumno = aproboMasDeNMAterias registro alumno (cantidadMaterias - 1) && estaEn alumno (buenosAlumnos registro)  && promedioAlumno alumno registro > ((yDeTuplaMayorY (todosLosPromedios registro)) - 1) 

estaEn :: Alumno -> [Alumno] -> Bool
estaEn _ [] = False
estaEn alumno (x:xs)
    | alumno == x = True
    | otherwise = estaEn alumno xs

yDeTuplaMayorY :: [(Alumno, Float)] -> Float
yDeTuplaMayorY [(x,y)] = y
yDeTuplaMayorY ((x1,x2):(y1,y2):xs)
    | x2 >= y2 = yDeTuplaMayorY ((x1,x2):xs)
    | otherwise = yDeTuplaMayorY ((y1,y2):xs)