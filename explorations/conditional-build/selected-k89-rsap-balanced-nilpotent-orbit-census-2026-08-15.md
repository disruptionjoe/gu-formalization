---
title: "Selected-K89 RSAP balanced nilpotent-orbit census"
status: active_research
doc_type: exact_real_nilpotent_signed_diagram_census_and_principal_rank_certificate
created: "2026-08-15"
registry: lab/process/selected-k89-rsap-balanced-nilpotent-orbit-census.json
probe: tests/channel-swings/selected_k89_rsap_balanced_nilpotent_orbit_census_probe.py
grade: "COMPLETE NILPOTENT CONE IN Ad(G)p; ALL 99 CONNECTED REAL ORBITS SATURATE POINTWISE RANK; MIXED JORDAN CENSUS OPEN"
canon_verdict_change: none
---

# Selected-K89 RSAP balanced nilpotent-orbit census

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds only the classical balanced symmetric-space moment
image `Ad(Spin_0(7,7))p`. It does not bind a source-selected physical phase
space, boundary condition, BFV reduction, quantization, positivity domain or
particle-physics comparator.

## Result first

The K88 balanced horn survives the complete real nilpotent cone. Every real
nilpotent signed-form type in split `so(7,7)` admits a `Q`-orthogonal
involution `R` with

```text
R^2=1,  RX+XR=0,
signature(Q|R=+1)=(4,3),
signature(Q|R=-1)=(3,4),
```

up to swapping the two eigenspaces. Hence every nilpotent orbit meets the
balanced symmetric complement `p`. The exact finite census contains `43`
orthogonal partitions of `14` and `99` split-real signed-form allocations;
all `99` pass, all are stable signed diagrams, and none splits under
`SO_0(7,7)` or is omitted by a very-even split. Thus these are the `99`
connected real nilpotent adjoint-orbit classes, not merely full-orthogonal
types.

For both principal `[13,1]` orbits, explicit integer matrices have ambient
adjoint rank `84`, centralizer dimension `7`, trivial intersection with
`h=so(3,4)+so(4,3)`, and cotangent moment-map rank `91`. More strongly, exact
row reduction proves that every one of the `99` nilpotent classes saturates
its own `98D` pointwise rank bound, from rank `91` at either principal orbit
to rank `49` at zero. Two exact regular-nonsemisimple controls,
with zero-primary partitions `[5,1]` and `[3,1]`, also have map rank `91` and
trivial `h`-centralizer. They are controls, not an exhaustion of mixed primary
types.

## Exact signed-diagram construction

A real nilpotent orbit of `so(7,7)` has an orthogonal partition of `14`: every
even part occurs with even multiplicity. For each odd block `d=2k+1`, choose
the chain basis `e_0,...,e_(d-1)` with

```text
X e_i = e_(i-1),
Q(e_i,e_(d-1-i)) = c(-1)^i,
D e_i = (-1)^i e_i.
```

Then `X` is `Q`-skew, `D` is `Q`-orthogonal and `DX+XD=0`. The sign `c`
records the real signed-diagram row. Replacing `D` by `-D` swaps that block's
contribution between the two involution eigenspaces.

For an even size `d=2k` with multiplicity `2m`, the standard orthogonal
nilpotent block is

```text
Q = omega_d tensor eta_(2m),
R = D_d tensor A_(2m),
```

where `omega_d` and `eta_(2m)` are symplectic and both `D_d` and `A_(2m)`
are anti-symplectic involutions with Lagrangian `+/-` spaces. Their tensor is
orthogonal, anticommutes with `X`, and contributes signature `(km,km)` to
each `R` eigenspace.

The probe enumerates every admissible partition, every odd-block real-sign
allocation whose total form is `(7,7)`, and every blockwise choice of `D` or
`-D`. In all `99` cases one eigenspace has signature `(4,3)` and the other
has `(3,4)`. There is no very-even ambiguity: a partition with every part
even and every multiplicity even has size divisible by four, while `14` is
two modulo four. Since both balanced eigenspaces are indefinite, orientation
and time-orientation corrections can be made inside their block stabilizers;
the involution criterion therefore remains valid for `Spin_0(7,7)`, not only
the full orthogonal group.

