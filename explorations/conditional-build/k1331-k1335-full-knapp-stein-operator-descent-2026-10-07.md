---
title: "K1331--K1335 full Knapp--Stein operator descent"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1331--K1335 full Knapp--Stein operator descent

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the SC-META-53 positivity
question and `INTERNAL_STRUCTURAL_ONLY` for the normalized principal-series
operators, rank-one spectra, reducibility walls, cocycle and chamber descent.

Scope: the spherical minimal principal series of `Spin_0(7,7)` induced from
the trivial finite `M` character at K1311's supplied regular imaginary split
charge. This packet constructs the mathematical normalized simple
intertwiners and closes K1330's operator-valued chamber-descent obligation. It
does not derive the charge, choose a physical chamber or construct an
interacting GU state space.

```gu-typed-objects
result: full simple-root standard operators, complete even rank-one K-type spectrum, common K-finite core, reducibility walls, normalized D7 cocycle, G-equivariant chamber descent and admission replay
carrier: spherical minimal principal series on L2(K/M) with simple-root SL2 compact pictures SO2/{plus_or_minus 1} LAYER=toy CHIRALITY=N/A
pairing: positive compact-picture Haar Hilbert pairing ON=induced_sections
real_structure: regular imaginary split spectral parameter with adjoint z maps to minus z
grading: ungraded D7 Weyl transport plus even simple-root Fourier weights 2n
action_owner: repository-construction -- normalized Knapp--Stein control after an imported regular charge
target: whether K1330's spherical normalization extends to exact full mathematical G descent MAP-TYPE=not-a-map
```

## Preflight bookend

K1326--K1330 determine the spherical coefficient but deliberately stop before
the operator. The same rank-one compact picture already contains the complete
answer: its trivial-`M` modes have even weights, their coefficients obey a
first-order recurrence, and the standard normalized Knapp--Stein theorem then
composes those simple-root operators in higher rank. The first kill condition
is a mode whose normalized coefficient fails the inverse or unit-modulus law;
the second is a higher-rank cocycle that is only projective. Either would keep
K1330's conditional row open.

The source/action challenger remains more important physically, but no released
action, boundary or Green datum supplies an executable charge-selection or
interacting-domain calculation. This operator packet therefore pursues a
complete independent mathematical endpoint. It is the third adjacent packet
on the same arc, justified only because it closes the full operator debt rather
than adding another scalar distance result.

Two primary mathematical references fix the standard conventions:

- Bill Casselman's [*Representations of SL(2,R)*](https://personal.math.ubc.ca/~cass/research/pdf/Irr.pdf),
  sections 11--14, gives the compact-picture Fourier recurrence, meromorphic
  continuation and normalization on the even spherical principal series.
