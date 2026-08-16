---
artifact_type: exact_construction_and_object_crosswalk
status: active_research
doc_type: construction_result
record_kind: dropped_commitment_execution_and_scope_adjudication
created: 2026-08-16
work_item: AR-5
channel: archaeology
target_claim: NONE-NOT-A-KILL
result: LITERAL_CL95_CONTRACTION_SURJECTIVE__RANK_REAL_3584__KERNEL_REAL_19712__CURRENT_K77_MAP_DISTINCT
canon_verdict_change: none
claim_status_change: none
public_posture_change: none
ledger_row_changes: none
registry_change: pending_root_integration_this_wave
canonical_effect: none
probe: tests/channel-swings/joe_directed_ar5_cl95_full_shiab_rank_crosswalk.py
worklist_rows:
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md (section 5, row 12)
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md (section 6, row 21)
title: "AR-5: the literal canonical Cl(9,5) spinor contraction is surjective,
  with exact real rank 3,584 and kernel 19,712; the current K77
  1,274-by-1,274 Hodge--Shiab is a different object, and the supplied-192
  follow-up is retired behind two explicit revival triggers"
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

This artifact closes one exact repository-internal question about one literal
map. It does not identify Weinstein's preferred Shiab, select the supplied
`192`, transfer a Cl(9,5) result to K77, or adjudicate a physical claim.

---

## Result first

AR-1 row 12 quoted the open condition in
`canon/shiab-existence-cl95.md`: compute the full-domain rank and kernel of the
literal constructed Clifford contraction

\[
 A:\Lambda^2V^*\otimes S_{\mathbb R}\longrightarrow V^*\otimes S_{\mathbb R},
 \qquad
 A(\alpha\otimes s)=\sum_a e^a\otimes
 c(\iota_{e_a}\alpha)s,
\]

where `dim V=14`, the declared horn is `Cl(9,5)`, and
`S_R=H^64` has real dimension `256`.

The answer is exact:

```text
domain real dimension       = C(14,2) * 256 = 23,296
codomain real dimension     = 14 * 256       =  3,584
rank_R(A)                   =                    3,584
kernel dimension_R(A)       =                   19,712
```

Thus the literal map is **surjective and very far from injective**. The proof
does not estimate a `23,296 x 3,584` matrix. It constructs a signed algebraic
companion `A^sharp` and diagonalizes `A A^sharp` into the gamma-trace and
gamma-traceless summands. On the declared Cl(9,5)/W192 horn this companion is
the verified Krein adjoint. Its two eigenvalues at `n=14` are `26` and `12`,
both nonzero.

This closes AR-1 row 12 only at the following scope:

```text
CLOSED_EXACT_FOR_LITERAL_CL95_CONTRACTION
__NO_K77_OR_SOURCE_SELECTOR_TRANSFER
```

It does **not** supersede or duplicate the current selected-K77 theorem. That
theorem concerns a different coefficient carrier, formula, real-form branch,
and source grade.

---

## 1. Preflight and archaeology — eight lenses

### Lens 1 — object identity

The old canon object is a spinor-valued contraction:

```text
Lambda^2 V* tensor S_R  ->  V* tensor S_R.
```

The current selected-K77 object is the equation-(9.3) two-term Hodge--Shiab,
restricted as

```text
Lambda^2 V* tensor Cl_1  ->  V* tensor Cl_2.
```

The shared word “Shiab” is not a typed identification.

### Lens 2 — signature and real form

The literal map here uses the conditional `(9,5)` canon branch and its
quaternionic real spinor. The current construction uses the declared K77
`Cl(7,7)` source algebra. `REAL-CLIFFORD-FORM` is settled for the latter while
`SIGNATURE-AMBIENT` remains a distinct open fork. This computation selects
neither horn and imports no K95 coefficient into K77.

### Lens 3 — domain and codomain

The two shapes disagree before any rank calculation:

| map | source | target |
|---|---:|---:|
| literal Cl(9,5) spinor contraction | `91*256 = 23296` real | `14*256 = 3584` real |
| selected K77 `comm/symi/symi` map | `91*14 = 1274` real | `14*91 = 1274` real |

