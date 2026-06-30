---
title: "Y14 to K3 Index Bridge: Theorem or No-Go Map"
date: 2026-06-24
status: exploration
doc_type: theorem_nogo_map
verdict: "CONDITIONAL_BRIDGE_THEOREM; CURRENT_PHYSICAL_GU_INDEX_UNDERDEFINED"
owned_path: "explorations/generation-sector/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
depends_on:
  - "explorations/cycle-gates-and-audits/goal-draft-physical-rs-index-problem-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/analytic-index-fredholm/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md"
  - "explorations/analytic-index-fredholm/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md"
  - "explorations/analytic-index-fredholm/oc2-sobolev-a1-bounded-transform-2026-06-23.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
optional_executable:
  - "tests/y14_k3_bridge_gate.py"
---

# Y14 to K3 Index Bridge: Theorem or No-Go Map

## Inputs Read

This note uses the requested surfaces:

- `explorations/cycle-gates-and-audits/goal-draft-physical-rs-index-problem-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md`
- `explorations/analytic-index-fredholm/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md`
- `explorations/analytic-index-fredholm/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md`
- `explorations/analytic-index-fredholm/oc2-sobolev-a1-bounded-transform-2026-06-23.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`

All requested files were present. No fallback search was needed.

## 1. Verdict

**Verdict: conditional theorem, not a closed bridge.**

There is a clean theorem shape that would let a compact K3
Rarita-Schwinger index be used as the physical GU index of the noncompact
`Y^14` problem. The theorem is conditional on a precise projection, Sobolev,
compactification/APS, symbol-identification, and `H`-linear family package.

The bridge is not currently available as a proved theorem. The current status is:

```text
full unprojected noncompact Y^14 Fredholm problem:  no-go from current files
projected weighted tau/discrete Y^14 sector:        conditional
compact K3 raw RS index model:                      computed control, not physical GU
physical compact K3 GU RS index:                    specified open
Y^14 -> K3 physical-index equality:                 conditional theorem, underdefined
generation-count use:                               not allowed yet
```

The most important negative conclusion is simple:

```text
K3 raw RS index != physical noncompact GU index
```

unless the physical GU gauge-fixed or BRST RS complex is first derived and then
shown to be the K3 reduction of the same projected `Y^14` Fredholm family.

The compact K3 computation can become physically load-bearing only through one
of two exact bridges:

1. A **unitary discrete-sector bridge**, in which an `H`-linear unitary map
   identifies the finite-rank projected `Y^14` sector with a K3 RS bundle and
   intertwines the physical operators modulo compact homotopy.
2. An **APS/compactification bridge**, in which the noncompact end is replaced
   by a compact problem with boundary, the boundary operator is the same
   projected/gauge-fixed physical RS operator, and all `eta`, kernel, and
   spectral-flow corrections are computed.

Without one of these bridges, the K3 calculation is a compact control model.
It is not a theorem about the physical noncompact `Y^14` index.

### Bridge Condition Ledger