- Knapp and Stein's normalized-intertwiner theorem in
  [*Singular Integrals and the Principal Series IV*](https://www.math.stonybrook.edu/~aknapp/pdf-files/SING4.pdf)
  gives the exact cocycle, adjoint law and unitarity for imaginary parameters.
  Their longer [1980 treatment](https://www.math.stonybrook.edu/~aknapp/pdf-files/int-ops2-1980.pdf)
  supplies the general semisimple-group context.

The formulas below are rederived on the declared rank-one picture. The general
theorem is used only after its spherical normalizer and common carrier match
K1326 and K1312--K1313.

## K1331: the full rank-one operator and every even K-type

For a simple root let `G_alpha` be its split `SL(2,R)` subgroup. The spherical
compact picture is

```text
K_alpha/M_alpha = SO(2)/{plus_or_minus 1},
```

so its algebraic `K_alpha`-finite core is spanned by

```text
e_(2n)(theta)=exp(2 i n theta),  n in Z.
```

For `Re(z)>0`, the full raw standard operator is the convergent integral

```text
(J_z f)(g)=integral_R f(g w_alpha n(x)) dx.
```

At the identity, put `x=tan(theta)`. Including the phase of the standard Weyl
representative, the coefficient of `e_(2n)` is

```text
c_(2n)(z)
 =(-1)^|n| integral_(-pi/2)^(pi/2)
       cos(theta)^(z-1) exp(-2 i n theta) dtheta
 =(-1)^|n| pi Gamma(z)
       / (2^(z-1) Gamma((z+1)/2+|n|) Gamma((z+1)/2-|n|)).
```

At `n=0` this is exactly K1326's

```text
m(z)=sqrt(pi) Gamma(z/2)/Gamma((z+1)/2).
```

Normalize by `R_z=m(z)^(-1)J_z`. Gamma recurrence gives the complete spectrum

```text
a_n(z)=c_(2n)(z)/c_0(z)
      =product_(k=1)^|n| (2k-1-z)/(2k-1+z),
a_0(z)=1,
a_(-n)(z)=a_n(z).
```

Equivalently,

```text
a_(n+1)(z)/a_n(z)=(2n+1-z)/(2n+1+z).
```

The Weyl phase is essential: it makes `a_n(0)=1` on every even mode. Omitting
it would incorrectly leave `(-1)^n` and contradict the normalized identity at
zero. This is the complete rank-one spectrum. It does not claim that every
irreducible `Spin(7)xSpin(7)` K-type is one-dimensional; higher-rank use is by
induction in stages through these simple-root strings.

## K1332: one common dense core and unitary extension

All spherical principal-series compact pictures use the same underlying

```text
H=L2(K/M,dk),
H_Kfin=C[K/M]_K-finite.
```

The algebraic core `H_Kfin` is parameter-independent, dense in `H` and
preserved by every simple standard operator. On each simple-root string it is
the even Fourier core above. The coefficient recurrence has moderate growth,
so the meromorphic family also acts on the smooth compact picture.

For `z=i t`, each factor obeys

```text
|(2k-1-it)/(2k-1+it)|=1.
```

Therefore

```text
|a_n(it)|=1,
R_(it)^*=R_(-it),
R_(-it)R_(it)=I.
```

The K-finite operator consequently extends uniquely to a norm-one unitary map
between the two Hilbert principal-series representations. At `z=0` it is the
identity. At K1311's regular imaginary D7 charge, every one of the 42 root
coordinates is nonzero imaginary, so every simple-root operator and every
reduced product is bounded, unitary and invertible.

This common mathematical domain is not the common closed graph domain demanded
by K1146--K1150. Those rows concern the interacting action, constraints,
boundary traces and causal evolution, none of which acts here.

## K1333: normalized walls, kernels and reducibility

The product formula makes the normalized operator divisor exact. For mode
`n!=0`,

```text
zeros: z=1,3,...,2|n|-1,
poles: z=-1,-3,...,-(2|n|-1).
```

At a positive odd wall `z=2r+1`, precisely the modes with
`|n|>=r+1` are killed; the modes `|n|<=r` survive. At the negative wall
`z=-(2r+1)`, those high modes have the inverse simple poles. These are the
composition-series walls of the spherical even `SL(2,R)` principal series.
The point `z=0` is regular and `R_0=I`.

This normalized operator divisor differs from K1327's divisor of the raw
spherical scalar `m(z)`. Dividing by `m(z)` removes the spherical scalar and
exposes the mode-dependent odd walls. A raw c-function zero or pole is not by
itself an operator-kernel or reducibility theorem.

No imaginary parameter lies on a nonzero odd real wall. A regular imaginary
D7 parameter also has trivial Weyl stabilizer. The normalized family and
Knapp--Stein commuting-algebra theorem therefore leave no root-reducibility or
R-group sector: this supplied spherical minimal principal series is
irreducible. Singular charges and nontrivial `M`-types remain outside the
packet.

## K1334: exact D7 operator cocycle and chamber descent

Let

```text
R_i(lambda): I(lambda) -> I(s_i lambda)
```

be the seven normalized simple operators. Each is a genuine `G` intertwiner on
the common core and, on the regular imaginary locus, a Hilbert-space unitary.
The normalized theorem gives

```text
R_(w1 w2)(lambda)=R_w1(w2 lambda) R_w2(lambda).
```

Hence the parameter-shifted simple products obey exact involution,
nonadjacent commutation and adjacent braid relations. Every reduced expression
for `w` gives the same full operator, not merely the same spherical scalar.
This removes the K1319 projective countercontrol on the actual normalized
family rather than assuming all unitary edge maps are flat.

Use these operators as the chamber identifications `U_C` in K1316. Because
each `U_C` is a coherent `G` intertwiner, K1317's transported actions coincide.
Therefore

```text
[P, direct-sum_C pi_C(g)]=0
```

for every `g`, and the coherent diagonal is a `G` subrepresentation of the
322560-fold chamber sum. Its descended representation is one full copy of the
spherical principal series on `L2(K/M)`, not a one-dimensional representation.
The construction removes redundant chamber multiplicity but selects no single
chamber and derives no charge.

## K1335: mathematical descent closes; physical admission does not

The twenty-row census is now ten satisfied, three excluded, one conditional
and six missing. The full operator Coxeter-flat `G`-intertwiner row moves from
conditional to satisfied. Finite polarized-BFV compatibility remains the one
conditional row. The six physical rows remain missing: source-owned charge and
chamber selection, an action-derived interacting constraint complex, a common
local BV-BFV domain, causal Green or boundary data, positive nonzero physical
cohomology and observed export.

## Postflight hostile review

The strongest overclaim is to call the descended principal series the physical
GU Hilbert space. It is only a mathematical control built after importing the
charge. The strongest mistyping is to read `a_n(z)` as one scalar on every
higher-rank irreducible K-type; it is the complete simple-root spectrum used by
induction in stages, while general K multiplicity spaces remain higher
dimensional. The strongest contrary locus is a nonzero odd real root wall,
where high modes enter the kernel or pole. The supplied regular imaginary
charge meets none of those walls.

The weakest reproducibility seam is the Weyl-representative phase. Independent
quadratures at real `z`, the zero-parameter identity, exact recurrence and
hostile phase mutations jointly fix it. The higher-rank conclusion is then an
application of the normalized cocycle and unitarity theorem, not a finite
matrix extrapolation.

K1145/K1150 remain `0/7`; SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source,
ledger, canon, paper, prediction, confirmation or public status moves.

## Exact next input

The mathematical chamber-descent obligation is closed for the supplied
regular imaginary spherical minimal principal series. The live input is now
physical and source-owned: a released action, boundary or Green law must derive
the charge or replace the chamber construction, then supply the interacting
constraint complex, common local Lorentzian BV-BFV domain, causal evolution,
conserved positive nonzero physical cohomology and observed state map. Singular
charge or nonspherical `M`-type analysis is a separate representation-theory
branch, not an unrecorded condition on this result.
