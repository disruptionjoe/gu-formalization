---
title: "Hostile review — K124 native I1B principal TT evaluator and Cartan gate"
status: reviewed_reconstruction
created: "2026-08-15"
target: explorations/conditional-build/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate-2026-08-15.md
---

# Hostile review — K124

## Strongest objection

The phrase “common full-14D evaluator” can overstate what was constructed.
K124 uses the full real `Cl(7,7)` exterior carrier and directly differentiates
the selected scalar polynomial, but it closes only the local principal TT
normal form. It does not explicitly serialize the curved lower-order jets,
the complete fixed-chart `D2B_LC` recombination, or the noncyclic Cartan
potential. The result must not be summarized as a full nonlinear action or
global-domain completion.

## Adversarial checks

1. **Native-coordinate check:** the metric leg uses `delta B=DB_LC[H]` and
   `delta T=0`. The old fixed-`varpi` `14/3` path is absent.
2. **Direct-action check:** coefficients come from corner polarization of the
   scalar action, not from a prior Hessian column or Ward fit.
3. **Causal check:** `C_t_h_h` is `-24,+24,0` on unit timelike, spacelike and
   null TT representatives, exactly matching `-12q^2 N_DW`.
4. **Polarization check:** plus/cross diagonal values agree and their cross
   entry vanishes.
5. **Mixed-zero check:** `C_t_h_v` is evaluated, not assumed, on 120 entries
   spanning three causal representatives, both metric and distortion TT
   polarizations, and all ten vertical normals.
6. **Control check:** the same evaluator reproduces `8736` and `-56/3`.
7. **Boundary check:** the Green current passes its Lagrange identity, but is
   retained only as a principal representative.

## Residual risk

The main residual is lower-order covariance, not the reported principal
symbol. A fixed-chart implementation could expose nonzero lower-order or
boundary terms hidden by co-moving normalization. K125 must compute that
recombination explicitly and compare it with the principal normal form.

## Verdict

Accept the exact principal TT bulk coefficients and Green identity. Reject
any stronger wording that calls `O_K123` fully nonlinear, selects a complete
pencil or spectrum, or promotes the Cartan representative to a BFV charge.
