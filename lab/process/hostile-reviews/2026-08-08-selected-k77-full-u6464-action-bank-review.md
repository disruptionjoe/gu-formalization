# Hostile review — selected K77 full pointwise u(64,64) action bank

Date: 2026-08-08
Disposition: **PASS AFTER GEOMETRY CORRECTION AND GLOBAL FENCE**

## Charges

### 1. Symplectic geometer

The complete coefficient support changes the observed normal-image inertia
from `(5,5,0)` to `(4,6,0)`.  Rank `14/10` alone was therefore insufficient:
the omitted grade-5 directions alter the inherited quadratic geometry even
though they do not enlarge the equation image.  The corrected full-support
pairing is now the only admissible local input to later endpoint/BFV work.
Opposite local restrictions preserve that pairing, but no global moment map,
charge algebra, polarization or reduction is inferred.

### 2. Representation and real-form reviewer

The calculation covers every real direction in the **pointwise** K77
`u(64,64)` comparator: 8,128 B-skew real directions plus 8,256 `i` times
B-self directions.  That statement must not be widened to the K95/right-H
`Sp(32,32;H)` fork.  Nor does pointwise completeness construct the global
associated adjoint bundle or its sections.

### 3. Variational and exact-computation reviewer

The symbolic-adjoint shortcut is exact: it moves fixed Clifford factors
through the scalar trace rather than sampling directions.  Every v0.76
low-grade entry is recovered; direct grade-5 directions agree; a held-out
background has the same live grade set but a distinct support union.  An
independent Sage reconstruction reproduces determinants and inertias.  This
charge passes.

### 4. Generalization adversary

Two exact backgrounds show live grades `1,2,5`.  They do not prove that every
background has no support in grades `6,9,10,13,14`.  The report therefore
states a two-fixture exact result rather than a universal grade-selection
theorem.  The complete 16,384-direction evaluation is complete at each
fixture, not across field space.

### 5. Krein/operator reviewer

The scalar Clifford coefficient form is exact and nondegenerate on the
computed image, but it is not thereby a positive energy or an analytic Krein
domain.  The indefinite `(4,6,0)` inertia is reported as data.  Common closed
domains, Green hyperbolicity and physical positivity remain open.

### 6. Observation and source reviewer

The rational `4+10` equation-dual graph has an exact inverse, but it is not
the physical global observation section.  The source confirms the
`U(64,64)`-type presentation and product vocabulary; it is silent on the
preferred Shiab, global bundle, BFV and domain.  The full action bank is a
repo derivation, not a quotation.

## Two-sided synthesis audit

- **Summary outruns artifact:** prevented by replacing “full coefficient and
  bundle” with “full pointwise coefficient fibre” throughout.
- **Fence defends superseded object:** the v0.76 rank result is retained, but
  its low-grade pairing is superseded by the full-support geometry.  A
  planted test explicitly fires when rank is used as a proxy for completeness.

## Independent rerun

```text
Python exact probe:                 58/58 PASS
Independent Sage reconstruction:   27/27 PASS
seed union:                         549 = 14 + 59 + 476
held-out union:                     628
full/normal rank:                   14/10
raw/observed full-support inertia:  (4,6,0)/(4,6,0)
```

No claim-status, canon-verdict or public-posture change is authorized.
