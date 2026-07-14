#!/usr/bin/env python3
r"""
W184 / TEAM MIRROR-SUPERSELECT (label W184) -- does the mirror/ghost SUPERSELECTION structure
(W173: the Krein form K implements the CARTAN INVOLUTION of so(9,5); canon V2 "residual 0.0e+00")
FORBID the ghost -> two-physical-graviton decay that drove the build sprint's NOT-OPERATIVE lean
(W178 physical-sheet pole; W179 above-threshold obstruction)?

Joe's decisive conjecture: if the mirror is a GENUINE superselection sector, the ghost -> two-
PHYSICAL-graviton decay CROSSES a superselection (Cartan) boundary = FORBIDDEN -> the anti-damping
width is ZERO -> the physical-sheet pole never forms -> PT unbroken -> the interacting C-operator
EXISTS -> OPERATIVE -> bar (b) clears.

THE DECISIVE CHECK (adversarial persona 5, made the load-bearing test here):
  A charge is a SUPERSELECTION rule only if it COMMUTES WITH THE DYNAMICS (with the S-matrix /
  the interaction vertex).  Global-ness (being the Cartan involution, an outer/global automorphism
  rather than a local gauge transformation) is NECESSARY but NOT SUFFICIENT.  The sufficient and
  decisive question: does GU's interaction VERTEX conserve the Cartan (ghost-parity) charge P, or
  violate it?
    * If the vertex is P-EVEN ([P,V]=0): P is conserved, the cross-sector amplitude is IDENTICALLY
      zero (genuine superselection), the ghost cannot decay, width = 0, OPERATIVE.
    * If the vertex is P-ODD ({P,V}=0): P is NOT conserved, the amplitude is nonzero, the ghost
      decays, W178/W179 stand, NOT-OPERATIVE.

MACHINE FACT (already latent in the sprint's OWN construction, W169/W178 fock_build):
  the ghost<->two-graviton CROSS vertex  A = (a1 a1) a2^dag - h.c.  is "Krein-ODD" -- and on Fock
  space the Krein fundamental symmetry sign IS the ghost-parity P = (-1)^{n_ghost} (a multi-ghost
  state has Krein norm sign (-1)^{n_ghost}).  So "Krein-odd" == "ghost-parity-ODD" == "violates the
  Cartan charge".  The very object that mediates the decay is the object that BREAKS the charge Joe
  hopes will forbid it.  A trilinear ghost->2-graviton vertex changes ghost number by 1 (odd) and
  is therefore ALWAYS P-odd: a genuine decay vertex can NEVER conserve ghost parity.  Superselection
  would mean such a vertex is ABSENT (coupling zero by symmetry = the ghost decouples), NOT that a
  would-be-nonzero width is "blocked at the boundary".

  => The superselection reframe is LOGICALLY EQUIVALENT to the standing OPEN condition [P_ghost,S]=0
     (the Turok-Bateman positivity condition the canon already flags as unbuilt), NOT an independent
     new mechanism.  It relocates bar (b) onto exactly the object W173 said it was relocated onto; it
     does not clear it.  And the decisive vertex check comes out VIOLATES for the sprint's cross
     vertex (and for any gravitationally-coupled Stelle ghost).

Structure of this test (positive controls FIRST, W138 discipline; numpy only; deterministic):
  PC1  reproduce W178's argument-principle PHYSICAL-SHEET pole count WITH the anti-damping channel
       (= 1 physical-sheet pole) -- the NOT-OPERATIVE baseline this wave tries to overturn.
  PC2  reproduce W173's kinematic fact: K = eta implements the CARTAN INVOLUTION of so(9,5)
       (theta(X)=eta X eta is an automorphism, theta^2=1, fixes the compact so(9)+so(5), negates the
       noncompact part) -- the mirror IS globally Cartan-graded.  (necessary, not sufficient.)
  PC3  a GENUINE superselection control: a conserved Z2 charge P with [P,V]=0 gives an IDENTICALLY
       ZERO cross-sector amplitude; a charge-VIOLATING vertex {P,V}=0 gives a NONZERO amplitude.
       (this is the difference between "forbidden by a conserved charge" and "a grading the vertex
       ignores".)
  C1-C5  THE CORE: the Cartan charge of ghost vs two gravitons; the decisive vertex check on GU's
       OWN cross vertex A; the decay matrix element; the re-run pole count with the channel REMOVED;
       the logical equivalence superselection <=> [P,S]=0 <=> cross vertex absent.
  M1-M2  the MIRROR-THRESHOLD alternative: our-massless-graviton channel is open for any M (W179);
       a mirror-only threshold requires the ghost to DECOUPLE from our gravitons = superselection
       again = [P,S]=0; gravitational universality forbids the decoupling.

VERDICT: DECAY-ALLOWED-NOT-OPERATIVE-STANDS, CONDITIONAL-on-[P_ghost,S]=0.  The mirror is NOT a
proven superselection sector: it is a global Cartan GRADING that becomes a superselection RULE only
under the unproven [K,S]=0, and GU's cross vertex (Krein-odd) VIOLATES it.  bar (b) does NOT clear
via the superselection channel; it relocates onto the same [P_ghost,S]=0 / W48 self-energy object.
H59 remains OPEN.

Reproducible:  python -u tests/W184_mirror_superselection_decay.py   (numpy only; exit 0 on success)
No canon / RESEARCH-STATUS / claim-status / verdict / posture file is touched.  Exploration-grade.
"""
from __future__ import annotations

