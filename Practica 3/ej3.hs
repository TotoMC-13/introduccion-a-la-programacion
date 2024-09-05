-- (res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para algún k ∈ Z con k ̸= 0)
-- k = -a/b, si a/b no da como resultado un entero entonces es False ya que k ∈ Z

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = x `mod` y == 0