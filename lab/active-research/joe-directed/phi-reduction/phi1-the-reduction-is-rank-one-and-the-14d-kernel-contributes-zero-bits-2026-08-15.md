---
artifact_type: exploration
status: exploration
doc_type: construction-delta
created: 2026-08-15
work_item: PHI-1
channel: conditional_ledger_advancement
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
axis: ANOMALY_CONSISTENCY
rows: [AC-C2, AC-D1, AC-D2, AC-D3, AC-D4, AC-D5, AC-E1]
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: "NONE-NOT-A-KILL — no GU source claim is targeted, attacked or defended. The object BUILT is the previously-unbuilt 14→4 reduction map `phi : Z^15 → Z^6` that LA-5 §2.9 typed and left at T3. The objects ADJUDICATED are (i) LA-5's stated success criterion `phi(ker M) ⊆ L`, together with its attached shape constraint 'phi must annihilate at least 8 of the 10 admissible content directions and at least 5 of the 7 Hodge-antisymmetric ones'; and (ii) the `distance` strings carried by ledger rows AC-C2 and AC-D1..AC-D5 ('none after the chiral 16 shadow is selected' / 'none after the 16 is observed'), which locate the residual condition in the 14D kernel."
title: "PHI-1: phi is CONSTRUCTED and it has RANK ≤ 1 — so LA-5's rank bound is met by every candidate and is not a criterion at all. Derived from the observation pullback MD-1 established: s^* annihilates Ω^p for p ≥ 5 outright (Λ^p T*X4 = 0), so phi factors through the truncation T(x) = (x_0..x_4); and the form index is GAUGE-BLIND inside CB-C's own construction of M (the Casimir Y occurs only in ch(S)), so psi_p = k_p·v with v ∈ Z^6 the internal SM content of the observed 4D spinor. Explicitly phi = v ⊗ (1,−1,1,−1,1,0,…,0), the k_p being the exact signed spin-1/2 multiplicities of Λ^p T*X4 ⊗ (1/2,0). T maps ker M ONTO Z^5 (Smith divisors all 1), so phi(ker M) = phi(Z^15) = Z·v: 14D anomaly cancellation contributes EXACTLY ZERO bits to the 4D anomaly verdict through the observation. Since L is saturated, phi(ker M) ⊆ L ⟺ v ∈ L ⟺ the observed 4D content is SU(5)-complete. ZERO ROWS ADVANCE; six of seven get a strictly narrower, re-arena'd condition. Contrary horn: on the disavowed KK projection the reduction functional k'' = (1+t^5)(1+t)^9 lies IN the row space of M, so phi_KK(ker M) = {0} and the criterion holds unconditionally by producing an identically EMPTY 4D spectrum — a kill of that horn, not a derivation of the rows."
grade: "EXACT throughout: fractions.Fraction / integer linear algebra over Q, sympy Rational, Smith and Hermite normal forms on integer matrices, exact sympy symbolic differentiation against a general metric section, and exact integer weight-multiset decomposition of sl(2,C)⊕sl(2,C) representations. No float is load-bearing anywhere; assert_no_float sweeps the result dict. 149/149, exit 0, via tests/channel-swings/joe_directed_phi_reduction_construction.py, which IMPORTS tests/anomaly/cb_c_anomaly_rank.py rather than reimplementing the 14D system. Certificate splits as 101 [E] exact results, 32 [C] controls that must fire, 16 [R] reproductions of filed owners (CB-C's rank 5 / kernel 10 / Hodge A7 / W-in-row-space; LA-2's 2189 height-1 kernel points; LA-3's rank 4 / L / saturation / the 2D1−27D2−36D3−9D4+9D5 relation; MD-1's E1/E2/E3). FAILURE PATH EXERCISED: five planted mutations (k-sign, truncate, gauge-blind, L-wrong, kk-fibre) each run to exit 1 through the check harness. NOT: a source action, a chirality-production mechanism, a generation count, a real-form statement, a decision of the SOLDERED-AD fork, a supply of the representation datum v, a ledger edit, or any verdict movement."
disposition: PHI_CONSTRUCTED_AND_HAS_RANK_AT_MOST_ONE__LA5_RANK_BOUND_MET_BY_EVERY_CANDIDATE_AND_IS_THEREFORE_NOT_A_CRITERION__LA5_NAMED_BASIS_PROSE_IS_FALSE_WHILE_ITS_PROBES_RANK_READING_IS_TRUE__TRUNCATION_MAPS_KER_M_ONTO_Z5_SO_14D_ANOMALY_CANCELLATION_CONTRIBUTES_ZERO_BITS__CRITERION_COLLAPSES_TO_v_IN_L_A_PURE_4D_REPRESENTATION_DATUM__U4S_ANOMALY_RELEVANT_HALF_IS_NOT_INDEPENDENT_OF_U1_EMB__KK_CONTRARY_HORN_SELF_KILLS_BY_EMPTYING_THE_4D_SPECTRUM__ZERO_ROWS_ADVANCE
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched: [AC-C2, AC-D1, AC-D2, AC-D3, AC-D4, AC-D5, AC-E1]
rows_advanced: 0
grants_retyped: [U4]
depends_on:
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - tests/anomaly/cb_c_anomaly_rank.py
  - lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la2-aca1-needs-no-kernel-selection-and-the-cascade-is-two-thirds-already-banked-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - lab/methods/source-native-comparator-routing.md
  - lab/process/conditional-physics-ledger-v0.258.json
