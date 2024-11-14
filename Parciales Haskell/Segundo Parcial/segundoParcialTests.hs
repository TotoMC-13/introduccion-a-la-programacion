import Test.HUnit
import SegundoParcial

tests1 = test[
    "Una sola formula: " ~: porcentajeDeVotos "a" [("a","b")] [5] ~?= 100.0,
    "Tres formulas: " ~: porcentajeDeVotos "e" [("a","b"),("c","d"),("e","f")] [5,10,5] ~?= 25.0,
    "Tres formulas, mismos votos: " ~: porcentajeDeVotos "e" [("a","b"),("c","d"),("e","f")] [3,3,3] ~?= 33.333332
    ]

tests2 = test[
    "1 formula: " ~: proximoPresidente [("a","b")] [5] ~?= "a",
    "3 formulas, gana la segunda: " ~: proximoPresidente [("a","b"),("c","d"),("e","f")] [5,10,5] ~?= "c",
    "5 formulas, gana ultima " ~: proximoPresidente [("a","b"),("c","d"),("e","f"),("g","h"),("i","j")] [10,7,40,32,50] ~?= "i",
    "3 formulas, empate entre las 2 primeras " ~: proximoPresidente [("a","b"),("c","d"),("e","f")] [10,10,5] ~?= "a"
    ]

main = runTestTT tests2