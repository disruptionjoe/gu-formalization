---
title: 'P3: closed auxiliary domains and family cancellation'
status: active_research
doc_type: exploration
created: '2026-11-11'
program_target: X-P2-P3
tier: T2
expected_delta: derive a structural-subfamily constraint; no full-C decision
actual_delta: 'constrained: exact endpoint-domain reduction and contraction criterion;
  fixed-expression families carry a boundary-bundle index obstruction'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: No class-C witness or exclusion, source verdict, physical state or
  generation count
scripts:
- tests/program-focus/p3_auxiliary_domain_family_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. No conventional-index conclusion is
transported to the native two-true-plus-effective-imposter observation construction.
SC-GEN-02/03/54 ASSERTS the native generation/supercharge claims; SC-CHI-01/51 ASSERTS
the nonchiral-total/effectively-chiral split with the source's stated qualifications.
This note does not adjudicate those claims. RA-F1, AC-F1 and LT-SM8 remain NEEDS.

```gu-typed-objects
result: p3-auxiliary-domain-family
carrier: smooth finite-rank bundles and explicitly defined compatibility or Hilbert complexes LAYER=UNTYPED (no physical identification) CHIRALITY=N/A
pairing: auxiliary Hermitian Hilbert pairing where used ON=declared_carrier
real_structure: real or complex coefficient bundles as stated; complex family K theory only
grading: complex degree, optional commuting internal grading; not physical chirality
action_owner: N/A -- structural subfamily theorem, no action constructed
target: X-P2-P3 MAP-TYPE=homomorphism
```

## Native bookends

program_target: X-P2-P3
tier: T2
expected_delta: derive a structural-subfamily constraint; no full-C decision
actual_delta: constrained: exact endpoint-domain reduction and contraction criterion; fixed-expression families carry a boundary-bundle index obstruction

## Question and prior evidence

When may a purported auxiliary or gauge pair be removed without changing its
closed complex, and what survives when endpoint data vary in a family? Equal
carrier ranks and equal numerical indices do not answer this. We classify the
entire two-endpoint interval category below and execute its global-family test.
This is a structural analytic category, not an action, GU end model, APS
realization or physical ghost complex.

The [relative-domain theorem](p3-symmetry-relative-domain-2026-11-11.md) already
owns scalar/equivariant finite trace defects. The [mixed-twist result](p3-family-index-mixed-twist-2026-11-11.md)
already separates numeric and family index. [K471](k471-k77-effective-homology-transfer-2026-09-25.md) supplies finite homological
elimination, and [K89](k89-observed-functional-bfv-domain-lift-wave-2026-09-01.md) already shows why finite inverses do not imply a bounded
infinite-dimensional inverse. None is counted as new here. The new analytical
endpoint is an explicit bounded chain reduction for all endpoint subspaces,
including jumping intersections, and a family obstruction arising only from
boundary bundles while the differential expression stays fixed.

## 1. Exact closed-domain classification

Let V be a complex finite-dimensional Hilbert space, dim V=r, and U,W linear
subspaces. Consider the two-term complex D=D_(U,W),

    Dom D = {u in H1([0,1],V): u(0) in U, u(1) in W},
    D u = u',                    target L2([0,1],V).

H1 is equipped with its usual norm, equivalent to the graph norm of D.
Trace continuity gives a closed domain condition. D as an unbounded operator
on L2 is densely defined and closed. Define L2_0={g: integral_0^1 g=0}.
There is a bounded invertible graph-space map

    U (+) W (+) L2_0 -> Dom D,
    (c,w,g) -> c + x(w-c) + integral_0^x g(t)dt.

The inverse is c=u(0), w=u(1), g=u'-(w-c). With L2 identified as V (+) L2_0
by average and mean-zero part, the differential becomes

    ((c,w),g) -> (w-c,g).

Thus it is the finite complex T:U (+) W -> V, T(c,w)=w-c,
plus an identity complex on L2_0. Boundedness follows from trace estimates and
Cauchy--Schwarz for the integral; all formulas are explicit. It follows that
the range is closed, kernel and cokernel are finite, and

    H0 = U intersection W,
    H1 = V/(U+W),
    ind D = dim U + dim W - r.

The index is the Euler characteristic of THIS complex, not a chiral family
count. There is no discretization or unproved continuum limit in this argument.

## 2. Complete contraction criterion and actual repair

The pair is contractible iff V=U direct-sum W. Necessity follows from H0=H1=0.
For sufficiency let P_U be projection onto U along W. The inverse

    (h f)(x) = -P_U integral_0^1 f(t)dt + integral_0^x f(t)dt

is bounded L2->H1, meets both endpoint conditions, and obeys D h=I and h D=I
on the stated spaces. It is a domain-respecting contraction, not just a fibre
inverse. The finite reduction above remains valid when complementarity fails.

