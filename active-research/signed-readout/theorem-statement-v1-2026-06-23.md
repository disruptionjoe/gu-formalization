---
title: "Signed-Readout Boundary Theorem: Formal Statement v1"
date: 2026-06-23
status: active_research
verdict: CONDITIONALLY_RESOLVED
source_explorations:
  - explorations/signed-calm-jordan/signed-readout-theorem-statement-2026-06-23.md
  - explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md
  - explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md
  - explorations/signed-calm-jordan/signed-readout-oq2-integer-index-2026-06-23.md
  - explorations/signed-calm-jordan/signed-readout-oq2a-k-theory-lift-2026-06-23.md
  - explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md
prior_art:
  - active-research/signed-readout/jordan-calm-formalization.md
  - active-research/signed-readout/gw-boundary-tests.md
  - active-research/signed-readout/historical-factorization-iff-theorem.md
  - active-research/signed-readout/signed-readout-verdict-2026-05-31.md
---

# Signed-Readout Boundary Theorem: Formal Statement v1

## 0. One-Line Summary

Monotone provenance coexists with signed (non-monotone) readout at the boundary: adding evidence
never decreases either the positive or negative accumulation, yet the scalar difference R_+ - R_-
can decrease under input growth. The precise boundary is w_- = 0 (every generator weight is
non-negative). This is the core claim, stated and proved below.

---

## 1. History and Scope

The signed-readout boundary theorem is the successor to three prior synthesis passes:

- **v1 (anomaly-iff):** "Q is CALM-monotone iff Q has no 't Hooft anomaly." Falsified: anomaly
  is neither necessary nor sufficient for CALM-class membership.
- **v2/v2.1 (factorization-iff):** Introduced the monotone-provenance / signed-readout layer
  split. The v3 unified verdict (PARTIAL) accepted the signed-readout monotonicity criterion as
  the primitive.
- **v3 (this theorem):** The signed-readout criterion stated as a formal theorem, with full
  hypotheses, five-part conclusion (M/P/C/Z/K), explicit falsification conditions, and two
  worked physical instances.

The theorem is not about CALM directly. It characterizes the boundary between monotone and
non-monotone scalar readout for any evidence-accumulation system, with CALM and Ginsparg-Wilson
as canonical physical instantiations.

---

## 2. Definitions

### 2.1 Evidence Monoid

Let **X** be a nonempty set (the **contribution event types**).

The **evidence monoid** is the free commutative monoid on X:

```
E = N_0^{(X)} = { sum_{x in X} n_x [x] : n_x in N_0, finitely many n_x nonzero }
```

with componentwise addition and 0 as identity.

The **information order** is:

```
e <=_E e'   iff   e' - e in E   (i.e., e' = e + d for some d in E)
```

This is the componentwise partial order: n_x <= n'_x for every x in X.

Key properties of (E, <=_E):
- (E, <=_E) is a directed poset: any two elements have a join e v e' = e + e'.
- 0 <=_E e for every e in E.
- E is cancellative.
- The order is well-founded.

### 2.2 Readout Codomain

Let **(G, +, <=_G)** be a **lattice-ordered abelian group**: an abelian group with a partial
order compatible with addition (g <=_G g' implies g+h <=_G g'+h for all h), and with meet and
join operations for every pair of elements.

The **positive cone** is:

```
G_+ = { g in G : 0_G <=_G g }
```

G_+ is closed under addition and N_0-scalar multiplication.

Standard instances: Z with G_+ = N_0; R with G_+ = R_{>=0}.

### 2.3 Weight Function and Signed Readout

A **weight function** is any map w: X -> G.

The **signed readout** R_w: E -> G is the unique monoid homomorphism extending w:

```
R_w( sum_{x in X} n_x [x] ) = sum_{x in X} n_x w(x)
```

Uniqueness follows from freeness of E (hypothesis H1 below).

### 2.4 PN/Jordan Split

The **PN/Jordan split** of w is the unique minimal pair (w_+, w_-) with w_+, w_-: X -> G_+ and
w = w_+ - w_-, defined by the canonical lattice decomposition:

```
w_+(x) = w(x) v 0_G     (positive part)
w_-(x) = (-w(x)) v 0_G  (negative part)
```

Minimality: for any other decomposition (u_+, u_-) with u_+, u_- in G_+^X and w = u_+ - u_-,
one has u_+(x) >=_G w_+(x) and u_-(x) >=_G w_-(x) for every x.

