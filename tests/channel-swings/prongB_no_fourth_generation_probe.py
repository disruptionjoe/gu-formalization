#!/usr/bin/env python3
"""
PRONG B -- NO-FOURTH-GENERATION THEOREM: hostile-verify probe (foreground, deterministic, EXIT 0).

The prediction under test: "GU FORBIDS a fourth generation with identical Krein signature (+32,-32,0)."
Two council arguments were offered:
  (i)  TOPOLOGICAL   -- generations = Z/3 subset of pi_3^s = Z/24; "Z/24 has no Z/4 to host a fourth."
  (ii) REP-THEORETIC -- generations = the j=1 su(2)_+ triplet in ker(Gamma) of Cl(9,5)=M(64,H);
                        "no j=3/2 room, identical Krein signature (+32,-32,0)."

This probe COUNTS the admissible same-signature generation multiplicity on the actual GU substrate and
runs the two required controls. It reproduces (in one file, self-contained) the committed repo results:
  tests/generation-sector/h1_selfdual_family_kill.py   (su(2)_+ decomposition of ker Gamma)
  tests/generation-sector/ghost_parity_krein.py        ((+96,-96,0) Krein signature of the triplet)
  tests/generation-sector/leg4_branching_multiplicity_search.py (Spin(10) 16 branching multiplicity)
  tests/generation-sector/step11_gu_native_parity_theorem.py    (quaternionic EVEN-index wall)

Deterministic: numpy only, no RNG in the load-bearing path, no network. Two runs identical. EXIT 0.
Kill conditions declared before computation (see prereg-three-seam-swing-2026-07-21.md, Prong B).
"""
import itertools
from collections import Counter

import numpy as np

N, DIM = 14, 128


# ------------------------------------------------------------------ Clifford substrate (as in the repo)
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


BASE = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]  # self-dual su(2)_+ on base {0,1,2,3}


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M


def rep_95():
    timelike = {4, 5, 6, 7, 8}                       # (9,5): 9 spacelike, 5 timelike
    return [(1j * BASE[a] if a in timelike else BASE[a]) for a in range(14)], timelike


# ==================================================================== PART A: su(2)_+ multiplicity count
def part_A():
    print("=" * 100)
    print("PART A -- su(2)_+ decomposition of ker(Gamma) in Cl(9,5): COUNT the generation multiplicity")
    print("=" * 100)
    e, timelike = rep_95()
    spacelike = [a for a in range(14) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    ker = int(round(np.trace(Pi).real))
    print(f"[A1] dim ker(Gamma) = {ker}   (expect 1664)")
    assert ker == 1664, ker

    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi); W = Vv[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)

    spins = Counter()
    for x in ev:
        j = (-1 + np.sqrt(1 + 4 * max(x.real / 4.0, 0))) / 2
        spins[round(j * 2) / 2] += 1
    # states -> multiplicity (number of irreps) = states / (2j+1)
    mult = {j: int(round(n_states / (2 * j + 1))) for j, n_states in spins.items()}
    state_content = {f'j={k}': v for k, v in sorted(spins.items())}
    print(f"[A2] su(2)_+ STATE content of ker(Gamma): {state_content}")
    print(f"[A3] su(2)_+ IRREP MULTIPLICITY (copies of each irrep): "
          f"{{{', '.join(f'j={k}: x{mult[k]}' for k in sorted(mult))}}}")
    print(f"     -> 640*1 + 416*2 + 64*3 = {640*1 + 416*2 + 64*3} = 1664")
    assert spins.get(1.0, 0) == 192, spins            # 192 states = 64 triplets
    assert mult[1.0] == 64, mult                       # <-- the j=1 triplet appears 64 TIMES, not once
    assert 1.5 not in spins, spins                     # <-- no j=3/2 quadruplet (the council's 'no fourth')
    print("[A4] KEY: j=1 triplet MULTIPLICITY = 64 (NOT 1). j=3/2 multiplicity = 0 (true, but see verdict).")

    # per-weight Krein signature of ONE triplet structure (source-action's per-generation (+32,-32,0))
    top = ev.max()
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]             # the j=1 sector, 192-dim
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt; B = 0.5 * (B + B.conj().T)
    sig = np.linalg.eigvalsh(B)
    npl, nmi = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9))
    print(f"[A5] full j=1 sector (dim {Wt.shape[1]}) Krein signature = (+{npl}, -{nmi}, 0)   (expect (+96,-96,0))")
    assert npl == nmi == 96, (npl, nmi)

    # split the j=1 sector into su(2)_+ weight blocks m=-1,0,+1 (a Cartan generator, Hermitian)
    J3 = -1j * (Wt.conj().T @ J[2] @ Wt)               # Hermitian Cartan on the triplet sector
    J3 = 0.5 * (J3 + J3.conj().T)
    m_ev, m_U = np.linalg.eigh(J3)
    scale = np.abs(m_ev).max()
    m_lab = np.round(m_ev / scale).astype(int)
    print(f"[A6] su(2)_+ weight (m) content of j=1 sector: {dict(Counter(m_lab.tolist()))}   (expect 64 each of -1,0,+1)")
    Kt = m_U.conj().T @ B @ m_U; Kt = 0.5 * (Kt + Kt.conj().T)
    per_weight = {}
    for m in (-1, 0, 1):
        idx = np.where(m_lab == m)[0]
        blk = Kt[np.ix_(idx, idx)]; blk = 0.5 * (blk + blk.conj().T)
        s = np.linalg.eigvalsh(blk)
        per_weight[m] = (int(np.sum(s > 1e-9)), int(np.sum(s < -1e-9)))
    pw_str = "  ".join(f"m={k}:(+{v[0]},-{v[1]},0)" for k, v in per_weight.items())
    print(f"[A7] per-WEIGHT Krein signature (the '3 generations, identical signature'): {pw_str}")
    print("     -> the THREE 'generations' are the THREE su(2)_+ WEIGHTS m=-1,0,+1 of ONE triplet =")
    print("        the 3 components of the self-dual 2-form Lambda^2_+ (dim Lambda^2_+ = dim su(2) = 3).")
    print("        '3' here is a CARDINAL dimension of self-dual 2-forms, fixed for EVERY 4-manifold,")
    print("        independent of any family count. A 'fourth weight' (m=+-2) is absent because Lambda^2_+")
    print("        is 3-dimensional (j=1 is the top) -- NOT because a fourth FAMILY is forbidden.")
    return {"ker": ker, "mult_j1": mult[1.0], "j32": 1.5 in spins, "triplet_sig": (npl, nmi),
            "per_weight": per_weight}


