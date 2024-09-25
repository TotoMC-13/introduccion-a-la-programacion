module Ej7 where

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((nombreContacto, _): restoContactos)
    | nombre == nombreContacto = True
    | otherwise = enLosContactos nombre restoContactos

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto x [] = [x]
agregarContacto (nombreContacto, numeroContacto) ((nombreContactoLista, numeroContactoLista): restoContactos)
    | enLosContactos nombreContacto ((nombreContactoLista, numeroContactoLista):restoContactos) == False = (nombreContacto, numeroContacto) : ((nombreContactoLista, numeroContactoLista):restoContactos)
    | otherwise = actualizarContacto (nombreContacto, numeroContacto) ((nombreContactoLista, numeroContactoLista): restoContactos)
    where
    actualizarContacto :: Contacto -> ContactosTel -> ContactosTel
    actualizarContacto (nombreContacto, numeroContacto) ((nombreContactoLista, numeroContactoLista): restoContactos)
        | nombreContacto == nombreContactoLista = (nombreContacto, numeroContacto) : restoContactos
        | otherwise = (nombreContactoLista, numeroContactoLista) : (actualizarContacto (nombreContacto, numeroContacto) restoContactos)

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre ((nombreContacto, numeroContacto): restoContactos)
    | enLosContactos nombre ((nombreContacto, numeroContacto) : restoContactos) == False = (nombreContacto, numeroContacto) : restoContactos -- Si el contacto no esta, no hacer nada.
    | otherwise = recorrerContactos nombre ((nombreContacto, numeroContacto): restoContactos)
    where
    recorrerContactos  :: Nombre -> ContactosTel -> ContactosTel
    recorrerContactos nombre ((nombreContactoLista, numeroContactoLista): restoContactos)
        | nombre == nombreContactoLista = restoContactos
        | otherwise =  (nombreContactoLista, numeroContactoLista) : recorrerContactos nombre restoContactos