### 2.5 Provenance Layer

The **provenance readout pair** is:

```
Provenance_w: E -> G_+ x G_+,   Provenance_w(e) = (R_{w_+}(e), R_{w_-}(e))
```

The **readout map** is:

```
r: G_+ x G_+ -> G,   r(p, n) = p - n
```

The signed readout factorizes as:

```
R_w = r o Provenance_w
```

R_w is **monotone** if: e <=_E e' implies R_w(e) <=_G R_w(e').

R_w is **non-monotone** if: there exist e <=_E e' with R_w(e') <_G R_w(e).

---

## 3. Formal Hypotheses

**H1 (Free commutative monoid).** E = N_0^{(X)} is the free commutative monoid on X.

**H2 (Information order).** The order on E is the componentwise N_0 order.

**H3 (Lattice-ordered abelian group).** G is an abelian group with a lattice-compatible partial
order: addition is order-preserving, and every pair has a meet and join in G.

**H4 (Unique homomorphic extension).** R_w: E -> G is the unique monoid homomorphism extending
w: X -> G. Guaranteed by freeness (H1).

**H5 (PN/Jordan split exists).** The lattice structure of G (H3) guarantees w_+(x) = w(x) v 0
and w_-(x) = (-w(x)) v 0 exist in G for every x in X.

**H6 (For Part Z: Integer weights).** G = Z and w: X -> Z.

