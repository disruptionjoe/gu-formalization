---
title: "Selected K77 split-layer commutant and action-parent gate"
status: exact_scoped_construction_result
created: 2026-08-12
target_claim: NONE-NOT-A-KILL
ledger: v0.191
canon_verdict_change: none
---

# Selected K77 split-layer commutant and action-parent gate

## Result in one paragraph

The full-ambient C1/C2 certificate and Joe's two-halves correction are both
right, but they concern different layers.  Exact integer arithmetic gives

\[
\operatorname{End}_{\mathrm{Spin}(1,3)\times\mathrm{Spin}(6,4)}
 (S_{\mathbb R})=\operatorname{span}_{\mathbb R}
 \{1,J_4,J_{10},\omega\}\cong\mathbb C\oplus\mathbb C,
\]

where `S_R` has real dimension 128, `J4^2=J10^2=-1`,
`J4 J10=omega`, and `omega^2=1`.  Each real ambient Weyl half has dimension
64 and a native complex structure, hence complex dimension 32; after
complexification it splits into conjugate complex-32 pieces and has complex
dimension 64.  This is the exact representation-theoretic content behind the
source's two `C^(32,32)` Weyl halves.  It does **not** identify one real half
with `C^(32,32)`, derive its Hermitian signature, or show that the source action
selects a block parent.

## Pre-registration and Layer 0

- **Fork assumed:** `REAL-CLIFFORD-FORM=Cl(7,7)` only.  No resolution of the
  separate `SIGNATURE-AMBIENT` row is claimed.
- **Objects compared:** the real 128-dimensional Clifford module; its two real
  ambient-Weyl halves; their complexifications; the source's complex
  `C^(32,32)` halves; the full complex `U(64,64)` parent; its block-preserving
  `U(32,32) x U(32,32)` subgroup; and the finer subgroup-native endomorphism
  `J4`.  None is silently identified with another.
- **Search dimension:** the complete real commutant in `M(128,R)` is decided
  wholesale by an exact nullspace calculation.  Action ownership is not.
- **New unowned object:** none.  `J4` and `J10` are Clifford volume elements of
  the declared 4+10 split, not fitted matrices.
- **Kill conditions:** commutant dimension one; no square-minus-one element;
  wrong half ranks; failure of subgroup equivariance; or a planted mixed
  generator leaving the commutant unchanged.  None fired.

## Adaptive preflight lenses

| lens | basis | confidence | contribution |
|---|---|---|---|
| Layer-0 semantics | DIRECT | very high | separated real half, complexified half, Hermitian half and group parent |
| prior art/source | DIRECT | high | checked draft eqs. (11.6), (12.19), Curt's two halves and Weinstein's full parent |
| real Clifford/commutant | DIRECT | very high | computed the complete four-dimensional split commutant |
| representation branching | DIRECT | very high | computed real-64 to complex-32 and complexified 32+32 dimensions |
| Krein/Hermitian typing | DIRECT | high | tested invariant real bilinear blocks instead of inferring `(32,32)` |
| principal-bundle/action | PRINCIPLE | high | distinguished compatible reduction from action-selected reduction |
| construction versus selection | PRINCIPLE | very high | native `J` constructs an allowed reduction; it does not select the connection |
| exact controls | DIRECT | very high | wrong split, ambient Spin and dimension-collapse plants all fired |
| contrary path | DIRECT | high | all 40 mixed bivectors preserve `omega` while breaking `J` |
| symplectic/variational | PRINCIPLE | medium | no phase-space or stationary-action conclusion is inferred from the commutant |

## Exact certificate

The deterministic probe reports `20 PASS, 0 FAIL`.

1. The declared indices give disjoint exhaustive signatures `(1,3)+(6,4)`.
2. The 51 subgroup bivectors have a complete real commutant of dimension four,
   exactly spanned by `1,J4,J10,omega`.
3. `J4^2=J10^2=-1`, `J4 J10=J10 J4=omega`, and `omega^2=1`; hence the algebra
   is `C + C`, one complex factor per ambient Weyl half.
4. Both `omega` eigenspaces have real rank 64.  `J4` restricts to each, making
   each complex dimension 32.  Complexifying a real half yields the `+i` and
   `-i` eigenspaces, each complex dimension 32.
5. The subgroup commutant on each real half has dimension two, exactly complex
   type.  However, the invariant real bilinear block dimensions are
   `pp/mm/pm/mp = 0/0/2/2`: the subgroup alone supplies no same-half real
   bilinear from which Curt's Hermitian `(32,32)` can be derived.
6. A subgroup-valued connection preserves both `omega` and `J4`.  All 40 mixed
   base-normal bivectors preserve `omega` but anticommute with `J4`.  All 14
   odd Clifford directions exchange the ambient Weyl halves.
7. Adding one mixed bivector collapses the commutant from four to two.  The full
   ambient Spin commutant is exactly `span{1,omega}` and contains no real
   square-minus-one operator, reproducing C2 at its correct scope.

## What the two group statements mean

The source's statements are compatible, not interchangeable:

- `U(64,64)` is the full complex parent on a complex 128-dimensional carrier.
- Two complex Weyl halves of Hermitian signature `(32,32)` support the
  block-preserving subgroup `U(32,32) x U(32,32)`.
- `D_varpi omega=0` is the algebraic block-preservation condition.
- `D_varpi J4=0` preserves the finer observation split and is stronger than
  block preservation.

The scalar `i` defining the complex parent is also not the same object as the
real endomorphism `J4`.  The latter becomes native only after reducing to
`Spin(1,3) x Spin(6,4)`.  Consequently, the old phrase "complexification is
non-native" survives only at full ambient-Spin equivariance; it is false if
read as a statement about the operative split layer.

## C3-prime disposition

- **C3a — split commutant:** PASSED exactly.
- **C3b — two-half carrier typing:** PASSED for dimensions and complex type.
  The Hermitian `(32,32)` signature is source-asserted and compatible, but is
  not derived by this real commutant calculation.
- **C3c — action parent:** OPEN.  The source does not say whether the operative
  action connection obeys `D_varpi omega=0`, the finer `D_varpi J4=0`, or acts
  through the full parent before observation.

This is a real gain for the conditional build: a valid path to the two-half
geometry now exists and is exact.  It is not yet a source-action selection.

## Implications and boundary

The result narrows `AC-G1a`, `AC-F1`, `RA-F2`, `RA-G2` and `LT-SM3` in distance
and evidence only.  It neither constructs observed chiral cohomology nor
computes local/global anomalies, masses, an index or a generation count.
`P1/P2/P3`, residue, quotients, verdicts, canon and public posture do not move.

The next decisive truth-status research gate is to make `omega` and `J4` moving fields of the
observation reduction and compute their covariant derivatives under the
action-owned connection.  Then test whether stationarity or a declared source
constraint enforces block preservation, the finer split reduction, neither,
or both.  That gate must keep the Hermitian form, external scalar `i`, `omega`
and `J4` typed separately.

Postflight mailbox review found no newer GU-formalization proposal after the
four 2026-08-10 notes already represented by the current priority surfaces;
the successor therefore remains unchanged.
