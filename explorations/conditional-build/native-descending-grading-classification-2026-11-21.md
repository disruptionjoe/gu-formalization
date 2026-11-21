---
title: Native descending gradings and the missing physical index realization
status: exploration
doc_type: structural-result
created: '2026-11-21'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Classify grading lifts and total index parity/residues or isolate the exact native missing datum
actual_delta: Complete quotient-lift normal form and four-grade symbol comparison; native outcome3 blocked on physical graded Fredholm observation realization
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Which grading is native?

> **GU-COMPARATOR-ROUTING — scope before inference.** A conventional family
> index or chirality comparator binds only its declared construction. It is
> not evidence for or against Weinstein's source-native mechanism without a
> typed bridge. Read `lab/methods/source-native-comparator-routing.md` and its
> source pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2-P3
tier: T2
expected_delta: Exhaustive lift parameterization, typed index bounds and decisive packet disposition
actual_delta: Observation does not force the coherent lift; native data do not decide the zero-total premise

Authority: `joe_direct_chat_2026_11_21`; base `cc6bd40f4110c5e3a0f4cc8519b4a80e3508d2a1`.
[Exact probe](../../tests/program-focus/native_descending_grading_probe.py) ·
[Data](../../lab/process/native-descending-grading-classification.json) ·
[Review](../../lab/process/hostile-reviews/2026-11-21-native-descending-grading-review.md).

```gu-typed-objects
result: Complete split-quotient involution normal form; scoped natural-symbol grading and index table; native missing-input disposition
carrier: supplied graded Hilbert/graph quotient; separately canonical native14 RS with horizontal4 normal10 and positive closed spin4 comparison LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: supplied positive Hilbert topology for analytic splitting; native K95 restriction where specified, not physical positivity ON=declared_carrier
real_structure: complex classification; native K95 quaternionic compatibility is an additional restriction, K77 a distinct subclass
grading: fixed observed involution g, hidden involution A and off-diagonal lift T; physical weak-current projector not assumed equal to chiH
action_owner: N/A -- structural operator categories and existing symbols, no action built or enumerated
target: same-grade native total index and observed weak-current identification MAP-TYPE=intertwiner
```

## 1. Native input audit: the physical projector is not yet supplied

SC-CHI-01/04/51 assert a non-chiral fundamental theory and an effectively
chiral observed sector through decoupling/branching. Their source status is
retained. They do not specify the physical Fredholm complex, its grading,
weak-current representation or closed end domain.

P1 names a required chiral projector on an observed carrier. It is a demand,
not a source-authenticated construction of that projector. The Nov11
[p1-observation-descent](p1-observation-descent-2026-11-11.md) result proves
conditional selector/intertwining and mirror-normalizer requirements; it
explicitly leaves physical current identification open. The August3
[chirality audit](../chirality-grading-and-77-rerun-2026-08-03.md) names its
ambient and joint grades kinematic and states that the physical RS projector
is unavailable. The [actual native quotient](native-rs-observed-compatibility-2026-11-11.md)
supplies a carrier/principal-symbol map, not that missing physical projector.
These are different evidence levels, not a new search for an already-known
source assertion.

Important correction to the shorthand in the question: ambient chiY **does
descend**, but to chiH chiN, not to plain chiH on the full observed bundle.
Its index is zero in the closed positive comparison. Neither that zero nor
the failure to equal plain chiH is a native physical verdict. A separately
justified normal-chirality selection changes the observed complex.

Also, one-sided weak coupling does not require a nonzero Fredholm index or
conserved chirality during massive propagation. The odd-operator conditions
below test this packet's proposed index realization, not every way P1 can hold.

## 2. All lifts of a supplied observed grading

Let q:V→B be a surjective linear bundle map with a chosen smooth splitting,
or a bounded Hilbert-space surjection with a bounded splitting. Write
V=K⊕B, K=ker q. Fix a bounded involution g on B (g=2P_w−1 for a specified
projector and its complement). Then **every** bounded linear involution
satisfying qG=gq, and only those, has the form

