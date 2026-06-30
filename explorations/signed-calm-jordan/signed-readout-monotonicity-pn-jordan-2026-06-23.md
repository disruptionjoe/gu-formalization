---
title: "Signed-Readout Monotonicity Criterion: Proof and PN/Jordan Factorization Obligation"
date: 2026-06-23
problem_label: "signed-readout-monotonicity"
status: reconstruction
verdict: RESOLVED
---

# Signed-Readout Monotonicity Criterion: Proof and PN/Jordan Factorization Obligation

## 1. Problem Statement

The signed-readout boundary theorem is the highest-upside active-research item in the repo (publish potential 5). Its core claim is:

> Monotone provenance can coexist with non-monotone, signed, phase-sensitive, or cancellation-bearing readout.

Two open obligations from NEXT-STEPS.md drive this computation:

1. **Prove the monotonicity criterion** — the precise iff characterizing when the scalar readout R: E -> G is monotone in the information order on E.
2. **State the PN/Jordan factorization obligation** for the signed-readout boundary theorem — the exact algebraic structure that separates the provenance layer (monotone) from the readout layer (possibly non-monotone).

These obligations are stated in `active-research/signed-readout/signed-readout-verdict-2026-05-31.md` as the corrected theorem spine for the boundary theorem, superseding the earlier anomaly-iff claim. This file provides a complete proof and canonical statement at reconstruction grade.

---

## 2. Established Context

Prior work this builds on:

- `active-research/signed-readout/signed-readout-verdict-2026-05-31.md` (v2.1): the corrected theorem spine, evidence monoid and signed-readout definitions, proof sketch, PN/Jordan replacement structure named.
- `active-research/signed-readout/historical-factorization-iff-theorem.md` (v3): the unified factorization iff theorem synthesizing v2 (PCP/Jordan lens) and v2.1 (signed-readout direct criterion).
- `active-research/signed-readout/jordan-calm-formalization.md` (01): Jordan-decomposed signed-CALM (JD-CALM) with explicit J1–J4 conditions; GW axial-charge admissibility check.
- `active-research/signed-readout/gw-boundary-tests.md` (03): full bridge-test table; the integer-index bridge fails under all three frameworks; the signed-real bridge survives under JD-CALM and AC-CALM.
- `active-research/signed-readout/verdict-and-walkthrough-packet.md` (05): layer-split verdict confirmed 5/5 personas.
- `explorations/time-as-finality-crosswalk/rate-independence-negative-finding-2026-06-22.md`: the signed-readout monotonicity criterion is rate-independent (closed finding; do not re-run).
- `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md`: specification for a record-graph test; success criteria and failure conditions stated.

The v2.1 signed-readout criterion is the load-bearing mathematical primitive. The v3 factorization iff places it in the broader architecture. This file supplies the missing proof and the canonical PN/Jordan obligation statement.

---

## 3. Definitions

### 3.1 Evidence Monoid

Let E be the **free commutative monoid** on a generating set X of local contribution events. Concretely:

```
E = { finite formal sums  sum_i n_i x_i : x_i in X, n_i in N_0 }
```

with componentwise addition as the monoid operation and identity 0.

Equip E with the **information order**:

```
e <= e'  iff  e' = e + d for some d in E
```

This is the standard divisibility order on the free commutative monoid. It is a partial order (reflexive, transitive, antisymmetric), and (E, <=) is a join-semilattice with join e ∨ e' = e + e' (in the free commutative monoid, two elements always have a least upper bound equal to their sum).

Key properties:
- E is cancellative: e + d = e + d' implies d = d'.
- The information order is well-founded: any descending chain stabilizes (each element has finite support in X).
- Every element of E is a finite join of generators: e = x_{i_1} + ... + x_{i_k}.

### 3.2 Ordered Abelian Group and Positive Cone

Let (G, +, <=_G) be an **ordered abelian group**: G is an abelian group with a total or partial order <=_G compatible with addition (g <= g' implies g + h <= g' + h for all h). The **positive cone** is:

```
G_+ = { g in G : 0 <=_G g }
```

