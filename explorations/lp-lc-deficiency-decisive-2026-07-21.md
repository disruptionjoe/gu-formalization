---
title: "The DECISIVE LP/LC deficiency-index computation (single-carrier reduction of O-b): the genuine J-symmetric / Krein deficiency indices of A~ = -iK_uG d_s + W~ at the TRUE flat-geodesic ends of F=GL(4,R)/O(3,1) — verdict LC-SELECTOR. The genuine noncompact ends cross {q<0} generically (~8%, measure-invariant), where K_S is EXACTLY null on the deficiency-relevant halves so the K-definite cut, hence the canonical J-self-adjoint realization of A~, DOES NOT EXIST; the n+=n- guarantee is void and an external Z/2 orientation prescription = the ±i0 section bit = the deck/holonomy phase T_θ=e^{iθ}S(b) = σ = w₁ is required; O-b does NOT close from committed structure. LP-FORCED is NOT available (reconciling with the q<0 crossing needs an unowned excision — Prong-0 CONFIRMED, not refuted). NEW sharpening: even the surviving GAPPED sector's limit-point / 'θ dissolves there' concession is MEASURE- and RAY-contingent — limit-point in flat measure but LIMIT-CIRCLE in the native DeWitt volume on nonzero-drift rays (conf-up w'/w=-8), so Prong-0 A2's drift=0 contradicts its own native-measure Part N. Controls all pass; the true-end computation provably differs from the bounded-collar toy the prior FORCED verdict planted."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-lp-lc-deficiency-decisive-2026-07-21.md
verifies_horns_from: explorations/wave-swing1-the-lemma-2026-07-21.md
inputs:
  - explorations/prereg-lp-lc-deficiency-decisive-2026-07-21.md
  - explorations/wave-swing1-the-lemma-2026-07-21.md
  - explorations/oracle-relative-prong0-measure-lemma-2026-07-21.md
  - explorations/decision-tree-Q1a-hostile-verify-2026-07-21.md
  - explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md
  - explorations/wave-swing3-the-outside-2026-07-21.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/oracle_relative_prong0_measure_lemma_probe.py
  - tests/channel-swings/decision_tree_Q1a_hostile_verify_true_end_probe.py
probe: tests/channel-swings/lp_lc_deficiency_decisive_probe.py (foreground, EXIT 0, double-run byte-identical, all controls pass)
outcome: LC-SELECTOR
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
---

# The decisive LP/LC deficiency-index computation

> **CORRECTION (2026-07-22 — operator/domain/w1 bridge audit).** This run did not construct the
> source-owned noncompact boundary operator or its minimal/maximal domains, Green form, trace space, and
> deck action.  Its reduced potential and WKB/Lyapunov count therefore do not prove that the crossed GU
> expression has unequal deficiency indices or no `J`-self-adjoint realization.  More strongly, the exact
> committed `Cl(9,5)` carrier contains a timelike generator whose `+/-i` spectral halves are `K_S`-null
> while the full generator is still `K_S`-self-adjoint.  The result that survives is: genuine sampled ends
> enter `q<0`, and the **`K_S`-definite spectral cut fails** there.  The conclusions “no canonical
> `J`-self-adjoint realization,” “an external domain prescription is required,” and “that prescription is
> exactly `sigma=w1`” are retracted to `SOURCE-GAP`.  See
> `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md` and
> `tests/channel-swings/operator_domain_w1_bridge_audit.py`.  Original text is retained below as the run
> record and is superseded where it conflicts with this notice.

Adversarial truth-test, maximum skepticism, anti-toy discipline binding. A prior
`Q1a-FORCED` (limit-point) verdict was reached by **planting a toy** (bounded
collar coefficients `P=1+0.2sin`, etc.) and was refuted (`HV-REFUTE`). This run
does the computation the whole program gates on — the single-carrier deficiency
count that decides O-b — on the **actual** `GL(4,R)/O(3,1)` end geometry, with the
**genuine** J-symmetric (Krein/Sims) count, and it **confronts the `{q<0}` stratum
honestly**. This is NOT advocacy; either horn is a result. A summit-closing
`LP-FORCED` would be a PROPOSAL pending independent hostile verification and is
**never** banked here as a theorem.

## 0. Verdict up front

