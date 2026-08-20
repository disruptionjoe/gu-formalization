---
artifact_type: exploration
status: exploration
doc_type: source-native-conditional-compatibility-classifier
created: 2026-08-20
work_item: SA-2
channel: soldered_ad
title: "SA-2: the two live Lorentz embeddings do not preserve the same source package -- the block embedding preserves external-spin/internal-partner factorization, while the endogenous graph embedding fuses the factors, removes every pure Weyl submodule from F, moves both exact PS owner lines, and admits no simultaneous PS-plus-endogenous invariant in 16 tensor 144; this is a conditional structural discriminator, not a physical selection"
grade: "EXACT conditional theorem over integer weights and rational matrices represented by Python's `fractions.Fraction`. The certificate verifies source/prior-owner custody, doubled-weight restrictions of 10, both 16 halves, 144, both F sectors, both Z sectors, the full 16 tensor 144 product, and the 45/54/210 owner summands; direct rational matrices verify the PS lines, orbit ranks, and graph-invariance commutator span. 80/80 exact checks pass with no load-bearing float. Eight planted false routes are caught only by genuine FAIL lines after a clean baseline: torus-fifth, wrong-144, drop-f-term, inert-delta, trace-owner, freeze-phi, drop-graph-commutators, block-acts. NOT: a selected physical Lorentz embedding, action, background, vacuum, external datum, coefficient, family row, scale, selector, global quotient, analytic domain, spectrum, or observed net-chirality theorem."
disposition: H_PRESERVES_SOURCE_FACTORIZATION__ENDO_FUSES_EXTERNAL_AND_INTERNAL_SPIN_AND_KILLS_FACTORISED_SIMULTANEOUS_PS_PARTNER_CUSTODY__NO_PHYSICAL_SELECTION
target_claim: "INTERNAL/source-custody conditional. Given SA-1's already-built soldered P_H bundle and its two still-live Lorentz embeddings, classify the exact F, M_3, internal-144, and 16/144 partner packages under each embedding. No GU source claim is adjudicated."
target_claim_verdict: "Under so(1,3)_H, the internal so(6,4) modules are Lorentz-inert and the source's external-Weyl/internal-partner factorization is preserved. Under so(1,3)_endo, external and internal actions compose diagonally: F has no pure Weyl submodule, both unique PS owner lines move in rank-three boost orbits, and the graph-invariance implication uses the exact rank-45 span k_PS + [delta(so13),k_PS], so HE-3's zero D5 singlet implies zero simultaneous PS-plus-endo invariants in 16 tensor 144. This excludes factorized simultaneous source custody on the endogenous horn; it does not exclude a different non-PS fully mixed intertwiner and does not select which embedding is physical."
canon_verdict_change: none
priority_change: "Within SOLDERED-AD, prioritize the action-owned embedding selector only after an action lane owns it; stop further factorized PS-owner searches on the endogenous horn."
steering_effect: conditional_path_reprioritization_only
canonical_effect: pending_integration
rows_advanced: 0
fork_assumed:
  - CARRIER-SPLIT
  - SECTION-VS-OBSERVERSE
fork_classified:
  - id: SOLDERED-AD
    horn_compatible_with_factorized_source_package: "so(1,3)_H"
    horn_incompatible_with_factorized_simultaneous_PS_partner_custody: "so(1,3)_endo"
    physical_selection: open_action_owned_gate
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - lab/active-research/joe-directed/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-two-ps-channels-have-distinct-upstairs-owners-2026-08-16.md
  - lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/process/path-dependencies.md
