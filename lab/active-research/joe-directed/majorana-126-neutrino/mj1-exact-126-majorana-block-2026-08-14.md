---
artifact_type: exploration
status: exploration
doc_type: conditional-mechanism-gate
created: 2026-08-14
work_item: MJ-1
channel: majorana_126_neutrino_mechanism
title: "MJ-1 exact Lambda^5/126 Majorana block: the SU(5)-singlet direction of the 126 gives a SYMMETRIC, rank-exactly-one block supported on nu_R alone, with zero mass on the 5bar+10 and no opposite-chirality part -- a genuine Majorana channel, not a vectorlike mass. Exact type-I asymptotics follow. The carrier FIELD and its VEV remain type-missing, so no M_R is derived."
grade: "EXACT integer representation theory in Z[i] on an explicit Cl(10) module, 55/55 primary + 31/31 independent re-verification, no floating point load-bearing anywhere. Plus exact symbolic seesaw asymptotics. NOT: a source action, a vacuum, a VEV, a 5-form field in GU's content, a value or bound for M_R, or any claim-status movement."
disposition: MAJORANA_BLOCK_EXACT_SYMMETRIC_RANK_ONE_ON_NU_R__SM_SECTOR_UNTOUCHED__VECTORLIKE_ALTERNATIVE_EXCLUDED_AT_FAMILY_LEVEL__CARRIER_FIELD_AND_VEV_STILL_TYPE_MISSING
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
fork_robust: true
fork_note: >-
  Every statement here is a complexified-internal statement. Both horns of
  SIGNATURE-AMBIENT reduce through the same internal factor Spin(6,4)
  ((1+6,3+4)=(7,7) and (3+6,1+4)=(9,5)), so no result below depends on the
  open ambient signature. Verified in both probes.
depends_on:
  - tests/chase/MOVE-4/move4_spinor_square_forms.py
  - explorations/yukawa-scoping-2026-07-13.md
  - explorations/su4c-seesaw-retrodiction-2026-08-03.md
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
  - lab/active-research/pati-salam-chain-verification.md
scripts:
  - tests/channel-swings/joe_directed_majorana_126_block_probe.py
  - tests/channel-swings/joe_directed_majorana_126_block_indep_verify.py
---

# MJ-1 — the Lambda^5/126 Majorana block, exactly

## Decision question

Does the located `Lambda^5`/126 channel produce a genuine right-neutrino
**Majorana** block and seesaw scaling, rather than another direct **vectorlike**
mass?

**Answer: a genuine Majorana block — conditional on a VEV that is still not
earned.** The vectorlike alternative is excluded at the equivariant-family
level, exactly.

## What was computed

An explicit `Cl(10)` module (32-dimensional), its chiral half `S+ = 16`, the
charge conjugation `C`, and every bilinear channel `16 (x) 16 -> Lambda^k`.
All arithmetic is integer arithmetic in `Z[i]` carried as paired `int64`
arrays; gamma products are monomial with entries in `{0,+-1,+-i}` and the
largest intermediate magnitude is `2^5`, so every equality tested is an exact
integer equality. No floating-point comparison is load-bearing. This matters
because the prior art on this channel (MOVE-4, H28) is float-based at
`TOL = 1e-9`, and `AGENTS.md` forbids citing a float null.

### 1. The channel table and its symmetry types (exact)

| degree | image | complex rank | transpose type |
|---|---|---|---|
| `Lambda^1` | 10 | 10 | **symmetric** |
| `Lambda^3` | 120 | 120 | **antisymmetric** |
| `Lambda^5` | 126 | 126 | **symmetric** |

Hard checksum `10 + 120 + 126 = 256 = 16^2`, saturating `End(S+)`. The
symmetry types are computed entry-by-entry on every index set, not inferred
from a formula.

One trap is worth recording because it is easy to fall into. In Euclidean
`R^10` the Hodge star on `Lambda^5` obeys `*^2 = (-1)^{5*5} = -1`, so its
eigenvalues are `+-i` and **`Lambda^5(R^10)` does not split over `R`**. The
real map `A |-> C.Gamma_A` is therefore injective with a 252-dimensional real
image, while the complex span is the 126. Both numbers are certified
separately (`252 = 2 x 126`); conflating them reads as a failed checksum when
nothing is wrong.

### 2. The Majorana block (the result)

Take the SU(5)-singlet direction of the 126 — the all-antiholomorphic 5-form
built from `z_j = e_{2j-1} - i e_{2j}`. Its block on `S+ x S+` is:

- **nonzero**;
- **symmetric** — hence a Majorana-type flavor structure, not a `Lambda^3`-style
  antisymmetric one;
- **rank exactly one**, certified by the exact vanishing of all `2x2` minors,
  not by a numerical rank tolerance;