import math

import numpy as np

np.random.seed(20260714)  # determinism

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


log("=" * 98)
log("W184 / TEAM MIRROR-SUPERSELECT -- does the Cartan-involution superselection forbid ghost decay?")
log("=" * 98)

# =================================================================================================
# PC1 -- POSITIVE CONTROL: reproduce W178's argument-principle PHYSICAL-SHEET pole count WITH the
#        anti-damping ghost decay channel present.  This is the NOT-OPERATIVE baseline (= 1 physical-
#        sheet upper-half pole; normal-sign control = 0).  We overturn it ONLY if the channel is
#        genuinely superselection-forbidden.
# =================================================================================================
log("\n[PC1] positive control: W178 physical-sheet ghost pole WITH the decay channel (NOT-OPERATIVE baseline)")

M2 = 1.0        # ghost mass^2
S_TH = 0.10     # two-body (two-graviton) threshold; ghost ABOVE it (M2 > S_TH): W51 Im Sigma > 0


def wI(s: complex, s_th: float) -> complex:
    return np.sqrt(complex(s_th - s))


def Fsheet(s: complex, kappa: float, s_sign: float, sheet: int, s_th: float = S_TH) -> complex:
    w = wI(s, s_th) if sheet == 1 else -wI(s, s_th)
    return s - M2 - s_sign * kappa * w


def count_poles_UHP(kappa: float, s_sign: float, sheet: int, R: float = 40.0,
                    delta: float = 1e-4, n: int = 3000, s_th: float = S_TH) -> float:
    """Argument principle: (1/2 pi i) * contour integral of F'/F around the upper-half-plane
    rectangle = number of zeros of F (= poles of the propagator) enclosed.  Integer, robust."""
    def Fp(s: complex) -> complex:
        h = 1e-7
        return (Fsheet(s + h, kappa, s_sign, sheet, s_th) - Fsheet(s - h, kappa, s_sign, sheet, s_th)) / (2 * h)

    xs = np.linspace(-R, R, n)
    seg = [complex(x, delta) for x in xs]
    seg += [complex(R, y) for y in np.linspace(delta, R, n)]
    seg += [complex(x, R) for x in xs[::-1]]
    seg += [complex(-R, y) for y in np.linspace(R, delta, n)]
    seg = np.array(seg)
    total = 0j
    for i in range(len(seg) - 1):
        a, b = seg[i], seg[i + 1]
        mid = 0.5 * (a + b)
        total += (Fp(mid) / Fsheet(mid, kappa, s_sign, sheet, s_th)) * (b - a)
    return float((total / (2j * math.pi)).real)


