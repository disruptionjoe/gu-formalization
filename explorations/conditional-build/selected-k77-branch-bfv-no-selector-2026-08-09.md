---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: NONZERO_BRANCH_AMPLITUDES_SYMPLECTOMORPHIC__CLASSICAL_MINIMAL_EDGE_BFV_CME_EXACT_STRATUMWISE__COMMON_DOMAIN_QUANTUM_MEASURE_AND_PHYSICAL_SELECTION_OPEN
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# K77 branch symplectic equivalence and classical edge BFV

## Result in plain English

The previous next gate accidentally asked to build something the repository
already had. v0.103 constructed the compact-boundary `H^7 x H^-7` strong
cotangent phase space and its real vertical polarization. This wave composed
the two new v0.113 branch amplitudes with that existing object instead of
rebuilding it.

The two opposite-sign Galois branches are the same **classical symplectic
phase-space type**. If `Omega_p=p Omega_0`, the exact real map

```text
(Theta,P) -> (Theta,(p_plus/p_minus)P)
```

pulls `Omega_p_minus` back to `Omega_p_plus`. It preserves the vertical
polarization and leaves the unique edge coefficients `(-1,+1)` unchanged.
Consequently neither strong Sobolev completion, the vertical polarization,
minimal-edge horizontality nor classical BFV closure can choose one nonzero
branch or determine its amplitude.

On every declared nonempty compact-boundary edge-torsor stratum, add the
cotangent momentum `ell in H^-8` for the `H^8` edge group and impose the
first-class coisotropic constraint `G=-mu_v0.103+ell=0`. (The minus sign
reorients v0.103's recorded minus-moment convention.) The minimal edge-gauge
horn then has the standard classical BFV charge

\[
Q=c^a\mu_a-\frac12 f_{ab}{}^c c^a c^b b_c.
\]

The `c c mu` coefficients of `{Q,Q}` vanish by the already-built first-class
moment-map algebra, and the `c c c b` coefficients vanish by Jacobi. Omitting
the cubic ghost term gives a nonzero exact failure on a nonabelian `sl_2`
control. The charged boundary-symmetry horn remains a distinct physical
current-algebra rival; it is not silently quotiented.

This is classical and stratum-wise. It does not prove that the global edge
torsor is nonempty, construct a bulk Green/Krein domain preserving the trace
spaces, couple bulk BV to boundary BFV, choose a quantum contour or measure,
cancel anomalies, select the physical horn or select among the Spin-native,
two-`U(32,32)` and full-`U(64,64)` action parents.

## Layer 0 and prior art

| phrase | object here | distinct from |
| --- | --- | --- |
| strong boundary phase space | v0.103 `H7 x H-7` cotangent completion | a new v0.114 construction |
| branch equivalence | symplectomorphism for nonzero scalar multiples | equality of actions, Hessians or quantum orientations |
| boundary BFV | classical odd extension of edge first-class constraints | G3 bulk minimal BV |
| CME | componentwise classical master equation | quantum master equation/anomaly cancellation |
| edge horn | gauge reduction on a nonempty torsor stratum | charged physical boundary symmetry |
| vertical polarization | real cotangent polarization | complex contour, positive state or measure |

G3 already builds bulk minimal BV through antifield number one, while v0.103
builds the even boundary reduction. Neither contains the edge-boundary odd BFV
charge constructed here. The source confirms the tilted bulk grammar and its
boundary debt but is silent on all BFV and selection data.

## Exact symplectic theorem

Let `p,q` be nonzero real scalars and write `Omega_p=p Omega_0` on the strong
cotangent product. Then

\[
T_{p\to q}=\operatorname{diag}(1,p/q),\qquad
T_{p\to q}^{*}\Omega_q=\Omega_p.
\]

The momentum rescaling is a bounded isomorphism of `H^-7`; for opposite signs
it includes momentum reversal. It sends the vertical subspace to itself. All
primitive endpoint and edge terms scale homogeneously, so the horizontality
equations still fix `c_0=-1,c_3=+1` independently of `p`.

This theorem is deliberately classical. An action, path-integral orientation,
reality condition or quantum measure can distinguish data a symplectic
isomorphism does not; no claim about those is made.

## Classical minimal edge BFV

Use ghosts `c` in the `H^8` boundary gauge algebra and ghost momenta `b` in
its continuous dual `H^-8`. The coisotropic ambient is the physical cotangent
space times the cotangent bundle of the edge group. With
`G=-mu_v0.103+ell`, the reoriented constraints satisfy

\[
\{\mu_a,\mu_b\}=f_{ab}{}^c\mu_c,
\]

the displayed `Q` has two possible master-equation coefficient families:

- `c^a c^b mu_c`: the first-class closure defect;
- `c^a c^b c^c b_e`: the Jacobi defect.

Both vanish identically. The primary exact probe realizes the moment maps in
the canonical two-dimensional `sl_2` representation and checks every
coefficient. The independent Sage/FLINT route reconstructs the quadratic
field, symplectic map, structure constants, moment maps and both defect
families from scratch.

Primary probe: `49/49 PASS`. Independent Sage/FLINT: `21/21 PASS`.

## Constraint and physical fences

The edge cotangent momentum and ghost pair resolve an existing gauge
redundancy and add no physical field or fit parameter. No continuous residue, discrete datum,
booked quotient or P1/P2/P3 entry moves. The two nonzero branches remain
physical candidates on either live boundary horn; classical boundary geometry
has now been proved unable to select their relative sign or amplitude.

The selected Spin-native carrier remains the operative conditional parent.
Curt's two `U(32,32)` Weyl halves and the later full `U(64,64)` principal group
remain separate rival parents requiring their own enlarged action traces.

## Progress and next gate

```text
Ledger v0.114 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84..86; >=19 function-valued slots; 9 forks; 5 booked quotients

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Next: prove global edge-torsor nonemptiness/topology and construct one bulk
Green/Krein domain preserving the `H7/H-7` physical traces and `H8/H-8` ghost
traces. Only then test coupled bulk-boundary BV-BFV compatibility. Keep the
charged horn, quantum measure and action-parent selection open.
