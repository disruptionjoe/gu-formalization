#!/usr/bin/env sage-python
"""Exact portfolio test for the ten H640 transverse defect images.

This decides the shared-subspace hypothesis and tests the first natural
N* tensor S intertwiner. It does not identify unrelated rank-128 objects or
claim a full Spin(6,4) associated-bundle theorem.
"""
from sage.all import GF, block_matrix, identity_matrix, matrix, zero_matrix

F = GF(1009)
n, nv, spin, total = 7, 14, 128, 1920
i2 = identity_matrix(F, 2, sparse=True)
s1 = matrix(F, [[0, 1], [1, 0]], sparse=True)
s3 = matrix(F, [[1, 0], [0, -1]], sparse=True)
eps = matrix(F, [[0, 1], [-1, 0]], sparse=True)

def tensor_all(xs):
    out = matrix(F, [[1]], sparse=True)
    for x in xs:
        out = out.tensor_product(x)
    return out

plus, minus = [], []
for k in range(n):
    plus.append(tensor_all([s3] * k + [s1] + [i2] * (n - 1 - k)))
    minus.append(tensor_all([s3] * k + [eps] + [i2] * (n - 1 - k)))
gammas = plus + minus
eta = [1] * 7 + [-1] * 7
i128 = identity_matrix(F, spin, sparse=True)
z128 = zero_matrix(F, spin, spin, sparse=True)
i1920 = identity_matrix(F, total, sparse=True)
omega = i128
for g in gammas:
    omega *= g
p_plus = (i128 + omega) / F(2)
p_minus = (i128 - omega) / F(2)

def block_spin(v):
    return block_matrix(F, nv, nv,
        [[v if r == c else z128 for c in range(nv)] for r in range(nv)],
        sparse=True)

def wedge(k):
    return block_matrix(F, nv, nv,
        [[F(eta[r]) * gammas[r] * gammas[k] * gammas[c]
          if r != k and c not in (r, k) else z128
          for c in range(nv)] for r in range(nv)], sparse=True)

def k_map(k):
    return block_matrix(F, nv, 1,
        [[i128 if r == k else z128] for r in range(nv)], sparse=True)

def codiff(k):
    return block_matrix(F, 1, nv,
        [[F(eta[c]) * i128 if c == k else z128 for c in range(nv)]], sparse=True)

weights = p_plus + F(2) * p_minus
southeast = F(11) / F(24) * p_plus + F(11) / F(12) * p_minus

def symbol(k):
    return block_matrix(F, 2, 2,
        [[wedge(k) * block_spin(weights), k_map(k)],
         [-codiff(k), gammas[k] * southeast]], sparse=True)

symbols = [symbol(k) for k in range(14)]
evolutions = {k: symbols[0].solve_right(symbols[k]) for k in range(1, 14)}

observed_slots = (0, 7, 8, 9, 14)
slot_lift = matrix(F, 15, 5, sparse=True)
for c, r in enumerate(observed_slots):
    slot_lift[r, c] = 1
coordinate_lift = slot_lift.tensor_product(i128)
observation = coordinate_lift.transpose()
zero_seed = block_matrix(F, 2, 1,
    [[zero_matrix(F, nv * spin, spin, sparse=True)], [i128]], sparse=True)
obs = (7, 8, 9)
e0, e1, e2 = [evolutions[k] for k in obs]
words = [i1920, e0, e1, e2, e0*e1, e0*e2, e1*e2, e0*e1*e2]
span = block_matrix(F, 1, len(words), [[w*zero_seed for w in words]], sparse=True)
h640 = span.matrix_from_columns(list(span.pivots()))
rh = observation * h640
lift = h640 * rh.inverse()
complement = i1920 - lift * observation
transverse = tuple(k for k in range(1, 14) if k not in obs)

images = {}
raw_maps = {}
for k in transverse:
    raw = complement * evolutions[k] * lift
    raw_maps[k] = raw
    images[k] = raw.matrix_from_columns(list(raw.pivots()))
    assert images[k].rank() == 128

print("transverse", transverse)
print("signs", {k: eta[k] for k in transverse})
joins, intersections = {}, {}
for ai, i in enumerate(transverse):
    for j in transverse[ai+1:]:
        joined = block_matrix(F, 1, 2, [[images[i], images[j]]], sparse=True).rank()
        joins[(i,j)] = int(joined)
        intersections[(i,j)] = 256 - int(joined)

from collections import Counter
print("join histogram", Counter(joins.values()))
print("intersection histogram", Counter(intersections.values()))
print("same-sign join histogram", Counter(v for (i,j),v in joins.items() if eta[i] == eta[j]))
print("opposite-sign join histogram", Counter(v for (i,j),v in joins.items() if eta[i] != eta[j]))
print("pairs", joins)
assert set(joins.values()) == {256}
assert set(intersections.values()) == {0}