```json
{
  "version": "2026-06-24",
  "verdict": "CONDITIONAL_THEOREM_CURRENTLY_UNDERDEFINED",
  "current_decision": "OPEN_MISSING_BRIDGE_DATA",
  "k3_raw_index_status": "CONTROL_ONLY",
  "y14_full_unprojected_status": "NO_GO",
  "required_bridge_conditions": [
    {
      "id": "C1_PHYSICAL_RS_COMPLEX",
      "status": "open",
      "failure_decision": "OPEN_MISSING_SYMBOL_DATA"
    },
    {
      "id": "C2_TAU_DISCRETE_PROJECTION",
      "status": "conditional_open",
      "failure_decision": "NO_GO_EMPTY_OR_UNBOUNDED_SECTOR"
    },
    {
      "id": "C3_WEIGHTED_FREDHOLM_PARAMETRIX",
      "status": "conditional_open",
      "failure_decision": "NO_GO_NON_FREDHOLM"
    },
    {
      "id": "C4_K3_REDUCTION_OR_APS_COMPACTIFICATION",
      "status": "open",
      "failure_decision": "UNDERDEFINED_BRIDGE_MAP"
    },
    {
      "id": "C5_SYMBOL_CLASS_MATCH",
      "status": "open",
      "failure_decision": "OPEN_MISSING_SYMBOL_DATA"
    },
    {
      "id": "C6_RIGHT_H_STRUCTURE",
      "status": "conditional_open",
      "failure_decision": "COMPLEX_ONLY_H_STRUCTURE_MISSING"
    },
    {
      "id": "C7_BACKGROUND_CH2_F",
      "status": "open",
      "failure_decision": "OPEN_BACKGROUND_DEPENDENT"
    },
    {
      "id": "C8_BOUNDED_TRANSFORM_FAMILY",
      "status": "conditional_open",
      "failure_decision": "UNDERDEFINED_FAMILY_KSP_CLASS"
    },
    {
      "id": "C9_BOUNDARY_ETA_AND_SPECTRAL_FLOW",
      "status": "open_if_boundary_used",
      "failure_decision": "APS_CORRECTION_UNCOMPUTED"
    },
    {
      "id": "C10_NONCIRCULAR_GENERATION_READOUT",
      "status": "guard_active",
      "failure_decision": "INVALID_CIRCULAR"
    }
  ],
  "forbidden_inputs": [
    "ind_H(D_RS)=8",
    "ind_H(D_GU)=24",
    "rank_eff=4",
    "rank_eff=8",
    "three_generations",
    "physical_DOF_count_as_index"
  ]
}
```

## 2. Physical `Y^14` Index Problem

The actual noncompact problem is not the closed K3 operator. It is a right
`H`-linear Fredholm problem for the physical GU RS block on the noncompact
`Y^14` geometry.

The formal target has the shape:

```text
D^Y_RS,delta,disc
  = P_disc e^{delta r} D^Y_RS e^{-delta r} P_disc
  : W^{1,2}_{H,delta,disc}(Y^14,S)
      -> L^2_{H,delta,disc}(Y^14,S),
```

where:

- `S = H^64` is the `Cl(9,5) ~= M(64,H)` spinor module;
- `D^Y_RS` is the actual physical RS Schur/gauge-fixed block derived from
  `D_GU`, not merely a raw gamma-trace-free comparison operator;
- `r` is an end/radial function and `delta` is a weight avoiding indicial or
  Plancherel walls;
- `P_disc` is the tau-twisted relative discrete/residual projection for the
  corrected `SL(4,R)/SO_0(3,1)` fiber problem with the `S(6,4)` and RS
  coefficient data;
- `W^{1,2}_{H,delta,disc} = P_disc W^{1,2}_{H,delta}` only after `P_disc` is
  proved bounded on the weighted Sobolev scale.

The desired noncompact physical index is:

```text
Ind_Y_RS = ind_H(D^Y_RS,delta,disc).
```

This number exists only if the projected operator is closed, has finite
right-`H` kernel and cokernel, has closed range, and is stable under the
allowed family variation. In family form the analytic object is:

```text
F_x^Y = D_x^Y (1 + (D_x^Y)^*D_x^Y)^(-1/2) : X -> Fred_H(K_H).
```

The formal `KSp` classification is not the hard part. Once a fixed separable
quaternionic Hilbert space `K_H` and norm-continuous bounded transforms are
available, the class lies in:

```text
[X,Fred_H(K_H)] = KSp^0(X) = KO^4(X).
```

The current obstruction is analytic and representational: the full unprojected
operator on noncompact `Y^14` is not defensibly Fredholm from the current files.
Its split-signature principal symbol has a null cone:

```text
sigma(D_GU)(xi)^2 = g_Y(xi,xi) Id,
```

and the noncompact fiber carries continuous spectrum. Therefore ordinary
compact elliptic Fredholm theory cannot be imported. The only live
noncompact route is the projected weighted discrete/residual sector, and that
route remains conditional.