```
G = [ A  T ]       A²=1,     A T + T g=0.
    [ 0  g ]
```

Proof: qG=gq fixes the bottom row to (0,g); multiplying G² gives exactly
the two displayed equations. Conversely those equations give G²=1 and
descent. This includes twisted or mixed hidden gradings; it is not restricted
to scalar signs. A is an involution on the actual hidden bundle, equivalently
a splitting K=K_A^+⊕K_A^-; global eigenbundles and naturality matter.

At the level of split vector spaces/bundles, T is removable by the
q-preserving shear U=[[1,Tg/2],[0,1]]:
`G=U diag(A,g) U^-1`. This is **not automatically** equivalence for a fixed
physical operator. U must also intertwine that operator and preserve its
current, pairing, real structure and actual domain. An arbitrary shear need
not be an isometry. Thus the theorem does not quotient out physical choices
by an unauthorized field redefinition.

For a fixed nondegenerate orthogonal pairing on K⊕B, imposing G^sharp=+G
or G^sharp=−G forces T=0: the lower off-diagonal adjoint equation forces it.
The diagonal grades must satisfy that same adjoint sign. An indefinite
pairing with a degenerate hidden sector need not admit this orthogonal split;
use the general block equation instead. On the existing R_Y quotient the
hidden sector is nondegenerate and the canonical metric splitting is available.

### Operator and domain restrictions: the exact remaining equations

Suppose a full odd-operator realization is supplied, qD=D_o q, and the
splitting is compatible with the graph domains, so that

```
D = [ D_h  L ] .
    [  0  D_o]
```

A merely fiberwise or Hilbert splitting does not justify this unbounded
operator matrix. On the common invariant domain, G must satisfy

```
{A,D_h}=0,        {g,D_o}=0,
A L + T D_o + D_h T + L g = 0,
G Dom(D)=Dom(D),  q Dom(D)=Dom(D_o).
```

Also impose the selected covariance, real-structure and pairing equations,
plus closedness/Fredholmness and compatible adjoint domains when used. For
an x-dependent local grade, the anticommutator includes derivatives of G;
checking principal symbols omits them. For domain-dependent/nonlocal bounded
grades, the same operator equations apply but the fiberwise Schur shortcut
below does not. This is an exact characterization for **each supplied
realization**. Its union over action C cannot be evaluated without those data.
Class C does not specify them, and its Lorentzian/APSend wording does not
itself prove that any such realization is Fredholm.

Observation alone therefore leaves the hidden involution free. Coherent
horizontal grading is not forced by q. Whether a specified source weak
projector plus its full physical operator selects it remains undecided.

## 3. Exhaustive four-grade example in a declared symbol category

This section goes further than two convenient examples, but only in the
following fixed category: the canonical tangential projected RS symbol on
R_Y=ker Gamma_Y, a nondegenerate 4+10 split, the literal contraction q and its
canonical orthogonal right inverse r; complex, zero-order grades natural
under **independent Spin(H)×Spin(N)**; observed g=chiH on all H*⊗S; no extra
scalar companion, background tensor or physical quotient. This is a
structurally specified symbol comparison, not a classification of all C.
In particular N=Sym²T*X has induced diagonal covariance; requiring the
larger independent product covariance excludes additional mixed structures.

The hidden bundle is K=S_H⊗(R_N^+⊕R_N^-), with inequivalent irreducible
complex normal modules of dimension144. The observed normal modules are
16-type. There is no product-equivariant map from an observed16 to a hidden144,
so T=0. On K the tangential symbol is c_H(xi). A grade anticommuting with
every c_H(xi) has A=chiH⊗a: chiH A commutes with the full complex Clifford
algebra, whose spin module is irreducible. Schur's lemma gives

```
a = epsilon_+ P_N^+ + epsilon_- P_N^-,    epsilon_± in {−1,+1}.
G = A on K,  and r chiH r^-1 on im r.
```

