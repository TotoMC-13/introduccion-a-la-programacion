module Main where

import Ej2
import Test.HUnit

testMismosElementos :: Test
testMismosElementos = TestList [
    "Test 1" ~: mismosElementos [1, 2, 3] [3, 2, 1] ~?= True,
    "Test 2" ~: mismosElementos [1, 2, 2, 3] [3, 2, 1] ~?= True,
    "Test 3" ~: mismosElementos [1, 2, 3] [4, 5, 6] ~?= False,
    "Test 4" ~: mismosElementos [1, 2, 3] [1, 2, 2, 3, 3] ~?= True,
    "Test 5" ~: mismosElementos ([] :: [Int]) ([] :: [Int]) ~?= True,
    "Test 6" ~: mismosElementos [1, 2, 3] [] ~?= False,
    "Test 7" ~: mismosElementos [] [1, 2, 3] ~?= False,
    "Test 8" ~: mismosElementos [1, 1, 1] [1] ~?= True,
    "Test 9" ~: mismosElementos [1, 2, 3, 4] [1, 2, 3] ~?= False,
    "Test 10" ~: mismosElementos [1, 2, 3] [1, 2, 3, 4] ~?= False,
    "Test 11" ~: mismosElementos ["apple", "banana", "cherry"] ["cherry", "banana", "apple"] ~?= True,
    "Test 12" ~: mismosElementos ["apple", "banana", "banana", "cherry"] ["cherry", "banana", "apple"] ~?= True,
    "Test 13" ~: mismosElementos ["apple", "banana", "cherry"] ["date", "fig", "grape"] ~?= False,
    "Test 14" ~: mismosElementos ["apple", "banana", "cherry"] ["apple", "banana", "banana", "cherry", "cherry"] ~?= True,
    "Test 15" ~: mismosElementos ([] :: [String]) ([] :: [String]) ~?= True,
    "Test 16" ~: mismosElementos ["apple", "banana", "cherry"] [] ~?= False,
    "Test 17" ~: mismosElementos [] ["apple", "banana", "cherry"] ~?= False,
    "Test 18" ~: mismosElementos ["apple", "apple", "apple"] ["apple"] ~?= True,
    "Test 19" ~: mismosElementos ["apple", "banana", "cherry", "date"] ["apple", "banana", "cherry"] ~?= False,
    "Test 20" ~: mismosElementos ["apple", "banana", "cherry"] ["apple", "banana", "cherry", "date"] ~?= False
    ]

main :: IO Counts
main = runTestTT testMismosElementos