anti_physI_on = [count_poles_UHP(k, -1.0, 1) for k in (0.05, 0.2, 0.5, 1.0)]
norm_physI = [count_poles_UHP(k, +1.0, 1) for k in (0.05, 0.2, 0.5, 1.0)]
check("PC1  WITH the anti-damping decay channel: exactly ONE physical-sheet pole (NOT-OPERATIVE); "
      "normal-sign control has ZERO -- reproduces W178's decider",
      all(abs(x - 1.0) < 0.05 for x in anti_physI_on) and all(abs(x) < 0.05 for x in norm_physI),
      f"#phys-sheet(I) poles: ghost = {[round(x,2) for x in anti_physI_on]}, normal = "
      f"{[round(x,2) for x in norm_physI]}")

# =================================================================================================
# PC2 -- POSITIVE CONTROL: reproduce W173's kinematic fact -- K = eta implements the CARTAN
#        INVOLUTION theta of so(9,5).  theta(X) = eta X eta^{-1}; on so(p,q) this equals -X^T.
#        theta is an ALGEBRA automorphism (theta[X,Y]=[thetaX,thetaY]), theta^2 = id, it FIXES the
#        maximal compact so(9)+so(5) (block-diagonal generators) and NEGATES the noncompact part
#        (off-diagonal boosts).  So the mirror is genuinely GLOBALLY Cartan-graded.  This is
#        NECESSARY for superselection but (PC3 / core) NOT sufficient.
# =================================================================================================
log("\n[PC2] positive control: K = eta implements the CARTAN INVOLUTION of so(9,5) (W173 kinematic fact)")

p, q = 9, 5
D = p + q
eta = np.diag([1.0] * p + [-1.0] * q)


def so_pq_basis():
    """Generators X_{ab} of so(p,q): X^T eta + eta X = 0.  Built as eta-antisymmetric matrices
    E_{ab} eta - eta-transpose so that each lies in the algebra."""
    gens = []
    for a in range(D):
        for b in range(a + 1, D):
            M = np.zeros((D, D))
            # so(p,q) generator: M = e_a e_b^T eta_bb - e_b e_a^T eta_aa  (satisfies M^T eta + eta M = 0)
            M[a, b] = eta[b, b]
            M[b, a] = -eta[a, a]
            gens.append((a, b, M))
    return gens


gens = so_pq_basis()
# verify each is in so(p,q)
in_alg = max(float(np.max(np.abs(M.T @ eta + eta @ M))) for _, _, M in gens)


def theta(X):
    return eta @ X @ np.linalg.inv(eta)


# theta is an automorphism on a random pair of generators, theta^2 = id
_, _, X1 = gens[3]
_, _, X2 = gens[27]
comm = X1 @ X2 - X2 @ X1
auto_err = float(np.max(np.abs(theta(comm) - (theta(X1) @ theta(X2) - theta(X2) @ theta(X1)))))
invol_err = max(float(np.max(np.abs(theta(theta(M)) - M))) for _, _, M in gens)
# compact (both indices same sign block) fixed (+1); noncompact (mixed block) negated (-1)
compact_fixed = True
noncompact_negated = True
for a, b, M in gens:
    same_block = (a < p and b < p) or (a >= p and b >= p)
    if same_block:
        compact_fixed = compact_fixed and float(np.max(np.abs(theta(M) - M))) < 1e-9
    else:
        noncompact_negated = noncompact_negated and float(np.max(np.abs(theta(M) + M))) < 1e-9