One cannot be a re-expression of the other without a new carrier map in both
source and target.

### Lens 4 — explicit formula

The literal map contains one interior-product/Clifford-multiplication term.
The selected K77 map contains the source-displayed `Phi_1`, `Phi_2`, Hodge and
two-term nesting, plus a repository-selected triple of coefficient products.
The latter acts on a basis cell by

```text
F_ij^k |-> -2 epsilon_i epsilon_j epsilon_k T_k^ij.
```

No such signed-permutation formula is being asserted for the spinor map.

### Lens 5 — rank and kernel exactness

The selected K77 map already has exact rank `1274` and kernel zero. The old
canon condition remained open because only nonzero-ness, dimensional
noninjectivity, and a four-dimensional horizontal restriction had been filed.
The theorem below supplies the missing full-domain calculation.

### Lens 6 — source ownership

Canon explicitly describes the Cl(9,5) contraction as a constructed
counterexample to a universal forced-complexification objection and explicitly
leaves its identification with GU's actual Shiab open. The K77 equation-(9.3)
formula is source-displayed, but the `comm/symi/symi` product is still
repository-selected rather than Weinstein's recovered historical preference.
Neither result supplies the missing selector.

### Lens 7 — chronology and supersession

The K77 rank theorem landed later than the old canon gap but adjudicated a
different object. AR-1 row 12 was therefore not `SUPERSEDED`; it remained a
literal-map cleanup task. AR-5 executes that task and records the non-transfer
boundary rather than rewriting either history.

### Lens 8 — downstream dependency and novelty

No current K77 dependency requires this rank. Its value is exact canon hygiene
and prevention of a recurring object conflation. The result does not reopen the
old K95 generation-carrier programme, and it should not outrank current
source-native conditional-build work.

---

## 2. Exact signed-companion theorem

Let `(V,g)` be a nondegenerate real quadratic space of dimension `n>2`. Choose
an orthonormal frame with

\[
 g(e_a,e_b)=\epsilon_a\delta_{ab},\qquad \epsilon_a\in\{+1,-1\},
\]

and write `gamma_a=c(e_a)`, so

\[
 \gamma_a\gamma_b+\gamma_b\gamma_a
 =2\epsilon_a\delta_{ab}.
\]

Store a two-form spinor as `x_ab=-x_ba`. Then

\[
 (Ax)_a=\sum_b\gamma_b x_{ab}.
\]

Define the signed algebraic companion by

\[
 (A^\sharp y)_{ab}
 =\epsilon_b\gamma_b y_a-\epsilon_a\gamma_a y_b.
\]

Here `sharp` first names this displayed algebraic operator. On the repository's
declared Cl(9,5) spinor horn, and on W192's filed horizontal restriction, the
compatible nondegenerate Krein pairings identify the signed companion with the
Krein adjoint of `A`. Outside those filed horns, this theorem asserts only the
algebraic companion formula. It does **not** assert that every irreducible real
spinor in every signature carries the required induced form, or that `sharp`
is an adjoint there.

The metric signs are load-bearing in the companion formula. Omitting them
fails on the `(9,5)` branch; the probe carries that mutation as an adverse
control.

Now compose:

\[
\begin{aligned}
 (AA^\sharp y)_a
 &=\sum_{b\ne a}\gamma_b
   (\epsilon_b\gamma_b y_a-\epsilon_a\gamma_a y_b)\\
 &=(n-1)y_a+\epsilon_a\gamma_a
   \sum_{b\ne a}\gamma_b y_b\\
 &=(n-2)y_a+\epsilon_a\gamma_a\Gamma(y),
\end{aligned}
\]

where

\[
 \Gamma(y)=\sum_b\gamma_b y_b.
\]

Define gamma insertion by

\[
 G(s)_a=\epsilon_a\gamma_a s.
\]

Then

\[
 \Gamma G(s)=\sum_a\epsilon_a\gamma_a^2s=ns.
\]

Therefore

