---
artifact_type: exploration
status: exploration
created: 2026-07-04
title: "Base-sign selector audit: g -> -g is invisible to observerse fiber, shiab contraction, and RS anchors"
grade: "exploration / bounded finite audit"
depends_on:
  - explorations/big-swing-2026-07-03/BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md
  - tests/generation-sector/base_sign_selector_audit.py
---

# Base-Sign Selector Audit

## Question

The `(9,5)` vs `(7,7)` decide-tournament left one cheap follow-up: test whether
the base metric convention `g -> -g` is detected by the three GU-native proxy
surfaces named in the run notes:

- observerse tautological metric / trace-reversed fiber form
- canon shiab contraction channel
- RS constraint bridge anchors

This audit asks whether those finite proxies contain a base-sign selector. It
does not prove that no future GU selector can exist.

## Method

Added and ran:

```text
python tests/generation-sector/base_sign_selector_audit.py
```

The script compares the mostly-plus base convention `(3,1)` and the physically
equivalent mostly-minus convention `(1,3)` after trace-reversed Frobenius /
DeWitt fiber construction. It then rebuilds the corresponding Clifford and RS
constraint proxies for total signatures `(9,5)` and `(7,7)`.

## Result

Observed local output:

```text
observerse fiber signature mostly-plus:  (6, 4)
observerse fiber signature mostly-minus: (6, 4)
fiber form ||B(g)-B(-g)||: 0.00e+00
total signatures: mostly-plus -> (9, 5); mostly-minus -> (7, 7)

rank_gamma       plus=128 minus=128
ker_gamma        plus=1664 minus=1664
bare_commutator  plus=58.72150807160913 minus=58.72150807160913
C2               plus=155.36250696815043 minus=155.36250696815029

shiab contraction norm plus=152.630272 minus=152.630272
omega^2 error plus=0.00e+00 minus=0.00e+00
J^2 readout plus=-1.000 minus=+1.000
```

The bounded proxies carry no selector signal:

- The trace-reversed fiber form is exactly invariant under `g -> -g`.
- The RS bridge ranks and anchors are unchanged.
- The canon shiab contraction channel remains nonzero with identical norm.
- `J^2` changes only because the total signature was supplied as input.

## Verdict

No base-sign selector appears in these three finite GU-native proxy surfaces.
This strengthens the existing UNDER_DETERMINED verdict for the signature caveat:
the C-07 wall remains genuinely conditional on the `(9,5)` input, not derived
from these finite proxies, and the `(7,7)` branch remains admissible but not
forced.

This audit does not close the open 2-primary Witten/Dai-Freed channel and does
not decide whether a future source-action-level selector exists.
