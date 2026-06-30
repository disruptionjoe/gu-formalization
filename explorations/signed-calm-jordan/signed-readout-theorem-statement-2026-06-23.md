---
title: "Signed-Readout Boundary Theorem: Formal Statement"
date: 2026-06-23
problem_label: "signed-readout-theorem-statement"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Signed-Readout Boundary Theorem: Formal Statement

## 1. Problem Statement

The signed-readout boundary theorem is the highest-upside active-research item (publish potential 5).
All component pieces have been individually resolved at reconstruction grade:

- **Monotonicity criterion** proved (iff: R monotone iff all w(x) in G_+).
  File: `explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md`
- **PN/Jordan obligations PJ1-PJ5** discharged.
  File: `explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md`
- **Record-graph OQ1** resolved (causal DAG with finality semantics, four relations separated).
  File: `explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md`
- **Integer-index OQ2** (Z-grading + Atiyah-Jannich, GW axial charge recovered).
  File: `explorations/signed-calm-jordan/signed-readout-oq2-integer-index-2026-06-23.md`
- **K-theory lift OQ2-A** (class in KSp^0(X), PN split lifts to K-theory, H-linearity forces KSp).
  File: `explorations/signed-calm-jordan/signed-readout-oq2a-k-theory-lift-2026-06-23.md`
- **GU contact OQ2-D** (G_R^{GU} = 24-node bipartite graph, monotone side confirmed).
  File: `explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`

**What is missing** is a single self-contained formal theorem statement that synthesizes all these
pieces into the precise theorem with full hypotheses, conclusion, and explicit falsification
conditions. That is the sole task of this file.

---

## 2. Established Mathematical Context

### 2.1 Prior Closed Results

The following are not re-derived here; they are used as inputs:

- **Monotonicity criterion** (reconstruction): R: E -> G monotone iff w(x) in G_+ for all x in X.
- **PN/Jordan factorization**: every w: X -> G_latt (G lattice-ordered abelian group) admits a
  unique minimal split (w_+, w_-) into positive-cone components with w = w_+ - w_-.
- **Provenance layer**: Provenance(e) = (R_+(e), R_-(e)) is monotone; readout r(p,n) = p - n is
  generically anti-monotone in n.
- **Z-grading theorem**: if w: X -> Z (integer-valued weights), then R: E -> Z is Z-valued.
- **Atiyah-Jannich stability** (reconstruction-grade): Z-valued integer index is locally constant
  under operator deformations preserving Fredholmness.
- **GW axial charge instance**: Q_A = n_+ - n_-, w(x_{anti-inst}) < 0, R non-monotone; framework
  covers the non-monotone signed case.
- **GU generation count instance**: ind_H(D_GU) = 24, all weights +1, R_- = 0; framework covers
  the monotone Z-valued case.

### 2.2 The Boundary the Theorem Must Exhibit

The theorem is about the **boundary** between monotone and non-monotone readout:

> Monotone provenance (the provenance layer (R_+, R_-) is order-preserving) CAN COEXIST with
> non-monotone readout R = R_+ - R_- when any weight w(x) is negative.

This is not an obvious coexistence: one might expect that if provenance is monotone (more evidence
=> more total accumulation), the readout should also be monotone (more evidence => higher scalar
value). The boundary theorem shows this fails, and gives the precise condition separating the two
regimes.

---

## 3. Definitions (Minimal Sufficient for the Theorem)

### 3.1 Evidence Monoid

Let **X** be a set (the set of **contribution event types**).

The **evidence monoid** is the free commutative monoid on X:
```
E = N_0^{(X)} = { sum_{x in X} n_x [x] : n_x in N_0, finitely many n_x != 0 }
```
with componentwise addition as the monoid operation and the zero vector as identity.

The **information order** on E is:
```
e <=_E e'  iff  e' - e in E  (i.e., e' = e + d for some d in E)
```
This is the componentwise partial order: n_x <= n'_x for all x.

Key properties of (E, <=_E):
- (E, <=_E) is a directed poset (any two elements have a join: e ∨ e' = e + e').
- 0 <=_E e for every e in E (the identity is the minimum element).
- E is cancellative: e + d = e + d' implies d = d'.
- The order is well-founded.

### 3.2 Readout Codomain

