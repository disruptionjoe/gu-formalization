---
title: "K79 I1B weighted symmetric-domain equivalence wave"
status: active_research
doc_type: reverse_scaffold_i1b_weighted_symmetric_domain_equivalence_result
date: 2026-09-01
claim_ceiling: exact formal-symmetry, half-density conjugation, endpoint-class and Green-trace equivalence for one repository-owned weighted singular two-component control; no actual source cross-null operator, physical measure, rank-jump matching law or coefficient selector
manifest: lab/process/k79-i1b-weighted-symmetric-domain-equivalence-wave.json
probe: tests/channel-swings/k79_i1b_weighted_symmetric_domain_equivalence_probe.py
---

# K79 I1B weighted symmetric-domain equivalence wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: exact symmetric weight correction and unitary domain equivalence for the singular-residue two-component control in every power-law measure u^p du
carrier: complex two-component sections on 0<u<1 with real p,kappa,a LAYER=conditional CHIRALITY=N/A
pairing: positive repository-owned L2(u^p du) pairing, transported by the half-density unitary U_p f=u^(p/2)f
real_structure: componentwise conjugation preserved by real matrices J, S, H and real p,kappa,a
grading: two indicial modes u^(-p/2-rho)e_plus and u^(-p/2+rho)e_minus; no gauge, BRST, BV or physical grading
action_owner: repository owns the weighted symmetric countercontrol only; no filed source action owns its operator, measure, domain or boundary relation
target: whether the prior raw u du mode split survives after the differential expression is corrected for formal symmetry MAP-TYPE=classification
```

## Result first

The prior raw `u du` mode count distinguished `log(2)` from `log(3)`, but it
changed the measure without changing the differential expression. Once the
unique scalar half-density correction required for formal symmetry is added,
the weight cancels from the endpoint exponents. Every power-law weighted
control is unitarily equivalent to the unweighted one. Both candidate values
remain limit-point, and the raw weighted split disappears.

Freeze

```text
J=[[0,-1],[1,0]],  S=[[0,1],[1,0]],  H=[[1,0],[0,-1]],
D_(p,kappa,a)=J(d/du+p/(2u))+(kappa S+aH)/u.                  (1)
```

The Hilbert pairing is

```text
<f,g>_p=integral_0^1 f(u)^* g(u) u^p du.                     (2)
```

Integration by parts gives

```text
(J d/du)^*=J d/du+(p/u)J.                                   (3)
```

Because `J^*=-J`, the added multiplication term
`(p/(2u))J` contributes the opposite half of the defect. Thus (1) is formally
symmetric and its Green boundary form is

```text
[u^p f(u)^* J g(u)]_0^1.                                    (4)
```

Within scalar multiples of `J/u`, the coefficient `p/2` is forced by formal
symmetry.

## Exact half-density conjugation

Define

```text
U_p:L2(u^p du)->L2(du),       (U_p f)(u)=u^(p/2)f(u).          (5)
```

This is unitary. Direct differentiation shows

```text
U_p D_(p,kappa,a) U_p^(-1)=D_(0,kappa,a).                    (6)
```

Thus the minimal and maximal domains, deficiency indices, endpoint class,
Green traces and every self-adjoint extension of the frozen control transport
bijectively under `U_p`. This is an exact operator equivalence for the
repository-owned family, not a derivation of a physical measure.

Multiplying the zero-mode equation by `-uJ` gives

```text
u f'+C_p f=0,
C_p=(p/2)I+kappa H-aS.                                       (7)
```

Set `rho=sqrt(kappa^2+a^2)`. The two eigenvalues of `C_p` are
`p/2+rho` and `p/2-rho`, so the modes are

```text
f_+=u^(-p/2-rho)e_+,       f_-=u^(-p/2+rho)e_-.              (8)
```

Their squared weighted densities are exactly

```text
u^p |f_+|^2=u^(-2rho),      u^p |f_-|^2=u^(2rho).             (9)
```

Therefore the singular endpoint is limit-circle exactly when

```text
rho<1/2,                                                       (10)
```

independently of `p`. At `kappa=1/4`, both `a=log(2)` and `a=log(3)` have
`rho>1/2`, so both are limit-point for every power-law weight in the symmetric
family.

## What happened to the raw weighted split

For the uncorrected expression

```text
D_raw=J d/du+(kappa S+aH)/u                                  (11)
```

placed in `L2(u^p du)`, equation (3) leaves the formal-adjoint defect
`(p/u)J`. When `p=1`, the unchanged raw modes produce the earlier two-versus-
one count for `log(2)` and `log(3)`. But (11) is not symmetric in that
pairing. The count was a valid integrability fact about a mismatched
expression and measure, not a self-adjoint-domain discriminator.

Equation (4) also transports without residue:

```text
u^p f^*Jg=(U_p f)^*J(U_p g).                                 (12)
```

Hence a limit-circle boundary line or extension parameter is the same datum
in half-density coordinates. In the present two candidate cases the endpoint
is limit-point, so no boundary condition at `u=0` is available to select
between them inside this control.

## Hostile review and claim ceiling

The strongest overclaim would say that no physical measure can distinguish
the coefficient. What is proved is only that changing among the frozen
power-law measures while adding the exact scalar correction required for
formal symmetry produces a unitarily equivalent operator family. A source
operator may contain a different residue, matrix-valued density, connection,
rank-jump matching relation or spectral observable.

The strongest contrary control is the deliberately uncorrected expression
(11): it retains the raw split but fails formal symmetry for `p != 0`. The
weakest reproducibility seam is full source-domain ownership; the exact packet
transports the minimal/maximal domains of the frozen control but does not
identify them with the actual I1B cross-null domain.

The operator, measure family, half-density map and boundary traces are
repository-owned controls. They are not the actual source cross-null normal
operator, rank-changing presymplectic quotient, physical positive pairing or
rank-jump matching law. No coefficient selection, prediction, confirmation,
held-out score or GU verdict follows.

## Next condition

Derive the actual source/action-owned cross-null normal operator, density,
pairing and rank-jump matching or spectral law. Determine whether its
half-density normal form contains an `a`-dependent invariant not removable by
unitary conjugation and whether an independently owned physical boundary or
spectrum distinguishes the candidate values.

Reproduce with:

```bash
python3 tests/channel-swings/k79_i1b_weighted_symmetric_domain_equivalence_probe.py
python3 tests/channel-swings/k79_i1b_weighted_symmetric_domain_equivalence_probe.py --selftest
```
