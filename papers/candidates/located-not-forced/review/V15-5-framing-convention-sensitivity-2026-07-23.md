---
title: "V15-5 framed-cycle convention and sensitivity packet"
date: 2026-07-23
status: complete-internal
scope: "LNF v2.15 framing evidence; no manuscript or claim-grade change"
campaign_item: V15-5
executable: tests/boundary-eta/v15_framing_convention_sensitivity.py
---

# V15-5 framed-cycle convention and sensitivity packet

## Result

Under the declared reconstruction-grade premise that GU's
\(\Lambda^2_+=SU(2)_+\) twist is the **natural tangential framing** described
below, the convention chain gives the two signed framed classes
\[
[M,\tau_+]=2\in\mathbb Z/24,\qquad
[-M,\tau_+]=-2=22\in\mathbb Z/24.
\]
They have Adams values \(+1/12\) and \(-1/12\), respectively. Both full classes
and both Adams values have additive order \(12\). Only their projected
3-primary components have order \(3\):
\[
\begin{aligned}
2&\longmapsto(2\bmod8,2\bmod3),&
P_3(2)&=8\in\mathbb Z/24,\\
-2&\longmapsto(6\bmod8,1\bmod3),&
P_3(-2)&=16\in\mathbb Z/24.
\end{aligned}
\]
Thus every viable orientation, generator, and Adams-sign convention merely
sign-flips the nonzero 3-primary component. The standard factor-of-two
normalization is required for the exact class \(\pm2\), value
\(\pm1/12\), and full order \(12\). The two common factor-of-two mistakes alter
those full readouts but still cannot erase the mod-3 component.

No viable convention for this same framed cycle erases the nonzero 3-primary
component, so the V15-5 convention stop condition is **not triggered**.

There are two erasing possibilities, but neither is a convention for the same
framed cycle:

1. treating \(\Lambda^2_+\) as a gauge/coefficient bundle gives no tangential
   framing degree; and
2. changing the natural framing by a stable-framing shift
   \(k\equiv1\pmod3\) changes the framed object and sends \(2+k\) to zero in the
   3-primary projection.

Either outcome would falsify the declared GU-to-natural-framing premise and
would trigger the manuscript/campaign stop stated below.

## The oriented framed cycle and reference

The packet fixes the object rather than relying on an unspoken sign convention.

- **Underlying manifold:** \(M=\mathbb{RP}^3=L(2;1)\), the stated
  deformation-retract spine of
  \(\mathrm{GL}(4,\mathbb R)/O(3,1)\).
- **Orientation:** view \(M\) as the oriented Euler-\(+2\) circle bundle over
  the standard oriented \(S^2\), equivalently as the boundary of its oriented
  Euler-\(+2\) disk-bundle filling \(W\). Reversing this boundary orientation
  produces the displayed negative branch.
- **Framing on \(M\):** the natural fiber-preserving framing identified in the
  repository's Kirby--Melvin trace with the quotient/right-handed Lie framing.
  This is the framing denoted \(\tau_+\).
- **Stable degree reference:** the right-handed Lie framing of the oriented
  \(S^3\) is the positive stable generator \(\sigma\), normalized by
  \(J(\sigma)=\nu\) and \(e_{\mathbb R}(\nu)=1/24\). The charge-one adjoint
  clutching generator \(\rho\in\pi_3(SO(3))\) stabilizes to
  \(2\sigma\). Therefore the relative stable-framing degree of the natural
  \(M\)-framing is \(d=+2\); orientation or generator reversal gives \(d=-2\).

The phrase “reference framing” here means the explicit generator calibration
used to measure the relative stable-framing degree. It does not license adding
an arbitrary stable twist to \(\tau_+\). Such a twist changes the framed cycle,
as the sensitivity table shows.

## Link-by-link convention chain

### 1. GU tangential identification

