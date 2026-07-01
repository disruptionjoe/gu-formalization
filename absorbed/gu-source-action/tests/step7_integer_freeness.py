#!/usr/bin/env python3
"""STEP 7 / CONSTRUCT-04 - degree-0 integer-freeness (the unreachability leg).

A generation count must be a SCALE-INVARIANT (degree-0 homogeneous in xi) INTEGER that also
carries Dirac/geometric content. CONSTRUCT-02 softened the eta=0 wall (the index route is alive),
so the program's terminal now rests on a different question: even WITH a revived index, can an
HONEST INTEGER -- let alone 3 -- be extracted from the existing bridge data without importing it?
This step gives the sharpest available negative evidence, in two independent prongs.

PRONG 1 - the RANK / DIMENSION sector (prime-spectrum sieve).
    Every integer the rep supplies natively is a dimension/rank: 128, 64, 14, 1792, 1664, 832,
    416, 896, 16, 64 (Sp). Each is {2,7,13}-smooth (128=2^7, 14=2.7, 1792=2^8.7, 1664=2^7.13, ...).
    The prime 3 is ABSENT from the entire Cl(9,5) dimension prime-spectrum. Hence no count, rank,
    index, or ratio-of-dimensions built from the rep can EQUAL 3 (or any 3.k) without injecting the
    foreign prime 3 from outside -- which is exactly the forbidden target import (24/8=3, chi(K3)=24).

PRONG 2 - the degree-0 RATIO sector (Dirac-content invariants).
    Build a catalog of homogeneous-in-xi functionals of {Pi, Q, M_D(xi), Gamma} and form every
    equal-degree ratio (=> degree-0). Each is tested for (a) xi-INDEPENDENCE (genuine invariant vs
    isotropy artifact) over repo + random Euclidean + (9,5)-mixed xi, and (b) INTEGER-ness. RESULT:
    in this Frobenius/trace-RATIO sector, of the xi-independent degree-0 invariants the ONLY integers
    are trivial tight-frame 1's (||Gamma M_D|| = ||M_D|| etc., no Dirac content); every Dirac-content
    ratio is a NON-INTEGER algebraic number -- a surd / rational over the same prime set {2,7,13}:
    C2/bare = sqrt(7), bare/||E|| = sqrt(2), tr(Pi Md M Pi)/tr(M_KT) = 7/2, ... NONE equals an import.

    SCOPE NOTE (after an adversarial counter-computation). 'Integer-free' is precise about the
    RATIO sector. Broadening to RANK / SIGNATURE / eigenvalue-count quantities DOES produce many
    integers (rank M_D = 1792, npos(Pi M_D Pi) = 832, ...). But those are conjugation-invariant
    DIMENSION counts -- unchanged under a unitary scramble of the gammas, so no geometric Dirac
    content -- and none is a derived 3/4/8/24. The single genuine degree-0 Dirac-content INTEGER is
    the metric signature tr(sign(e_a^2)) = 9 - 5 = 4. That is a STRUCTURAL INPUT (the chosen Cl(9,5)
    signature -- the prong-1 analog), NOT an invariant derived from {Pi,Q,M_D,Gamma}, and it is 4,
    not the generation target 3. So it is not a counterexample; it is declared, like the dimensions.

COMBINED VERDICT: no honest scale-invariant INTEGER with Dirac content exists in the bridge data;
the only native integers (dimension ranks) are 3-free by prime spectrum, and the only Dirac-content
degree-0 invariants are non-integer algebraics. So "three generations" is unreachable from the
existing GU data -- evidence (NOT proof; bounded by this finite low-word-length catalog) that the
soft-wall GO of CONSTRUCT-02, even if fully realized, cannot by itself deliver the count. HONESTY
NOTE: the prime 3 is NOT absent from the full invariant ring -- it appears in the DENOMINATORS of
the ratio-invariant squares (C2/||Pi M_D Pi|| = sqrt(7/24), 24 = 2^3.3). That only makes those
invariants MORE irrational; it never produces the integer 3. The precise claim is two-pronged: (i)
the native integer DIMENSIONS are 3-free, so no rank/count equals 3; (ii) no degree-0 Dirac
invariant is an integer at all. So any honest "3" must arise as a genuine EXTERNAL topological /
families INDEX over the Y14/K3 geometry (a true integer invariant the rep does not contain), not
from the rep's native dimensions or its degree-0 Dirac magnitudes; producing it from the rep alone
is a target import.

Guards: M_D / bare commutator untouched (read-only invariants); no target fitted anywhere.
Run: python tests/step7_integer_freeness.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM


def factorize(n):
    n = int(round(n)); f = {}; d = 2
    m = abs(n)
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def smooth_primes(n):
    return sorted(factorize(n).keys())


def rational_square(v, qmax=64):
    """if v^2 ~ p/q (q<=qmax), return (p,q) else None."""
    s = v * v
    for q in range(1, qmax + 1):
        p = s * q
        if abs(p - round(p)) < 1e-6 and round(p) != 0:
            return int(round(p)), q
    return None


def main():
    np.set_printoptions(precision=6, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2

    # =====================================================================================
    # PRONG 1 - rank / dimension prime spectrum: is 3 absent?
    # =====================================================================================
    dims = {
        "spinor S (2^7)": 128, "S^+ chiral / Sp rank": 64, "RS vector index": 14,
        "RS space 14x128": 1792, "ker(Gamma) constraint surf": 1664, "raw RS kernel": 832,
        "raw RS kernel_H": 416, "vector-spinor S^+": 896, "H-rank E_+": 32,
        "M(.,H) block 16": 16,
    }
    print("\n=== PRONG 1: Cl(9,5) dimension prime-spectrum (is 3 absent?) ===")
    all_primes = set()
    for name, d in dims.items():
        f = factorize(d); all_primes |= set(f.keys())
        fac = " . ".join(f"{p}^{k}" if k > 1 else f"{p}" for p, k in sorted(f.items()))
        print(f"  {name:30} = {d:5}  = {fac}")
    three_absent = 3 not in all_primes
    print(f"  prime spectrum of all native dimensions = {sorted(all_primes)}")
    print(f"  => prime 3 ABSENT from the Cl(9,5) dimension spectrum: {three_absent}")
    print("     (so no REP-NATIVE rank/count equals 3.k without injecting the foreign prime 3 = import;")
    print("      GU geometric quantities CAN carry 3, e.g. dim SO(3,1)=6, self-dual 2-forms=3 -- but")
    print("      those are external, not Cl(9,5) rep dimensions, and 3 is exactly what must be imported)")
    metric_sig = int(sum(int(np.sign((e128[a] @ e128[a])[0, 0].real)) for a in range(N)))
    print(f"  STRUCTURAL INPUT (not derived): metric signature tr(sign(e_a^2)) = {metric_sig} (= 9-5); "
          f"a degree-0 Dirac integer, but a declared input (the chosen (9,5) signature), and it is 4 not 3.")

    # =====================================================================================
    # PRONG 2 - degree-0 ratio sector: xi-independent invariants, any nontrivial integer?
    # =====================================================================================
    fro = lambda X: float(np.linalg.norm(X))

    def MD(xi):
        return np.kron(np.eye(N), sum(xi[a] * e128[a] for a in range(N)))

    def functionals(xi):
        M = MD(xi); Md = M.conj().T
        B = Gamma @ M @ Pi
        return {
            "|xi|": (1, float(np.linalg.norm(xi))),
            "C2": (1, fro(B)),
            "bare": (1, fro(Pi @ M - M @ Pi)),
            "fro_MD": (1, fro(M)),
            "fro_PiMPi": (1, fro(Pi @ M @ Pi)),
            "fro_QMQ": (1, fro(Q @ M @ Q)),
            "fro_E": (1, fro(Q @ M @ Pi)),
            "tr_MKT": (2, float(np.trace(B.conj().T @ B).real)),
            "tr_MdM": (2, float(np.trace(Md @ M).real)),
            "tr_PiMdMPi": (2, float(np.trace(Pi @ Md @ M @ Pi).real)),
        }

    def degree_ratios(fa):
        items = list(fa.items()); out = {}
        for i in range(len(items)):
            for j in range(len(items)):
                if i == j:
                    continue
                (na, (da, va)), (nb, (db, vb)) = items[i], items[j]
                if da == db and vb > 1e-9:
                    out[f"{na}/{nb}"] = va / vb
        return out

    rng = np.random.default_rng(7)
    xis = [gu_bridge.XI.real.astype(float)] + [rng.standard_normal(N) for _ in range(5)]
    ratio_vals = {}
    for xi in xis:
        for k, v in degree_ratios(functionals(xi)).items():
            ratio_vals.setdefault(k, []).append(v)

    invariants, nontrivial_ints, surds = [], [], []
    for k in sorted(ratio_vals):
        vals = np.array(ratio_vals[k]); m = vals.mean()
        rstd = vals.std() / (abs(m) + 1e-12)
        if rstd < 1e-6:                                   # xi-independent => genuine invariant
            is_int = abs(m - round(m)) < 1e-6
            invariants.append((k, m, is_int))
            if is_int and abs(m - 1.0) > 1e-6:
                nontrivial_ints.append((k, round(m)))
            rs = rational_square(m)
            if rs and not is_int:
                surds.append((k, m, rs))

    print(f"\n=== PRONG 2: degree-0 ratio sector ({len(invariants)} xi-independent invariants) ===")
    print("  sample Dirac-content invariants recognized as algebraic numbers (v^2 = p/q):")
    for k, m, (p, q) in surds[:10]:
        fp, fq = factorize(p), factorize(q)
        sp = " . ".join(f"{x}^{y}" if y > 1 else f"{x}" for x, y in sorted(fp.items())) or "1"
        sq = " . ".join(f"{x}^{y}" if y > 1 else f"{x}" for x, y in sorted(fq.items())) or "1"
        print(f"    {k:24} = {m:.6f} = sqrt({p}/{q})   [{sp} / {sq}]")
    print(f"\n  nontrivial INTEGER invariants in the RATIO sector (excluding trivial 1): "
          f"{nontrivial_ints if nontrivial_ints else 'NONE'}")
    print("  (broadening to rank/signature counts yields dimension integers like 1792, 832, ... -- all")
    print("   conjugation-invariant dimension counts, no Dirac content; see the SCOPE NOTE in the docstring)")
    IMPORTS = {24, -5376, 3, 16, -16, 8, 4}
    hits = [t for t in nontrivial_ints if t[1] in IMPORTS]
    print(f"  any RATIO invariant equals an import/target integer {sorted(IMPORTS)}? {hits if hits else 'none'}")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    integer_free = (len(nontrivial_ints) == 0)
    print("\n=== VERDICT ===")
    print(f"PRONG 1: prime 3 absent from Cl(9,5) dimension spectrum {sorted(all_primes)}?   {three_absent}")
    print(f"PRONG 2: degree-0 Dirac-content ratio sector is integer-free?                {integer_free}")
    print(f"         (ratio Dirac invariants are non-integer algebraics over primes {sorted(all_primes & {2,7,13})};")
    print(f"          the only integers anywhere are conjugation-invariant dimension/rank counts + tight-frame 1's,")
    print(f"          plus the declared structural input sig={metric_sig}; none is a DERIVED 3/4/8/24)")
    print(f"COMBINED: no honest scale-invariant integer with Dirac content in the bridge data: "
          f"{three_absent and integer_free}")
    print("Reading: even with CONSTRUCT-02's revived (soft-wall) index, the count '3' has no honest")
    print("home in the existing data -- the native integer DIMENSIONS are 3-free by prime spectrum, and")
    print("the only Dirac-content degree-0 invariants are non-integer surds/rationals (the prime 3 does")
    print("appear, but only in irrational DENOMINATORS like sqrt(7/24), never as an integer). So any")
    print("honest '3' must arise as a genuine EXTERNAL topological/families index over the Y14/K3")
    print("geometry; producing it from the rep alone is a target import.")
    print("EVIDENCE, not proof: bounded by this finite low-word-length catalog.")

    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"
    assert three_absent, "prime 3 unexpectedly present in dimension spectrum"
    assert integer_free, "a nontrivial integer appeared in the degree-0 Dirac ratio sector"
    assert not hits, "an invariant hit an import/target integer"

    return {
        "bare": bare, "C2": C2, "dimension_primes": sorted(all_primes),
        "three_absent": three_absent, "n_invariants": len(invariants),
        "nontrivial_integers": nontrivial_ints, "integer_free": integer_free,
        "import_hits": hits,
    }


if __name__ == "__main__":
    main()
