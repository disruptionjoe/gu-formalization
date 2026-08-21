---
title: "B5 native Rarita--Schwinger BV/Hessian lift: full-carrier symbol exactness with a null boundary"
status: active_research
doc_type: exact_native_action_symbol_lift
created: "2026-08-20"
registry: lab/process/b5-native-rs-bv-hessian-lift.json
probes:
  - tests/channel-swings/b5_native_rs_bv_hessian_lift_probe.py
grade: "ON THE ACTUAL COMPLEXIFIED B5 128/1792/1792/128 CARRIER, THE REPRESENTATION-NATURAL RARITA--SCHWINGER GAUGE SYMBOL FORMS AN EXACT COMPLEX AT EVERY NON-NULL COVECTOR WITH RANKS 128/1664/128. ITS TWO NOETHER COMPOSITIONS VANISH IDENTICALLY, ITS NATIVE KREIN FORMAL SIGN IS ANTI, ITS RR BLOCK HAS W131 Q=1, AND ITS STRICT FOLD HAS ALL EIGHT ELIGIBLE S/I/R BLOCKS. A GAUGE-INERT S SPECTATOR GIVES A FULL-NINE GRADED EULER FAMILY WITH TWO FREE COEFFICIENTS. AT NULL COVECTORS THE MIDDLE SYMBOL HAS AN EXACT NONGAUGE KERNEL WITNESS, AND CURVED CLOSURE REMAINS OPEN."
target_verdict: B5_NATIVE_RS_BV_HESSIAN_LIFT_EXISTS_NONCHARACTERISTICALLY
target_claim: internal target B5-NATIVE-BV-HESSIAN-LIFT; verdict actual-carrier principal-symbol lift constructed with null and curved boundaries explicit
canon_verdict_change: none
---

# B5 native Rarita--Schwinger BV/Hessian lift

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the actual complexified B5
`S -> V* tensor S -> (V* tensor S)^vee_dens -> S^vee_dens` carrier and its
program-native `(9,5)` Clifford/Krein structure at formal compact-core
principal-symbol grade. It proves exactness only at non-null covectors. It
does not construct curved closure, the historical source-preferred Shiab, a
nonlinear/source BV action, null-symbol exactness, global cohomology, a Green
domain, quotient, particle result or GU verdict.

```gu-typed-objects
result: the strict B5 Rarita--Schwinger gauge symbol is an exact native full-carrier BV/Hessian complex off the null cone; a full-nine spectator extension exists
carrier: U0=S rank128, U1=V* tensor S=I+R rank1792, U2=density dual rank1792, U3=S density dual rank128 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native (9,5) invariant spinor Krein form and induced g tensor K vector-spinor form ON=independent-B5-full20-carrier
real_structure: complexified (9,5) Clifford carrier; absolute coflip trivialization and global Lorentzian realization remain UNTYPED
grading: linear abelian BV ghost/field/antifield/Noether grading with Grassmann-odd quadratic Euler polarization
action_owner: repository-construction Rarita--Schwinger quadratic action at flat principal-symbol grade; curved and nonlinear source completion remain unowned
target: native strict master/Noether identity, noncharacteristic exactness, formal-adjoint sign and Euler extension MAP-TYPE=evaluation
```

## Result first

Let `V` be the fourteen-dimensional gimmel cotangent carrier and `S` the
complex 128-spinor. For a covector `xi`, define

```text
A_xi(s)_a       = xi_a s,
(K_xi psi)_a   = gamma_[a b c] xi^b psi^c,
A_xi^vee(phi)  = xi^a phi_a.
```

Total antisymmetry immediately gives

```text
K_xi A_xi = 0,             A_xi^vee K_xi = 0
```

for every `xi`. These are the principal Noether identities and the quadratic
abelian BV master-equation coefficient; they do not follow merely from
Hessian symmetry.

At a normalized non-null covector choose `xi=e^0`. The gauge image is the
zeroth vector-spinor component. On the thirteen transverse components the
middle symbol is

```text
K_perp = gamma_0 (I - G Gamma),
K_perp^-1 = (I - G Gamma/12) gamma_0,
Gamma G = 13 I_S.
```

The exact Clifford inverse proves middle rank `13*128=1664`; the three arrow
ranks are therefore `(128,1664,128)`, and the actual
`128 -> 1792 -> 1792 -> 128` symbol complex is exact off the null cone. This
is an analytic rank proof, not a numerical fit.