scripts:
  - tests/channel-swings/joe_directed_phi_reduction_construction.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains a
> conventional particle-physics comparator: the 4D Standard-Model perturbative
> gauge-anomaly conditions and the lattice `L = Z·(15 of SU(5)) ⊕ Z·(nu^c)`,
> which are fork-1 objects. Any result about them binds only that named model.
> It is not evidence for or against Weinstein's source-native mechanism without
> an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers before reusing this result.
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`.**

# PHI-1 — the reduction is rank one, and the 14D kernel is invisible to it

**Blunt statement first, before any argument.** I constructed `phi`. It is a
`6 × 15` integer matrix of rank at most one. Because it has rank at most one,
LA-5's success criterion `rank(phi|ker M) ≤ 2` is satisfied — *and satisfied by
every other candidate in the space too*, which means LA-5 typed a criterion
that cannot discriminate. The criterion that does discriminate, `phi(ker M) ⊆ L`,
collapses exactly to a condition on a single six-component vector `v` that the
14D data provably cannot supply, and that the **representation** axis already
owns. So: **zero rows advance.** Six of the seven get a strictly narrower and
differently-located condition. One (`AC-E1`) is untouched.

I built a map. I did not derive the rows.

---

## 0. Prior art, swept by mechanism, and what this file does not re-claim

Swept by mechanism (pullback, contraction, section, exterior power, truncation,
gauge-blindness, internal singlet, form index, rank-1 reduction, lattice
homomorphism, row space, anomaly selector), not by label.

| already owned | by | what PHI-1 does with it |
|---|---|---|
| the 14D system: `12×15`, rank 5, `ker M` rank 10, Hodge row A7 | CB-C, `tests/anomaly/cb_c_anomaly_rank.py` | **imported**, never re-derived |
| `W = Σ_p x_p C(14,p)` lies in the row space of `M`, so `W = 0` on `ker M` | CB-C §STRUCTURE | **reproduced**; PHI-1's `k''` result is a *second instance* of the same phenomenon and is credited as such |
| 2189 / 82501 / 984169 / 6590681 kernel points at heights 1–4 | LA-2 | height-1 count **reproduced** as an anchor |
| 4D rank 4 not 5; `L` rank 2 and **saturated**; the exact relation `2D1 − 27D2 − 36D3 − 9D4 + 9D5 = 0`; `L` is a subgroup so a chiral 16 and the empty content give the same anomaly vector | LA-3 | **reproduced**; the last fact is the seed of §5's kill |
| the reduction is a **contraction**, `s^*` along `s(x) = (x, g_ab(x))`, surjective onto `T*X`, lossy by 10 on the 1-form leg | MD-1 (E1/E2/E3) | **reproduced**, then **extended** from the 1-form leg to every form degree |
| "vertical components become 4D scalars" is **refuted and withdrawn** | LA-8 | honoured; the clause is not re-imported, and §5 shows the horn that needs it self-destructs |
| 4D anomaly cancellation has **zero discriminating power** over GU's forks | AC-1 | PHI-1's zero-bit result is the *reduction-level* analogue, by a **different mechanism** (truncation + gauge-blindness, not vanishing group invariants). The headline "anomalies cannot select" is **not novel**; the route to it here is. |
| `AC-C2`'s doublet count is divisible by 4, not merely even | LA-5 §2.5 | **reproduced** on the constructed reduction |

Nothing below claims novelty for any row of that table.

---

## 1. PREFLIGHT — the requirement, re-derived, and what moved

LA-5 §2.9 states the target exactly:

> For `AC-D1..D5` to be `DERIVED` rather than `DERIVED_CONDITIONAL`, every
> admissible 14D content must reduce to an anomaly-free 4D content:
> `phi(ker M) ⊆ L`. Then `rank(phi|ker M) ≤ 2` and
> `dim ker(phi|ker M) ≥ 10 − 2 = 8`.
>
> "**At most 2 of the 10 admissible 14D content directions can survive to 4D.
> The reduction must annihilate at least 8 — and at least 5 of the 7
> Hodge-antisymmetric directions `e_p − e_{14−p}` that CB-C row A7 proved are
> free.**"

Re-derived from the banked artifacts and confirmed on the arithmetic. **Two
things moved.**

**(i) The rank half is right; the named-basis half is wrong.** "At least 5 of
the 7 Hodge-antisymmetric directions" is true as a *dimension* statement about
the antisymmetric span (`7 − rank(phi|A) ≥ 5`) and false as a statement about
the seven *named basis vectors* `a_p = e_p − e_{14−p}`. LA-5's own probe checks
the dimension version (`7 - rankL = 5`), so the probe is correct and only the
prose over-reaches. It matters here because the constructed `phi` annihilates
the antisymmetric span down to rank 1 — comfortably inside the bound — while
annihilating only **two** of the seven named directions, `a_5` and `a_6`. A
reader applying the prose test would wrongly reject the map that satisfies the
real one. Filed as a **prose correction to LA-5 §2.9**, not a defect in its
computation.

**(ii) `phi(ker M) ⊆ L` does not need the rank bound as a separate condition.**
Since `L` has rank 2, `phi(ker M) ⊆ L` *implies* `rank(phi|ker M) ≤ 2`
automatically. The rank bound is a consequence, not an independent test. LA-5
presents it as the actionable shape constraint the supplier must satisfy; it is
in fact the weakest possible consequence of the criterion, and §4 shows every
candidate satisfies it.

Everything else in the brief re-derives unchanged: `ker M` rank 10 with the
7-antisymmetric / 3-symmetric split; `L` rank 2 and saturated with witness
`(1,1,1,1,1,7)`; the 4D system rank 4; `Y14 = Met(X4)` with internal
`Sym^2(T*X4)`, DeWitt signature `(6,4)`.

**Preflight lenses, run inline.**

- **Lattice theory / commutative algebra.** The two endpoints are lattices, and
  the question `phi(ker M) ⊆ L` is a question about images of sublattices, so
  *saturation* is going to be load-bearing somewhere. It is: it is what makes the
  image index `g` in `phi(ker M) = Z·g·v` irrelevant to the verdict. Flagged
  before the build, used in §4, controlled by a witness on the non-saturated `2L`.
- **Homological / factorisation.** A map out of `Z^15` that is *induced* by
  something must factor through whatever that something does first. Asking "what
  does the observation do to the 15 slots *before* any 4D reading" is what turns
  an unbuilt object into a two-factor problem. This is the whole construction.
- **Representation theory.** The target `Z^6` is indexed by *internal* quantum
  numbers. The source index `p` is a *form degree*. If those two are independent
  the map is forced to be rank ≤ 1. So the first thing to check is whether they
  are independent — and the place to check it is not physics intuition but the
  construction of `M` itself. Predicted before computing; confirmed in §2.1.
- **Index theory.** `M`'s columns are degree-16 components of `Â ch(Λ^p T_C) ch(S)`.
  Any 4D multiplicity functional that is itself an index density has a real
  chance of lying in `M`'s row space. CB-C already found one (`W`). This lens
  predicted §5's `k''` result before it was computed.
- **Adversarial / red-team.** Two attacks were set up in advance: (a) reject the
  pullback, use a KK projection — §5; (b) reject gauge-blindness, solder `S` —
  §2.1's control. Both were built as live controls, not as prose caveats.
- **Ledger accounting.** LA-5 makes `U4` the axis SPOF with fan-out 7. If `phi`'s
  only free parameter turns out to be an object another grant already owns, then
  `U4` is not an independent atom for these rows and the axis's degree-of-freedom
  count is over-stated at this vertex. Predicted; realised in §6.

---

## 2. THE CONSTRUCTION

### 2.1 The form index is gauge-blind — and this is `M`'s own assumption

CB-C builds every column of the 14D system as a product

```
        D_p  =  [ A-hat(TY) ch(Lambda^p T_C) ]  *  ch(S_gauge)