scripts:
  - tests/channel-swings/joe_directed_sa2_two_lorentz_source_package_classifier.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`.** This artifact compares two
> representations of the same source-native soldered bundle. It uses no
> conventional family index, net-chirality obstruction, Higgs/VEV, `126`,
> anomaly, or vector-mass result. Its statements about Weyl type classify an
> intermediate representation only; they are not a net-chirality verdict.
>
> The routing registry is intentionally not edited here. Registration is an
> integration write and, under the method's registration discipline, occurs
> only after the artifact is committed and confirmed inside derived scope.

# SA-2 — two Lorentz embeddings, one exact source-package discriminator

## Result in plain language

The already-soldered bundle contains two genuinely different candidates for
what “four-dimensional Lorentz spin” means. They are not interchangeable.

Under the **block embedding** `so(1,3)_H`, Lorentz acts on the explicit
four-dimensional spinor factor and commutes with the internal `so(6,4)`.
Weinstein's source package therefore keeps its advertised shape: an external
Weyl-labelled factor tensored with a separate internal `16` or `144` partner.

Under the **endogenous embedding** `so(1,3)_endo`, the same frame rotation also
acts internally through SA-1's `delta`. The external and internal spin labels
fuse. Exact branching shows that the source imposter carrier `F` then contains
no pure `(1/2,0)` or `(0,1/2)` Lorentz submodule. More decisively, each of
HE-4's two exact Pati--Salam owner lines (`54` and `210`) moves under the three
endogenous boosts. If a tensor is fixed by both the endogenous graph and PS,
it is fixed by `[delta(so(1,3)), k_PS]`; the exact span of those commutators
with `k_PS` has rank `45`, all of `so(6,4)`. HE-3 already proves that
`16 tensor 144` has no `D5` singlet.
Consequently it has no simultaneous `PS + so(1,3)_endo` invariant either.

That is a structural incompatibility with the source's **factorized,
simultaneous PS-partner custody** on the endogenous horn. It is not a theorem
that the block embedding is physical. A different, fully mixed, non-PS
endogenous intertwiner remains logically possible, and selecting the observed
Lorentz embedding remains owned by the unbuilt action.

## 1. Conditional-build boundary

This wave begins after SA-1. It assumes the source-defined associated bundle
`P_H` is already soldered and asks only how two admitted subalgebras act on
already-owned carriers. It does **not** build or infer:

- an action, source action, background, vacuum, or external datum;
- a coefficient, family row, family index, scale, or selector;
- a global quotient, analytic domain, spectrum, or observed-state map;
- a deletion of either K77 half or any of the four corners; or
- the action-owned condition `D_varpi chi_epsilon = 0`.

The two horns are therefore labels for conditional representation theorems:

```text
H_LOR = H       : block so(1,3)_H, commuting with internal so(6,4)
H_LOR = ENDO    : graph so(1,3)_endo = {(X, delta(X))}
```

No sentence below converts either horn into a physical choice.

## 2. Archaeology and prior art

The light prior-art scan found that the required ingredients already existed,
but had not been composed:

1. **SA-1** built the two subalgebras exactly. They intersect in zero;
   `so(1,3)_H` commutes with `so(6,4)`; and the largest PS subspace invariant
   under `so(1,3)_endo` has dimension zero, versus all `21` under the block
   embedding.
2. **N5/SA-1 representation work** supplied the reconstruction-grade half-spin
   restriction that this certificate now recomputes exactly.
3. **CR-B** fixed the carrier as both K77 halves and all four corners rather
   than one selected Weyl corner.
4. **HE-3** supplied the exact four-corner `16/144` orientation ladder and the
   zero full-`D5` invariant in each relevant product.
5. **HE-4** identified two distinct unique PS owner lines, one in `54` and one
   in `210`, inside `16 tensor 144`.
6. **RSC-1** distinguished the gamma-trace `F`-shaped submodule from the
   internal gamma-traceless `144` and from the larger `Z` sector.
7. The **source extraction and conditional read packet** preserve the
   representation-origin `2+1`, the imposter/partner distinction, fundamental
   nonchirality, and the fact that observed chirality is still emergent.

**Novelty here:** the exact restriction of all these packages under both live
Lorentz embeddings; the source equation-(12.22) to equation-(11.6) `F`
crosswalk; exact endogenous restrictions of the `45`, `54`, and `210` owner
summands; direct motion of both unique PS owner lines; and the closure argument
turning HE-3's `D5` zero into a simultaneous `PS + endo` zero.

## 3. Ten-lens preflight

| Lens | Cheapest question | Result used |
|---|---|---|
| source-fidelity reader | Are `F`, `M_3`, and internal `144` the same object? | No; preserve all three provenances. |
| representation theorist | How do `10`, both `16` halves, and `144` restrict? | Exact doubled-weight branching, not a dimension analogy. |
| bundle geometer | Do the embeddings act on different bundles? | No; two subalgebras of one soldered `P_H`. |
| Clifford algebraist | Does the internal half-spin label survive restriction? | Both internal halves restrict equally under `endo`; do not delete either. |
| four-corner custodian | Can one corner stand for the carrier? | No; retain `nu_+`, `nu_-`, `zeta_+`, `zeta_-`. |
| chirality skeptic | Does absence of a Weyl submodule prove a chirality no-go? | No; it classifies this intermediate carrier only. |
| invariant theorist | Can either exact PS owner line be simultaneous `endo`-fixed? | No; both have rank-three boost orbits. |
| Lie-closure auditor | What does simultaneous graph and PS invariance actually imply? | It implies invariance under `[delta(so(1,3)),k_PS]`; that span with `k_PS` has rank 45. |
| provenance auditor | Does carrier isomorphism identify source roles? | No; `F^(12.22)` and graded `F_+/-^(11.6)` retain distinct source custody. |
| hostile scope reviewer | What is the strongest conclusion that survives? | Kill factorized simultaneous PS custody under `endo`, not all endogenous intertwiners and not the physical horn. |

The most efficient route was therefore one exact character certificate plus a
small rational-matrix orbit/closure certificate. Constructing an action or
choosing a state would answer a different and currently off-limit question.

## 4. Notation and exact branching theorem

All pairs `(a,b)` below are **doubled** Lorentz highest weights:
`(a,b) = (2j_L,2j_R)`. Their dimensions are `(a+1)(b+1)`. In particular,
ordinary Weyl notation `(1/2,0)` and `(0,1/2)` becomes doubled notation
`(1,0)` and `(0,1)` in these tables.

### 4.1 Internal carriers

Under `so(1,3)_H`, the internal `so(6,4)` factor is inert:

```text
10  -> 10 (0,0)
16+ -> 16 (0,0)          16- -> 16 (0,0)
144+ -> 144 (0,0)        144- -> 144 (0,0)
```

Under `so(1,3)_endo`, exact restriction gives:

```text
10 -> (2,2) + (0,0)