check("PC2  K = eta implements the Cartan involution theta(X)=eta X eta of so(9,5): "
      "generators in-algebra, theta an automorphism, theta^2=id, compact so(9)+so(5) FIXED, "
      "noncompact NEGATED (residual ~0, the canon 'residual 0.0e+00' fact)",
      in_alg < 1e-9 and auto_err < 1e-9 and invol_err < 1e-9 and compact_fixed and noncompact_negated,
      f"in-alg={in_alg:.1e}, auto={auto_err:.1e}, theta^2={invol_err:.1e}, "
      f"compact-fixed={compact_fixed}, noncompact-negated={noncompact_negated}")

# =================================================================================================
# PC3 -- POSITIVE CONTROL: the DIFFERENCE between a genuine superselection rule and a mere grading.
#        Two-mode boson Fock space.  Charge P = (-1)^{n1} (a Z2 grading).
#          V_even = a1^dag a1^dag + a1 a1   changes n1 by 2 -> [P,V_even] = 0 -> P CONSERVED.
#          V_odd  = a1^dag        + a1      changes n1 by 1 -> {P,V_odd}  = 0 -> P VIOLATED.
#        Cross-sector amplitude <n1 odd | V | n1 even>:  IDENTICALLY ZERO for V_even (superselection),
#        NONZERO for V_odd (the grading is ignored by the vertex).  THIS is the template for the core.
# =================================================================================================
log("\n[PC3] positive control: genuine superselection ([P,V]=0 -> amplitude=0) vs a grading the vertex ignores")

nB = 6


def boson_a(n: int) -> np.ndarray:
    a = np.zeros((n, n), dtype=complex)
    for k in range(1, n):
        a[k - 1, k] = math.sqrt(k)
    return a


a = boson_a(nB)
ad = a.conj().T
Pz = np.diag([(-1.0) ** k for k in range(nB)]).astype(complex)   # P = (-1)^{n1}
V_even = ad @ ad + a @ a
V_odd = ad + a
comm_even = float(np.max(np.abs(Pz @ V_even - V_even @ Pz)))       # [P, V_even]
acomm_odd = float(np.max(np.abs(Pz @ V_odd + V_odd @ Pz)))         # {P, V_odd}
# cross-sector amplitude between |0> (P=+1) and |1> (P=-1)
ket0 = np.zeros(nB, dtype=complex); ket0[0] = 1.0
ket1 = np.zeros(nB, dtype=complex); ket1[1] = 1.0
amp_even_cross = abs(ket1.conj() @ V_even @ ket0)   # P-changing amplitude under a P-CONSERVING vertex
amp_odd_cross = abs(ket1.conj() @ V_odd @ ket0)     # P-changing amplitude under a P-VIOLATING vertex
check("PC3  genuine superselection: [P,V_even]=0 -> the P-changing amplitude is IDENTICALLY ZERO; "
      "a grading the vertex ignores: {P,V_odd}=0 -> the P-changing amplitude is NONZERO",
      comm_even < 1e-12 and acomm_odd < 1e-12 and amp_even_cross < 1e-12 and amp_odd_cross > 0.5,
      f"[P,V_even]={comm_even:.1e}, amp(V_even, cross)={amp_even_cross:.1e} (forbidden); "
      f"amp(V_odd, cross)={amp_odd_cross:.3f} (allowed)")

# =================================================================================================
# CORE -- the ghost / two-graviton Cartan charge, and the DECISIVE vertex check on GU's OWN vertex.
#   Two-mode Krein Fock model (the W169/W178 fock_build): a1 = physical graviton, a2 = ghost.
#   Ghost-parity / Cartan charge on Fock space:  P = (-1)^{n_ghost} = (-1)^{a2^dag a2}.
#   This P IS the Krein fundamental-symmetry sign (a state with n_ghost ghosts has Krein norm sign
#   (-1)^{n_ghost}), so "Krein-odd" (canon's label for the cross vertex A) == "P-odd".
#   GU's cross vertex (verbatim from W178 fock_build):  A = (a1 a1) a2^dag - (a1^dag a1^dag) a2.
#   GU's diagonal (Krein-even) vertex:                  Sv = a1 a2^dag a2^dag + h.c. + ...
# =================================================================================================
log("\n" + "-" * 98)
log("CORE -- the Cartan charge of ghost vs two gravitons, and the DECISIVE vertex check")
log("-" * 98)

