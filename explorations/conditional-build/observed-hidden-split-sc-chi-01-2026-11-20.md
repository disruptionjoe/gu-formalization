---
title: "Observed and hidden index split — step 1 scope audit"
status: exploration
doc_type: audit
created: '2026-11-20'
program_target: X-P1-P2-P3
tier: T3
expected_delta: Precisely scope a reusable hypothesis or construction fork without a scientific verdict
actual_delta: Conditional statement scoped; no automatic finite-to-Fredholm transfer; packet survives
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Observed and hidden index split — step 1 scope audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2-P3
tier: T3
expected_delta: Precisely scope a reusable hypothesis or construction fork without a scientific verdict
actual_delta: Conditional statement scoped; no automatic finite-to-Fredholm transfer; packet survives

**Step 1 only; internal T3 audit of existing results.** Base revision `2ff923d10efdbc00b878512901c982185dcd6bef`.
[Packet](../../lab/process/work-packets/observed-hidden-index-split-2026-11-20.md). No P3 row retyping, new Lean theorem, carrier realization,
mirror-matter test, source verdict or paper addendum has been accepted here.

```gu-typed-objects
result: Conditional observed-hidden index statement and applicability audit
carrier: supplied two-term graded Banach Fredholm complexes; finite Krein W is a distinct carrier LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: positive auxiliary topology for Fredholm theory; independently specified nondegenerate Hermitian Krein form for finite theorem ON=declared_carrier
real_structure: complex category first; K77/K95 and physical conjugation transfers remain explicit obligations
grading: degree0 source and degree1 target of the same complex; not automatically ambient Weyl, observed weak chirality or ghost grade
action_owner: N/A -- reuses an existing conditional exact-sequence result, no action built
target: observation contraction with domain and target quotient maps MAP-TYPE=restriction
```

## 1. Four different classes and three different invariants

- **S** in `canon/antilinear-bound-RESULTS.md`: antilinear endomorphisms
  C=M conjugation on the supplied complex W, A1 carrier preservation and
  A2 M†KM=λ conjugate(K), real λ≠0. K is nondegenerate Hermitian,
  KΓ=-ΓK, its chiral halves are complementary isotropic subspaces; the
  physical comparison subspace is strictly K-positive. A3 (C²=±I) and A4
  (chiralizer shape) are refinements, not premises of the finite bound.
- **C_fin / C_inv** in the corrected paper and
  `canon/enum-completeness-class-c-RESULTS.md` are finite encoded/covariant
  construction categories, not the current action class.
- **Action C v1** is `lab/process/action-class.json`. It permits typed external
  P1/P2/P3 data. Neither nonemptiness nor a balanced Fredholm realization is
  certified merely by that declaration. Quantification over S is not over C.
- **F_obs**, used below, is the structural subclass of supplied compatible
  Fredholm observation complexes. Applying it to C requires proving that the
  chosen C realization has these properties; no specific action is constructed.

The July 23 correction in the antilinear canon and the current Lean module
`Lean/GUFormalization/LocatedNotForcedLegs.lean` identify the finite invariant
as **intersectionDifference**: difference of intersection dimensions of a
positive subspace with the two isotropic halves. It is not a Fredholm index.
The function-space notes concern paired spectral flow / spectral projections
and model boundary/family calculations. Their explicit true-RS-Y14 transfer
caveat remains. Neither a zero spectral flow nor the index of the full
self-adjoint operator is automatically the chiral-block index being added.

Thus the proposed implication “Located, Not Forced ⇒ ind D=0 throughout
current action C” is **not established** by these citations. The useful joint
statement retains `ind D=0` as an explicit, separately justified premise.
This respects the corrected manuscript's prohibition on unqualified “net
chiral index conservation”; it is not a reversal of the finite theorem.

## 2. Precise joint statement (reuse of November 11 §3)

Let D:E→F be bounded Fredholm between Banach spaces, with E the graph-norm
space of the actual closed degree0→degree1 operator when it is unbounded.
Fix that grading. Let qE:E→Eo and qF:F→Fo be **continuous surjections** onto
Banach spaces. Put Eh=ker qE and Fh=ker qF, with their closed induced
subspace topologies. Suppose Do:Eo→Fo is bounded, qF D=Do qE, and both
Dh=D|Eh:Eh→Fh and Do are Fredholm. These are the short exact sequences in
each degree; intertwining makes them an exact sequence of complexes.

