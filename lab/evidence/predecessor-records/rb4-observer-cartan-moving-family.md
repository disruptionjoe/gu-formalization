---
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-RB4
status: completed
created: 2026-07-31
branch: agent/operator-anomaly-big-swing
---

# RB4 observer/Cartan moving-family construction

## Target

Construct the moving reduction \(\chi\) needed by the conditional
fixed-Cartan four-component/full-20 lift, derive its variation, and decide
which of four mutually exclusive ownership classes it occupies:

1. a composite of the already-varied GU geometry, section, and
   \(\epsilon_{\rm IG}\);
2. a gauge/Cartan reduction with contractible continuous fibre and no new
   physical datum after quotient;
3. a dynamical order parameter that the source action must select; or
4. a genuinely new continuous external datum.

The fixed-Cartan result may enter N1 only after the moving family is
constructed and the ownership invoice is explicit.

## Layer 0

The following objects are not identified without a typed map:

| phrase | object |
| --- | --- |
| observer \(u\) | a future unit timelike line/vector in the base Lorentz four-plane |
| observer reduction | \(SO^+(3,1)\to SO(3)\), with fibre \(H^3\) |
| trace direction \(t\) | the canonical DeWitt-negative line in \(\operatorname{Sym}^2T^*X\) after Frobenius trace reversal |
| compatible \(J\) | an orthogonal complex structure on the trace-reversed \((6,4)\) fibre; the family is \(O(6,4)/U(3,2)\), and no member is canonical from the old trace/Lorentz data |
| \(Jt\) | the negative line to which a chosen \(J\) sends the distinguished trace direction; not a base observer or a count |
| \(W_4(u)\) | \(\mathbb Rt\oplus(u^\flat\odot u^\perp)\), conditional on \(u\) and the trace line |
| fibre Cartan reduction | a maximal-compact reduction of the native \((6,4)\) Frobenius fibre |
| internal \(\operatorname{Spin}(4)\) | the compact factor in \(\operatorname{Spin}(6)\times\operatorname{Spin}(4)\); its generators moving \(t\) are not base Lorentz boosts |
| \(\epsilon_{\rm IG}\) | the already-varied N1 soldering/IG section that can move the ambient Clifford plane |
| \(s:X\to Y\) | the metric/observer section; it selects a Lorentz metric, not automatically a timelike observer or internal Cartan point |
| P1/P2 | the already-typed flat real orientation line / vertical RS-symbol phase, conditionally one global \(Z/2\) bit |
| P3 | the separate relative real-\(KO\) twist; never a multiplicity or count readout |

Therefore \(\chi\) is **not** called P2. Only a residual orientation of a
constructed moving family may be compared with the P1/P2 line.

## Native construction and hostile comparators

- Native fibre:
  \(\operatorname{Sym}^2T^*X\) with Frobenius signature \((7,3)\), followed
  by DeWitt trace reversal to \((6,4)\).
- Hostile control: the raw \((7,3)\) Frobenius form.
- Native pairing: the active Krein/gimmel pairing; no positive-Hilbert
  replacement.
- Base covariance and internal covariance are computed separately:
  \[
  W_4(\Lambda u)=\operatorname{Sym}^2(\Lambda)W_4(u)
  \]
  does not by itself prove covariance under internal
  \(\operatorname{Spin}(4)\) rotations that move \(t\).
- The standard observer reduction and the program-native
  \(\epsilon_{\rm IG}\) orbit are both checked before any kill is accepted.

## Source branch

The local primary-source check is evidence about intended ownership, not a
proof. The 2025 Into the Impossible transcript says:

- trace reverse the vertical Frobenius metric from \((7,3)\) to \((6,4)\);
- “reduce maximal compact subgroups along the fibers”;
- take “the one dimension that's distinguished in the space of all
  metrics,” ask “where that gets sent,” and obtain Lorentz breaking “in a
  certain sense.”

This language is tested against:

- the 2021 author draft;
- the official Portal/Oxford transcript;
- the 2025 TOE transcript;
- the existing primary-source reinspection packet; and
- the repo-native definitions of \(s\), \(T_\omega\), and
  \(\epsilon_{\rm IG}\).

The expected source verdict, declared before the RB4 computation, is:

```text
SOURCE-BOUND / DYNAMICAL-REDUCTION-INTENT,
NOT SOURCE-EXPLICIT AS A TYPED FIELD OR ACTION TERM.
```

The phrase “this has a complex structure” also creates a mandatory rival:
\(\chi\) may be a moving compatible \(J\), or a flag containing \(J\) and
the trace line, rather than only the base observer \(u\). Existing owner
`VG-V3-j-commutant-conformal-native` proves that no orthogonal \(J\)
commutes with the trace projector or the full \(SO(3,1)\) data. RB4 treats
that as a no-canonicity theorem, not as a no-existence theorem: the moving
family still exists after trace reversal and may be a dynamical reduction.

## Expected mathematical verdict

