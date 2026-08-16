---
title: "Selected-K125 native I1B fixed-chart Cartan recombination"
status: active_research
doc_type: exact_fixed_chart_connection_curvature_coefficient_and_cartan_covariance_gate
created: "2026-08-15"
registry: lab/process/selected-k125-native-i1b-fixed-chart-cartan-recombination.json
probe: tests/channel-swings/selected_k125_native_i1b_fixed_chart_cartan_recombination_probe.py
grade: "K125 CLOSES THE EXPLICIT FIXED-CHART COVARIANCE SEAM BEHIND K124. THE SYMMETRIC-FRAME SPIN-LEVI-CIVITA CONNECTION HAS A LIVE NONZERO MIXED SECOND METRIC JET; RESTORING dB TO B-WEDGE-B MAKES CURVATURE TRANSFORM EXACTLY; AND TRANSPORTING THE PAIRING AND NONCYCLIC SHIAB-LIKE COEFFICIENT TOGETHER REPRODUCES THE CO-MOVING SCALAR WITHOUT A CYCLIC-TRACE ASSUMPTION. K126 VINDICATES THIS COVARIANCE AND COMPLETES THE COMMON-TRANSVERSE THREE-MOMENTUM POLYNOMIAL. K127 THEN REDUCES THE ALIGNED CURVED ONE-RADIAL TT RESPONSE TO 24 K_PERP I2 AND EXHIBITS GENERIC OFF-TT WEYL LEAKAGE; IT DOES NOT IDENTIFY THAT RESPONSE WITH THE PURE TT HESSIAN AT T=0. THE PRINCIPAL GREEN CURRENT IS FRAME-COVARIANT AND CARTAN IMPROVEMENTS CHANGE THE PRESYMPLECTIC REPRESENTATIVE BY A SPACETIME-EXACT TERM. K128 MUST CLOSE SOURCE-GLOBAL BACKGROUND LEGALITY, A QUADRATIC FLUCTUATION OWNER AND THE FULL METRIC CONSTRAINT SYSTEM BEFORE A UNIQUE PENCIL OR SPECTRUM IS CLAIMED."
target_claim: K124_NEXT_GATE__FIXED_CHART_D2LC_EXTERIOR_DERIVATIVE_NONCYCLIC_CARTAN_RECOMBINATION
target_verdict: FIXED_CHART_COVARIANCE_EXACT__CARTAN_CLASS_EXACT__K126_COMMON_TRANSVERSE_SYMBOL__K127_ALIGNED_ONE_SCALAR_COMPRESSION_AND_GENERIC_WEYL_LEAKAGE__GLOBAL_CLOSURE_OPEN_K128
canon_verdict_change: none
---

# Selected-K125 native I1B fixed-chart Cartan recombination

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, spin-Levi-Civita, noncyclic coefficient and
> Cartan/Green question. Ordinary Higgs/VEV, family-index, net-chirality,
> anomaly, symmetry-breaking and familiar four-dimensional gauge-model
> constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K124 computed the principal native TT coefficients in a co-moving K77 frame.
K125 checks the concern that this normalization might have hidden a coordinate
owner. It does not: the explicit fixed-chart connection has the expected
nonzero second metric jet, and the exterior derivative restores the exact
connection-curvature naturality square. The action coefficient packet must be
transported as one object—pairing, Shiab-like map and field coefficients. When
that is done, the fixed-chart scalar equals the co-moving scalar without using
cyclicity of a trace. Freezing the noncyclic map gives a planted nonzero mixed
mismatch.

At K125's generic covariance grade, K124's principal values appeared to remain
exact:

```text
C_t_h_h^prin=-12 q^2 <H1,H2>_DW,
C_t_h_v^prin=0,
D3_ttt=8736,
C_t_v_v=-(56/3)<V,*V>.
```

The Green current transforms covariantly when the induced frame connection is
included. A Cartan improvement can have a nonzero field-space curl, but its
effect on the presymplectic current is a spacetime-exact derivative. That
fixes the representative class; it does not select a boundary condition or a
BFV charge.

K125 also isolates the next honest deficit. On the two-polarization TT block,
the invariant principal operator may be written

```text
P(q)=-12 q^2 I_2+E_curved,
E_curved=[[a,c],[c,b]].
```

The three entries `(a,b,c)` are formal background-curvature/connection-jet data.
They do not change the principal symbol or its Green current, but they do
change the characteristic polynomial and spectrum. K124 and covariance do
not determine them at K125. K127 later replaces this generic placeholder with
an aligned one-scalar compression plus an off-TT leakage obstruction. K128
must close the full metric system before any unique pencil or spectral owner
is claimed.

## Layer-0 packet

| object | exact meaning here | not identified with |
| --- | --- | --- |
| fixed chart | local coordinate/frame coefficients with moving tetrad | fixed `varpi` action coordinate |
| `D2B_LC` | mixed second metric jet of the symmetric-frame spin connection | a fitted cubic coefficient |
| curvature | `dB+B wedge B` | the algebraic `B wedge B` summand alone |
| coefficient packet | pairing plus noncyclic Shiab and dual field transport | a cyclic trace shortcut |
| Cartan representative | one local variational potential/Green current | a reduced BFV charge |
| `E_curved` | same-action lower-order TT endomorphism | the principal `-12q^2` coefficient |

