---
title: "Selected-K77 RSAP A2 Kostant bridge and first split-A3 factor"
status: active_research
doc_type: exact_regular_bridge_and_higher_root_factor_construction
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-kostant-a3-factor.json
probe: tests/channel-swings/selected_k77_rsap_a2_kostant_a3_factor_probe.py
grade: "FULL REAL REGULAR A2 ATLAS CONSTRUCTED LOCALLY; SPLIT A3 PRINCIPAL FACTOR CONSTRUCTED; A2/A3 GLUING OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP `A2` Kostant bridge and first split-`A3` factor

## Result first

The missing regular-nilpotent `A2` transition constructs. A principal real
`sl2` triple gives a two-dimensional Kostant/Slodowy slice transverse to the
six-dimensional regular orbit. In `sl(3,R)` its directions are `f,f^2`; in
`su(2,1)` they are `f,i f^2`. The second mixed direction is essential: `f^2`
is Hermitian for the defining form, while `i f^2` is skew-Hermitian and stays
inside the mixed real Lie algebra.

The principal factors were already submersive at these values. The new slice
now types their transition to all four semisimple Cartan atlases. On every
overlap it is an ordinary local diffeomorphism; its cotangent lift preserves
the tautological primitive strictly and intertwines the moment map. Thus the
split and mixed principal-`A2` atlas now covers the complete real regular
locus locally at `98D` and map rank `91`. This does not cross a singular
centralizer jump.

Because the bridge passes, the first higher-root packet also runs. The split
principal factor

```text
T*(SL(4,R)/SO(2,2))
```

has dimension `18`, covers every regular real Jordan type by a signature
`(2,2)` self-adjoint representative, has moment-map rank `15` on the regular
locus and rank `9` at zero. With `T*R4` it gives the universal `26D`
`sl4* x R4_zero` refinement; adjoining the `72D` common leaf retains the
`98D` carrier and full regular map rank `72+15+4=91`. The `A3` origin schedule
is map rank `72+9+4=85`.

This constructs a factor, not its transition to the existing `A2` charts.
The next gate is the split `A2/A3` common-refinement transition and its first
noncommuting overlap. Other `A3` real forms remain untested.

## Exact real principal slices

For the split and mixed `A2` cases use

```text
e = [0 1 0]   f = [0 0 0]   h = [2 0  0]
    [0 0 1]       [2 0 0]       [0 0  0].
    [0 0 0]       [0 2 0]       [0 0 -2]
```

They obey `[h,e]=2e`, `[h,f]=-2f`, `[e,f]=h`. In the mixed case the Hermitian
form

```text
H = [0  0 1]
    [0 -1 0]
    [1  0 0]
```

has signature `(1,2)` (equivalently `(2,1)` after sign reversal), and both
`e` and `f` satisfy `x^T H + Hx=0`. The exact direct sums are

```text
sl(3,R) = [sl(3,R),e] direct-sum span_R{f,f^2},
su(2,1) = [su(2,1),e] direct-sum span_R{f,i f^2}.
```

Each orbit image has rank six and each displayed sum rank eight. The
centralizer kernel of `ad(e)` has real dimension two throughout the regular
slice, including at `e`. Hence the regular centralizer family is smooth there;
the nilpotent fibre is unipotent rather than toral, but it does not jump in
dimension.

The other discriminant points are not silently skipped. In the split slice,
`e+(3/4)f-(1/2)f^2` has characteristic polynomial
`(t-1)^2(t+2)` and a single size-two block at `1`; its centralizer still has
dimension two. In the mixed slice the corresponding real parameters
`e-(3/4)f+(i/2)f^2` give the repeated imaginary-root control and again orbit
rank six. Thus the bridge covers both the principal nilpotent and the regular
nonnilpotent discriminant type.

The action map from orbit coordinates times the slice is therefore a local
diffeomorphism. Away from the discriminant it overlaps the appropriate split,
complex-pair or compact Cartan chart. If its Jacobian is `J`, the induced
cotangent change is

```text
q' = phi(q),       p' = J(q)^(-T) p,
```

so `p'^T dq' = p^T dq`. This is the required primitive identity; exterior
differentiation gives the symplectic identity, and equivariance gives moment
intertwining. No logarithm, eigenline, new field or limiting torus coordinate
is used at the nilpotent.

## Split `A3` factor

Every regular real `4 x 4` Jordan type admits a nonsingular symmetric
symmetrizer of signature `(2,2)`: a real Jordan block uses its reverse form,
a conjugate-pair block is neutral, and signs on the one-dimensional real
blocks complete the total signature. Thus every regular covector is conjugate
to `ann(so(2,2))`. Its centralizer consists of polynomials in the regular
self-adjoint representative, so it is self-adjoint and has zero intersection
with the skew-adjoint isotropy. The cotangent moment differential therefore
has full rank `15`; at zero its rank is `dim SL4/SO(2,2)=9`.

The principal nilpotent control uses the size-four Jordan block and the
reverse-identity symmetrizer, which has signature `(2,2)`. It verifies that
the factor does not hide the `A2` candidate's old nilpotent rank defect.

## Claim ceiling

- The split and mixed principal-`A2` atlases cover their complete real regular
  loci locally at `98D`, map rank `91`.
- Singular values where the centralizer dimension jumps remain open.
- The split principal-`A3` factor constructs with the stated regular and
  origin schedules.
- No `A2/A3` transition, other `A3` real form, deeper stratum, zero-charge
  atlas or all-strata RSAP is claimed.
- No canon, ledger, residue, quotient datum, physical claim or public posture
  changes.

## Next exact gate

Construct the split `A2/A3` `26D` common-refinement symplectomorphism. Check
the full moment map and primitive on the connected regular overlap, then the
first noncommuting `A2/A3/A2` triple. Only that result can license expansion
to the compact and mixed `A3` real forms.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_kostant_a3_factor_probe.py
```

The probe uses exact integer and rational linear algebra only.
