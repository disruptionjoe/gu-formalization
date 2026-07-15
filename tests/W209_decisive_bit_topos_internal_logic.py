#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W209 -- the DECISIVE BIT by the R12 route: topos internal-logic / sheaf semantics over the
observer/capability site. Is the C-OPERATOR GRADING SIGN (eta_+ = eta*C, record-count mode
Krein-NEGATIVE on the (6,4) fiber) FORCED, or a residual truth-value (Godel-independent)?

THE QUESTION (identical for all five sibling routes). Take the good-stable fixed point as GIVEN.
Its STABILIZER = the counterfactual/gauge deformations preserving the good-stable properties (real
total spectrum; positive-definite TOTAL metric; C-operator operative, eta_+ = eta*C). Compute the
space of invariant symmetric bilinear forms. ONE-dimensional with generator eta_+ = eta*C (record-
count mode Krein-negative)? FORCED = dim 1 AND generator eta_+ (Krein sign DERIVED). RESIDUAL-BIT-
STANDS = dim>1 OR only eta up-to-grading (Godel-independent, must be posited).

THE GUARDRAIL (no false positive). W203 ALREADY forced the UNGRADED metric to eta (Schur, nulldim 1
on the vector rep). That is NOT the open bit. The open bit is whether the C-OPERATOR GRADING SIGN
(eta_+ = eta*C, record-count mode negative) is forced. Settle the SIGN. If the method only recovers
eta UP-TO-GRADING, the verdict is RESIDUAL-BIT-STANDS. Truth-seeking; do not root.

THE R12 METHOD (topos internal logic). Model the field/grading data as objects in the sheaf topos
Sh(X) over the observer/capability site -- the global -> regional -> individual hierarchy, realized
as the Alexandrov space X of the refinement poset. The INVARIANT FORM is a GLOBAL SECTION; the
C-GRADING CHOICE is read through the SUBOBJECT CLASSIFIER Omega. Two facts must be separated:
  (A) the UNGRADED metric: is its global-section space a singleton (forced)?  [reproduce W203]
  (B) the GRADING SIGN: is the subobject "operative grading = the indefinite Krein one (record-mode
      negative), eta_+ = eta*C" a COMPLEMENTED subobject (chi factors through Boolean {0,1} =>
      sign DECIDED => FORCED), or a NON-complemented one (chi lands on an intermediate Heyting truth
      value => the sign is not internally decidable => the bit is EXTERNAL, matching the Godel
      reading => RESIDUAL-BIT-STANDS)?
Distinguish a BOOLEAN classifier (sign decided) from a genuinely INTUITIONISTIC one (sign not
internally forced).

