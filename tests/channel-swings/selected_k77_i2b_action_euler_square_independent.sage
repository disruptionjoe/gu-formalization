#!/usr/bin/env sage
"""Independent exact checksum for the reduced corrected-E_act square."""

R.<rho, r, kappa> = PolynomialRing(QQ)
G = matrix(QQ, [[160, 320, 0], [320, 640, 0], [0, 0, 2]])
c = vector(R, [rho + r^2/3, r^2/3, kappa*r])
potential = (c * G * c) / 2
expected = 80*(rho + r^2)^2 + kappa^2*r^2
assert potential == expected
assert G.rank() == 2
assert diff(potential, r) == 2*r*(kappa^2 + 160*r^2 + 160*rho)
assert matrix(QQ, [[1, -44], [1, 36]]).det() == 80
print("PASS corrected-E_act reduced exact checksum")
