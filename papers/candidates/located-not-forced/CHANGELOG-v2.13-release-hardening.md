# v2.13 publication hardening

**Date:** 2026-07-23  
**Scope:** theorem-boundary clarity, evidence hardening, and later-release preparation.  
**Verdict:** unchanged. The paper does not claim three generations.

The Markdown manuscript is the canonical research draft for this hardening swing. Final TeX/PDF/Zenodo
parity and rendering are intentionally deferred until publication preparation resumes.

## Manuscript changes

- Added an explicit **IN class C / OUT of class C** table after Theorem 1. The table fixes the carrier,
  operator, data, and analytic boundaries of the completeness claim and states that “OUT” means outside
  the quantified class, not impossible or inadmissible.
- Separated finite-torsion constraints, integer-valued constraints, numerical projection-balance
  diagnostics, and the finite Krein intersection theorem. None is silently converted into another
  codomain or into a physical handedness/Fredholm index.
- Removed the stronger claims that the finite audit proves a universal operator no-go, makes antilinearity
  the unique escape, or makes external background data necessary. Non-equivariant, K-definite,
  function-space, and true-`Y14` source-action constructions remain open.
- Corrected the framed-class statement: `2 in Z/24` and `e_R=1/12 in Q/Z` have order 12; only the projected
  `Z/3` component has order 3.
- Narrowed the finite equivariant parity backstop, source-action toy tests, carrier-mass test, and global
  anomaly test to the constructions actually computed.
- Removed the long internal version history from the manuscript; detailed history stays in changelog files.
- Updated the creator line to **Joseph Hernandez, Independent Researcher**.
- A preliminary TeX sync and Tectonic render was completed before the Markdown-first decision. It is not
  the final publication artifact and must be reconciled and re-rendered at publication time.

## Reproducibility and review changes

- Re-ran the one-command numerical/symbolic harness: **31/31 enumerated checks pass**.
- Removed a cosmetic divide-by-zero warning from the deliberately invalid non-`su(2)` control without
  changing any scientific output.
- Added a machine-readable load-bearing-number manifest and release-evidence validator.
- Extended the finite Lean core and reviewer-facing replication material; these additions remain
  internal-tier verification and do not constitute independent external validation.
- Added a prior-art delta and adversarial release review for publication handoff.

## Claim-status guard

No theorem, novelty claim, or generation-count status is promoted by this release. In particular:

- the full framed class has order 12; its projected 3-primary component is not identified with an integer
  count (`Hom(Z/3,Z)=0`);
- the finite Krein intersection theorem is not a physical handedness, graded-trace, or Fredholm-index claim;
- the class-C no-go names a delimited obstruction class, not every conceivable construction; and
- the true-`Y14` source-action calculation remains open and is not silently treated as package hardening.
