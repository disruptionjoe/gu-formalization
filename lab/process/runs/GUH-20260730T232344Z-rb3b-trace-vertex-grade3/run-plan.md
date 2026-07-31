---
run_id: GUH-20260730T232344Z-rb3b-trace-vertex-grade3
status: completed
repository: gu-formalization
workflow: direct-chat-three-track-construction-swing
mode: execute
lane_id: "1"
work_item: RB3B-TRACE-REVERSED-BIDOUBLET-FULL20-JOIN
starting_revision: 8f1a332edaf6
opened_at: 2026-07-30T23:23:44Z
completed_at: 2026-07-31T00:18:09Z
write_boundary:
  - NEXT-STEPS.md
  - explorations/README.md
  - explorations/rb3-moving-soldering-spinzero-placement-2026-07-30.md
  - explorations/rb1b-native-bosonic-shiab-reopener-2026-07-30.md
  - explorations/rb3b-trace-reversed-bidoublet-full20-join-2026-07-30.md
  - explorations/rb3c-curvature-vertex-full20-green-join-2026-07-30.md
  - explorations/rb1c-native-grade3-curvature-admission-2026-07-30.md
  - tests/README.md
  - tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
  - tests/channel-swings/rb3c_curvature_vertex_full20_green_probe.py
  - tests/channel-swings/rb1c_native_grade3_curvature_probe.py
  - lab/process/runs/GUH-20260730T232344Z-rb3b-trace-vertex-grade3/run-plan.md
claim_status_change: none
canon_change: none
public_posture_change: none
---

# RB3b trace-reversed fixed-Cartan/full-20 join, curvature vertex, and grade-three source test

## Objective

Continue the source-action/external-datum construction at the first objects
exposed by RB3. This run must build or kill concrete maps rather than return
`SOURCE ACTION NEEDED` or `EXTERNAL DATUM NEEDED`.

The main track will:

1. execute the defining representation
   \(\rho_S:\mathfrak{sp}(32,32;\mathbb H)\hookrightarrow
   \operatorname{End}_{\mathbb H}(S)\);
2. use the actual trace-reversed
   \(\operatorname{Sym}^2T^*X\) fibre to construct the smallest native
   Pati--Salam-bidoublet candidate for \(\Phi_{\rm tr}\);
3. form
   \(A_S=c(\tau)\rho_S(\Phi_{\rm tr})\), test the separate \(K,C_+,C_-\)
   bilinear channels, and lift it canonically to
   \(S\oplus V\otimes S\);
4. resolve the lift through \(S/\operatorname{im}\Gamma/\ker\Gamma\) and the
   twenty existing thin slots at finite-matrix grade; and
5. send the identical \(\Phi_{\rm tr}\) into the ambient distortion
   quadratic, keeping its section Euler map explicit.

Two parallel construction tracks will:

- repair the dimensional type of the written curvature vertex before
  attempting a literal \(Q_F\)/Green join; and
- execute the full-adjoint grade-three source candidate on Riemann/Bianchi
  and generic-curvature controls, including the trace-line adjacent escape.

## Layer 0 before L1--L7

The following shared names are different objects until the displayed maps
relate them:

| shared name | objects to keep separate |
| --- | --- |
| Frobenius fibre | raw Frobenius \((7,3)\) versus DeWitt/trace-reversed Frobenius \((6,4)\) |
| trace | primal \(h_{\rm tr}=-g/4\), covector \(\tau=\operatorname{tr}_g/4\), and its Frobenius coordinate matrix \(+g^{-1}/4\) |
| \(\rho_S(\Phi_{\rm tr})\) | the canonical defining inclusion versus selection of the field value/subspace \(\Phi_{\rm tr}\) |
| Higgs | a carried Pati--Salam \((1,2,2)\) candidate versus a source-selected low-energy SM Higgs and versus a VEV |
| full-20 lift | an endomorphism of \(S\oplus V\otimes S\), its \(S/I/R\) blocks, and its twenty-slot/provenance placement |
| curvature vertex | the owned \(T_{\rm GT}:S\to R\) versus the written but untyped \(R\to R\) sandwich |
| \(Q_F\) | a conditional density-dual functional versus a literally executed full-20 matrix current |
| grade-three source | generic full-adjoint curvature response versus Levi--Civita/Riemann curvature response |
| scalar | a four-dimensional Lorentz scalar versus a \(\Lambda^0(V_{9,5})\) form carrier |

