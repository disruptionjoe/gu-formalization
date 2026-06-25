---
title: "Finite-Control Provenance Audit"
date: "2026-06-24"
status: exploration
doc_type: finite_control_provenance_audit
verdict: "NO_SELECTOR_SUCCEEDS; FIRST_FORBIDDEN_TARGET_A_F; PARTIAL_DERIVE_HOST_IMPORT_FAIL"
owner: "Codex"
depends_on:
  - "explorations/all-persona-wall-break-steelman-hegelian-2026-06-24.md"
  - "explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/goal-draft-type-ii1-fixed-data-selector-challenge-2026-06-24.md"
  - "explorations/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
  - "specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
  - "explorations/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/pc5-higgs-emergence-spec-2026-06-23.md"
  - "explorations/pc5-higgs-cas-clebsch-gordan-2026-06-23.md"
  - "explorations/pc5-higgs-su2l-u1y-gate-2026-06-23.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Finite-Control Provenance Audit

## 1. Verdict

**Verdict: no current selector succeeds.**

The current state is not an SM/Higgs derivation. It is a mixed provenance state:

```text
GU carrier and Pati-Salam one-generation branching: derived, but relative to a branch frame.
Finite Connes algebra and SM global gauge group: imported or failed as target-free outputs.
Type II_1 selector lane: failed for instantiated selectors; fixed-data rigidity remains open but empty.
Higgs quantum numbers: hosted by ambient adjoint branching; physical scalar and potential remain open.
Anomaly result: derived only for the ordinary SM shadow; the full GU/Type II_1 shadow remains open.
```

The first theorem-blocking datum is:

```text
A_F = C + H + M_3(C)
```

No allowed operation in the current GU or Type II_1 tables produces this finite algebra.
If a route intentionally bypasses the finite Connes algebra, the first gauge-specific
failure is the global SM quotient:

```text
G_SM = SU(3) x SU(2) x U(1) / Z_6.
```

This audit therefore preserves the previous ledger's posture but makes the target
lineage stricter: a datum does not count as derived if its proof trace passes through a
forbidden target table.

Status words in this file mean:

| status | meaning |
|---|---|
| derived | Computed from allowed inputs by a named operation, without using the datum as input. Relative derivations name their upstream condition. |
| hosted | The ambient structure contains a representation slot or embedding, but no selector chooses it as the physical datum. |
| imported | The datum is supplied as an external finite CC, SM, Pati-Salam-breaking, or phenomenological input. It may be used only with that label. |
| failed | The attempted selector either needs a forbidden target input or passes the replacement-family test. |
| open | A precise candidate exists, but a named proof object or computation is missing. |

## 2. Allowed Inputs And Forbidden Target Inputs

### Allowed Input Tables

| table | allowed rows | why allowed |
|---|---|---|
| `GU-CARRIER` | `Cl(9,5) ~= M_64(H)`, `S = H^64`, ambient `Sp(64)`, fiber `Spin(6,4)`, section data `theta` and `II_s^H` | These are typed carrier or geometric inputs from the GU side, not SM target data. |
| `REP-BRANCH` | Maximal compact `Spin(6) x Spin(4)`, Pati-Salam branching of `S(6,4)`, Clebsch-Gordan rules, `adj(Sp(16)) ~= Sym^2(C^16)` | Standard representation theory may be used to compute consequences of an already specified carrier. |
| `TYPEII1-CONTROLS` | Fixed `(N subset M, tau, A, H, D, J, gamma, Phi_CC)` only when justified by Type II_1 spectral-SM requirements rather than targets | These are selector-candidate controls. They are not enough by themselves to select finite CC data. |
| `TYPEII1-REQUIREMENTS` | Semifinite spectral triple axioms, KO-6 sign package, order-zero/order-one, tau-compactness, Breuer-Fredholm or cyclic-cohomology constraints, standard-invariant data, anomaly-safe shadow checks | These are filters. They may reject candidates but do not become SM data by assertion. |
| `ANOMALY-FORMULAS` | Perturbative SM anomaly sums and Freed-Hopkins-style compatibility tests applied after an observer-facing shadow is specified | These formulas can verify a computed packet; they cannot supply the packet. |
| `CLAIM-DAG` | Status discipline, forbidden-input discipline, closure/demotion conditions | Governance prevents overclaim. It is not evidence for a physics datum. |