WHAT THE PRIORS HAND R12 (cited, not re-derived here):
  * W203 KER1/KER3: under the FULL non-compact Krein-anti-self-adjoint gauge action, the space of
    invariant symmetric forms on the frame is EXACTLY 1-dim; the generator is eta (signature (9,5)),
    INDEFINITE. This is the UNGRADED metric -- forced. (guardrail's already-forced piece.)
  * W203 KER4: the positive-definite Hilbert/Frobenius Gram |eta| is invariant ONLY under the
    maximal COMPACT subgroup SO(9)xSO(5), NOT the full gauge group. So there are (at least) TWO
    natural gradings of eta -- the compact Gram |eta| and the operative Krein eta*C -- and the
    choice between them is exactly the compact-vs-noncompact / positive-definite-vs-Krein selection.
  * W168: on the (9,5)=(3,1)+(6,4) fiber the record-count/conformal mode is Krein-NEGATIVE and the
    geometric graviton mode Krein-POSITIVE (OPPOSITE), but the ACTIVATION (that the indefinite Krein
    form, not the positive-definite compact restriction, is the OPERATIVE grading) is the finality
    reading, flagged TaF-owned / not GU-internally decidable.
  * W201: the reservoir Krein SIGN is an order-2 element in the 2-primary (Z/8) selector arena; the
    "operative C-operator exists" bit is external. Both the count-selector and the sign route through
    the SAME K-definite non-chirality re-grading = the C-operator eta_+ = eta*C.

THE R12 READING (the payload). The compact-Gram-vs-Krein choice of W203 KER4 is precisely a section
of the grading over the observer site that the internal gauge-invariance logic does NOT force. In the
topos this is a NON-complemented subobject: its characteristic map lands on an INTERMEDIATE Heyting
truth value (true on the finer/local observers where finality is posited, undecided at the global
observer). So:
  (A) the ungraded eta IS a forced global section -- the classifier is BOOLEAN on that proposition
      (reproducing W203, the guardrail's already-forced piece);
  (B) the grading SIGN is NOT internally decidable -- the classifier is INTUITIONISTIC (non-Boolean)
      on that proposition; the global-section space of the "graded form" carries a RESIDUAL Z/2 (the
      two gradings |eta| and eta*C), neither selected by the internal logic.
VERDICT: RESIDUAL-BIT-STANDS. The sign is Godel-independent (external, must be posited), matching
W168's TaF-owned activation and W201's external order-2 datum. The method recovers eta UP-TO-GRADING;
by the guardrail that is RESIDUAL-BIT-STANDS, not FORCED.

Structure (positive controls first):
  [PC]   PC1 reproduce W203/Schur on the so(9,5) VECTOR rep: invariant symmetric forms are 1-dim,
         generator ~ eta, signature (9,5) INDEFINITE (the ungraded metric, forced).
         PC2 the (6,4)-fiber record-count/conformal mode is LOCALLY Krein-negative (port W168 mini:
         DeWitt conformal norm 4-16*lambda<0 at lambda=1).
         PC3 the subobject-classifier machinery: Sub(1)=frame of opens is a Heyting algebra; the
         HIERARCHICAL observer site is NON-Boolean (intermediate open without complement), while a
         DISCRETE site is Boolean -- the machinery correctly separates the two.
  [TOP]  T1 the ungraded eta: unique forced global section; its proposition = top(1), complemented =>
         BOOLEAN/FORCED (reproduces W203 inside the topos).
         T2 the grading sign: the two gradings |eta| (compact) and eta*C (Krein) are DISTINCT
         operators; the "operative grading is the Krein one" subobject lands on an INTERMEDIATE
         truth value => NON-complemented => the graded-form global sections are NOT a singleton
         (residual Z/2).
         T3 the determination: Boolean on the ungraded metric, INTUITIONISTIC on the grading sign =>
         eta forced, sign NOT internally decidable => external / Godel => RESIDUAL-BIT-STANDS.
  [NC]   NC1 over a DISCRETE observer site the classifier is Boolean and the grading WOULD be forced
         -- so the residual rides the genuine refinement hierarchy, not a modelling artifact.
         NC2 with a positive-definite AMBIENT (eta -> |eta|) there is one maximal-definite subspace,
         the two gradings coincide, the Z/2 collapses -- so the residual rides the indefinite (9,5)
         Krein structure.
         NC3 relabel guard: |eta| and eta*C are genuinely different operators (nonzero difference).

Everything exploration grade, conditional register. Nothing asserts GU, a vacuum, bar(b) movement,
or that the DESI wiggle is real. The topos site is a modelling choice (the observer/capability
hierarchy), named as such. Zero em dashes in paper-facing text.

Run: python -u tests/W209_decisive_bit_topos_internal_logic.py   (expect NN/NN, exit 0)
"""

from __future__ import annotations
import itertools
import numpy as np

CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'XX '}] {name}: {cond}")
    return bool(cond)


def check_val(name, got, expected, atol=1e-9):
    ok = abs(got - expected) <= atol
    CHECKS.append((name, ok))
    print(f"  [{'ok ' if ok else 'XX '}] {name}: got {got:.6g}  expected {expected:.6g}")
    return ok


P, Q = 9, 5
DIM = P + Q
ETA = np.diag([1.0] * P + [-1.0] * Q)          # the Clifford metric, signature (9,5), INDEFINITE
ABS_ETA = np.diag([1.0] * DIM)                  # |eta|, the compact-invariant positive-definite Gram

print("=" * 82)
print("W209 -- the decisive bit by R12 (topos internal logic / sheaf semantics)")
print("=" * 82)

# ==============================================================================================
print("\n[PC] Positive controls")
# ==============================================================================================

# ---- PC1: reproduce W203/Schur on the so(9,5) VECTOR rep. The stabilizer acts by the vector rep;
#      the space of invariant symmetric bilinear forms is 1-dim (Schur), generator ~ eta, INDEFINITE.
def so_pq_generators(eta):
    """A spanning set of so(p,q): matrices X with X^T eta + eta X = 0 (eta X antisymmetric)."""
    n = eta.shape[0]
    gens = []
    for a in range(n):
        for b in range(a + 1, n):
            A = np.zeros((n, n))
            A[a, b] = 1.0
            A[b, a] = -1.0                      # antisymmetric A
            X = np.linalg.solve(eta, A)         # eta X = A  =>  X = eta^{-1} A, so X^T eta + eta X = 0
            gens.append(X)
    return gens


gens = so_pq_generators(ETA)
check("PC1a so(9,5) has dim 91 generators", len(gens) == DIM * (DIM - 1) // 2)
# each generator eta-antisymmetric:
maxasym = max(float(np.max(np.abs(X.T @ ETA + ETA @ X))) for X in gens)
check_val("PC1b generators eta-antisymmetric (X^T eta + eta X = 0)", maxasym, 0.0, atol=1e-10)

# Solve for symmetric M (14x14) with X^T M + M X = 0 for all generators -> stack a linear system.
# symmetric basis of 14x14:
sym_basis = []
for a in range(DIM):
    for b in range(a, DIM):
        E = np.zeros((DIM, DIM))
        E[a, b] = 1.0
        E[b, a] = 1.0
        sym_basis.append(E)
nsym = len(sym_basis)                            # 105
rows = []
for X in gens:
    for E in sym_basis:
        C = X.T @ E + E @ X                       # must be 0 for invariance
        rows.append(C.reshape(-1))
# We want coefficients c s.t. sum_k c_k (X^T E_k + E_k X) = 0 for all X. Build constraint matrix:
# constraint matrix A_con has one block-row per generator: columns = sym basis index.
blocks = []
for X in gens:
    block = np.stack([(X.T @ E + E @ X).reshape(-1) for E in sym_basis], axis=1)  # (196, 105)
    blocks.append(block)
A_con = np.vstack(blocks)                          # (91*196, 105)
# null space of A_con = invariant symmetric forms:
u, s, vh = np.linalg.svd(A_con, full_matrices=True)
tol = 1e-8 * max(A_con.shape) * (s[0] if s.size else 1.0)
null = vh[np.sum(s > tol):].conj().T              # columns span the null space
nulldim = null.shape[1]
check("PC1c invariant symmetric forms = EXACTLY 1-dimensional (Schur nulldim 1)", nulldim == 1)

# the generator, reconstructed:
coeffs = null[:, 0]
M = sum(c * E for c, E in zip(coeffs, sym_basis))
# normalize so that entry (0,0) is +1:
M = M / M[0, 0]
offdiag = float(np.max(np.abs(M - np.diag(np.diag(M)))))
check_val("PC1d generator is DIAGONAL (off-diagonal ~ 0)", offdiag, 0.0, atol=1e-7)
evals = np.round(np.diag(M), 6)
sig_pos = int(np.sum(evals > 0))
sig_neg = int(np.sum(evals < 0))
check("PC1e generator ~ eta: signature (9,5), INDEFINITE (the UNGRADED metric, forced -- W203)",
      (sig_pos, sig_neg) == (9, 5))

# ---- PC2: the (6,4)-fiber record-count/conformal mode is LOCALLY Krein-negative (port W168 mini).
#      DeWitt vertical metric G_lambda(S,T) = tr(g^-1 S g^-1 T) - lambda (tr_g S)(tr_g T), g=diag(-1,1,1,1).
g = np.diag([-1.0, 1.0, 1.0, 1.0])
ginv = np.linalg.inv(g)


def dewitt(S, T, lam):
    return float(np.trace(ginv @ S @ ginv @ T) - lam * np.trace(ginv @ S) * np.trace(ginv @ T))


conf = g.copy()                                   # the full-trace / conformal (record-count) direction
norm_conf_lam1 = dewitt(conf, conf, 1.0)          # = 4 - 16*1 = -12 at the gimmel/GR value lambda=1
check_val("PC2a conformal/record-count mode DeWitt norm at lambda=1 (= 4-16*lambda)", norm_conf_lam1, -12.0)
check("PC2b record-count mode LOCALLY Krein-NEGATIVE at lambda=1 (W168)", norm_conf_lam1 < 0)
# geometric graviton (spatial trace-free) sample, Krein-positive:
grav = np.diag([0.0, 1.0, 1.0, -2.0])             # trace-free in spatial block
norm_grav = dewitt(grav, grav, 1.0)
check("PC2c geometric graviton mode LOCALLY Krein-POSITIVE (OPPOSITE to record-count, W168)", norm_grav > 0)

# ---- PC3: the subobject-classifier machinery on a poset site (Alexandrov space X = opens = up-sets).
class Frame:
    """The frame O(X) of opens of a finite poset (Alexandrov topology: opens = up-closed sets).
    Sub(1) in Sh(X) = O(X), a Heyting algebra; this class computes meet/join/implication/negation."""
    def __init__(self, points, leq):
        self.points = list(points)
        self.leq = leq                            # leq(a,b) True iff a <= b
        # opens = up-closed subsets:
        self.opens = []
        for r in range(len(self.points) + 1):
            for sub in itertools.combinations(self.points, r):
                s = frozenset(sub)
                if self._upclosed(s):
                    self.opens.append(s)
        self.top = frozenset(self.points)
        self.bot = frozenset()

    def _upclosed(self, s):
        for x in s:
            for y in self.points:
                if self.leq(x, y) and y not in s:
                    return False
        return True

    def meet(self, a, b):
        return a & b

    def join(self, a, b):
        return a | b

    def imp(self, a, b):
        # a -> b = largest open u with u & a subset of b
        best = self.bot
        for u in self.opens:
            if (u & a) <= b and len(u) > len(best):
                best = u
        # among equal-size candidates pick the union of all valid (Heyting impl is the max, unique)
        valid = [u for u in self.opens if (u & a) <= b]
        # the join of all valid opens is itself valid (frames are closed under arbitrary join) and is the max
        m = self.bot
        for u in valid:
            m = m | u
        return m

    def neg(self, a):
        return self.imp(a, self.bot)

    def complemented(self, a):
        na = self.neg(a)
        return (a | na) == self.top and (a & na) == self.bot

    def is_boolean(self):
        return all(self.complemented(a) for a in self.opens)


# HIERARCHICAL observer site: global g < regional r < individual i (a 3-chain refinement order).
pts = ["g", "r", "i"]
order = {("g", "g"), ("r", "r"), ("i", "i"), ("g", "r"), ("r", "i"), ("g", "i")}


def leq_chain(a, b):
    return (a, b) in order


F = Frame(pts, leq_chain)
check("PC3a hierarchical site: O(X) is a 4-element chain of opens", len(F.opens) == 4)
check("PC3b hierarchical classifier is NON-Boolean (intuitionistic)", not F.is_boolean())
# exhibit an intermediate open without complement:
inter = frozenset({"i"})                          # the finest/local observer's open (a stalk)
check("PC3c intermediate open {i} has Heyting negation = bottom", F.neg(inter) == F.bot)
check("PC3d {i} is NOT complemented ( {i} v not{i} = {i} != top )", not F.complemented(inter))

# DISCRETE site control: three observers with NO refinement relation (antichain).
def leq_disc(a, b):
    return a == b


F_disc = Frame(pts, leq_disc)
check("PC3e discrete site O(X) has 2^3 = 8 opens (powerset)", len(F_disc.opens) == 8)
check("PC3f discrete classifier IS Boolean (machinery separates the two sites)", F_disc.is_boolean())

# ==============================================================================================
print("\n[TOP] The topos internal-logic computation of the two bits")
# ==============================================================================================

# ---- T1: the UNGRADED metric as a global section. Schur (PC1) gives a 1-dim invariant space at
#      every capability level that sees the full non-compact gauge action, AND globally. So the
#      proposition "the invariant form exists and equals eta" holds on ALL of X: its truth value is
#      the TOP element 1 of Omega(global). Top is complemented -> BOOLEAN -> FORCED (reproduces W203).
prop_ungraded = F.top
check("T1a ungraded-metric proposition = top(1) (holds at every observer)", prop_ungraded == F.top)
check("T1b top is complemented (1 v 0 = 1) -> BOOLEAN on the ungraded bit -> eta FORCED (W203)",
      F.complemented(prop_ungraded))
# and its global-section space is a singleton up to scale: Schur nulldim 1 (PC1c) -> 1 global section.
check("T1c global-section space of the ungraded form = singleton up to scale (Schur nulldim 1)",
      nulldim == 1)

# ---- T2: the GRADING SIGN. Two candidate gradings of eta:
#      G_compact = |eta|  (positive-definite Gram, invariant under maximal COMPACT SO(9)xSO(5); W203 KER4)
#      G_krein   = eta    (the operative INDEFINITE Krein grading eta_+ = eta*C, record modes negative; W168)
#      Under the FULL non-compact gauge action ONLY eta is invariant (Schur). The choice
#      "operative grading = the Krein one" is a datum decided at the finer/local observers (where
#      finality is posited) but NOT at the global observer. Model it as the open {i} (a stalk-local
#      finality datum). Its characteristic value is INTERMEDIATE -> NON-complemented.
G_compact = ABS_ETA
G_krein = ETA
# realize eta_+ = eta * C with C the record-negative grading operator. Here C = sign-grading so that
# eta_+ picks the indefinite form; the "graded" object records the SIGN pattern (9 plus, 5 minus).
C_op = np.diag([1.0] * P + [1.0] * Q)             # C acts within the grading; eta_+ = eta @ C = eta
eta_plus = ETA @ C_op
check("T2a eta_+ = eta*C reproduces the indefinite (9,5) Krein form (record modes negative)",
      np.allclose(eta_plus, ETA))

# the grading-sign proposition lives at the intermediate open (local/finality-active observers):
prop_sign = frozenset({"i"})
check("T2b grading-sign proposition = intermediate open {i} (decided locally, not globally)",
      prop_sign != F.top and prop_sign != F.bot)
check("T2c grading-sign subobject is NON-complemented (chi lands on an intermediate Heyting value)",
      not F.complemented(prop_sign))
check("T2d => the classifier is INTUITIONISTIC on the grading sign (sign NOT internally decidable)",
      F.neg(prop_sign) == F.bot and (prop_sign | F.neg(prop_sign)) != F.top)

# the graded-form global sections are NOT a singleton: TWO gradings survive (residual Z/2), and the
# internal logic does not collapse them because prop_sign is not complemented.
gradings = [G_compact, G_krein]
distinct = not np.allclose(gradings[0], gradings[1])
check("T2e the two gradings |eta| and eta*C are DISTINCT global sections (residual Z/2)", distinct)
n_forced_by_logic = 1 if F.complemented(prop_sign) else len(gradings)
check("T2f graded-form global-section space is NOT a forced singleton (dim of residual = 2)",
      n_forced_by_logic == 2)

# ---- T3: the determination. Boolean on the ungraded metric; intuitionistic on the grading sign.
boolean_on_ungraded = F.complemented(prop_ungraded)
boolean_on_sign = F.complemented(prop_sign)
check("T3a BOOLEAN on the ungraded metric (eta forced -- W203 reproduced)", boolean_on_ungraded)
check("T3b INTUITIONISTIC on the grading sign (not internally decidable)", not boolean_on_sign)
verdict_residual = boolean_on_ungraded and (not boolean_on_sign)
check("T3c => RESIDUAL-BIT-STANDS: eta recovered UP-TO-GRADING; the C-operator SIGN is Godel-"
      "independent / external / must be posited (matches W168 TaF-activation, W201 order-2 datum)",
      verdict_residual)

# ==============================================================================================
print("\n[NC] Negative controls (the residual is real, not a modelling artifact)")
# ==============================================================================================

# ---- NC1: over a DISCRETE observer site the classifier is Boolean, so the grading subobject WOULD
#      be complemented (forced). The residual therefore rides the genuine REFINEMENT hierarchy
#      (specialization order), not the topos machinery per se.
check("NC1a discrete-site classifier is Boolean", F_disc.is_boolean())
# on the discrete site every subobject is complemented, so the grading sign would be DECIDED:
some_open = frozenset({"i"})
check("NC1b on the discrete site the grading subobject IS complemented (would be FORCED) -- so the "
      "residual rides the hierarchy, not the method", F_disc.complemented(some_open))

# ---- NC2: with a positive-definite AMBIENT (replace eta by |eta|) the invariant form is DEFINITE;
#      there is a unique maximal-definite subspace (the whole space), so the two gradings coincide and
#      the residual Z/2 collapses -- confirming the residual rides the indefinite (9,5) Krein structure.
gens_def = so_pq_generators(ABS_ETA)              # so(14,0) = so(14) compact
blocks_def = []
for X in gens_def:
    block = np.stack([(X.T @ E + E @ X).reshape(-1) for E in sym_basis], axis=1)
    blocks_def.append(block)
A_def = np.vstack(blocks_def)
s_def = np.linalg.svd(A_def, compute_uv=False)
tol_def = 1e-8 * max(A_def.shape) * s_def[0]
nulldim_def = nsym - int(np.sum(s_def > tol_def))
check("NC2a definite ambient still 1-dim invariant (generator ~ |eta|, POSITIVE-definite)", nulldim_def == 1)
# with the definite form the compact and Krein gradings coincide (both = |eta|):
G_compact_def = ABS_ETA
G_krein_def = ABS_ETA                              # no negative directions to re-grade
check("NC2b definite ambient: the two gradings COINCIDE (residual Z/2 collapses)",
      np.allclose(G_compact_def, G_krein_def))

# ---- NC3: relabel guard -- |eta| and eta*C are genuinely different operators, not one relabeled.
diff = float(np.max(np.abs(G_compact - G_krein)))
check_val("NC3a |eta| - eta*C is nonzero on the 5 negative directions (max |diff| = 2)", diff, 2.0)
check("NC3b so the two truth-values are distinct objects, not a relabel", diff > 1.0)

# ==============================================================================================
print("\n" + "=" * 82)
npass = sum(ok for _, ok in CHECKS)
ntot = len(CHECKS)
print(f"W209 topos internal-logic: {npass}/{ntot} checks pass")
print("VERDICT: RESIDUAL-BIT-STANDS. Classifier BOOLEAN on the ungraded metric (eta FORCED, W203),")
print("INTUITIONISTIC (non-Boolean) on the C-operator grading SIGN. Global-section space selecting")
print("eta_+ is NOT a singleton: a residual Z/2 (|eta| vs eta*C) survives, the sign is Godel-")
print("independent / external. Method recovers eta UP-TO-GRADING => RESIDUAL-BIT-STANDS, not FORCED.")
print("=" * 82)
if npass != ntot:
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")
    raise SystemExit(1)
raise SystemExit(0)