The active construction uses actual
\(\operatorname{Sym}^2T^*X\), total signature \((9,5)\), native
\(Sp(32,32;\mathbb H)\), right-\(\mathbb H\), indefinite Krein pairing,
the gamma-traceless full-20 carrier, and the Cartan/maximal-compact
\(6+4\) internal split. Raw Frobenius \((10,4)\), exterior-ten, \(U(128)\),
positive-Hilbert, and fixed-plane generic-full-\(Sp\) objects are hostile
comparators.

## Pre-registered expected verdict

Before executable calculation:

- \(\rho_S\) should prove canonical; the earlier `MISSING-FIRST-FACTOR`
  wording should move to the selection of a physical
  \(\Phi_{\rm tr}\) subspace/value.
- Trace reversal should be load-bearing: it should make the trace line
  negative, produce the internal \(6+4\) split, and fix the native
  \(q=5\) Hodge signs. A probe in which the raw Frobenius comparator is
  invisible is powerless and must be aborted.
- The two native internal form copies
  \(\Lambda^3W\) and
  \(\operatorname{vol}_6\wedge W\), \(W\simeq(1,2,2)\), should admit a
  trace-relative Krein-real combination. Isotropy may reduce a continuous
  relative coefficient to a discrete sign; this is an expectation, not a
  target inserted into the calculation.
- The resulting \(A_S\) should be right-\(\mathbb H\)-linear and
  \(K\)-self-adjoint. At most one of the two charge-conjugation branches is
  expected to have the required Grassmann transpose class.
- The canonical lift
  \(A_{20}=A_S\oplus(1_V\otimes A_S)\) should be an honest full-carrier
  endomorphism, but provenance \(Y_K/Y_C\) and a complete low-energy SM
  selector may remain separate downstream choices.
- The owned curvature map should type as \(S\to R\), forcing an
  \(S\leftrightarrow R\) Krein-polarized lift before literal \(Q_F\).
- The raw grade-three curvature source should be nonzero generically but
  vanish on torsion-free Riemann curvature by Bianchi identities. A
  trace-line adapter may reopen a smaller-stabilizer response but is not
  expected to satisfy the RB2 cyclic identity without further structure.

## Kill, block, and go conditions

Kill only the affected trace-placement branch if:

- trace reversal fails to distinguish the physical and planted Frobenius
  geometries linearly and by signature/Hodge sign;
- the candidate \(\Phi_{\rm tr}\) is not native Krein-skew or
  right-\(\mathbb H\)-linear;
- the four candidate components lose rank, fail their carried
  Pati--Salam type, or require a separately fitted matrix per component;
- \(A_S\) fails every physical \(K/C\) bilinear channel;
- the canonical full-carrier lift fails \(\Gamma,j,P_R\) decomposition or
  corrected-coflip covariance; or
- the same \(\Phi_{\rm tr}\) cannot enter both the fermion insertion and
  the ambient distortion response with one declared normalization.

Block, rather than kill, complete SM recovery if the surviving bidoublet is
only carried by the already-known Pati--Salam host and no target-free
low-energy selector is emitted.

Kill the literal curvature-current branch if no \(S\leftrightarrow R\)
full-20 lift passes native reality, right-\(\mathbb H\), gamma-trace, and
moving-covariance tests. Until that lift exists, keep the RB1
\(Q_F/J_F\)/Green formulas explicitly conditional.

Kill the grade-three source candidate on the Levi--Civita/Riemann stratum if
Bianchi makes its projected output zero. Do not transfer that kill to
generic non-Riemannian full-adjoint curvature or to a trace-adapted smaller
stabilizer without testing them separately. RB1 re-entry additionally
requires the cyclic/transgression derivative identity.

## Preregistered controls

Require rejection or exact adverse disposition of:

- raw Frobenius fibre \((7,3)\) and total \((10,4)\);
- naive identification \(h_{\rm tr}\equiv\tau\);
- a quadratic-only test that squares away the trace sign;
- exterior \(\Lambda^2\oplus\Lambda^3\) ten;
- generic complex non-right-\(\mathbb H\) \(\Phi\);
- \(U(128)\) or positive-Hilbert substitution;
- arbitrary matrices fitted independently to the four components or five
  physics legs;
- a non-isotropic relative bidoublet coefficient;
- \(C_+=C_-\) transpose collapse;
- pairing-only rather than Gamma-natural coflip;
- a same-rank nonintertwining \(P_0\);
- extending the three-copy provenance matrix silently to the eight \(X\)
  slots;
- treating ambient Pati--Salam containment as a complete SM selector;
- inserting a VEV, mass, \(R/4\), cosmological value, index, or count;
- the dimensionally invalid \(P_R T_{\rm GT}P_R\) sandwich;
- wrong \(1/6\) gamma-trace coefficient;
- dropped \(P_R,V_b,K_E\), density, formal-adjoint, or boundary response;
- raw Frobenius Hodge signs in the Green map;
- a generic-curvature grade-three success promoted to Riemann curvature;
  and
- covariance promoted to the stronger cyclic/transgression identity.

## Held out

This run does not insert or solve for a VEV, select numerical Yukawa values,
derive the full Standard Model quotient or spectrum, prove stationarity,
construct a stabilizing quartic, close the nonlinear CME, prove a common
global domain, compute an anomaly or Fredholm index, infer a generation
count, or predict a cosmological constant.

## Planned outputs

- `explorations/rb3b-trace-reversed-bidoublet-full20-join-2026-07-30.md`;
- `tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py`;
- `explorations/rb3c-curvature-vertex-full20-green-join-2026-07-30.md`;
- `tests/channel-swings/rb3c_curvature_vertex_full20_green_probe.py`;
- `explorations/rb1c-native-grade3-curvature-admission-2026-07-30.md`;
- `tests/channel-swings/rb1c_native_grade3_curvature_probe.py`;
- appended corrections to the RB3/RB1b owners; and
- navigation, next-step, validation, and completion records.

## Execution result

### RB3b trace-relative vertex

The fixed-frame trace-reversed algebra passed every preregistered native and
hostile numerical control. A subsequent Layer-0 check narrowed the object
constructed.

- Raw Frobenius gives fibre signature \((7,3)\); DeWitt gives \((6,4)\).
  The trace line changes from positive to negative, and the total signature
  changes from \((10,4)\) to \((9,5)\).
- Trace reversal fixes the signature class and negative trace line but does
  not select the displayed \(A_6\oplus W_4\) maximal-compact split. The
  finite formula is conditional on an observer/Cartan reduction \(\chi\).
  Rotations preserve the chosen split; all three induced boosts mix it, and
  a finite rapidity-\(0.37\) boost moves the \(W_4\) projector by
  \(1.940205721\).
- The defining \(\rho_S\) is the canonical inclusion. The placement gap
  moves to selection/retention of the physical adjoint field subspace.
- The trace-relative two-copy ansatz has one four-dimensional image.
  \(\lambda=\pm1\) are related by the planted domain reflection
  \(\operatorname{diag}(1,-1,-1,-1)\); whether this is a physical
  orientation or a field redefinition is unresolved. \(\lambda=2\)
  retains the image but has Hilbert--Schmidt Gram ratio \(1:4:4:4\).
- At fixed \(t\), the image closes under its Spin(3) stabilizer with zero
  leakage. Each of the three Spin(4) generators that moves \(t\) leaks from
  the image span by \(5.656854249\). A moving-\(\chi,t\) family is required
  before a \((2,2)\) claim.
- The scalar and pseudoscalar copies are independent. Every tested component
  is right-\(\mathbb H\), Krein-skew before trace insertion, Krein-self after
  it, commutes with the frozen first-four spin generators, and is physically
  cross-chirality after the Krein pairing. \(C_+M\) is alternating;
  \(C_-M\) is symmetric.