16+ -> (3,1) + (1,3)
16- -> (3,1) + (1,3)

144+ = 144- ->
  2[(1,1) + (1,3) + (3,1) + (3,3)]
  + (5,1) + (5,3) + (1,5) + (3,5).
```

The equality of the two half-spin restrictions is a branching fact. It is not
permission to identify, discard, or conjugate away either K77 half.

### 4.2 The source imposter `F` and the equation crosswalk

The source extraction gives the ungraded equation-(12.22) carrier

```text
F_imp^(12.22) = S-slash(TX) tensor S-slash(N)
              = (2+ + 2-) tensor (16+ + 16-).
```

Equation (11.6) partitions its four tagged summands exactly and disjointly:

```text
F+ = (2- tensor 16+) + (2+ tensor 16-)
F- = (2+ tensor 16+) + (2- tensor 16-).
```

Each has dimension `64`; together they exhaust the `128`-dimensional imposter
carrier. Under `so(1,3)_H`, each graded sector retains the factorized type

```text
F+|H = F-|H = 16(1,0) + 16(0,1).
```

Under `so(1,3)_endo`, each restricts instead as

```text
F+|endo = F-|endo =
  (4,1) + (3,2) + (2,3) + (1,4)
  + (3,0) + (2,1) + (1,2) + (0,3).