> **`LC-SELECTOR`.** The genuine noncompact fiber ends of `F=GL(4,R)/O(3,1)` — the
> diagonal flat geodesics `exp(s·diag(α))·o` — **cross into `{q<0}` generically**
> (~8% of random genuine ends, on and off the Weyl slice; the sign of `q` is
> measure-invariant). On the crossed ends the Krein form `K_S` is **exactly null**
> (`8.9e-16`) on the deficiency-relevant spectral halves `E_{±i}(D)`, so the
> **K-definite cut that builds the section splitting — hence the canonical
> J-self-adjoint realization of `A~` — DOES NOT EXIST**. `A~` remains a well-defined
> *differential expression* there (`P>0`, so `K_u`, `B`, `W~` all exist), but its
> `n_+ = n_-` guarantee is **void** (the J-real conjugation that would force equal
> indices degenerates with `K_S`), and the generic fate of a first-order end that
> has lost its balancing structure is **unequal indices / no self-adjoint
> extension** (the `-i d/ds → (1,0)` control exhibits it). **An external
> prescription is required to realize the operator at all**, and that prescription
> is the section's `±i0` **orientation bit** — a `Z/2` datum = the deck / holonomy
> phase `T_θ = e^{iθ}S(b)` = **`σ = w₁`**.
>
> **Consequently O-b does NOT close from committed structure.** The single-carrier
> norm-resolvent boundary value is not essentially self-adjoint on the genuine
> ends; the bit gating the lemma **is the posited `σ`**. The pencil theorem stays
> open; `z*` sits in the continuum/washout regime; PP1 stays non-distinctive.
>
> **`LP-FORCED` is NOT available.** Reaching it requires declaring the
> timelike-crossing ends "not genuine," i.e. an **imported excision** of the `q<0`
> stratum that GU does not own. I did not find any structural excision;
> **Prong-0 is CONFIRMED here, not refuted.** (See §5 for the failed reconciliation.)
>
> **NEW sharpening (a genuine correction to the record, at the grade stated in §4).**
> Even the *surviving* gapped sector's "limit-point / `θ` dissolves there"
> concession — granted by `Q1a-FORCED`, by `HV`, and by Prong-0 A2 — is
> **measure- and ray-contingent**. The reduced gapped block is limit-point in the
> **flat/normalized** measure `(n_+,n_-)=(1,1)` but **LIMIT-CIRCLE** `(2,2)` in the
> **native DeWitt volume** on rays with nonzero radial drift (conf-up, `w'/w=-8`),
> because the fast-decaying weight makes **both** modes `L²`; it stays limit-point
> only on drift-0 rays (the traceless shape ray). **Prong-0 A2 computed the gapped
> count with `drift=0`, inconsistent with its own native-measure Part N (`drift=-8`).**
> So the surviving-sector LP is not uniform, and committed structure does not fix
> the measure that decides it — HV's open measure datum is **not** closed by merely
> naming DeWitt. This is a supporting leg; the decisive, **measure-invariant**
> obstruction is the `{q<0}` crossing (§3).

Probe: `tests/channel-swings/lp_lc_deficiency_decisive_probe.py` — foreground,
numpy only, seed `20260721`, **EXIT 0**, double-run **byte-identical**, **all
controls pass**.

## 1. The controls FIRST (kill conditions declared before GU's case)

Maximum-skepticism discipline: the counting method must be shown to have power
*before* it is trusted on GU. One first-order fundamental-matrix / adiabatic-WKB
Lyapunov counter `defect_indices` (counts `L²(w ds)` solutions of `(A~-z)ψ=0` at
`z=±i` via the accumulated real parts of `eig[B^{-1}(z-W~)]`, with the native
measure entering as the `+(1/2)(w'/w)` mode-exponent shift), plus an **independent**
second-order Weyl (Sturm–Liouville) counter `scalar_weyl_defect` with the genuine
WKB amplitude prefactor `|q-i|^{-1/4}` (the factor a bare Lyapunov count omits).

| control | result | reading |
|---|---|---|
| **[b1]** Dirac LP witness: hyperbolic, bounded mass, flat | `(1,1)` | LIMIT-POINT ✓ |
| **[b2]** scalar Weyl `q=-s^{1.5}` (p<2) | `1` | LIMIT-POINT ✓ |
| **[b2]** scalar Weyl `q=-s^{3}` (p>2, degenerate end) | `2` | LIMIT-CIRCLE ✓ |
| **[b2]** scalar Weyl `q=+s^{3}` (confining) | `1` | LIMIT-POINT ✓ |
| **[b3]** UNEQUAL witness `-i d/ds` on `(0,∞)` | `(1,0)` | no s.a. extension ✓ |
| **[b4]** bounded LP block in native-type measure `w~e^{-8s}` | `(2,2)` | LP→LC (measure moved it) ✓ |

