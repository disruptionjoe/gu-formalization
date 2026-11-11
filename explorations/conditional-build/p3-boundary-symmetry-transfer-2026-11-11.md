---
title: "P3: symmetry must survive the full boundary realization"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: P3xsymmetry
tier: T2
expected_delta: "Refine constrained cell with an exact operator-and-domain transfer criterion."
actual_delta: "Constrained: parallel symmetry, full operator intertwining and spectral-domain preservation are separate; an interior quaternionic symmetry permits an odd index when the boundary breaks it."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# A symmetry of the carrier need not be a symmetry of its index problem

**Result.** In a structurally specified analytic subfamily, the symmetry used
to constrain an index must intertwine the **full operator** and preserve its
closed domain. For a selfadjoint adapted boundary operator B with compact
resolvent, an antiunitary J commuting with B preserves the allowed spectral
trace space `E_<0(B) ⊕ L`, `L ⊂ ker B`, exactly when `JL=L`. If J instead
anticommutes with B and a negative eigenspace is nonzero, it exchanges negative
and positive modes and does not preserve this one-sided condition. These are
transfer requirements, not a realized class-C index or a physical count.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P3xsymmetry
tier: T2
expected_delta: Refine the existing symmetry requirement at its analytic transfer.
actual_delta: Full operator and boundary preservation isolated; no class-wide verdict.

```gu-typed-objects
result: boundary-symmetry-transfer
carrier: complex Hilbert graph domain and spectral boundary trace space LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form for spectral theorem ON=declared_carrier
real_structure: antiunitary J with specified square; separate from a moving geometric complex structure
grading: source and target of complex Fredholm operator, not observed family labels
action_owner: repository-construction -- structural analytic subfamily; no field action supplied
target: preserved closed boundary domain MAP-TYPE=inclusion
```

## 1. What is reused, and what is added

The [earlier symmetry result](p3-symmetry-relative-domain-2026-11-11.md) already
proves the equivariant relative-index formula and distinguishes real from
quaternionic dimensions. The [phase/domain result](x-p2-p3-phase-domain-index-2026-11-11.md)
owns the half-line analytic argument. We do not present these as new theorems.
K2221's periodic descent and K2203/K2233 already separate local invariance
from holonomy. The new consumer is the missing chain from a carrier symmetry
to the **chosen spectral cut and zero modes**, with an exact odd-index
countercontrol and its composition with the multiplicity weld.

For a connected base and connection, parallel linear endomorphisms correspond
to the commutant of full holonomy at one point. An antilinear map `J=A conjugation`
instead obeys `A conjugate(h)=h A` for every holonomy element h. Necessity follows
by transporting around loops; sufficiency follows by transporting A along any
path, with loop invariance making the result path-independent. This standard
principle is reused. The relevant group is actual holonomy, not the declared
gauge group acting also on the connection.

As fibre controls, full standard U(p,q) holonomy includes `iI` and hence permits
no nonzero parallel antilinear endomorphism: `A(-iI)=iA`. The complex standard
SU(3) representation has the same conclusion using its nonreal central cube
root. The SU(2) standard representation admits `J=epsilon conjugation`,
`epsilon=[[0,-1],[1,0]]`, with square -I. These statements do not assign any of
these holonomy groups to C. They also do not exclude moving gauge-covariant
J fields or conjugate-summand exchange. An indefinite U(p,q) form is not the
positive Hilbert form needed below.

## 2. Exact domain transfer

Assume a graph-norm-continuous trace map `gamma:E_max→H_trace` is surjective onto the trace space
under consideration and intertwines bounded invertible J actions. Define
`E_W={u∈E_max: gamma(u)∈W}` for a closed trace subspace W. Assume J preserves
E_max and the full operator satisfies `D J_E=J_F D` there. Then

`J_E E_W=E_W  iff  J_trace W=W`.

The forward implication uses surjectivity: lift every w∈W to u∈E_W. The reverse
implication follows by applying gamma to Ju and to J inverse. Without a
surjective trace, only the attained trace intersection can be tested. This
theorem by itself supplies neither Fredholmness nor elliptic regularity.