G_+ satisfies:
- G_+ + G_+ subset G_+ (closed under addition),
- G_+ ∩ (-G_+) = {0} (non-degeneracy when the order is strict),
- G_+ ∪ (-G_+) = G when the order is total.

Standard examples: G = Z with G_+ = N_0; G = R with G_+ = R_{>=0}; G = R^n with G_+ = R_{>=0}^n (coordinatewise).

### 3.3 Weight Function and Scalar Readout

Let w: X -> G be a **weight function** assigning each generator x in X a signed element w(x) in G. Extend w to a **scalar readout** R: E -> G by:

```
R(sum_i n_i x_i) = sum_i n_i w(x_i)
```

This extension is the unique group homomorphism E -> G (as abelian groups) extending w from the generators. It is well-defined and unique because E is free commutative.

R is **monotone** with respect to the information order on E and the group order on G if:

```
e <=_E e' implies R(e) <=_G R(e')
```

---

## 4. Proof of the Signed-Readout Monotonicity Criterion

**Theorem (Signed-Readout Monotonicity Criterion).** Let E, X, G, G_+, w, R be as in Section 3. Then:

```
R is monotone (e <=_E e' => R(e) <=_G R(e'))
   if and only if
w(x) in G_+ for every generator x in X.
```

**Proof.**

(=>) Direction: Assume R is monotone. Let x in X be any generator. Consider the pair e = 0 (the identity) and e' = x (the generator). Then:

```
0 <=_E x
```

because x = 0 + x = 0 + d with d = x in E, satisfying the definition of the information order.

Monotonicity of R gives:

```
R(0) <=_G R(x).
```

Since R is a group homomorphism and 0 is the identity of E:

```
R(0) = 0_G (the identity of G).
```

Therefore:

```
0_G <=_G R(x) = w(x),
```

which means w(x) in G_+. Since x was arbitrary, every generator has nonnegative weight.

(<=) Direction: Assume w(x) in G_+ for every generator x. Let e <=_E e'. By definition of the information order, e' = e + d for some d in E. Write d = sum_j m_j x_j (a finite sum with m_j in N_0 and x_j in X). Then:

```
R(e') = R(e + d) = R(e) + R(d)    [R is a homomorphism]
       = R(e) + sum_j m_j w(x_j).
```

Since w(x_j) in G_+ for each j, and m_j >= 0, and G_+ is closed under addition and under multiplication by N_0 (since n * g = g + g + ... + g (n times) for g in G_+ gives an element of G_+), we have:

```
sum_j m_j w(x_j) in G_+.
```

Therefore:

```
R(e') = R(e) + (something in G_+),
```

so by the defining property of the order (adding a nonnegative element does not decrease):

```
R(e) <=_G R(e').
```

Since e <=_E e' was arbitrary, R is monotone. QED.