- supported on **exactly one entry**, the diagonal entry of `nu_R`;
- **zero on the entire `5bar + 10`** — every Standard-Model fermion stays
  massless at this scale, which is precisely the SM-preserving property the
  mechanism requires;
- carrying **no opposite-chirality (`S+ x S-`) part** — the vectorlike
  alternative is absent, not merely subleading.

The conjugate half (`126bar`, the all-holomorphic direction) is *identically
zero* on `S+ x S+`. Exactly one of the two singlet directions acts, which is
the expected 126-versus-`126bar` assignment and is verified rather than
assumed.

A planted contrary control is included: a generic (non-singlet) `Lambda^5`
direction does **not** give the `nu_R`-only block, so SM-preservation is a
special property of the singlet direction, not an artifact of the channel.

### 3. Independent re-verification

`joe_directed_majorana_126_block_indep_verify.py` re-derives the result while
changing every convention the primary probe could have smuggled in:

1. a **different Clifford construction** (recursion placing string factors on
   the right, versus left-strung Jordan-Wigner);
2. the **other charge conjugation** (`C'` = product of odd gammas, giving
   `C' G C'^-1 = +G^T` instead of `-G^T`);
3. an **intrinsic `nu_R` identification** — the unique weight vector of the
   `so(10)` Cartan whose five weights are all equal — with no reference to
   basis ordering or occupation number;
4. a **different prime and different square root of `-1`** for the rank
   computations.

All conclusions survive: `31/31`. The verifier also corrected a wrong
expectation in drafting — the all-minus weight has five minus signs, hence
odd parity, hence lies in the `16bar`; the 16 contains exactly **one**
all-equal weight vector, so its SU(5) singlet is unique.

### 4. Seesaw asymptotics (exact symbolic)

For `[[0, m], [m, Lambda]]`: `det = -m^2` and `trace = Lambda` exactly; the
light eigenvalue is exactly `-m^2/Lambda + O(1/Lambda^3)` and the heavy one
exactly `Lambda + O(1/Lambda)`, with `light * heavy = -m^2` identically. The
three-generation type-I form `m_nu = -m_D M_R^-1 m_D^T` is exactly symmetric
and scales exactly as `1/Lambda`. These are symbolic limits and series, not
numerics.

## Claim ceiling — read this before citing

**Standard, not GU-native:** that `16 (x) 16 = 10 + 120 + 126`, that the 126's
SU(5)-singlet VEV gives `nu_R` a Majorana mass, and that type-I seesaw
suppresses the light eigenvalue, are textbook `SO(10)` GUT representation
theory. This artifact does not claim novelty for any of them.

**GU-native content:** (a) the placement of that channel inside the ambient
equivariant family — the Lorentz-scalar part of the ambient `Lambda^5(14)`
channel is exactly `Lambda^5(10) = 126 + 126bar`, with the ambient channel at
multiplicity one; (b) fork-robustness across the open SIGNATURE-AMBIENT horn;
(c) exact integer certification replacing float-graded prior art; and (d) the
sharp separation from SHIAB-05 recorded below.

**What is NOT supplied, and what therefore cannot be said:** GU supplies no
identified field carrying this `Lambda^5` VEV, no VEV, no value or bound for
`M_R`, and no Dirac `m_D`. Every mass statement is conditional on a VEV that
remains unearned (M-H3). **No `M_R` is derived here, and this artifact is not
evidence that GU predicts neutrino masses.** The `1.1-6.0 x 10^14 GeV` band in
M-H3 is standard GUT arithmetic on the verified group-theory chain, not a GU
output, and nothing here changes that.

## Misaimed-kill guard: SHIAB-05 does not target this gate

SHIAB-05 establishes `dim Hom(S+ (x) S+, Lambda^0) = 0` — no same-chirality
Majorana **scalar** channel. That is a statement about `Lambda^0` of the
ambient `V_14`. The object here is the **Lorentz-scalar component of the
`Lambda^5(14)` channel**, i.e. an internal 5-form, which is a different object
in the same equivariant family. The primary probe reproduces the SHIAB-05
result as a live control (`Lambda^0` absent on `S+ x S+`) *and* exhibits the
nonzero `Lambda^5` block in the same run, so the two coexist. Citing SHIAB-05
against the 126 route is a misaimed kill.

## Next in-channel gate (MJ-2)

The mechanism is available in the representation theory; what is missing is a
**carrier**. The next gate is therefore: does GU's actual field content
contain any object that can carry a VEV in the internal `Lambda^5(10)`
SU(5)-singlet direction? CB-A already excludes the entire rank-two internal
tensor class as a Higgs parent; `Lambda^5` is untouched by that theorem, so
the question is open and decidable. A negative there would convert this
conditional mechanism into a located structural gap — which is a more useful
result than the conditional itself.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface is moved by this artifact.
