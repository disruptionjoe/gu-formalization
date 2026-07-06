# Pati-Salam Chain Checks

This directory exposes the existing active-research Pati-Salam verification as
a `tests/` reproduction surface.

`run_pati_salam_chain_checks.py` runs both owner scripts:

- `lab/active-research/pati_salam_chain_verification.py`
- `lab/active-research/verify_clifford_explicit.py`

The harness checks that both scripts exit successfully and still emit their
success markers. It does not change the active-research verdict and does not
claim that the Pati-Salam chain derives a physical generation count.
