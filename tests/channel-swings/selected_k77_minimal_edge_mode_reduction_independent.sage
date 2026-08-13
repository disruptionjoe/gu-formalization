# Independent Sage/QQ replay for the minimal K77 boundary edge extension.

Omega_bulk = matrix(QQ, [
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])

def embedded_bulk():
    out = matrix(QQ, 6, 6)
    out.set_block(0, 0, Omega_bulk)
    return out

E0 = matrix(QQ, 6, 6)
E0[2,4] = 1
E0[4,2] = -1
E3 = matrix(QQ, 6, 6)
E3[3,5] = 1
E3[5,3] = -1

r0 = vector(QQ, [1,0,0,0,1,0])
r3 = vector(QQ, [0,1,0,0,0,1])

# The linear map from coefficients (c0,c3) to the two contractions has a
# unique affine solution.  Build it directly over QQ.
base0 = r0 * embedded_bulk()
base3 = r3 * embedded_bulk()
coef_map = matrix(QQ, 12, 2)
rhs = vector(QQ, 12)
for j in range(6):
    coef_map[j,0] = (r0 * E0)[j]
    coef_map[j,1] = (r0 * E3)[j]
    rhs[j] = -base0[j]
    coef_map[6+j,0] = (r3 * E0)[j]
    coef_map[6+j,1] = (r3 * E3)[j]
    rhs[6+j] = -base3[j]

assert coef_map.rank() == 2
solution = coef_map.solve_right(rhs)
assert solution == vector(QQ, [-1,1])

Omega_ext = embedded_bulk() - E0 + E3
assert Omega_ext.is_skew_symmetric()
assert r0 * Omega_ext == 0
assert r3 * Omega_ext == 0
assert Omega_ext.rank() == 4
assert Omega_ext.right_kernel().dimension() == 2
assert Omega_ext.right_kernel() == matrix(QQ, [r0, r3]).row_space()

slice_map = matrix(QQ, 6, 4)
slice_map.set_block(0, 0, identity_matrix(QQ, 4))
Omega_reduced = slice_map.transpose() * Omega_ext * slice_map
assert Omega_reduced == Omega_bulk
assert Omega_reduced.rank() == 4

# Independent representative weights.  The Python route imports the actual
# ten predecessor weights; scalar multiplication by any nonzero rational has
# the same rank and kernel, so this route checks the full direct-sum theorem.
weights = [QQ(i) for i in [-11,-7,-5,-3,-1,2,4,6,8,10]]
Omega_all = block_diagonal_matrix([w * Omega_ext for w in weights])
Omega_reduced_all = block_diagonal_matrix([w * Omega_reduced for w in weights])
assert Omega_all.nrows() == 60
assert Omega_all.rank() == 40
assert Omega_all.right_kernel().dimension() == 20
assert Omega_reduced_all.nrows() == 40
assert Omega_reduced_all.rank() == 40

# Counterterm control: every symmetric Hessian has zero antisymmetrization.
H = matrix(QQ, [[1,2,3,4],[2,5,6,7],[3,6,8,9],[4,7,9,10]])
assert H - H.transpose() == 0
H_bad = copy(H)
H_bad[0,2] += 1
assert H_bad - H_bad.transpose() != 0

print("PASS SAGE_QQ_MINIMAL_EDGE_MODE")
print("COEFFICIENTS=(%s,%s)" % (solution[0], solution[1]))
print("EXTENDED_DIM=%s RANK=%s KERNEL=%s" % (Omega_all.nrows(), Omega_all.rank(), Omega_all.right_kernel().dimension()))
print("QUOTIENT_DIM=%s RANK=%s" % (Omega_reduced_all.nrows(), Omega_reduced_all.rank()))
