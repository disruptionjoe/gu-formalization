---
artifact_type: exploration
status: exploration
created: 2026-07-12
title: "D6 Bach Null-Sector Audit"
depends_on:
  - tests/threads/D_hclass_vs_conformal_gravity.py
  - tests/wave1/H1_bach_flat_exact_vacua.py
  - explorations/threads/D-structural-conformal-willmore-functor-scoping-and-first-swing-2026-07-11.md
  - explorations/wave1/H1-gravity-shadow-bach-branch-2026-07-11.md
companion_test: tests/threads/D6_bach_null_sectors.py
---

# D6 Bach Null-Sector Audit

Companion test: `tests/threads/D6_bach_null_sectors.py` (exact sympy, exit 0).

## Question

The D-thread computed that the H-class linearized section operator `box^2 h` is proportional to the linearized
Bach operator on the transverse-traceless spin-2 sector. H1 then showed that exact Schwarzschild/Kerr clear in
the Bach branch, but honestly reduced GU-proper to the OQ2-A functional datum: is the functional the
conformal/gauge-invariant Bach combination, or only the naive componentwise `box^2 h` operator?

D6 audits the linearized null sectors that decide that distinction:

- pure trace/conformal modes,
- pure gauge/diffeomorphism modes,
- and the TT spin-2 baseline.

## Computed Result

The executable audit returns:

| sector | Bach residual | naive `box^2 h` | consequence |
|---|---:|---:|---|
| TT spin-2 profile `h_yy=x^4`, `h_zz=-x^4` | nonzero, with `box^2 h = -4 Bach` | nonzero | agrees with the D-thread: same spin-2 operator |
| pure trace `h_ab = eta_ab x^4` | zero | nonzero | Bach has the conformal null sector; naive `box^2 h` does not |
| pure gauge `h_ab = partial_a xi_b + partial_b xi_a`, `xi_t=x^5` | zero | nonzero | Bach has the diffeomorphism null sector; naive `box^2 h` does not |

The pure-gauge row also verifies that the linearized Riemann tensor is identically zero before checking Bach, so
the vanishing is the expected geometric null mode rather than an accidental cancellation.

## OQ2-A Consequence

The OQ2-A gate is now sharper:

```text
Gravity clears GU-proper only if OQ2-A supplies the conformal/gauge-invariant Bach combination.
The naive componentwise box^2 h operator is insufficient, because it fails the trace and gauge null-sector tests.
```

This does not settle the nonlinear curved-ambient Willmore first variation, the DeWitt ambient curvature terms,
the fiber/gauge terms, or the source action. It does eliminate one ambiguity in the framing: the required
functional is not merely "a fourth-order operator like Bach." It must carry Bach's null sectors.

## Grade

Computation-grade for the linearized null-sector audit. Structural for the implication to full GU OQ2-A.

No claim status, canon verdict, public posture, or source-action state changes. This feeds the same D/H1
follow-up: compute the full higher-codimension Willmore first variation and determine whether GU's OQ2-A
functional is the conformal/gauge-invariant Bach combination.