Exact contrary example: U=W=span(e1) in C². The scalar index is zero but H0 and
H1 are each one-dimensional. Equal index therefore does not establish pair
removal, even when all dimensions are finite. Changing W to span(e2) supplies
the complementary-domain repair and the displayed inverse. That changes the
boundary data; it does not retroactively validate removal on the old domain.

The unrestricted/unrestricted, zero/unrestricted and zero/zero endpoint choices
have indices r,0,-r respectively. These recover old relative-domain intuition;
their novelty here is their inclusion in one full analytic classification.

## 3. Released family classification and boundary-only obstruction

Let V be a finite-rank Hermitian vector bundle over a compact base B and U,W
continuous vector subbundles. Form the interval Hilbert bundles fibrewise.
The same explicit isomorphisms continuously reduce the family to T plus I,
even if dim(U_b intersection W_b) jumps. Therefore the family index is

    Ind D = [U]+[W]-[V] in K0(B).

If U_b and W_b are complementary everywhere, T is a bundle isomorphism; its
inverse is continuous and uniformly bounded on compact B. The formulas above
then provide a continuous uniformly bounded family contraction. Conversely
a contraction on every fibre requires complementarity. Vanishing family
K-class alone is not sufficient: the constant U=W=line example already has
class zero but nonzero cohomology.

Take B=CP1, V=trivial C², U=L the tautological line, and W a fixed trivial line.
Each fibre has numerical index 1+1-2=0, but

    Ind D=[L]-1, with first Chern class c1(L)=-1.

Hence the family class is nonzero. At the unique parameter where L=W, both
kernel and cokernel appear; elsewhere the endpoints are complementary. The
differential expression u' and its principal symbol never change. This is a
boundary-domain family obstruction, distinct from a bulk mixed-twist example.

For a direct clutching check, local frames for L over the two projective charts
may be chosen (1,z) and (w,1), w=1/z. The first equals z times the second on
the overlap; the transition has unit winding (with c1(L)=-1 in the tautological
convention). Nonzero winding, rather than its sign convention, detects the
nonzero reduced class. The exact probe checks the frame relation and unit-
circle differential; the topological conclusion uses the stated clutching
argument, not a floating-point loop sample.

An actual family repair sets W=L-perp. Both endpoint lines are then nontrivial,
but L (+) L-perp=V and the orthogonal projection P_L is global and norm one.
The inverse above is uniformly bounded and contracts every fibre. This
explicitly distinguishes repair of the boundary family from inserting an
unjustified rank cancellation. It also shows that nontrivial endpoint bundles
do not themselves prevent contraction: their relative position matters.

## 4. Grading and physical transfer

A domain-preserving bounded chain homotopy is a sufficient certificate for
cohomology cancellation. It is not the only way two indices may be equal.
For general unbounded complexes, every chain map and homotopy must be bounded
in the appropriate graph norms and every composition must be defined.

If an additional degree-zero involution Gamma on V preserves U,W and commutes
with the interval differential, the same formulas split into its plus and
minus bundles. The refined indices are [U_plus]+[W_plus]-[V_plus] and likewise
minus. Arbitrary endpoint choices need not preserve Gamma. Example: Gamma=
diag(1,-1), U=span(1,1), W=span(1,-1) contracts the ungraded complex but neither
endpoint line is Gamma-invariant, so no inherited Gamma grading exists on that
domain. The contraction does not certify a chiral reduction.

Even a compatible internal grading is not automatically the source's observed
chirality. Euler characteristic, degree-zero cohomology and a physical family
observable are distinct. This boundary calculation cannot choose the raw RS
versus ghost-subtracted symbol, establish BV nilpotency, or construct a positive
physical Hilbert space.

## Matrix consequence

P3xglobal_index and X-P2-P3 gain a complete analytic domain-category criterion:
auxiliary cancellation in this category is equivalent to endpoint
complementarity, and a family-index comparison must retain the actual endpoint
bundle classes. Any transfer to C needs the actual coupled complex, closed
boundary domain and observation/physical grading bridge. No such realization
is asserted and the original family/action gates remain. The scalar equality
test cannot close them; the explicit complement-family repair is usable only
if the target's genuine boundary requirements admit it.

## Reproduction and acceptance

Run [the exact probe](../../tests/program-focus/p3_auxiliary_domain_family_probe.py). Its [saved report](../../lab/process/p3-auxiliary-domain-family.json)
contains supporting identities and contrary controls, not a numerical proof of
all smooth operators or Hilbert families. Universal statements above have written
proofs; independent internal specialist and hostile reviews completed with substantive findings empty. No Lean
or external-expert certification is claimed for this Tier-2 result.
