# -*- coding: utf-8 -*-
"""
REFEREE verification of LEG-A2 (corner (a), leg 2: massless-limit bookkeeping).

Independent machinery, per the referee protocol:
  - The leg used SU(2)xSU(2) weight arithmetic + sympy symbolics.
  - This referee uses EXPLICIT CLIFFORD GAMMA MATRICES (Pauli tensor
    construction) for Spin(10) and Spin(4), with invariant-subspace counts by
    numerical rank (entries in {0, +-1, +-i, +-1/2...}; rank gaps are huge and
    unambiguous), plus numpy numerics at exact integer points for the toys,
    plus Fractions for the index table, plus verbatim needles on BOTH
    primaries (transcript AND the in-repo GU draft PDF, which the leg never
    opened).

Referee findings verified here:
  (R1) The leg's rep primitives are CORRECT (trace maps flip the respective
       chirality; 10x16 = 144 + 16bar; dims close).
  (R2) But the leg's CENSUS CONTENT Omega^0(S14+) + Omega^1(S14+) (same Weyl
       half) is stated by NEITHER primary. The transcript's only explicit
       chirality declaration (L107) is Omega^0(S+) (+) Omega^1(S-); the GU
       draft (p63 item iii) declares full NON-chiral Dirac content whose
       emergent luminous half (draft eq 11.6 + p50 diagram) is exactly the
       L107 mixed-half content.
  (R3) Under the STATED content the census is: three spin-1/2 16-families ALL
       in the SAME internal 16 (net +3, genuinely chiral), spin-3/2 family in
       the CONJUGATE 16bar -- reproducing [00:40:27] "conjugate of the
       internal symmetry representation" and the draft's "right handed matter
       and left handed anti-matter" reversal, which the leg's census CANNOT
       reproduce (its spin-3/2 sits in 16, same as its Omega^0 family; its
       three families carry mixed 16/16bar with no common rep).
  (R4) 16 (x) 16 of Spin(10) contains NO singlet; 16 (x) 16bar contains
       EXACTLY ONE. Hence within the luminous chiral half the spin-3/2 (and
       the families) have NO bare mass channel: every mass is VEV-borne, and
       the only Dirac channel is the inter-sector (gen<->mirror) one that the
       draft's eq 12.12 puts under the SINGLE VEV Lambda. The leg's "heavy
       two-thirds stay at VEV-independent M" has no stated-mechanism support.
  (R5) The chirality PAIRING (4d chirality locked to internal chirality inside
       each 14d Weyl half) is STRUCTURAL: the 14d chirality operator factors
       as gamma5 (x) Gamma11 (verified on explicit 128-dim gammas). The leg's
       corner-open strand treated pairing as an unbuilt "IF".
  (R6) The leg's toy spectra and index table are arithmetically CORRECT
       (re-verified numerically / with Fractions).
  (R7) Multiplicity claims (exactly 3 spin-1/2 family slots + exactly 1
       spin-3/2 slot per half) HOLD in every reading -- that part survives,
       and the draft's p50 diagram states it directly.

Exit 0 == all referee checks pass.
"""

import sys
import re
from fractions import Fraction

import numpy as np

N = 0


def check(name, cond):
    global N
    if not cond:
        print(f"[REFEREE FAIL] {name}")
        sys.exit(1)
    N += 1
    print(f"[ok] {name}")


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def rank(A, tol=1e-8):
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    r = int((s > tol * max(A.shape) * (s[0] if s.size else 1)).sum())
    # demand a clean gap (exactness surrogate)
    if r < s.size:
        assert s[r] < 1e-6 * (s[0] + 1e-300), "ambiguous rank -- refuse"
    return r


print("=" * 78)
print("R-S1: explicit Spin(10) Clifford algebra (32x32 Pauli-tensor gammas)")
print("=" * 78)