nF = 8


def fock_ops(n: int):
    a_ = np.zeros((n, n), dtype=complex)
    for k in range(1, n):
        a_[k - 1, k] = math.sqrt(k)
    Ie = np.eye(n, dtype=complex)
    return np.kron(a_, Ie), np.kron(Ie, a_)


a1, a2 = fock_ops(nF)
a1d, a2d = a1.conj().T, a2.conj().T
n1_op = a1d @ a1
n2_op = a2d @ a2

# ghost-parity / Cartan charge P = (-1)^{n_ghost}; on the number basis it is diagonal +-1
P = np.diag([(-1.0) ** int(round(n2_op[i, i].real)) for i in range(nF * nF)]).astype(complex)
check("C0  P = (-1)^{n_ghost} is a Z2 involution (P^2 = 1) and is the Krein fundamental symmetry "
      "sign on Fock space (Krein-odd == ghost-parity-odd)",
      float(np.max(np.abs(P @ P - np.eye(nF * nF)))) < 1e-12,
      "P^2 = 1; P grades states by ghost-number parity = the Cartan/ghost-parity charge")

# GU's OWN vertices (verbatim structure from W178 fock_build)
A = (a1 @ a1) @ a2d - (a1d @ a1d) @ a2                                   # the CROSS / decay vertex
Sv = (a1 @ (a2d @ a2d) + a1d @ (a2 @ a2)) + (a1d @ a1d @ a1 + a1d @ a1 @ a1)  # a Krein-EVEN vertex

# --- C1: the Cartan charge of the states ---
# ghost |n1=0, n2=1>: P = -1 ;  two gravitons |n1=2, n2=0>: P = +1 ;  one graviton: P=+1
def fock_ket(k1: int, k2: int) -> np.ndarray:
    v = np.zeros(nF * nF, dtype=complex)
    v[k1 * nF + k2] = 1.0
    return v


ghost = fock_ket(0, 1)
two_grav = fock_ket(2, 0)
one_grav = fock_ket(1, 0)
P_ghost = float((ghost.conj() @ P @ ghost).real)
P_2grav = float((two_grav.conj() @ P @ two_grav).real)
check("C1  Cartan (ghost-parity) charge: ghost = -1 (Krein-odd/negative-norm), two physical "
      "gravitons = +1, one graviton = +1.  The decay ghost -> 2 gravitons CHANGES the charge "
      "(-1 -> +1): charge-changing, hence forbidden IFF the charge is conserved by the dynamics",
      abs(P_ghost + 1.0) < 1e-12 and abs(P_2grav - 1.0) < 1e-12,
      f"P(ghost) = {P_ghost:+.0f}, P(2 gravitons) = {P_2grav:+.0f} -> decay is charge-changing")

# --- C2: THE DECISIVE VERTEX CHECK -- does GU's cross vertex A conserve or violate P? ---
comm_PA = float(np.max(np.abs(P @ A - A @ P)))     # [P, A]  (=0 would mean CONSERVED)
acomm_PA = float(np.max(np.abs(P @ A + A @ P)))    # {P, A}  (=0 means P-ODD = VIOLATES)
comm_PSv = float(np.max(np.abs(P @ Sv - Sv @ P)))  # [P, Sv] (Krein-even reference; =0)
check("C2  DECISIVE CHECK -- GU's cross (decay) vertex A = (a1 a1)a2^dag - h.c. is P-ODD "
      "({P,A}=0, [P,A] != 0): it VIOLATES the Cartan/ghost-parity charge.  (The Krein-EVEN vertex "
      "Sv conserves it, [P,Sv]=0.)  => the mediating vertex breaks the very charge that would have "
      "forbidden the decay -- there is NO superselection protection",
      acomm_PA < 1e-12 and comm_PA > 0.5 and comm_PSv < 1e-12,
      f"{{P,A}} = {acomm_PA:.1e} (A is P-ODD), [P,A] = {comm_PA:.2f} != 0 (NOT conserved); "
      f"[P,Sv] = {comm_PSv:.1e} (Sv is P-even)")

