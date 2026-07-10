---
artifact_type: exploration
status: exploration
created: 2026-07-09
title: "SG1 -- both-signature control: the C-07 quaternionic-parity no-go on (7,7) = M(128,R)"
grade: "COMPUTED (bit-exact matrix certificate on both signatures); class-relativity finding, reconstruction-tier. Internal: computed, single implementation, not externally replicated. No verdict/canon/posture change."
depends_on:
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/multiplicity-theorem.md
  - explorations/big-swing-2026-07-07/BIG-SWING-RS-INDEX-STILL-GATED.md
  - tests/oq_rk1_cl95_explicit_rep.py
scripts:
  - tests/big-swing/sg1_signature_carrier_parity_77.py
---

# SG1 -- both-signature control: is the C-07 even-parity no-go carrier-universal or (9,5)-specific?

## The swing

The canon C-07 no-go (`canon/no-go-quaternionic-parity-generation-sector.md`) proves that every
GU-native Hermitian carrier on `Cl(9,5) = M(64,H)` commutes with a quaternionic structure `J_quat`
with `J^2 = -1`, so by Kramers' theorem its kernel nullity (hence its signature, the literal
generation index) is forced **even** -- an odd count such as 3 cannot arise natively. The canon
already flags, **at proof grade**, that this "DISSOLVES under a defensible alternative real-class
signature such as (7,7) (J^2 = +1)", and BIG-SWING-RS-INDEX (2026-07-07) records "(7,7) = M(128,R)
unprobed" as "the cheapest remaining hardening." This goal **probes it by explicit computation**,
converting the proof-grade caveat into a computed both-signature control.

## What was computed (`tests/big-swing/sg1_signature_carrier_parity_77.py`, exit 0)

For each signature `(p,q)` in `{(9,5), (7,7)}` (both `p+q=14`, `dim_C S = 128`), an explicit
Jordan-Wigner Clifford rep, and the antilinear intertwiner `J = U . conj` commuting with **every**
generator `e_a`, built (no search) as the product of the imaginary-conjugation generators:

| signature | `p-q mod 8` | algebra | `J^2` | Kramers even-nullity | odd-rank J-projector |
|---|---|---|---|---|---|
| (9,5) | 4 | `M(64,H)` quaternionic | `-1` (dev 0.0e+00) | **ACTIVE** (all eigval mults even) | rank-3 target forced to rank **6** (even) -- **unreachable** |
| (7,7) | 0 | `M(128,R)` real | `+1` (dev 0.0e+00) | **INACTIVE** | genuine rank-**3** J-commuting projector exhibited -- **reachable** |

All Clifford relations bit-exact (`max_err = 0.0e+00`); `J^2 = ±1` scalar to `0.0e+00`.

## Verdict

**The C-07 even-parity no-go is SIGNATURE-SPECIFIC (class-relative in the six-axis sense).** It is a
theorem on the `(9,5)`/H-class carrier and **dissolves** on the `(7,7)`/R-class carrier, where an odd
generation index including 3 is parity-**admissible**. Two honest qualifiers, unchanged:

1. **This does not force three on (7,7).** The rank/index stays a **free choice** on *both* carriers
   (C-06 under-determination); `(7,7)` removes the parity *obstruction*, it does not supply the
   integer. Under-determination is untouched.
2. **This does not assert GU selects (7,7).** It is a class-relativity / robustness control that
   prices which located-not-forced conclusions are carrier-universal (the under-determination) and
   which are `(9,5)`-specific (the even-parity wall). Whether GU's `Y^14` is `(9,5)` or `(7,7)` is a
   separate metric-convention question (the trace-reverse signature choice in the primary sources).

## Consequence for the program

The even-parity wall should be cited **only** with its `(9,5)`/H-class hypothesis attached (the canon
already does this). Any argument that leans on "odd is impossible" is invalid on the real-class
signature; the durable, carrier-universal content is the **under-determination**, not the parity
no-go. No target imported; no verdict, canon, or public-posture change. Generation count stays OPEN
(located, not forced).