G10 = []
pre = []
for k in range(5):
    G10.append(kron(*(pre + [X] + [I2] * (4 - k))))
    G10.append(kron(*(pre + [Y] + [I2] * (4 - k))))
    pre.append(Z)
check("Clifford relations {Ga,Gb} = 2 delta (all 55 pairs)",
      all(np.allclose(G10[a] @ G10[b] + G10[b] @ G10[a],
                      (2.0 if a == b else 0.0) * np.eye(32))
          for a in range(10) for b in range(10)))

G11 = G10[0]
for g in G10[1:]:
    G11 = G11 @ g
# normalize chirality so G11c^2 = 1, hermitian
phase = np.trace(G11 @ G11) / 32
G11c = G11 / np.sqrt(phase)
check("chirality Gamma11: Gamma11^2 = 1, traceless, commutes w/ generators",
      np.allclose(G11c @ G11c, np.eye(32)) and abs(np.trace(G11c)) < 1e-9)

evals, evecs = np.linalg.eigh(G11c.real @ np.eye(32))  # G11c is real diag +-1 here
Splus = evecs[:, evals > 0.5]     # 32 x 16
Sminus = evecs[:, evals < -0.5]   # 32 x 16
check("S+ and S- are each 16-dimensional", Splus.shape[1] == 16 and Sminus.shape[1] == 16)

Sig10 = [(G10[a] @ G10[b] - G10[b] @ G10[a]) / 4.0
         for a in range(10) for b in range(a + 1, 10)]
check("45 so(10) generators built; all commute with Gamma11 (chirality preserved)",
      len(Sig10) == 45 and all(np.allclose(S @ G11c, G11c @ S) for S in Sig10))

# Clifford contraction c10: V10 (x) S+ -> full spinor space; must land in S-.
# columns indexed by (a, j): Ga . (S+ e_j)
Cmap = np.hstack([G10[a] @ Splus for a in range(10)])          # 32 x 160
check("Clifford contraction of V10 (x) S+ lands ENTIRELY in S- (chirality flip)",
      np.allclose(Splus.conj().T @ Cmap, 0))
r10 = rank(Sminus.conj().T @ Cmap)
check("trace map V10 (x) S+ ->> S- is SURJECTIVE (rank 16) => 10x16 = 144 + 16bar,"
      " with the trace part in the OPPOSITE chirality [leg primitive CONFIRMED]",
      r10 == 16 and 10 * 16 - r10 == 144)

# ---- invariant (singlet) counts: the mass-channel arithmetic the leg omitted
def su_action_on_product(gens, B1, B2):
    """Stack rho(S) (x) 1 + 1 (x) rho(S) on span(B1) (x) span(B2)."""
    rows = []
    d1, d2 = B1.shape[1], B2.shape[1]
    for S in gens:
        r1 = B1.conj().T @ S @ B1
        r2 = B2.conj().T @ S @ B2
        rows.append(np.kron(r1, np.eye(d2)) + np.kron(np.eye(d1), r2))
    return np.vstack(rows), d1 * d2


A_pp, d_pp = su_action_on_product(Sig10, Splus, Splus)
A_pm, d_pm = su_action_on_product(Sig10, Splus, Sminus)
n_sing_pp = d_pp - rank(A_pp)
n_sing_pm = d_pm - rank(A_pm)
check("Spin(10): 16 (x) 16 contains NO singlet (computed: 0) "
      "=> NO bare mass term inside one internal chirality", n_sing_pp == 0)
check("Spin(10): 16 (x) 16bar contains EXACTLY ONE singlet (computed: 1) "
      "=> the ONLY Dirac mass channel is gen<->mirror (inter-sector)", n_sing_pm == 1)

print()
print("=" * 78)
print("R-S2: explicit Spin(4) side (4x4 gammas) -- the 4d trace-flip primitive")
print("=" * 78)
G4 = [kron(X, I2), kron(Y, I2), kron(Z, X), kron(Z, Y)]
check("4d Clifford relations",
      all(np.allclose(G4[a] @ G4[b] + G4[b] @ G4[a],
                      (2.0 if a == b else 0.0) * np.eye(4))
          for a in range(4) for b in range(4)))
