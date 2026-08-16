---
title: "Selected-K132 native I1B T=0 all-grade Noether/compatibility complex"
status: active_research
doc_type: exact_all_grade_dn_symbol_covariant_square_noether_kt_bfv_obstruction
created: "2026-08-16"
registry: lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json
probe: tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py
grade: "K132 TOTALIZES THE SELECTED-SHIAB T=0 FIRST-ORDER DISTORTION COEFFICIENT ON THE COMPLETE 229376-DIMENSIONAL REAL OMEGA1(CL(7,7)) CARRIER. ITS TIMELIKE, SPACELIKE AND NULL PRINCIPAL/GREEN RANKS ARE 130912,130912,122746, WITH RADICALS 98464,98464,106630. THE COMPLETE 229386-DIMENSIONAL COUPLED DOUGLIS-NIRENBERG SYMBOL HAS RANKS 130912,130912,122748 AND RADICALS 98474,98474,106638: THE METRIC CURVATURE BLOCK ADDS NO NONNULL RANK AND TWO NULL RANKS. THE GRADE GRAPH IS TWO EXACT CHAINS EXHAUSTING GRADES ZERO THROUGH FOURTEEN. AN ACTUAL 56-DIMENSIONAL BLOCK SHOWS THAT ONLY 11 OF 24 NORMAL-NULL ROWS ARE ALSO TANGENTIAL-NULL. NONZERO KAPPA1 K BREAKS EVERY WOULD-BE IDENTITY BASED ONLY ON PRINCIPAL NULLITY; AT KAPPA1=0 GENERIC RICCI-FLAT WEYL CURVATURE GIVES D_B SQUARED EQUALS AD(F_B) NONZERO, SO THE DISTORTION DIFFERENTIAL DOES NOT FORM A COMPLEX. ONLY THE FOUR METRIC DIFFEOMORPHISM NOETHER COLUMNS ARE ACTION-OWNED AT THIS GERM. NO DISTORTION KT TOWER, REGULAR GLOBAL BFV REDUCTION, CLOSED DOMAIN OR PHYSICAL COHOMOLOGY FOLLOWS. K133 MUST CLASSIFY THE FLAT/CENTRAL-CURVATURE KAPPA-ZERO EXCEPTIONAL COMPLEX AND THE FULL KAPPA PENCIL BEFORE ANY DOMAIN OR COHOMOLOGY CLAIM."
target_claim: K131_NEXT_GATE__ALL_GRADE_PRINCIPAL_TANGENTIAL_SUBPRINCIPAL_NOETHER_COMPATIBILITY_COMPLEX
target_verdict: ALL_GRADE_DISTORTION_AND_COUPLED_DN_CAUSAL_RANKS_EXACT__TANGENTIAL_NULL_ROWS_NOT_PRESERVED__NONZERO_KAPPA_BREAKS_PRINCIPAL_IDENTITIES__GENERIC_WEYL_COVARIANT_SQUARE_OBSTRUCTS_DISTORTION_COMPLEX__ONLY_METRIC_DIFF_NOETHER_OWNED__GLOBAL_KT_BFV_UNSELECTED
canon_verdict_change: none
---

# Selected-K132 native I1B T=0 all-grade Noether/compatibility complex

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, full-adjoint Clifford-grade, mixed-order symbol,
> covariant-compatibility and variational Noether calculation. Ordinary
> Einstein-action, fermionic K77, particle-spectrum, Higgs/VEV, family-index,
> chirality, anomaly and symmetry-breaking constructions do not adjudicate it
> without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds the selected displayed `comm/symi/symi` Shiab in the
source-native `I1B` Hessian at K127's local Ricci-flat `T=0` fixed-boundary
germ. It totalizes the finite all-grade principal/Green coefficient and the
formal coupled Douglis--Nirenberg symbol. It does not prove uniqueness among
every source-natural Shiab, select `kappa_1`, construct a global closed
operator, or identify a physical BFV quotient or cohomology.

## Result in plain English

K130 and K131 used the serialized `196+24` distortion carrier. The source
variable is larger:

```text
V_T = Omega1(Cl(7,7)),        dim V_T = 14*2^14 = 229376.       (1)
```

K132 totalizes the selected first-order coefficient without constructing a
dense `229376`-square matrix. A basis vector
`e^mu tensor gamma_J` has invariant label `J xor {mu}`. For a nonnull
one-axis conormal, the Euler coefficient connects labels in 28-dimensional
blocks; a null two-axis conormal connects them in 56-dimensional blocks.
Signed-permutation orbits reduce the exhaustive calculation to 56 timelike,
56 spacelike and 49 null block types with exact combinatorial
multiplicities.

The distortion coefficient has:

| conormal | raw-density rank | Euler/Green rank | radical |
| --- | ---: | ---: | ---: |
| timelike | 122864 | 130912 | 98464 |
| spacelike | 122864 | 130912 | 98464 |
| null | 122864 | 122746 | 106630 |

The raw rank is not the equation rank: formal integration by parts uses the
antisymmetrized coefficient. The null radical is `8166` dimensions larger
than the nonnull radical.

The exhaustive unordered Clifford-grade graph is

```text
0--3--4--7--8--11--12
1--2--5--6--9--10--13--14.                                 (2)
```

Thus K130's adjacent `Cl1`--horizontal-`Cl2` block was one exact edge of a
much larger source graph, not a representative full-carrier ratio.

## 1. Complete coupled DN symbol

The quadratic source Hessian remains

```text
H_DN(n) = [[0,A(n)^*],[A(n),C_1(n)]],                    (3)
```

where `A` is the second-order metric-curvature row and `C_1` is the
first-order all-grade coefficient above. Directly inserting the complete
selected-Shiab curvature columns gives:

| conormal | `rank A` | `rank H_DN` | coupled radical |
| --- | ---: | ---: | ---: |
| timelike | 6 | 130912 | 98474 |
| spacelike | 6 | 130912 | 98474 |
| null | 4 | 122748 | 106638 |

On nonnull strata the metric-curvature image is already absorbed by the
distortion image, so adding ten metric columns changes no rank. On the null
stratum it adds exactly two ranks. The coupled cross-null radical jump is
therefore `8164`, not K131's tracked-carrier jump of two and not the
distortion-only all-grade jump of `8166`.

This is a formal DN symbol statement with the K131 relative weights. It does
not choose an operative domain or make the symbol elliptic or hyperbolic.

## 2. Tangential and subprincipal compatibility

The actual all-grade operator confirms K131's abstract warning. On the
smallest label block closed under a timelike normal `n=e0` and spacelike
tangent `tau=e1`, both `C_1(n)` and `C_1(tau)` have rank `32` on 56
dimensions. The normal kernel has dimension `24`, but its intersection with
the tangential kernel has dimension only `11`. An exact basis left-null row
of the normal coefficient has nonzero contraction with the tangential
coefficient. Normal-null rows are therefore not automatically propagated
constraints.

The lower-order fork is sharper:

```text
C = C_1(D_B) + kappa_1 K.                               (4)
```

- If `kappa_1 != 0`, nondegeneracy of `K` means no nonzero principal
  left-null row remains a differential identity merely because it annihilates
  `C_1(n)`. It receives a live algebraic equation.
- If `kappa_1 = 0`, covariant differentiation still obeys
  `D_B^2=ad(F_B)`. K127 permits generic nonflat Ricci-flat Weyl germs. An
  exact Ricci-free Clifford fixture has nonzero `ad(F_B)` on a grade-one
  coefficient, so the distortion differential does not form a complex on
  that stratum.

Only a flat or curvature-central exceptional stratum removes this particular
square obstruction. Even there, vanishing of the square would not by itself
turn the distortion radical into gauge or select boundary conditions.

## 3. Noether, KT and BFV disposition

At the stationary `T=0` germ, the reduced `(g,T)` action owns the four metric
diffeomorphism Noether columns. The connection difference transforms
tensorially, so it has no independent `d chi` distortion column there. The
action-owned gauge image therefore has dimension four, while the coupled
principal radicals have dimensions `98474/98474/106638`.

The minimal honest sequence is consequently:

```text
vector fields --G_diff--> metric plus distortion fields --H_DN--> Euler rows
```

with `G_diff` landing only in the metric component at `T=0`. The distortion
principal radicals are characteristic and algebraic-constraint data, not a
Koszul--Tate generator list. For nonzero `kappa_1` the lower-order flat map
breaks principal-null identities; for zero `kappa_1` generic Weyl curvature
breaks the candidate covariant complex. Neither stratum supplies a
distortion reducibility tower or nilpotent BV completion.

The null rank jump also continues to obstruct one regular constant-rank BFV
reduction across causal strata. No closed DN realization, boundary
polarization, operative adjoint, inverse or physical cohomology is selected.

## 4. Next gate

K133 must separate the exceptional horns rather than quotient the generic
radical:

1. on `kappa_1=0` with flat or curvature-central background, test the actual
   selected-Shiab compatibility maps, symbol cohomology and characteristic
   integrability; and
2. for `kappa_1!=0`, build the all-grade invariant-block parameter pencil and
   determine whether any uniform characteristic/domain statement survives
   the covector-dependent exceptional loci.

Only after that split can a closed realization, KT/BFV edge packet, reduced
inverse or cohomology be considered. No ledger, canon, public posture,
particle, phenomenology or GU truth-status claim changes. Joe input is not
required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py
```