**Declared premise, reconstruction-grade.** GU's self-dual
\(\Lambda^2_+=SU(2)_+\) twist is identified with the exact natural tangential
framing \(\tau_+\) on \(M\), not merely with some unspecified tangential
framing and not with a gauge coefficient bundle.

Source trace: manuscript Section 7,
`located-not-forced-generation-count-2026-06-29.md`, calls this identification
reconstruction-grade; `GEOMETER-VS-PHYSICS-OBJECTS.md` requires this
program-native tangential/torsion construction to be distinguished from an
integer-index or gauge-coefficient default. The existing boundary-\(\eta\)
checks likewise separate the tangential framing carrier from the internal
coefficient channel.

### 2. Relative Pontryagin number

**Imported standard framing input.** For the natural fiber-preserving framing
of \(L(2;1)\), the Euler-\(2\) disk-bundle calculation gives
\[
\langle p_1(W,M),[W,M]\rangle
=2+\frac{\chi(S^2)^2}{2}=2+\frac4{2}=4.
\]
Orientation reversal changes the relative characteristic number's sign.

Source trace: the repository's Kirby--Melvin summary in
`papers/drafts/two-primary-no-go-three-primary-boundary-class-2026-06-28.md`
and the fuller normalization paragraph in the parallel TeX Section 7. Markdown
is canonical during this hardening campaign; the TeX paragraph is used only as
an explicit record of the convention assembly already summarized by the
canonical Markdown and `PRIOR-ART-DELTA.md`. This packet does not present the
repository summary as a new derivation of the published theorem.

### 3. \(p_1/2\) normalization

**Imported characteristic-class convention.**
\(H^4(BSpin;\mathbb Z)\) is generated by the spin characteristic class
\(\tfrac12p_1\). Hence
\[
\left\langle\frac{p_1}{2}(W,M),[W,M]\right\rangle=\pm2.
\]

Source trace: McLaughlin and Sati--Shim, as identified in
`PRIOR-ART-DELTA.md` and the manuscript normalization paragraph. The executable
checks only the resulting exact arithmetic; it does not reprove the
characteristic-class theorem.

### 4. Stabilization

**Imported homotopy input.** With \(\rho\) the charge-one adjoint generator and
\(\sigma\) the chosen positive stable generator,
\[
\pi_3(SO(3))\longrightarrow\pi_3(SO),\qquad
\rho\longmapsto2\sigma.
\]
This agrees with the relative value \(p_1/2=2\). The stable degree is therefore
\(\pm2\), not the unstable adjoint Dynkin index \(4\).

Source trace: Kirby--Melvin, as recorded in the canonical Section 7
summary, the parallel TeX normalization paragraph, `PRIOR-ART-DELTA.md`, and
V15-5 in `HARDENING-QUEUE.md`.

### 5. Adams convention

**Imported normalization.** Choose
\(\nu=J(\sigma)\in\pi_3^S\cong\mathbb Z/24\) and normalize the real Adams
invariant by
\[
e_{\mathbb R}(\nu)=\frac1{24}\in\mathbb Q/\mathbb Z.
\]
Then
\[
J(\pm2\sigma)=\pm2\nu,\qquad
e_{\mathbb R}(\pm2\nu)=\pm\frac2{24}=\pm\frac1{12}.
\]

Source trace: Adams's image-of-\(J\) and \(e\)-invariant normalization, with
the original paper and correction listed in `PRIOR-ART-DELTA.md`. As the
manuscript already says, the composite
\((p_1/2)/24=p_1/48\) is the repository's assembly of sourced conventions, not
a verbatim theorem attributed to one source.

### 6. Exact CRT image and orders

