#!/usr/bin/env python3
"""Phase-0 scoping checks for the torsor-identification decision tree (ID-1).

DESIGN: explorations/phase0-torsor-identification-tree-2026-07-20.md
SCOPE:  Phase-0 ONLY -- settles ledger columns (naturality kill-test power,
        negative-control kill, minimal-sufficiency arithmetic). No Phase-1
        candidate is built or executed here.

WHAT IS CHECKED (all exact or machine-eps, seconds):
  [N] the NATURALITY kill test (commutant-valuedness vs all 14 Cl(9,5)
      generators) has demonstrated power:
        - R1 (known k = 64) PASSES bit-exact (linear + antilinear parts);
        - R2 (known rep-weight-blind, winding 0) is KILLED (residual O(1));
        - the PLANT (K_S-conjugated spin lift, deliberately false candidate)
          is KILLED by the same test, WHILE it passes the Z/2 shadow test
          exactly -- demonstrating the shadow test alone has zero power here.
  [Z] center-faithfulness: the adjoint action of -1 in Sp(1) is the identity
      rotation, so adjoint-type transports contradict the machine-verified
      deck monodromy Lambda(-v0) = -I and are excluded by the EXISTING Z/2
      receipt (new power extracted from an old verification).
  [M] minimal-sufficiency arithmetic: order(J(k)) = 3 iff 8|k and 3-not-|k;
      k = 64c lands in {0, 8nu, 16nu} for every integer c, order 3 iff
      3-not-|c; the class SET {8nu,16nu} is identical for every n with
      8|n, 3-not-|n -- the full-carrier value 64 buys nothing beyond it.
"""
from __future__ import annotations
import os, sys, time
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as bridge  # noqa: E402

FAILURES = []
def check(tag, name, ok, detail=""):
    s = "PASS" if ok else "FAIL"
    print(f"[{tag}] {s}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok: FAILURES.append(name)

t0 = time.time()
e, Gamma, Pi_RS, M_D = bridge.constraint_objects()
G = bridge.cl95.jordan_wigner_gammas(7)
I128 = np.eye(128, dtype=complex)

C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]      # J_quat = C . conj
K_S = e[0].copy()
for i in range(1, 9): K_S = K_S @ e[i]
check("T", "fixtures: J_quat^2 = -1, K_S Hermitian unitary",
      float(np.max(np.abs(C @ C.conj() + I128))) == 0.0
      and float(np.max(np.abs(K_S - K_S.conj().T))) < 1e-12
      and float(np.max(np.abs(K_S @ K_S - I128))) < 1e-12)

# ---- the naturality (commutant-valuedness) test ------------------------------------
def res_linear(X):        # linear twist generator vs the whole algebra
    return max(float(np.max(np.abs(X @ e[a] - e[a] @ X))) for a in range(14))
def res_antilinear(Cop):  # antilinear X = Cop . conj:  e_a Cop = Cop conj(e_a)
    return max(float(np.max(np.abs(e[a] @ Cop - Cop @ e[a].conj()))) for a in range(14))

# [N] power validation on known candidates
r1_lin  = res_linear(1j * I128)          # R1 linear generator i_R = i I
r1_anti = res_antilinear(C)              # R1 antilinear generator j_R = C . conj
check("N", "R1 (known k = 64) PASSES naturality bit-exact",
      r1_lin == 0.0 and r1_anti == 0.0, f"lin {r1_lin:.1e}, anti {r1_anti:.1e}")

Q0 = G[9] @ G[0]                          # R2 twist generator, legs (9,0,1,2)
r2_res = res_linear(Q0)
check("N", "R2 (known rep-weight-blind, winding 0) is KILLED by naturality",
      r2_res > 1.0, f"residual {r2_res:.2f}")

# [N] NEGATIVE CONTROL: the plant K7 = K_S-conjugated spin lift.
# Constructed to look plausible ('record-weighted transport'): unitary family,
# correct deck monodromy. Provably rep-weight-blind (winding is conjugation-
# invariant, so = R2's zero). The pipeline must kill it, and the Z/2 shadow
# test must NOT (that is exactly the verifier's rep-weight-blindness point).
def sphere(p, t, f):
    return np.array([np.cos(p), np.sin(p)*np.cos(t),
                     np.sin(p)*np.sin(t)*np.cos(f), np.sin(p)*np.sin(t)*np.sin(f)])
Q = [G[9] @ G[k] for k in (0, 1, 2)]
def lam(p, t, f):
    v = sphere(p, t, f)
    return v[0]*I128 + v[1]*Q[0] + v[2]*Q[1] + v[3]*Q[2]
def lam7(p, t, f):
    return K_S @ lam(p, t, f) @ K_S      # K_S unitary Hermitian: K_S^-1 = K_S

L7 = lam7(0.7, 1.1, 2.3)
shadow7 = float(np.max(np.abs(lam7(np.pi, 0, 0) + I128)))
check("N", "PLANT passes the Z/2 shadow test (deck monodromy -I exact) -- "
           "shadow test has NO power against it",
      float(np.max(np.abs(L7 @ L7.conj().T - I128))) < 1e-12 and shadow7 < 1e-12,
      f"|Lambda7(-v0) + I| = {shadow7:.1e}")
p_res = res_linear(K_S @ Q0 @ K_S)
check("N", "PLANT is KILLED by the naturality test",
      p_res > 1.0, f"residual {p_res:.2f}")

# [Z] center-faithfulness: adjoint of -1 is the identity rotation
def adj_rot(q):           # rotation matrix of x -> q x qbar on Im H
    w, x, y, z = q
    return np.array([
        [1-2*(y*y+z*z), 2*(x*y-w*z),   2*(x*z+w*y)],
        [2*(x*y+w*z),   1-2*(x*x+z*z), 2*(y*z-w*x)],
        [2*(x*z-w*y),   2*(y*z+w*x),   1-2*(x*x+y*y)]])
z_res = float(np.max(np.abs(adj_rot(np.array([-1.0, 0, 0, 0])) - np.eye(3))))
check("Z", "adjoint action of -1 in Sp(1) = identity -- adjoint-type transports "
           "contradict the verified deck monodromy -I and are EXCLUDED by the "
           "existing Z/2 receipt", z_res == 0.0)

# [M] minimal-sufficiency arithmetic
def order24(x): return next(n for n in range(1, 25) if (n * x) % 24 == 0)
ok_iff = all((order24(n % 24) == 3) == (n % 8 == 0 and n % 3 != 0)
             for n in range(1, 400))
check("M", "order(J(n)) = 3  iff  8|n and 3-not-|n (n = 1..399)", ok_iff)
ok_64c = all(((64*c) % 24 in (0, 8, 16)) and
             ((order24((64*c) % 24) == 3) == (c % 3 != 0)) for c in range(1, 100))
check("M", "k = 64c: class always in {0, 8nu, 16nu}; order 3 iff 3-not-|c "
           "(torsor-type degree c = +-1 always qualifies)", ok_64c)
classes = {tuple(sorted({(s*n) % 24 for s in (1, -1)}))
           for n in range(8, 400, 8) if n % 3 != 0}
check("M", "the orientation-unpinned class SET {8nu, 16nu} is IDENTICAL for "
           "every n with 8|n, 3-not-|n -- full-carrier n = 64 adds nothing "
           "beyond the minimal statement", classes == {(8, 16)})

print(f"\n{'ALL PASS' if not FAILURES else 'FAILURES: ' + str(FAILURES)}"
      f"  ({time.time()-t0:.1f} s)")
sys.exit(0 if not FAILURES else 1)