These **four** and only these four grades belong to that category. The
coherent horizontal lift is epsilon_+=epsilon_-=−1. Flipping the hidden
grade to both+1 gives a second descending lift of the same symbol. The
mixed signs are ±chiH chiN on K, with chiH still fixed on im r. They are
not the uniform ambient grade, which would change g downstairs.

The canonical tangential projected RS symbol preserves K and its orthogonal complement, so its off-diagonal block L is zero at symbol level.

All four preserve the actual normal contraction kernel and anticommute with
the hidden tangential symbol. In the explicit K95 fixture they obey the
cross-grade Krein adjoint relation. If one additionally requires a single
quaternionic law JG=−GJ matching chiH downstairs, J exchanges the normal
halves and requires epsilon_+=epsilon_-. Then **two**, not one, remain.
This is not a transfer of K95 to K77 or to a positive elliptic real structure.
Full lower-order couplings and domains can reduce or invalidate this symbol
list; they have not been supplied. No action variants are enumerated here.

## 4. Total index, parity and integer residue

### Closed positive elliptic transfer only

Use the same comparison as Nov11/Nov20: closed oriented spin X^4, positive
elliptic transfer of this symbol, smooth spin normal bundle N of rank10,
no boundary or end. Set p=integral p1(TX), n=integral p1(N). The normal
half-spin characters have rank16 and degree-four term2p1(N). Since gamma
contraction flips normal chirality,

```
[R_N^±] = [N_C][S_N^±] − [S_N^∓],
ch(R_N^±) = 144 + 34 p1(N) through degree4.
```

Consequently the hidden half index is `−6p+34n`, the observed index is
`(80/3)p+16n`, and for every one of the four declared grades

`I_total = (80/3)p+16n + (epsilon_++epsilon_-)(−6p+34n)`.

For N≅Sym²T*X, n=6p and p=3sigma(X), so

| Hidden signs | Total index | Hidden index | Observed index |
|---|---:|---:|---:|
| (−,−), coherent horizontal | −820 sigma | −1188 sigma | 368 sigma |
| (+,−) | 368 sigma | 0 | 368 sigma |
| (−,+) | 368 sigma | 0 | 368 sigma |
| (+,+), hidden-reversed lift | 1556 sigma | 1188 sigma | 368 sigma |

For closed smooth spin X, sigma=16k. Every total is even (indeed divisible
by64), and **[I_total]_24=[8k]_24 for all four**. On K3 (sigma=−16),
the totals are 13120, −5888, −5888, −24896; each has residue16 modulo24.
For signature0 they all vanish, but the observed index also vanishes.
Thus the nonzero-signature comparison excludes balanced total in this
four-grade category; signature0 supplies no nonzero observed-count witness.
Neither case proves native class-C membership. No topology is chosen to fit3.

The table fixes the orientation/sign convention g=chiH. Reversing the
entire grading with g also reversed negates the integers and residues; it
is not a second lift of the same fixed observed projector.

Here [I]_24 is the ordinary integer reduction Z→Z/24. It is **not** an
identified Adams e-invariant, stable homotopy class or the Item2 rho class.
Uniform ambient chiY has total0, parityeven and integer residue0 in this
closed comparison, but descends to a different g=chiH chiN. These cannot
be mixed in a single cancellation argument.