```

and the gauge Casimir `Y = y^2` — the Sp(1) Cartan square, the only place gauge
charge enters — occurs **only in `ch(S)`**. Verified over all 15 columns:

```
   Y-exponents in the form-leg factor  A-hat ch(Lambda^p T_C) :  [0]
   Y-exponents in the gauge factor     ch(S)                  :  [0,1,2,3,4]
   Y-exponents in the assembled D_p                           :  [0,1,2,3,4]
```

So in the arena where `ker M` is defined, **the Standard-Model quantum numbers
live entirely in `S`, and the form degree `p` carries none of them.**

This is the load-bearing structural input and it is *not a grant*. It is an
assumption already made by `M`, the very object whose kernel we are reducing. A
reduction that denies it does not get a different `phi` — it loses `ker M`, and
with it the entire question. (Control: an internal-blindness-violating map
reaches rank 5 and breaks the LA-5 bound, so the rank result is genuinely bought
by gauge-blindness and not by the shape of `ker M`.)

### 2.2 The observation pullback truncates: ten slots die outright

MD-1's `s^*` reproduced (E1, E2, E3), then extended. On `p`-forms the
observation acts by `Λ^p(ds^T) : Λ^p T*Y → Λ^p T*X`. Since `X4` is
four-dimensional, `Λ^p T*X4 = 0` for `p ≥ 5`. Computed exactly on two
independent rational sections:

```
   rank( Lambda^p s^* )  =  C(4,p)  =  1, 4, 6, 4, 1      for p = 0..4
   rank( Lambda^p s^* )  =  0                              for p = 5..14