- The canonical full-20 lift closes all twenty witnesses with maximum
  residual \(8.55\times10^{-16}\), resolves \(I/R\) with maximum projector
  defect \(4.44\times10^{-16}\), and genuinely mixes those sectors.
- Every scalar and pseudoscalar component has exactly the supported ordered
  blocks
  \(4_{SS}+4_{II}+8_{IR}+8_{RI}+20_{RR}=44\), with a minimum nonzero block
  norm \(0.8081\) versus maximum classified-zero norm
  \(9.675\times10^{-16}\). \(P_0\) cell ceilings are \(44/4/4/20\) for
  \(1/P_S/P_I/P_R\).
- The corrected Gamma-natural coflip has slot leakage
  \(9.37\times10^{-15}\), while the pairing-only plant leaks by \(5.11\).
  It makes the zero-order scalar vertex even and the pseudoscalar companion
  odd but supplies no parity/CP selection.

Disposition:

```text
FIXED-CARTAN-FOUR-COMPONENT/FULL20: CONSTRUCTED CONDITIONALLY
OBSERVER-CARTAN/MOVING-SPIN4: REQUIRED / UNBUILT
COMPLETE-SM-SELECTOR/RETAINED-MODE/VEV/STABILIZATION: OPEN
```

### RB3c typed curvature completion and finite amplitude/Green fixture

Layer 0 found that the W125/N4a map has shape \(1792\times128\):

\[
T_b:S\longrightarrow R.
\]

The written right-\(P_R\) sandwich is therefore dimensionally invalid.
Closing \(T_b\) with its Krein reverse constructs one right-\(\mathbb H\),
\(K\)-self-adjoint \(S\leftrightarrow R\) full-20 completion. It has rank
\(256\) and kernel dimension \(1664\). The separately selected diagonal
\(G_2\)-plus-\(R\) pairing has full signature \((960,960)\); nondegeneracy
belongs to that pairing, not to the completion. Neither this choice nor
\(\lambda_F\) is selected.

The finite amplitude/Green fixture passes:

```text
unique gamma-trace coefficient                 -1/6
wrong-coefficient gamma leak                    11.313708
A0 connection finite-difference defect          2.52e-11
one matrix amplitude q(0)                       0.007437949
moving-amplitude derivative                    -0.006808802
finite planted comparator derivative            0.022717673
analytic connection + amplitude response        0.022717673
frozen-amplitude response                      -0.006333215
planted endpoint contribution                   0.040852811
```

The native DeWitt Hodge signs pass as an independent compatibility control
and are not used in the polynomial Green calculation. One finite compact
\(SO(3)\) connection derivative passes, and one matrix-derived scalar
amplitude is joined to a planted abelianized one-dimensional
\(1/12/13\)-degree Green/chain-rule profile. Its connection,
moving-amplitude, and endpoint terms are separately load-bearing. The probe
does not construct the full \(Q_F\) 12-form, \(D_A^{\rm coad}Q_F\), a
native \(Y^{14}\) formal-adjoint/domain/boundary problem, a common
\(\epsilon_{\rm IG}\) mover, density variation, or the physical W125 field
embedding.

Disposition:

```text
TYPED-S<->R-COMPLETION: CONSTRUCTED / RANK 256 / KERNEL 1664
ONE-Q_F-AMPLITUDE/FINITE-1D-GREEN-FIXTURE: CONSTRUCTED
FULL-Q_F/D_A-CURRENT/NATIVE-GREEN/COMMON-EPSILON: OPEN
G2/lambda_F/CONNECTION-BRANCH/JD-VS-TOTAL-SELECTION: OPEN
```

### RB1c grade-three admission

Trace reversal again fires as a hostile control. The native grade-three map
is nonzero on generic non-Riemannian curvature, with norm \(25.2982\).
Independent scalar, traceless-Ricci, and Weyl fixtures verify the pointwise
Clifford/Bianchi reduction and exhaust the algebraic-Riemann representation
with dimensions \(1+104+3080=3185\). The projected first, second, and full
grade-three sources vanish on every irrep. Powered raw controls remain
nonzero; the scalar raw norm is \(82.2679\). The trace-line adapter reopens
the scalar fixture with norm \(78.2304\).

