---
title: "K2175 Homogeneous anticommutator exclusion with mixed commutator"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2175_mixed_grade_euler_localization_probe.py
---

# K2175 Homogeneous anticommutator exclusion with mixed commutator

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2175 homogeneous anticommutator exclusion with unrestricted commutator grades
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

For scalar-square normal seven-form v and t=i u with u a normal three-form,
EVERY normalized descent candidate with nonzero homogeneous anticommutator
x=(vt+tv)/2 of grade4 OR8 is excluded. The commutator y=(vt-tv)/2 may mix
both grades6 AND10. This strictly enlarges K2173's homogeneous-x/homogeneous-y
class. Remaining scalar-square candidates must have BOTH x4 and x8 nonzero;
nonscalar-square ports remain open. The Euler filter remains necessary only.

Keep K2173's full real Cl77 carrier, fixed W(3,1)+N(4,6), supplied common reverse,
simple contraction and normalized zero-order adapters. SC-OP-04 ASSERTS candidate
four-field grammar; SC-GEO-55 ASSERTS rotated-Levi-Civita displacement, neither
selects these supplied adapters. No source/full16cell/full20/K-C, native2+1/chirality,
physical quotient or global-domain verdict follows. Source, ledger0.263, canon and
LT-SM8/LT-GR6b/AC-F1 stay unchanged. No novelty or external certification is claimed.

## 1. Localize the full mixed commutator

Work in complex normal Clifford algebra Mat32(C), using the tangent volume as i.
Let v²=a, t²=c, x=(vt+tv)/2, y=(vt-tv)/2 and D0=P²=d−210x, d=49a+225c.
K2169 requires P and D0 invertible for every nonzero descent candidate. Scalar
squares imply x commutes with v,t,y and y²=x²−ac. K2173 derives the ordered
quartic E=0 from the original Euler contraction of all ten descent equations.

If x=0 or y=0, reuse K2171's anticommuting/commuting exclusion. Otherwise assume
K(x)=kx, k=2 for grade4 or −6 for grade8. Write y=y6+lambda I_N, where I_N is
normal volume. It squares to−1 and commutes with the even algebra. Therefore
K(y)=−2y−8lambda I_N. Reversion separates the quartic exactly into

    g(x)=0, h(x)y=8lambda I_N D0,
    g(X)=delta X²+alpha X+f, h(X)=beta+gamma X,
    delta=182+126k,
    alpha=42c−1470a−k(49a+315c)/2,
    f=343a²+1491ac−540c²,
    beta=−49a−153c, gamma=392+21k.              (1)

When lambda=0 the old homogeneous y6 theorem applies, including singular y.
For lambda≠0, the right side is invertible; finite matrix algebra therefore
forces both h(x) and y invertible. This inference uses no separate invertibility
assumption about v or t.

## 2. Trace identity without dividing a possibly zero resultant

Let tau be normalized matrix trace; tau(x)=0 and tau(I_N^-1 y)=lambda.
Multiplying(1) by I_N^-1 and taking trace yields

    8 tau(D0 h(x)^-1)=1.                       (2)

Put Delta=delta beta²−alpha beta gamma+f gamma². Modulo g(x)=0,

    h(x)(delta beta−alpha gamma−delta gamma x)=Delta.

Multiply this identity by h(x)^-1 D0 and take trace. Since
 tau(x²)=−f/delta, the result is

    Delta tau(D0/h)=d(delta beta−alpha gamma)−210 gamma f.

This uses h(x)^-1, already proved to exist, and NEVER divides by Delta. In fact
Delta vanishes at two candidate projective roots below; those cases are not
silently removed. Combining with(2) gives the necessary scalar polynomial

    H=8(d beta delta−d gamma alpha−210 gamma f)
      −(beta² delta−beta gamma alpha+gamma² f)=0. (3)

The minus sign before210 gamma f is essential: it comes from tau(x²)=−f/delta.
Exact factorization is

| k | H |
|---|---|
|2|−340256(a−3c)(98a+585c)|
|−6|−784(49a+495c)(259a+159c)|

If c=0 this forces a=0; then g(x)=delta x²=0 contradicts invertible D0=−210x.
Thus c≠0 and q=a/c is one of the four listed roots.

## 3. Integer spectral multiplicities rule out every root

At each root f≠0 and alpha²−4delta f≠0. Thus g has distinct, nonzero complex
roots r,s. Normal volume has two complex eigenspaces of dimension16. The trace
of x on EACH is zero: tau(x)=tau(I_N x)=0 since I_N x has grade6 or2, not0 or10.
Each block therefore contains both roots; otherwise its trace would16r or16s≠0.
Let their multiplicities be m and16−m, with1<=m<=15. From mr+(16−m)s=0,
r+s=−alpha/delta and rs=f/delta, obtain

    n=m(16−m)=−256 delta f/(alpha²−4delta f),
    15<=n<=64.                                 (4)

