#!/usr/bin/env python3
"""
Executable certificate for the Distler-Garibaldi (DG) scope-exit note.

Purpose
-------
Verify the PURELY STRUCTURAL group-theory facts that make DG assumption DG-A1
(the gauge group is a real form of E8) impossible to satisfy for GU's gauge
group Sp(64) = U(64,H) (compact symplectic group of 64x64 quaternionic unitary
matrices). Two independent obstructions are checked:

  (I)  dimension obstruction: dim_R Sp(64) = 8256 > 248 = dim E8, so sp(64)
       cannot be a subalgebra of any real form of e8 (a subalgebra has
       dimension <= the ambient algebra).

  (II) rank obstruction: rank Sp(64) = 64 > 8 = rank E8. A maximal torus of a
       (compact) subgroup embeds in a maximal torus of the ambient compact
       group, so rank of a subgroup <= rank of the group. 64 > 8 forbids it.

Either obstruction alone kills DG-A1. Both are reported.

HOUSE-DISCIPLINE NOTE
---------------------
Every number here is a Lie-group structural constant (dim/rank of standard
groups). NO generation target (3, 8, 16, 24, 32, chi(K3)=24, ...) is imported,
divided by, or normalized to anywhere in this file. The scope-exit verdict is
independent of the value of ind_H(D_GU).

Independent re-derivation
-------------------------
dim and rank of Sp(n) [compact, quaternionic n x n unitary, sometimes written
USp(2n)] are computed two ways and cross-checked:
  * closed form: dim = n(2n+1), rank = n
  * root-count:  dim = rank + #roots, with Sp(n) having 2n^2 roots (type C_n).
E8 dim/rank are likewise cross-checked against its root-count (240 roots).
"""

def sp_dim_closedform(n):
    # compact Sp(n) = USp(2n), quaternionic unitary n x n; dim_R = n(2n+1)
    return n * (2 * n + 1)

def sp_rank(n):
    # type C_n, rank n
    return n

def sp_num_roots(n):
    # C_n root system has 2 n^2 roots
    return 2 * n * n

def sp_dim_rootcount(n):
    # dim of a compact simple Lie group = rank + number of roots
    return sp_rank(n) + sp_num_roots(n)

# --- E8 structural constants (standard, exceptional group) ---
E8_DIM = 248
E8_RANK = 8
E8_NUM_ROOTS = 240  # E8 root system has 240 roots
E8_dim_rootcount = E8_RANK + E8_NUM_ROOTS

# --- GU gauge group: Sp(64) = U(64,H) ---
N = 64
sp64_dim_cf = sp_dim_closedform(N)
sp64_dim_rc = sp_dim_rootcount(N)
sp64_rank = sp_rank(N)

failures = []

# cross-check the two dim derivations for Sp(64)
if sp64_dim_cf != sp64_dim_rc:
    failures.append(f"Sp(64) dim mismatch: closed-form {sp64_dim_cf} != root-count {sp64_dim_rc}")

# cross-check E8 dim
if E8_DIM != E8_dim_rootcount:
    failures.append(f"E8 dim mismatch: stated {E8_DIM} != root-count {E8_dim_rootcount}")

# expected literal values (structural, not targets)
if sp64_dim_cf != 8256:
    failures.append(f"Sp(64) dim expected 8256, got {sp64_dim_cf}")
if sp64_rank != 64:
    failures.append(f"Sp(64) rank expected 64, got {sp64_rank}")

# --- Obstruction I: dimension ---
dim_obstruction = sp64_dim_cf > E8_DIM

# --- Obstruction II: rank ---
# real rank of ANY real form of E8 is at most the rank of complex E8 = 8
# (split form E8(8) attains 8; compact form has real rank 0). Subgroup rank
# (over the maximal torus / maximal split torus) is bounded by the ambient.
rank_obstruction = sp64_rank > E8_RANK

print("=" * 70)
print("DG scope-exit structural certificate")
print("=" * 70)
print(f"Sp(64)=U(64,H)  dim_R (closed form n(2n+1)) = {sp64_dim_cf}")
print(f"Sp(64)=U(64,H)  dim_R (rank + #roots)       = {sp64_dim_rc}")
print(f"Sp(64)=U(64,H)  rank                        = {sp64_rank}")
print(f"E8              dim                          = {E8_DIM}")
print(f"E8              dim (rank + #roots)          = {E8_dim_rootcount}")
print(f"E8              rank                         = {E8_RANK}")
print("-" * 70)
print(f"Obstruction I  (dim):  dim Sp(64)={sp64_dim_cf} > dim E8={E8_DIM}  -> {dim_obstruction}")
print(f"Obstruction II (rank): rank Sp(64)={sp64_rank} > rank E8={E8_RANK}  -> {rank_obstruction}")
print("-" * 70)

no_embedding = dim_obstruction and rank_obstruction

if failures:
    print("CROSS-CHECK FAILURES:")
    for f in failures:
        print("  ! " + f)

verdict_ok = no_embedding and not failures

if verdict_ok:
    print("VERDICT: No Lie-type embedding Sp(64) -> (real form of) E8 exists.")
    print("         DG-A1 (gauge group is a real form of E8) is UNSATISFIABLE for GU.")
    print("         [Both obstructions hold; both dim derivations agree.]")
    print("RESULT: PASS")
else:
    print("RESULT: FAIL")

import sys
sys.exit(0 if verdict_ok else 1)
