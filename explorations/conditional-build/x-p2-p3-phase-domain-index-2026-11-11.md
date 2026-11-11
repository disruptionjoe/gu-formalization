---
title: "X-P2-P3: phase, domain and noncompact index requirements"
status: exploration
claim_verdict: conditional_structural_result
doc_type: structural-result
created: "2026-11-11"
program_target: X-P2-P3
tier: T2
expected_delta: "open to constrained through operator/domain/asymptotic requirements"
actual_delta: "Whole-operator phase preserves index; domain restrictions and noncompact asymptotics supply distinct index mechanisms. P2-to-realized-index bridge remains open."
classification: INTERNAL_STRUCTURAL_ONLY
canon_verdict_change: none
---

# X-P2-P3: phase is not a complete index datum

**Result.** Multiplying a supplied closed Fredholm operator by a nonzero scalar
preserves its index on the same graded domain. Restricting its domain by `q`
independent graph-continuous conditions lowers the index by `q`. A separate
half-line control has identical principal symbol and domain but different
indices because its lower-order behavior at infinity differs. These facts
constrain what a phase-to-index claim must specify; they do not settle the
intersection for every action in C.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result. Classification: `INTERNAL_STRUCTURAL_ONLY`.

## Native bookends and Layer 0

program_target: X-P2-P3
tier: T2
expected_delta: open to constrained through operator/domain/asymptotic requirements
actual_delta: A conditional structural requirement, no class-wide verdict.

The matrix's P2 is the phase/orientation of a projected RS symbol; P3 is an
integer realized chiral index/count datum. Symbol phase, whole-operator scalar,
grade reversal, boundary subspace and end behavior are different objects.
No equality between them is inferred. The carrier here is a supplied Hilbert
pair `H+`, `H-`, not an asserted physical RS/BV quotient. Its norm is the given
positive Hilbert norm, not an identified ambient Krein or action pairing.
For real carriers only real nonzero scalars are used; arbitrary complex phases
need a complex-linear operator. Both signature subclasses of C inherit these
requirements only after their own typed operator/domain bridge is supplied.
No specific action, coefficients or Lagrangian is constructed or searched.

Demand lineage is weak chirality and three observed families → a graded
observable carrier → a realized stable count → an operator, grading, boundary
and end prescription that actually support such an index. The source's
SC-GEN-01 disavowal of three simply repeated families and SC-CHI-01/51
non-chiral total/effectively chiral world remain intact. Ordinary index
arithmetic does not decide the source-native `2+1` observation mechanism.

```gu-typed-objects
result: X-P2-P3 whole-operator phase, finite-codimension domain and noncompact end index requirements
carrier: Hilbert pair Hplus/Hminus and graph-norm domain E; half-line H1/L2 analytic control; LAYER=toy; CHIRALITY=N/A
pairing: positive Hilbert inner products ON=abstract Hilbert modules, not an identified GU action/Krein pairing
real_structure: real operators for real scalar rescaling; complex-linear operators for complex phases
grading: supplied Hplus/Hminus domain-codomain grading, fixed during scalar rescaling
action_owner: repository-construction
target: Fredholm integer index and conditional mod-three requirement; MAP-TYPE=not-a-map
```

## 1. Whole-operator phase theorem

Let `D:E=Dom(D)⊂H+→H-` be a closed Fredholm operator, with graph norm on `E`.
For a nonzero scalar `z`, `ker(zD)=ker D` and `ran(zD)=ran D`: a linear range
is invariant under nonzero scalar multiplication. The graph norms are
equivalent. Thus closedness, Fredholmness, cokernel dimension and index agree.
The real sign `-1` is covered directly, without a complex path through
operators that might violate reality. For an invertible bounded codomain map
`V`, the range becomes `V ran D` and the cokernel is isomorphic; the same index
conclusion holds, even if a nonconstant multiplier changes symbol coefficients.

This is about the **entire** operator. A phase on one projected principal block,
with coupled blocks, lower-order terms or domains fixed differently, need not
be of this form. No source-defined P2 operation is identified with `zD` here.

