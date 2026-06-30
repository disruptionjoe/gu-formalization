---
title: "SM Gauge/Higgs Finite-Control Extraction Ledger"
date: "2026-06-24"
status: exploration
doc_type: finite_control_extraction_ledger
verdict: "PARTIAL_HOST_WITH_SELECTOR_NO_GO"
owner: "Codex"
depends_on:
  - "explorations/cycle-gates-and-audits/goal-draft-type-ii1-fixed-data-selector-challenge-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
  - "lab/specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
  - "lab/specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md"
  - "explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/pc5-higgs-emergence-spec-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/pc5-higgs-cas-clebsch-gordan-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/pc5-higgs-su2l-u1y-gate-2026-06-23.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# SM Gauge/Higgs Finite-Control Extraction Ledger

## 1. Verdict

**Verdict: partial host with selector no-go for current instantiated routes.**

The typed GU carrier can reconstruct substantial representation content:

```text
Cl(9,5) ~= M_64(H), S = H^64,
S(6,4) = C^16 -> (4,2,1) + (4bar,1,2),
Pati-Salam -> one SM generation with the usual hypercharges.
```

It can also host the Higgs quantum numbers in the ambient `sp(16)`/`sp(64)` representation
decomposition. But neither the GU carrier nor any current Type II_1 selector derives the
observer-facing finite-control package:

```text
A_F = C + H + M_3(C),
G_SM = SU(3) x SU(2) x U(1) / Z_6,
the physical Higgs scalar and its potential,
or a full anomaly-safe Connes-channel shadow with no extra modes.
```

The Type II_1 lane remains a conditional host. Its selector lane is negative for all
instantiated classes: fixed embedded CC data import the target, trace and `C_n` selectors
transport a chosen cardinality, and C3/D4 style examples fail the replacement test.

Status words below mean:

- `derive`: computed from the stated typed carrier or fixed input without inserting that
  datum as an argument. If the derivation is relative to a chosen subgroup, the reason says so.
- `host`: the ambient data contain a representation slot or embedding, but no selector
  chooses it as the physical datum.
- `import`: the datum is supplied from finite CC, Pati-Salam, or SM convention.
- `open`: a necessary condition or candidate exists, but a named proof object is missing.
- `fail`: the attempted derivation collapses to host-only, imported data, or cardinality
  transport under the current selector filters.

## 2. Extraction Ledger Table