**Remark on tightness.** The proof uses only:
- That E is a free commutative monoid (freeness gives the factorization e' = e + d; commutativity gives well-defined sums; the extension is unique).
- That G is an ordered abelian group (N_0-module structure on G_+ is needed in the (<=) direction).
- That R is the unique monoid homomorphism extending w.

No topology, no measure theory, no lattice theory beyond order theory is required.

**Corollary (Failure Mode).** R is non-monotone if and only if there exists a generator x in X with w(x) not in G_+. In that case, the information-order pair (0, x) witnesses the failure: R(0) = 0_G and R(x) = w(x) <_G 0_G, so R(x) <_G R(0) even though 0 <=_E x.

---

## 5. The PN/Jordan Factorization Obligation

### 5.1 Statement of the Obligation

The PN/Jordan factorization obligation for the signed-readout boundary theorem is as follows.

**Definition (PN/Jordan Factorization).** A weight function w: X -> G admits a PN/Jordan factorization if there exist two functions:

```
w_+ : X -> G_+     (positive part)
w_- : X -> G_+     (negative part, nonnegative-valued)
```

such that:

```
w(x) = w_+(x) - w_-(x)   for every x in X.
```

Extend to readouts:

```
R_+(e) = sum_i n_i w_+(x_i)    (monotone, nonneg-valued)
R_-(e) = sum_i n_i w_-(x_i)    (monotone, nonneg-valued)
R(e)   = R_+(e) - R_-(e)        (signed, possibly non-monotone)
```

**Obligation Statement.** For the signed-readout boundary theorem to achieve its stated goal:

> monotone provenance can coexist with non-monotone, signed readout

the theorem MUST exhibit the PN/Jordan factorization explicitly. Specifically, the obligation is:

(PJ1) **Existence of factorization.** For every weight function w: X -> G, exhibit an explicit PN/Jordan split (w_+, w_-) with w_+(x), w_-(x) in G_+ and w = w_+ - w_-.

(PJ2) **Monotonicity of components.** Show that R_+ and R_- are both monotone (both satisfy the monotonicity criterion from Theorem 4).

(PJ3) **Non-monotonicity of composite.** Show that R = R_+ - R_- can be non-monotone even when R_+ and R_- are each monotone. Exhibit an explicit example.

(PJ4) **Provenance layer identification.** Identify the provenance layer as the pair (E, (R_+, R_-)) with the information order; the readout layer as the scalar map r: G_+ x G_+ -> G, (p, n) |-> p - n. Show that the provenance layer is a monotone structure (both components increase under <=_E) while the readout layer is generically non-monotone (p - n can decrease even as p and n individually increase).

(PJ5) **Minimal split.** Among all PN/Jordan factorizations (w_+, w_-), there exists a canonical **minimal split** given by:

```
w_+(x) = max(w(x), 0_G)   (positive part)
w_-(x) = max(-w(x), 0_G)  (negative part)
```

where max is taken in the order of G. This is the standard Jordan-Hahn decomposition of a signed function into its positive and negative parts. Minimality means: for any other split (w_+', w_-') with w = w_+' - w_-', one has w_+'(x) >= w_+(x) and w_-'(x) >= w_-(x) for all x (they are "larger" in both components). The minimal split is the unique one with w_+ and w_- mutually singular (disjoint supports in the ordered-group sense: w_+(x) > 0 => w_-(x) = 0 and vice versa).

### 5.2 Discharge of Obligations PJ1–PJ5

**PJ1 (Existence).** Given any w: X -> G, define:
```
w_+(x) = max(w(x), 0_G)
w_-(x) = max(-w(x), 0_G) = max(0_G - w(x), 0_G)
```

Then w_+(x), w_-(x) >= 0_G (both in G_+), and:
```
w_+(x) - w_-(x) = max(w(x), 0) - max(-w(x), 0) = w(x)
```

(standard identity for signed decomposition). Obligation PJ1 is discharged.

**PJ2 (Monotonicity of components).** For all x in X, w_+(x) in G_+ and w_-(x) in G_+. Therefore by the Monotonicity Criterion (Section 4, (<=) direction), both R_+ and R_- are monotone. Obligation PJ2 is discharged.

**PJ3 (Non-monotonicity of composite).** Worked example: let X = {x_1, x_2}, G = Z, G_+ = N_0. Set w(x_1) = +1 and w(x_2) = -1. Then w_+(x_1) = 1, w_+(x_2) = 0, w_-(x_1) = 0, w_-(x_2) = 1.

Consider e = 0 and e' = x_2. Then 0 <=_E x_2 (information order).

R_+(0) = 0 <= R_+(x_2) = 0. (Monotone, equality.)
R_-(0) = 0 <= R_-(x_2) = 1. (Monotone, strictly increasing.)
R(0) = 0 and R(x_2) = -1. So R(x_2) < R(0) even though 0 <=_E x_2.

R is non-monotone. Both components are individually monotone. Obligation PJ3 is discharged.

**PJ4 (Provenance layer identification).** Define:

```
Provenance(e) = (R_+(e), R_-(e)) : E -> G_+ x G_+
```

The map Provenance is monotone componentwise: for e <=_E e', both R_+(e) <=_G R_+(e') and R_-(e) <=_G R_-(e') by PJ2. So (G_+ x G_+, <=_componentwise) is a partially ordered set under the product order, and Provenance: (E, <=_E) -> (G_+ x G_+, <=_componentwise) is order-preserving.

The readout map r: G_+ x G_+ -> G is r(p, n) = p - n. This is:
- Monotone in p (increasing p by d gives r(p+d, n) = r(p,n) + d >= r(p,n) since d >= 0).
- **Anti-monotone** in n (increasing n by d gives r(p, n+d) = r(p,n) - d <= r(p,n)).

So r is not order-preserving on the product order of G_+ x G_+: increasing n decreases the readout. Therefore R = r ∘ Provenance is not monotone in general.

This is the fundamental structure: the provenance layer (G_+ x G_+) is a monotone lattice; the readout layer r introduces signed cancellation. The signed readout being non-monotone is a consequence of the anti-monotone dependence on the negative-part component. Obligation PJ4 is discharged.

**PJ5 (Minimal split).** The standard Jordan-Hahn decomposition assigns:
```
w_+(x) = max(w(x), 0_G)
w_-(x) = max(-w(x), 0_G)
```

Minimality: if (w_+', w_-') is any other split with w_+'(x) - w_-'(x) = w(x) and both in G_+, then write w_+'(x) = w_+(x) + delta for some delta >= 0_G (since w_+'(x) >= max(w(x), 0_G)), so w_-'(x) = w_-'(x) = w_+(x) + delta - w(x) = w_-(x) + delta >= w_-(x). Both components are pointwise >= the minimal ones. Obligation PJ5 is discharged.

