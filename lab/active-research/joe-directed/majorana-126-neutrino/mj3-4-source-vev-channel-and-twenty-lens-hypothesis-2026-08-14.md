---
artifact_type: exploration
status: exploration
doc_type: source-targeted-gate-and-hypothesis-council
created: 2026-08-14
work_item: MJ-3 / MJ-4
channel: majorana_126_neutrino_mechanism
title: "MJ-3/MJ-4: the source's single declared VEV channel (spin-0 eps = internal adjoint 45) is ORTHOGONAL to the entire renormalizable fermion-mass sector -- 45 is absent from 16 (x) 16 for every direction. Only the 126 reaches the (nu_R,nu_R) entry; the 10 and 120 have it identically zero. Gauge exchange does reach the 126, but only as a dimension-six four-fermion operator, Fierz coefficient exactly -5/32. Twenty-lens council selects DIRAC-NEUTRINOS-FROM-OBSERVATION as the strongest hypothesis, falsifiable by neutrinoless double beta decay."
grade: "EXACT integer representation theory in Z[i] plus an exactly-verified Fierz identity (checked on all 16^4 = 65536 components after clearing denominators, not fitted). MJ-3 11/11, MJ-4 16/16. NOT: a source action, a vacuum, a condensate, a dynamical claim, a value for M_R, or any claim-status movement."
disposition: SOURCE_DECLARED_VEV_CHANNEL_ORTHOGONAL_TO_RENORMALIZABLE_FERMION_MASS__ONLY_126_REACHES_NU_R__GAUGE_EXCHANGE_REACHES_126_ONLY_AT_DIMENSION_SIX__DIRAC_HYPOTHESIS_SELECTED_AND_FALSIFIABLE
target_claim: SC-COS-01
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
  - canon/shiab-existence-cl95.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/channel-swings/joe_directed_majorana_126_fierz_probe.py
  - tests/channel-swings/joe_directed_majorana_source_vev_channel_probe.py
---

# MJ-3 / MJ-4 — the source's VEV channel, and the strongest hypothesis

## Source targeting first

MJ-2 asked which GU field could carry a 126 VEV using a generic Higgs framing.
That framing was checked against what the source actually says, and the check
sharpened the result rather than overturning it.

`lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md` records:

- the draft's three-way link, dispositioned `SOURCE-EXPLICIT`:
  **cosmological "constant" <-> spinless gauge field <-> fermion mass**, with
  the cosmological constant being the VEV of the field playing the role of
  fundamental mass;
- the pack's own construction prompt: test *"the source's **single** spinless
  gauge-potential/VEV channel as a common zero-order carrier for fermion mass
  and the cosmological sector"*;
- 2021 Into the Impossible `01:41:43`: which fields acquire VEVs, and where,
  is **not** selected by the source.

So the source declares exactly one VEV channel — the spin-0 part of the
ad-valued gauge potential `eps`, whose internal content is the adjoint,
`Lambda^2(10) = 45`. That is precisely the object MJ-2 computed, so MJ-2's
targeting was correct. It also makes a sharper test available.

Two readings of the link must be separated before testing:

- **R1 (direct):** the `eps` spin-0 VEV is itself the channel of the mass term.
- **R2 (scale):** the `eps` spin-0 VEV sets a scale that enters fermion mass
  through some other operator.

Only R1 is decided here. R2 is untouched and requires the operator.

## MJ-4 result — R1 is killed exactly

> **The 45 block on `16 (x) 16` vanishes identically for every one of the 45
> adjoint directions.** The whole even tower `{1, 45, 210}` is absent from
> `16 (x) 16`; the surviving renormalizable channels are exactly
> `{10, 120, 126}`.

So the source's single declared VEV channel is **orthogonal to the entire
renormalizable fermion-mass sector**. Under reading R1 the three-way link
cannot hold: an `eps` spin-0 VEV gives no fermion — Dirac or Majorana — a
renormalizable mass. Under R2 it may still hold, and nothing here touches that.

And on which channel can make `nu_R` Majorana:

| channel | `(nu_R, nu_R)` entry, over **every** direction |
|---|---|
| 10 | **identically zero** |
| 120 | **identically zero** |
| 126 | **reachable** (MJ-1: symmetric, rank one, SM-preserving) |

The 10 is still a live Dirac channel — nonzero on `16 (x) 16` overall, just
never on the `nu_R` diagonal.

## MJ-3 result — gauge exchange reaches the 126, but only at dimension six

`16 (x) 16bar = 1 + 45 + 210` and `16 (x) 16 = 10 + 120 + 126` are two bases for
the same three-dimensional space of so(10)-invariant four-fermion tensors. The
Fierz matrix relating them was solved over `Q(i)` and then **verified exactly on
all 65536 components** with denominators cleared — not fitted to the components
used to solve it. Rows, as coefficients on `[10, 120, 126]`:

```
  1 (singlet) : [ 1/16,  1/16,  1/32]
 45 (adjoint) : [27/16,  3/16, -5/32]
210           : [21/8,  -7/8,  5/16]
```

**`F[45][126] = -5/32`, nonzero.** GU's own gauge sector therefore reaches the
126 pairing channel — but as a *four-fermion* operator, i.e. at dimension six,
not as a VEV. Whether that operator condenses is dynamics, and the sign's
attractiveness depends on the overall coupling sign, which is action-gated and
unresolved (SG4). **No condensate is claimed here.**

An earlier version of this computation produced a different, wrong Fierz matrix
that satisfied the three components it was solved on and failed globally. It is
recorded because the global check is the only reason the error was caught, and
a locally-fitted Fierz matrix is a realistic way to publish a false coefficient.

## Twenty-lens hypothesis council

Each lens is charged to propose a route, not to comment on one. High-conviction
outliers are preserved even where they dissent from the synthesis.

1. **Clifford/representation theorist.** The chirality parity is the whole
   story: only odd `Lambda^k` survive on `S+ (x) S+`. Every even-channel VEV —
   including the source's — is structurally excluded from renormalizable mass.
   Route: stop looking for a scalar VEV; classify dimension-six operators.
2. **SO(10) GUT model-builder.** Standard SO(10) needs `126` (or a `16`-pair)
   for `M_R`. GU has neither. Route: ask whether a `16`-valued scalar exists in
   any SG4 completion; that is the cheapest standard repair.
3. **Pati-Salam / left-right specialist.** The `(10bar,1,3)` block is what
   breaks `SU(2)_R` and gives `M_R`. GU's breaking is `Spin(6,4) -> Spin(6)xSpin(4)`
   by *observation*, not by a Higgs in that block. Route: compute what the
   observation-induced breaking does to `B-L` — if `B-L` survives unbroken,
   Majorana mass is forbidden outright, which is stronger than "unreachable".
   **HIGH CONVICTION.**
4. **Neutrino phenomenologist.** Oscillations fix mass-squared splittings and
   need no Majorana mass. Dirac neutrinos are fully consistent with all
   oscillation data. Route: treat Dirac as the null, not the exotic option.
5. **Neutrinoless-double-beta experimentalist.** This is the decisive
   observable, and it is live now. Route: state the GU prediction as a
   falsifiable `0nubb` null and let experiment adjudicate. **HIGH CONVICTION.**
6. **NJL / dynamical-breaking theorist.** `F[45][126] = -5/32` is a real
   channel, but NJL condensation needs supercritical coupling. Route: compute
   the critical coupling for the 126 channel and compare to GU's gauge coupling
   at the relevant scale — a genuine, bounded calculation.
7. **EFT / operator-counting specialist.** Dimension-six `(nu nu)(nu nu)` gives
   `M_R ~ g^2 <nu nu> / M^2`; with no separate scale, `M_R` is tied to the
   condensate scale, not to a fundamental `M_R`. Route: this changes the seesaw
   prediction qualitatively and is checkable against M-H3's band.
8. **Lattice / strong-coupling skeptic.** Four-fermion channels that look
   attractive at tree level routinely fail to condense. Route: demand a
   nonperturbative criterion before any condensate claim. Dissents from any
   optimistic reading of MJ-3.
9. **Riemannian geometer.** `Y14 = Met(X4)`, internal 10 `= Sym^2(T*X4)`, and
   the tautological datum — the metric one observes at — is a **vector** in that
   10. A single vector spans no 5-form. Route: observation breaking is
   structurally a 10-direction phenomenon and can never reach `Lambda^5`.
   **HIGH CONVICTION — this is the load-bearing geometric point.**
10. **Gauge-bundle specialist.** `eps` and `$` exhaust the bosonic content, and
    both are ad-valued. Route: any 126 carrier must come from outside `ad`,
    i.e. from SG4, not from the declared table.
11. **Source-fidelity reader.** The source explicitly does not select a vacuum
    or VEV location. Route: any GU "prediction" of `M_R` is therefore
    unsupported at source grade regardless of the group theory — including
    M-H3's band, which is standard GUT arithmetic.
12. **Cosmological-constant specialist.** The same `eps` spin-0 VEV is supposed
    to carry `Lambda`. MJ-4 shows it cannot carry fermion mass under R1, so the
    three-way link *splits*: `Lambda` and fermion mass cannot share one
    renormalizable channel. Route: this is a genuine internal tension in the
    source worth reporting on its own. **HIGH CONVICTION.**