Now let B be selfadjoint with compact resolvent on the positive boundary
Hilbert space, and let antiunitary J preserve Dom(B). If `BJ=JB`, every real
eigenspace is J-invariant. Consequently `E_<0(B)` and ker B are invariant, and
`W=E_<0(B)⊕L` is invariant iff L is. The same argument applies in the spectral
Sobolev norm because J preserves eigenvalues. If `BJ=-JB`, a negative
eigenvector maps to a positive one. It cannot lie in W, so W is not invariant
when the negative spectrum is nonempty. The zero-only case still depends on L.
For linear unitary symmetries the commuting case is identical. A subspace
L is only a spectral trace choice here: selfadjoint boundary admissibility
additionally requires the applicable Green-form/Lagrangian condition. No
arbitrary L is declared admissible for a selfadjoint problem.

Full B matters. A lower-order selfadjoint perturbation can fail to commute
with J while leaving the principal symbol unchanged. For example, take a
supplied real selfadjoint boundary operator B0 and tensor it with C²;
J acts by epsilon-conjugation on the C² factor and conjugation on the real
B0 factor. Adding `I tensor diag(1,-1)` breaks commutation. One abstract B0
is `[[0,∂],[-∂,0]]` on periodic real two-component sections, complexified.
These are independent boundary-operator controls, not C realizations.

## 3. A genuine odd index despite quaternionic interior symmetry

Take `D=∂x+1` from `H¹(R_+,C²)` to `L²(R_+,C²)`. Its full differential
expression commutes with constant quaternionic J. For **any** linear subspace
L⊂C² impose `u(0)∈L`. The domain is closed since trace is continuous. The
zero-initial solution

`u(x)=∫_0^x exp(-(x-t)) f(t) dt`

belongs to this domain, is bounded L²→H¹ (Young's inequality and `u'=f-u`),
and solves Du=f. The kernel is `exp(-x)L`. Therefore this realization is
Fredholm, surjective, and has complex index dim L. Its trace realizes every
element of L. For L=span(e1), the index is **one** and J sends L to span(e2),
so the domain is not J-invariant. For L=0 and C² the indices are zero and two
and J is preserved. Nothing contradicts quaternionic parity: the odd
realization lacks the theorem's domain hypothesis. This is an abstract analytic
control, not an action in C and not an asserted APS realization on Y14.

## 4. Spectral cuts and actual finite transitions

In an independently supplied elliptic, coercive-at-infinity setup with an
adapted selfadjoint B, let the **allowed** boundary values be `E_<a(B)`.
Increasing the cut from a to b adds the finite spectral band `[a,b)`.
Provided the trace/domain and Fredholm hypotheses hold, the earlier relative
index theorem gives `index(D_b)-index(D_a)=dim E_[a,b)(B)`. This fixes the
sign convention: more allowed boundary values increase the index.

This is the setting of Bär–Ballmann, *Guide to elliptic boundary value problems
for Dirac-type operators*, Example 3.21, Corollary 4.2 and Example 4.3
([primary text](https://archive.mpim-bonn.mpg.de/id/eprint/1180/1/preprint_2013_44.pdf)).
Their hypotheses are not imported into Lorentzian/ultrahyperbolic Y14.
If a preserved quaternionic J commutes with B, each full band has even complex
dimension; a chosen subspace of its zero eigenspace can break this preservation.
Even full-band dimensions still give no divisibility by three. No varying-B
spectral-flow formula or family-index realization is asserted here.

## 5. Composition and program consequence

The [multiplicity weld](x-p1-p2-multiplicity-weld-2026-11-11.md) supplies a
pointwise candidate coflip only after all coefficient/naturality arrows,
invertibility, square and pairing constraints are imposed. To use it for P3
one must additionally prove connection descent, full operator intertwining,
trace intertwining and preservation of the chosen W. Only then can it act on
kernel/cokernel and invoke the earlier representation or parity constraints.
A symbol-compatible involution can fail at any later step. Conversely a failed
particular boundary cut does not exclude other admissible cuts.

`P3xsymmetry` remains constrained with this sharper requirement. `X-P2-P3`
retains its phase/domain/asymptotic distinction. SC-CHI-01/51 ASSERT the
nonchiral-total/effectively-chiral goal and SC-GEN-02/03/54 ASSERT their native
2+1/extension claims; these analytic controls adjudicate neither. RA-F1 and
AC-F1 remain NEEDS. No source, physics ledger, C declaration or canon changes.

## Verification

[Exact controls](../../tests/program-focus/p3_boundary_symmetry_transfer_probe.py)
check holonomy intertwiners, spectral-sign and zero-space preservation,
lower-order symmetry breaking, and trace/kernel calculations. The infinite
half-line proof is the written argument above, independently reviewed, not a
finite matrix certification. [Evidence](../../lab/process/p3-boundary-symmetry-transfer.json)
records finite checks separately from analytic acceptance.