g5 = G4[0] @ G4[1] @ G4[2] @ G4[3]
ph = np.trace(g5 @ g5) / 4
g5c = g5 / np.sqrt(ph)
ev4, evc4 = np.linalg.eigh((g5c + g5c.conj().T).real / 2)
S4L = evc4[:, ev4 > 0.5]
S4R = evc4[:, ev4 < -0.5]
Sig4 = [(G4[a] @ G4[b] - G4[b] @ G4[a]) / 4.0
        for a in range(4) for b in range(a + 1, 4)]
C4 = np.hstack([G4[a] @ S4L for a in range(4)])   # V4 (x) S4L, 4 x 8
check("V4 (x) S4L trace part lands entirely in S4R (4d chirality FLIP) and the "
      "trace map is surjective: 4x2 = 6 + 2 [leg primitive CONFIRMED]",
      np.allclose(S4L.conj().T @ C4, 0) and rank(S4R.conj().T @ C4) == 2)

# RS4L = kernel of the trace map inside V4 (x) S4L (the (1,1/2), dim 6)
M4 = S4R.conj().T @ C4                       # 2 x 8
_, s4, Vh4 = np.linalg.svd(M4)
RS4L_basis = Vh4[2:, :].conj().T             # 8 x 6 kernel basis
check("RS4L kernel dim = 6 (the (1,1/2))", RS4L_basis.shape[1] == 6)

# Lorentz-singlet counts (mass bilinears), via generators acting on V4 (x) S4L:
Sig4_on_VS = [np.kron(np.zeros((4, 4)), np.eye(2)) for _ in range(6)]
# generator action on V4: (Sab)_cd = delta_ac g_bd - delta_ad g_bc ... build directly:
V4gens = []
for (a, b) in [(i, j) for i in range(4) for j in range(i + 1, 4)]:
    Mv = np.zeros((4, 4))
    Mv[a, b] = 1.0
    Mv[b, a] = -1.0
    V4gens.append(Mv)
S4Lgens = [S4L.conj().T @ S @ S4L for S in Sig4]
VSgens = [np.kron(V4gens[i], np.eye(2)) + np.kron(np.eye(4), S4Lgens[i])
          for i in range(6)]
RSgens = [RS4L_basis.conj().T @ Gv @ RS4L_basis for Gv in VSgens]


def singlets(gens, d1gens, d2gens=None):
    if d2gens is None:
        d2gens = d1gens
    d1 = d1gens[0].shape[0]
    d2 = d2gens[0].shape[0]
    rows = [np.kron(d1gens[i], np.eye(d2)) + np.kron(np.eye(d1), d2gens[i])
            for i in range(len(d1gens))]
    A = np.vstack(rows)
    return d1 * d2 - rank(A)


n_RSRS = singlets(None, RSgens)
n_RSS = singlets(None, RSgens, [S4Lgens[i] for i in range(6)])
n_SS = singlets(None, S4Lgens)
check("Lorentz singlets: (1,1/2)x(1,1/2) has EXACTLY 1; (1,1/2)x(1/2,0) has 0; "
      "(1/2,0)x(1/2,0) has 1  [so a spin-3/2 mass bilinear exists Lorentz-wise "
      "ONLY with itself/its mirror, never with a spin-1/2 family]",
      n_RSRS == 1 and n_RSS == 0 and n_SS == 1)

check("REFEREE R4 ASSEMBLED: luminous spin-3/2 in 16bar has NO bare mass "
      "(Lorentz channel exists (1) x internal 16bar-16bar singlet (0) = 0); "
      "its ONLY Dirac channel is with the mirror Q in 16 (1 x 1 = 1) -- the "
      "inter-sector VEV-borne coupling of draft eq (12.12)",
      n_RSRS * n_sing_pp == 0 and n_RSRS * n_sing_pm == 1)