If `D` is densely defined between Hilbert spaces, its Hilbert adjoint with its
actual adjoint domain has index `-ind D`. Reversing the grading of the full
odd self-adjoint operator built from `D,D*` exchanges these chiral operators.
Multiplying `D` by `-1` does neither. Even index negation preserves whether the
integer is zero modulo three, while generally exchanging residues one and two.
None of these operations chooses an initial index or establishes a family count.

## 2. Finite-codimension domain theorem

Let `B:E→F` be continuous for the graph norm and onto a finite-dimensional
space of dimension `q`. Put `E0=ker B`. Then `D0=D|E0` is closed and Fredholm as
a map from the graph-norm Banach space `E0` to `H-`, with

`ind D0 = ind D - q`.

Proof: the exact sequence is

`0 → ker D0 → ker D --B→ F --δ→ coker D0 → coker D → 0`,

where `δ(Bu)=[Du]`. This is independent of the lift, since two lifts differ
by an element of `E0`. Exactness at `F` follows because `[Du]=0` iff `Du=Dv`
for some `v∈E0`, hence `u-v∈ker D`. The other positions follow from inclusion
and quotient. The restricted range is closed: `E0+ker D` is closed (a closed
subspace plus a finite-dimensional space), and its quotient by `ker D` maps
homeomorphically to `D(E0)` inside the closed range of `D`. The exact sequence
then proves finite-dimensional cokernel and, by alternating dimensions, the
stated index formula. In particular the restriction may remove kernel, add
cokernel, or do both; it is not merely a zero-mode deletion rule.

This theorem does **not** assert that `E0` remains dense in `H+`. That is a
separate requirement for unbounded-adjoint interpretation. A genuine boundary
trace vanishing on a dense interior core retains density. Redundant written
conditions count by their actual rank on `E`, not by the number of equations.

For two domains with common graph-closed finite-codimensional intersection
`Ecap`, assuming a closed Fredholm realization on one and the same differential
expression on both, the other finite extension is Fredholm. With
`qi=dim(Ei/Ecap)`,

`ind D_E2 - ind D_E1 = q2-q1`.

Indeed restrict the first to `Ecap` and extend by a finite-dimensional complement
to the second; finite-dimensional extension adds its dimension to the index.
This is a relative **domain** formula. It makes no claim that all such domains
are compatible with an action, gauge complex, reality, or physical boundary law.

For an already justified elliptic APS problem, removing `q` independently
attainable allowed boundary modes is such a restriction. A finite-dimensional
spectral band and a trace/rank argument are needed. Noncompact boundaries can
have continuous spectrum; the mode-count shortcut does not apply there.
Changing the sign of a named adapted boundary operator while keeping a normal
symbol convention fixed is not automatically the boundary rule for `-D`.

## 3. Same principal symbol and domain can still have different indices

This independent analytic control attacks a stronger proposed transfer.
On the half-line use exactly the same spaces for every real `a`:

`Da=∂x+a : H1(0,∞) → L2(0,∞)`.

There is no boundary condition at zero. Graph norm and `H1` norm are equivalent
for each fixed `a`. The principal symbol is always `iξ`.

For `a>0`, the past-convolution right inverse is

`u(x)=∫_0^x exp(-a(x-t)) f(t) dt`.

Extension of `f` by zero and the L1 convolution bound give
`||u||2 ≤ ||f||2/a`; the equation gives `u'=f-au∈L2`. It is onto, and its
kernel is exactly the one-dimensional span of `exp(-ax)`. Thus `ind Da=1`.

For `a<0`, the future-convolution inverse is

`u(x)=-∫_x^∞ exp(a(t-x)) f(t) dt`.

The same bound is `||u||2 ≤ ||f||2/|a|`, with derivative controlled by the
equation. Homogeneous solutions grow and none except zero is in `L2`.
Thus `Da` is invertible and `ind Da=0`.