The index framework is the standard closed elliptic index pairing
([Gilkey, chapter5](https://www.maths.ed.ac.uk/~v1ranick/papers/gilkey3.pdf));
the coefficients above are rederived from all32 normal spin weights in the
probe, not obtained from dimensions alone.

### Supplied Fredholm realization, including end data

For any compatible graded Fredholm observation complex the exact answer is
`I_G=I_h(A)+I_o(g)`, hence parity and integer mod24 are the corresponding
sums. No numerical value follows from q and g alone. A compact index problem
with product collar and an applicable elliptic APS theorem instead gives
its own bulk density minus `(eta(B_G)+h(B_G))/2`, with any specified finite
spectral-section correction. Noncompact ends also need an actual Fredholm
realization (for example suitable coercivity/invertibility at infinity in
the relevant elliptic category). Do not put the closed sigma table into a
Lorentzian Y14 formula or assume its eta correction is zero.

The [Bär–Ballmann boundary theory](https://archive.mpim-bonn.mpg.de/id/eprint/327/1/preprint_2011_2.pdf)
requires explicit boundary and infinity hypotheses; it does not confer
Fredholmness on the native symbol. The already-proved
[graph-domain restriction formula](x-p2-p3-phase-domain-index-2026-11-11.md)
gives `I(D|E0)=I(D)−r` for r independent graph-continuous conditions.
Finite-rank changes of elliptic spectral boundary data similarly carry a
relative integer. Whether such modifications preserve the source reality,
observation and admissibility is a separate check; this is not a claim that
all integer shifts are available in C. Without their selection, neither
zero, parity nor a unique mod24 residue is certified for the native total.
A grade-preserving quaternionic operator symmetry preserving the actual and adjoint domains would force evenness;
a suitable cross-grade kernel–cokernel symmetry would force zero. Neither
is inferred just from the Clifford signature or principal symbol.

## 5. Outcome3 and exact missing datum

**Outcome3: close Item1 as blocked on `NATIVE-GRADED-FREDHOLM-OBSERVATION`.**
This names a missing input, not mathematical undecidability or a claim that
an entire action must be built. The minimum missing tuple is:

1. The source-authenticated physical observed carrier/current, its weak
   projector P_w, and the actual contraction-plus-physical-reduction map.
   Decide whether g is chiH, chiH chiN on a selected internal sector, or
   another explicitly identified grade.
2. The total/hidden/observed graded symbol classes and compatibility with
   source lower-order couplings: enough to decide the block equations in §2.
   A typed structural certificate can suffice; no full coefficient fit is needed.
3. Graph-continuous surjective observation on the actual analytic spaces,
   common grade-stable closed domains/end prescription, Fredholm and adjoint
   compatibility, including the boundary spectral/relative index datum.

These are independently missing; even declaring g=chiH does not fix A or
the domain. The source's non-chirality assertion supplies none as an index
realization. Class C admits external boundary data and does not restrict
all gradings to the four-grade symbol comparison.

**Outcome1 is not established:** zero-signature comparison and abstract
balanced doubles are not inhabited native witnesses with an identified
physical integer. **Outcome2 is not established:** there is no exhaustive
native grading/domain set with universally nonzero index. No T1 kill is
claimed, no row/class/source verdict moves, and the joint intersection stays
open. The conditional hidden=−observed theorem remains valid under its
explicit premises, but is not promoted to a native realized claim.

Item2step4 is parked until Item1 supplies a native integer observable. Its
imposter/gamma-traceless connection is an ambient kernel-label relation only:
under actual observation the draft imposter is gamma-trace. SC-GEN-52 stays
uncertain. This packet closure releases ordinary selection elsewhere under
the unchanged program rules; it is not a work-stopping checkpoint. Do not
build the missing operator/action to reopen it. Reopen only when the named
input arrives or an independently proved structural theorem decides it.

## 6. Verification and optional additivity

The exact probe checks the quotient normal form and non-isometric/non-operator
shear controls, independent normal half-spin character expansion, all four
totals/parities/residues, graph-domain sensitivity, actual K95 hidden-kernel
and symbol conditions, and the extra quaternionic restriction. Independent
specialist review is recorded separately. These tests do not certify an
unbuilt physical projector or analytic domain.

Item1step3 is optional T3; the existing conditional corollary remains checked.
The finite six-space kernel/cokernel exact-sequence additivity theorem and
balanced-total corollary in `Lean/GUFormalization/ObservedHiddenSplit.lean`
compiled with Lean4.32rc1 and the existing mathlib cache, without `sorry`.
Exactness is supplied as range=kernel; dimensions are derived by rank-nullity.
Constructing the analytic exact sequence and identifying the native physical
grade remain obligations. This optional T3 result adds no native realization.