## Native polarization and W131 normalization

Use the intrinsic gamma splitting

```text
I=im Gamma-sharp,  P_I=(1/14) Gamma-sharp Gamma,
R=ker Gamma,       P_R=I-P_I.
```

Exact Clifford reduction shows that `P_I A_xi` and `P_R A_xi` are both
nonzero and that all four middle blocks
`P_I K P_I`, `P_I K P_R`, `P_R K P_I`, and `P_R K P_R` are nonzero. The
strict fold therefore has all eight eligible coarse blocks and structural
`SS=0` on the actual carrier.

Under the invariant spinor Krein form and the induced `g tensor K` form on
vector-spinors, `K_xi` is formally anti-adjoint. Its `RR` restriction is
exactly

```text
P_R c(xi) P_R,
```

so it inherits the written W131 principal coefficient with `q=1`; no
favorable rescaling was used. This owns the native strict-branch formal sign
at symbol grade. It does not select the separate `S/I` multiplicity Gram of
the previously serialized full-nine Euler family.

## Full-nine Euler extension

Let `chi in S` be gauge-inert and put `B_xi=Gamma K_xi`. Then
`B_xi A_xi=0`. For free coefficients `a,t`, the graded Euler symbol

```text
H_xi(a,t) = [[a c(xi),       t B_xi],
             [-t B_xi^x,     K_xi ]]
```

is formally Krein anti-adjoint, has all nine coarse `S/I/R` blocks nonzero
for generic nonzero `a,t`, and obeys

```text
H_xi(a,t) (0,A_xi)^T = 0.
```

Thus the canonical free BV master equation leaves both spectator
coefficients free, just as the coarse bridge predicted. The construction is
an actual-carrier lift of the relation pattern, not a normalization theorem.
The current Stage-B `H9` witness remains a different graph-mixing branch and
is neither recovered nor excluded by this lift.

## The null boundary is exact, not rhetorical

For `xi=e^0+e^9` in signature `(9,5)`, `c(xi)^2=0`. With transverse positive
directions `e^1,e^2`, the nonzero vector-spinor

```text
psi_1 = gamma_2 c(xi) u,
psi_2 = gamma_1 c(xi) u,
psi_a = 0 otherwise
```

lies in `ker K_xi` for generic `u` and is not a gauge vector, because a gauge
vector is supported only in the `xi` direction. Hence the native complex is
not exact on the null characteristic cone. No ellipticity, null quotient or
physical-mode claim follows.

## Preflight, route choice and controls

Mechanism-level retrieval covered the B5 20-slot ledger, first-write action,
native polarization, strict support, Euler separation, coarse BV bridge and
all-Gram obstruction. None contained the triple-Clifford full-rank sequence,
its transverse inverse or the null nongauge witness.

The route council compared Clifford/Rarita--Schwinger structure, abstract
homological algebra, BV/BRST ownership, Krein polarization, brute-force
matrix rank, source custody and hostile scope review. The triple-Clifford
route dominated because antisymmetry proves both Noether identities and an
exact transverse inverse proves rank without materializing a fitted
`1792 x 1792` matrix. Computation is the final symbolic certificate.

The exact probe passes `26/26`. It works only with rational coefficients and
finite Clifford-word reduction. It plants a longitudinal middle block that
breaks the master equation, a wrong `RR` normalization, and the exact null
counterexample. These controls distinguish a genuine native lift from a
full-looking matrix or a noncharacteristic overclaim.

## Hostile result review and continuation

The strongest overclaim would be to call noncharacteristic symbol exactness a
curved differential resolution. Covariantizing `A` and `K` produces curvature
commutators; the prior W177 calculation already proves a live obstruction for
the current nine-block ansatz/background combination. The strongest contrary
route is still the filtered graph action for the current Stage-B witness. The
weakest seam is the word "native": it binds the actual carrier, maps and
pairing, not a source-attested nonlinear action or preferred global domain.

`B5-NATIVE-BV-HESSIAN-LIFT` is therefore constructed at actual-carrier
principal-symbol grade. The exact next owner is
`B5-CURVED-RS-BV-COMPLETION`: compute the covariant defect `K_nabla A_nabla`
and its Noether dual on an owned compatible background, then either construct
an action/source-owned curvature completion or prove that branch obstructed.
Do not move to coflip or domain work until that curved operator exists.