## 3. Compact K3 Model And What It Currently Proves

The compact model uses a closed Riemannian K3 surface. Its fixed topological
inputs are:

```text
Ahat(K3) = 2
chi(K3) = 24
sigma(K3) = -16
p1(TK3)[K3] = -48
```

Let:

```text
V = T_C^*K3
F = s^*S(6,4)
n = rank_C(F)
k = ch_2(F)[K3].
```

For the GU internal bundle, the expected rank is:

```text
n = 16
rank_H(F) = 8, if the right-H structure and connection are verified.
```

The current K3 raw RS computation establishes a characteristic-class formula
for the standard raw gamma-trace-free RS symbol class:

```text
E_raw = (V + 1) tensor F
ind_C(E_raw) = -38 n + 5 k.
```

In the flat/trivial `F` branch:

```text
n = 16
k = 0
ind_C(E_raw) = -608
ind_H(E_raw) = -304, only if the right-H certificate is supplied.
```

A familiar BRST/anomaly-style comparison class would be:

```text
E_BRST_style = (V - 1) tensor F
ind_C(E_BRST_style) = -42 n + 3 k.
```

In the flat branch this gives:

```text
ind_C(E_BRST_style) = -672
ind_H(E_BRST_style) = -336, only if H-linear.
```

That class is not currently derived from the GU physical gauge fixing. It is a
comparison class. Subtracting ghost complexes because the formula is familiar,
or because it moves an index toward a desired generation count, is invalid.

Therefore the compact K3 model currently proves exactly this:

1. The raw gamma-trace-free K3 RS control index is computable.
2. The flat-`F` raw and BRST-style comparison classes produce large
   `OTHER_INDEX` values, not Candidate A or Candidate B.
3. The physical constrained/gauge-fixed GU RS symbol class is still missing.
4. The background value `k = ch_2(F)[K3]` is not fixed by the current physical
   `Sp(64)` background.
5. The right-`H` conversion is allowed only after the global `H` structure and
   connection compatibility are verified.

Thus the K3 model is a useful compact control surface. It is not yet the
physical GU index.

## 4. Exact Bridge Conditions

### Conditional Bridge Theorem

Let `D^Y_RS` be the actual physical GU RS operator or elliptic RS complex on
noncompact `Y^14`. Let `D^K_RS` be the compact K3 physical RS operator or
elliptic complex obtained from the same GU data after section pullback,
projection, or compactification.

If Conditions C1-C10 below hold, then the K3 physical RS index is the physical
noncompact GU RS index, possibly with explicitly computed APS/end and
spectral-flow corrections:

```text
Ind_Y_RS
  = Ind_K3_RS^phys
    - (eta(A_RS^phys) + h(A_RS^phys))/2
    + SF_bridge
    + C_end.
```

For closed K3 with a unitary discrete-sector reduction and no boundary/end
correction, this reduces to:

```text
Ind_Y_RS = Ind_K3_RS^phys.
```

Only in that reduced case may the compact K3 RS index be used directly as the
physical GU index.

### C1. Physical RS Complex

The RS object must be derived from the actual GU operator/action. The artifact
must specify the bundles, chirality conventions, gamma-trace maps, gauge maps,
gauge condition, and ghost or subtraction fields. A raw gamma-trace-free
operator does not become physical by name.

Minimum data:

```text
E_RS^+
E_RS^-
G_+, G_-                 gamma-trace maps
P_+, P_-                 gamma-trace projectors
g_+                      gauge symbol
gauge-fixing block       if using an operator
ghost complex            if using a BRST/elliptic complex
sigma_RS^phys(xi)        for all xi != 0
```

If this data is absent, the bridge decision is:

```text
OPEN_MISSING_SYMBOL_DATA.
```

### C2. Tau-Discrete Projection

There must be a nonempty finite-multiplicity tau-twisted relative
discrete/residual sector for the actual coefficient system:

```text
P_disc : L^2_H(Y^14,S) -> L^2_{H,disc}(Y^14,S).
```

The projection must be:

- right-`H` linear;
- orthogonal or otherwise compatible with the Fredholm domain proof;
- bounded on `L^2_{H,delta}` and `W^{1,2}_{H,delta}`;
- invariant under the physical RS operator, at least modulo compact controlled
  terms;
- stable under the allowed family variation.

The scalar sector on `SL(4,R)/SO_0(3,1)` has no scalar discrete series in the
current notes. Thus the noncompact physical sector cannot be inherited from a
scalar BC1 shortcut. The open representation-theoretic claim is that the
tau-twisted `S(6,4)`/RS coefficient system creates the needed discrete or
residual sector.

If `P_disc = 0`, the projection is trivially bounded but physically empty.
If `P_disc` is unbounded on weighted Sobolev spaces, the bridge fails.

### C3. Weighted Fredholm Parametrix

For some weight `delta` avoiding indicial roots and Plancherel walls, the
projected operator must have a compact-remainder parametrix:

```text
Q_delta D^Y_RS,delta,disc = I_disc - Pi_ker + K_L
D^Y_RS,delta,disc Q_delta = I_disc - Pi_coker + K_R,
```

where `Pi_ker` and `Pi_coker` are finite-rank `H`-linear projections and
`K_L`, `K_R` are compact on the selected Hilbert space.

The proof may use a spectral parametrix, b-calculus, 0-calculus, scattering
calculus, edge/fibred-boundary calculus, or a rank-3 fibred-corners calculus.
The common requirement is the same: the normal/indicial family at infinity is
invertible on the chosen weight line after projection.

### C4. K3 Reduction Or APS Compactification Map

There must be an actual map from the noncompact problem to the compact K3
problem. One of the following is enough.

**Unitary reduction route.** A finite-rank `H`-bundle `Z -> K3` of normalized
discrete modes and an `H`-linear unitary:

```text
U : L^2_H(K3,Z) -> P_disc L^2_H(Y^14,S)
```

such that:

```text
U^{-1} P_disc D^Y_RS P_disc U
```

has the same principal symbol and Fredholm index as `D^K_RS`, up to compact
homotopy.

**APS/compactification route.** A compactification or truncation of the
noncompact end to a compact problem with boundary, together with the APS
operator for the same physical projected/gauge-fixed RS complex:

```text
index_APS
  = bulk_index - (eta(A_RS^phys) + h(A_RS^phys))/2.
```

Older `S^3` or spin-1/2 eta cancellations cannot be imported unless the
boundary operator is exactly the same physical RS boundary operator.

### C5. Symbol-Class Match

The K3 symbol class must be the reduction of the physical `Y^14` symbol class
in `K^0_c(T*K3)` or in an equivalent elliptic-complex class. It is not enough
to say both objects are "Rarita-Schwinger".

The current raw class:

```text
E_raw = (V + 1) tensor F
```

is available only as a control. The physical class may be `E_raw`,
`E_BRST_style`, or something else. The class must be derived before indexing.

### C6. Right-`H` Fredholm Family

Every map in the bridge must preserve the right-`H` structure:

- the `Cl(9,5) ~= M(64,H)` left action commutes with right multiplication;
- the `Sp(64)` connection preserves the right-`H` metric;
- gamma-trace projectors, gauge-fixing, ghost maps, `P_disc`, and the
  reduction/compactification maps are right-`H` linear;
- the bounded transforms form a norm-continuous family:

```text
F_x = D_x(1 + D_x^*D_x)^(-1/2) : X -> Fred_H(K_H).
```

If only a complex Fredholm index is justified, the decision is:

```text
COMPLEX_ONLY_H_STRUCTURE_MISSING.
```

### C7. Background Chern Character

The K3 formula must carry the internal background honestly:

```text
F = s^*S(6,4)
n = rank_C(F) = 16
k = ch_2(F)[K3].
```

If `k` is not fixed by the physical `Sp(64)` connection and section pullback,
the result is background dependent:

```text
OPEN_BACKGROUND_DEPENDENT.
```

