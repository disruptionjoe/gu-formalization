#!/usr/bin/env python3
"""LEG 3 - characterize the EXTERNAL datum precisely.

Question (firewall weak form, location half): does GU genuinely REDUCE "how many
generations" to a topological/families INDEX of an EXTERNAL base (the compactification
topology: the metric fiber GL(4,R)/O(3,1), or the K3-end), so the count is set by the
base manifold rather than the Clifford algebra? And is that REDUCTION sound independent
of whether the specific value (24 -> 3) was honestly derived or imported?

This script does NOT re-derive the internal under-determination (steps 7/9/10/11 do that).
It characterizes the two candidate EXTERNAL bases and asks, for each, whether an index over
it could carry the prime 3 at all, and whether GU's internal data SELECTS the base or the
normalization. No target is fitted; anchors are reproduced as a guard.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0] * 9 + [-1.0] * 5)


def factor(n):
    n = int(round(n)); m = abs(n); f = {}; d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def fstr(n):
    f = factor(n)
    s = " . ".join(f"{p}^{k}" if k > 1 else f"{p}" for p, k in sorted(f.items())) or "1"
    return f"{'-' if n < 0 else ''}{s}"


def main():
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"

    def sig(A):
        ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        tol = 1e-7 * np.abs(ev).max()
        return int((ev > tol).sum()) - int((ev < -tol).sum())

    def gd(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex); M[i, j] = ETA[j]; M[j, i] = -ETA[i]; return M

    def sigma(i, j):
        return 0.25 * (e128[i] @ e128[j] - e128[j] @ e128[i])

    def Jfull(i, j):
        return np.kron(Mvec(i, j), np.eye(DIM)) + np.kron(np.eye(N), sigma(i, j))

    def conn_index(J):
        return sig(herm(gd(1j * J)))

    print("\n" + "=" * 78)
    print("STEP A. Is the FILE'S internal claim reproduced: the natural geometric '3'")
    print("        (self-dual Lambda^2_+ over a Euclidean 4-frame) gives pointwise index 0?")
    print("=" * 78)
    SDp = [Jfull(0, 1) + Jfull(2, 3), Jfull(0, 2) + Jfull(3, 1), Jfull(0, 3) + Jfull(1, 2)]
    sd = [conn_index(J) for J in SDp]
    pairs = list(itertools.combinations(range(N), 2))
    rng = np.random.default_rng(3)
    Js = [Jfull(i, j) for i, j in pairs]
    alg = [conn_index(sum(c * Js[i] for i, c in enumerate(rng.standard_normal(len(Js))))) for _ in range(3)]
    print(f"  self-dual su(2)_+ pointwise indices (the geometric '3'): {sd}")
    print(f"  random metric so(9,5) connection indices:                {alg}")
    metric_pointwise_zero = all(v == 0 for v in sd + alg)
    print(f"  => every metric so(9,5) connection gives pointwise index 0: {metric_pointwise_zero}")
    print("     So the spectral asymmetry that a families/spectral-flow invariant would")
    print("     integrate over the base VANISHES pointwise for physical connections.")

    print("\n" + "=" * 78)
    print("STEP B. CANDIDATE BASE 1 -- the metric fiber GL(4,R)/O(3,1).")
    print("        Homotopy retract and the prime content of where a families index lives.")
    print("=" * 78)
    # GL(4,R) ~ O(4) (maximal compact); O(3,1) ~ O(3)xO(1) (maximal compact).
    # GL(4,R)/O(3,1) ~ O(4)/(O(3)xO(1)) = Grassmannian of unoriented lines in R^4 = RP^3.
    # (the "time direction" of the Lorentzian metric is an unoriented line.)
    print("  GL(4,R) retracts to O(4); O(3,1) retracts to O(3)xO(1).")
    print("  GL(4,R)/O(3,1) ~ O(4)/(O(3)xO(1)) = Grassmannian of unoriented lines in R^4 = RP^3.")
    # H^*(RP^3; Z): degrees 0..3 = Z, Z/2, 0, Z.  Reduced K-theory: K~^0(RP^3)=Z/2, K^1(RP^3)=Z.
    cohomology = {0: ("Z", 0), 1: ("Z/2", 2), 2: ("0", 0), 3: ("Z", 0)}
    print("  H^k(RP^3; Z) =", {k: v[0] for k, v in cohomology.items()})
    print("  Reduced K-theory: K~^0(RP^3) = Z/2,  K^1(RP^3) = Z  (a known computation).")
    torsion_primes = sorted({p for k, (grp, tor) in cohomology.items() if tor for p in factor(tor)})
    print(f"  All torsion in H^*(RP^3) and K~(RP^3) is 2-PRIMARY: torsion prime set = {torsion_primes}")
    fiber_can_carry_3 = 3 in torsion_primes
    print(f"  => a families/odd index over this base lands in a 2-primary group; can it carry 3? {fiber_can_carry_3}")
    print("  STRUCTURAL READING: the reduction 'count = families index over the metric fiber'")
    print("  is well-posed in SHAPE but is provably 3-FREE -- the metric-fiber base can only")
    print("  ever deliver an even / 2-torsion answer, never the odd prime 3.")

    print("\n" + "=" * 78)
    print("STEP C. CANDIDATE BASE 2 -- the K3-end. Where the prime 3 actually lives,")
    print("        and the cost (imports) of extracting it.")
    print("=" * 78)
    k3 = {"chi(K3)": 24, "Ahat(K3)": 2, "sig(K3)": -16, "p1(K3)": -48,
          "ch2(S_X)[K3] honest": -5376}
    for name, val in k3.items():
        has3 = 3 in factor(val)
        print(f"  {name:24} = {val:6}  = {fstr(val):16}  contains prime 3? {has3}")
    print("  The narrative route to 3:  chi(K3)=24  ->  24 / 8  =  3.")
    print("  Two SEPARATE imports are required for that line:")
    print("    (i)  CHOICE OF BASE: 'the relevant base is K3' is not selected by GU internal data")
    print("         (ic4-ricci-flat-k3-selection: K3 metric selection is CONDITIONAL on K3 topology")
    print("          being fixed first; the source-free equations do not pick K3).")
    print("    (ii) NORMALIZATION: the divisor 8 (H-line / spinor-unit) is the target-fitted step;")
    print("         the honest characteristic class is ch2(S_X)[K3] = -5376, not 24.")
    print(f"  NOTE (honesty): the prime 3 IS present in -5376 ({fstr(-5376)}), but -5376/8 = -672,")
    print("  not a clean generation count. The clean '24' (hence the clean 3) is the imported object.")

    print("\n" + "=" * 78)
    print("STEP D. Does GU INTERNAL (Clifford) data SELECT the external base or the")
    print("        normalization? (the load-bearing question for the REDUCTION's soundness)")
    print("=" * 78)
    # The internal data fixes the signature (9,5) -> metric fiber model, NOT the K3-end.
    metric_sig = int(sum(int(np.sign((e128[a] @ e128[a])[0, 0].real)) for a in range(N)))
    print(f"  internal data fixes the metric signature (declared input): tr(sign e_a^2) = {metric_sig} (=9-5)")
    print("  -> this points at the metric-fiber base (signature geometry), which is 3-FREE (Step B).")
    print("  -> it does NOT point at, or select, the K3-end (the only 3-carrying base, Step C).")
    print("  So the internal data neither selects the 3-carrying base nor fixes the /8 normalization.")
    print("  The reduction therefore has TWO stacked external imports: WHICH base, and the VALUE/norm.")

    print("\n" + "=" * 78)
    print("LEG 3 VERDICT")
    print("=" * 78)
    print("  LOCATION half  (count is external/global, not in the Clifford algebra): SOUND.")
    print("    - internal data gives a free rank / pointwise-zero metric index (steps 7/9/10/11);")
    print("    - any honest integer must be a GLOBAL index, i.e. it lives OUTSIDE the algebra.")
    print("  IDENTIFICATION half (the external datum is specifically 'a topological index of THE")
    print("    compactification base'): NOT ESTABLISHED, and partially refuted:")
    print("    - the families pushforward is not closed (non-convex fiber, no Fredholm family /")
    print("      K-orientation: FamiliesIndexPushforwardGate_V0 open);")
    print("    - the signature-selected base (metric fiber ~ RP^3) is 2-primary, hence 3-FREE;")
    print("    - the only 3-carrying base (K3-end) is itself an unforced import, and its honest")
    print("      class is -5376, with the clean 24 (and the /8) target-fitted.")
    print("  => 'multiplicity = a topological index of the external base' is a SOUND statement about")
    print("     WHERE the answer must come from (outside the Clifford algebra), but is NOT a sound")
    print("     IDENTIFICATION of a specific base-invariant that GU's data computes. The base itself")
    print("     is a second external datum GU does not pin; the value 24/3 is a third.")

    assert metric_pointwise_zero, "metric so(9,5) connections must give pointwise index 0"
    assert not fiber_can_carry_3, "metric-fiber base must be 3-free (2-primary)"
    assert 3 in factor(24) and 3 in factor(-5376), "sanity: 3 lives in the K3-end numbers"
    return {
        "anchors_ok": True,
        "metric_pointwise_zero": metric_pointwise_zero,
        "metric_fiber_torsion_primes": torsion_primes,
        "metric_fiber_3_free": not fiber_can_carry_3,
        "k3_chi": 24, "ch2_honest": -5376,
    }


if __name__ == "__main__":
    out = main()
    print("\nRESULT:", out)