**Derived exact arithmetic.** The CRT map and its subgroup projectors are
\[
x\longmapsto(x\bmod8,x\bmod3),\qquad
P_2(x)=9x,\quad P_3(x)=16x\pmod{24}.
\]
The multipliers are the CRT idempotents:
\[
9\equiv(1,0),\qquad16\equiv(0,1).
\]
Consequently
\[
\begin{array}{c|c|c|c|c}
x&\mathrm{CRT}(x)&P_2(x)&P_3(x)&\operatorname{ord}(x)\\
\hline
2&(2,2)&18&8&12\\
22=-2&(6,1)&6&16&12
\end{array}
\]
and \(P_3(2)=8\), \(P_3(-2)=16\) each have order \(3\). In
\(\mathbb Q/\mathbb Z\),
\[
\frac1{12}=\frac34+\frac13,\qquad
-\frac1{12}=\frac14+\frac23\pmod{\mathbb Z}.
\]

Source trace: this arithmetic is asserted and exhaustively checked by the new
executable, consistent with LBN-023 and
`tests/big-swing/R4_crt_two_arena.py`. LBN-022 is the
\(e_{\mathbb R}=1/12\) link; LBN-023 correctly distinguishes full order \(12\)
from projected order \(3\).

## Assumptions versus derivations

| Link | Status in this packet | Evidence/source role |
|---|---|---|
| \(M=\mathbb{RP}^3=L(2;1)\) is the metric-fiber spine | GU reconstruction premise inherited from the manuscript | Section 7 |
| GU \(\Lambda^2_+\) equals the exact natural tangential framing \(\tau_+\) | load-bearing reconstruction premise | Section 7; boundary-\(\eta\) fork |
| Euler-\(+2\) filling and natural/right-handed Lie framing | imported framing specification | Kirby--Melvin trace in repo |
| relative \(p_1=\pm4\) | imported standard-result application | Kirby--Melvin trace |
| \(\tfrac12p_1\) is the integral Spin generator | imported convention/theorem | McLaughlin; Sati--Shim |
| \(\rho\mapsto2\sigma\) under stabilization | imported theorem/convention | Kirby--Melvin |
| \(e_{\mathbb R}(\nu)=1/24\) | imported Adams convention | Adams plus correction |
| degree \(\pm2\), class \(\pm2\), \(e_{\mathbb R}=\pm1/12\) | derived from the preceding links | exact executable |
| CRT coordinates/projectors and all additive orders | derived, exhaustive exact arithmetic | exact executable |
| any relation to an integer generation count | **not derived** | blocked by \(\operatorname{Hom}(\mathbb Z/3,\mathbb Z)=0\) |
| external establishment of the convention chain | **not present** | requires an independent specialist |

## Sign sensitivity

Four sign sources can appear in notation: orientation of \(M\), charge-one
clutching/self-duality sign, choice of stable generator \(\sigma\), and sign of
the Adams calibration. Their product gives only the two branches above. The
executable enumerates all \(2^4=16\) combinations: eight produce \(+2\), eight
produce \(-2\), and all sixteen retain a nonzero order-3 projection.

Changing the Adams sign without changing the named generator changes only the
reported sign of \(e_{\mathbb R}\). Replacing the generator by its negative
changes the coordinate label in the same way. Neither operation changes an
additive order or turns a nonzero mod-3 class into zero.

## Factor and object sensitivity

| Branch | Signed stable degrees | Signed classes | Full order | 3-primary outcome | Adjudication |
|---|---:|---:|---:|---|---|
| sourced \(\rho\mapsto2\sigma\), \(d=p_1/2\) | \(\pm2\) | \(2,22\) | 12 | nonzero, order 3 | viable convention chain |
| omit the stabilization factor \(2\) | \(\pm1\) | \(1,23\) | 24 | nonzero, order 3 | alters LBN-022/023; contradicted by sourced stabilization |
| use \(p_1\), not \(p_1/2\), as stable degree | \(\pm4\) | \(4,20\) | 6 | nonzero, order 3 | alters LBN-022/023; double-counts the factor \(2\) |
| multiply the correct degree by adjoint rank \(3\) | \(\pm6\) | \(6,18\) | 4 | **zero** | erases, but rank is not a framing convention |
| gauge/coefficient reading, no tangential framing degree | \(0\) | \(0\) | 1 | **zero** | different construction and failure of the GU tangential premise |