```

and the annihilated source spaces are not small — `dim Λ^p T*Y` for `p = 5..14`
is `2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1`. **Ten of the fifteen
content slots are annihilated by the observation itself, not by a choice.**
(Control: a degenerate rank-3 section drops `rank Λ^2` from 6 to 3 and `rank Λ^4`
from 1 to 0, so the check has power.)

Therefore `phi` factors:

```
        phi  =  psi o T ,        T : Z^15 -> Z^5 ,  T(x) = (x_0, x_1, x_2, x_3, x_4)
```

### 2.3 The form degree only multiplies

By §2.1 the factor `Λ^p T*X4` carries no SM charge, so the SM content of
`Λ^p T*X4 ⊗ s^*S` is an **integer multiple of one vector**:

```
        psi_p  =  k_p * v ,     v in Z^6 = the internal SM content of s^*S
```

The integers `k_p` are Lorentz multiplicities, and for the spin-1/2 projection
they are computed here exactly, by weight-multiset decomposition of
`sl(2,C) ⊕ sl(2,C)` representations (no character table is asserted; every
decomposition is derived and the routine is controlled against a planted wrong
answer):

```
   Lambda^0 T*X4 = (0,0)                 Lambda^0 (x) (1/2,0) = (1/2,0)
   Lambda^1 T*X4 = (1/2,1/2)             Lambda^1 (x) (1/2,0) = (1,1/2) + (0,1/2)
   Lambda^2 T*X4 = (1,0) + (0,1)         Lambda^2 (x) (1/2,0) = (3/2,0) + (1/2,0) + (1/2,1)
   Lambda^3 T*X4 = (1/2,1/2)             Lambda^3 (x) (1/2,0) = (1,1/2) + (0,1/2)
   Lambda^4 T*X4 = (0,0)                 Lambda^4 (x) (1/2,0) = (1/2,0)