At `a=0`, the derivative is injective but not Fredholm. Take triangular
piecewise-linear functions supported in `[3n,5n]`, height one and slopes
`±1/n`, and normalize in `L2`. Their unnormalized squared norm is `2n/3` and
derivative squared norm `2/n`. Hence the normalized derivative norm squared
is `3/n²→0` while the function norm is one. If this injective closed operator
had closed range, its inverse into its graph-norm domain would be bounded,
contradicting this sequence. The change of index therefore crosses a genuine
non-Fredholm parameter; it does not violate Fredholm homotopy invariance.
The lower-order constant perturbation is not compact from this `H1` domain
to `L2`, as translating any fixed bump also shows.

This is an analytic control, not a class-C action witness. In particular a
half-line first-order scalar operator is not the specified Y14 RS/gauge/BV
system. It proves that a same-symbol/same-domain *abstract inference* is invalid
on noncompact spaces, not that C contains both indices.

## 4. Execute the boundary and modulo-three consumers

Impose `u(0)=0` on the same half-line spaces. Trace is onto and graph-continuous;
the restricted domain contains the dense compactly supported interior core.

| End coefficient | Unrestricted index | Zero-trace index | Mechanism |
| --- | ---: | ---: | --- |
| `a>0` | 1 | 0 | The decaying homogeneous kernel is removed; past inverse survives. |
| `a<0` | 0 | -1 | Kernel stays zero; range obeys `∫_0^∞ e^(at) f(t)dt=0`. |

For `a<0` this moment is a nonzero continuous functional, so the range really
has codimension one. This calculates the domain effect independently of
finite-dimensional rank examples. Fixing the phase to one leaves two distinct
index residues at the unrestricted endpoints; restricting the domain changes
them again without changing the differential expression.

For a general supplied index `N`, whole-operator phase cannot repair a wrong
residue. An admitted rank-`q` restriction gives `N-q mod3`; two commensurable
domains change it by `q2-q1 mod3`. A proposed mod-three law must therefore
constrain allowed relative domain dimensions (and end components), or supply
another mechanism that fixes them. It cannot infer a law from phase alone.
This does not authorize choosing boundary conditions to fit three.

## 5. Matrix consequence and remaining mathematical obligation

X-P2-P3 becomes **constrained**, not `decided_for_C` or `empty`. The required
bridge must specify P2's operation on the full graded operator, its closed
physical domain, and its asymptotic Fredholm component. A scalar phase on a
fixed realization has zero index effect. Relative domain dimensions and
noncompact lower-order end data are independently material. The actual C
realization and the physical readout remain unproved, so no two-datum floor,
independence of P2/P3, global GU verdict, or physical-family count follows.

The earlier relative-KO result supplies an input twist map, not an analytic
index; this work does not relabel it as one. The earlier X-P1-P2 weighted-weld
scope and X-D1-P3 local-system distinction remain unchanged.

## Verification and references

The companion exact probe reconstructs finite kernel/cokernel restriction
sequences, whole-scalar invariance and adjoint signs; symbolically verifies
half-line inverses, actual moment-compatible forcing and singular-sequence
integrals. Its half-line index table is a report of the written analytic
proof, not an independent numerical certification. No finite matrix proves
infinite-dimensional Fredholmness. Internal specialist review checks the proof
and strongest contrary case; no external-expert or Lean certification claimed.

- [Exact probe](../../tests/program-focus/x_p2_p3_phase_domain_probe.py).
- [Structured evidence](../../lab/process/x-p2-p3-phase-domain-index.json).
- [Prior relative KO input](selected-k77-relative-boundary-p3-ko-interface-2026-08-10.md).
- [Current weld scope](x-p1-p2-class-c-lift-2026-11-11.md).
- Bär and Ballmann, [Boundary Value Problems for Elliptic Differential Operators of First Order](https://archive.mpim-bonn.mpg.de/id/eprint/327/1/preprint_2011_2.pdf), Theorem1.18: elliptic boundary index changes and coercivity-at-infinity hypotheses. This is background for the applicability distinction; the graph-domain and half-line arguments above are given directly. Its elliptic hypotheses are not asserted for the ultrahyperbolic GU ambient operator.