# Strongest cheap common-module check: each image's observation-slot support.
def slot_support(basis):
    support=[]
    for slot in range(15):
        rows=list(range(slot*128,(slot+1)*128))
        if basis.matrix_from_rows(rows).rank():
            support.append(slot)
    return tuple(support)
print("slot supports", {k:slot_support(v) for k,v in images.items()})
domain_block_ranks = {}
for k, raw in raw_maps.items():
    domain_block_ranks[k] = tuple(
        int(raw.matrix_from_columns(range(block*128, (block+1)*128)).rank())
        for block in range(5)
    )
print("domain block ranks (four vector slots, zero-form)", domain_block_ranks)

# Full sum dimension tests whether there is one shared D, a direct sum of ten,
# or an intermediate module. This is coordinate-free as a span dimension only.
all_join = block_matrix(F, 1, len(transverse), [[images[k] for k in transverse]], sparse=True)
print("all defect span rank", all_join.rank())
assert all_join.rank() == 1280

# Candidate natural-module map: feed the shared observed zero-form spinor into
# each transverse residual.  This is stronger than equal rank and makes the
# covector label explicit.
zero_cols = range(4*128, 5*128)
phi_blocks = [raw_maps[k].matrix_from_columns(zero_cols) for k in transverse]
phi = block_matrix(F, 1, len(phi_blocks), [phi_blocks], sparse=True)
phi_eta = block_matrix(F, 1, len(phi_blocks),
    [[F(eta[k]) * raw_maps[k].matrix_from_columns(zero_cols) for k in transverse]],
    sparse=True)
print("zero-form residual assembly rank", phi.rank())
assert phi.rank() == 1280

def spin_gen(i, j):
    return (gammas[i] * gammas[j]) / F(2)

def vector_gen(i, j):
    # [S_ij,gamma(v)] = gamma(A_ij v)
    A = matrix(F, 14, 14, sparse=True)
    A[i,j] = F(eta[j])
    A[j,i] = -F(eta[i])
    return A

def full_carrier_gen(i, j):
    A = vector_gen(i,j)
    Sij = spin_gen(i,j)
    one = (-A.transpose()).tensor_product(i128) + block_matrix(
        F, 14, 14,
        [[Sij if r == c else z128 for c in range(14)] for r in range(14)],
        sparse=True,
    )
    return block_matrix(F, 2, 2,
        [[one, zero_matrix(F,14*128,128,sparse=True)],
         [zero_matrix(F,128,14*128,sparse=True), Sij]], sparse=True)

def source_tensor_gen(i, j):
    # N^* tensor S in the ordering used by phi.
    A = vector_gen(i,j)
    pos = {axis:k for k,axis in enumerate(transverse)}
    AN = matrix(F, 10, 10, sparse=True)
    for a in transverse:
        for b in transverse:
            AN[pos[a],pos[b]] = A[a,b]
    Sij = spin_gen(i,j)
    return (-AN.transpose()).tensor_product(i128) + block_matrix(
        F, 10, 10,
        [[Sij if r == c else z128 for c in range(10)] for r in range(10)],
        sparse=True,
    )

equivariant = {}
equivariant_eta = {}
for ai,i in enumerate(transverse):
    for j in transverse[ai+1:]:
        defect = full_carrier_gen(i,j) * phi - phi * source_tensor_gen(i,j)
        equivariant[(i,j)] = defect.is_zero()
        defect_eta = full_carrier_gen(i,j) * phi_eta - phi_eta * source_tensor_gen(i,j)
        equivariant_eta[(i,j)] = defect_eta.is_zero()
print("so(6,4) N* tensor S equivariance", sum(equivariant.values()), "/", len(equivariant))
if not all(equivariant.values()):
    print("non-equivariant pairs", [k for k,v in equivariant.items() if not v])
print("eta-scaled so(6,4) N* tensor S equivariance", sum(equivariant_eta.values()), "/", len(equivariant_eta))
if not all(equivariant_eta.values()):
    print("eta-scaled non-equivariant pairs", [k for k,v in equivariant_eta.items() if not v])
same_sign = [pair for pair in equivariant if eta[pair[0]] == eta[pair[1]]]
mixed_sign = [pair for pair in equivariant if eta[pair[0]] != eta[pair[1]]]
assert len(same_sign) == 21 and all(equivariant[pair] for pair in same_sign)
assert len(mixed_sign) == 24 and not any(equivariant[pair] for pair in mixed_sign)

# Planted failure: if the ten images were literally one shared D, joining the
# first image to itself would stay rank 128, unlike every real pair above.
duplicate_join = block_matrix(F, 1, 2,
    [[images[transverse[0]], images[transverse[0]]]], sparse=True).rank()
assert duplicate_join == 128 and duplicate_join != next(iter(joins.values()))

print("PASS: 10 rank-128 images are pairwise disjoint; total rank 1280")
print("PASS: 21/21 compact same-sign intertwiners; 0/24 mixed boosts")
print("OPEN: normalization/companion solve for full so(6,4) equivariance")