13. **Anomaly/index theorist.** `16` is anomaly-free in SO(10); adding a
    `126` scalar is safe, adding chiral fermions is not. Route: no anomaly
    obstruction either way — this lens returns a clean negative and should not
    be counted as support.
14. **Real-form / signature specialist.** Everything here is complexified
    internal structure; both SIGNATURE-AMBIENT horns share `Spin(6,4)`. Route:
    fork-robust, so the signature fork cannot be blamed for the negative.
15. **Conformal / scale-invariance specialist.** GU's trace-reversal and the
    DeWitt metric single out a conformal direction in `Sym^2`. Route: check
    whether the conformal (trace) direction of the 10 is the tautological one —
    if so the Dirac channel is further constrained to one direction.
16. **Seesaw taxonomist.** Type-I needs `M_R`; type-II needs an `SU(2)_L`
    triplet (also in the 126, also unreachable); type-III needs a fermionic
    triplet. Route: with 126 unreachable, *all three standard seesaws* close
    together — a much stronger statement than type-I alone.
17. **Flavor/texture specialist.** H28 already showed the surviving Yukawa
    couplings are free and ungraded. Route: even granting a Majorana block, GU
    supplies no texture, so no mass-ordering prediction follows.
18. **Philosopher of science.** A theory that forbids Majorana mass makes a
    sharper, riskier claim than one that permits it with free parameters.
    Route: the Dirac reading is the *more falsifiable* and therefore the more
    scientifically valuable hypothesis. **HIGH CONVICTION.**
19. **Adversarial referee.** Strongest overclaim available here is "GU predicts
    Dirac neutrinos". It is not earned: SG4 is open, so GU-as-stated is not
    GU-as-completed. The honest form is conditional on the declared field
    content. Rejects any unconditional phrasing.
20. **Honesty auditor.** Three separate things must not merge: the *channel*
    exists (MJ-1), the *carrier* does not (MJ-2/MJ-4), and the *dynamics* is
    untested (MJ-3). Route: keep them in separate rows forever.

### Synthesis — the strongest hypothesis

**H-DIRAC: within GU's declared field content and its own observation-based
breaking, neutrinos are Dirac, and every standard seesaw is closed.**

The support is convergent and exact, and each leg is independently certified:

- the observation datum is a **vector in the 10** (lens 9), and the 10's
  `(nu_R,nu_R)` entry is **identically zero over every direction** (MJ-4);
- the source's **single declared VEV channel is the 45**, which is **absent
  from `16 (x) 16` entirely** (MJ-4) — so it gives no fermion mass under R1;
- the only channel that reaches `nu_R` is the **126**, which has a **unique
  wedge home `Lambda^5`** and **zero multiplicity in every GU bosonic field**,
  tilted-group robustly (MJ-2);
- therefore type-I, type-II and type-III seesaw close **together** (lens 16),
  since all need the 126 or a field GU does not have.

**Falsifier, stated in advance:** an observation of neutrinoless double beta
decay. `0nubb` requires lepton number violation by two units and hence a
Majorana mass; H-DIRAC forbids one from GU's declared content. This is a real,
current, and adjudicable experimental test, which is why lens 5 and lens 18
both rate it above the internally-tidier alternatives.

**The one live escape, preserved:** H-CONDENSATE. `F[45][126] = -5/32` is
nonzero, so GU's gauge sector does reach the 126 as a dimension-six operator.
If that channel condenses, `nu_R` gets a dynamically generated Majorana mass
with no elementary carrier, and H-DIRAC fails. Lens 6 gives the bounded next
calculation (critical coupling versus GU's gauge coupling); lens 8 dissents and
expects it not to condense. This is the materially distinct minority route and
is deliberately not collapsed into the consensus.

**Second live escape:** SG4. Canon establishes that GU-as-stated does not force
a unique completion and that the field-space declaration is the open decider.
A completion may simply declare a 126 or a `16`-valued scalar (lens 2). H-DIRAC
is therefore a statement about GU-as-declared, never about GU-as-completed —
the referee's correction in lens 19, adopted.

**Reported separately as a source tension, not as a physics result:** the
three-way link `Lambda <-> spin-0 gauge field <-> fermion mass` cannot hold in
its direct reading R1, because the channel carrying `Lambda` is orthogonal to
all renormalizable fermion mass (lens 12). Either the link is the scale reading
R2, or the "fermion mass" in it is the carrier-bit mass of the `zeta` sector
rather than a Standard-Model fermion mass. Both readings remain open; this
artifact decides only R1.

## Next in-channel gate

MJ-5: compute the critical coupling for condensation in the 126 channel and
compare it to GU's gauge coupling at the breaking scale — the one bounded
calculation that separates H-DIRAC from H-CONDENSATE. A negative there
promotes H-DIRAC from selected to load-bearing; a positive reopens the
Majorana route without any new field.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
