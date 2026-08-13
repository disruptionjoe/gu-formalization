---
title: "Next object: the 1472 non-generation sector of ker(Gamma). Its Spin(10)/SM content is characterized NOWHERE, the moment map couples to the 832 and not the 640, and that asymmetry is computed and unexplained"
artifact_type: exploration_result
created: 2026-08-09
status: NEXT_OBJECT_SPECIFIED__640_AND_832_SM_CONTENT_UNCHARACTERIZED__MU_COUPLING_ASYMMETRY_IS_AN_EXISTING_UNEXPLAINED_COMPUTATION__FOUR_STEP_PLAN_WITH_HONEST_DEFLATION_OF_THE_DELTA_NEFF_LEAD
grade: "SPECIFICATION + TRIAGE. No new computation was run for this note. Every fact quoted is already in
  canon or in test output; the contribution is (a) noticing that 1472 of 1664 dimensions have no rep-theoretic
  identification, (b) surfacing the existing mu-coupling asymmetry as an unexplained result, and (c) an
  honest deflation of the cosmological lead this note was originally motivated by. NOT a claim about the
  generation count."
canon_verdict_change: none
follows:
  - canon/source-action-seiberg-witten-RESULTS.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/carrier-dirac-mass-capstone-RESULTS.md
  - canon/leg3-closure-and-spinor-2smoothness.md
  - canon/h2-base-index-chirality.md
---

# The 1472

> ### STEPS 1 AND 2 ARE NOW DONE — this note's "not currently known" is stale.
>
> **Step 1 (content):** `ker(Gamma)` is exactly two-valued under the `Spin(10)` Casimir,
> `(C+11.25)(C+21.25) = 0` at `6.78e-13` — **512 of 16-type, 1152 of 144-type, no `Spin(10)` singlets.** But
> `Spin(10)`-singlet is NOT SM-singlet: building the actual `su(3)+su(2)+u(1)` subalgebra gives **40
> SM-neutral states** (32 at `-11.25`, 8 at `-21.25`). **The dark-sector branch is NOT dead.**
>
> **Step 2 (Krein signature):** all sectors balanced — `640 -> (+320,-320,0)`, `832 -> (+416,-416,0)`,
> `192 -> (+96,-96,0)`, every Gram eigenvalue exactly `+/-1`. K-orthogonality holds structurally. The balance
> is **forced** by `{K,chir}=0`, so it is a corollary, not a discovery.
>
> Both in `run-fast-sweep-carrier-identification-non-discriminating-2026-08-09.md`. The open question is now
> **what the 40 SM-neutral states are**, not whether the sectors are balanced.


## The object

```
ker(Gamma) = 1664 = 640 (j=0) + 832 (j=1/2) + 192 (j=1)
```

under the self-dual `SU(2)_+` Casimir, spectrum `{0, 3, 8}`. As multiplicities:
**640 singlets + 416 doublets + 64 triplets** (`640.1 + 416.2 + 64.3 = 1664`).

**Only the 192 has an identification.** It is the pure `Spin(10)` generation spinor `16 (+) 16bar`, Casimir
`-11.25` exact, spread `1.7e-13`.

**The other 1472 dimensions have no rep-theoretic identification anywhere in the repository.** They are in
the matter module, they are not the generation carrier, and nobody has said what they are.

## The fact that makes this interesting rather than bookkeeping

From the source-action build, verbatim:

> `"16" is false: mu also fires on j=1/2 (median 0.058) and vanishes only on j=0. The restriction to ...`

> **DEFLATED 2026-08-09 (same day). This is a TRIVIALITY, not an anomaly.** `Cas_+ = sum_k J_k^dag J_k` is
> positive semidefinite, so `Cas_+ v = 0` iff `J_+[k] v = 0` for every `k`. The moment map
> `mu^k(Psi) = <Psi, J_+^k Psi>_K` is therefore **identically zero on the 640 BY CONSTRUCTION** --
> the `su(2)_+` moment map vanishes on the `su(2)_+` invariants. Computed: `||J_+[k].W640||_F ~ 3.56e-13`
> against `||W640||_F = 25.298`, versus `||J_+[0].W832||_F = 2.884e+01`. **There is no story to attach here,
> and this note's claim that it was "the cheapest entry point" was wrong.**

