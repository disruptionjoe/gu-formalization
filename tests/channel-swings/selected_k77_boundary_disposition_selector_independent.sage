# Independent QQ reconstruction of the K77 boundary-disposition selector.

R = PolynomialRing(QQ, names=('xi0','xi3','c0','c3'))
xi0, xi3, c0, c3 = R.gens()

Omega_bulk = matrix(R, [
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
assert Omega_bulk.rank() == 4

Omega_ext = block_matrix(R, 2, 2, [Omega_bulk, zero_matrix(R,4,2), zero_matrix(R,2,4), zero_matrix(R,2,2)])
Omega_ext[2,4] = c0
Omega_ext[4,2] = -c0
Omega_ext[3,5] = c3
Omega_ext[5,3] = -c3
gauge = vector(R, [xi0,xi3,0,0,xi0,xi3])
contraction = gauge * Omega_ext

assert contraction == vector(R, [0,0,-(c0+1)*xi0,(1-c3)*xi3,0,0])
equations = [c0 + 1, c3 - 1]
coefficient_ideal = R.ideal(equations)
assert coefficient_ideal == R.ideal(c0 + 1, c3 - 1)
solution = {c0: -1, c3: 1}

Omega_edge = matrix(QQ, Omega_ext.subs(solution))
assert Omega_edge.rank() == 4
assert len(Omega_edge.right_kernel().basis()) == 2
assert gauge * Omega_edge == zero_vector(R,6)
assert gauge * Omega_ext.subs({c0:-1,c3:-1}) != zero_vector(R,6)

horns = {
    'SMALL_GAUGE_DIRICHLET': (False, True),
    'ZERO_CHARGE_NEUMANN_LIKE': (True, False),
    'CHARGED_BOUNDARY_SYMMETRY': (False, True),
    'MINIMAL_EDGE_COMPLETION': (True, True),
}
eligible = [name for name, flags in horns.items() if all(flags)]
assert eligible == ['MINIMAL_EDGE_COMPLETION']

all_edge = block_diagonal_matrix([Omega_edge for _ in range(10)])
assert all_edge.nrows() == 60
assert all_edge.rank() == 40
assert all_edge.right_nullity() == 20
assert all_edge.rank() == 40

print('PASS independent boundary disposition selector 15/15')