All controls pass: the method distinguishes limit-point, a genuine limit-circle
**degenerate** end, an **unequal-index / no-self-adjoint-extension** end, and the
**measure-driven** LP→LC transition. `[b4]` is the crux for §4: the *same* bounded
limit-point operator becomes limit-circle in a fast-decaying measure — so the
LP/LC classification is **not fixed** until the native fiber measure is fixed.

## 2. The true-end asymptotics (real geometry, NOT a toy)

The faithful `n2`/Prong-0 end-model verbatim (DeWitt `(9,5)` form, closed-form
G-orthonormal frame, `D(t,s)=c(ξ(t,s))`, ray `a(s)=exp(2αs)`). Along the genuine
flat geodesics the physical scale is **exponentially unbounded**, and the native
DeWitt radial drift `w'/w = (1/2)d_s log|det G|` is large and non-positive:

| genuine end `exp(s·diag(α))·o` | `slope log|ξ|` | `slope log C_0` | `w'/w` | sector |
|---|---|---|---|---|
| conf-up `(1,1,1,1)/2` | `+0.49/s` | `+0.49/s` | `-8.00` | `q>0` gapped |
| shape `(1,1,-1,-1)/2` | `+0.94/s` | `+0.92/s` | `-0.00` | `q>0` gapped |
| timelike `(0,0,0,1)` | `+0.81/s` | `+0.85/s` | `-4.00` | `q<0` **crossed** |
| tl-tilt `(.3,.2,.1,1)` | `+0.83/s` | `+0.87/s` | `-6.40` | `q<0` **crossed** |

`C_0 = √|q|` grows **exponentially** — it is emphatically **not** the bounded
`O(1)` `P=1+0.2sin` collar surrogate the prior FORCED verdict planted (that is what
`HV-REFUTE` established, reproduced here). The **one theorem-grade survivor** holds
on **both** sectors: `B = -iK_uG` is a product of two involutions, so its singular
values are `1` at any scale wherever `P>0`:

    sv(B) ∈ [1.0000, 1.0000],  K_u² = I to 1e-16,  on gapped AND crossed ends.

Crucially, on the crossed timelike ends `P` stays strictly positive
(`P≈39, 111 > 0`) while `q<0` (`q≈-1.5e4`): **the crossing is NOT `B` degenerating**
— `B` is fine — it is `q` flipping sign, **upstream of `B`**, in the Krein pairing.

## 3. The `{q<0}` confrontation — the decisive, measure-INVARIANT obstruction

The prereg forbids papering over the `K_S`-null stratum. It is confronted directly.

**(Q1) The genuine ends cross `{q<0}` generically.** Over 2000 random genuine flat
ends at `s=5` (half conjugated off the Weyl slice by a random `O(3,1)` boost, which
keeps them genuine `p`-directions), **8% cross into `q<0`**. Since `q = ⟨ξ,ξ⟩_{9,5}`
is built from the symbol and `K_S` alone, its sign is **measure-invariant**: no
positive weight can move a genuine end from `q<0` to `q>0`. The timelike-dominant
flats are **non-conjugate** to the gapped ones (distinct `Ad(O(3,1))` causal type),
so they cannot be rotated into the gapped sector. Reconfirms Prong-0 C2.

**(Q2) At `q<0` the cut does not exist.** `K_S D` is Hermitian (residual `0`) and
the `Im>0` eigenvectors of `D` satisfy `⟨x,K_S x⟩ = 0` to `8.9e-16` — the halves
`E_{±i}(D)` are **exactly `K_S`-null**. Those halves are what the K-definite section
cut is built from; where they are null **no cut exists**, so the canonical
J-self-adjoint realization of `A~` via the cut is **absent**. This is precisely
Prong-0's / wave-swing-3's non-constructibility (`OBSTRUCTED`). Sharper than the
prior record: `A~` is still a well-defined *differential expression* on the crossed
ends (`P>0` keeps `K_u`, `B`, `W~` defined) — what is absent is its canonical
self-adjoint domain.

**(Q3) The `n_+ = n_-` guarantee is void — the operator needs an external bit.**
A J-symmetric operator has equal deficiency indices (hence a J-self-adjoint
extension) only when a **J-real conjugation** maps `ker(A~-i) ↔ ker(A~+i)`. The
Krein Gram between the `+i` and `-i` halves is computed: the **intra-half** pairings
are null (`|⟨+|K_S|+⟩|, |⟨-|K_S|-⟩| ≈ 6–9e-16`) and only the **cross** pairing is
nondegenerate (rank 64). So the conjugation that would force `n_+=n_-` **degenerates
with `K_S`**, and equal indices are **not forced** — the `-i d/ds → (1,0)` control
[b3] exhibits the generic unequal-index / no-self-adjoint-extension fate concretely.
Maximum-skepticism discipline forbids fabricating a `2×2` crossed model to read a
number off it (that is exactly the planting the prior win did); the honest,
committed-structure statement is: **on the crossed ends `A~` has no canonical
self-adjoint realization, and an external prescription is required to define one.**