```

Counting `(1/2,0)` as `+1` and its conjugate `(0,1/2)` as `−1`:

```
        k  =  ( +1, -1, +1, -1, +1 )  =  ( (-1)^p )_{p=0..4} ,     gcd = 1
```

Note this is **not** the naive dimension count `C(4,p)` — the chirality flips at
odd form degree, which is exactly why the alternating pattern appears.

---

## 3. THE MATRIX

```
        phi  =  v (x) k  :  Z^15 -> Z^6 ,        k = (1, -1, 1, -1, 1, 0,0,0,0,0,0,0,0,0,0)
```

For `v = (1,1,1,1,1,1)`, the complete 16, the `6 × 15` integer matrix is

```
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = Q
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = u^c
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = d^c
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = L
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = e^c
        [ 1  -1   1  -1   1   0 0 0 0 0 0 0 0 0 0 ]     row = nu^c
```

`rank(phi) ≤ 1` for every `v` — checked on five different `v` including a
generic one — and `rank(phi) = 0` exactly when `v = 0`.

**The rank bound is robust to the entire Lorentz read-off question.** Which
components of `Λ^p T*X4 ⊗ S` count as 4D chiral fermions is *not* settled by the
source. It does not matter: over an exhaustive sweep of all `3125` integer
weightings in `{−2..2}^5` of the five Lorentz types that occur, the maximum rank
attained is **1** (ranks `{0,1}` both attained, so the sweep is neither vacuous
nor saturated). Every candidate satisfies LA-5's `≤ 2`.

---

## 4. THE DECISION

**The truncation maps `ker M` onto the whole of `Z^5`.** `M`'s pivot columns are
exactly `{0,1,2,3,4}` — the observed slots — and its free columns are exactly
`{5,…,14}` — the annihilated ones. The `10 × 5` matrix `T(ker M basis)` has rank 5
and Smith elementary divisors `[1,1,1,1,1]`, so

```
        T(ker M)  =  T(Z^15)  =  Z^5      exactly.
```

Consequently, for **every** `psi` — not only the rank-1 ones — `psi(T(ker M))`
and `psi(T(Z^15))` are the *same lattice*, verified by canonical Hermite normal
form on a rank-5, a rank-2 and the derived rank-1 `psi`.

```
        phi(ker M)  =  phi(Z^15)  =  Z . v
```

`k` applied to the ten `ker M` basis vectors gives
`[−377, −1373, −2002, −1373, −377, −1, 1, −1, 1, −1]`, whose gcd is 1 — so the
image is `Z·v` on the nose, not a proper sublattice.

> **ZERO-BIT RESULT. 14D anomaly cancellation contributes exactly zero bits to
> the 4D anomaly verdict through the observation.** The image of the rank-10
> admissible lattice is identical to the image of the entire unconstrained
> content lattice `Z^15`. Imposing `M x = 0` changes nothing that observation can
> see.

Control: the 14D system is *not* invisible to everything — a primitive row of
`M` annihilates `ker M` and does not annihilate `Z^15`. The invisibility is
specific to maps that factor through the observation.

**And so, since `L` is saturated:**

```
        phi(ker M) subset L      <==>      v in L
                                 <==>      n_Q = n_u = n_d = n_L = n_e   (n_nu free)
                                 <==>      the observed 4D content is SU(5)-complete