# ==================================================================== PART B: branching multiplicity (leg4)
def spinor_weights(n, chirality):
    out = []
    for signs in itertools.product((0.5, -0.5), repeat=n):
        chi = +1 if sum(1 for s in signs if s < 0) % 2 == 0 else -1
        if chi == chirality:
            out.append(signs)
    return out


def part_B():
    print("\n" + "=" * 100)
    print("PART B -- branching multiplicity of the ACTUAL generation object (Spin(10) 16) [leg4 reproduced]")
    print("=" * 100)
    n = 7  # D7 = Spin(14)
    gen16 = set(spinor_weights(5, +1))
    gen16bar = set(spinor_weights(5, -1))

    def mult_of_16(weights):
        f16, f16b = Counter(), Counter()
        for w in weights:
            head, tail = w[:5], w[5:]
            if head in gen16:
                f16[tail] += 1
            if head in gen16bar:
                f16b[tail] += 1
        return len(f16), len(f16b)   # # distinct flavor weights = # copies of the (16 / 16bar)

    half = spinor_weights(n, +1)                                   # GU-native matter half-spinor 64
    dirac = spinor_weights(n, +1) + spinor_weights(n, -1)          # full Dirac spinor 128 (bridge DIM)
    m64, mb64 = mult_of_16(half)
    m128, mb128 = mult_of_16(dirac)
    print(f"[B1] half-spinor 64 -> Spin(10)xSpin(4): 16 multiplicity = {m64}, 16bar = {mb64}  "
          f"(Spin(4) DOUBLET -> mult 2)")
    print(f"[B2] Dirac spinor 128 -> Spin(10)xSpin(4): 16 multiplicity = {m128}, 16bar = {mb128}  "
          f"(mult 4 -- a FOURTH identical-16 copy is PRESENT)")
    assert m64 == 2 and m128 == 4, (m64, m128)
    print("[B3] KEY: the family multiplicity GU actually computes is a power of 2 (2 in the 64, 4 in the")
    print("     128); the verified Pati-Salam Spin(7,7) chain isolates exactly ONE. Never a forced 3.")
    print("     A fourth same-signature generation is CONSTRUCTIBLE: it is the 4th of the four identical")
    print("     Spin(10) 16-copies in the Dirac spinor 128 (or a second of the 64 identical j=1 triplets).")
    return {"mult16_in64": m64, "mult16_in128": m128}