A fixed physical generation-count index cannot be claimed from a formula that
still contains an unspecified `k`.

### C8. Family Continuity And Spectral Flow Control

The bridge must be stable over the observer parameter space, not merely at one
sample point. The varying `L^2` spaces and domains must be identified by
right-`H` unitaries, and:

```text
x |-> D_x : W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}
```

must be continuous strongly enough to imply norm continuity of the bounded
transforms.

If the bridge uses spectral sections or Riesz projections, zero crossings and
threshold collisions must be controlled. Any spectral flow between the
noncompact and compact problems must either vanish or be included in
`SF_bridge`.

### C9. Boundary And End Corrections

Closed K3 has no boundary term. A punctured K3, collar model, or compactified
end does. In those cases the physical index is:

```text
Ind_Y_RS = bulk_K3_like_index - (eta + h)/2 + end/spectral-flow corrections.
```

K3 can be used directly only if those correction terms are proved to vanish for
the same physical RS boundary operator or are explicitly added to the final
index.

### C10. Non-Circular Generation Readout

The following values are forbidden as inputs:

```text
ind_H(D_RS) = 8
ind_H(D_GU) = 24
rank_eff = 4
rank_eff = 8
three generations
physical degree-of-freedom count as an analytic index
```

They may appear only after the independent index and bridge theorem are
complete.

## 5. Failure Modes And Counterexamples

### F1. Full Unprojected `Y^14` Fredholmness

The full unprojected `Y^14` operator is not currently Fredholm. The split
signature symbol has a null cone and the noncompact fiber carries continuous
spectrum. This blocks any direct appeal to compact elliptic theory.

Decision:

```text
NO_GO for the full unprojected noncompact Fredholm claim.
```

### F2. Empty Discrete Sector

If the tau-twisted `S(6,4)`/RS coefficient system does not create a nonempty
relative discrete or residual sector, then:

```text
P_disc = 0.
```

This is bounded but physically empty. The K3 compact index would then be a
separate compact calculation, not the noncompact `Y^14` physical index.

### F3. Unbounded `P_disc` At Zero Crossings

The A1 note gives a failure family where section deformations carry discrete
eigenvalues through zero. Near a crossing:

```text
||(D_{s_t} - z)^(-1)|| ~ 1 / |z - lambda_j(t)|
```

and the Riesz projection norm can blow up as `lambda_j(t) -> 0`. The bounded
transform may still exist, but the projection-based bridge must handle the
crossing with spectral sections or explicit spectral-flow terms.

### F4. Weight Or Indicial Failure

If `delta` crosses an indicial root or a Plancherel wall, the weighted
Fredholm package fails. A K3 index then cannot be imported as a stable
noncompact index.

### F5. Rank-3 End Calculus Failure

The full `A3` fiber end has corner structure. Single-face b-calculus for the
dilaton direction is not enough unless the remaining Weyl-chamber faces are
controlled by a rank-3 fibred-corners, scattering, edge, or equivalent
calculus.

### F6. Raw K3 Index Promoted To Physical Index

The raw class gives:

```text
ind_C(E_raw) = -38 n + 5 k.
```

The BRST-style comparison class gives:

```text
ind_C(E_BRST_style) = -42 n + 3 k.
```

These differ by two spinor complexes. Therefore a change in gauge/ghost data
changes the index. Promoting `E_raw` to the physical GU index without deriving
the physical complex is a counterexample to the bridge discipline, not a proof.

### F7. Unfixed `ch_2(F)`

Even after a physical K3 symbol is found, a formula depending on
`k = ch_2(F)[K3]` is not a fixed generation-count index. It is a family of
background-dependent indices.

### F8. Missing Right-`H` Certificate

A complex index cannot be halved just because the ambient algebra looks
quaternionic. The right-`H` structure must be global and preserved by the
connection, the operator, the projection, and the boundary/reduction maps.

### F9. Wrong APS Boundary Operator