**The moment map couples to the 832 and not to the 640.** So the 1472 is not a spectator sector — it splits
into a dynamically coupled half and a genuinely decoupled half, and **that asymmetry is computed, recorded,
and unexplained.** Why the source action's moment map sees the doublets but not the singlets is a well-posed
question with an existing computation already behind it.

This is the cheapest entry point in the whole area: an anomaly that exists in output, with no story attached.

## The plan

### Step 1 — identify the content (decisive, cheap, pure rep theory)

Run the same Casimir/branching analysis that identified the 192 on the 640 and the 832. Machinery exists:
`tests/source-action/sw_moment_map_cl95.py` (the Casimir split), `tests/oq_rk1_cl95_explicit_rep.py` (the
explicit `Cl(9,5)` rep). The 192's identification came from a single exact Casimir value; the same method
applies unchanged.

**Binary and decisive outcome:**

- **SM-charged** -> confront existing collider bounds directly. New charged fermions below ~TeV are excluded,
  so a light charged sector is falsified by data already in hand. That is a real result obtainable now.
- **SM-singlet** -> dark-sector candidates. Proceed to step 2.

### Step 2 — Krein signature per sector (the one that could surprise)

The 192 is `(+96, -96, 0)` — balanced, hence vectorlike. **Compute the signature on the 640 and the 832.**

If also balanced: same mass dichotomy applies, and see the deflation below.
If **unbalanced**: that is a chirally asymmetric sector inside `ker(Gamma)`, and it would be the single most
important object in the program. The whole "net chirality is identically zero" result is stated for the
triplet sector; extending it to the other summands has apparently not been done.

**This is the step with real upside**, and it is a signature computation on an existing substrate.

### Step 3 — mass protection, and the honest deflation

`canon/carrier-dirac-mass-capstone-RESULTS.md` establishes for the carrier: Kramers `C^2 = -1` is pseudoreal,
hence self-conjugate, hence vectorlike, which **admits** a mass rather than forbidding one. Massive ->
decouples to zero net chiral; massless -> a zero-net-chiral modulus.

**If the same argument applies to the 640 and 832 — and there is no obvious reason it would not — they are
generically massive, they decouple, and there is NO cosmological constraint on them at all.**

**So the `Delta N_eff` lead that motivated this note is probably weak.** It bites only if something protects
the sector light, and the default expectation from the capstone reasoning is that nothing does. Recording
that here rather than discovering it after spending a wave on cosmology.

### Step 4 — anomaly cancellation (the better constraint if step 1 returns "charged")

If any of the 1472 carries SM charge, it must cancel anomalies. That is **exact algebra**, needs no cosmology,
no thermal history, and no source action. The repo already computes this class of condition
(`Tr Y = Tr Q = 0` on the Pati-Salam chain). Non-cancellation would mean the module assignment is wrong,
which is a significant finding in either direction.

**Prefer this over `Delta N_eff`.** It is sharper, cheaper, and assumption-free.

## What would kill this lead

1. **640 and 832 are SM singlets AND generically massive** -> they decouple, contribute nothing, and are
   unobservable in principle. Lead dies quietly. **This is the most likely outcome.**
2. They are charged and light -> excluded by existing collider data. The lead dies, but as a *result*.
3. The `mu`-coupling asymmetry turns out to be a normalization artifact rather than structure.

## What this does NOT claim

- Nothing about the generation count. The standing verdict is *located, not forced*, and tilts toward **one**.
- No claim that the 1472 is dark matter. The dimension ratio `1472 : 192` is **not** a mass-density ratio, and
  converting one to the other requires masses, which requires the source action. Quoting `1472/192 ~ 7.7`
  against `Omega_DM/Omega_b ~ 5.4` would be exactly the numerology pattern this repository has caught itself
  in four times.
- No claim that 1472 real Clifford-module dimensions equal any particular number of 4D Weyl fields. That
  conversion is a KK-reduction step and has not been done.

All `(9,5)` arithmetic, on a live but undetermined horn.

## Why this is worth a swing

Every other route in this program waits on the unbuilt source action — six independent leads, all gating on
it. **Steps 1, 2 and 4 need none of it.** They are representation theory and exact algebra on a substrate
that already exists and already runs. Step 2 in particular has genuine upside: it asks whether any sector of
`ker(Gamma)` is Krein-unbalanced, and the answer is not currently known.