Declared before execution:

```text
BASE-LORENTZ MOVING-u FAMILY: EXPECTED TO CLOSE EXACTLY.
FIXED-u/FIXED-t FAMILY: EXPECTED TO CLOSE ONLY UNDER ITS STABILIZER.
INTERNAL-SPIN4 MOVING-t FAMILY: EXPECTED TO REQUIRE EXPLICITLY MOVING t.
COMPATIBLE-J FAMILY: EXPECTED TO EXIST ONLY AFTER TRACE REVERSAL, TO MOVE
  COVARIANTLY AS O(6,4)/U(3,2), AND NOT TO BE CANONICAL.
CONTINUOUS OBSERVER CHOICE: EXPECTED TO BE GAUGE/CONTRACTIBLE IF THE
  WHOLE ASSOCIATED FAMILY IS CARRIED.
INTERNAL CARTAN/TRACE PLACEMENT: EXPECTED TO BE COMPOSITE IN
  epsilon_IG OR A DYNAMICAL ORDER PARAMETER, NOT P2.
```

This expectation is falsifiable and will be reported as failed if the exact
probe or ownership audit disagrees.

## Kill conditions

Kill the RB4 insertion into N1 if any one of these survives controls:

1. the jointly transported \(u,W_4,P_W\) family fails induced base-Lorentz
   covariance;
2. the DeWitt restriction on \(W_4\) loses the required four-dimensional
   negative sector or the complement loses the six-dimensional positive
   sector;
3. the required Clifford, volume, orientation, Krein, or right-\(\mathbb H\)
   maps cannot be transported jointly;
4. internal \(\operatorname{Spin}(4)\) covariance is claimed while keeping
   \(t\) fixed and the known moving-\(t\) leakage remains;
5. \(\chi\) is inserted as a free continuous coefficient without a gauge
   quotient, a construction from \(\epsilon_{\rm IG}\), or an Euler
   equation;
6. the \(\chi\)-variation is omitted from a term whose projector or
   zero-order operator depends on \(\chi\);
7. a source passage is used to identify a gauge transformation, metric
   section, timelike observer, Cartan involution, and soldering field without
   the required maps;
8. the branch breaks any carried Standard Model/Yukawa/provenance,
   quantum/Krein/BV, gravity/cosmology, UV/causality, or P3
   index/count-separation interface without a replacement construction;
9. a multiplicity, four-component image, 44-block support count, or
   transcript phrase is read as a physical generation/count result.
10. a fixed compatible \(J\) is called native or Lorentz invariant despite
    the exact VG-V3 commutant obstruction, or \(Jt\) is silently identified
    with \(u\), P1/P2, or a physical compactification.

## Positive and hostile controls

The executable probe must include:

- projector idempotence, ranks \(4+6=10\), and DeWitt orthogonality;
- raw Frobenius and trace-reversed signatures;
- finite and infinitesimal joint base-Lorentz transport;
- fixed-projector and fixed-observer planted failures;
- exact \(SO(3)\) stabilizer closure;
- internal fixed-\(t\) leakage and moving-\(t\) restoration as separate
  tests;
- orientation reversal as a planted disconnected component;
- a non-timelike observer plant;
- existence of an orthogonal \(J\) on \((6,4)\), nonexistence on the raw
  \((7,3)\) comparator, negativity and orthogonality of \(t,Jt\), and joint
  \(O(6,4)\) transport;
- fixed-\(J\) failure against a transformation that moves \(J\);
- reconstruction of \(W_4\) from transported primitives rather than
  matching a permissive label; and
- no target count or Standard Model label in the executable input.

## Variation to construct

For a normalized timelike \(u\), write the mixed subspace through a spanning
map \(B(u)\) and its DeWitt Gram matrix

\[
G_W(u)=B(u)^\top G_{\rm DW}B(u).
\]

The orthogonal projector is

\[
P_W(u)=B(u)G_W(u)^{-1}B(u)^\top G_{\rm DW}.
\]

Its variation must be evaluated either by differentiating this expression
or by the invariant projector identity

\[
\delta P_W
=P_{W^\perp}\,\delta P_W\,P_W
+P_W\,\delta P_W\,P_{W^\perp},
\qquad
P_W\delta P_WP_W=0.
\]

For every N1/RB3b operator \(\Phi_\chi\) built from \(P_W(\chi)\), record

\[
\delta_\chi S_{20}
=\frac12\operatorname{Re}
\langle Z,\mathbb K_{\mathbf G}
  (\delta_\chi\Phi_\chi)Z\rangle
\]

and all additional \(\epsilon_{\rm IG}\), section, Hodge, density, and
connection dependence. If \(\chi=\chi(\epsilon_{\rm IG},s)\), use the chain
rule and do not add a second independent field.

## Five-leg non-regression

