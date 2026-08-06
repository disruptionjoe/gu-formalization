---
artifact_type: hostile_review
created: 2026-08-06
target: explorations/conditional-build/selected-action-n2-null-little-group-green-2026-08-06.md
verdict: PASS_AFTER_REPAIRS
---

# Hostile review: N2 little-group and Green-flux typing

## Reviews

### Representation-theory / massless-field lens

**Attack.** A two-dimensional kernel was previously treated as a plausible
graviton pair before its stabilizer representation was known. Count the
representation, not only its dimension.

**Result.** The exact transverse rotation descends to
`[[0,-1],[1,0]]`, with square `-I` and polynomial `x^2+1`. The spin-two target
has square `-4I` and polynomial `x^2+4`. The mismatch is invariant under a
change of quotient basis. `N2_WRONG_HELICITY` fires.

### Variational-PDE lens

**Attack.** The Schur symbol is mixed order. A two-point derivative formula
would silently treat its quartic metric block as second order and could give a
false Green matrix.

**Repair.** The final probe evaluates six exact time-covector values, verifies
zero fifth finite difference and differentiates the degree-at-most-four pencil
with exact five-node Lagrange weights. The resulting flux has rank two.

### Symplectic-geometry lens (mandatory)

**Attack.** A matrix obtained by differentiating a characteristic symbol is
not automatically the covariant presymplectic current. It must at least
descend under gauge, and even then it remains local principal data.

**Result.** The physical-to-gauge cross is exactly zero and changing the two
physical lifts by gauge leaves the matrix unchanged. This clears finite
principal gauge descent. The report was narrowed to “local principal Green
flux”; covariant phase space, preboundary reduction, BFV and the global
right-`H`/Krein domain remain open.

### Clifford/Krein lens

**Attack.** The finite flux is definite at the positive algebraic embedding,
but the action Hessian is indefinite and the overall action sign is not a
Hilbert-space fundamental symmetry.

**Result.** The report records definiteness up to overall action convention
and makes no positive-energy, ghost-clearance, Fock or unitarity claim.

### Source-critical lens

**Attack.** Do not attribute the coefficient locus, helicity or Green form to
Weinstein merely because the source places Shiab inside an Einstein-directed
action.

**Result.** `SOURCE-CONFIRMS_AND_SOURCE-SILENT`: the source confirms action
placement and intended Einstein replacement, while the new exact results are
repo constructions.

## Two-sided epistemic charges

### Charge 1: where does the summary outrun the artifact?

The first draft called the differentiated two-by-two matrix “the Green form.”
That outran the construction. After the symplectic review it is called the
**local principal Green flux**, with explicit gauge descent and explicit
global-domain exclusions.

### Charge 2: where might rigor defend a superseded or mistyped object?

The tempting continuation was to harden the `N2` domain because the kernel had
two modes and a definite block. The representation calculation shows that
this would rigorously complete the wrong carrier: it is helicity one. The
domain campaign is therefore not continued for `N2`; the distinct second-layer
action owner is promoted instead.

## Scope audit

- Ultimate kill: **no**.
- Scoped route kill: **yes**—positive `N2` as the spin-two carrier of the
  completed first-layer grade-one bank.
- Verdict-count change: none.
- Residue or quotient booking: none.
- P1/P2/P3 use: none.
- Curt/third-lane change: none.
- Canon/public-posture change: none.

## Final disposition

`PASS_AFTER_REPAIRS`.

The exact kernel, rotation action, helicity mismatch and gauge-descending
principal flux are reproducible. The next gate is the separate
`I2B <-> observer ||II||^2` moving owner map with helicity and preboundary
typing, not a global-domain proof for `N2`.