```

Verified exhaustively over `[−3,3]^6`, with the saturation step controlled by a
witness on the non-saturated `2L` (where `2·(15) ∈ 2L` but `(15) ∉ 2L`, so the
step genuinely uses saturation). Positive witnesses: the 16, the 15, `15 + 7ν^c`,
`4 × 16`. Firing controls: a lone `Q`; `(1,1,1,1,0,0)`; a 16 minus one `d^c`.

And directly, over all `59049` integer points of `ker M` with free coordinates in
`{−1,0,1}`: the 4D anomaly verdict is **constant**. With `v = Q` alone the same
sweep is not constant, so the check has power.

**`AC-C2` on the constructed reduction.** The doublet count is
`(3n_Q + n_L)·m = 4n_Q·m` for `v ∈ L` and any 14D multiplicity `m = k·x ∈ Z` —
divisible by 4, reproducing LA-5's sharpening, and failing for `v ∉ L`.

---

## 5. THE CONTRARY CONSTRUCTION, BUILT — and it self-destructs

The strongest attack is to reject the pullback and take the **disavowed KK-style
projection** instead: split `Ω^p(Y) ⊃ Λ^a T*X ⊗ Λ^b(fibre)` with `a + b = p`,
`a ≤ 4`. Now all fifteen slots reach 4D and `T` is not the right first factor.

Two things happen, and the second is decisive.

**First, the rank result survives untouched.** The fibre is `Sym^2(T*X4)`, which
MD-1 showed is *endogenous* — built from the same tangent space the Lorentz group
acts on. It therefore carries no SM charge either, so `Λ^b` of it is still an
internal singlet and `psi_p = k''_p · v`. `rank(phi_KK) = 1`. The generating
function is closed-form:

```
        sum_p k''_p t^p  =  (1 - t + t^2 - t^3 + t^4)(1+t)^10  =  (1 + t^5)(1+t)^9

        k''  =  [1, 9, 36, 84, 126, 127, 93, 72, 93, 127, 126, 84, 36, 9, 1]
```

**Second — and this kills the horn — `k''` lies IN the row space of `M`.**

```
        rank( M | k''      )  =  5  =  rank(M)      k'' IS an anomaly condition
        rank( M | k_pullback )  =  6                 k  is NOT
        k'' . (every ker M basis vector)  =  0