print()
print("=" * 78)
print("R-S3: the 14d Weyl condition PAIRS 4d and internal chirality (structural)")
print("=" * 78)
# 14d gammas on 4 (x) 32 = 128: Gmu = g_mu (x) 1 (mu<4), G_{4+a} = g5 (x) G_a
G14 = [np.kron(G4[m], np.eye(32)) for m in range(4)] + \
      [np.kron(g5c, G10[a]) for a in range(10)]
check("14d Clifford relations (all 105 pairs)",
      all(np.allclose(G14[a] @ G14[b] + G14[b] @ G14[a],
                      (2.0 if a == b else 0.0) * np.eye(128))
          for a in range(14) for b in range(14)))
Gtot = G14[0]
for g in G14[1:]:
    Gtot = Gtot @ g
pht = np.trace(Gtot @ Gtot) / 128
Gtotc = Gtot / np.sqrt(pht)
check("14d chirality operator FACTORS: Gamma_14d = +- g5 (x) Gamma11 exactly "
      "=> inside S14+ the 4d chirality DETERMINES the internal chirality "
      "(the chirality pairing is STRUCTURAL, not an unbuilt 'IF')",
      np.allclose(Gtotc, np.kron(g5c, G11c)) or
      np.allclose(Gtotc, -np.kron(g5c, G11c)))

print()
print("=" * 78)
print("R-S4: the census, on the three candidate field contents")
print("=" * 78)
# Bookkeeping over labeled slots, using ONLY the verified primitives:
#  - inside S14+: (4dL, 16) and (4dR, 16bar); inside S14-: (4dL, 16bar), (4dR, 16)
#    [R-S3: pairing structural; '16'/'16bar' = the two internal Weyl halves]
#  - V4-trace flips the 4d factor's chirality [R-S2]
#  - V10-trace flips the internal factor's chirality [R-S1]
#  - a slot's Weyl-UNIT label = its 4dL piece's internal rep (CPT: 4dR piece
#    always carries the conjugate -- holds slot-by-slot below)
CONJ = {"16": "16bar", "16bar": "16", "144": "144bar", "144bar": "144"}


def census(one_form_half):
    """Return family units for Omega^0(S14+) + Omega^1(S14 one_form_half)."""
    # S14+ = (4dL,16) + (4dR,16bar);  S14- = (4dL,16bar) + (4dR,16)
    S = {"+": [("L", "16"), ("R", "16bar")],
         "-": [("L", "16bar"), ("R", "16")]}
    units = []
    # Omega^0(S14+): unit = internal rep of its 4dL piece
    units.append(("Omega0", "1/2", "16"))
    src = S[one_form_half]
    # 4d-trace slot of V4 (x) S14(half): 4d chirality flipped, internal kept
    tr4 = [("R" if c == "L" else "L", r) for (c, r) in src]
    rep4 = [r for (c, r) in tr4 if c == "L"][0]
    units.append(("4d-trace", "1/2", rep4))
    # internal-trace slot of V10 (x) S14(half): internal flipped, 4d kept
    tr10 = [(c, CONJ[r]) for (c, r) in src]
    rep10 = [r for (c, r) in tr10 if c == "L"][0]
    units.append(("int-trace", "1/2", rep10))
    # spin-3/2 slot: 4d factor -> (1,1/2)-type (chirality kept), internal kept
    rep32 = [r for (c, r) in src if c == "L"][0]
    units.append(("RS4-slot", "3/2", rep32))
    # dark slot: internal -> 144-type of the flipped... internal RS part keeps
    # internal chirality (kernel of the trace), 4d kept:
    repD = "144" if [r for (c, r) in src if c == "L"][0] == "16" else "144bar"
    units.append(("dark", "1/2", repD))
    return units