### 5.3 Physical Instantiation: GW Axial Charge

The GW axial-charge observable Q_A = n_+ - n_- (Atiyah-Singer index on the GW lattice) is a PN/Jordan factorized observable at the **global chirality** level:

```
w_+ = n_+   (count of positive-chirality zero modes)
w_- = n_-   (count of negative-chirality zero modes)
Q_A = w_+ - w_-
```

Per `active-research/signed-readout/jordan-calm-formalization.md` §3, the **local pointwise** decomposition is also available:
```
q_+(x) = max(q_A(x), 0)   (positive part of per-site axial density)
q_-(x) = max(-q_A(x), 0)  (negative part)
```

The local decomposition satisfies J1–J4 (JD-CALM admissibility). The minimal split is uniquely defined at the per-site level by the standard positive/negative part construction.

The **integer-index bridge failure** identified in `active-research/signed-readout/gw-boundary-tests.md` §1-2 is not a failure of the PN/Jordan factorization per se: Q_A is correctly factorized as R_+(e) - R_-(e) = n_+ - n_-. The bridge failure is a failure of the *readout layer* r(p,n) = p - n being non-CALM-monotone (as predicted by the criterion: w(x_anti-instanton) < 0 so R is not monotone). This is the correct diagnostic.

### 5.4 Connection to the v3 Factorization Iff Theorem

The PN/Jordan factorization obligation is the concrete algebraic form of the v3 Factorization Iff Theorem from `active-research/signed-readout/historical-factorization-iff-theorem.md` §2.1:

```
v3 Factorization Iff Theorem:  Q = read ∘ acc
   acc: inputs -> E     (monotone-provenance accumulator)
   read: E -> G          (scalar-readout decoder)

Q is CALM-monotone iff every generator-weight w(x) in G_+.
```

The acc map is the inclusion of events into E (append-only, monotone by construction); the read map is R = the weight-extended homomorphism. The PN/Jordan split makes the two-layer architecture explicit: R_+ = read_+ ∘ acc and R_- = read_- ∘ acc are each individually monotone; R = R_+ - R_- is the composite with the signed readout map.

---

## 6. Explicit Failure Conditions

The following conditions would falsify this result:

**F1: Free commutative monoid fails.** If E is not freely generated by X (e.g., there are relations among generators), then the extension of w to R is not uniquely determined by w|_X alone. The proof of the (=>) direction uses that 0 <=_E x for every x (which holds in the free monoid), but might fail if there is a relation x = 0. A non-free E with x ~ 0 for some generator x would give e' = 0 <= 0 = e for any pair with e' = x, collapsing the information order.

**F2: G not an ordered abelian group.** The proof uses the N_0-module structure of G_+ (that n * g in G_+ for g in G_+, n in N_0). If G is only a group (not ordered), or if G_+ is not stable under scalar multiplication by N_0 (a non-standard cone), the (<=) direction fails.

**F3: Weight function not well-defined on generators.** If some generator x has ambiguous weight (e.g., x appears in two inequivalent contexts with different weights), the extension to R is undefined. The theorem requires w: X -> G to be a well-defined function.