```

So on the KK horn, `phi_KK(ker M) = {0}`. The criterion `phi(ker M) ⊆ L` holds
**unconditionally, for every `v` whatsoever** — because the 4D fermion content of
every admissible 14D content is **identically empty**. That is a vacuous
derivation of `AC-D1..D5`, in exactly the sense LA-3 already identified when it
found that a chiral 16 and the empty content return the same anomaly vector. It
is a kill of the horn, not a win for the rows.

This is the same phenomenon CB-C already banked for the net-chirality functional
`W = Σ_p x_p C(14,p)`, which is likewise in the row space. PHI-1 adds the exact
characterisation of the family:

> **`c(t)·(1+t)^10` annihilates `ker M` if and only if `c` is palindromic**
> (`c_0 = c_4`, `c_1 = c_3`). Both `W` (`c = (1,4,6,4,1)`) and `k''`
> (`c = (1,−1,1,−1,1)`) are instances. Verified exhaustively over `c ∈ {−1,0,1}^5`,
> with a non-palindromic control that does not annihilate.

**The fork is therefore load-bearing and it is already decided.** MD-1 settled
the reduction as the contraction, and LA-8 withdrew the vertical-scalar clause the
KK horn needs. The pullback horn is the source-native one, and it is the one that
leaves a residual condition.

One more separation worth recording: `k''` is Hodge-**symmetric**, so it
annihilates all seven named antisymmetric directions; `k` annihilates only two.
LA-5's *prose* criterion separates the two horns; its *rank* criterion does not
(both are rank 1); and the `L`-verdict does not either — it is `v ∈ L` on the
pullback horn and vacuously true on the KK horn.

---

## 6. WHAT MOVES FOR THE SEVEN ROWS

**Zero verdict advances.** Stated first so nothing below reads as a promotion.

| row | before | after PHI-1 |
|---|---|---|
| `AC-D1..D5` | `SAME` / `EXACT`, distance *"none after the chiral 16 shadow is selected"*, revival *"a physical carrier not equal to complete 16s"* | verdict and grade **unchanged**. The `distance` string is **wrong in arena**: it locates the residual condition in a selection inside the rank-10 14D kernel, and no such selection can change the 4D verdict. Corrected condition: **"none after the internal SM content `v` of the observed 4D spinor `s^*S` is fixed, and `v` is SU(5)-complete: `n_Q = n_u = n_d = n_L = n_e`, `n_ν` free."** The revival trigger is now exactly checkable — it fires iff `v ∉ L` — and, as LA-3 already found, *"complete 16s"* is strictly too strong: `15` and `15 + 7ν^c` are both fine. |
| `AC-C2` | `SAME` / `EXACT_CONDITIONAL`, distance *"none after the 16 is observed"* | unchanged; reconfirmed as a strict corollary on the constructed reduction, with LA-5's divisibility-by-4 sharpening reproduced. Same arena correction as the `D` rows. |
| `AC-E1` | `SAME` / `CITED_NOT_REDERIVED`, distance *"independently recompute the full Dai-Freed shadow"* | **untouched.** PHI-1 is a statement about the perturbative lattice. It supplies nothing toward the global/Dai-Freed recomputation and does not shorten that distance by one step. |

**The grant-structural consequence, and it is the real ledger result.** LA-5
makes `U4` — "the 14→4 reduction plus whatever produces 4D chirality" — the
anomaly axis's single highest-fan-out atom, blocking seven rows. PHI-1 builds the
reduction half of `U4` and finds that its entire anomaly-relevant content is the
vector `v`. But `v` is the internal SM content of the observed 4D spinor: that is
`U1`/`EMB`'s object, the representation axis's own central unknown (LA-4 counts
13 grants on that axis). Therefore:

> **`U4` is not an independent grant atom for these seven rows.** Its
> anomaly-relevant half is a function of `U1`/`EMB`. The anomaly axis is
> *entirely downstream* of the representation axis for `AC-C2` and `AC-D1..D5`,
> with zero independent content of its own. LA-5's incidence rank of 7 is
> over-counted at this vertex.

That does not move a verdict. It removes a vertex from the work graph, which is
worth more than a verdict that would have been conditional anyway.

---

## 7. POSTFLIGHT

**Postflight lenses, run inline: lattice/saturation, representation theory,
index theory, differential geometry of sections, 4D anomaly physics, adversarial
red-team, ledger accounting.**

### 7.1 Strongest overclaim available, and why it is refused

*"`phi` is built and it satisfies LA-5's criterion, so `AC-D1..D5` are `DERIVED`."*

Refused on three counts, in descending order of severity.

1. **The criterion is not discriminating.** `rank(phi|ker M) ≤ 2` is satisfied by
   every one of the 3125 candidates swept, on both fork horns, for every `v`.
   Passing a bound that nothing in the candidate space can violate is not
   evidence. LA-5 presented it as the actionable shape constraint; it is not one.
   **This is a correction to LA-5, not a win.**
2. **`phi` is built only up to `v`, and `v` is a grant.** The 14D half is complete
   and exact — the truncation, the gauge-blindness, the Lorentz multiplicities.
   The 4D half is not built at all. Saying "`phi` is built" without that
   qualification would be false. What is proved is that `v` is the *only*
   remaining freedom and that the map is rank ≤ 1 in it.
3. **"Zero bits" is scoped.** 14D anomaly cancellation contributes zero bits *to
   the 4D perturbative anomaly verdict, through the observation pullback*. It does
   not follow that `ker M` is uninformative about anything else, nor that the 14D
   anomaly conditions are physically vacuous. `AC-A1`–`AC-A7` are untouched.

A fourth, weaker overclaim also refused: the arithmetic `dim S = 128 = 2 × 64`
and `64 = 4 × 16` is *not* a derivation that `v = 4 × 16`. It is arithmetic. It
is recorded here only so a later wave does not rediscover it and mistake it for
a result.

### 7.2 Strongest contrary construction

Built, not described — §5. The KK horn is the only route that escapes the
truncation, and it survives the rank test (rank 1, same as the pullback) but
destroys itself on the image test: its multiplicity functional is an anomaly
condition, so its 4D spectrum is identically empty. The second contrary — solder
`S` so the form index carries gauge charge — is carried as a live control (rank 5
is then reachable, LA-5's bound is then violated), and it is not available because
`M` itself assumes the factorisation; taking it removes `ker M`.

The contrary that is **not** closed: if the true 4D internal content does not lie
in the six-dimensional constituent lattice of a `16` — if there are exotics — then
the target `Z^6` is the wrong arena and the whole criterion moves. LA-3's own
arena-extension controls already show one exotic `Y = 1/2` singlet or one exotic
`Y = −1/6` triplet restores rank 5. The arena is a fork-1 comparator choice and it
is not derived. Named, not closed.

### 7.3 Weakest seam

**The spin-1/2 projection discards charged higher-spin content that contributes
to the same anomalies.** `Λ^p T*X4 ⊗ S` contains `(1,1/2)`, `(3/2,0)` and
`(1/2,1)` pieces carrying the *same* internal quantum numbers as the spin-1/2
pieces. `phi` lands in `Z^6`, the SM **constituent** lattice, which has no spin
slot — so those components are simply not represented in the target, while
`D1..D5` as functionals on `Z^6` would not be the complete 4D anomaly conditions
for a spectrum containing charged spin-3/2.

This does **not** break the rank result — that survives every weighting, §3 — but
it does mean the *target lattice* would have to be extended before the criterion
`v ∈ L` is the whole 4D anomaly condition. The repo already has the exact
machinery: AC-1 derived the Rarita-Schwinger rescalings (pure-gauge `3, 4, 5`;
mixed gauge-gravitational `−21, −20, −19`) at literature-fetched grade. Wiring
them into an extended target lattice is the named next step, and it is a
comparator-side extension, not a source-native one.

Second seam, smaller: `T(ker M) = Z^5` and the pivot/free split coinciding with
the observed/annihilated split are computed in the coordinate basis `x_0..x_14`.
The image statement is basis-free (Smith divisors all 1), but the *pivot*
statement is a left-to-right elimination artefact and is reported as such — it is
presented as "the first five columns span the column space", which is basis-order
dependent and true, not as a canonical property.

---

## 8. CERTIFICATE

`tests/channel-swings/joe_directed_phi_reduction_construction.py` — **149/149,
exit 0.**

```
   [E] 101   exact results
   [C]  32   controls that must fire
   [R]  16   reproductions of filed owners