| k | q | Required n |
|---|---|---|
|2|−585/98|−137372160/32228329|
|2|3|−619008/8843|
|−6|−495/49|19798080/1739761 <15|
|−6|−159/259|−1058563584/1045519|

Every possibility is impossible. The proof assumes neither positive trace-square,
real spectrum nor diagonalizability in advance; the distinct-root quadratic itself
implies diagonalizability where it is used. Degenerate a=c=0 and lambda=0 were
handled separately. This settles the entire stated class, not sampled amplitudes.

## 4. Released original-equation consumer

For normal basis n1,...,n10 with the first four positive, take

    v=n1234567,
    u=(n1+2n8)(n2+3n9)n10.

The factors in u are mutually orthogonal and nonnull. Direct Clifford evaluation
gives a=1,c=−24, nonzero PURE x8, and BOTH y6,y10 nonzero. This lies beyond
K2173's homogeneous-y class. Its x satisfies(x²−1)(x²−25)=0, so D0=−5351−210x
is invertible. The exact probe constructs the original ten residual rows using
K2169's unique adapters, checks their Euler contraction against the quartic, and
finds nonzero residuals. It also checks the new reversion split on this fixture.
The full-class proof above eliminates a continuum of such candidates; the fixture
checks the transfer back to the actual equations rather than certifying universality.

## 5. Released successor: localize the remaining mixed-grade escape

For arbitrary scalar-square x=x4+x8 set U=K(x), J=y10=lambda I_N. The SAME
ordered quartic is E=F+UL, where

    L=126x−(49a+315c)/2+21y,
    F=f+(42c−1470a)x+182x²+(−49a−153c)y+392xy−8J D0.

Because x,y,I_N commute, F commutes with both x,y. Thus E=0 implies
[U,x]L=[U,y]L=0. Let r=(a+9c)/6, b=(7a+45c)/6 and
Lrev=21(6x−y−b), the reversion of L. Direct factorization gives

    L Lrev=441(35x²−12bx+b²+ac)
           =−(147/2)D0(x−r).                    (5)

Invertible D0 commutes with x−r, so every survivor obeys

    [U,x] (x−r)=[U,y] (x−r)=0.

Reversion gives the LEFT annihilations as well: x,U are reversion-even, y is
odd, and the commutators have parities minus and plus respectively. Consequently
both commutators map into ker(x−r), annihilate im(x−r), and have rank at most
nullity(x−r). If r is absent from the spectrum, both vanish; then x4=(U+6x)/8
and x8=(2x−U)/8 commute with each other and with y.

More strongly, nonzero[U,x] requires a Jordan defect at r. If x is semisimple
at r, the primary decomposition makes ker(x−r) disjoint from im(x−r).
Localization restricts the commutator to that eigenspace, whereas on an r-eigenvector
[U,x]v=−(x−r)Uv lies in im(x−r). Therefore it vanishes there and on the complementary
primary components. This is a necessary structural restriction, not diagonalizability
assumed for every candidate.

There is also a scalar condition on singular L. For any nonzero v in ker L,
(5) and invertible D0 imply xv=rv and yv=sv, s=(a−9c)/6. On that vector
D0=2(7a−45c), so7a−45c≠0. Exact substitution yields

    Fv=(8/9)(7a−45c)(17a+18c−18J)v.

E=0 forces Jv=(17a+18c)v/18. Since J²=−lambda², this requires

    (17a+18c)²+324lambda²=0.                    (6)

This is NOT a positive-sum exclusion: with real v,u and t=i u, lambda may be
imaginary. If(6) fails, L must be invertible and[U,x]=[U,y]=0. The singular
hypersurface and the commuting mixed-grade class both remain open, and every
survivor still owes all ten original equations.

The probe reuses K2173's order-sensitive mixed-grade fixture. It verifies the
ordered E=F+UL identity, the exact pencil factor(5), and the commutator relation.
For this actual fixture x−r is invertible but[U,x] is nonzero, so localization
rejects it directly. It also checks the singular-face factorization symbolically.
This executes the next mixed-grade discriminator released by the homogeneous-x
exclusion; it does not turn that discriminator into an all-port theorem.

## Verification and continuation

Run the named Python probe in the repository SymPy environment; --write regenerates
the report. Exact polynomial factorizations, inverse identities, multiplicity values,
Clifford grade relations and original-row controls supplement the independently
reviewed proof. Five genuine input/equation faults are rejected after green baseline,
including the trace-sign error discovered and corrected during derivation. Counts
of controls are distinct from proof acceptance. No Lean/external-expert claim.

For scalar-square ports the surviving search space now REQUIRES mixed x4+x8.
Use the new exceptional-spectrum and singular-face filters, K2173's ordered quartic, and then all ten K2169 rows; homogeneous x cannot be
rescued by adding a volume component to y. Nonscalar squares, moving geometry,
changed reverse and mixed odd/even ports remain genuinely distinct alternatives.