### Allowed Operations

| operation id | operation | valid output class |
|---|---|---|
| `CL-CARRIER` | Build the quaternionic Clifford carrier and ambient `Sp(64)` module. | Carrier data only. |
| `MAXCOMPACT` | Restrict `Spin(6,4)` to `Spin(6) x Spin(4) ~= SU(4) x SU(2)_L x SU(2)_R`. | Pati-Salam branch frame, not low-energy gauge selection. |
| `PS-SPINOR-BRANCH` | Branch `S(6,4)=C^16` to `(4,2,1) + (4bar,1,2)`. | One-generation Pati-Salam packet. |
| `PS2SM-BRANCH` | After a Pati-Salam-to-SM embedding is supplied, compute `Y = T_3^R + (B-L)/2` and the SM charges. | Relative SM charge packet and relative hypercharge. |
| `SP-ADJ-CG` | Decompose `adj(Sp(16)) ~= Sym^2(C^16)` under Pati-Salam and then SM. | Ambient Higgs-representation slots. |
| `CC-FIXED-DATA-ATTACH` | Attach finite Connes-Chamseddine data into a hyperfinite or semifinite host. | Imported/hosted finite CC lane only. |
| `TYPEII1-TRACE-SPLIT` | Split a II_1 projection into equal-trace subprojections. | Fails as generation selector because arbitrary `n` works. |
| `CN-FOURIER` | Use `C_n` crossed-product Fourier idempotents. | Fails as generation selector because it transports chosen `n`. |
| `C3D4-ARM-READOUT` | Read three arms or order-3 labels from C3/D4-style examples. | Fails unless fixed data force the object and block `n != 3`. |
| `CONNES-SHADOW` | Map Type II_1/GU data to finite CC observer-facing data. | Open unless functorial and target-free. |
| `SECTION-PROJECTION` | Compute `pr_(1,2,+1/2)(II_s^H)` or the fiber component of `theta` on a specified critical section. | Open physical Higgs selector. |
| `EFFECTIVE-POTENTIAL` | Derive Higgs mass and quartic terms from the written GU action or spectral-action analog. | Open electroweak-symmetry-breaking gate. |

### Forbidden Target Inputs

| forbidden target input | forbidden when used to prove | why forbidden |
|---|---|---|
| `A_F = C + H + M_3(C)` | finite algebra selection, SM gauge group selection, Higgs as CC inner fluctuation | This is the finite CC target algebra. Supplying it is hosting/import, not derivation. |
| finite CC tuple `(A_F, H_F, D_F, J_F, gamma_F)` | one-generation module, SM inner fluctuations, anomaly-safe shadow | It already contains the finite-control answer. |
| `G_SM = SU(3) x SU(2) x U(1) / Z_6` | gauge-group emergence, central quotient, hypercharge normalization | Naming the observer gauge group bypasses the selector. |
| central quotient `Z_6` | global SM group derivation | The local Lie-algebra branch does not determine the global quotient without a separate lattice/kernel theorem. |
| absolute hypercharge embedding as target | hypercharge selection | `Y = T_3^R + (B-L)/2` is allowed only after the Pati-Salam-to-SM embedding is independently supplied or selected. |
| one-generation finite module `K_SM` | `T_1` or Connes-channel output | External attachment of the already known SM packet is not a selector. |
| `n = 3`, `C3`, index-3 inclusion, D4 triple arm, three projections, `dim H_F = 96` | generation-count selection | These visible-three inputs transport the target count. |
| physical Higgs doublet, nonzero Higgs projection, Mexican-hat potential, negative mass squared | Higgs emergence | Ambient quantum numbers are not the physical scalar or its dynamics. |
| ordinary anomaly-free SM shadow | anomaly compatibility | Anomaly cancellation may verify a computed shadow, but cannot supply the shadow or erase extra modes. |

## 3. Provenance Ledger Table