| leg | RB4 requirement |
| --- | --- |
| SM/Yukawa/provenance | no Pati--Salam or four-component physical placement until the moving reduction and zero-order \(P_0/\rho/Y_K/Y_C/C\)-reality map are built |
| quantum/Krein/BV | active Krein pairing, moving-field ghost/antifield ownership if independent, and no positive-Hilbert projection |
| gravity/cosmology | Frobenius trace reversal remains load-bearing; distinguish metric-trace variation from vertical connection trace; propagate section/soldering variation |
| UV/causality | retain the \(g=1\) cure, common moving causal cone, and full-\(Sp\) versus stabilizer fork |
| P3/index/count | carry the relative \(KO\) twist without reading any image, support, kernel, or block number as an index/count |

## Outputs

- `tests/channel-swings/rb4_observer_cartan_moving_family_probe.py`
- `explorations/rb4-observer-cartan-moving-family-2026-07-30.md`
- scoped append/correction to the N1/N3 and RB3b owners
- scoped integration updates in `NEXT-STEPS.md`,
  `explorations/README.md`, and `tests/README.md`

No canon, claim-status, public-posture, mass, stationary-vacuum, anomaly,
unitarity, index, or generation-count change is authorized by this run.

## Execution result

The native probe passes.

```text
W4(u) signature:                       (0,4)
A6(u) signature:                       (6,0)
joint base-Lorentz P_W defect:         3.33e-16
frozen P_W boost residual:             1.940205721
joint Clifford/Phi defect:             1.11e-15
frozen soldering residual:             4.857134150
frozen-volume Phi residual:            7.760822882
internal moving-t defect:              5.55e-17
internal fixed-t residual:             3.188874624
fixed-u rotation moves J:              1.790325043
fixed-u rotation moves Jt:             0.407134320
P_W-compatible J-family nullity:       8
```

The expected moving-\(u\) and moving-\(t\) verdicts passed. The original
idea that the source's \(J\) might be absorbed into the observer family
failed a hostile descent check:

\[
u\ \longmapsto\ J
\]

is not well defined because the fixed-\(u\) \(SO(3)\) stabilizer moves every
candidate compatible \(J\). The passing joint-\(J\) transport had carried a
spatial frame, an additional object. This is the run's main Layer-0
correction.

The source verdict agrees with preregistration:

```text
SOURCE-BOUND / DYNAMICAL-REDUCTION-INTENT
```

but the likely field is now more sharply typed as a compatible
complex--Cartan flag, not merely \(u\). Weinstein's \(t\mapsto Jt\)
language is consistent with a Lorentz-breaking order parameter; it is not a
typed source action or VEV receipt.

## Ownership disposition

```text
u -> P_W(u):                       CONSTRUCTED POINTWISE/COVARIANTLY
u -> full Cartan orbit:            SPECIAL 3D SEED, NOT FULL 24D DEFINITION
u -> J:                            REFUTED
epsilon_IG -> (P_W,J,t,volume):    UNBUILT
pure-gauge quotient:               UNTESTED
dynamical flag Euler/Hessian:      UNBUILT
frozen flag:                       NEW CONTINUOUS EXTERNAL SPURION
P1/P2 identification:             REFUTED AS STATED; ONLY FUTURE HOLONOMY MAP
P3:                                UNCHANGED / SEPARATE
```

The current best construction branch is a source-selected compatible flag

\[
(J,\Theta_\chi;t,\Omega_{\mathbb C}),
\]

where the complex-volume/unimodularity field is required to reduce
\(U(3)\times U(2)\) to \(S(U(3)\times U(2))\) rather than leave an extra
\(U(1)\).

## Validation receipt

Passed:

```text
python3 -B tests/channel-swings/rb4_observer_cartan_moving_family_probe.py
python3 -B tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
uv run --with-requirements requirements.txt python -B tests/big-swing/vg_v3_j_commutant_conformal_native.py
uv run --with-requirements requirements.txt python -B tests/W240_z2even_compact_image_nogo.py
uv run --with-requirements requirements.txt python -B tests/W243_charged_corridor_closure.py
git diff --check
```

The direct system Python lacked SciPy for the last three inherited probes;
they pass in the repository dependency environment. This is an environment
receipt, not a scientific discrepancy.

## Final boundary

```text
MOVING-u-CARTAN FAMILY:                  CONSTRUCTED
MOVING CLIFFORD/VOLUMES/Phi:             CONSTRUCTED FINITELY
FULL INTERNAL moving-t FAMILY:           CONDITIONAL ON EXPLICIT SPURION
OBSERVER-ONLY COMPLEX STRUCTURE:         REFUTED
COMPATIBLE COMPLEX--CARTAN FLAG:         TYPED / UNSELECTED
epsilon_IG FLAG OWNERSHIP:               OPEN
FLAG EULER/NOETHER/HESSIAN:              OPEN
SM DETERMINANT-ONE/EXTRA-U1 GATE:        OPEN
EXTERNAL DATUM LEDGER:                   UNCHANGED PENDING OWNERSHIP TEST
```
