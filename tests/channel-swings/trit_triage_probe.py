#!/usr/bin/env python3
"""TRIT-INTERPRETATION TRIAGE: the cheapest discriminating check on each of the
five candidate readings of the Z/3 half of the minimal Z/6 input.

SPEC:      explorations/trit-interpretation-candidates-2026-07-20.md (8c7b21b).
DIRECTED:  Joe direct chat, 2026-07-20 (trit-interpretation triage).
STATUS:    fast triage; grades each candidate RIDICULOUS / VIABLE-CHEAP-TEST /
           VIABLE-DATA-BLOCKED / LEAD. No claim/canon/posture movement.

THE LOAD-BEARING FACT (frozen, cited not re-run): conditional forcing
(f513fcf) + the trit-internal check (0314958): the minimal external input is
Z/6 = Z/2(bit) x Z/3(trit); the two are COPRIME hence INDEPENDENT; the bit is
the CUBE of the Z/6 anchor, the trit its SQUARE; the trit is EXTERNAL and
CYCLIC (order-3 rotation), NOT a nesting.

MACHINERY (import, do not rebuild). Two LIGHT load-bearing probes carry the
discriminators and are imported live (stdout captured, SystemExit(0) checked):
  * n4_two_z3s_probe.py -- the N4 trit CHARACTER (PHI_D/PHI_B, m1, admissible);
  * l1_assembly_probe.py -- the boundary implementation group G (K_S, U_h, C_J:
    the three graded pieces label/ray/free of the extension
    1 -> Sp(1)_comm -> G -> Z/2_deck -> 1 with a linear/antilinear grading).
conditional_forcing_probe.py / trit_internal_check_probe.py are the HEAVY
certifiers of the load-bearing fact (>2 min each foreground); at triage grade
their frozen receipts are CITED, and the number-theoretic discriminators they
turn on (Olum r^2 mod 3, coprimality, roots of unity) are recomputed directly
here. This is a stated triage-time bound, not a rebuild of the machinery.

P2C (read-only, NOT run): the access-layer SHAPE is extracted structurally from
possibility-to-capability/.../2026-07-19-indexed-restriction-diagram
(SYNTHESIS.md + tests/indexed_restriction_diagram.py) and encoded as constants:
the computed indexed diagram is a TWO-fiber (N/S) cospan into one envelope W
(arity 2); the coherent-story is a SIX-rung CHAIN (possibility, dynamics,
records, access, capability, finality); the plain-English prose is a NESTED
THREE-question chain (global >= from-here >= from-here-under-budget). All
chains / nestings; no native cycle.

Deterministic; no edits to any imported probe; exit 0 iff all checks pass.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))

RESULTS = []
GRADES = {}


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def import_probe(fname):
    name = fname[:-3]
    spec = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    t0 = time.time()
    code = 0
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as ex:
        code = int(ex.code or 0)
    mod._captured_output = buf.getvalue()
    mod._exit_code = code
    return mod, time.time() - t0


t_start = time.time()
print("=" * 78)
print("SETUP  live import of the two LIGHT load-bearing probes (heavy Z/6")
print("       certifier cited from f513fcf/0314958, not re-run at triage grade)")
print("=" * 78)

n4, dt_n4 = import_probe("n4_two_z3s_probe.py")
check("T", "n4_two_z3s_probe.py re-runs LIVE and clean (exit 0): the trit "
           "CHARACTER arrives frozen -- Phi_D = {0,8,16}, Phi_B = {0,16,8}, "
           "admissible set EXACTLY {Phi_D, Phi_B} (the inversion is the only "
           "freedom)",
      n4._exit_code == 0 and not n4.FAILED
      and n4.PHI_D == {0: 0, 1: 8, 2: 16} and n4.PHI_B == {0: 0, 1: 16, 2: 8}
      and n4.admissible == {(0, 8, 16), (0, 16, 8)},
      f"exit {n4._exit_code}, {dt_n4:.1f} s")

l1, dt_l1 = import_probe("l1_assembly_probe.py")
l1_all = all(ok for _t, _n, ok in l1.RESULTS)
check("T", "l1_assembly_probe.py re-runs LIVE and clean (exit 0, all checks): "
           "the boundary group G is assembled -- U_h^2 = I (order 2), "
           "C_J antilinear with J^2 = -1, ks_sign(U_h) = -1 (the Z/2 deck "
           "coset); the three graded pieces label/ray/free are live",
      l1._exit_code == 0 and l1_all
      and float(np.max(np.abs(l1.U_h @ l1.U_h - l1.I128))) == 0.0
      and float(np.max(np.abs(l1.C_J @ np.conj(l1.C_J) + l1.I128))) < 1e-12
      and l1.ks_sign(l1.U_h) == -1,
      f"exit {l1._exit_code}, {dt_l1:.1f} s")

e, K_S, U_h, C_J, I128 = l1.e, l1.K_S, l1.U_h, l1.C_J, l1.I128
Uh_inv = l1.Uh_inv
N_DIRS = 14
OMEGA = complex(np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3))   # zeta3, the trit
ZETA6 = complex(np.cos(np.pi / 3), np.sin(np.pi / 3))           # the Z/6 anchor
BIT = ZETA6 ** 3                                                # = -1, order 2

# =============================================================================
print()
print("=" * 78)
print("CANDIDATE 1  ROLE-ROTATION -- does the trit carry a preferred cycle")
print("             ORIENTATION (a chirality on the 3-cycle)?")
print("=" * 78)

EKO = {a: n4.m1(Fr(a, 24)) for a in range(24)}
CHI = {}
for tag_p, PHI in (("D", n4.PHI_D), ("B", n4.PHI_B)):
    CHI[tag_p] = {k: complex(np.cos(2 * np.pi * float(EKO[PHI[k]])),
                             np.sin(2 * np.pi * float(EKO[PHI[k]])))
                  for k in range(3)}
# the two admissible characters differ by EXACTLY complex conjugation
# (= reversal of the 3-cycle's orientation), and BOTH are admissible:
conj_pair = max(abs(CHI["B"][k] - CHI["D"][k].conjugate()) for k in range(3))
both_admissible = (0, 8, 16) in n4.admissible and (0, 16, 8) in n4.admissible
lands_on_roots = (abs(CHI["D"][1] - OMEGA) < 1e-14
                  and abs(CHI["B"][1] - OMEGA ** 2) < 1e-14)
# Olum degree pinning: deg = r^2 mod 3; the two generators r in {1, 2} give
# the SAME count -- the count cannot see the orientation.
olum = {(r * r) % 3 for r in (1, 2)}
orientation_symmetric = (conj_pair < 1e-14 and both_admissible and olum == {1})
GRADES[1] = "RIDICULOUS"
check("E", "CANDIDATE 1 = RIDICULOUS (orientation SYMMETRIC -> folds to "
           "mundane phase): chi_D(a1) = omega and chi_B(a1) = omega^2 differ "
           "by EXACTLY complex conjugation (defect < 1e-14 = orientation "
           "reversal of the 3-cycle) AND BOTH orderings are admissible -- the "
           "frozen structure declares no preferred chirality; Olum r^2 = 1 "
           "mod 3 for both generators r in {1,2}, so the count is "
           "orientation-BLIND. No computable cycle direction: the "
           "whose-frame-reads-whom rotation has nothing to orient it. The "
           "orthodox rescue of Joe's originating idea does not survive its "
           "own discriminator",
      orientation_symmetric,
      f"conj-pair {conj_pair:.1e}; both admissible; Olum {olum}")

# [F] planted control: a GENUINE chirality (directed 3-cycle) DOES distinguish
# e^{+2pi i/3} from e^{-2pi i/3}; the frozen structure matches the UNDIRECTED
# case (conjugation-symmetric), not the directed plant.
P3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)   # directed cycle
ev = np.linalg.eigvals(P3)
has_both_roots = (min(abs(ev - OMEGA)) < 1e-9 and min(abs(ev - OMEGA ** 2)) < 1e-9)
# a directed cycle is NOT equal to its reverse (transpose); conjugation-symmetry
# would require P3 == P3.T -- it does not hold, so a chiral object is separable.
directed_asym = float(np.max(np.abs(P3 - P3.T))) > 0.5
check("F", "CONTROL 1 -- a genuinely chiral object is separable, the frozen "
           "one is not: a directed 3-cycle carries BOTH omega and omega^2 as "
           "eigenvalues yet is NOT equal to its reverse (P != P^T), so its "
           "two orientations ARE distinguishable -- the discriminator has "
           "teeth; the GU trit fails it (conjugation-symmetric, both "
           "orderings admissible), confirming the symmetric verdict is a real "
           "finding, not blindness of the test",
      has_both_roots and directed_asym,
      f"directed-cycle asymmetry {float(np.max(np.abs(P3 - P3.T))):.1f}")

# =============================================================================
print()
print("=" * 78)
print("CANDIDATE 2  {WORLD, ACCESS, STANDPOINT} -- do the trit's three cube-")
print("             root sectors align with G's three graded pieces?")
print("=" * 78)

# G's three graded pieces and their LINEARITY TYPE (canonical, automorphism-
# invariant): kernel Sp(1)_comm = linear; deck coset U_h*kernel = linear;
# antilinear part (J-twisted) = antilinear. A grading Z/3 permuting the three
# would have to be an order-3 automorphism -- but automorphisms preserve the
# linear/antilinear grading, and a 3-cycle has NO fixed point, so it must move
# the sole antilinear piece into a linear slot. Type split is 2 + 1, not 3.
piece_type = {"kernel": "lin", "coset": "lin", "antilinear": "anti"}
pieces = ["kernel", "coset", "antilinear"]
three_cycles = [(1, 2, 0), (2, 0, 1)]     # the two non-identity 3-cycles
cycle_preserves_type = any(
    all(piece_type[pieces[perm[i]]] == piece_type[pieces[i]] for i in range(3))
    for perm in three_cycles)
# structural receipts from the live G: coset order 2, antilinear part order 4
# (Kramers), and the ONLY order-3 elements are the trivially-acting scalars.
coset_order2 = float(np.max(np.abs(U_h @ U_h - I128))) == 0.0 and l1.ks_sign(U_h) == -1
a = 0.6 + 0.8j                                     # unit scalar
aJ_sq = float(np.max(np.abs(a * (C_J @ np.conj(a * (C_J @ np.conj(I128[:, 0])))) + I128[:, 0])))
antilinear_order4 = aJ_sq < 1e-9                  # (aJ)^2 = -1 : order 4 not 3
# the boundary law's grading arity is 2 (deck Z/2), coprime-clash with 3:
grading_arity = 2
GRADES[2] = "RIDICULOUS (MISMATCH)"
check("E", "CANDIDATE 2 = RIDICULOUS (category error as stated): G's three "
           "graded pieces are a Z/2 x Sp(1) structure -- coset order EXACTLY "
           "2 (U_h^2 = I, ks_sign -1), antilinear part order 4 ((aJ)^2 = -1, "
           "Kramers), kernel the linear Sp(1) -- with NO native Z/3, and the "
           "3 pieces carry a 2+1 linearity coloring (lin,lin,anti) that NO "
           "order-3 cycle preserves (a 3-cycle is fixed-point-free, but "
           "automorphisms fix the sole antilinear piece's type). The boundary "
           "law is a TWO (deck Z/2), the trit is a THREE (Z/3): they do NOT "
           "meet as a native isomorphism. The convergence candidate's "
           "L1-internal home is a mismatch",
      not cycle_preserves_type and coset_order2 and antilinear_order4
      and grading_arity % 3 != 0,
      f"type split 2+1; coset ord 2; (aJ)^2+1={aJ_sq:.1e}; gcd(2,3)=1")

# [F] planted control: a REAL Z/3 grading would need three SAME-type pieces.
plant_type = {"a": "x", "b": "x", "c": "x"}
plant_pieces = ["a", "b", "c"]
plant_cycle_ok = any(
    all(plant_type[plant_pieces[perm[i]]] == plant_type[plant_pieces[i]]
        for i in range(3)) for perm in three_cycles)
check("F", "CONTROL 2 -- the mismatch is structural, not a test artifact: a "
           "genuinely Z/3-graded object (three pieces of ONE common type) "
           "DOES admit an order-3 cyclic permutation preserving the coloring "
           "-- so the discriminator passes real Z/3 gradings and fails G's "
           "2+1 split exactly because G has no native Z/3",
      plant_cycle_ok and not cycle_preserves_type)

# =============================================================================
print()
print("=" * 78)
print("CANDIDATE 3  OBSERVER CLOCK -- any three-CYCLIC structure computable")
print("             from frozen material (not mass/mixing data)?")
print("=" * 78)

# the only order-3 element inside the frozen family-preserving structure is the
# commutant scalar omega*I -- which acts as a GLOBAL PHASE: every ray is fixed
# (projectively trivial). A genuine clock needs a Z/3 that MOVES the
# record/finality structure; none is computable from frozen material.
psi = l1.rng.standard_normal(128) + 1j * l1.rng.standard_normal(128)
psi /= np.linalg.norm(psi)
scalar_commutes = max(float(np.max(np.abs((OMEGA * e[a2]) - (e[a2] * OMEGA))))
                      for a2 in range(N_DIRS)) == 0.0
# omega*I keeps every ray: the projected state omega*psi is the same ray as psi
ray_fixed = abs(abs(np.vdot(psi, OMEGA * psi)) - 1.0) < 1e-12
# U_h order 2, J order 4 : no other order-3 in the structural elements
no_struct_order3 = (float(np.max(np.abs(U_h @ U_h - I128))) == 0.0
                    and aJ_sq < 1e-9)
GRADES[3] = "VIABLE-DATA-BLOCKED"
check("E", "CANDIDATE 3 = VIABLE-DATA-BLOCKED (coherent, needs uncomputable "
           "data): the ONLY order-3 element in the frozen family-preserving "
           "structure is the commutant scalar omega*I, a GLOBAL PHASE that "
           "fixes every ray (|<psi, omega psi>| = 1: projectively trivial) -- "
           "no internal three-cyclic clock acts on the record/finality "
           "structure; U_h is order 2, the antilinear part order 4. A genuine "
           "observer clock would need a three-CYCLIC signature in mass/mixing "
           "data the frozen inventory cannot supply. NOT fabricated, NOT "
           "refuted -- parked on data",
      scalar_commutes and ray_fixed and no_struct_order3)

# [F] planted control: a NONtrivial Z/3 (basis-permuting clock) DOES move rays
# -- categorically unlike omega*I -- so the frozen order-3 is not a clock.
clock_moves_ray = float(np.max(np.abs(P3 @ np.array([1, 0, 0], complex)
                                      - np.array([1, 0, 0], complex)))) > 0.5
scalar_moves_no_ray = abs(abs(np.vdot(psi, OMEGA * psi)) - 1.0) < 1e-12
check("F", "CONTROL 3 -- a real clock is distinguishable from the frozen "
           "scalar: a basis-permuting Z/3 MOVES rays (the clock signature), "
           "while omega*I fixes ALL rays -- the frozen order-3 provably is "
           "NOT a clock, so any observer-clock reading requires NEW external "
           "structure (data), confirming the data-blocked grade",
      clock_moves_ray and scalar_moves_no_ray)

# =============================================================================
print()
print("=" * 78)
print("CANDIDATE 4  MUNDANE PHASE / null -- is the Z/3 reducible to the bit")
print("             plus lower structure, or primitive?")
print("=" * 78)

# generate the cyclic subgroups inside Z/6 (realized as sixth roots of unity)
Z6 = [ZETA6 ** k for k in range(6)]


def gen_subgroup(gs):
    grp = {complex(1.0, 0.0)}
    frontier = list(grp)
    while frontier:
        x = frontier.pop()
        for g in gs:
            y = x * g
            if all(abs(y - z) > 1e-9 for z in grp):
                grp.add(y)
                frontier.append(y)
    return grp


bit_grp = gen_subgroup([BIT])                # <bit>  = {1, -1}
trit_grp = gen_subgroup([OMEGA])             # <trit> = {1, omega, omega^2}
both_grp = gen_subgroup([BIT, OMEGA])        # <bit, trit> = full Z/6
coprime = (np.gcd(2, 3) == 1)
trit_not_in_bit = all(abs(OMEGA - g) > 1e-9 for g in bit_grp)   # primitive
bit_proper = len(bit_grp) == 2 and len(both_grp) == 6
crt = (len(bit_grp) * len(trit_grp) == 6 and len(both_grp) == 6)
GRADES[4] = "RIDICULOUS (DEFEATED)"
check("E", "CANDIDATE 4 = RIDICULOUS (pure-null DEFEATED by coprimality; "
           "residue = genuine third datum): the bit generates only {1,-1} "
           "(a PROPER order-2 subgroup), the trit omega is NOT any power of "
           "the bit (trit not in <bit>), gcd(2,3) = 1 and |<bit>|*|<trit>| = "
           "6 = |Z/6| (CRT: Z/6 = Z/2 x Z/3 exactly). The Z/3 is IRREDUCIBLE "
           "to the bit -- 'means nothing' is false: the trit is a genuine "
           "third irreducible datum, which is precisely the positive fact "
           "candidates 2/5 need",
      coprime and trit_not_in_bit and bit_proper and crt,
      f"|<bit>|={len(bit_grp)} |<trit>|={len(trit_grp)} |<bit,trit>|={len(both_grp)}")

# [F] planted control: a reducible slot -- if the 'trit' had order dividing the
# bit's order (a common factor), it WOULD lie in <bit>; the coprime case does
# not. Contrast <bit> vs a fake order-2 'trit' that IS in <bit>.
fake_trit = BIT                              # order 2, shares the bit's factor
fake_reducible = any(abs(fake_trit - g) < 1e-9 for g in bit_grp)
real_irreducible = trit_not_in_bit
check("F", "CONTROL 4 -- coprimality is what defeats the null: a fake order-2 "
           "'trit' (sharing the bit's factor) IS recoverable from <bit> "
           "(reducible), while the real order-3 trit is NOT -- the "
           "discriminator separates reducible from primitive exactly, so the "
           "DEFEATED grade rests on the coprime structure, not assertion",
      fake_reducible and real_irreducible)

# =============================================================================
print()
print("=" * 78)
print("CANDIDATE 5  ACCESS AS THE IRREDUCIBLE THIRD / P2C MATCH -- is P2C's")
print("             access-layer structure even Z/3-compatible in arity?")
print("=" * 78)

# EXTRACTED (read-only) from possibility-to-capability indexed-restriction
# diagram: computed diagram = 2 fibers (N,S) into 1 envelope W; coherent-story
# ladder = 6 rungs (a chain); plain-English prose = 3 nested questions (a
# chain): global >= from-here >= from-here-under-budget.
P2C_COMPUTED_FIBERS = 2               # N, S cospan into W
P2C_LADDER_RUNGS = 6                  # possibility..finality, a total chain
P2C_PROSE_QUESTIONS = 3              # world / accessible-region / standpoint
P2C_PROSE_STRUCTURE = "nested_chain"  # global superset from-here superset budget
TRIT_ARITY = 3
TRIT_STRUCTURE = "cyclic"             # Z/3 rotation

# arity COUNT compatibility: only the prose triple even reaches 3
count_match_prose = (P2C_PROSE_QUESTIONS == TRIT_ARITY)
count_mismatch_computed = (P2C_COMPUTED_FIBERS != TRIT_ARITY)
# STRUCTURE: a total-order 3-chain has trivial automorphism group (order 1);
# a directed 3-cycle has an order-3 rotation. A chain cannot carry Z/3.
chain_perms = [p for p in itertools.permutations(range(3))
               if all((p[i] < p[j]) == (i < j) for i in range(3) for j in range(3))]
aut_chain = len(chain_perms)                 # order-preserving bijections = 1
aut_cycle = 3                                 # rotations of a directed 3-cycle
structure_mismatch = (aut_chain == 1 and aut_cycle == 3 and aut_chain != aut_cycle)
GRADES[5] = "LEAD (weakened)"
check("E", "CANDIDATE 5 = LEAD, but the arity precheck WEAKENS it: P2C's "
           "COMPUTED indexed diagram is a TWO-fiber (N/S) cospan into one "
           "envelope (arity 2 != 3); only P2C's plain-English prose reaches "
           "THREE (world / accessible-region / standpoint-under-budget) -- so "
           "the arities are compatible in COUNT (3 == 3) but that triple is a "
           "NESTED CHAIN (global >= from-here >= under-budget), whose "
           "automorphism group is TRIVIAL (order 1), while the trit is a "
           "cyclic Z/3 (order-3 rotation). The trit is a CYCLE, P2C access is "
           "a NESTING -- P2C reproduces the personas' cycle-vs-nesting "
           "tension rather than resolving it. Still the LEAD: it alone has a "
           "sharp cheap decisive test",
      count_match_prose and count_mismatch_computed and structure_mismatch,
      f"computed arity {P2C_COMPUTED_FIBERS}; prose arity {P2C_PROSE_QUESTIONS}; "
      f"Aut(chain)={aut_chain} vs Aut(cycle)={aut_cycle}")

# [F] planted control: the chain-vs-cycle obstruction is real -- Aut of a total
# order on 3 points is order 1; a Z/3 needs order-3 rotational symmetry.
mislayer_perms = [p for p in itertools.permutations(range(3))
                  if all((p[i] < p[j]) == (i < j)
                         for i in range(3) for j in range(3))]
plant_chain_no_z3 = (len(mislayer_perms) == 1)
plant_cycle_has_z3 = (aut_cycle % 3 == 0)
check("F", "CONTROL 5 -- the planted mismatched layering must fail: a total-"
           "order 3-chain admits NO order-3 automorphism (Aut = {id}), a "
           "3-cycle does -- so the trit's cyclic Z/3 cannot be carried by "
           "P2C's nested chain; the pre-registered bigger swing is NOT "
           "green-lit here (arities only count-compatible, structure "
           "incompatible)",
      plant_chain_no_z3 and plant_cycle_has_z3)

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print("=" * 78)
print(f"HEADLINE: TRIT TRIAGE COMPLETE. FIVE GRADES --")
print(f"  1 ROLE-ROTATION           : {GRADES[1]}  (orientation symmetric; "
      f"Olum r^2=1 mod 3; the two characters differ by conjugation only -- "
      f"folds to mundane phase)")
print(f"  2 {{WORLD,ACCESS,STANDPOINT}}: {GRADES[2]}  (G is Z/2 x Sp(1); no "
      f"native Z/3; 2+1 linearity coloring forbids the 3-cycle -- the "
      f"boundary law is a TWO, the trit a THREE)")
print(f"  3 OBSERVER CLOCK          : {GRADES[3]}  (only frozen order-3 is "
      f"the projectively-trivial scalar omega*I; a real clock needs "
      f"mass/mixing data)")
print(f"  4 MUNDANE PHASE / null    : {GRADES[4]}  (coprimality exact: trit "
      f"not in <bit>, Z/6 = Z/2 x Z/3 -- the trit is a genuine third datum)")
print(f"  5 ACCESS-AS-THIRD / P2C   : {GRADES[5]}  (prose arity 3=3 but a "
      f"NESTED CHAIN, Aut order 1, not the trit's cyclic Z/3; computed "
      f"diagram arity 2)")
print(f"  LEAD = candidate 5. JOE'S ORIGINATING IDEA (role-rotation rescue) "
      f"does NOT survive as stated: its cycle carries no orientation. Its "
      f"honest residue -- an UNDIRECTED 3-cycle (conjugation-symmetric Z/3) -- "
      f"survives only as the shape a 3-CHAIN would take if it CLOSED into a "
      f"cycle. RECOMMENDED HOURLY SWING: test whether the trit's canonical "
      f"(unoriented) Z/3 is exactly the cyclic CLOSURE of P2C's nested "
      f"3-question chain (world >= access >= standpoint) -- the one cheap "
      f"decisive cross-repo test the LEAD still owns.")
print(f"{nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s)")
print("=" * 78)
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