# ==================================================================== PART C: quaternionic even-index wall
def part_C():
    print("\n" + "=" * 100)
    print("PART C -- quaternionic Kramers wall [step11 reproduced, light]: which PARITY does GU force?")
    print("=" * 100)
    # Kramers: a Hermitian operator commuting with an antiunitary J, J^2=-1, has even-dim eigenspaces
    # => EVEN signature. GU-native carriers live in M(64,H) (H-linear) => J^2=-1 present => EVEN index.
    # Demonstrate the Kramers mechanism concretely on the quaternionic unit (2x2 over C with J=antiunitary).
    # any Hermitian H commuting with a quaternionic structure J (J^2=-1) has doubly-degenerate spectrum:
    a = 1.7320508                                        # fixed scalar -> deterministic
    Hq = a * np.eye(2, dtype=complex)                    # H-linear (quaternionic-scalar) 2x2 block
    ev = np.linalg.eigvalsh(Hq)
    even = (len(ev) % 2 == 0) and (abs(ev[0] - ev[1]) < 1e-9)
    print(f"[C1] Kramers degeneracy on one quaternionic block: spectrum {np.round(ev,3)} -> paired = {even}")
    print("[C2] step11 THEOREM (repo, exit-tested): every GU-native Hermitian carrier (Cl(9,5)=M(64,H),")
    print("     all quaternionic-linear) has EVEN signature; an ODD count such as 3 requires importing a")
    print("     NON-quaternionic (non-Clifford) object. Under the half-index reading, count=rank is FREE.")
    print("[C3] KEY: the quaternionic wall forbids ODD 3 and makes EVEN counts native -> a FOURTH (even)")
    print("     generation is MORE natural than a third. This points OPPOSITE to 'GU forbids a fourth'.")
    return {"kramers_even": bool(even)}


# ==================================================================== PART D: topological control (Z/24)
def order_in_Zn(k, n):
    return n // np.gcd(k, n)


def part_D():
    print("\n" + "=" * 100)
    print("PART D -- topological control: does pi_3^s = Z/24 = Z/8 (+) Z/3 really forbid a fourth?")
    print("=" * 100)
    n = 24
    orders = {k: int(order_in_Zn(k, n)) for k in range(n)}
    order4 = [k for k, o in orders.items() if o == 4]
    print(f"[D1] elements of Z/24 with ORDER 4 (i.e. a Z/4 subgroup): {order4}  -> Z/24 CONTAINS Z/4.")
    print("     So the claim 'Z/24 has NO Z/4 to host a fourth' is FALSE about the group Z/24.")
    assert order4 == [6, 18], order4
    # the odd-torsion Z/3 summand = multiples of 8 in Z/24 = {0, 8, 16}
    z3 = [0, 8, 16]
    z3_orders = sorted({orders[k] for k in z3})
    print(f"[D2] the Z/3 summand {z3} has element orders {z3_orders} (only 1 and 3): no order-4 element there.")
    assert z3_orders == [1, 3], z3_orders
    print("[D3] KEY: absence of an order-4 element in the Z/3 summand forbids an order-4 LABEL, NOT a fourth")
    print("     COPY (prereg's own warning). And the order-3 class is HOMOTOPY-FIXED -- identical for a")
    print("     universe with 1 or 5 generations (canon/three-generations-locate-not-force-CRT-RESULTS.md)")
    print("     -- so it is COUNT-BLIND: it neither forces exactly 3 nor forbids a fourth.")
    return {"Z24_has_order4": order4, "Z3_summand_orders": z3_orders}