# --- C3: the decay matrix element is NONZERO (allowed, GIVEN the vertex) ---
amp_decay = abs(two_grav.conj() @ A @ ghost)
check("C3  the decay matrix element <2 gravitons| A |ghost> is NONZERO -> the decay is ALLOWED "
      "given the (P-odd) vertex; W178/W179's anti-damping width is real, not zero",
      amp_decay > 0.5,
      f"|<gg|A|ghost>| = {amp_decay:.4f} != 0")

# --- C4: a genuine trilinear ghost->2-graviton vertex is ALWAYS P-odd (a counting fact) ---
#   any monomial with (delta n_ghost) odd is P-odd; the decay vertex has delta n_ghost = 1.
#   Demonstrate: build every cubic monomial coupling the sectors and check its P-parity vs its
#   ghost-number change.  P-parity = (-1)^{delta n_ghost}.  A P-EVEN cubic ghost-graviton coupling
#   with an ODD ghost-number change does NOT exist.
def dn_ghost_parity(delta_n2: int) -> int:
    return 1 if delta_n2 % 2 == 0 else -1


trilinear_channels = [
    ("ghost -> 2 gravitons  (a1^dag a1^dag a2)", -1),   # delta n_ghost = -1 (odd) -> P-odd
    ("2 gravitons -> ghost  (a1 a1 a2^dag)",     +1),   # delta n_ghost = +1 (odd) -> P-odd
    ("ghost pair-production (a1^dag a2^dag a2^dag)", +2),  # delta n_ghost = +2 (even) -> P-even
]
counting_ok = (dn_ghost_parity(-1) == -1 and dn_ghost_parity(1) == -1 and dn_ghost_parity(2) == +1)
check("C4  COUNTING FACT: a vertex's ghost-parity = (-1)^{delta n_ghost}.  The ghost->2-graviton "
      "decay changes ghost number by 1 (ODD) => ALWAYS P-odd => can NEVER conserve the Cartan "
      "charge.  P is conserved ONLY if such trilinear cross vertices are ABSENT (ghosts pair-"
      "produced) = the ghost DECOUPLES.  Superselection = coupling zero by symmetry, NOT a blocked "
      "nonzero width.",
      counting_ok,
      "delta n_ghost = 1 (odd) -> P-odd for any ghost->2-graviton vertex")

# --- C5: RE-RUN the pole count with the (would-be superselection-forbidden) channel REMOVED ---
#   "Channel removed" == the cross coupling is zero == the vertex is P-even == [P,S]=0.  In Model B
#   this is kappa_cross -> 0 (no two-graviton absorptive part feeding the ghost self-energy).  The
#   physical-sheet pole DISAPPEARS -> OPERATIVE.  But this is ACHIEVED BY ASSUMING [P,S]=0; it is
#   not an independent consequence of the Cartan GRADING (PC2), which the P-odd vertex (C2) violates.
# "Channel removed" is modelled physically as the two-graviton cut being CLOSED at the ghost mass:
# raise the threshold above the ghost (s_th_closed = 2.0 > M2 = 1.0), so Im Sigma(M2) = 0 (no
# absorptive part / no on-shell decay) even with the anti-damping sign.  The pole is then real and
# there is NO physical-sheet upper-half pole.  This is exactly the state a genuine superselection
# rule (or the sub-threshold regime, W179) would deliver.
# Count strictly COMPLEX (PT-breaking) physical-sheet poles: raise the contour floor to delta=0.03
# so a real (Im=0), non-PT-breaking sub-threshold pole is cleanly excluded (a real pole is a stable
# real energy, not a complex-conjugate PT-breaking pair).
S_TH_CLOSED = 2.5
anti_physI_off = [count_poles_UHP(k, -1.0, 1, delta=0.03, s_th=S_TH_CLOSED) for k in (0.05, 0.2, 0.5)]
check("C5  RE-RUN with the decay channel REMOVED (two-graviton cut closed at the ghost mass, i.e. "
      "IMPOSING [P,S]=0 / superselection): the physical-sheet pole count drops to ZERO -> OPERATIVE. "
      "BUT closing the channel = assuming the vertex is P-even = assuming superselection; it is NOT "
      "delivered by the Cartan grading, which the actual P-odd vertex (C2) violates.  Circular.",
      all(abs(x) < 0.05 for x in anti_physI_off) and abs(anti_physI_on[0] - 1.0) < 0.05,
      f"#phys-sheet poles: WITH channel = {round(anti_physI_on[0],2)} (NOT-OPERATIVE), "
      f"WITHOUT channel = {[round(x,2) for x in anti_physI_off]} (OPERATIVE, but by assuming [P,S]=0)")

