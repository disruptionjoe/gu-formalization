---
title: "Spectral Section Carrier Goal"
date: 2026-06-30
status: complete
claim_grade: bounded_negative
claim_promotion: false
depends_on:
  - COMPENSATOR-ADAPTER-GOAL-2026-06-30.md
  - ../temporal-issuance/explorations/E097-clock-free-cadence-absorber-gauntlet-2026-06-30.md
  - lib/spectral_section_carrier.py
  - tests/test_spectral_section_carrier.py
---

# Spectral Section Carrier Goal

## Goal

Test whether the missing GU source-action adapter can be a boundary spectral
section rather than a local compensator matrix.

The object under test is the existing boundary operator:

```text
E = (I - Pi_RS) M_D Pi_RS
D_Sigma = E + E^dag
```

The target question is:

```text
Can a spectral section of D_Sigma produce a nonzero asymmetry/index carrier
while preserving the verified GU anchors and avoiding clean RS decoupling?
```

## Temporal-Issuance Warning Imported

The newest temporal-issuance exploration, `E097`, is relevant as a discipline
constraint. It showed that clock-free record coherence can look meaningful but
still be fully absorbed by fixed-site sheaf compatibility, database constraint
checking, fixed-H record update, and fixed latent source plus changing access.

The GU translation is:

```text
A spectral section is not source-side just because it selects modes.
If all it does is choose a fixed zero-mode projector, it is a fixed-H or fixed
compatibility absorber, not a source-action carrier.
```

Therefore this discriminator separates:

- nonzero spectral asymmetry in the nonzero boundary spectrum;
- fixed zero-mode filling conventions;
- clean decoupling of the RS escape channel.

## Method

For each section rule, compute:

```text
selected_rank
positive_selected
negative_selected
zero_selected
nonzero_eta = positive_selected - negative_unselected
zero_mode_balance
section_balance
||[P_section, D_Sigma]||
escape_ratio = ||Q M_D Pi_RS|| / ||Q M_D Pi_RS||
```

The strict promotion gate is:

```text
nonzero_eta != 0
anchors preserved
escape_ratio not decoupled
not merely a zero-mode convention
```

## Candidate Sections

| candidate | shape | role |
|---|---|---|
| `strict_positive_aps` | strictly positive spectral projection | canonical APS baseline |
| `nonnegative_zero_fill` | positive spectrum plus all zero modes | fixed-H absorber probe |
| `rs_weighted_zero_fill` | positive spectrum plus zero modes with dominant `Pi_RS` weight | fixed RS-projector probe |
| `normal_weighted_zero_fill` | positive spectrum plus zero modes with dominant `Q` weight | fixed normal-projector probe |
| `eta_weighted_zero_fill` | positive spectrum plus positive `(9,5)` eta-weighted zero modes | fixed signature-rule probe |

## Results

Run:

```powershell
python -m unittest tests.test_spectral_section_carrier -v
```

Concrete discriminator table:

| candidate | rank | pos selected | neg selected | zero selected | nonzero eta | zero balance | status |
|---|---:|---:|---:|---:|---:|---:|---|
| `strict_positive_aps` | 128 | 128 | 0 | 0 | 0 | -1536 | `symmetric_section_zero` |
| `nonnegative_zero_fill` | 1664 | 128 | 0 | 1536 | 0 | 1536 | `zero_mode_choice_absorbed` |
| `rs_weighted_zero_fill` | 1664 | 128 | 0 | 1536 | 0 | 1536 | `zero_mode_choice_absorbed` |
| `normal_weighted_zero_fill` | 128 | 128 | 0 | 0 | 0 | -1536 | `symmetric_section_zero` |
| `eta_weighted_zero_fill` | 1359 | 128 | 0 | 1231 | 0 | 926 | `zero_mode_choice_absorbed` |

Boundary spectrum:

```yaml
D_Sigma_positive_count: 128
D_Sigma_negative_count: 128
D_Sigma_zero_count: 1536
D_Sigma_eta: 0
anticomm_norm_for_G_D_plus_D_G: 5.474e-14
```

Aggregate verdict:

```text
only_symmetric_or_fixed_zero_mode_sections
```

## Plain-English Reading

If this works, it would be a more serious adapter than the compensator attempt.
A spectral section is a boundary choice about which modes count as outgoing,
incoming, protected, or rejected. That is closer to the desired "adapter" role
than another local perturbation.

But the temporal-issuance absorber result raises the bar. A fixed projector is
not enough. The section has to do more than choose a pre-existing compatible
subspace; otherwise it is just the GU analogue of fixed sheaf/database/fixed-H
record filtering.

## Verdict

This goal does not find a live spectral-section carrier.

The strict positive APS section is perfectly symmetric on the nonzero spectrum:

```text
#positive = #negative = 128
eta = 0
```

That is not an accident. The grading

```text
G = Pi_RS - Q
```

anticommutes with `D_Sigma` to numerical precision:

```text
||G D_Sigma + D_Sigma G|| = 5.474e-14
```

so every positive boundary mode is paired with a negative one.

The only way these first-pass section rules create large balances is by choosing
some or all of the 1536 zero modes. That does not count as a source-action
carrier in this discriminator. It is the GU analogue of the temporal-issuance
`E097` absorber: a fixed compatibility/projector/fixed-H rule can reproduce the
surface behavior without adding source-side issuance.

Plainly:

```text
the nonzero boundary spectrum has no asymmetry;
zero-mode filling can create bookkeeping asymmetry;
bookkeeping asymmetry is absorbed by fixed projector/fixed-H explanations.
```

The spectral-section route is still not dead in the strongest possible form,
but the next version cannot be "choose a static section of the current
D_Sigma." It would need a nonfixed admissibility datum: a section that changes
under a source-current law, a BV/BRST boundary field, a K-class not reducible to
a fixed projector, or an anomaly/flow equation that forces a section rather than
chooses one.

## Not Claimed

This goal does not claim:

- a source action exists;
- a spectral section is physical;
- zero-mode filling is source-side issuance;
- observer-side reconstruction choices are enough to close GU.