The already-owned connecting sequence is

    0 → ker Dh → ker D → ker Do → coker Dh → coker D → coker Do → 0.

Alternating finite dimensions give ind D=ind Dh+ind Do. **If, in this same
index convention and realization, ind D=0 and ind Do=N, then ind Dh=-N.**
For an alleged physical count, additionally supply the map identifying N with
that count; the algebra does not supply it. Acyclic hidden cohomology implies
N=0; a nonzero N needs non-acyclic hidden cohomology. Observed zero modes need
not lift to total zero modes: the connecting map can be nonzero.

For a graded Hilbert formulation D is the chosen chiral block D⁺, not the
whole self-adjoint doubled operator. State actual domains, boundary/end
prescriptions, reality and grade compatibility on all three complexes.
Krein compatibility is not a substitute for Fredholmness in those topologies.
A **sufficient additional way** to justify balanced total is the existing
paired operator structure with a genuine degree-exchanging kernel/cokernel
identification on the full closed domains. Finite ranks or a formal bulk
symmetry do not certify this identification. No new global theorem is
claimed by this audit.

## 3. Is observation an interior operator in the theorem?

**A proper observation quotient is not a member of S.** S consists of
invertible antilinear self-maps of one fixed W: A2 and nondegenerate K imply
injectivity, hence bijectivity in finite dimension. A surjective quotient
with nonzero kernel changes carrier and is noninvertible; it cannot satisfy
that same A2 identity with nondegenerate source form. Nor is qE/qF a
covariant endomorphism merely because the bundle contraction is natural.
A choice of section could turn a quotient into a noninvertible projector,
but no choice makes it a conformal Krein automorphism. Source observation
is contraction, not an arbitrary physical projector.

That type distinction is **not proof of physical admissibility or of nonzero
observed index**. A quotient might independently inherit the same balancing
symmetry, in which case its own index can still vanish. If both q maps are
isomorphisms, the observed complex has the total index and cannot realize
N≠0 at total0. If the actual quotient preserves the relevant balancing
structure on its domains, test that structure rather than treating every
quotient as an escape. If physical positivity is claimed, also prove the
induced pairing/physical-state construction; a nondegenerate form does not
automatically descend through a nonzero kernel.

The exact finite example already in November 11 §5D has D=0:C²→C²,
qE onto C and qF onto0: total0, observed+1, hidden−1. It shows that the
abstract Fredholm hypotheses do **not** force observed0. It is not an
inhabited C action or a source realization. §5E supplies the nonzero connecting
map countercontrol; §5's weak-current correction shows that observed weak
chirality need not be a nonzero index at all. These are reused, not discoveries.

## 4. Source match and explicit routes

SC-CHI-01/03/50/54 describe nonchiral total versus luminous/dark or effectively
chiral observations. SC-CHI-51/52 retain the VEV/curvature decoupling mechanism,
and SC-CHI-53 its hedged reconnection claim. They do not select our Banach
complex, index convention or count map. The conditional compensation relation
is a **necessary-condition match in F_obs**, compatible with that shape; it
neither confirms the mechanism nor says every effective-chirality mechanism
must be an exact index quotient. `hidden index -N` does not yet mean N mirror
families, dark matter abundance or exact parity-paired particle spectra.

| Route | Obligation retained |
|---|---|
| T04 | q must come from the actual section contraction, then be extended to the chosen graph-domain spaces; no free projection. |
| T06 | Ambient Weyl halves, observed weak grading, two true families and effective imposter remain distinct; attach the actual count map. |
| T11 | Continuous surjectivity, closed kernels, intertwining and all three Fredholm realizations must hold on the stated domain/end. |
| T14 | Integer chiral-block index differs from finite intersectionDifference and from torsion rho; ordinary and family indices remain distinct. |

## 5. Disposition

**Neither packet kill condition fires.** Proper quotient membership in S is
excluded by type, but no realization of action C with the required hypotheses
has been proved or disproved. No cell status, P3 row, source claim, class C or
paper verdict moves. The overstrong *automatic* finite-nullity-to-Fredholm
inference is rejected. The packet remains executable with its explicit
balanced-total premise and its concrete-carrier check still outstanding.

Step2 can now assess conditional candidate typing while retaining the old
external-count rival. If it changes the row, apply T1 before acceptance.
The exact finite checks in `tests/program-focus/priority_packets_probe.py`
are controls only; no Lean or analytic certification is claimed this session.