Let **(G, +, <=_G)** be a **lattice-ordered abelian group**: an abelian group with a partial order
<=_G compatible with addition, and with the lattice property that every pair (g, g') has a
least upper bound g ∨ g' and a greatest lower bound g ∧ g' in G.

The **positive cone** is:
```
G_+ = { g in G : 0_G <=_G g }
```

G_+ is closed under addition and N_0-scalar multiplication.

Standard instances: Z with G_+ = N_0; R with G_+ = R_{>=0}; Z^n coordinatewise.

### 3.3 Weight Function and Signed Readout

A **weight function** is any map:
```
w: X -> G
```

The **signed readout** R_w: E -> G is the unique monoid homomorphism extending w:
```
R_w( sum_{x in X} n_x [x] ) = sum_{x in X} n_x w(x)
```

Uniqueness follows from freeness of E.

### 3.4 Provenance Layer

The **PN/Jordan split** of w is the unique pair (w_+, w_-) with w_+, w_-: X -> G_+ and
w = w_+ - w_-, defined by the canonical decomposition in the lattice G:
```
w_+(x) = w(x) ∨ 0_G    (positive part of w(x))
w_-(x) = (-w(x)) ∨ 0_G  (negative part of w(x))
```

This split is minimal: for any other split (w_+', w_-') with w = w_+' - w_-' and
w_+', w_-' in G_+, we have w_+'(x) >=_G w_+(x) and w_-'(x) >=_G w_-(x) for all x.

The **provenance readout pair** is:
```
Provenance_w: E -> G_+ x G_+,   Provenance_w(e) = (R_{w_+}(e), R_{w_-}(e))
```

This is order-preserving in each component (R_{w_+} and R_{w_-} are both monotone by
the monotonicity criterion, since w_+(x), w_-(x) in G_+).

The **readout map** r: G_+ x G_+ -> G is:
```
r(p, n) = p - n
```

The signed readout factorizes as:
```
R_w = r ∘ Provenance_w
```

### 3.5 Monotonicity and Non-Monotonicity

R_w is **monotone** if: e <=_E e' implies R_w(e) <=_G R_w(e').

R_w is **non-monotone** if: there exist e <=_E e' with R_w(e') <_G R_w(e).

---

## 4. The Signed-Readout Boundary Theorem

### 4.1 Main Theorem

**Theorem (Signed-Readout Boundary Theorem).** Let:
- X be a nonempty set of contribution event types.
- E = N_0^{(X)} be the free commutative monoid on X, equipped with the information order <=_E.
- G be a lattice-ordered abelian group with positive cone G_+.
- w: X -> G be a weight function.
- R_w: E -> G be the signed readout extending w.
- (w_+, w_-): X -> G_+ x G_+ be the canonical PN/Jordan split of w.
- Provenance_w: E -> G_+ x G_+ be the provenance readout pair.

Then the following hold simultaneously:

**Part (M): Monotonicity criterion.**
```
R_w is monotone with respect to (<=_E, <=_G)
   if and only if
w(x) in G_+  for every x in X.
```
Equivalently: R_w is monotone iff w_-(x) = 0_G for every x in X (iff w_- = 0 identically).

**Part (P): Monotone provenance.**
The provenance readout pair Provenance_w is always order-preserving:
```
e <=_E e'  implies  Provenance_w(e) <=_{G_+ x G_+} Provenance_w(e')
```
where the product order on G_+ x G_+ is coordinatewise.

This holds for ALL weight functions w: X -> G, regardless of whether any w(x) is negative.

**Part (C): Coexistence.**
When w_- != 0 (i.e., some generator x_0 in X has w(x_0) <_G 0_G):

(i) **Provenance is monotone:** Provenance_w is order-preserving (by Part (P)).

