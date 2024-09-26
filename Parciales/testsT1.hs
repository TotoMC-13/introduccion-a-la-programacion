import Test.HUnit
import SolucionT1

-- Test cases
run = runTestTT tests

tests = test [
    -- Caso básico
    "Caso 1: personaConMasAmigos" ~: personaConMasAmigos [("Charlie", "Ana"), ("Pedro", "Charlie"), ("Jose", "Charlie")]  ~?= "Charlie",
    
    -- Caso con lista vacía
    "Caso 2: personaConMasAmigos con lista vacía" ~: personaConMasAmigos [] ~?= "",
    
    -- Caso con una sola relación
    "Caso 3: personaConMasAmigos con una sola persona" ~: personaConMasAmigos [("Charlie", "Ana")] `elem` ["Charlie", "Ana"] ~? "Debe ser 'Charlie' o 'Ana'",
    
    -- Caso con dos personas con igual cantidad de amigos
    "Caso 4: personaConMasAmigos con dos personas con igual cantidad de amigos" ~: personaConMasAmigos [("Charlie", "Ana"), ("Pedro", "Charlie"), ("Jose", "Ana")] `elem` ["Ana", "Charlie"] ~? "Debe ser 'Ana' o 'Charlie'",
    
    -- Caso con tres personas con amigos distintos
    "Caso 5: personaConMasAmigos con tres personas diferentes" ~: personaConMasAmigos [("Ana", "Charlie"), ("Pedro", "Jose"), ("Jose", "Ana")] ~?= "Ana",
    
    -- Caso donde una persona tiene todos los amigos
    "Caso 6: personaConMasAmigos con una persona que tiene todos los amigos" ~: personaConMasAmigos [("Pedro", "Charlie"), ("Jose", "Charlie"), ("Ana", "Charlie")] ~?= "Charlie",
    
    -- Caso con relaciones repetidas (no permitidas)
    "Caso 7: personaConMasAmigos no debe considerar relaciones repetidas" ~: personaConMasAmigos [("Ana", "Charlie"), ("Ana", "Charlie")] ~?= "Ana",
    
    -- Caso con relaciones invertidas (no permitidas)
    "Caso 8: personaConMasAmigos no debe considerar relaciones invertidas como distintas" ~: personaConMasAmigos [("Ana", "Charlie"), ("Charlie", "Ana")] ~?= "Ana",
    
    -- Caso con muchas personas
    "Caso 9: personaConMasAmigos con muchas personas" ~: personaConMasAmigos [("Ana", "Charlie"), ("Pedro", "Ana"), ("Jose", "Ana"), ("Lucia", "Ana")] ~?= "Ana"
    ]