The native metric graph remains `delta B=DB_LC[H]`, `delta T_h=0`.
Fixed-chart frame motion does not reintroduce the old fixed-`varpi` `14/3`
partial representative.

## Exact fixed-chart recombination

For TT waves `(h,p)` and `(l,q)`, the symmetric-frame square root contains the
mixed term
`-(1/8)[(eta h)(eta l)+(eta l)(eta h)]tu`. Evaluating
`omega_mu=(e Gamma_mu-partial_mu e)e^-1` gives an eta-skew connection whose
mixed coefficient is nonzero and symmetric under exchange of the two TT
inputs. This reproduces the K120 `D2B_LC` owner in the fixed chart.

For a moving frame `F`, the fixed-chart connection is
`B^F=F^-1 B F+F^-1 dF`. The exact two-coordinate noncommuting witness gives

```text
dB^F+B^F wedge B^F = F^-1(dB+B wedge B)F
```

including the mixed second frame coefficient. The planted algebraic-only
replacement fails. The exterior derivative is the term that makes the
fixed-chart connection packet equivalent to the co-moving curvature packet.

## Noncyclic coefficient transport

If `v_f=M v_c`, then the pairing and noncyclic map transport as
`P_f=M^-T P M^-1` and `S_f=M S M^-1`. Direct contraction gives
`v_f^T P_f S_f w_f=v_c^T P S w_c`. This proof never rotates factors through a
trace. Freezing `S` gives a nonzero mixed mismatch.

## Green and Cartan class

For a moving K-orthogonal frame `M(x)`, the induced connection
`A=-M' M^-1` makes

```text
j_A=-12[<H1,nabla_A H2>_DW-<nabla_A H1,H2>_DW]
```

equal to K124's co-moving current. A local Cartan improvement may have
nonzero field-space curl; its presymplectic change is the spacetime derivative
of that curl. Boundary conditions, corner terms and topology still decide
whether the exact local shift survives as edge data. No BFV charge follows.

## What closed and what did not

| packet | K125 result |
| --- | --- |
| explicit fixed-chart `D2B_LC` owner | exact, nonzero, symmetric |
| `dB+B wedge B` frame covariance | exact through mixed order |
| noncyclic coefficient transport | exact without trace cyclicity |
| K124 principal coefficients | K126: exact specialization of the common-transverse three-momentum polynomial |
| principal Green current | frame-covariant |
| Cartan representative ambiguity | spacetime-exact class identified |
| curved one-radial TT response | K127: aligned `24 K_perp I_2`; generic Weyl leaks off TT; not the pure TT Hessian at `T=0` |
| unique full pencil, spectrum, global domain, BFV charge | not selected |

## Reverse scaffold

```text
R4 K124: homogeneous-radial/back-to-back principal TT evaluator
R5 K124: -12 q^2 DeWitt, mixed zero, principal Green current
R6 K125: fixed-chart D2LC + exterior derivative + noncyclic transport exact
R7 K125: Cartan representative class exact; BFV boundary value still open
R8 K126: isolated `d(D2B_LC)=-24` cancelled by natural transport `+24`; complete three-momentum polynomial exact
R9 K127: local Ricci-flat stationary family and aligned one-scalar compression
R10 K127: generic Weyl leakage blocks automatic two-field closure
R11 K128: source-global legality and full metric constraint/gauge closure
R12 later: common global domain, BFV reduction and 2D-to-98D attachment
```

## K126 successor correction

K125 proves a covariance identity, not the value of every principal action
cell. K126 evaluates both the isolated K77 contraction and an independent
fixed-coordinate completion. K124's metric waves were back-to-back and its
radial leg was homogeneous, so total metric momentum killed `d(D2B_LC)`.
With nonzero radial momentum that exterior term is live: the selected witness
has `d(D2B_LC)=-24`, `B^2=0`, and partial Cartan covector
`(-12,0,0,-12)`. But the omitted coframe/pairing/tautological transport is
`+24`, so the complete witness is zero. K125's covariance theorem is thereby
vindicated, and K126 completes the common-transverse result as
`-6(p^2+q^2+3r^2)<DW>`.

## K127 successor refinement

K127 replaces the generic three-entry lower-order placeholder with a sharper
stationary-family result. On aligned `T=0` Ricci-flat Weyl germs the one-radial
TT response compression is `24 K_perp I_2`, but `K_perp` is not selected. Generic
Ricci-flat Weyl curvature sends the selected polarizations outside the TT
plane, so even that compression is not automatically a closed response block.
It is not the pure TT Hessian at `T=0`.
The K125 covariance and Cartan-class theorems survive; K128 now owns
source-global legality and constraint/domain closure.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k125_native_i1b_fixed_chart_cartan_recombination_probe.py
```