The factor-of-two result has a simple exact reason: \(2\) is a unit modulo
\(3\). Multiplying or dividing the nonzero class by a valid power-of-two
normalization can alter its 2-primary coordinate and full order, but cannot
erase its mod-3 coordinate. Erasure needs a factor divisible by \(3\), a zero
degree, or a change of framed object.

The integer-degree part of the stable-framing torsor also matters. Replacing
\(\tau_+\) by a genuinely different framing shifted by integral stable degree
\(k\) changes the degree from \(2\) to \(2+k\). Its 3-primary projection
vanishes exactly when
\[
2+k\equiv0\pmod3,\quad\text{equivalently}\quad k\equiv1\pmod3.
\]
This is not generator relabeling: it changes the framed cycle. It shows why
“GU supplies some tangential framing” is insufficient. The manuscript needs
the exact natural-framing identification it currently declares.

## Existing boundary-\(\eta\) checks

The existing scripts establish a neighboring distinction, not external
adjudication of this convention packet:

- `tests/boundary-eta/aps_eta_antilinear_plus96_rp3.py` separates the
  tangential \(1/12\) channel from the coefficient \(k/8\) channel;
- `tests/boundary-eta/plus96_framing_class_lens_eta.py` checks the modeled
  frame charge and the \(p_1/48\) arithmetic; and
- `tests/boundary-eta/verify/plus96_eta_denominator_indep_check.py` repeats the
  denominator and frame-projection calculation without importing the direct
  certificates.

Those are internal repository checks produced within the same AI-directed
process. The new exact arithmetic is another internal certificate. Repetition,
even through a separate implementation, is **not** external specialist
adjudication, independent replication, or peer review.

## Manuscript consequences

With the declared premise retained and the sourced normalization used:

- Section 7 may state the two classes as \(\pm2\), with
  \(e_{\mathbb R}=\pm1/12\);
- the full class and full Adams value have order \(12\);
- only the CRT-projected 3-primary component has order \(3\);
- sign ambiguity is immaterial to nonvanishing, but not to the displayed
  representative;
- LBN-022 and LBN-023 are arithmetically consistent;
- the carrier remains homotopy-fixed and does not become an integer generation
  count; and
- no claim moves from “located” to “forced.”

If a specialist validates a factor-of-two alternative, the nonzero 3-primary
statement would survive, but the exact \(\pm2\), \(\pm1/12\), and order-12
statements would not. That would make LBN-022/023 and the current manuscript
wording false and would independently trigger the campaign's load-bearing
statement stop.

If GU's \(\Lambda^2_+\) object is instead a gauge coefficient, or if its
tangential framing differs from \(\tau_+\) by
\(k\equiv1\pmod3\), the nonzero 3-primary carrier statement itself fails.
Section 7 could no longer exhibit this carrier from GU's tangential data.

## Campaign stop condition

Stop V15-5 integration and return to Joe if any of the following is established:

1. a viable convention for the **same** natural oriented framed cycle sends
   \(\pm2\) to zero in the 3-primary projection;
2. the sourced stabilization or Adams normalization is shown to insert a
   factor divisible by \(3\) or to make the stable degree zero;
3. GU's \(\Lambda^2_+\) is adjudicated as gauge/coefficient rather than the
   exact natural tangential framing; or
4. GU supplies a tangential framing shifted from \(\tau_+\) by
   \(k\equiv1\pmod3\).

The internal audit found no branch satisfying conditions 1 or 2. Conditions 3
and 4 remain premise-level risks because the GU tangential identification is
reconstruction-grade. They are not silently promoted to externally settled
facts.

## Reproduction

Run from the repository root:

```sh
python3 tests/boundary-eta/v15_framing_convention_sensitivity.py
```

The executable uses only Python's standard library, prints both signs and every
sensitivity branch, exhaustively asserts the CRT projector identities on all
24 classes, and exits nonzero on any failed expectation.