**The prescription is `σ`.** The required datum is the section's `±i0` **orientation
bit** (sector-relative section theory §4: the two global conventions `q±i0` agree on
the gapped sector and differ by the sign of the crossed-sector polarization; the bit
is `Z/2`, and its operator-grade promotion is the named open question). Geometrically
(wave-swing-1, Member 3, probe-checked topology) this `Z/2` **is** the deck of the
spin cover `S³→RP³≃F`, i.e. `w₁`, i.e. the boundary phase `T_θ=e^{iθ}S(b)` — the
externally-posited `σ`. The negative horn is coherent with the whole program: the
one free bit gating O-b **is** `σ`.

## 4. The gapped sector is not cleanly limit-point either (supporting, grade-limited)

On the gapped ends `q>0` the section symbol `M/√q = K_S e^{αw}` is a `K_S`-definite
involution — the cut exists, and the reduced J-symmetric block is hyperbolic
(`B=-iσ_z`, bounded real mass; the winding `→0` on single-exponent ends). This is
the reduced form `Q1a-FORCED`, `HV`, and Prong-0 A2 all used. The question they did
not press: **in which measure?**

| gapped reduced block | measure | `(n_+,n_-)` | reading |
|---|---|---|---|
| **[K1]** flat `w=1` | flat/normalized | `(1,1)` | LIMIT-POINT (θ dissolves) |
| **[K2]** conf-up, native DeWitt `w~e^{-8s}` | native, `w'/w=-8` | `(2,2)` | **LIMIT-CIRCLE (θ survives)** |
| **[K3]** shape ray, native DeWitt `w'/w=0` | native, drift 0 | `(1,1)` | LIMIT-POINT |

The fast-decaying native weight makes even the "growing" bare Dirac mode `L²`
(`Re(μ)=±√(1+m²)<4=|w'/w|/2`), flipping the gapped end to limit-circle on
nonzero-drift rays. **Prong-0 A2 named `w~e^{-8s}` as the native measure (its Part N)
but then computed the gapped deficiency with `drift=0` (getting `(1,1)`) — an
internal inconsistency.** With its own measure the gapped conf-up end is limit-circle.

**Honest grade of this leg.** Whether the DeWitt volume is truly the `L²` measure in
which `A~` (with its constructed `W~`) is J-symmetric is **not verified** — HV called
the native measure an unfixed datum, Prong-0 asserted DeWitt without verifying
symmetry, and neither is settled here. So this leg does **not** upgrade to "the
gapped ends are limit-circle"; it establishes the weaker, robust claim: **the
surviving-sector LP is measure- and ray-contingent, not a structural fact.** It
removes the last clean refuge for `LP-FORCED` but rests on the DeWitt-measure
assumption and is reported as supporting, not decisive.

## 5. Steelmen (mandatory) and why `LP-FORCED` / `BLOCKED-D2` are not the call

**Steelman `LP-FORCED`.** The `{q<0}` region is where the Dirac symbol hits its
characteristic variety `{q=0}` (wave-swing-3), a genuine finite lightcone — so
perhaps the "real" fiber ends are only the gapped `{q≥0}` interior, on which `A~` is
limit-point and O-b closes. **Why it fails:** `exp(s·diag(0,0,0,1))·o` is a genuine
geodesic of the complete symmetric space `F` reaching `s→∞` with `q→-∞`; the `q<0`
region **is reached by genuine noncompact ends** (and the `q=0` crossing happens at
*finite* `s`, an interior symbol degeneration along the way, which independently
spoils essential self-adjointness). Restricting to `{q≥0}` is exactly the **imported
excision** Prong-0 §4/§7.3 flags as unowned. `LP-FORCED` needs an import GU does not
have; it does not close from structure. **Prong-0 confirmed.**

**Steelman `BLOCKED-D2`.** The measure sub-datum (§4) and the operator-grade
cardinality of the orientation bit (`Z/2` vs `Z/2×Z/2`, section-theory §7.2) are
genuinely open, so maybe the honest verdict is "cannot be pinned; name the missing
input." **Why it is not the call:** the true-end asymptotics **are** pinned here
(`B` a unit involution, `C_0` exponential, `w'/w` computed, the `q<0` crossing, the
`K_S`-null halves). What is external is **identified**, not merely "missing": the
crossed-stratum selector is at least a `Z/2` orientation bit, and that `Z/2` = deck
= `w₁` = `σ`. Naming `σ` as the gating bit is strictly more informative than
`BLOCKED`. The residual openness (native measure; exact cardinality) is a
**sub-grade** of `LC-SELECTOR`, recorded in the ledger — not a retreat to `BLOCKED`.