legA = census("+")   # the leg's content: Omega^1(S14+)  (same half)
legB = census("-")   # transcript L107 content: Omega^1(S14-)

flux = lambda rep: +1 if rep == "16" else (-1 if rep == "16bar" else 0)

famsA = [u for u in legA if u[1] == "1/2" and u[2] in ("16", "16bar")]
famsB = [u for u in legB if u[1] == "1/2" and u[2] in ("16", "16bar")]
q32A = [u for u in legA if u[1] == "3/2"][0]
q32B = [u for u in legB if u[1] == "3/2"][0]

check("MULTIPLICITY (leg claim SURVIVES): both contents give exactly 3 spin-1/2 "
      "16-family units + exactly 1 spin-3/2 unit",
      len(famsA) == 3 and len(famsB) == 3)

# --- the leg's census (A), reproduced, then shown to contradict the primaries
check("leg census (A) reproduced: families in (16, 16bar, 16bar), net -1; "
      "spin-3/2 in 16",
      sorted(u[2] for u in famsA) == ["16", "16bar", "16bar"]
      and sum(flux(u[2]) for u in famsA) == -1 and q32A[2] == "16")
common_rep_A = len(set(u[2] for u in famsA)) == 1
check("REFEREE R3a: in the leg's census the three families have NO COMMON "
      "internal rep and the spin-3/2 (16) is NOT the conjugate of any common "
      "family rep -- [00:40:27] 'conjugate of the internal symmetry "
      "representation' is UNREPRODUCIBLE in the leg's own census",
      (not common_rep_A) and q32A[2] == "16")
check("REFEREE R3b: in the leg's census the 'imposter' (int-trace, 16bar) has "
      "CONJUGATE quantum numbers to the Omega0 family (16) -- contradicting "
      "the transcript's 'at low energy, it'll look the same as the other two' "
      "and the draft's 'merely effectively identical'",
      [u for u in legA if u[0] == "int-trace"][0][2] ==
      CONJ[[u for u in legA if u[0] == "Omega0"][0][2]])

# --- the stated census (B): transcript L107 = draft's luminous half
check("STATED census (B): ALL THREE families in the SAME internal 16, net +3 "
      "(genuinely chiral effective sector: 'exactly three families of chiral "
      "fermions' as NET, which the leg's census cannot produce)",
      all(u[2] == "16" for u in famsB) and sum(flux(u[2]) for u in famsB) == 3)
check("STATED census (B): spin-3/2 unit in 16bar = THE CONJUGATE of the common "
      "family rep  [00:40:27 REPRODUCED EXACTLY: 'aside from being spin three "
      "halves is just the conjugate of the internal symmetry representation'; "
      "draft p51: 'right handed matter and left handed anti-matter' reversal]",
      q32B[2] == CONJ[famsB[0][2]])
check("STATED census (B): imposter (int-trace) has THE SAME internal rep as "
      "the other two families (looks the same at low energy) -- the '2+1' is "
      "an ORIGIN split (the ADDED product-rule term), not internal conjugation",
      [u for u in legB if u[0] == "int-trace"][0][2] ==
      [u for u in legB if u[0] == "Omega0"][0][2])
check("draft total content (C) = (B) + conj(B): net flux 0 (fundamentally "
      "non-chiral -- capstone vectorlike matches HERE, at the total level, "
      "not at the leg's per-half level)",
      sum(flux(u[2]) for u in famsB) + sum(flux(CONJ[u[2]]) for u in famsB) == 0)
check("net-flux CORRECTION: stated luminous half nets +3 (families) and -1 "
      "(spin-3/2 channel); the leg's published 'net -1 per Weyl half' describes "
      "a content stated by NEITHER primary",
      sum(flux(u[2]) for u in famsB) == 3 and flux(q32B[2]) == -1
      and sum(flux(u[2]) for u in famsA) == -1)

