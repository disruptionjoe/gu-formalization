---
title: "Selected-K126 native I1B three-momentum principal completion and transport cancellation"
status: active_research
doc_type: exact_fixed_chart_principal_recombination_scope_correction_and_cartan_gate
created: "2026-08-15"
registry: lab/process/selected-k126-native-i1b-radial-momentum-principal-scope-correction.json
probe: tests/channel-swings/selected_k126_native_i1b_radial_momentum_principal_scope_correction_probe.py
grade: "K126 COMPLETES THE COMMON-TRANSVERSE THREE-MOMENTUM PRINCIPAL TT POLYNOMIAL AND FIRES A PLANTED PARTIAL-FRAME FAILURE. K124'S -12 Q2 DEWITT RESULT IS THE HOMOGENEOUS-RADIAL BACK-TO-BACK SPECIALIZATION. AT NONZERO NULL RADIAL MOMENTUM THE ISOLATED K77 D(D2B_LC) CELL IS -24 WITH PARTIAL CARTAN COVECTOR (-12,0,0,-12), BUT AN INDEPENDENT FIXED-COORDINATE CURVATURE EXPANSION SHOWS THE OMITTED COFRAME/PAIRING/TAUTOLOGICAL TRANSPORT IS +24, SO THE COMPLETE WITNESS IS ZERO. ON THE COMMON-TRANSVERSE PLUS/CROSS FAMILY THE FULL RESULT IS C_THH=-6(P2+Q2+3R2)<H1,H2>_DW, R=-(P+Q); CROSS POLARIZATIONS VANISH. C_THV REMAINS ZERO ON THE SELECTED 120-ENTRY TT PACKET. CURVED LOWER ORDER, GLOBAL DOMAIN AND BFV REMAIN OPEN K127."
target_claim: K125_PRINCIPAL_RETENTION__AUDIT_ACTUAL_K77_D_D2BLC_AT_NONZERO_RADIAL_MOMENTUM
target_verdict: COMMON_TRANSVERSE_THREE_MOMENTUM_PRINCIPAL_POLYNOMIAL_EXACT__PARTIAL_D_D2LC_MINUS24_CANCELLED_BY_TRANSPORT_PLUS24__K125_COVARIANCE_VINDICATED__CURVED_LOWER_ORDER_OPEN_K127
canon_verdict_change: none
---

# Selected-K126 native I1B three-momentum principal completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, spin-Levi-Civita and variational-Cartan calculation.
> Ordinary Higgs/VEV, family-index, chirality, anomaly and familiar symmetry-
> breaking constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K124's number is exact on its actual kinematics: one homogeneous radial `t`
leg and two back-to-back TT metric waves. On that slice total metric momentum
is zero, `d(D2B_LC)` vanishes, and the connection-square term reproduces

```text
C_t_h_h = -12 q^2 <H1,H2>_DW.
```

K126 now computes the common-transverse three-point extension. If the radial
leg carries momentum `r`, momentum conservation gives `r+p+q=0`. The
connection-curvature part contains

```text
F_B^(2)[(H1,p),(H2,q)]
  = (p+q) wedge D2B_LC[(H1,p),(H2,q)]
    + DB_LC[H1,p] wedge DB_LC[H2,q]
    + DB_LC[H2,q] wedge DB_LC[H1,p].                 (1)
```

The selected K77 contraction is `24` times the six diagonal horizontal
curvature cells. For the exact common-transverse TT witness

```text
p=(1,0,0,0), q=(0,0,0,1), r=(-1,0,0,-1),
H1=H2=plus  (or both cross),
```

the radial momentum is null but nonzero. The isolated co-moving connection
packet gives

```text
<Phi1,S((p+q) wedge D2B_LC)> = -24,
<Phi1,S(DB1 DB2 + DB2 DB1)>  =   0.                 (2)
```

This is a deliberately planted partial-frame trap. An independent fixed-
coordinate expansion of the complete mixed scalar curvature gives zero on
the same witness. Therefore the omitted coframe, pairing and tautological-
`Phi1` transport contributes `+24` and cancels (2). K125's warning was
load-bearing: curvature covariance is not obtained by adding `d(D2B_LC)` to a
frozen coefficient packet.

