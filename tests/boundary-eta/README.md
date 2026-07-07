# Boundary-eta certificate family

Executable certificates for the boundary-eta +96 selector fork. This directory records the
finite APS / Dai-Freed denominator checks separating the internal +96 selector from the
tangential order-3 carrier channel.

Boundary posture: this README is a certificate map for boundary-eta scripts, not a claim
status, verdicts, or public posture change. The guarded boundary is that the +96 selector
stays 2-primary or zero on the boundary-eta channel, while the order-3 denominator lives in
the separate tangential framing channel.

## Result Boundary

The recorded boundary is selector/carrier separation. The current checks support the
decoupled reading: the +96 selector is internal to the coefficient/Krein-Clifford factor,
so it does not source the tangential framing term where the order-3 denominator appears.
This is a finite certificate-family boundary, not a derivation of a GU source action and
not a generation-count verdict.

## Scripts

| script | role |
|---|---|
| `aps_eta_antilinear_plus96_rp3.py` | Direct APS eta-bar computation on `L(2;1)`, including coefficient-channel controls, tangential framing controls, and the frame-triviality discriminator for the +96 selector. |
| `plus96_framing_class_lens_eta.py` | Framed-bordism / e-invariant class check comparing the tangential self-dual carrier with the internal +96 selector frame charge. |
| `verify/plus96_eta_denominator_indep_check.py` | Independent denominator and frame-projection re-check that avoids importing the direct boundary-eta certificates. |

## Running

From the repo root, run the central harness:

```powershell
python scripts/reproduce_all.py --quick -k boundary-eta
```

For targeted review, run the direct and independent checks:

```powershell
python tests/boundary-eta/aps_eta_antilinear_plus96_rp3.py
python tests/boundary-eta/plus96_framing_class_lens_eta.py
python tests/boundary-eta/verify/plus96_eta_denominator_indep_check.py
```

## Honest Scope

- Computed certificates: lens-space eta denominator controls, tangential e-invariant controls,
  and finite frame-charge discriminators for the selector/carrier fork.
- Independent verification: denominator arithmetic and frame-projection separation are rechecked
  under `verify/`.
- Analytic boundary: these scripts do not build the GU source action, do not promote claim status,
  do not change verdicts, and do not assert a public-posture change. They keep the boundary-eta
  separation explicit for later review.