Neither linear source clears the RB2 cyclic gate. The six deterministic
seeded full-adjoint gaps are order one, the four-ordering repair family has
sampled rank four, and the least-singular training combination fails the
ordering-fit held-out fixture. The restricted grade-\(2/3\) first pass is
corrected explicitly: its tiny gaps did not support the earlier failure
label, and its apparent
\((1,1,1,1)\) null relation fails held out.

Canonical symmetric polarization is nonzero, native-covariant, and
derivative-correct in one finite moving-data homogeneous proxy, but a
planted zero-polarized-curvature pair produces a nonzero Euler covector. It
is therefore a different two-input Euler-covector geometry rather than one
linear curvature-source map in the tested fixture.

Disposition:

```text
GENERIC-NON-RIEMANNIAN-GRADE3: LIVE
ALL-ALGEBRAIC-RIEMANN-IRREPS: PROJECTED SOURCE ZERO
TRACE-LINE-LINEAR-REOPENER: CYCLIC GATE FAILED
POLARIZATION: DIFFERENT TWO-INPUT EULER-COVECTOR GEOMETRY
```

## Correction log

1. The preregistered expectation that isotropy might leave “two branches”
   is narrowed: the two signs parameterize one image and are related by a
   planted domain reflection; its physical quotient is unresolved. The
   \(\lambda=2\) plant is rejected only as an isometric soldering
   normalization, not as a distinct image.
2. The normalized trace Clifford insertion and the geometric covector
   normalization are kept separate; the finite bilinear probe uses the unit
   negative trace gamma while the action restores the geometric factor.
3. The fixed-\(P_R\) covariance phrase is rejected. The full-20 zero-order
   lift may mix \(I/R\); simultaneous moving-frame covariance and exact slot
   closure are the correct tests.
4. The W125/N4a vertex is rectangular, so the formerly written right
   projector cannot compose. The constructed off-diagonal Krein completion
   replaces, rather than rationalizes, that expression. It is rank \(256\)
   with kernel \(1664\); nondegeneracy belongs to the chosen pairing.
5. An early restricted grade-\(2/3\) fixture was degenerate enough to
   produce tiny cyclic gaps and a training null. The saved probe reports
   that near-pass honestly and uses deterministic seeded full-adjoint
   fixtures plus an ordering-fit held-out fixture for the supported failure.
6. A derivative-correct polarization is not promoted to the original linear
   source map because the planted algebraic factorization control fails; its
   surviving object is a two-input Euler covector.
7. Passing finite controls did not establish that the right object had been
   asked about. Trace reversal supplies the signature and trace line, not
   the Cartan split. Layer 0 therefore narrows RB3b to a fixed-Cartan
   construction conditional on an unbuilt observer/Cartan reduction.
8. One matrix amplitude plus a finite/planted one-dimensional Green fixture
   is not the full \(Q_F\), a physical current, or a native \(Y^{14}\)
   Green problem. Those remain construction targets.

## Validation

Direct construction probes:

```text
python3 tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py PASS
python3 tests/channel-swings/rb3c_curvature_vertex_full20_green_probe.py   PASS
python3 -B tests/channel-swings/rb1c_native_grade3_curvature_probe.py      PASS
```

Preserved-leg regressions:

```text
rb3_moving_soldering_spinzero_probe.py       PASS
rb1b_native_bosonic_shiab_probe.py           PASS
rb2_source_action_exactness_probe.py         PASS
rb1_source_repo_current_musical_probe.py     PASS
full20_dewitt_loop_transport_probe.py        PASS
actual_sym2_c14_orbit_probe.py               PASS
unified_source_variation_probe.py            PASS
unified_source_datum_packet_v0_probe.py      PASS
```

Process and hygiene gates:

```text
explorations_readme_surface_map_audit.py      PASS
tests_manifest_count_audit.py                 PASS
next_steps_frontdoor_guard_audit.py           PASS
changed_public_path_hygiene_audit.py          PASS
research_posture_audit.py                     PASS
git diff --check                              PASS
```

No claim, canon, or public-posture status changes are made by this run.