APS correction terms belong to a specific boundary operator. An eta value for
an unrelated spin-1/2 or unprojected boundary Dirac operator does not compute
the physical RS APS correction.

### F10. Same K3 Bulk, Different Ends

Two noncompact compactifications can have the same K3-like bulk symbol and
different `eta`, kernel, or spectral-flow corrections. They then have different
physical noncompact indices. The compact K3 bulk number alone is not enough.

### F11. Continuous Sector Not Removed

If the continuous sector remains coupled to the physical RS block, the compact
K3 discrete count is at best a sub-index. The bridge must either prove the
continuous sector is excluded by the physical projection or include its effect.

### F12. Family Noncontinuity

Pointwise Fredholmness is not enough for a `KSp` family class. If the bounded
transforms fail to vary norm-continuously, the Atiyah-Jannich/KSp readout is
not available over the observer parameter space.

## 6. What This Means For Generation-Count Claims

The generation-count claim remains open.

The live governance state remains:

```text
RS-RAW:      advanced_but_open, usable as raw control only
RS-SYMBOL:   specified_open
GEN-COUNT:   open
```

The compact K3 raw index does not support Candidate A or Candidate B. In the
flat-`F` raw branch it gives:

```text
ind_H(E_raw) = -304, if H-linear.
```

In the flat BRST-style comparison branch it gives:

```text
ind_H(E_BRST_style) = -336, if H-linear.
```

Both are `OTHER_INDEX` controls for simple classes, not physical generation
counts.

Only after the physical GU RS index and the `Y^14 -> K3` bridge are proved may
one compare:

```text
I = ind_H(D_RS^phys).
```

Then the existing decision convention is:

```text
I = 8:
  Candidate A
  total_H_index = 16 + 8 = 24
  generation_count = 24 / 8 = 3

I = 16:
  Candidate B
  total_H_index = 16 + 16 = 32
  generation_count = 32 / 8 = 4

I not in {8,16}:
  OTHER_INDEX
  total_H_index = 16 + I
  generation_count = (16 + I) / 8
```

If `16 + I` is not divisible by `8`, the current generation normalization does
not produce an integral generation count. If the bridge is missing,
background-dependent, complex-only, non-elliptic, or circular, no generation
readout is allowed.

## 7. Next Meaningful Proof Or Computation Step

The next useful step is not another raw rank calculation. It is a bridge
certificate with one positive or negative answer.

The most efficient proof packet is:

1. Derive the physical GU RS complex from the actual typed operator/action.
   State whether the source is the current `D_GU`, `D_roll`, or a deliberately
   branched comparison operator.
2. Build the K3 principal symbol for that same physical complex and determine
   its K-theory class. Decide whether it is `E_raw`, `E_BRST_style`, or a third
   class.
3. In parallel, prove or refute the tau-twisted noncompact projection theorem:
   nonempty finite `P_disc`, bounded on `L^2_{H,delta}` and
   `W^{1,2}_{H,delta}`, invariant for the physical RS block, and stable in the
   family.
4. Construct one explicit bridge map:
   an `H`-unitary KK/discrete-mode reduction `U`, or an APS compactification
   with the physical RS boundary operator and computed correction terms.
5. Only then evaluate the K3 characteristic-class formula and compare with
   Candidate A/B.

The optional audit for this note is:

```text
python tests/y14_k3_bridge_gate.py
```

It checks the bridge ledger and decision logic. It is not a proof of the
physical GU index.

## Final Decision

Current decision:

```text
CONDITIONAL_BRIDGE_THEOREM_CURRENTLY_UNDERDEFINED
```

The theorem shape is sharp enough to be useful: if C1-C10 are supplied, the K3
physical RS index can be used as the physical noncompact GU index, with any
APS/end/spectral-flow corrections included. But the current files do not yet
supply the physical RS symbol class, the nonempty bounded tau-discrete sector,
the `Y^14 -> K3` unitary or APS bridge, the `ch_2(F)` background, or the full
right-`H` family certificate.

Until those are supplied, K3 remains a compact control model and the physical
generation-count index remains open.
