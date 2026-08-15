---
title: "Selected-K77 RSAP mixed-A2 factor and adjacent-transition type gate"
status: active_research
doc_type: exact_transverse_construction_and_transition_type_gate
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-mixed-real-form-and-transition-gate.json
probe: tests/channel-swings/selected_k77_rsap_a2_mixed_real_form_and_transition_gate_probe.py
grade: "ALL THREE REAL A2 PRINCIPAL FACTORS CONSTRUCTED; ADJACENT COMMON-REFINEMENT MAP TYPE-MISSING; GLOBAL RSAP OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP mixed-A2 factor and adjacent-transition type gate

## Result first

The mixed real form also constructs. The ten-dimensional Hamiltonian factor

```text
X_mixed = T*(SU(2,1)/SO(2,1))
```

maps onto `su(2,1)*`, has moment-differential rank eight above every regular
covector—including regular nilpotents and regular covectors with a non-real
conjugate eigenvalue pair—and has rank five at zero. Together with the split
`SL(3,R)/SO(2,1)` and compact `SU(3)/SO(3)` results, this completes the
principal symmetric-pair census for all three real forms of complex `A2`.

The conditional adjacent-gluing step does not yet close. It finds a precise
typing defect in the previously requested comparison: the rank-one wall chart
and the `A2` chart split four symplectic dimensions differently between their
leaf and transverse blocks. Their bare cotangent factors have dimensions 16
and 20, so equality of their tautological potentials is not even a statement
on a common domain. The next object is an explicit 20-dimensional common-
refinement symplectomorphism. Until it is built, the pairwise moment and
potential cocycles are `NOT-YET-TYPED`, not failed.

No global `98D` RSAP follows.

## Layer 0: mathematical carrier, not physical phase space

This is a mathematical Hamiltonian transverse factor for a Lie--Poisson
realization. It is not a source-owned GU boundary phase space, action-selected
subcarrier, stationary background, physical quotient or quantum state space.

Let

```text
q = diag(1,1,-1),
G = SU(q),
H = SO(q).
```

Writing an element of `su(q)` as `A+iB` with real matrices gives

```text
A^T q + q A = 0,
B^T q = q B,
tr A = tr B = 0.
```

Thus, as a real symmetric pair,

```text
su(2,1) = so(2,1) direct-sum i Sym_0(q;R).
```

The second five-plane is the annihilator of `so(2,1)` under an invariant real
trace pairing. Consequently

```text
T*(G/H) = G times_H ann(h),
mu([g,xi]) = Ad_g^*(xi),
rank(d mu_[e,xi]) = 8 - dim(h intersect g_xi).
```

The source dimension is `2(8-3)=10`, and equivariance makes `mu` Poisson.

## Complete mixed orbit coverage

For `X in su(q)`, set `Y=-iX`. Then `Y` is `q`-Hermitian:

```text
Y^* q = q Y.
```

Its characteristic polynomial is real, so in complex dimension three its
spectrum is either three real roots (with Jordan degenerations) or one real
root plus one non-real conjugate pair. The pseudo-Hermitian canonical forms
can be chosen with real matrices and real Lorentz Gram forms:

- real Jordan blocks use reverse-identity Gram blocks;
- distinct or repeated real semisimple blocks use diagonal Gram forms;
- a non-real pair `a plus/minus ib` uses the real block
  `[[a,-b],[b,a]]` with split Gram form `diag(1,-1)`;
- direct-sum signs are chosen to give total signature `(2,1)`.

All nondegenerate real symmetric forms of signature `(2,1)` are congruent.
Therefore a pseudo-unitary change of basis carries `Y` to a real
`q`-self-adjoint matrix `B`; equivalently it carries `X` to `iB` in the
annihilator. If the conjugator initially lies in `U(2,1)`, multiply it by a
central unit scalar whose cube corrects its determinant. This does not change
the conjugation and places it in `SU(2,1)`. Hence

```text
Ad_SU(2,1)(i Sym_0(q;R)) = su(2,1),
```

so the mixed moment map is onto.

## Regular and origin ranks

Take a regular annihilator representative `xi=iB`. If a real
`A in so(q)` commutes with `xi`, then it commutes with `B`. Regularity makes
the real centralizer the trace-free polynomial algebra in `B`. Every real
polynomial in a `q`-self-adjoint matrix is `q`-self-adjoint, whereas `A` is
`q`-skew. Their intersection is zero. Thus

```text
rank(d mu)=8
```

above every regular value. This covers the regular nilpotent size-three block
and the non-real-pair semisimple block, not merely diagonal samples. At zero,
all three isotropy directions stabilize the covector, so

```text
rank(d mu_0)=8-3=5.
```

Composed with the `78D` leaf and `T*R^5`, the mixed chart has the same exact
schedule as the split and compact charts: carrier dimension `98`, map rank
`91` over regular `A2` values, and map rank `88` at the `A2` origin.

## The first actual adjacent-transition gate

The old wording “compare the cotangent potentials” omitted a necessary common
domain. The neighboring rank-one and `A2` descriptions are

```text
rank-one chart: S_82 x X_4(A1) x T*R^6,
A2 chart:       S_78 x X_10(A2) x T*R^5.
```

Both total 98 dimensions, but their displayed transverse blocks do not:

```text
dim(X_4 x T*R^6) = 16,
dim(X_10 x T*R^5) = 20.
```

The missing four dimensions are not an error; they are the orbit directions
that move from the `82D` leaf to the transverse `A2` model near the adjacent
intersection. Extracting the common `78D` leaf makes the required transition
object explicit:

```text
Phi:
O_4 x X_4(A1) x T*R^6  --->  X_10(A2) x T*R^5,
```

where both sides are 20-dimensional. `Phi` must be a symplectomorphism on the
common regular overlap, intertwine the full `A2 plus R^5` moment map, and pull
back the target tautological potential to the source potential up to the
declared exact gauge term. Neither the previous `A1` factor nor the new `A2`
factor specifies `O_4`, its embedding, the centre-coordinate conversion, or
this map. Directly equating the bare factor potentials would compare forms on
different-dimensional spaces and is invalid.

This is a `TYPE-MISSING` transition, not a nonexistence theorem and not a
nonzero Cech defect. The first noncommuting triple remains dependency-blocked
until pairwise `Phi` maps exist.

## Hostile scope and claim ceiling

The strongest overclaim would be “all adjacent `A2` overlaps are solved.” The
factor census is solved; the transitions are not. The strongest contrary
possibility is that one pseudo-Hermitian orbit type does not meet the real
slice; the canonical-form census includes real semisimple, repeated/Jordan,
regular nilpotent and non-real-pair blocks, and the determinant-one adjustment
closes the `U` versus `SU` seam. The weakest reproducibility seam is that the
global coverage step uses the standard pseudo-Hermitian canonical-form theorem
rather than a finite enumeration of all matrices; the executable probe checks
every canonical block family and the two adversarial regular controls exactly.

Deeper strata, zero charge, the rank-at-most-49 zero gate, the global carrier,
physical stationarity, cohomology, spectrum and Standard Model selection all
remain open. The `182D` cotangent parent remains the all-charge fallback. No
ledger, canon, residue, quotient, datum or public posture changes.

## Next exact gate

Construct the common refinement `Phi`. Fix one adjacent root embedding,
identify the four-dimensional orbit-transfer block `O_4`, write both full
moment maps into the same `sl(3)^* plus R^5` coordinates, and solve the
symplectic/potential pullback equations. Only a passing pair map licenses the
first noncommuting triple Cech test.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_mixed_real_form_and_transition_gate_probe.py
```

The probe uses exact integer and rational linear algebra only.