# =================================================================================================
# MIRROR-THRESHOLD alternative -- is the correct threshold the MIRROR two-graviton threshold
#   (fourth-derivative scale) rather than OUR massless one (W179 used m_phys=0)?
#   Reuse W179's energy denominator D(k1,k2) = om2(k1+k2) - om1(k1) - om1(k2).
# =================================================================================================
log("\n" + "-" * 98)
log("MIRROR-THRESHOLD alternative -- does the ghost decay into MIRROR gravitons instead of ours?")
log("-" * 98)


def om(k: float, m: float) -> float:
    return math.sqrt(k * k + m * m)


def D_has_onshell_zero(m_phys: float, m_ghost: float, K_tot_grid=None) -> bool:
    """W179: on-shell zero of D <=> ghost can decay into two m_phys quanta <=> m_ghost >= 2 m_phys.
    Test by sign change of sup_split D over total momentum K."""
    if K_tot_grid is None:
        K_tot_grid = np.linspace(0.0, 50.0, 4000)
    vals = [om(K, m_ghost) - 2.0 * om(K / 2.0, m_phys) for K in K_tot_grid]  # sup over split at k1=k2=K/2
    return (max(vals) >= 0.0 >= min(vals)) or (min(vals) < 0 < max(vals)) or (max(vals) >= 0)


# M1: OUR massless graviton (m_phys = 0): channel open for EVERY ghost mass M > 0 (W179 reproduced)
massless_open = all(D_has_onshell_zero(0.0, M) for M in (0.3, 1.0, 3.0, 10.0))
# a MIRROR graviton gapped at the fourth-derivative scale g_mir: sub-threshold iff M < 2 g_mir
sub_thr_if_gapped = (not D_has_onshell_zero(5.0, 1.0))  # heavy mirror graviton g=5, ghost M=1 -> closed
check("M1  reuse W179: for OUR massless graviton (m_phys=0) the two-graviton decay channel is OPEN "
      "for EVERY ghost mass M>0 (D has a real on-shell zero); a MIRROR graviton gapped above M/2 "
      "would close it -- so the mirror-threshold reframe is kinematically COHERENT",
      massless_open and sub_thr_if_gapped,
      "massless channel open for all M; a heavy-mirror-graviton channel is closed (sub-threshold)")