The identity-component count is also checked at the signed-diagram level.
Under the orthogonal `ab`-diagram splitting rule recalled by
[Đoković--Lemire--Sekiguchi](https://doi.org/10.2748/tmj/1178207418), a full
orbit splits only at a diagram whose odd rows have one common middle letter.
All `99` signature-`(7,7)` diagrams contain both middle letters and are stable.
Hence every full orbit is already one connected `SO_0(7,7)` orbit; the central
`Spin_0 -> SO_0` cover adds no adjoint class.

## Principal `[13,1]` certificate

Take a thirteen-chain with alternating anti-diagonal form of signature
`(7,6)` and add one negative singleton. Give the chain the alternating grading
and the singleton negative grading. The two grading spaces have signatures
`(4,3)` and `(3,4)`.

The complete `so(Q)` basis is generated as `Q^{-1}S` for skew matrices `S`.
Exact row reduction gives

```text
rank(ad_X on so(Q)) = 84,
rank(ad_X on h)     = 42,
rank(ad_X on p)     = 42.
```

Thus `dim g_X=7`, `h intersection g_X=0`, `dim ker(ad_X:p->h)=7`, and

```text
rank(dJ) = 49 + 42 = 91.
```

The seven centralizer directions can also be seen constructively: the six odd
powers `X,X^3,...,X^11` plus the one cross-map between the singleton and the
two ends of the thirteen-chain. All seven anticommute with `R`, so none lies
in `h`.

## Pointwise rank on all 99 nilpotent orbits

Let `lambda'` be the transpose orthogonal partition, let `o(lambda)` be its
number of odd rows, and set

```text
c(lambda) = (sum_j (lambda'_j)^2 - o(lambda))/2.
```

This is the real centralizer dimension. For every canonical representative,
the probe builds the complete `91D` `so(Q)` basis, splits it into `42D h` and
`49D p`, and row-reduces both adjoint maps. It obtains

```text
rank(ad_X:h->p) = rank(ad_X:p->h) = (91-c(lambda))/2,
dim h_X = (c(lambda)-7)/2,
dim p_X = (c(lambda)+7)/2,
rank(dJ) = 49 + rank(ad_X:p->h) = (189-c(lambda))/2,
target Poisson rank = 91-c(lambda).
```

Consequently `2 rank(dJ)=98+target Poisson rank` on all `99` connected real
nilpotent orbits. Integer row reduction modulo a prime supplies lower bounds
whose fixed-plus-moving sum reaches the exact characteristic-zero adjoint rank
`91-c(lambda)`; the partition centralizer formula supplies the matching upper
bound, so the displayed ranks are exact over the rationals. Nilpotent
singularity introduces precisely the rank loss required by the target Poisson
structure and no additional defect.

## Regular-nonsemisimple controls

Two independently typed direct sums test that nilpotent admission composes
with nonzero primary blocks:

1. A principal `[5,1]` zero primary on a split six-plane, plus two positive
   and two negative elliptic two-planes with weights `1,2,4,8`.
2. A principal `[3,1]` zero primary on a split four-plane, plus two positive
   elliptic, two negative elliptic and one hyperbolic two-plane with weights
   `1,2,4,8,16`.

Both have ambient adjoint rank `84`, `h`-adjoint rank `42`, `p`-adjoint rank
`42`, trivial `h`-centralizer and moment-map rank `91`. Distinct weights and
disjoint primary spectra prevent accidental centralizer enlargement. These
rows prove that mixed regular points exist in the image; they do not classify
all regular nonsemisimple primary decompositions.

## Claim ceiling and next gate

- The complete nilpotent cone meets `Ad(G)p`.
- All `99` connected real nilpotent orbit classes saturate the `98D`
  pointwise rank bound.
- Both principal regular nilpotent orbits are submersive for the `98D` horn;
  zero has map rank `49`.
- Two regular-nonsemisimple controls are submersive.
- Complete regular-nonsemisimple and singular mixed-Jordan coverage remains
  open. Nilpotent coverage does not imply it.
- Zero-neighborhood coverage, surjectivity and global RSAP existence remain
  open until that mixed-primary census closes.
- The ambient `A3` successor remains `TYPE_MISSING`; `[98,182]` is unchanged.
- No source selection, canon, ledger, residue, quotient, datum or public-
  posture change follows.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k89_rsap_balanced_nilpotent_orbit_census_probe.py
```

The certificate uses exact integer and rational arithmetic only.
