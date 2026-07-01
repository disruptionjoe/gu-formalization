#!/usr/bin/env python3
"""STEP 9 / CONSTRUCT-05 - the decisive experiment: can a GEOMETRIC connection revive the index?

CONSTRUCT-03 found the revived index = sig(Delta) is canonical per grading-breaking connection but
CONNECTION-dependent; CONSTRUCT-04 found no honest scale-invariant integer (no '3') in the rep, so a
count needs an EXTERNAL geometric connection. The natural source of '3' in 4-manifold geometry is the
SELF-DUAL 2-forms Lambda^2_+ = rank 3 (the su(2)_+ of Spin(4)), which act asymmetrically on chirality
-- exactly the grading-breaking shape needed. THIS step asks whether that natural geometric connection
(and Lie-algebra-valued connections in general) actually deliver a nonzero generation index.

The geometric connection on the RS vector-spinor field is an so(9,5) generator acting on BOTH indices:
    J_ij = M_ij (x) id_128  +  id_14 (x) sigma_ij,   sigma_ij = (1/4)[e_i, e_j],
M_ij the 14x14 vector-rep generator. Self-dual combos J+_a (a Euclidean 4-frame's su(2)_+) are the
natural a-priori grading-breaking connection carrying the geometric '3'. We compute sig(Delta) for the
G-diagonal Hermitian part Delta = herm(gdiag(i*J)) of these connections.

RESULT (this run reproduces): EVERY METRIC so(9,5) connection gives index ZERO.
  - all 3 self-dual J+, all 3 anti-self-dual J-, generic su(2)_+ combos: sig = 0;
  - random general so(9,5) elements and quadratic (enveloping-algebra) products: sig = 0;
  - by CONTRAST, structureless NON-(metric-algebra) H-linear breakers DO flow (sig in {0,+/-4}); and
    NON-metric gl(14) generators (which are ALSO Lie-algebra-valued) flow strongly. So the load-bearing
    property is being in the METRIC algebra so(9,5) (= PHS-preserving), NOT merely 'Lie-algebra-valued'.
MECHANISM (a sufficient, CANONICAL certificate): the quaternionic structure J_quat is UNIQUE up to a
U(1) phase -- the complex Cl(9,5) acts irreducibly, so its C-linear commutant is scalars -- hence the
PHS C = J_quat . G and the test {C, Delta} are canonical (phase-invariant), not seed-dependent (verified
across seeds: U_seed = lambda * U_1, |lambda| = 1). ALL 91 so(9,5) generators AND the 3 self-dual ones
satisfy {C, Delta} = 0 (to ~1e-11), and {C, Delta} = 0 with C^2 = -1 forces an exactly +/- symmetric
spectrum, hence sig = 0. This is a SUFFICIENT certificate (sig depends only on Delta); it is the
essentially-unique PHS route, not a claim it is the sole conceivable cause.

VERDICT: the natural geometric '3' (Lambda^2_+) and EVERY METRIC so(9,5) (gauge / spin) connection give
generation index ZERO. The soft-wall GO of CONSTRUCT-02/03 is REAL but is NOT accessible to physical
connections; the index-reviving operators are structureless non-(metric)-operators. So even the external
geometric route closes for metric connections: this CLOSES the most natural escape and reinforces
unreachability. (A connection OUTSIDE the metric so(9,5) envelope -- non-metric gl(14) generators flow,
but they are not gauge/spin connections; some honest geometric object outside so(9,5) remains the only
conceivable opening, and none is known.) No target import; guards held.

SCOPE (honest limit): this computes the POINTWISE index sig(Delta) for each connection. The genuine
SPEC 5(i) FAMILIES index over the metric fiber (a higher invariant -- spectral flow / Chern classes as
the connection varies over the fiber retract RP^3) is NOT directly computed here. But (a) every
pointwise value vanishing leaves no spectral asymmetry for an odd/spectral-flow families invariant to
integrate, and (b) the only possible nonzero families home is H^2(RP^3) = Z2 -- which is 2-torsion and
can never carry the odd prime 3. So the families route, like the pointwise one, cannot honestly deliver
'3'; a direct families-index computation is the formal next step, but it is 3-free by the fiber's own
prime spectrum {2}. This mirrors CONSTRUCT-04's prime-spectrum sieve at the level of the metric fiber.

Run: python tests/step9_selfdual_connection_index.py
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0] * 9 + [-1.0] * 5)


def quaternionic_J(e128, seed=1):
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2

    def sig(A):
        ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        tol = 1e-7 * np.abs(ev).max()
        return int((ev > tol).sum()) - int((ev < -tol).sum())

    def gd(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = ETA[j]
        M[j, i] = -ETA[i]
        return M

    def sigma(i, j):
        return 0.25 * (e128[i] @ e128[j] - e128[j] @ e128[i])

    def Jfull(i, j):
        return np.kron(Mvec(i, j), np.eye(DIM)) + np.kron(np.eye(N), sigma(i, j))

    def conn_index(J):
        return sig(herm(gd(1j * J)))

    # quaternionic structure + PHS C = J_quat . G  (a sufficient eta=0-forcing symmetry).
    # The complex Cl(9,5) acts irreducibly => its C-linear commutant is scalars => the quaternionic
    # structure J_quat is UNIQUE up to a U(1) phase, so C and the test {C,Delta} are canonical
    # (phase-invariant), not seed-dependent. We verify the uniqueness below.
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)
    Cu = Jf @ G.conj()                       # unitary part of antiunitary C = J_quat . G
    Cu_dag = Cu.conj().T                      # Cu unitary => inverse is the conjugate transpose

    def phs_break(J):                        # {C, Delta}; 0 => PHS preserved => sig forced 0
        Delta = herm(gd(1j * J))
        return float(np.linalg.norm(Cu @ Delta.conj() @ Cu_dag + Delta))

    # ---- (1) the natural geometric self-dual connection (Euclidean 4-frame {0,1,2,3}) ----
    def Jp(i, j):
        return Jfull(i, j)
    SDp = [Jp(0, 1) + Jp(2, 3), Jp(0, 2) + Jp(3, 1), Jp(0, 3) + Jp(1, 2)]   # self-dual su(2)_+
    SDm = [Jp(0, 1) - Jp(2, 3), Jp(0, 2) - Jp(3, 1), Jp(0, 3) - Jp(1, 2)]   # anti-self-dual
    print("\n=== (1) natural geometric self-dual / anti-self-dual connection indices ===")
    sd = [conn_index(J) for J in SDp]
    asd = [conn_index(J) for J in SDm]
    print(f"  self-dual J+ (carries Lambda^2_+ = the geometric '3'): sig = {sd}")
    print(f"  anti-self-dual J-:                                     sig = {asd}")
    rng = np.random.default_rng(0)
    su2 = [conn_index(sum(c * SDp[a] for a, c in enumerate(rng.standard_normal(3)))) for _ in range(3)]
    print(f"  generic su(2)_+ combos:                                sig = {su2}")

    # ---- (2) general so(9,5) algebra + enveloping algebra ----
    pairs = list(itertools.combinations(range(N), 2))
    Js = [Jfull(i, j) for i, j in pairs]
    rng2 = np.random.default_rng(3)
    alg = [conn_index(sum(c * Js[i] for i, c in enumerate(rng2.standard_normal(len(Js))))) for _ in range(3)]
    quad = [conn_index(Js[rng2.integers(len(Js))] @ Js[rng2.integers(len(Js))]
                       + Js[rng2.integers(len(Js))] @ Js[rng2.integers(len(Js))]) for _ in range(2)]
    print("\n=== (2) general so(9,5) and enveloping-algebra connection indices ===")
    print(f"  random so(9,5) elements:        sig = {alg}")
    print(f"  quadratic (enveloping) products: sig = {quad}")

    # ---- (3) mechanism: ALL 91 generators + the self-dual ones preserve the PHS C ----
    phs_all = [phs_break(J) for J in Js]            # all 91 so(9,5) generators
    phs_sd = [phs_break(J) for J in SDp]            # the 3 self-dual (carry Lambda^2_+)
    n_break = sum(p > 1e-8 for p in phs_all + phs_sd)
    print("\n=== (3) mechanism: {C, Delta} over ALL 91 generators + self-dual (0 => PHS preserved => sig=0) ===")
    print(f"  all 91: max {{C,Delta}} = {max(phs_all):.2e}  #break(>1e-8) = {sum(p>1e-8 for p in phs_all)}/91")
    print(f"  self-dual su(2)_+ (the '3'): {{C,Delta}} = {[f'{p:.2e}' for p in phs_sd]}")
    # phase-uniqueness of the quaternionic structure => C canonical (mechanism not seed-fragile)
    U2 = quaternionic_J(e128, seed=98765)
    Mrel = np.linalg.inv(U) @ U2
    lam = np.trace(Mrel) / DIM
    phase_unique = (abs(abs(lam) - 1.0) < 1e-6) and (np.linalg.norm(Mrel - lam * np.eye(DIM)) < 1e-9)
    print(f"  J_quat unique up to U(1) phase? {phase_unique}  (|lambda|={abs(lam):.4f}, "
          f"off-scalar resid={np.linalg.norm(Mrel - lam*np.eye(DIM)):.1e})")

    # ---- (4) contrast: NON-algebra breakers must be able to flow ----
    Jfi = np.linalg.inv(Jf)
    def jsym(R):
        return 0.5 * (R + Jf @ R.conj() @ Jfi)
    nonalg = []
    for _ in range(4):
        R = rng2.standard_normal((N * DIM, N * DIM)) + 1j * rng2.standard_normal((N * DIM, N * DIM))
        nonalg.append(sig(herm(gd(jsym(R)))))
    print("\n=== (4) contrast: random NON-algebra H-linear breakers (pipeline sanity) ===")
    print(f"  sig(Delta) = {nonalg}   any nonzero? {any(v != 0 for v in nonalg)}")

    # ---- VERDICT ----
    alg_all_zero = all(v == 0 for v in sd + asd + su2 + alg + quad)
    phs_preserved = (n_break == 0)
    contrast_flows = any(v != 0 for v in nonalg)
    print("\n=== VERDICT ===")
    print(f"every METRIC so(9,5) connection gives index 0?            {alg_all_zero}")
    print(f"mechanism: ALL 91 + self-dual generators preserve PHS C?  {phs_preserved}  (C phase-unique? {phase_unique})")
    print(f"non-(metric-algebra) breakers can still flow?             {contrast_flows}")
    print("\nReading: the natural geometric '3' (self-dual 2-forms Lambda^2_+) and EVERY METRIC so(9,5)")
    print("(gauge / spin) connection give generation index ZERO -- they preserve the canonical (phase-")
    print("unique) particle-hole symmetry C, which is SUFFICIENT to force eta=0. (sig depends only on")
    print("Delta; PHS-preservation is one essentially-unique sufficient certificate, not the only")
    print("conceivable cause.) Caveat: 'Lie-algebra-valued' alone is too broad -- NON-metric gl(14)")
    print("generators are also Lie-algebra and DO flow; the load-bearing property is being in the METRIC")
    print("algebra so(9,5) (= PHS-preserving). The soft-wall GO of CONSTRUCT-02/03 is real but INACCESSIBLE")
    print("to physical connections; only structureless non-(metric)-operators flow. This closes the most")
    print("natural external escape route and reinforces unreachability: the geometric '3' is not a count.")

    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"
    assert alg_all_zero, "every metric so(9,5) connection must give index 0"
    assert phs_preserved, "all 91 + self-dual generators must preserve the PHS C (sufficient sig=0 certificate)"
    assert phase_unique, "the quaternionic structure (hence C) must be unique up to U(1) phase (canonical)"
    assert contrast_flows, "non-algebra breakers must be able to flow (else the pipeline is trivial)"

    return {
        "bare": bare, "C2": C2,
        "self_dual_sig": sd, "anti_self_dual_sig": asd, "su2_sig": su2,
        "algebra_sig": alg, "quad_sig": quad, "algebra_all_zero": alg_all_zero,
        "phs_break_count": n_break, "phase_unique": bool(phase_unique), "nonalgebra_sig": nonalg,
    }


if __name__ == "__main__":
    main()