\[
 V^*\otimes S=\ker\Gamma\oplus\operatorname{im}G,
\]

with exact projectors

\[
 P_{\rm tr}=\frac1nG\Gamma,
 \qquad
 P_{\rm RS}=I-P_{\rm tr}.
\]

The composition is diagonal on this decomposition:

\[
 AA^\sharp=(n-2)P_{\rm RS}+2(n-1)P_{\rm tr}.
\]

For `n=14`, the eigenvalues are `12` and `26`. Hence `AA^sharp` is invertible,
so `A` is surjective. An explicit right inverse is

\[
 R=A^\sharp\left(\frac1{n-2}P_{\rm RS}
       +\frac1{2(n-1)}P_{\rm tr}\right),
 \qquad AR=I.
\]

The signed-companion/right-inverse identity, and therefore surjectivity of
`A`, is signature-independent **for nondegenerate Clifford relations**. This
is an algebraic statement, not a universal claim about induced-form adjoints
on irreducible real spinors. The cancellation is exact because
`epsilon_a gamma_a^2=epsilon_a^2=1`. It is not available on a degenerate form;
the probe's `epsilon_a=0` contrary control destroys gamma invertibility and
fires as required.

At `n=14` and `dim_R S=256`, surjectivity gives

\[
 \operatorname{rank}_{\mathbb R}A=14\cdot256=3584,
\]

and rank-nullity gives

\[
 \dim_{\mathbb R}\ker A
 =(91-14)\cdot256=77\cdot256=19712.
\]

---

## 3. Independent four-dimensional control

W192 computed the horizontal restriction on the frozen `(3,1)` observer
section using the explicit complex `128`-dimensional Cl(9,5) representation:

```text
Lambda^2 H tensor C^128 -> H tensor C^128
shape                         768 -> 512
rank_C                              512
kernel dimension_C                  256
singular values          sqrt(2) x 384, sqrt(6) x 128
```

The theorem predicts at `n=4`:

```text
gamma-traceless eigenvalue of AA^sharp = n-2       = 2
multiplicity                            = 3*128      = 384
gamma-trace eigenvalue of AA^sharp      = 2(n-1)    = 6
multiplicity                            = 128
```

Thus the old explicit computation is reproduced exactly as squared singular
values, rank and nullity. AR-5 did not fit its formula to W192: the universal
Clifford calculation fixes the two values before that receipt is read.

---

## 4. Current-K77 object crosswalk

| axis | literal canonical Cl(9,5) contraction | selected current-K77 Hodge--Shiab |
|---|---|---|
| real-form branch | conditional K95 `(9,5)` | declared K77 `(7,7)` |
| coefficient carrier | real spinor `S_R=H^64` | Clifford grades `Cl_1 -> Cl_2` |
| source shape | `Lambda^2 V* tensor S_R` | `Lambda^2 V* tensor Cl_1` |
| target shape | `V* tensor S_R` | `V* tensor Cl_2` |
| formula | one interior contraction | two-term `Phi_1/Phi_2` Hodge--Shiab |
| size | `23296 -> 3584` real | `1274 -> 1274` real |
| exact rank/kernel | `3584 / 19712` | `1274 / 0` |
| source ownership | constructed existence counterexample; actual selector open | displayed candidate grammar; product still repo-selected |

The current result is the exact signed-permutation theorem

```text
F_ij^k |-> -2 epsilon_i epsilon_j epsilon_k T_k^ij,
```

not a spinor contraction rank computation. No source, target, action, or
observation maps have been constructed that make the square between these two
operators commute. **No transfer in either direction is licensed.**

---

## 5. AR-1 row dispositions

### Row 12 — executed, with a narrower scope than AR-1's label suggested

Disposition:

```text
CLOSED_EXACT_FOR_LITERAL_CL95_CONTRACTION
__NO_K77_OR_SOURCE_SELECTOR_TRANSFER
```

The literal map is surjective, not injective; its exact kernel has dimension
`19,712`. This closes the rank calculation. It does not close canon's separate
source-forced selector question, port the result to K77, or change a canon
verdict. Accordingly this artifact records a successor crosswalk and does not
rewrite AR-1's historical table or canon.

