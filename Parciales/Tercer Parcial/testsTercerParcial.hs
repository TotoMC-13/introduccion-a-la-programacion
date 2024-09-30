import Test.HUnit
import TercerParcial

-- Ejemplo de registro de alumnos
registroEjemplo :: Registro
registroEjemplo = [
    ("Ana", [10, 9, 8]),
    ("Beatriz", [6, 8, 9]),
    ("Carlos", [5, 7, 8]),
    ("Elena", [9, 10, 9])
  ]

-- Test para `aproboMasDeNMAterias`
testAproboMasDeNMAterias :: Test
testAproboMasDeNMAterias = TestCase $ do
    assertEqual "Ana tiene más de 2 materias aprobadas" True (aproboMasDeNMAterias registroEjemplo "Ana" 2)
    assertEqual "Beatriz no tiene más de 2 materias aprobadas" True (aproboMasDeNMAterias registroEjemplo "Beatriz" 2)
    assertEqual "Carlos tiene más de 1 materia aprobada" True (aproboMasDeNMAterias registroEjemplo "Carlos" 1)
    assertEqual "Elena tiene más de 2 materias aprobadas" True (aproboMasDeNMAterias registroEjemplo "Elena" 2)

-- Test para `buenosAlumnos`
testBuenosAlumnos :: Test
testBuenosAlumnos = TestCase $ do
    assertEqual "Lista de buenos alumnos" ["Ana", "Elena"] (buenosAlumnos registroEjemplo)

-- Test para `mejorPromedio`
testMejorPromedio :: Test
testMejorPromedio = TestCase $ do
    assertEqual "Alumno con mejor promedio" "Elena" (mejorPromedio registroEjemplo)

-- Test para `seGraduoConHonores`
testSeGraduoConHonores :: Test
testSeGraduoConHonores = TestCase $ do
    assertEqual "Elena se graduó con honores" True (seGraduoConHonores registroEjemplo 3 "Elena")
    assertEqual "Carlos no se graduó con honores" False (seGraduoConHonores registroEjemplo 3 "Carlos")

-- Agrupación de todas las pruebas
tests :: Test
tests = TestList [
    testAproboMasDeNMAterias,
    testBuenosAlumnos,
    testMejorPromedio,
    testSeGraduoConHonores
  ]

main :: IO ()
main = do
    _ <- runTestTT tests
    return ()