print()
print("=" * 78)
print("R-S5: toy spectra re-verified NUMERICALLY (numpy, exact integer points)")
print("=" * 78)
M0, v0 = 7.0, 3.0
Jz = np.diag([1.0, 0.0, -1.0])
Jx = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / np.sqrt(2)
H1 = np.block([[M0 * Jz, v0 * np.eye(3)], [v0 * np.eye(3), M0 * Jz]])
ev = np.sort(np.linalg.eigvalsh(H1))
check("T1 spectrum at (M,v)=(7,3): {-10,-4,-3,3,4,10} = {+-(M+v),+-(M-v),+-v}",
      np.allclose(ev, [-10, -4, -3, 3, 4, 10]))
w, U = np.linalg.eigh(H1)
light = U[:, np.abs(np.abs(w) - v0) < 1e-9]
check("T1 light eigenvectors supported EXACTLY on the w=0 slot (rows 1 and 4)",
      np.allclose(light[[0, 2, 3, 5], :], 0))
H2p = M0 * Jz + v0 * Jx
check("T2 block spectrum {0, +-sqrt(M^2+v^2)} = {0, +-sqrt(58)}",
      np.allclose(np.sort(np.linalg.eigvalsh(H2p)),
                  [-np.sqrt(58), 0, np.sqrt(58)]))
H1m0 = np.block([[0 * Jz, v0 * np.eye(3)], [v0 * np.eye(3), 0 * Jz]])
check("branch M=0: spectrum {+-3 x3} -- nothing exactly massless, net 0",
      np.allclose(np.sort(np.linalg.eigvalsh(H1m0)), [-3, -3, -3, 3, 3, 3]))
# slope check numerically: light mass vs v
sl = []
for vv in (1e-3, 1e-4):
    Hs = np.block([[M0 * Jz, vv * np.eye(3)], [vv * np.eye(3), M0 * Jz]])
    lm = np.min(np.abs(np.linalg.eigvalsh(Hs)))
    sl.append(lm / vv)
see = []
for vv in (1e-3, 1e-4):
    lam = np.min(np.abs(np.linalg.eigvalsh(np.array([[0, vv], [vv, M0]]))))
    see.append(lam / vv ** 2)
check("light mass LINEAR in v (slope -> 1.000) vs seesaw control quadratic "
      "(lam/v^2 -> 1/M) [leg toy arithmetic CONFIRMED]",
      abs(sl[-1] - 1) < 1e-6 and abs(see[-1] - 1 / M0) < 1e-3)

print()
print("=" * 78)
print("R-S6: index table (Fractions) [leg S4a CONFIRMED]")
print("=" * 78)
sigma = Fraction(-16)
tab = {"A": Fraction(21, 8) * sigma, "B": Fraction(19, 8) * sigma,
       "bare": Fraction(5, 6) * 3 * sigma, "dbl": Fraction(11, 12) * 3 * sigma}
check("indices A=-42, B=-38, bare=-40, dbl=-44; Ahat=2 (from sigma only)",
      (tab["A"], tab["B"], tab["bare"], tab["dbl"]) == (-42, -38, -40, -44)
      and -sigma / 8 == 2)
check("additivity -40 - (-2) = -38; fork = 4 = 2*ind(D); mod3 = (0,1,2,1)",
      tab["bare"] - (-2) == tab["B"] and tab["B"] - tab["A"] == 4
      and tuple(int(x) % 3 for x in (tab["A"], tab["B"], tab["bare"], tab["dbl"]))
      == (0, 1, 2, 1))

print()
print("=" * 78)
print("R-S7: verbatim needles -- BOTH primaries (the leg needled only one)")
print("=" * 78)
REPO = r"C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization"
TR = REPO + r"\papers\drafts\Transcript into the impossible.md"
with open(TR, encoding="utf-8", errors="replace") as f:
    T = f.read()