| datum | status | introduced-by operation | why-provenance | missing proof object |
|---|---|---|---|---|
| Typed GU carrier `Cl(9,5) ~= M_64(H)`, `S = H^64`, ambient `Sp(64)` | derived | `CL-CARRIER` | The Clifford/quaternionic module produces the large carrier without SM target data. This derives the host, not the finite-control package. | No missing proof for the carrier row; missing downstream selector from this carrier to finite-control data. |
| Pati-Salam branch frame `SU(4) x SU(2)_L x SU(2)_R` | derived | `MAXCOMPACT` | The maximal compact of `Spin(6,4)` is `Spin(6) x Spin(4) ~= SU(4) x SU(2) x SU(2)`. This is a branch frame, not yet a selected low-energy gauge group. | Physical gauge-selection theorem saying why this branch frame is the observer gauge group rather than a useful decomposition frame. |
| Finite Connes algebra `A_F = C + H + M_3(C)` | imported | `CC-FIXED-DATA-ATTACH` | Every current positive Type II_1 lane starts only after the finite algebra is supplied. No allowed `GU-CARRIER` or fixed-data Type II_1 operation outputs this algebra. | Target-free `Phi_CC` or finite-control selector computing `C + H + M_3(C)` without naming it or its summands as input. |
| SM gauge group `SU(3) x SU(2) x U(1) / Z_6` | failed | `CC-FIXED-DATA-ATTACH -> inner fluctuations` or `MAXCOMPACT -> imported Pati-Salam breaking` | Inner fluctuations recover this only after `A_F` is imported; GU branching reaches Pati-Salam but does not select the SM subgroup or global quotient. | Functorial gauge selector from allowed data, including the global kernel that gives `Z_6`. |
| Central quotient `Z_6` | failed | Target global-group import or finite CC unimodularity after `A_F` import | Local Lie algebra branching can suggest `su3 + su2 + u1`, but it does not by itself prove the shared center quotient. | Lattice/kernel theorem deriving the global quotient from GU or target-free finite spectral data. |
| Pati-Salam-to-SM breaking `SU(4) x SU(2)_R -> SU(3) x U(1)_Y` | imported | Standard Pati-Salam breaking assumption | The subgroup chain is standard, but the current GU/Type II_1 data do not provide the breaking field, vacuum, boundary condition, or section selector. | GU/Type II_1 mechanism that selects the breaking and its order without naming the SM target. |
| Hypercharge `Y = T_3^R + (B-L)/2` | derived | `PS2SM-BRANCH` | Once the Pati-Salam-to-SM embedding is supplied, the charge formula and normalization follow by standard branching. The derivation is relative to the imported/selected breaking. | Absolute selector for the `U(1)_Y` embedding and normalization, independent of target SM input. |
| One-generation Pati-Salam packet `(4,2,1) + (4bar,1,2)` | derived | `PS-SPINOR-BRANCH` | `S(6,4)=C^16` branches to the standard Pati-Salam 16-dimensional packet. This is genuine representation provenance from the carrier. | Upstream physical-gauge selector remains missing; the branch packet is not by itself the finite CC module. |
| One-generation SM charge packet with right-handed neutrino | derived | `PS-SPINOR-BRANCH -> PS2SM-BRANCH` | Given the Pati-Salam-to-SM embedding, the usual SM charges follow, including `nu_R(1,1,0)`. | Same upstream selector gap: the packet is relative to a chosen breaking and does not derive `A_F`. |
| Exactly three Type II_1 generation sectors `n = 3` | failed | `TYPEII1-TRACE-SPLIT`, `CN-FOURIER`, `C3D4-ARM-READOUT`, external `K_SM tensor C^3` | Equal-trace, `C_n`, visible-three, and external-attachment selectors all pass the replacement test or import `K_SM`. They transport a chosen count. | Fixed-data rigidity theorem forcing a canonical three-sector orbit, preserving `J`, `gamma`, `D`, order-one, and anomaly shadow, with named obstruction for `n = 2,4`. |
| GU `2 + 1` generation story and exact `n = 3` | open | `CL-CARRIER -> PS-SPINOR-BRANCH` plus RS/index reconstruction | The representation story supports two spin-1/2 sectors plus one RS/imposter sector, but exact multiplicity still needs analytic index closure. | H-linear noncompact or APS index computation proving the RS contribution and total quaternionic index without target normalization. |
| Pati-Salam Higgs bidoublet `(1,2,2)` in `adj(Sp(16))` | derived | `SP-ADJ-CG` | `adj(Sp(16)) ~= Sym^2(C^16)` and `C^16=(4,2,1)+(4bar,1,2)` give one `(1,2,2)` from the cross term. | Machine CAS confirmation would upgrade grade; physical selection remains a separate proof object. |
| SM Higgs doublet quantum-number slot `(1,2,+1/2)` | hosted | `SP-ADJ-CG -> PS2SM-BRANCH` | The ambient adjoint contains the right quantum numbers. At the SM level there is also an additional `(1,2,+1/2)` from the SU(3)-singlet inside `(15,2,2)`, so containment does not select the physical light Higgs. | Projection/disambiguation theorem selecting the light `(1,2,2)` component rather than a heavy or mixed Pati-Salam component. |
| Physical Higgs scalar as a 0-form from `theta` or `II_s^H` | open | `SECTION-PROJECTION` | The fiber-component construction is plausible, but the actual critical section may have zero projection or may lie in the geometric `j_s(N_s)` sector rather than the off-diagonal Higgs block. | Gauge-covariant fiber-component map and nonzero computation of `pr_(1,2,+1/2)(II_s^H)` on a specified GU critical section. |
| Higgs potential and electroweak symmetry breaking | open | `EFFECTIVE-POTENTIAL` | Ambient representation theory does not give a Mexican-hat potential, negative mass squared, quartic coefficient, or Yukawa block. | Effective-potential computation from a written GU action or spectral-action analog, including sign, quartic term, and Pati-Salam breaking. |
| Ordinary one-generation perturbative anomaly cancellation | derived | `ANOMALY-FORMULAS` after `PS2SM-BRANCH` | For the relative ordinary SM charge packet, the standard anomaly sums cancel per generation. This verifies the packet; it does not select the packet. | No missing proof for the ordinary shadow if the observer-facing content is exactly the ordinary SM generation. |
| Full GU/Type II_1 anomaly shadow and Freed-Hopkins compatibility | open | `CONNES-SHADOW -> ANOMALY-FORMULAS` | Compatibility passes only if the observer-facing shadow is exactly ordinary anomaly-free SM content or if all extra surviving modes cancel. Current maps do not prove either. | Functorial Connes-channel shadow proving no extra observer-facing modes, or complete anomaly computation for every surviving mode. |