| datum | status | reason | missing proof object |
|---|---|---|---|
| Typed GU carrier `S = H^64`, `Cl(9,5) ~= M_64(H)`, ambient `Sp(64)` | derive | The quaternionic carrier and ambient `Sp(64)` follow from the typed Clifford module. This derives the large carrier, not the SM finite-control data. | No missing proof for the carrier; missing finite-control selector from `Sp(64)` to the SM package. |
| Finite CC algebra `A_F = C + H + M_3(C)` | import | Current Type II_1 hosting can embed or carry finite CC data only after `A_F` is supplied. No current selector computes this algebra. | Fixed-data selector theorem producing `A_F` from Type II_1/GU data without naming `C`, `H`, or `M_3(C)` in the input. |
| SM gauge quotient `SU(3) x SU(2) x U(1) / Z_6` | fail | GU inner fluctuations preserve the already input `Sp(64)` connection orbit, and Type II_1 inner fluctuations do not currently select the compact SM quotient from the larger unitary structure. This is the first target-level derivation failure. | A functorial `Phi_CC` or inner-fluctuation theorem selecting the SM gauge quotient, including the central `Z_6`, from fixed data. |
| Pati-Salam carrier subgroup `SU(4) x SU(2)_L x SU(2)_R` | derive | From the typed fiber `Spin(6,4)`, the maximal compact is `Spin(6) x Spin(4) ~= SU(4) x SU(2) x SU(2)`. | Physical-selection theorem saying why this subgroup, rather than merely a useful branching frame, is the low-energy gauge group. |
| Pati-Salam to SM breaking | import | The subgroup chain and formula are the standard Pati-Salam route, but the GU/Type II_1 data do not yet provide the breaking field, vacuum, or boundary condition. | GU/Type II_1 mechanism for `SU(4) x SU(2)_R -> SU(3) x U(1)_Y`. |
| Hypercharge normalization `Y = T_3^R + (B-L)/2` | derive | Relative to the imported Pati-Salam breaking, the charges follow by standard branching: `4 -> (3,+1/3) + (1,-1)` and `2_R -> T_3^R = +/-1/2`. | Absolute selector for the `U(1)_Y` embedding and normalization, not just the standard Pati-Salam calculation after the subgroup is chosen. |
| One-generation Pati-Salam packet `(4,2,1) + (4bar,1,2)` | derive | `S(6,4)=C^16` branches to exactly this Pati-Salam spinor packet with the right complex dimension for one generation. | No missing proof for the representation branch; missing upstream gauge-subgroup selector. |
| One-generation SM charge packet, including right-handed neutrino | derive | Under the Pati-Salam-to-SM branch, the packet gives `Q_L(3,2,+1/6)`, `L_L(1,2,-1/2)`, conjugate right-handed quark/lepton singlets, and `nu_R(1,1,0)`. | Same upstream selector gap: the charge packet is derived only after the Pati-Salam/SM embedding is chosen. |
| Exactly three generation sectors from Type II_1 data | fail | Equal trace projections, finite-group `C_n` idempotents, C3/D4 arms, and `K_SM tensor C^n` Connes-channel shadows all transport a chosen `n`. Current instantiated selectors do not derive `n=3`. | Fixed-data rigidity theorem with a canonical three-sector orbit and a named obstruction for `n=2,4`. |
| GU `2+1` generation story | open | The representation story supports two spin-1/2 sectors plus one RS/imposter sector, but the analytic index value and RS multiplicity remain open. | H-linear or KO index computation proving the relevant zero-mode multiplicity, including the RS symbol/index gate. |
| Ambient Higgs bidoublet `(1,2,2)` in `adj(Sp(16))` restricted to `G_PS` | derive | The Clebsch-Gordan decomposition `adj(sp(16)) ~= Sym^2(C^16)`, with `C^16=(4,2,1)+(4bar,1,2)`, contains one `(1,2,2)` from `(4,2,1) tensor (4bar,1,2)`. | Machine CAS confirmation is still useful, but the larger missing object is physical projection, not ambient multiplicity. |
| SM Higgs quantum numbers `(1,2,+1/2)` | host | `(1,2,2)` branches to `(1,2,+1/2) + (1,2,-1/2)`. The ambient representation contains the right quantum numbers, but containment is only a necessary condition. | Section-specific proof that the actual `theta` or `II_s^H` of a GU critical section has nonzero projection onto this block. |
| Physical Higgs scalar as a 0-form from `theta`/`II_s^H` | open | The fiber-component construction is plausible, but gauge covariance and nonzero projection are not proved. The `j_s(N_s)` image may sit in the geometric sector rather than the off-diagonal Higgs block. | Gauge-covariant fiber-component map plus computation of `pr_(1,2,+1/2)(II_s^H)` on a specified critical section. |
| Higgs potential and electroweak symmetry breaking | open | A Mexican-hat potential, negative mass squared, Yukawa block, and Pati-Salam breaking are not derived from the GU action. | Effective potential computation from the written GU action or spectral-action analog, including sign and quartic coefficient. |
| Ordinary one-generation SM anomaly cancellation | derive | Given the derived relative SM charge packet, the standard perturbative anomalies cancel per generation. This is a consequence of the SM content, not an independent Type II_1 selector. | None if the smooth shadow is exactly the ordinary SM generation; otherwise an explicit anomaly calculation is required. |
| Freed-Hopkins/anomaly compatibility of the GU or Type II_1 shadow | open | Compatibility conditionally passes only if the Connes-channel shadow forgets the Type II_1/GU enrichment and lands on exactly ordinary anomaly-free SM content. It fails if extra modes survive with uncanceled anomaly. | Functorial Connes-channel shadow proving either no extra observer-facing modes or a complete anomaly cancellation computation for all surviving modes. |

## 3. First Genuine Derivation Failure

The first genuine target-level failure is:

```text
fixed typed GU / Type II_1 data -/-> SU(3) x SU(2) x U(1) / Z_6.
```

If the dependency chain is expanded one step earlier, the same failure appears as:

```text
fixed typed GU / Type II_1 data -/-> A_F = C + H + M_3(C).
```

This is not a small missing calculation. It is the first place where the extraction stops
being a representation-theoretic decomposition and starts needing a selector.