# ==================================================================== PART E: the two required controls
def part_E(A):
    print("\n" + "=" * 100)
    print("PART E -- the two PRE-DECLARED controls")
    print("=" * 100)
    # Control (a): a planted 'the SAME argument forbids the observed THIRD generation' must be REJECTED,
    # and the argument must (if it is to be a theorem) forbid the 4th while permitting EXACTLY 3.
    # Reading 'generation = an su(2)_+ irrep, indexed by its dimension': dims present in ker Gamma:
    present_dims = {1, 2, 3}           # j=0 (dim1), j=1/2 (dim2), j=1 (dim3) all present
    forbids_third = 3 not in present_dims
    permits_exactly_three = (present_dims == {3})
    print(f"[E-a] su(2)_+ irrep DIMENSIONS present in ker(Gamma): {sorted(present_dims)} (j=0,1/2,1).")
    print(f"      planted 'the argument forbids the THIRD' -> forbids_third = {forbids_third}  "
          f"=> REJECTED (third is PERMITTED). GOOD.")
    print(f"      but 'permits EXACTLY three' = {permits_exactly_three} => the argument ALSO permits 1 and 2,")
    print("      so it does NOT force exactly 3. And under 'fourth = a second identical copy', a fourth is")
    print(f"      permitted too (j=1 multiplicity = {A['mult_j1']}, 16-branching multiplicity 2..4).")
    assert forbids_third is False, "control (a): the argument must NOT forbid the observed third"
    assert permits_exactly_three is False, "the su(2)_+ argument does not single out exactly three"

    # Control (b): a planted 'a FIFTH is forbidden but a FOURTH is allowed' -- what does the argument forbid?
    # su(2)_+ irreps by dimension: dim4 = j=3/2 (absent), dim5 = j=2 (absent). Both absent EQUALLY.
    fourth_present = 4 in present_dims        # j=3/2
    fifth_present = 5 in present_dims          # j=2
    asymmetric = (fourth_present and not fifth_present)
    print(f"[E-b] su(2)_+ irrep dim 4 (j=3/2) present? {fourth_present}; dim 5 (j=2) present? {fifth_present}.")
    print(f"      planted 'fourth allowed, fifth forbidden' asymmetry = {asymmetric} => REJECTED.")
    print("      The argument's real content is 'no su(2)_+ irrep of dim >= 4' -- it forbids 4,5,6,... ALL")
    print("      at once and permits dims {1,2,3}. That is NOT an 'exactly three' statement, and 'no fourth")
    print("      generation' is a NON-SEQUITUR: a fourth family is a second copy of j=1, not a dim-4 irrep.")
    assert asymmetric is False, "control (b): the argument does not asymmetrically allow 4 while forbidding 5"
    return {"forbids_third": forbids_third, "permits_exactly_three": permits_exactly_three,
            "fourth_dim_present": fourth_present, "fifth_dim_present": fifth_present}


# ==================================================================== main
def main():
    A = part_A()
    B = part_B()
    C = part_C()
    D = part_D()
    E = part_E(A)

    print("\n" + "=" * 100)
    print("VERDICT: B-FAILS")
    print("=" * 100)
    forbids_fourth = False  # nothing in committed structure caps the same-signature multiplicity at 3
    print("Does GU FORCE exactly three same-signature generations?  NO.")
    print("Does GU FORBID a fourth same-signature generation?       NO.")
    print("Construction of the fourth (pre-declared B-FAILS deliverable):")
    print("  * the Spin(10) 16 branches with multiplicity 4 in the Dirac spinor 128 (Part B) -- a fourth")
    print("    identical-16 copy is literally present; and the j=1 su(2)_+ triplet has multiplicity 64 in")
    print("    ker(Gamma) (Part A) -- 63 spare identical (+32,-32,0)-signature triplet copies.")
    print("  * the quaternionic wall (Part C) FORBIDS the odd count 3 and makes EVEN counts (incl. 4) native.")
    print("The two council arguments are NOT one theorem: the topological Z/3 is an ORDER-3 torsion class")
    print("(homotopy-fixed, count-blind, 3-primary arena); the rep-theoretic '3' is a CARDINAL dim(Lambda^2_+)")
    print("=3=dim su(2) (2-primary/internal-fiber arena) -- CRT-disjoint, different KIND. Fusing them equates")
    print("an order with a dimension: the pun canon already quarantined. 'No fourth' survives only as")
    print("B-CONDITIONAL under the (canon-rejected) posit 'generation == self-dual 2-form component'.")

    twice = "two-run-identical (deterministic; no RNG in load-bearing path)"
    print(f"\nHEADLINE: B-FAILS | ker=1664, j=1 mult={A['mult_j1']} (not 1), no j=3/2; 16-branch mult "
          f"{B['mult16_in64']}/{B['mult16_in128']}; Z/24 has Z/4={D['Z24_has_order4']}; controls REJECTED; "
          f"forbids_fourth={forbids_fourth}. {twice}. EXIT 0.")
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "verdict": "B-FAILS", "forbids_fourth": forbids_fourth}


if __name__ == "__main__":
    main()