## 4. First Genuine Forbidden-Input Or Selector Failure

The target-free provenance theorem has the shape:

```text
allowed GU/Type II_1 inputs
  -> allowed selector operations
  -> finite-control package
```

The first failure is `A_F`.

The trace is:

```text
CL-CARRIER
  -> MAXCOMPACT
  -> PS-SPINOR-BRANCH
  -> one Pati-Salam generation branch
  -/-> A_F = C + H + M_3(C)
```

At that point the current proof has no target-free operation that produces the finite
Connes algebra. The only operation that introduces `A_F` is `CC-FIXED-DATA-ATTACH`, and
that is explicitly an import. Any downstream recovery of `G_SM`, central `Z_6`, finite
inner fluctuations, or finite CC anomaly shadow inherits that import unless a new
selector is supplied.

For a GU-only route that declines to pass through `A_F`, the first gauge datum that fails
is:

```text
MAXCOMPACT -/-> SU(3) x SU(2) x U(1) / Z_6.
```

The Pati-Salam branch frame and one-generation charge computation are useful and real,
but they do not select the SM global gauge group. The central quotient is especially
diagnostic because it is not fixed by the local branching calculation alone.

**No current selector succeeds.** Fixed embedded finite CC data host/import the target.
Trace, `C_n`, and C3/D4 selectors fail by replacement. Fixed-data rigidity remains the
only open class, but no instantiated candidate exists in the repo.

## 5. Claim Certificate Table For TYPEII1-SELECTOR, SM-GAUGE, HIGGS, ANOMALY