## Complete three-momentum polynomial

Let both TT polarizations lie in the common transverse `1-2` plane and let

```text
p=(a,0,0,b), q=(c,0,0,d), r=-(p+q).
```

The independent coordinate-curvature route gives the exact mixed scalar
coefficient

```text
R^(2)=2(p^2+q^2)+3 p.q.
```

Calibrating its overall K77 normalization on K124's three causal back-to-back
controls yields

```text
C_t_h_h(p,q,r)
  = -6 (p^2+q^2+3r^2) <H1,H2>_DW,                  (3)
```

with zero plus-cross and cross-plus entries. At `r=0`, `q=-p`, equation (3)
reduces to K124's `-12p^2<DW>`. On the nonzero-null-radial witness above,
`p^2+q^2=0=r^2`, so the complete coefficient is zero even though the isolated
exterior cell is nonzero.

## Partial Cartan diagnostic

The noncyclic Shiab is used directly; no cyclic trace identity is assumed.
For the witness, define the principal Cartan covector

```text
Theta^mu(Phi1;D2B) = <Phi1,S(e^mu wedge D2B)>.
```

Exact `Cl(7,7)` arithmetic on the isolated exterior cell gives

```text
Theta^mu = (-12,0,0,-12),
(p+q)_mu Theta^mu = -24.                            (4)
```

Since `r=-(p+q)`, integration by parts transfers the partial term to the radial
derivative. But this covector is not the full Cartan potential: its bulk is
cancelled by the transported natural coefficient packet on the witness. It is
retained as an exact adverse control, not promoted to a BFV charge.

## What remains unchanged

The selected `C_t_h_v` packet has only one metric leg, so `D2B_LC` cannot
enter it. Direct full-polynomial evaluation remains zero on the selected
`3 x 2 x 2 x 10 = 120` fixed-frame TT census. The K122 controls
`D3_ttt=8736` and `C_t_v_v=-(56/3)<V,*V>` are also unaffected.

## Curved lower-order boundary

K126 does not invent a curved background. At nonzero background connection,
curvature, torsion or coefficient jets, the same fixed-chart expansion gains
lower-order terms. The exact probe displays a nonzero background-connection
coordinate witness, but correctly refuses to call it a covariant invariant:
the natural coefficient packet and gauge/frame transport must be composed on
a selected background.

Therefore K126 closes the flat-germ common-transverse three-momentum
principal polynomial, not the curved lower-order operator, global phase space
or domain. A unique lower-order packet is not identifiable until the background
jet and Cartan representative/domain convention are selected.

## Scope correction to K124

| statement | disposition after K126 |
| --- | --- |
| K124 `-12q^2<DW>` | exact homogeneous-radial/back-to-back specialization of (3) |
| nonzero-null-radial witness | complete zero after `-24+24` transport cancellation |
| isolated `d(D2B_LC)` | generally live but not a complete fixed-chart action cell |
| partial noncyclic Cartan | exact adverse-control covector; not full Cartan |
| selected `C_t_h_v` | still zero on 120-entry TT packet |
| curved lower-order operator | background-dependent and open |
| global Green/BFV/domain | open |

## Reverse scaffold

```text
R0 target: complete native radial response of the I1B TT Hessian
R1--R5: K122--K124 owner, evidence and homogeneous-radial principal slice
R6 K125: generic fixed-chart curvature and noncyclic transport covariance
R7 K126 adverse control: isolated d(D2LC)=-24 is cancelled by transport +24
R8 K126 complete: common-transverse three-momentum polynomial (3)
R9 K126: K125 covariance vindicated; partial Cartan not promoted
R10 next at K127: select a stationary curved background jet and representative/domain convention
R11 then: assemble curved lower-order operator and test a unique full pencil
R12 later: common Green domain, BFV reduction and 2D-to-98D attachment
```

No ledger, canon, particle interpretation, phenomenology or GU truth-status
claim changes. Joe input is not required for K127 unless no source/action
background can be selected from existing evidence.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k126_native_i1b_radial_momentum_principal_scope_correction_probe.py
```