**F4: Information order is not the free-monoid divisibility order.** If <=_E is some other partial order (e.g., a causal order from an external poset structure), the proof of (=>) uses 0 <=_E x, which may not hold under arbitrary causal orders. In that case, the criterion is necessary but may not be sufficient.

**F5: G_+ is not the positive cone of an ordered group.** If the order on G is not compatible with addition (e.g., G = Z but with a reversed order for negative elements), the criterion fails. Specifically: if w(x) > 0 but R(x) < R(0) due to a non-standard order, the (<=) direction breaks.

**F6: The PN/Jordan split does not exist in G.** The minimal split requires G to be a lattice-ordered group (so that max(g, 0) exists for every g). If G is only partially ordered and max(g, 0) does not exist for some g in G, the canonical minimal split cannot be constructed. The theorem still holds (proof of PJ1–PJ5 requires the lattice structure), but PJ5 (minimality of the split) cannot be stated without it.

---

## 7. Result and Verdict

**Monotonicity Criterion: RESOLVED at reconstruction grade.**

The proof is complete and self-contained. All steps are direct and elementary (no appeal to functional analysis, topology, or advanced algebra beyond the definition of free commutative monoids and ordered abelian groups). The reconstruction grade reflects the fact that no CAS verification was performed, but the proof has no unverified steps — the gaps are in the boundary cases (non-free E, non-lattice G), which are explicitly named as failure conditions.

**PN/Jordan Factorization Obligation: STATED AND DISCHARGED at reconstruction grade.**

All five obligations (PJ1–PJ5) have been explicitly discharged. The canonical minimal split exists by the standard Jordan-Hahn construction whenever G is a lattice-ordered group. The provenance/readout layer split has been formalized. The connection to the v3 Factorization Iff Theorem and the GW axial-charge instantiation is established.

**What the boundary theorem now has:**

1. A proved iff criterion (monotonicity iff all generator weights are nonneg).
2. A canonical factorization (the PN split) into a monotone provenance layer and a signed readout layer.
3. A concrete failure example (GW axial charge, Q_A = n_+ - n_-, with negative-weight anti-instanton contributions).
4. Six explicit failure conditions for falsification.

**What remains open:**

- **OQ1 (Record-graph test completion).** The `signed-readout-record-graph-test.md` specification requires exhibiting the four relations (evidence order, causal order, finality relation, readout order) as distinct in a concrete toy diagram. This file proves the algebraic criterion; the record-graph test would add an observer-finality layer.
- **OQ2 (Integer-index recovery at the topological level).** The PN/Jordan split explains why the signed-real bridge survives (Section 5.3) but the integer-index bridge does not (r(p,n) = p - n is non-monotone). The deeper question — whether some enriched provenance structure can recover the integer index monotonically — is not resolved here. Current evidence: no, under all three frameworks tested.
- **OQ3 (Non-lattice-ordered G).** PJ5 requires max(g, 0) to exist in G. For G a general ordered (non-lattice) abelian group, the canonical split may not exist. Stating the correct form of PJ5 for the non-lattice case is an open algebraic question (though not relevant for the main physics instantiations where G = Z or G = R).

---

## 8. Promotion to Canon

This result meets the stated publication-potential criteria (publish potential 5, per NEXT-STEPS.md). The theorem is precise, proved, and has explicit failure conditions. It directly supports the recommended theorem package from `signed-readout-verdict-2026-05-31.md`:

1. Signed readout monotonicity criterion — **PROVED here.**
2. Monotone provenance factorization via PN/Jordan decomposition — **DISCHARGED (PJ1–PJ5) here.**
3. GW axial charge as a corollary — **instantiated in Section 5.3 here.**
4. CALM as the monotone/reducible subcase — follows immediately: R is CALM-monotone iff all w(x) in G_+.
5. Wolfram/local-rule systems as broader superframe — not addressed here (architecture question, not proven).
6. Source/shadow rendering hypothesis — not addressed here (future work).

Status recommendation: upgrade from `active-research` to `reconstruction` for items 1 and 2. Items 3–6 remain at prior grades.