```

The dimension is again `64`, but the multiplicities of `(1,0)` and `(0,1)`
are exactly zero. The ungraded `128` is likewise Weyl-submodule-free under
`endo`.

This carrier equality does not collapse source roles. `F_imp^(12.22)` remains
the imposter referent; `F+/-^(11.6)` remain graded sector labels. Likewise,
RSC-1's gamma-trace `F`-shaped `128` inside the internal vector-spinor package
does not identify the source imposter with the internal gamma-traceless `144`.

### 4.3 The internal `144` partner and `Z`

Under the block embedding each graded `Z` sector keeps

```text
Z+|H = Z-|H = 144(1,0) + 144(0,1),             dim = 576.
```

Under the endogenous embedding each conjugate sector has the same exact
22-type restriction:

```text
4[(3,2)+(2,3)+(2,1)+(1,2)]
+3[(4,3)+(3,4)+(4,1)+(1,4)]
+2[(5,2)+(2,5)+(3,0)+(0,3)+(1,0)+(0,1)]
+  (6,3)+(5,4)+(4,5)+(3,6)
+  (6,1)+(1,6)+(5,0)+(0,5).
```

Unlike `F`, `Z` retains exactly two copies each of `(1,0)` and `(0,1)` under
`endo`. This contrary control matters: the theorem is not the false universal
claim that endogenous composition removes every Weyl type everywhere.

### 4.4 `M_3` is multiplicity, not the imposter and not the partner

`M_3` is the abstract three-dimensional family-multiplicity space in the
source packet. It is neither `F` nor the internal `144`. No Lorentz action on
`M_3` is derived here. If it is carried as inert multiplicity, it merely
triples the restriction of the attached `16`; tripling cannot create a Lorentz
type absent from the underlying summand. No ordinary family index, row, or
imposter-to-partner alignment follows.

## 5. The complete `16 tensor 144` partner package

The source-native `D5` owner decomposition is

```text
16 tensor 144 = 45 + 54 + 210 + 945 + 1050,          dim = 2304.
```

Under `so(1,3)_H`, all five internal summands remain Lorentz-inert. Under
`so(1,3)_endo`, the certificate restricts the full product to 22 doubled-weight
types:

```text
(8,4) + 2(6,6) + (4,8)
+2(8,2) + 6(6,4) + 6(4,6) + 2(2,8)
+(8,0) + 8(6,2) + 14(4,4) + 8(2,6) + (0,8)
+4(6,0) + 17(4,2) + 17(2,4) + 4(0,6)
+8(4,0) + 20(2,2) + 8(0,4)
+9(2,0) + 9(0,2) + 4(0,0).
```

For the three owner summands needed by the custody test:

```text
45|endo  = (4,2)+(2,4)+(2,2)+(2,0)+(0,2)

54|endo  = (4,4)+(4,0)+(0,4)+2(2,2)+(0,0)

210|endo = (6,2)+(2,6)+(6,0)+(0,6)
          +2[(4,4)+(4,2)+(2,4)]
          +(4,0)+(0,4)+3(2,2)+(2,0)+(0,2)+(0,0).
