import Test.HUnit
import Ej7 -- Assuming the module name is Ej7

-- Test data
contactos :: ContactosTel
contactos = [("Alice", "1234"), ("Bob", "5678"), ("Charlie", "91011")]

-- Tests for enLosContactos
testEnLosContactos = TestList [
    TestCase (assertBool "Alice should be in contactos" (enLosContactos "Alice" contactos)),
    TestCase (assertBool "Bob should be in contactos" (enLosContactos "Bob" contactos)),
    TestCase (assertBool "Charlie should be in contactos" (enLosContactos "Charlie" contactos)),
    TestCase (assertBool "David should not be in contactos" (not (enLosContactos "David" contactos)))
    ]

-- Tests for agregarContacto
testAgregarContacto = TestList [
    TestCase (assertEqual "Add new contact David" [("David", "1213"), ("Alice", "1234"), ("Bob", "5678"), ("Charlie", "91011")] (agregarContacto ("David", "1213") contactos)),
    TestCase (assertEqual "Update existing contact Alice" [("Alice", "0000"), ("Bob", "5678"), ("Charlie", "91011")] (agregarContacto ("Alice", "0000") contactos))
    ]

-- Tests for eliminarContacto
testEliminarContacto = TestList [
    TestCase (assertEqual "Remove existing contact Alice" [("Bob", "5678"), ("Charlie", "91011")] (eliminarContacto "Alice" contactos)),
    TestCase (assertEqual "Remove non-existing contact David" contactos (eliminarContacto "David" contactos))
    ]

-- Run all tests
main :: IO Counts
main = runTestTT $ TestList [testEnLosContactos, testAgregarContacto, testEliminarContacto]