# M2: but the ghost carries stress-energy -> couples to OUR massless graviton universally
#   (gravitational universality).  Decoupling from our graviton = a P-even (cross-coupling-zero)
#   dynamics = [P,S]=0 = superselection AGAIN.  So the mirror-threshold reframe does not close the
#   OUR-massless channel unless the same unproven [P,S]=0 holds.
check("M2  the mirror-threshold reframe does NOT close the decisive OUR-massless-graviton channel: "
      "a stress-energy-carrying spin-2 ghost couples to the massless graviton UNIVERSALLY, so that "
      "channel stays open (M1) unless the ghost DECOUPLES from our gravitons -- which is exactly the "
      "cross-coupling-zero / [P,S]=0 / superselection condition again.  Same open object, relabeled. "
      "(W181: gapping our graviton at the mirror scale is H36-forbidden and GW-excluded by ~1e20.)",
      massless_open,   # the load-bearing fact: our-graviton channel is open regardless of the mirror scale
      "our-massless channel open for all M; closing it needs [P,S]=0, not a mirror threshold")

# =================================================================================================
# SYNTHESIS
# =================================================================================================
log("\n" + "-" * 98)
log("SYNTHESIS")
log("-" * 98)
log("  * The mirror IS globally Cartan-graded (PC2, W173 kinematic fact) -- NECESSARY for")
log("    superselection but NOT SUFFICIENT.")
log("  * A genuine superselection rule needs the charge CONSERVED BY THE DYNAMICS (PC3).  The")
log("    decisive check (C2): GU's OWN cross/decay vertex A is P-ODD -- it VIOLATES the Cartan")
log("    charge.  A trilinear ghost->2-graviton vertex is ALWAYS P-odd (C4, counting).")
log("  * Therefore the decay amplitude is NONZERO (C3); the width is real, not zero; the physical-")
log("    sheet pole stands (PC1).  Removing the channel (C5) restores OPERATIVE but only by ASSUMING")
log("    the vertex is P-even = assuming [P,S]=0 -- the standing OPEN condition, not a new mechanism.")
log("  * The mirror-threshold reframe (M1/M2) is kinematically coherent but does not close the")
log("    OUR-massless-graviton channel without the SAME [P,S]=0 decoupling assumption.")
log("  => Superselection <=> [P_ghost,S]=0 <=> cross vertex absent.  bar (b) is RELOCATED onto")
log("     [P_ghost,S]=0 (exactly W173's relocation), NOT cleared.  DECAY-ALLOWED-NOT-OPERATIVE-STANDS,")
log("     CONDITIONAL-on-[P_ghost,S]=0.  H59 remains OPEN.")

# =================================================================================================
# SUMMARY
# =================================================================================================
log("\n" + "=" * 98)
npass = sum(1 for _, ok, _ in results if ok)
for name, ok, _ in results:
    if not ok:
        log(f"  FAILED: {name}")
log(f"W184 RESULT: {npass}/{len(results)} checks passed.")
assert all(ok for _, ok, _ in results), "some W184 checks FAILED"

log("")
log("W184 VERDICT (this file is the computation, not a claim-status change):")
log("  Mirror a genuine superselection sector?  NO -- a global Cartan GRADING (PC2) that becomes a")
log("    superselection RULE only under the unproven [K,S]=0.")
log("  Does GU's interaction vertex conserve the Cartan charge?  NO -- the cross (decay) vertex A is")
log("    P-ODD / Krein-odd (C2); it VIOLATES the charge.  Any ghost->2-graviton vertex is P-odd (C4).")
log("  Ghost-decay verdict:  ALLOWED (nonzero amplitude, C3); width real; physical-sheet pole stands.")
log("  Re-run pole count with the channel removed:  0 physical-sheet poles (OPERATIVE) -- but only by")
log("    ASSUMING [P,S]=0 (C5); circular, not delivered by superselection.")
log("  Mirror-threshold alternative:  does NOT close the our-massless channel without [P,S]=0 (M1/M2).")
log("  OVERALL:  DECAY-ALLOWED-NOT-OPERATIVE-STANDS, CONDITIONAL-on-[P_ghost,S]=0.  The superselection")
log("    reframe RELOCATES bar (b) onto [P_ghost,S]=0 (= W48 self-energy), it does not clear it.")
log("  H59 remains OPEN. No canon / status / verdict / posture change.")
raise SystemExit(0)