```

These restrictions type the ambient summands. They do not by themselves say
where HE-4's unique PS lines sit inside the displayed Lorentz irreducibles;
that is supplied directly by the rational orbit calculation next.

## 6. Exact owner motion and the closure theorem

In SA-1's rational `(6,4)` adapted basis, let `D` be the internal form. The
unique PS line in `54` is represented by

```text
q_54 = 2 D_A - 3 D_B,
```

which is `D`-traceless and fixed by all `21` PS generators. The unique PS line
in `210` is represented by the oriented four-form

```text
phi_210 = vol(B_4).
```

It is also PS-fixed. Their exact orbit ranks are:

| owner line | under `so(1,3)_H` | under `so(1,3)_endo` | moving generators |
|---|---:|---:|---|
| `q_54` | `0` | `3` | the three boosts |
| `phi_210` | `0` | `3` | the three boosts |

Thus neither exact PS owner is a simultaneous endogenous-Lorentz scalar.

There is a stronger owner-independent proof, but its implication must be typed
through the **graph** action. Let `G_X = X_ext + delta(X)` be an endogenous
Lorentz generator and let `A` lie in `k_PS`. If a tensor `v` is fixed by every
`G_X` and every `A`, it is fixed by their commutator. The external Lorentz
action commutes with the internal PS action, so

```text
[G_X,A] v = [delta(X),A] v = 0.
```

The certificate directly finds

```text
rank( k_PS + [delta(so(1,3)), k_PS] ) = 45 = dim so(6,4).
```

Therefore any tensor fixed by both PS and endogenous **graph** Lorentz is fixed
by full `D5`. HE-3's exact product certificate gives

```text
Inv_D5(16 tensor 144) = 0.
```

Hence

```text
Inv_(PS + so(1,3)_endo)(16 tensor 144) = 0.
```

This conclusion includes possible compensation among the external Lorentz
factors already present in the source package: simultaneous invariance under
the graph generators plus PS forces invariance under their generated internal
algebra. It does not transfer to a construction that abandons PS custody and
uses a different fully mixed intertwiner.

## 7. Four corners and chirality ceiling

The computation retains both ambient K77 halves and the four observed slots
`nu_+`, `nu_-`, `zeta_+`, `zeta_-`. Both internal `16` halves restrict equally,
and the conjugate `Z` sectors also restrict equally, but this is not a corner
identification. Equation-(9.16)'s bars and unbars remain independent.

Weinstein's target is representation-origin `2+1`: two true-family sectors and
an imposter/remainder sector inside a fundamentally nonchiral total carrier,
with observed chirality intended to emerge only after observation and later
reduction. SA-2 does not replace that mechanism with an ordinary three-family
index or net-chirality test. “`F|endo` has no Weyl submodule” means exactly what
it says at this intermediate representation layer and nothing more.

## 8. Kill, survive, and reopen rules

### Killed on the endogenous horn

- A factorized reading in which source `F` remains an external Weyl factor
  tensored with a separately custodial internal spinor.
- Either HE-4 unique PS line as a simultaneous endogenous-Lorentz scalar.
- Any simultaneous PS-plus-endogenous invariant in `16 tensor 144`.
- Repeating the carrier through inert `M_3` as a repair for an absent type.

### Survives

- The block horn as an exact structural realization of the source's
  external-spin/internal-partner factorization.
- Both K77 halves, all four corners, fundamental nonchirality, and the
  emergent-observed-chirality target.
- A non-PS, fully mixed endogenous intertwiner not factorized through the two
  known owner lines.
- The action-owned physical selector between `so(1,3)_H` and
  `so(1,3)_endo`.

### Reopen trigger

Reopen endogenous partner custody only with an already-owned source-native map
that (i) is typed on the full four-corner carrier, (ii) does not assume
simultaneous PS invariance, (iii) explicitly intertwines the endogenous graph
action, and (iv) preserves the imposter/partner provenance distinction. Do not
reopen merely with a conventional chirality, Higgs, family-index, or `126`
comparator.

## 9. Hostile-review ceiling and reprioritization

The strongest hostile objection is that a representation-theoretic
compatibility theorem cannot choose the observed symmetry of an unbuilt
action. Accepted. The theorem intentionally stops one layer earlier.

The next path priority is therefore:

1. **Bank this exact discriminator.** Do not spend further conditional-build
   cycles searching for a factorized simultaneous PS owner under `endo`.
2. **Keep the block horn live but conditional.** Its structural compatibility
   is not physical evidence until the action-owned invariance gate is built by
   its own lane.
3. **Allow one sharply typed endogenous escape only if new prior art appears:**
   a non-PS fully mixed intertwiner satisfying the reopen trigger above.

Fertility is **9/10 as a conditional closure**: it cheaply removes a broad
class of repeated partner-custody searches and identifies precisely what a
genuinely new endogenous proposal would have to supply. Fertility is **0/10
for physical selection** because that question remains outside this wave.

## 10. Reproduction

Run from the GU repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 tests/channel-swings/joe_directed_sa2_two_lorentz_source_package_classifier.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 tests/channel-swings/joe_directed_sa2_two_lorentz_source_package_classifier.py --selftest
```

Expected receipts:

```text
CERTIFICATE: 80/80 checks pass; mutation=none; no load-bearing float.
VERDICT: H_PRESERVES_SOURCE_FACTORIZATION__ENDO_FUSES_F_AND_KILLS_SIMULTANEOUS_PS_PARTNER_CUSTODY__NO_PHYSICAL_SELECTION
SELFTEST: clean baseline green before mutations
SELFTEST: 8/8 false routes caught via genuine [FAIL] lines
```

The probe replays HE-3's exact `23/23` dependency certificate before asserting
the closure consequence. It imports SA-1's rational matrix helpers with bytecode
disabled and writes no repository cache.