```

Reproductions: CB-C (12 monomial keys, rank 5, kernel dim 10, Hodge row A7, the
integral kernel basis, `W` in the row space); LA-2 (2189 height-1 integer kernel
points); LA-3 (rank 4, `dim ker = 2`, `15` and `ν^c` anomaly-free, the
`(1,1,1,1,1,7)` witness, the exact `2D1 − 27D2 − 36D3 − 9D4 + 9D5 = 0` relation,
`L` saturated); MD-1 (E1 `ds` rank 4, E2 the contraction formula against a general
metric section, E3 the 10-dimensional kernel).

Exactness: `fractions.Fraction` and integer arithmetic over `Q`, sympy `Rational`,
Smith and Hermite normal forms on integer matrices, exact symbolic differentiation,
exact integer weight-multiset representation decomposition. `assert_no_float`
sweeps the result dict. No float is load-bearing anywhere.

**Failure path exercised — five planted mutations, each exits 1 through the check
harness:**

| `--mutate=` | plants | fires |
|---|---|---|
| `k-sign` | flips the sign of `k_2` | 6 checks |
| `truncate` | truncates at `p ≤ 3` instead of `p ≤ 4` | 4 checks |
| `gauge-blind` | pretends the form leg carries `Y` | 1 check |
| `L-wrong` | uses a lone `Q` as the positive witness | 1 check |
| `kk-fibre` | fibre dimension 9 instead of 10 | 12 checks |

---

## 9. WHAT THIS DOES NOT SUPPLY

No source action. No chirality-production mechanism. No generation count. No
real-form statement. No decision of the `SOLDERED-AD` fork. No supply of `v`. No
ledger edit. No verdict movement. No claim about the global/Dai-Freed sector.
The 14D system is imported and the 4D lattice is reproduced; neither is
re-claimed here.