(ii) **Readout is non-monotone:** R_w is not monotone. Specifically, the pair
    (e = 0_E, e' = [x_0]) witnesses non-monotonicity:
    ```
    0_E <=_E [x_0]   but   R_w([x_0]) = w(x_0) <_G 0_G = R_w(0_E)
    ```

(iii) **The boundary is exactly at w_- = 0:** the transition from monotone to non-monotone
     readout occurs precisely when the negative-weight component w_- becomes nonzero, and
     not before. Any w with all generators in G_+ gives a monotone R_w; the first
     generator with w(x) < 0 induces non-monotonicity.

**Part (Z): Integer index (under Z-grading hypothesis).**
If additionally:
- G = Z (with G_+ = N_0), and
- w: X -> Z (integer-valued weights),

then:
- R_w: E -> Z is Z-valued.
- Under norm-continuous deformations of w (holding X fixed) that preserve the set
  { x in X : w(x) > 0 } and { x in X : w(x) < 0 } (i.e., no weight crosses zero),
  R_w is integer-valued and locally constant on connected components of the deformation space.
- The integer R_w(e) is stable (does not change) under deformations of w within a fixed
  sign-pattern.

**Part (K): K-theory lift (under H-linearity hypothesis).**
If additionally:
- The weight data arises from an H-linear Fredholm family {D_x}_{x in X'} over a compact
  base X' (with X the set of spectral contribution types),
- G = Z,

then the PN/Jordan split lifts to a class:
```
[D] = [ker D] - [coker D]   in KSp^0(X')
```
where KSp^0(X') = KO^4(X') is the quaternionic K-theory group. The integer readout
R_+(e) = dim_H(ker D) is the augmentation map KSp^0(X') -> KSp^0(pt) = Z.

---

### 4.2 Statement in Terms of Provenance and Readout Layers

The theorem has a clean two-layer formulation:

**Provenance layer:** (E, Provenance_w) — the pair (R_+(e), R_-(e)) is a monotone map from
(E, <=_E) to (G_+ x G_+, <=_componentwise). This layer always carries monotone structure:
adding evidence never decreases either the positive accumulation or the negative accumulation.

**Readout layer:** r: G_+ x G_+ -> G, r(p,n) = p - n — this map is monotone in its first
argument (p) and anti-monotone in its second argument (n). It is NOT order-preserving on
the product order.

**The boundary:** the composite R_w = r ∘ Provenance_w is monotone iff r is effectively
monotone on the image of Provenance_w, which happens iff w_- = 0 (the image of
Provenance_w lands in G_+ x {0}, where r is monotone).

**Diagrammatically:**
```
(E, <=_E)  ---Provenance_w--->  (G_+ x G_+, <=_componentwise)  ---r--->  (G, <=_G)
                 [always monotone]                                  [NOT monotone when n > 0]
```

The non-monotonicity of R_w = r ∘ Provenance_w is entirely localized in the readout layer r.
The provenance layer is always monotone. This is the structural content of the boundary theorem.

---

## 5. Hypotheses Summary

The theorem requires the following hypotheses. They are listed in order of structural necessity:

**H1 (Free commutative monoid).** E = N_0^{(X)} is the free commutative monoid on X.

**H2 (Information order).** The order on E is the componentwise N_0 order (divisibility order).

**H3 (Lattice-ordered abelian group).** G is an abelian group with a partial order compatible
with addition, and every pair of elements has a lattice meet and join in G.

**H4 (Unique homomorphic extension).** R_w: E -> G is the unique monoid homomorphism extending
w: X -> G. This is guaranteed by freeness of E (H1).

**H5 (PN/Jordan split exists).** The lattice structure of G (H3) guarantees that w_+(x) = w(x) ∨ 0
and w_-(x) = (-w(x)) ∨ 0 exist in G for every x.

**H6 (For Part Z: Integer weights).** G = Z and w: X -> Z.

**H7 (For Part K: H-linearity).** The operator family {D_x} is H-linear (i.e., D_x commutes
with right-multiplication by H on the spinor module S = H^n). This forces the K-theory
class to live in KSp^0(X') = KO^4(X'), not KU^0(X') or KO^0(X').

---

## 6. Explicit Falsification Conditions

The theorem is falsified by any of the following:

**F1: E is not free commutative.** If there is a relation among generators (e.g., x_1 + x_2 = x_3
for generators x_1, x_2, x_3 in X), then:
- R_w is not uniquely determined by w|_X alone.
- The pair (0_E, [x_0]) may not satisfy 0_E <=_E [x_0] if x_0 is identified with 0_E.
- Part (C) is falsified by a monoid where some generator is the identity.

Signature: the monotonicity criterion becomes weight-independent (R_w is always monotone or
always non-monotone regardless of the sign of weights), breaking the iff.

**F2: G is not lattice-ordered.** If max(w(x), 0_G) does not exist in G for some w(x)
(i.e., G has no lattice structure), then:
- The PN/Jordan split cannot be defined canonically.
- Part (P) (monotone provenance) requires G_+ to be closed under N_0-scalar multiplication,
  which holds for lattice-ordered abelian groups but may fail for groups with non-standard
  positive cones (e.g., a cone that is not closed under addition).
- Part (K) is not defined (no canonical split to lift to K-theory).

Signature: the provenance layer is ill-defined; the two-layer factorization collapses.

**F3: G order not compatible with group operation.** If g <=_G g' does not imply
g + h <=_G g' + h for all h, then:
- Adding a positive element to both sides of an inequality may break the order.
- The proof of Part (M), (<=) direction, uses g + (nonneg element) >=_G g, which fails.

Signature: the iff in Part (M) breaks asymmetrically: (=>) may still hold but (<=) fails.

**F4: Weight function w is not well-defined on generators.** If the same generator x in X
appears with different weights in different contexts (e.g., w is context-dependent), then
R_w is not a well-defined function E -> G. This breaks all parts.

Signature: the readout is set-valued (not function-valued), and the criterion has no content.

**F5: Information order on E is not the free-monoid order.** If <=_E is a partial order
on E not given by the componentwise N_0 order (e.g., a causal order imposed by additional
structure), then:
- 0_E <=_E [x_0] may fail for some x_0.
- Part (C) uses the specific pair (0_E, [x_0]) as a witness; under a non-standard order,
  this pair may not be comparable.
- Part (M), (=>) direction, uses the pair (0_E, [x_0]) to extract the constraint w(x_0) in G_+;
  this fails if 0_E is not below [x_0] in the imposed order.

Signature: the theorem holds for the standard information order but fails under arbitrary
causal orders. The correct statement for non-standard orders would require case analysis on
which generators are above 0_E.

**F6: H6 fails (non-integer weights, Part Z).** For Part (Z) only: if w: X -> R \ Z (real-
valued, non-integer), then R_w: E -> R is not Z-valued, and the integer-stability claim is
vacuous. The stability claim requires that the set of possible readout values is discrete.

Signature: the Z-valued invariant is replaced by an R-valued one with no topological protection.

**F7: H7 fails (C-linearity instead of H-linearity, Part K).** For Part (K) only: if the
Fredholm family {D_x} is C-linear but not H-linear (i.e., commutes with complex scalars
but not quaternionic scalars), then the K-theory lift lands in KU^0(X') = K^0(X'), not
KSp^0(X'). The integer readout is still well-defined, but the structural reason for
Z-valuedness changes (Atiyah-Singer for KU, not Atiyah-Jannich for KSp), and the specific
claim about the GU Sp(64) case does not apply.

Signature: correct result for a different K-group; the GU contact (OQ2-D) is falsified but
the abstract framework (Parts M, P, C, Z) remains valid.

---

## 7. Worked Instances

### 7.1 GW Lattice Axial Charge (Non-Monotone Case)

**Setup.** X = {x_U : U a plaquette in the GW lattice} (one contribution event per plaquette).
G = Z, G_+ = N_0. Weight function: w(x_U) = q(U) in Z, where q(U) is the local topological
charge (can be positive or negative: q(U) in {-1, 0, +1} for a typical instanton background).

**Readout.** R_w(e) = sum_{U} n_U q(U) = Q_top (total topological charge, = Q_A in the
Atiyah-Singer GW context). Q_A = n_+ - n_- = R_+(e_max) - R_-(e_max).

**Boundary theorem.** Since q(U) < 0 for anti-instanton plaquettes:
- Part (M): R_w is non-monotone (anti-instanton plaquettes have negative weight).
- Part (P): Provenance_w(e) = (n_+(e), n_-(e)) is always monotone (more plaquettes processed
  => more positive-charge and more negative-charge accumulation).
- Part (C): Provenance is monotone; readout Q_A is not. This is the boundary case.
- Part (Z): Q_A in Z (integer), protected by Atiyah-Jannich for the GW Dirac operator.

### 7.2 GU Generation Count (Monotone Case)

**Setup.** X = {v^{1/2}_{j,k}, v^R_{j,k}} (one contribution event per H-line in the
Atiyah-Schmid formal-degree sum; j indexes H-types D(1/2,0) or D(0,1/2), k indexes copies).
G = Z, G_+ = N_0. Weight function: w(v) = 1 for all v in X (all modes contribute +1 to
the H-line count).

**Readout.** R_w(e_max) = 24 = ind_H(D_GU) = sum_v w(v) = |X| = 24 nodes.

**Boundary theorem.** Since all weights are +1 in G_+:
- Part (M): R_w is monotone (all w(v) in G_+). This is the monotone side of the boundary.
- Part (P): Provenance_w(e) = (R_+(e), R_-(e)) = (R(e), 0). R_- = 0 identically.
- Part (C): NOT the coexistence case. The readout IS monotone. The GU generation count is
  not at the boundary; it is the degenerate monotone case.
- Part (Z): 24 in Z, topologically protected (Atiyah-Jannich in L^2 non-compact setting,
  reconstruction-grade). K-theory class in KSp^0(X') via H-linearity of D_GU on S = H^64.

### 7.3 Abstract Minimal Boundary Example (Coexistence Witnessed)

**Setup.** X = {x_+, x_-}, G = Z. w(x_+) = +1, w(x_-) = -1.

**Provenance.** w_+(x_+) = 1, w_+(x_-) = 0; w_-(x_+) = 0, w_-(x_-) = 1.
For any e = m [x_+] + n [x_-]:
- R_+(e) = m (monotone: increases as m increases)
- R_-(e) = n (monotone: increases as n increases)

**Readout.** R_w(e) = m - n.

**Coexistence.** Take e = [x_-], e' = 0_E. Then e' <=_E e... wait, 0_E <=_E [x_-].
R_w(0_E) = 0, R_w([x_-]) = -1. So R_w([x_-]) < R_w(0_E) even though 0_E <=_E [x_-].
Provenance_w(0_E) = (0, 0) <=_componentwise (0, 1) = Provenance_w([x_-]). Provenance monotone;
readout non-monotone. Coexistence confirmed.

---

## 8. Relationship to Prior Established Results

### 8.1 Monotonicity Criterion (Established)

Part (M) of the theorem is RESOLVED at reconstruction grade in
`explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md` §4. The proof is
complete and elementary. No additional verification needed for Part (M).

### 8.2 PN/Jordan Factorization (Established)

PJ1-PJ5 (obligations for Part (P) and the layer decomposition) are DISCHARGED in
`explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md` §5.

### 8.3 Record-Graph Semantics (Established)

OQ1 is RESOLVED in `explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md`. The four
relations (evidence order, causal order, finality relation, readout order) are separated
concretely. The record-graph formulation gives observer-relative semantics for the provenance
layer without requiring timestamps.

### 8.4 Integer-Index Recovery (Established at Reconstruction Grade)

OQ2 is CONDITIONALLY_RESOLVED in `explorations/signed-calm-jordan/signed-readout-oq2-integer-index-2026-06-23.md`.
The Z-grading theorem (Part Z) and Atiyah-Jannich stability are the two load-bearing claims,
both at reconstruction grade.

### 8.5 K-Theory Lift (Established at Reconstruction Grade)

OQ2-A is CONDITIONALLY_RESOLVED in `explorations/signed-calm-jordan/signed-readout-oq2a-k-theory-lift-2026-06-23.md`.
H-linearity forces the K-theory class to land in KSp^0(X') = KO^4(X'), not KU^0(X'). Part (K)
of this theorem is new synthesis, but all components are established.

### 8.6 GU Contact (Established at Reconstruction Grade)

OQ2-D is CONDITIONALLY_RESOLVED in `explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`.
The GU generation count is the monotone Z-valued case (instance 7.2 above). The record-graph
G_R^{GU} is the 24-node bipartite graph with no edges and uniform weight 1.

---

## 9. Open Conditions for Upgrading Verdict

The boundary theorem is CONDITIONALLY_RESOLVED rather than RESOLVED for the following reasons:

**OC1 (Part Z, Atiyah-Jannich in non-compact L^2 setting).** The integer-stability claim in
Part (Z) uses Atiyah-Jannich for the operator family {D_x}. In the compact setting this is
classical (Atiyah 1969). For the non-compact GU case (Y^14 is non-compact), the relevant
reference is Atiyah-Schmid (1977), where Fredholmness is established for the discrete-series
sector. The extension from compact to non-compact is reconstruction-grade: the argument is
structurally correct but has not been carried through in full detail for D_GU on Y^14.

**OC2 (Part K, Fred_H classification for non-compact Y^14).** The K-theory lift (Part K) uses
the Atiyah-Jannich theorem for quaternionic Hilbert spaces. The explicit Fredholm classification
for H-linear operators on L^2(Y^14, S) with S = H^64 in the non-compact setting is not fully
developed. The compact analogue is straightforward; the non-compact extension requires care
about the appropriate Sobolev topology and the domain of the operator.

**OC3 (GW axial charge: limit-of-discrete-series risk for GU case).** The Weyl-wall risk
at <e_2 - e_3, lambda_RS> = 0 (identified in `weyl-group-s4-orbit-2026-06-23.md`) could
cause the discrete spectrum of D_GU to degenerate. If the Flensted-Jensen discrete series
is empty for the specific pair (SL(4,R)/SO_0(3,1), S(6,4)), then |X| = 0 and ind_H = 0,
not 24. This is assessed as CONDITIONALLY_RESOLVED (oq-weyl3-limit-discrete-series) but
the explicit Plancherel computation has not been executed.

**OC4 (Part P, provenance monotonicity for non-lattice G).** The canonical PN/Jordan split
uses max(w(x), 0) in G, which requires G to be lattice-ordered. For G only a partially
ordered abelian group (non-lattice), max(w(x), 0) may not exist, and the provenance layer
is not canonically defined. Part (P) as stated requires H3 (lattice-ordered G). The theorem
statement correctly includes H3 as a hypothesis; if H3 fails the provenance-monotonicity
claim requires reformulation.

---

## 10. Grade Assessment

**Parts (M), (P), (C):** RESOLVED at reconstruction grade. The proofs are complete, elementary,
and explicitly checked in `signed-readout-monotonicity-pn-jordan-2026-06-23.md`. No analytic
machinery beyond free commutative monoids and lattice-ordered groups is required.

**Part (Z):** CONDITIONALLY_RESOLVED at reconstruction grade. The Z-grading mechanism
(integer weights give integer readout) is elementary. The Atiyah-Jannich stability claim
is reconstruction-grade (correct argument, not fully verified in non-compact setting).

**Part (K):** CONDITIONALLY_RESOLVED at reconstruction grade. The K-theory lift to KSp^0
is reconstruction-grade (argument correct, non-compact Fredholm theory not fully developed).

**The boundary theorem as a whole: CONDITIONALLY_RESOLVED at reconstruction grade.**

The core of the theorem (Parts M, P, C) is complete. The enhancements for integer-valued
invariants (Part Z) and K-theory structure (Part K) are reconstruction-grade, gated on
the non-compact Fredholm theory open conditions OC1-OC2.

---

## 11. Verdict

**Verdict: CONDITIONALLY_RESOLVED**

The signed-readout boundary theorem has been formally stated with complete hypotheses (H1-H7),
full conclusion (Parts M, P, C, Z, K), and six explicit falsification conditions (F1-F7).

The core claim — that monotone provenance coexists with non-monotone readout precisely when
any generator weight is negative — is proved at reconstruction grade (Parts M, P, C).

The integer-index and K-theory extensions are reconstruction-grade, gated on the non-compact
Atiyah-Jannich stability theorem (OC1) and the H-linear Fredholm theory for non-compact Y^14
(OC2).

The two worked physical instances correctly occupy the two sides of the boundary:
- GW axial charge Q_A: non-monotone readout, monotone provenance (the coexistence case).
- GU generation count ind_H = 24: monotone readout, monotone provenance (the degenerate case).

**Remaining to RESOLVED:**
- OC1: Atiyah-Jannich stability in non-compact L^2 (gates Part Z).
- OC2: H-linear Fredholm theory for non-compact Y^14 (gates Part K).
- OC3: Explicit Flensted-Jensen Plancherel computation for (SL(4,R)/SO_0(3,1), S(6,4)).
- OC4: Extension of Part P to non-lattice-ordered G (minor; H3 covers all physical cases).