def nrm(s):
    return re.sub(r"[>*`\"'\s]+", " ", s)


check("TRANSCRIPT L107 (the leg-OMITTED declaration): 'zero forms valued in "
      "the positive spinners, direct sum one forms valued in the negative "
      "spinners' -- present verbatim",
      nrm("zero forms valued in the positive spinners, direct sum one forms "
          "valued in the negative spinners on that top space, you're gonna "
          "get three generations of standard model fermions") in nrm(T))
check("TRANSCRIPT [00:40:27] conjugate gloss present",
      nrm("aside from being spin three halves is just the conjugate of the "
          "internal symmetry representation") in nrm(T))

with open(r"C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB"
          r"\79411e9e-5aaa-44a7-ba95-2f380675a349\scratchpad\corners-swing"
          r"\LEG-A2-massless-bookkeeping.py", encoding="utf-8") as f:
    LEGPY = f.read()
check("the leg's script contains NO reference to the L107 declaration "
      "('positive spinners' absent) -- the omission is real",
      "positive spinners" not in LEGPY)

import pypdf   # noqa: E402
rd = pypdf.PdfReader(REPO + r"\Geometric_UnityDraftApril1st2021.pdf")
p50 = rd.pages[50].extract_text() or ""
p51 = rd.pages[51].extract_text() or ""
p63 = rd.pages[63].extract_text() or ""
check("GU DRAFT p63 item iii: 'unadorned non-chiral Dirac spinors' + "
      "'light Fermions being light in low gravity regimes' (mass = VEV of a "
      "single field, cosmological-constant-like) -- present verbatim",
      nrm("unadorned non-chiral Dirac spinors") in nrm(p63)
      and nrm("light Fermions being light in low gravity regimes") in nrm(p63))
check("GU DRAFT p51: 'a non-chiral total theory splits' (emergent chirality) "
      "-- present verbatim", nrm("a non-chiral total theory splits") in nrm(p51))
check("GU DRAFT p51: spin-3/2 cousin generation with REVERSED chirality logic "
      "('right handed matter and left handed anti-matter') -- present verbatim",
      nrm("right handed matter and left handed anti-matter") in nrm(p51 + p50))
check("GU DRAFT was never opened by the leg (no 'Geometric_Unity' path, no "
      "pypdf, no draft quote in the leg script)",
      "Geometric_Unity" not in LEGPY and "pypdf" not in LEGPY)

print()
print("=" * 78)
print("R-S8: audit of the leg's 81-check count (vacuous/tautological items)")
print("=" * 78)
# computed from the leg's source itself:
n_literal_true = len(re.findall(r",\s*True\)", LEGPY))          # lines 306/385/498
n_tauto_net = LEGPY.count("net_half + (-net_half) == 0")        # line 257: x-x==0
n_gp_const = (3 if "gp_engages(False, COUPLED) is False" in LEGPY else 0) \
    + (1 if "gp_engages(True, COUPLED) is True" in LEGPY else 0)  # constant fn
n_firewall_const = LEGPY.count("58.72 != 0 and COUPLED")        # constants
n_vac = n_literal_true + n_tauto_net + n_gp_const + n_firewall_const
print(f"   literal-True: {n_literal_true}; x-x==0 tautology: {n_tauto_net}; "
      f"constant-input gp_engages: {n_gp_const}; constant firewall: "
      f"{n_firewall_const}; TOTAL vacuous/tautological: {n_vac} of 81")
check("computed from source: 9 of the leg's 81 checks are vacuous or "
      "tautological (literal-True conds, x-x==0, constant-input boolean fn, "
      "constant firewall) -- including the one sold as the 'independent "
      "rep-arithmetic match' to the capstone's vectorlike measurement",
      n_vac == 9 and n_tauto_net == 1)

print()
print(f"REFEREE: ALL {N} CHECKS PASSED (exit 0)")
sys.exit(0)