**H7 (For Part K: H-linearity).** The operator family {D_x}_{x in X'} is H-linear, i.e., D_x
commutes with right-multiplication by H on the spinor module S = H^n. This forces the K-theory
class into KSp^0(X') = KO^4(X'), not KU^0(X') or KO^0(X').

---

## 4. The Signed-Readout Boundary Theorem

**Theorem (Signed-Readout Boundary Theorem).** Under hypotheses H1-H5, let X be nonempty, let
E = N_0^{(X)} with the information order <=_E, let G be a lattice-ordered abelian group, let
w: X -> G be a weight function, and let (w_+, w_-) be the canonical PN/Jordan split of w.

Then the following five parts hold simultaneously.

---

### Part (M): Monotonicity Criterion

```
R_w is monotone with respect to (<=_E, <=_G)
   if and only if
w(x) in G_+  for every x in X.
```

Equivalently: R_w is monotone iff w_-(x) = 0_G for every x (iff w_- = 0 identically).

**Proof of (M).**

(=>) Suppose R_w is monotone. For any x_0 in X, consider the pair e = 0_E and e' = [x_0].
Then 0_E <=_E [x_0] (since [x_0] = 0_E + [x_0]). Monotonicity gives:

```
R_w(0_E) <=_G R_w([x_0])
0_G <=_G w(x_0)
```

So w(x_0) in G_+.

(<=) Suppose w(x) in G_+ for all x. For any e <=_E e', write e' = e + d with d in E. Then:

```
R_w(e') = R_w(e) + R_w(d) = R_w(e) + sum_x n_x^d w(x)
```

Since each w(x) in G_+ and each n_x^d >= 0, the sum sum_x n_x^d w(x) is in G_+. Therefore
R_w(e') >=_G R_w(e). Monotonicity holds. QED

---

### Part (P): Monotone Provenance (Universal)

The provenance readout pair Provenance_w is always order-preserving:

```
e <=_E e'  implies  Provenance_w(e) <=_{G_+ x G_+} Provenance_w(e')
```

with the coordinatewise order on G_+ x G_+. This holds for ALL weight functions w: X -> G,
regardless of the signs of the values w(x).

**Proof of (P).** Since w_+(x) in G_+ for all x (by definition of the positive part), Part (M)
applied to w_+ gives: R_{w_+} is monotone. Similarly, w_-(x) in G_+ for all x, so R_{w_-} is
monotone. Provenance_w(e) = (R_{w_+}(e), R_{w_-}(e)) is coordinatewise monotone. QED

---

### Part (C): Coexistence at the Boundary

When w_- != 0 (i.e., there exists x_0 in X with w(x_0) <_G 0_G):

**(i) Provenance is monotone:** Provenance_w is order-preserving (by Part (P)).

**(ii) Readout is non-monotone:** R_w is not monotone. The pair (0_E, [x_0]) witnesses
non-monotonicity:

```
0_E <=_E [x_0]   but   R_w([x_0]) = w(x_0) <_G 0_G = R_w(0_E)
```

**(iii) Boundary is exactly w_- = 0:** The transition from monotone to non-monotone readout
occurs precisely at the first generator with w(x) < 0. Any w with all generators in G_+ gives
monotone R_w; the first generator with w(x) <_G 0_G induces non-monotonicity.

**Proof of (C).** Part (i) follows from Part (P). Part (ii) is direct: 0_E <=_E [x_0] since
[x_0] = 0_E + [x_0]; R_w(0_E) = 0_G; R_w([x_0]) = w(x_0) <_G 0_G by assumption; therefore
R_w([x_0]) <_G R_w(0_E) with 0_E <=_E [x_0]. Part (iii) is the combination of (M) and (ii).
QED

---

### Part (Z): Integer-Index Stability (under H6)

Under the additional hypothesis H6 (G = Z, w: X -> Z):

- R_w: E -> Z is Z-valued and integer-valued.
- Under deformations of w (holding X fixed) that preserve the sign pattern
  {x in X : w(x) > 0} and {x in X : w(x) < 0} (no weight crosses zero), R_w(e) is locally
  constant on connected components of the deformation space.
- The integer R_w(e) is topologically protected against deformations within a fixed sign-pattern.

**Mechanism.** The integer-valuedness is immediate from w: X -> Z and the homomorphic extension.
Stability follows because deformations preserving the sign partition preserve the set of
generators contributing to R_+ and R_- respectively; R_w(e) = R_+(e) - R_-(e) is constant as
long as no weight crosses zero (no generator switches between positive-cone and negative-cone).
Under norm-continuous deformations with fixed sign-pattern, R_w(e) in Z cannot vary continuously
except by jumping, but it also cannot jump since no weight crosses zero. Hence it is constant.

**Physical instance.** For the GW axial charge Q_A = n_+ - n_- in Z: integer stability is the
Atiyah-Jannich theorem for the family of GW Dirac operators. The integer n_+ - n_- is constant
under deformations of the gauge field that do not change the number of zero modes (do not cross
eigenvalue zero). This is the standard statement of index stability.

---

### Part (K): K-Theory Lift (under H7)

Under the additional hypothesis H7 (H-linear Fredholm family {D_x}_{x in X'} over compact X'):

- The PN/Jordan split lifts to a class in quaternionic K-theory:

```
[D] = [ker D] - [coker D]   in KSp^0(X') = KO^4(X')
```

where KSp^0(X') is the quaternionic K-theory group of the base X'.

- The integer readout R_+(e_max) = dim_H(ker D) is the augmentation map:

```
aug: KSp^0(X') -> KSp^0(pt) = Z
```

- H-linearity (H7) is the forcing condition: a C-linear Fredholm family lifts to KU^0(X') = K^0(X');
  H-linearity forces the lift to KSp^0(X') = KO^4(X'), a strictly finer invariant.

**Why H-linearity forces KSp.** The right-H-module structure on S = H^n commutes with D_x
(H7). This means D_x is H-linear, not merely C-linear. The Atiyah-Jannich theorem for
quaternionic Hilbert spaces then classifies the family {D_x} by a class in KSp^0(X').
The forgetful map KSp^0(X') -> KU^0(X') is generally non-injective; H-linearity carries
strictly more information.

**Physical instance (GU generation count).** The GU Dirac operator D_GU acts on S = H^64
(from Cl(9,5) ~ M(64,H)). H-linearity is exact: Cl(9,5) acts on the left, H acts on the
right, and these commute. The family {D_GU} parameterized by gauge field A gives a class
[D_GU] in KSp^0(X') with dim_H(ker D_GU) = 24 at the section pullback level (reconstruction
grade, gated on OC1-OC2 below).

---

## 5. Two-Layer Diagram

The theorem has a clean two-layer formulation:

```
(E, <=_E)  ---Provenance_w--->  (G_+ x G_+, <=_componentwise)  ---r--->  (G, <=_G)
                 [ALWAYS monotone: Part (P)]             [NOT monotone when R_{w_-}(e) > 0]
```

The non-monotonicity of R_w = r o Provenance_w is entirely localized in the readout map r.
The provenance layer is always monotone. The boundary is:

```
R_w monotone  iff  r is effectively monotone on Im(Provenance_w)
              iff  Im(Provenance_w) is contained in G_+ x {0}
              iff  w_- = 0 identically   [Part (M)]
```

---

## 6. Formal Hypotheses Summary and Explicit Falsification Conditions

### 6.1 Hypotheses (recap)

H1: E = N_0^{(X)} (free commutative monoid)
H2: <=_E is the componentwise N_0 order
H3: G is a lattice-ordered abelian group
H4: R_w is the unique homomorphic extension of w (follows from H1)
H5: PN/Jordan split exists (follows from H3)
H6 (Part Z only): G = Z, w: X -> Z
H7 (Part K only): operator family is H-linear

### 6.2 Falsification Conditions

**F1: E is not free commutative.** If generators satisfy a relation (e.g., x_1 + x_2 = x_3 in
the monoid), then R_w is not uniquely determined by w|_X. The witness pair (0_E, [x_0]) for
Part (C) fails if x_0 is identified with 0_E. The iff in Part (M) breaks.

Signature: the monotonicity criterion becomes weight-independent; the iff has no content.

**F2: G is not lattice-ordered.** If max(w(x), 0_G) does not exist in G for some w(x), the
canonical PN/Jordan split is not defined. Part (P) (provenance monotonicity) and Part (K)
require G_+ to be an additive monoid, which holds for lattice-ordered groups but not
arbitrary ordered groups.

Signature: the provenance layer is ill-defined; the two-layer factorization collapses.

**F3: G order not compatible with group operation.** If g <=_G g' does not imply g+h <=_G g'+h,
the proof of Part (M), (<=) direction fails: R_w(e') = R_w(e) + R_w(d) >= R_w(e) uses this
compatibility.

Signature: the iff breaks asymmetrically; (=>) may hold but (<=) fails.

**F4: Weight function w is context-dependent.** If the same generator x in X has different
weights in different contexts, R_w is not a well-defined function E -> G. All parts fail.

Signature: the readout is set-valued; the criterion has no content.

**F5: <=_E is not the free-monoid order.** If <=_E is a partial order on E not given by
componentwise N_0 (e.g., a causal order with additional constraints), then 0_E <=_E [x_0] may
fail for some x_0. Part (C) uses this pair as the explicit witness; Part (M), (=>) direction
uses it to extract w(x_0) in G_+. Under a non-standard order, the criterion may still hold
but the proof requires case analysis on which generators are above 0_E.

Signature: the theorem holds for the standard information order; fails for arbitrary causal
orders without case analysis.

**F6 (Part Z): Non-integer weights.** If w: X -> R \ Z, then R_w: E -> R and the integer-
stability claim (local constancy on connected components) is vacuous. The set of possible
readout values is R, not Z; there is no discrete protection.

Signature: the Z-valued invariant is replaced by an R-valued one with no topological
protection.

**F7 (Part K): C-linearity instead of H-linearity.** If {D_x} is C-linear but not H-linear,
the K-theory lift lands in KU^0(X') = K^0(X'), not KSp^0(X'). The integer readout is still
defined, but the structural constraint forcing KSp does not apply. The GU Sp(64) contact
(OQ2-D) is not supported.

Signature: correct K-theory invariant for a different group; GU contact breaks.

---

## 7. Worked Physical Instances

### 7.1 GW Lattice Axial Charge: Non-Monotone Side of the Boundary

**Setup.**
- X = {x_U : U a plaquette in the GW lattice}
- G = Z, G_+ = N_0
- w(x_U) = q(U) in {-1, 0, +1} (local topological charge; negative for anti-instanton plaquettes)

**Readout.** R_w(e) = sum_U n_U q(U) = Q_top (total topological charge = Q_A in the GW context).
Q_A = n_+ - n_- by the Atiyah-Singer index theorem for the GW Dirac operator.

**Boundary theorem application.**

Since some w(x_U) < 0 (anti-instanton plaquettes), Part (C) applies:
- Part (P): Provenance_w(e) = (n_+(e), n_-(e)) is always monotone. More plaquettes processed
  implies more positive-charge and more negative-charge accumulation.
- Part (C)(ii): R_w is non-monotone. Adding an anti-instanton plaquette x_U with q(U) = -1
  to any evidence state e gives R_w(e + [x_U]) = R_w(e) - 1 < R_w(e), with e <=_E e + [x_U].
- Part (Z): Q_A in Z, topologically protected by Atiyah-Jannich stability for the GW Dirac
  operator family (integer n_+ - n_- locally constant under deformations preserving Fredholmness).

**Conclusion.** The GW axial charge is the canonical physical instance of coexisting monotone
provenance and non-monotone readout.

### 7.2 GU Generation Count: Monotone Side of the Boundary

**Setup.**
- X = {v_{j,k}} (one event per H-line in the formal-degree sum; j indexes H-types D(1/2,0)
  or D(0,1/2), k indexes copies; |X| = 24 via the APS/K3 route only (reconstruction grade,
  gated on OQ-RK1); the Flensted-Jensen discrete-series route is explicitly FAILED —
  SL(4,R) has no discrete series (rank(G)=3 != rank(K)=2; Harish-Chandra criterion fails),
  so the Atiyah-Schmid formal-degree sum is an empty sum; all four tau-twisted rescue routes
  also fail independently (Kobayashi non-admissibility, Oshima-Matsuki correction, split-rank
  mismatch A3 vs BC1, and vanishing formal degree); |X| = 24 is supported only by the APS/K3
  computation ind_H = 8*A-hat(K3) + 8 = 24, conditional on rank_H(S_RS^+) = 4 (GEN-01 OPEN))
- G = Z, G_+ = N_0
- w(v) = +1 for all v in X (each mode contributes +1 to the H-line count)

**Readout.** R_w(e_max) = 24 = ind_H(D_GU) (the quaternionic index of the GU Dirac operator,
counting 16 spin-1/2 H-lines + 8 RS H-lines under the K3-type vacuum selection).

**Boundary theorem application.**

Since all w(v) = +1 in G_+, Part (M) applies in the monotone direction:
- Part (M): R_w is monotone. Adding any evidence increases the readout.
- Part (P): Provenance_w(e) = (R_w(e), 0). The negative component R_{w_-} = 0 identically.
- Part (C): NOT the coexistence case. The GU generation count is on the monotone side of the
  boundary. This is the degenerate case w_- = 0.
- Part (Z): 24 in Z. Topologically protected by Atiyah-Jannich stability for the H-linear
  Fredholm family {D_GU} (reconstruction grade, gated on OC1-OC2).
- Part (K): The K-theory class [D_GU] in KSp^0(X') with H-linearity from Cl(9,5) ~ M(64,H).
  dim_H(ker D_GU) = 24 is the augmentation KSp^0(X') -> Z (reconstruction grade, gated on OC2).

**Conclusion.** The GU generation count is the monotone Z-valued case with w_- = 0 identically.
It is not at the boundary; the coexistence phenomenon does not arise.

### 7.3 Minimal Abstract Boundary Instance (Coexistence Witnessed)

**Setup.** X = {x_+, x_-}, G = Z. w(x_+) = +1, w(x_-) = -1.

**PN/Jordan split:** w_+(x_+) = 1, w_+(x_-) = 0; w_-(x_+) = 0, w_-(x_-) = 1.

**Provenance.** For e = m [x_+] + n [x_-]:
- R_{w_+}(e) = m (monotone)
- R_{w_-}(e) = n (monotone)

**Readout.** R_w(e) = m - n.

**Coexistence.** Take e = 0_E, e' = [x_-]. Then 0_E <=_E [x_-] (since [x_-] = 0_E + [x_-]).
- Provenance: Provenance_w(0_E) = (0, 0) <=_componentwise (0, 1) = Provenance_w([x_-]). Monotone.
- Readout: R_w(0_E) = 0, R_w([x_-]) = -1. So R_w([x_-]) < R_w(0_E) with 0_E <=_E [x_-]. Non-monotone.

Coexistence confirmed in the minimal case with |X| = 2.

---

## 8. Link to Prior Results and Open Conditions

### 8.1 What is RESOLVED (reconstruction grade)

- **Parts (M), (P), (C):** Complete proofs above. No analytic machinery beyond free commutative
  monoids and lattice-ordered groups is required. The proofs are elementary and fully explicit.
- **Part (Z), integer-valuedness:** Immediate from the homomorphic extension property.
- **Part (Z), stability mechanism:** The discreteness of Z forces local constancy under
  continuous deformations preserving the sign pattern.

### 8.2 What is CONDITIONALLY_RESOLVED (reconstruction grade)

- **Part (Z), Atiyah-Jannich stability in GU non-compact setting.** The integer-stability claim
  for D_GU on Y^14 (non-compact) uses Atiyah-Schmid (1977) for the discrete-series sector and
  the APS route on K3-type X^4. The compact case is classical. The non-compact extension is
  reconstruction-grade: the argument is structurally correct but not fully verified in detail
  for D_GU on Y^14.

- **Part (K), H-linear Fredholm theory for non-compact Y^14.** The K-theory lift for the full
  non-compact GU family requires a Fredholm classification for H-linear operators on L^2(Y^14, S).
  Compact analogue is classical (Atiyah-Jannich 1969, quaternionic case). Non-compact extension
  requires Sobolev topology care and domain analysis.

- **GU generation count (OC3).** The Weyl-wall risk at <e_2 - e_3, lambda_RS> = 0 could cause
  degeneration of the discrete spectrum of D_GU. If the Flensted-Jensen discrete series is empty
  for (SL(4,R)/SO_0(3,1), S(6,4)), then |X| = 0 and ind_H = 0. The OQ-weyl-3 root-wall check
  ran (2026-06-23): the A3 formal-degree product does not vanish at lambda_RS, removing the zero-
  factor objection, but the explicit Plancherel computation for the full spectrum has not been
  executed at verified grade.

### 8.3 Open Conditions for Upgrading to RESOLVED

**OC1 (Part Z, Atiyah-Jannich non-compact).** Full Atiyah-Jannich stability theorem for H-linear
operator families on non-compact Y^14 in the L^2 Sobolev setting. Reference: Atiyah-Schmid (1977)
for the discrete-series sector; APS (1975-76) for the boundary framework.

**OC2 (Part K, H-linear Fredholm on Y^14).** Explicit Fredholm classification for D_GU on
L^2(Y^14, S) with S = H^64. Gates G1 (Sobolev domain), G2 (KK zero-mode unitarity, CONDITIONALLY
RESOLVED 2026-06-23), G3 (bounded-transform continuity in Fred_H), G4 (APS eta Lorentzian).

**OC3 (GU generation count Plancherel explicit computation).** Verified-grade computation of
the Flensted-Jensen multiplicity for (SL(4,R)/SO_0(3,1), S(6,4)) including the full Plancherel
measure at the lambda_RS spectral parameter.

**OC4 (Part P, non-lattice G).** If G is only a partially ordered abelian group (not lattice-
ordered), the canonical PN/Jordan split may not exist. Part (P) requires H3. For G = Z or G = R,
H3 holds automatically; for non-standard readout groups, this must be verified separately.

---

## 9. Grade Assessment

| Part | Grade | Note |
|---|---|---|
| (M) Monotonicity criterion | RESOLVED (reconstruction) | Elementary proof; complete above |
| (P) Monotone provenance | RESOLVED (reconstruction) | Immediate from (M) applied to w_+ and w_- |
| (C) Coexistence | RESOLVED (reconstruction) | Explicit witness pair (0_E, [x_0]) |
| (Z) Integer-index stability | CONDITIONALLY_RESOLVED | Atiyah-Jannich non-compact (OC1) |
| (K) K-theory lift | CONDITIONALLY_RESOLVED | H-linear Fredholm on Y^14 (OC2) |
| GW instance | RESOLVED (reconstruction) | Standard lattice QFT |
| GU instance | CONDITIONALLY_RESOLVED | OC1, OC2, OC3 outstanding |

**Overall verdict: CONDITIONALLY_RESOLVED**

The core theorem (Parts M, P, C) is complete at reconstruction grade with full proofs. The integer-
index and K-theory enhancements are reconstruction-grade, gated on the non-compact Atiyah-Jannich
stability theorem (OC1) and H-linear Fredholm theory for non-compact Y^14 (OC2).

---

## 10. Publication Path

The theorem as stated (Parts M, P, C) is complete enough for a short mathematical paper at the
level of a note or letter. Target venues include:

- **TCS:** Logical Methods in Computer Science (LMCS) or Theory of Computing (ToC) -- the
  CALM/distributed-systems motivation connects directly.
- **Mathematical physics:** Letters in Mathematical Physics -- the GW and GU physical instances
  provide application.

The most publishable standalone unit is Parts (M)+(P)+(C) together with the GW axial charge
corollary (Section 7.1). The K-theory lift (Part K) and GU generation count (Section 7.2) are
enhancements conditional on OC1-OC2.

The paper title from v2.1/v3: "Monotone Provenance, Non-Monotone Readout: A Boundary Theorem
for the CALM / Ginsparg-Wilson Analogy."