| certificate | current decision | accepted evidence | forbidden inputs that would void the certificate | closure or demotion condition |
|---|---|---|---|---|
| `TYPEII1-SELECTOR` | `negative_filter`; no positive selector finality | Anti-smuggling theorem, replacement criterion, and host/selector separation | `A_F`, `K_SM`, `C3`, index-3, three arms, three projections, `K_SM tensor C^3` | Upgrade only under fixed-data selector forcing a canonical three-sector or finite-control output and blocking `n = 2,4`; demote candidates that remain cardinality transport. |
| `SM-GAUGE` | target-free derivation failed at `A_F`; direct GU gauge route fails at `G_SM/Z_6` | `MAXCOMPACT` and `PS-SPINOR-BRANCH` for branch frame and relative charges | `A_F`, `G_SM`, central `Z_6`, preselected Pati-Salam breaking field or vacuum | Upgrade only with a functorial gauge selector deriving the algebra/subgroup and global quotient; demote any claim that treats Pati-Salam branching as SM gauge selection. |
| `HIGGS` | necessary-condition pass, physical Higgs open | `SP-ADJ-CG` gives `(1,2,2)` in `adj(Sp(16))`; SM doublet slot is hosted | physical Higgs field, nonzero projection, negative mass squared, preselected light-Higgs component | Upgrade only after a section-specific nonzero projection and effective-potential computation; demote emergence language if projection vanishes or dynamics lacks EWSB. |
| `ANOMALY` | relative ordinary SM shadow passes; full GU/Type II_1 shadow open | Standard anomaly sums after a computed ordinary charge packet | assuming ordinary SM shadow, deleting extra modes by fiat, using anomaly cancellation to select the packet | Upgrade only when `CONNES-SHADOW` proves exactly ordinary anomaly-free content or computes cancellation for all surviving modes; demote if any extra observer-facing mode is anomalous. |

## 6. Branch/Selector Robustness Table

| branch or selector | fixed data? | what it can output | replacement robustness | verdict |
|---|---|---|---|---|
| Fixed-data rigidity selector | Not instantiated | Could in principle select `T_A`, `T_G`, `T_1`, or `T_3` | Unknown until a named `X` and `X_2`, `X_4`, `X_n` audit exist | Open but empty; no current selector success. |
| Trace selector | No target-independent count | Equal-trace equivalent projections | Fails because equal-trace `n`-partitions exist for arbitrary `n` in a diffuse II_1 factor | Failed as selector. |
| `C_n` crossed-product selector | No; `n` is chosen | `n` Fourier idempotents | Fails because the same construction works for `n = 2,3,4,...` | Failed as cardinality transport. |
| C3/D4 visible-three selector | No; three is visible in the input | Three arms, labels, or idempotents | Fails unless an independent theorem forces the object and blocks neighboring replacements | Failed toy control. |
| Imported finite CC host | Fixed only after target import | Hosts `A_F`, `K_SM`, inner fluctuations, ordinary anomaly shadow | Replacing `K_SM tensor C^3` by `K_SM tensor C^n` changes only copied count unless another obstruction appears | Host/import only, not selector. |
| GU carrier only | Yes for carrier; no for low-energy selector | Derives carrier, Pati-Salam branch frame, one-generation packet; hosts Higgs quantum numbers | Does not derive `A_F`, `G_SM/Z_6`, Pati-Salam breaking, exact `n=3`, or physical Higgs dynamics | Partial derive/host with first finite-control failure at `A_F`. |

## 7. Next Meaningful Proof/Computation Step

The next meaningful step is a fixed-data `Phi_CC` computation, not another visible triple
or another ambient representation-containment check.

Minimal target:

```text
Input:
  X = (N subset M, tau, A, H, D, J, gamma, Phi_CC)

Input-independence rule:
  X must not be parameterized by A_F, G_SM, K_SM, n=3, C3, index 3,
  three graph arms, three projections, dim H_F=96, or a target-normalized index.

Computation:
  compute Phi_CC(X)
  list selected data versus imported data
  run X_2, X_4, and X_n replacement checks where available
  run J, gamma, D, order-one, tau-compactness, and anomaly-shadow checks

First binary question:
  Does Phi_CC select A_F or G_SM without forbidden target input?
```

If the answer is no, the finite-control theorem attempt remains:

```text
GU carrier: derived branch data and hosted Higgs slots.
Type II_1: conditional host plus negative selector filter.
SM/Higgs emergence: not derived.
```

If the answer is yes, the next gates are, in order:

1. derive the central quotient `Z_6` and absolute hypercharge normalization;
2. compute `pr_(1,2,+1/2)(II_s^H)` on a specified critical section;
3. derive the Higgs effective potential and Pati-Salam breaking mechanism;
4. run the full anomaly-shadow computation on every observer-facing mode;
5. rerun the replacement audit for any generation-count output.

Until that proof object exists, the decision-grade posture is:

```text
NO_SELECTOR_SUCCEEDS.
FIRST_FORBIDDEN_TARGET_A_F.
CURRENT_STATE = partial derived branch data + host/import/fail/open finite-control data.
```
