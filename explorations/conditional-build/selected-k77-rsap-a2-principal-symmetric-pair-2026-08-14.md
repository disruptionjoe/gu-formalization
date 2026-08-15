---
title: "Selected-K77 RSAP A2 principal symmetric-pair construction"
status: active_research
doc_type: exact_transverse_construction
created: "2026-08-14"
registry: lab/process/selected-k77-rsap-a2-principal-symmetric-pair.json
probe: tests/channel-swings/selected_k77_rsap_a2_principal_symmetric_pair_probe.py
grade: "SPLIT AND COMPACT 10D A2 TRANSVERSE FACTORS CONSTRUCTED; MIXED REAL FORM, ADJACENT COCYCLES, AND GLOBAL RSAP OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP A2 principal symmetric-pair construction

## Result first

The regular-nilpotent defect found in `T*(SL(3,R)/SL(2,R))` is not a
universal adjacent-`A2` obstruction. It is an isotropy-choice defect.

Replacing the block `SL(2,R)` by the principal symmetric subgroup gives

```text
X_split = T*(SL(3,R)/SO(2,1)).
```

This is ten-dimensional, its moment map is onto `sl(3,R)*`, its differential
has rank eight above every regular covector—including every regular
nilpotent—and it has the required rank five over zero. The compact analogue
`X_compact=T*(SU(3)/SO(3))` has the same dimension and rank schedule and is
also onto. Thus the split and compact real `A2` transverse factors both
construct at the sharp `98D` total-carrier ceiling.

The mixed real form `su(2,1)`, adjacent-chart potential gluing, the first
noncommuting triple cocycle, deeper strata, zero charge and a global RSAP all
remain open.

## Typed object and construction fork

The object is a mathematical Hamiltonian transverse factor for a local
Lie--Poisson realization, not a source-owned physical phase space. For a Lie
group `G` and a three-dimensional subgroup `H`, the canonical cotangent moment
map is

```text
mu : T*(G/H) -> g*,       mu([g,xi]) = Ad_g^*(xi),
```

with `xi` in `ann(h)`. Its source dimension is `2(dim G-dim H)=10`, its image
is `Ad_G ann(h)`, and at `[e,xi]`

```text
rank(d mu) = dim(g) - dim(h intersect g_xi).
```

Because this is an equivariant Hamiltonian moment map, it is Poisson. The
entire gate is coverage plus isotropy rank; no physical symplectic form,
action owner, boundary law or quotient is imported.

## Split construction

Take `q` to be a Lorentz form of signature `(2,1)` and

```text
h = so(q),
p = {A in sl(3,R) : A^T q = q A}.
```

Under the trace pairing, `p=ann(h)`, and `sl(3,R)=h+p` with dimensions `3+5`.
For exact computation use the reverse-identity form

```text
q = [0 0 1]
    [0 1 0].
    [1 0 0]
```

The annihilator consists of the trace-free persymmetric matrices

```text
xi = [ a   u   v]
     [ r  -2a  u].
     [ s   r   a]
```

This resembles the failed block-`SL2` arrowhead, but its principal isotropy is
different and that difference is decisive.

### Coverage is global

Every real `3x3` matrix is self-adjoint for some nondegenerate symmetric form
of signature `(2,1)`. This follows blockwise from real Jordan normal form:

- a real Jordan block is symmetrized by its reverse-identity matrix;
- a `2x2` complex-pair block is symmetrized by a split diagonal form;
- direct sums can be signed so the total form has signature `(2,1)`.

If `A^T Q=Q A` and `Q=S^T q S`, then `S A S^-1` is `q`-self-adjoint. Hence
every traceless real matrix is conjugate into `p`, so
`Ad_SL(3,R)(p)=sl(3,R)`. The moment map is surjective.

### Every regular value is submersive

If `xi` is regular in `sl(3,R)`, its centralizer is the two-dimensional
trace-free part of `R[xi]`. Since `xi` is `q`-self-adjoint, every polynomial
in `xi` is `q`-self-adjoint. But `h=so(q)` consists of `q`-skew operators. In
characteristic zero their intersection is zero. Therefore `rank(dmu)=8` at
every regular `xi` in the annihilator, and equivariance transports this over
the complete regular target.

The adversarial control is the regular nilpotent Jordan block

```text
N = [0 1 0]
    [0 0 1].
    [0 0 0]
```

It obeys `N^T q=qN`, has `N^3=0`, `N^2!=0`, and has centralizer dimension two.
Unlike the block-`SL2` model, its intersection with the principal `so(q)` is
zero, so the moment differential retains rank eight. At `xi=0`, the whole
three-dimensional `h` stabilizes and `rank(dmu_0)=8-3=5`, exactly the required
`A2`-origin rank.

## Compact construction

For `G=SU(3)` take the fixed subgroup `H=SO(3)`. Under the invariant real
pairing,

```text
su(3) = so(3) direct-sum i Sym_0(3,R).
```

The second summand is `ann(so(3))`. Every skew-Hermitian traceless matrix is
unitarily diagonalizable, and an imaginary diagonal traceless matrix lies in
`i Sym_0(3,R)`. Thus the moment map from `T*(SU(3)/SO(3))` is onto.

A regular compact covector has three distinct imaginary eigenvalues. In a
real symmetric representative, any real skew matrix commuting with it
vanishes. Hence the stabilizer intersection is zero on the regular locus and
the differential rank is eight; at zero it is five. Compact `su(3)` has no
nonzero nilpotent orbit, so the split regular-nilpotent control has no compact
analogue to pass.

## Composition into the 98D schedule

At an adjacent `A2` overlap, the ambient transverse decomposition has a `78D`
symplectic leaf, one `10D` factor above, and `T*R^5`. Thus the carrier has
dimension `78+10+10=98`. Over regular `A2` values the complete moment rank is
`78+8+5=91`, over target Poisson rank `78+6=84`. At the `A2` origin it is
`78+5+5=88`, over target rank `78`. Rank loss there is permitted by the RSAP
contract.

## Hostile scope and claim ceiling

The strongest overclaim would be “the adjacent overlap is solved.” It is not.
This result constructs the required split and compact transverse factors. It
does not identify transition symplectomorphisms from neighboring rank-one
charts or prove equality of their tautological potentials and moment maps.

The strongest contrary route is the mixed real form `su(2,1)`. The compact
spectral proof and real Lorentz-self-adjoint proof do not automatically cover
its noncompact unitary orbit types. It remains an explicit third case.

The weakest reproducibility seam is split global coverage. The probe checks a
complete real-Jordan block symmetrizer census, not only semisimple samples.
The classification step remains a theorem-level argument rather than a finite
enumeration of all matrices.

No global `98D` RSAP, noncommuting cocycle, deeper-stratum chart, zero-charge
rank-`49` construction, physical superposition space, stationary background,
cohomology, spectrum or Standard Model selection follows. The `182D`
cotangent parent remains the all-charge fallback. No ledger, canon, residue,
quotient, datum or public posture changes.

## Next reverse gate

Complete the real-form census at `su(2,1)`. Test the principal symmetric-pair
candidate, if one exists with a five-dimensional quotient, against every real
semisimple and regular-nilpotent orbit type. If it passes, construct the actual
adjacent transition maps and compare cotangent potentials and moment
components before testing the first noncommuting triple Cech cocycle. If it
fails, classify noncotangent or multicomponent `10D` alternatives without
reopening the now-passing split and compact factors.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_principal_symmetric_pair_probe.py
```

The probe uses exact integer and rational linear algebra only.