## 6. Anti-toy control (a): the true-end computation is provably not a toy

The prior FORCED verdict was the counter fed a **bounded collar toy**
(`P=1+0.2sin`, `T=1+0.5sin`, `φ'=0.24cos`) reading LP. Feeding the **same method**
that toy vs the true end:

- collar toy, flat: `(1,1)` limit-point, and it **never** crosses `q<0` (`P,T~1`);
- true gapped end, native measure: `(2,2)` limit-circle (measure-blind toy cannot
  see this);
- true ends cross `q<0` at **8%** with `K_S` exactly null (the toy: 0%, never null).

The true-end computation **differs from the collar toy on both axes** (the count
and the crossing). It is therefore **not itself a toy** — it is sensitive to exactly
the true-end features (`q`-crossing, native measure) the surrogate erases. Control
(b) — LP vs LC degenerate end — is the §1 suite (`[b1]/[b2]/[b4]` distinguish LP,
a genuine LC degenerate end, and the measure-driven LC).

## 7. Typed claims and honest ledger

- **Theorem-grade (unconditional algebra, machine-corroborated):** `B=-iK_uG` is a
  unit involution (`‖B‖=‖B⁻¹‖=1`, `sv=1`) wherever `P>0`, on both sectors; `q`'s
  sign is measure-invariant; at `q<0` the halves `E_{±i}(D)` are exactly `K_S`-null
  (`8.9e-16`); the crossed-half Krein Gram is rank-deficient so the `n_+=n_-`
  conjugation degenerates.
- **NATIVE-computed (faithful end model, sampled ledger):** the genuine ends cross
  `{q<0}` at ~8%; `C_0=√|q|` and `|ξ|` blow up exponentially; the DeWitt radial
  drift `w'/w ∈ [-8,0]` (ray-dependent); the gapped reduced count is `(1,1)` flat /
  `(2,2)` native on conf-up / `(1,1)` native on the drift-0 shape ray.
- **Identification (rides on banked structure):** the crossed-stratum external
  prescription = the `±i0` orientation bit = the deck `Z/2` = `w₁` = `σ` = the
  boundary phase `T_θ=e^{iθ}S(b)`.
- **Residual open (BLOCKED-D2 sub-grade, named not papered):** (i) whether the DeWitt
  volume is truly the J-symmetrizing `L²` measure of `A~` (decides the gapped-sector
  LP/LC and the §4 sharpening's grade); (ii) the operator-grade cardinality of the
  orientation bit (`Z/2` vs `Z/2×Z/2`, sector-theory §7.1–7.2, the N2 operator lift);
  these refine, but do not undo, "the gating bit is `σ`."
- **Falls (do not ship):** "the genuine ends are spacelike-gapped / limit-point at
  both ends" (they cross `q<0`); "O-b closes from structure / `θ=0`" (needs an
  unowned excision AND a fixed measure); "the gapped sector is cleanly limit-point"
  (measure- and ray-contingent).

## 8. Boundary

Exploration tier. Only two NEW files were written — this document and the probe
`tests/channel-swings/lp_lc_deficiency_decisive_probe.py` (foreground, seed
`20260721`, numpy only, **EXIT 0**, double-run **byte-identical**, kill-conditioned
controls declared and run **before** GU's case, all controls pass). GU otherwise
read-only. No commit, no push. No edit to LANE-STATE, research-portfolio,
NEXT-STEPS, the prereg, Prong-0, the Q1a win or its HV, the sector-relative theory,
wave-swing-1/3, or any other agent's artifact, or any claim/canon/verdict/ledger
file. No claim-status, canon-verdict, paper-status, or public-posture change; the
externality of `σ`/`τ` is consumed, not moved. The verdict is **`LC-SELECTOR`**: the
genuine flat-geodesic ends cross `{q<0}`, where the K-definite cut and hence the
canonical J-self-adjoint realization of `A~` do not exist; the `n_+=n_-` guarantee is
void; the required external selector is `σ = w₁`; O-b does **not** close from
committed structure. **`LP-FORCED` is a PROPOSAL that was tested and did not survive
— it is not available and is not banked; Prong-0 is confirmed, not refuted.**