The typed GU carrier derives a large ambient structure and a useful Pati-Salam branching
frame. It does not select the finite Connes algebra, the SM gauge quotient, or the
Pati-Salam-to-SM breaking. Type II_1 data can host the finite CC package after import, but
the selector filters rule out treating that hosting as a derivation.

Everything downstream inherits this failure:

- Hypercharge is computed correctly only after the Pati-Salam-to-SM embedding is chosen.
- The one-generation packet is a real branch computation, but it is relative to the chosen
  gauge frame.
- Higgs quantum numbers are present in the ambient adjoint, but the physical Higgs field is
  not derived.
- Anomaly cancellation follows for the ordinary SM shadow, but the existence of exactly that
  shadow is not proved.

## 4. Higgs-Specific Conclusion

The Higgs result is a strong necessary-condition pass and a failed emergence claim if stated
too strongly.

What is in hand:

```text
adj(sp(16))|_{SU(4) x SU(2)_L x SU(2)_R}
  = (10,3,1) + 2(6,1,1) + (1,2,2) + (15,2,2) + (10bar,1,3),
```

so the Pati-Salam Higgs bidoublet `(1,2,2)` is present once at the Pati-Salam level. It
branches to the SM doublet and conjugate:

```text
(1,2,2) -> (1,2,+1/2) + (1,2,-1/2).
```

What is not in hand:

- a proof that the actual section-specific distortion has nonzero `(1,2,+1/2)` projection;
- a gauge-covariant construction of the scalar 0-form from the fiber component;
- a disambiguation of the extra SM-level `(1,2,+1/2)` contribution coming from the
  `SU(3)`-singlet inside `(15,2,2)`;
- a Pati-Salam breaking mechanism;
- a Mexican-hat potential with the correct sign and quartic dynamics.

Therefore the Higgs sector is **hosted at the quantum-number level** and **open at the
physical finite-control level**.

## 5. Anomaly Compatibility Conclusion

The anomaly result is conditional in a clean way:

```text
exact ordinary SM shadow -> anomaly compatible;
extra surviving GU/Type II_1 modes -> anomaly check open, and possibly fatal.
```

For the relative one-generation SM packet, ordinary perturbative anomaly cancellation follows:
the `SU(3)^2 U(1)`, `SU(2)^2 U(1)`, `U(1)^3`, and gravitational-`U(1)` sums vanish per
generation. With three identical ordinary generations, this remains true copywise.

But this does not prove the GU/Type II_1 construction is anomaly compatible. The construction
must still prove that the Connes-channel observer shadow contains exactly the ordinary SM
content, or else explicitly compute the anomaly of every additional observer-facing mode.
The Freed-Hopkins compatibility claim is downstream of that shadow theorem.

## 6. What This Means For Standard Model Emergence Claims

The strongest honest claim is:

```text
The typed GU carrier derives a Pati-Salam one-generation representation branch and hosts
the Higgs quantum numbers. Current Type II_1 data provide a conditional hosting lane.
No current route derives the full SM finite-control package.
```

The following stronger claims should not be made from the present data:

- "The SM gauge group is derived."
- "Hypercharge is absolutely selected."
- "The Higgs sector emerges."
- "Type II_1 selects three generations."
- "Anomaly compatibility is proved for the full GU/Type II_1 model."

The live-claim DAG posture is therefore preserved:

```text
TYPEII1-HOST: conditional hosting lane.
TYPEII1-SELECTOR: negative_filter / no positive selector yet.
```

## 7. Next Meaningful Proof/Computation Step

The next meaningful step is not another visible triple or another ambient representation
containment check. It is a selector/shadow computation.

Minimal proof target:

```text
Construct fixed data X = (N subset M, tau, A, H, D, J, gamma, Phi_CC)
not parameterized by A_F, G_SM, K_SM, or n=3,
and compute Phi_CC(X).
```

The computation must answer one binary question first:

```text
Does Phi_CC select A_F or G_SM, or does it import them?
```

If it imports them, the gauge/Higgs emergence claim stays demoted to host/relative-branch
status. If it selects them, the next checks are:

1. prove the central quotient and hypercharge normalization;
2. compute the actual Higgs projection `pr_(1,2,+1/2)(II_s^H)` on a specified critical section;
3. run the anomaly/Freed-Hopkins shadow check;
4. run the `n=2,4` replacement audit for any generation-sector claim.

Until that selector/shadow computation exists, the finite-control extraction succeeds only
as a partial host and relative representation ledger, not as a Standard Model derivation.