### Row 21 — retired from current work, not refuted

AR-1 row 21 inherited a reported zero coupling between the old Cl(9,5)
contract+wedge family and the supplied `192`-dimensional `W`. The later carrier
scope correction establishes that `W` is a supplied conditional carrier, not a
source- or action-selected physical generation carrier. The current K77 Shiab
is also a different map.

Disposition:

```text
RETIRED_NONCURRENT
__REVIVE_ONLY_IF_W192_SOURCE_ACTION_SELECTED
__AND_TYPED_CL95_TO_K77_SHIAB_BRIDGE
```

This does not refute the old conditional fixed-`W` zero. It says there is no
current source-native question to ask of that zero. Reopening requires both:

1. an independently source- or action-owned selection of the proposed `W`; and
2. a typed bridge between the old Cl(9,5) spinor Shiab family and the operative
   K77 equation-(9.3) coefficient map.

The present conditional-build lane is forbidden to construct either missing
owner. Therefore row 21 is dependency-fenced rather than a successor swing.

---

## 6. Exact probe and adverse controls

The companion probe uses no floating point arithmetic.

1. It implements the Clifford algebra on its ordered signed-blade basis.
2. It constructs `A` and the signed algebraic companion `A^sharp`
   independently; on the declared Cl(9,5)/W192 horn the latter is the verified
   Krein adjoint.
3. It checks the coefficient identity on the unit generator of the faithful
   Cl(9,5) left regular module in every vector slot. Because both sides are
   identities of left Clifford coefficients, equality on the unit implies
   equality after their action on every Clifford blade by associativity; this
   is the exact universal step, not a numerical sample.
4. It independently replays the identity on a deterministic blade insurance
   set (unit, volume, even/odd alternating blades, and all 14 one-blades), then
   checks both the algebraic companion formula and its exact right inverse on
   that set in every ordered signature class `(p,14-p)`, `p=0,...,14`. This is
   the signature-independent surjectivity sweep; it makes no universal
   adjointhood claim.
5. It verifies gamma invertibility, the two eigenspaces, and the exact rational
   right inverse.
6. It reproduces W192's `2/6` squared singular values, `384/128`
   multiplicities, rank and nullity from the filed receipt.
7. It reads the current K77 registry and checks the distinct
   `comm/symi/symi`, `1274 x 1274` signed-permutation object.

Adverse controls all fire:

- dropping the metric signs from the signed companion breaks the `(9,5)`
  identity;
- reversing the antisymmetric output sign breaks it independently;
- setting one `epsilon_a=0` destroys Clifford invertibility;
- the dimension control rejects injectivity;
- the object-shape control rejects Cl95/K77 conflation.

Reproduce:

```text
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ar5_cl95_full_shiab_rank_crosswalk.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ar5_cl95_full_shiab_rank_crosswalk.py --selftest
```

---

## 7. Claim ceiling and reprioritization

**Established:** the exact full-domain rank and kernel of the literal canonical
Cl(9,5) Clifford contraction; a signature-independent algebraic
signed-companion/right-inverse theorem for nondegenerate Clifford relations at
`n>2`; identification of that companion as the Krein adjoint on the declared
Cl(9,5)/W192 horn; exact agreement with W192's horizontal restriction; and a
typed nonidentity with the current selected-K77 map.

**Not established:** that the literal contraction is Weinstein's preferred or
actual Shiab; a selector among the natural equivariant family; a choice of the
`SIGNATURE-AMBIENT` horn; a source/action selection of `W`; a Cl95-to-K77
bridge; existence of a compatible induced-form adjoint on every irreducible
real spinor/signature; an action, vacuum, coefficient, external datum,
observation quotient, analytic domain, physical mode, family count, chirality
mechanism, mass, or spectrum.

**Priority consequence:** bank row 12 as exact internal cleanup. Retire row 21
behind its two-part revival trigger. Neither belongs on the active
conditional-build portfolio unless genuinely new source-owned structure
arrives.
