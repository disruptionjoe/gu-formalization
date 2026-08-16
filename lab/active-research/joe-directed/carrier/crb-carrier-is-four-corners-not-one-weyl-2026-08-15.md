---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-15
work_item: CR-B
channel: carrier
target_claim: "INTERNAL — HE-2 §6, the contrary construction it named as the live attack: 'if GU's declared spinorial content is not a single ambient Weyl (or symplectic-Majorana-Weyl) spinor but a full ambient Dirac or non-Weyl Majorana object, then the ambient chirality tie of §3.3 never engages ... and n_g = 0 outright.'"
target_claim_verdict: "PREMISE REFUTED AS A DICHOTOMY, WITH A SOURCE-LAYER CORRECTION. The total field-space declaration is not a single ambient Weyl or symplectic-Majorana-Weyl spinor: it is an unsubscripted Dirac bundle printed in four corners. That does not erase the separate source-attested claim SC-GEN-55 that one effective generation is the pullback of a properly understood Weyl spinor, nor SC-GEN-56's package-to-three claim. The four corners partition into exactly two Z/4 class-homogeneous halves, and the criterion governing the bare pairing is ODD CENTRE-CLASS HOMOGENEITY, not single-Weyl-ness. On the total declaration the conventional n_g comparator has no chiral input; on a source-stated effective half it does. Which effective split is dynamically realized remains SG4 bit 2 and is not constructed here."
title: "CR-B: GU's total fermionic field space is four corners in an unsubscripted Dirac bundle, while the source separately describes one effective generation as a Weyl-spinor pullback. The governing bare-pairing invariant is odd Z/4 centre-class homogeneity, not carrier minimality. Computed: the four corners carry classes 3,1,1,3; exactly two 0-form/1-form pairings are class-homogeneous; and the source's opposite-half package is one of them. The result forbids only a bare mass: a class-2 bosonic insertion can recouple the halves, so the physical split remains conditional on SG4 bit 2."
grade: "EXACT integer/Z[i] arithmetic. Instrument 1: explicit Jordan-Wigner Clifford algebras over Z[i] carried as int64 real/imaginary pairs for 15 signatures, relations verified elementwise, antilinear intertwiners SOLVED for (eta read off, not assumed), Z[i] magnitude sweep max |entry| = 1 against a bound of 2^20 so no int64 overflow can hide. Ranks over F_p for three primes p = 1 mod 4 whose PRIMALITY IS CHECKED IN THE FILE (a composite modulus was caught corrupting a rank during the build and is now guarded); every rank SANDWICHED between the F_p lower bound and a codomain upper bound, so each is pinned exactly rather than probabilistically. Instrument 2: exact integer weight combinatorics in DOUBLED coordinates, class arithmetic mod 4, 2^7 weight enumeration for the tie. 179/179 checks, exit 0. No float is load-bearing anywhere; assert_no_float sweeps the whole result dict. NON-VACUITY three ways: 13 predeclared positive controls reproducing HE-2's banked reality table row-for-row plus its two horn rows (dim_R J-fixed set 64 on (7,7), 0 on (9,5)); TWO contrary controls, (9,5) where Majorana-Weyl provably does NOT exist and D_6/12 dimensions where the centre-class protection provably FAILS; and 13/13 planted false assertions each observed False. Failure path: 14/14 injected machinery mutations drive exit 1 under --selftest, which exits 0 on success. STANDARD REPRESENTATION THEORY throughout: mod-8 Clifford periodicity, the Z/4 grading of the D_n representation ring, -w_0 by weight-multiset negation. NOT: an index, a generation count, a physical carrier, a source action, a dynamical or VEV statement, a resolution of SIGNATURE-AMBIENT, or any claim-status movement."
disposition: TOTAL_DECLARATION_IS_FULL_DIRAC_FOUR_CORNER__ONE_WEYL_TO_ONE_EFFECTIVE_GENERATION_REMAINS_SOURCE_ATTESTED__PACKAGE_TO_THREE_REMAINS_SOURCE_ATTESTED__GOVERNING_BARE_PAIRING_INVARIANT_IS_ODD_Z4_CENTRE_CLASS_HOMOGENEITY__PHYSICAL_SPLIT_REMAINS_CONDITIONAL_ON_SG4_BIT_2
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/sources/source-claim-register.yaml
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/shiab-existence-cl95.md
  - explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md
  - explorations/p77-real-index-W1-builder-2026-07-19.md
  - papers/drafts/hardening-pass-2026-07-03/A3-enum-completeness-route-a-classification-attempt.md
  - lab/methods/source-native-comparator-routing.md
scripts:
  - tests/channel-swings/joe_directed_crb_carrier_admissibility.py
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
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY` — see §6, which separates the
> source-native leg (what the draft and the talks DECLARE the carrier to be,
> with loci) from the fork-1 comparator leg (whether a content is "vectorlike"
> and what `n_g` would be). Registration in
> `lab/process/source-native-comparator-routing-registry.json` is the method
> owner's call; the notice and classification string above are in the exact form
> `process_gates/source_native_comparator_routing_audit.py` requires.

# CR-B — four ambient corners and an effective Weyl-generation claim live at different layers

> [!CAUTION]
> **CORRECTION IV-20260815 — SOURCE LAYER.** The original framing below predicted
> that “one Weyl spinor” would turn out to be repository compression rather than
> a source claim. That prediction was false as a global statement. `SC-GEN-55`
> records Weinstein saying that one effective Standard-Model generation is the
> pullback of a properly understood Weyl spinor; `SC-GEN-56` separately records
> the full `Omega^0(S+) (+) Omega^1(S-)` package-to-three claim. The exact
> four-corner and centre-class calculations remain unchanged. Their correct use
> is to distinguish the **total ambient field-space declaration** from a
> **reduced effective-generation description**, not to reject the latter as
> unsourced.

## 0. The gate, verbatim

HE-2 (2026-08-15, 204/204) removed HE-1's Fence 4 and then named, in its own
hostile review, the attack it could not answer:

> **Strongest contrary construction available against HE-2.** Not a real form —
> Leg B forecloses that entire class of attack. The live one is a **carrier**
> attack: if GU's declared spinorial content is not a single ambient Weyl (or
> symplectic-Majorana-Weyl) spinor but a full ambient Dirac or non-Weyl Majorana
> object, then the ambient chirality tie of §3.3 never engages, the 4d
> left-handed content is `16 + 16 + 16bar + 16bar` [...] the sector is
> vectorlike, and `n_g = 0` outright.

and its weakest seam:

> HE-2 makes the subtraction rule real-form-stable; it does not supply its input.

This file executes that gate. **The premise is refuted as a dichotomy and the
consequent is confirmed as stated.** Both halves of that sentence are load-
bearing and neither is the headline on its own.

The brief asked whether the mathematics alone might decide the question cheaply,
because "if the mathematics permits only one carrier type, the source half may
not matter." **That route is closed, and §3.1 closes it by computation:** the
availability table is a function of `(p-q) mod 8` alone and it returns THREE
admissible carriers on horn A and THREE on horn B. Availability never forces a
carrier — a Dirac object is available in every signature. So the source half had
to be done, and it was.

---

## 1. Prior-art sweep, by mechanism — and the honest ratio

Swept by mechanism before a line of the probe was written (*symplectic-Majorana,
Majorana-Weyl, pseudo-Majorana, reality condition, Bott, mod 8, `(p-q) mod 8`,
charge conjugation, `B` matrix, quaternionic parity, centre class, Z/4 grading,
coordinate-sum class, chirality-coherent, `Omega^0(S_+)`, `Omega^1(S_-)`*), not
by label. **The great majority of the signature arithmetic in this file was
already banked, and is reproduced rather than re-derived.**

| Result | Owner | Status before CR-B |
|---|---|---|
| **13-signature Weyl-half reality table, `(p-q) mod 8` in {0,2,4,6} -> REAL/COMPLEX/QUATERNIONIC/COMPLEX, exact `Z[i]`** | HE-2 §3.1 + `tests/channel-swings/joe_directed_he2_real_form_reality_probe.py:260` | **exact — §3.1 reproduces all 13 rows** |
| **`(7,7)`: `sign(J^2) = +1`, Majorana-Weyl available, `dim_R` J-fixed set inside `S^+` = 64; `(9,5)`: `-1`, symplectic-Majorana-Weyl, `dim_R` = 0** | HE-2 §3.3 horn table | **exact — §3.1 reproduces both by an independent realification** |
| `Cl(7,7) = M(128,R)`, `Cl(9,5) = M(64,H)`, index `(9-5) mod 8 = 4` | `canon/shiab-existence-cl95.md` Step 2 | canon |
| `ABS_TABLE` real Clifford Morita class by `(p-q) mod 8` | `tests/majorana_weyl_forces_the_seven_seven_horn.py:64`, and two other test files verbatim | exact |
| Majorana-Weyl exists iff `p - q = 0 mod 8`; of the horns GU's 4+10 split reaches, only `(7,7)` qualifies | `tests/majorana_weyl_forces_the_seven_seven_horn.py` | exact |
| **`dim_C Hom_{Spin(p,q)}(S^+ (x) S^+, Lambda^0) = 0` for EVERY signature with `n = 2 mod 4`; `= 1` for `n = 0 mod 4`** | `explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md` | **exact — this IS §3.2's theorem, for the bare half-spinor** |
| `16^* = 16bar` "uses only weights (the `D5` diagram automorphism), *no signature* — it holds in *every real form*" | A3 Part D | exact |
| The `Z/4` centre of `Spin(10)` read off mod-4 coordinate sums (`16 -> 1`, `16bar -> 3`, `10 -> 2`, `144 -> 3`) | HE-1 §3.1, re-used as HE-2 Leg B's third route | **exact — this IS §3.2's method, at `D_5`** |
| `PH-K1-KINEMATIC`: the `Cl(9,5)` 128 block is kinematically vectorlike, `64+64`, both signatures | `explorations/chirality-grading-and-77-rerun-2026-08-03.md` | CONFIRMED |
| The four printed corners, `832±/64±`, `Spin(7,7)±` superscripts, eq (11.6), eq (12.20), eq (12.22) | `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` (SHA-256 pinned) | primary source |
| `S` UNSUBSCRIPTED at eq (9.16); `nu, nubar, zeta, zetabar` are **four distinct fields**; reality adjoint `SOURCE-SILENT` | `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` | primary source |
| **One effective generation is the pullback of a properly understood Weyl spinor** | `SC-GEN-55`, TOE `01:29:19`, with UCSD twin at `00:46:40` | source-attested; coexists with the total declaration |
| **The opposite-half `Omega^0(S+) (+) Omega^1(S-)` package is claimed to yield three generations** | `SC-GEN-56`, UCSD `00:32:46` | source-attested claim; mechanism not constructed |
| SG4 is the single open decider; the residual is 2 bits, bit 2 = "phase: chiral/unbroken vs massive/super-Higgs" | `canon/gu-forces-field-space-declaration-RESULTS.md` | canon |

**Honest ratio: Instrument 1 (§3.1) is ~85% reproduction of banked work — every
one of its 13 predeclared rows and both horn rows already existed. Instrument 2
(§3.2–§3.4) extends a banked `D_5` method and a banked `n = 2 mod 4` lemma to
`D_7` and to the 1-form slot, which is where the new content is. The source half
(§2, §4) is 100% cited from two SHA-pinned primary-source extractions and the
110-claim register; no new source reading is claimed.**

### 1.1 What is actually new here

1. **The five-carrier x eight-residue availability table** (§3.1). The repo banks
   `ABS_TABLE` (algebra Morita class), HE-2's Table B (Weyl-half reality type),
   and Majorana-Weyl at `s = 0`. It banks **no** general Majorana rule, **no**
   symplectic-Majorana rule, and **no** table listing all five conditions against
   all residues. §3.1 fills that named gap and proves the table is a function of
   `s` alone.
2. **The centre-class instrument at `D_7`, applied to the 1-FORM slot** (§3.2–3.3).
   The banked `n = 2 mod 4` lemma covers `S^+ (x) S^+`. GU's content is not a
   half-spinor; it is `Omega^0 (+) Omega^1` valued in one, and the form degree
   shifts the class by 2. That shift is the whole result and nothing in the repo
   computes it.
3. **The verdict that HE-2's fork is a false dichotomy**, with the third object
   exhibited and computed.
4. **A correction to the framing**: carrier availability is the wrong instrument.
   The 12-dimensional contrary control (§3.5) exhibits a signature where
   Majorana-Weyl EXISTS and the half-spinor is nevertheless SELF-DUAL.

---

## 2. Preflight — retrieval first, then five specialist lenses

**Retrieval ran before any construction.** Searches were issued for
`symplectic-Majorana`, `Majorana-Weyl`, `pseudo-Majorana`, `reality condition`,
`Bott`, `mod 8`, `carrier`, `centre class`, `Z/4 grading`, `coordinate-sum
class`, `chirality-coherent`, `Omega^0(S_+)`, `Omega^1(S_-)`, plus a full sweep
of `lab/sources/` for the declaration loci. §1 is that sweep's output and it is
stated at the top rather than in a footnote, per the standing eight-count
false-novelty correction. Two searches returned ZERO hits and those zeros are the
only places novelty is claimed: `chirality-coherent`/`centre-class` (no hits
anywhere) and the `Omega^0(S_+)` / `Omega^1(S_-)` OPPOSITE-half pairing (one hit,
`explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md:105`,
which carries all FOUR corners as a Krein domain, not as a chirality-coherent
pair). Zero hits from a substring search is not by itself evidence of novelty;
the positive evidence is that the two banked mechanisms (`D_5` centre class,
`n = 2 mod 4` scalar-vanishing) are each present and neither is applied to a
form-degree-shifted module.

**Lens 1 — real Clifford algebra / Bott periodicity.** *Route:* do not quote a
reality table; build `Cl(p,q)` over `Z[i]`, solve for the antilinear intertwiners
`B_eta`, and DERIVE the five availability bits from stated definitions
(`J^2 = +1` for Majorana, `J^2 = -1` for symplectic-Majorana, commuting with
chirality for the Weyl variants). *Prediction:* the answer will be a function of
`s = (p-q) mod 8` alone, and it will reproduce HE-2's 13 rows exactly, because
the invariant is Morita-theoretic and cannot see anything finer than `s`.
*Stake:* if any two signatures share `s` and disagree, the construction is wrong.

**Lens 2 — spinor reality by signature / supersymmetry carrier taxonomy.**
*Route:* the brief's hoped-for cheap decision is "the mathematics permits only
one carrier." That is a category error and this lens says so in advance: a Dirac
object is available in *every* signature, so availability is a lower bound on the
carrier zoo and never a singleton. The only way the mathematics could decide
cheaply is if it forbade the MINIMAL carrier, and even then "take the minimal
carrier" is a string/sugra selection principle GU does not declare. *Prediction:*
three carriers admissible on each horn; the cheap route dies; the source half
becomes mandatory. *Stake:* if any horn admits exactly one, this lens is wrong
and the file gets much shorter.

**Lens 3 — representation theory of the ambient group.** *Route:* "is it one Weyl
spinor" is the wrong question because it is not invariant under the operation
that actually matters — tensoring with the form degree. The invariant that IS
stable is the grading of the representation ring by `P/Q`, which for `D_n` with
`n` odd is `Z/4`. Compute the class of every declared corner. *Prediction:*
`cls(Omega^1(X)) = cls(X) + 2`, so the 0-form and 1-form slots are class-
compatible exactly when they carry OPPOSITE half-spinors. *Stake:* this predicts,
before looking, that the source's `+/-` assignment must be opposite if the source
means the content to be chiral.

**Lens 4 — source philologist.** *Route:* the register (`lab/sources/source-claim-register.yaml`,
110 claims, edition-pinned, `sha256:3f28d742...`) is the authority, not repo
prose. Read the DECLARATION loci (eq 5.2 p.31, eq 9.16 p.46) separately from the
GRADING loci (p.51, eq 11.6 p.52, eq 12.20 p.61), the EFFECTIVE-GENERATION locus
(`SC-GEN-55`), and the PACKAGE-TO-THREE locus (`SC-GEN-56`). *Corrected outcome:*
the declaration is unsubscripted and retains both halves, while “one Weyl
spinor” is independently source-attested at the reduced effective-generation
layer. *Binding condition:* every source sentence quoted with a locus; anything
the source does not say gets typed `SOURCE-SILENT` and stays there.

**Lens 5 — adversary / kill designer.** *Route:* design the failure before
computing. A "protection" verdict is worthless unless the instrument can see the
protection FAIL where it really fails. `-w_0 = id` exactly for `D_n` with `n`
even, so `D_6` — TWELVE dimensions — is a case where the half-spinor is genuinely
self-dual. Run it and require the instrument to return "not protected". Second
contrary control: `(9,5)`, where Majorana-Weyl provably does not exist, so the
Clifford instrument must return an exact real fixed-set dimension of **zero**.
Third: plant assertions false by construction and require each observed False.
Fourth: mutate the machinery and require every mutant to exit 1.

**Lens 6 — honesty auditor.** *Route:* this is the highest prior-art density
region in the repository and the standing correction is that eight false-novelty
claims were burned in one session. Grep the exact objects first; lead with the
ratio; and grade the swing by what is NEW, not by what is COMPUTED. *Binding
condition:* if a banked artifact already owns a leg, cite it in the results table
and do not re-claim it.

**Cheapest kill-or-switch, recorded before computing.** If `cls(Omega^0(S_+))`
and `cls(Omega^1(S_-))` differ, the source's own `+/-` assignment is not
chirality-coherent, the whole Instrument-2 line is dead, and this file reports
that instead.

**One credible contrary route, recorded before computing.** Odd class forbids a
BARE invariant bilinear. It does not obviously forbid one with a bosonic
insertion. If GU's declared bosonic content contains a class-2 object, the
protection is conditional rather than absolute and must be reported as such.
**It does** — §3.6 computes it, and that is the honest ceiling of this file.

---

## 3. The swing — exact results

Probe: `tests/channel-swings/joe_directed_crb_carrier_admissibility.py`,
**179/179 exact checks, exit 0**, `_local/cas-venv/bin/python`, run from the
repository root. Failure path: `--selftest`, **14/14 injected mutations exit 1**,
the selftest itself exiting 0 on success, plus 13/13 planted false assertions
observed False inside the run.

### 3.1 Instrument 1 — which carriers EXIST, and why this does not decide anything

Five conditions derived from stated definitions, on explicit `Z[i]` Clifford
algebras, 15 signatures:

```
  sig       s    Weyl half      admissible carriers
  ( 7, 7)   0    REAL           Weyl + Majorana, Majorana-Weyl                        <-- horn A
  ( 9, 5)   4    QUATERNIONIC   Weyl + symplectic-Majorana, symplectic-Majorana-Weyl  <-- horn B
  ( 5, 9)   4    QUATERNIONIC   Weyl + symplectic-Majorana, symplectic-Majorana-Weyl
  ( 6, 4)   2    COMPLEX        Weyl + Majorana, symplectic-Majorana                  <-- GU internal
  ( 4, 6)   6    COMPLEX        Weyl + Majorana, symplectic-Majorana
  (13, 1)   4    QUATERNIONIC   Weyl + symplectic-Majorana, symplectic-Majorana-Weyl
  (11, 3)   0    REAL           Weyl + Majorana, Majorana-Weyl
  ( 3, 1)   2    COMPLEX        Weyl + Majorana, symplectic-Majorana
  ( 1, 3)   6    COMPLEX        Weyl + Majorana, symplectic-Majorana
  ( 9, 1)   0    REAL           Weyl + Majorana, Majorana-Weyl
  ( 5, 5)   0    REAL           Weyl + Majorana, Majorana-Weyl
  ( 7, 3)   4    QUATERNIONIC   Weyl + symplectic-Majorana, symplectic-Majorana-Weyl
  ( 4, 0)   4    QUATERNIONIC   Weyl + symplectic-Majorana, symplectic-Majorana-Weyl
  (10, 0)   2    COMPLEX        Weyl + Majorana, symplectic-Majorana
  ( 6, 6)   0    REAL           Weyl + Majorana, Majorana-Weyl                        <-- CONTRARY B (12d)

  s=0 : Weyl, Majorana, Majorana-Weyl
  s=2 : Weyl, Majorana, symplectic-Majorana
  s=4 : Weyl, symplectic-Majorana, symplectic-Majorana-Weyl
  s=6 : Weyl, Majorana, symplectic-Majorana

  J-fixed real dimensions inside S^+ :  (7,7) -> 64,   (9,5) -> 0
```

Every row's Weyl-half type matches the value predeclared from `(p-q) mod 8`
before the run; rows for `(6,4)`, `(9,1)`, `(5,5)`, `(7,3)`, `(1,3)`, `(3,1)`,
`(4,0)`, `(10,0)`, `(7,7)`, `(9,5)`, `(5,9)` reproduce HE-2's banked table
row-for-row, and the `64`/`0` fixed-set dimensions reproduce HE-2's horn table by
an independent realification and a three-prime rank agreement. The table is
verified to be a **function of `s` alone**: no two signatures sharing `s` disagree.

**And this settles nothing about GU.** Each horn admits **three** carriers, and a
plain Dirac object is available in every signature. *"Y^14 admits a
Majorana-Weyl spinor"* is a true statement about `(7,7)` and is not a statement
about GU's field content. The brief's cheap route is closed by computation, not
by assertion. The interesting fact in the table is a NEGATIVE one, and it is the
first contrary control: **on horn B, Majorana-Weyl does not exist at all** — the
real fixed set inside `S^+` has dimension exactly `0`, pinned by an `F_p` rank
equal to the full `128` on three primes, so the absence is detected and not
merely unobserved.

### 3.2 Instrument 2 — the invariant that actually governs the tie

For `D_n` the representation ring is graded by `P/Q`. In DOUBLED integer weight
coordinates the class map is

```
    cls(lambda) = (sum of doubled coordinates)  mod 4
```

well defined because every `D_n` root has doubled-coordinate sum in `{0, +-4}`
(verified for `n = 4,5,6,7`), **additive** over `(+)` and **multiplicative** over
`(x)`. At `D_7`:

```
    cls(S^+) = 3      cls(S^-) = 1      cls(V) = 2      cls(ad) = 0
```

and all 64 weights of each half-spinor share one class, so the class is a
property of the module rather than of a chosen weight.

**The theorem.** A module `M` homogeneous of **ODD** class admits **no** invariant
bilinear form on `M (x) M`, because `cls(M (x) M) = 2 cls(M) = 2 mod 4 /= 0` and
an invariant requires the centre to act trivially. It is:

- **real-form BLIND**, for exactly HE-2 Leg B's reason — it is settled in the
  complexification that every real form shares;
- **signature BLIND**, because `Cl(p,q) (x) C` depends only on `p+q`, so both
  horns of SIGNATURE-AMBIENT complexify to the same `D_7`;
- **additive**, so it can be evaluated on a whole field content without
  decomposing it into irreducibles. That is what makes it usable here, and it is
  the property the banked `S^+ (x) S^+` lemma does not have.

The banked `explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md`
(`dim Hom(S^+ (x) S^+, Lambda^0) = 0` for every signature with `n = 2 mod 4`) is
the `k = 0` case of this and is cited, not re-claimed. The second, independent
leg — `-w_0` by weight-multiset negation — agrees on every rank tested.

### 3.3 The four printed corners, and which pairings are protected

The 2021 draft p.51 prints FOUR corners (`lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`
§2.1, SHA-256-pinned, rendered-page verified): `nu_+ in Omega^0(S_+)`,
`nu_- in Omega^0(S_-)`, `zeta_+ in Omega^1(S_+)`, `zeta_- in Omega^1(S_-)`.
Their classes, computed:

```
    nu_+   in Omega^0(S_+)    class 3
    nu_-   in Omega^0(S_-)    class 1
    zeta_+ in Omega^1(S_+)    class 1
    zeta_- in Omega^1(S_-)    class 3
```

The `1`-form index shifts the class by `cls(V) = 2`, so a `0`-form slot and a
`1`-form slot are class-compatible **exactly when they carry OPPOSITE
half-spinors**. Enumerating all four `0`-form/`1`-form pairings:

```
    nu_+ | zeta_+     classes (3,1)   homogeneous=False  protected=False
    nu_+ | zeta_-     classes (3,3)   homogeneous=True   protected=True    <-- L107
    nu_- | zeta_+     classes (1,1)   homogeneous=True   protected=True
    nu_- | zeta_-     classes (1,3)   homogeneous=False  protected=False
```

**Exactly two of the four are class-homogeneous, and both of those are ODD, hence
protected.** The verdict is invariant under global conjugation (swapping which
half is called `+` swaps classes `3` and `1`, both odd), so nothing here depends
on a sign convention — only on the two slots carrying OPPOSITE halves.

And the source declares one of the protected pairings, verbatim
(`papers/drafts/Transcript into the impossible.md:107`, verified at the locus):

> "if you pull back ordinary spinners, **zero forms valued in the positive
> spinners, direct sum one forms valued in the negative spinners** on that top
> space, you're gonna get three generations of standard model fermions"

The repository's own shorthand — `nu in Omega^0(S)`, `zeta in Omega^1(S)`, the
same unsubscripted `S` in both slots — is faithful to eq (9.16) when `S` is read
as the full Dirac bundle. But when it is read as *the same Weyl half twice*,
which is how HE-2's contrary construction reads it, it names the ONE pairing that
is class-MIXED. That reading carries the vectorlike answer inside it.

### 3.4 The tie, computed — and the source's own eq (12.20) reproduced

Splitting the seven `D_7` coordinates as `2 + 5` and reading the tie off the
`2^7` weights:

```
    ambient S^+ :  (4d-L, internal class 1) x 32    (4d-R, internal class 3) x 32
    ambient S^- :  (4d-L, internal class 3) x 32    (4d-R, internal class 1) x 32
```

Each ambient half is a **two-term chirality-CORRELATED sum**: restricted to 4d
left-handed, a single ambient half sees only ONE internal class. That is the tie.
The full ambient Dirac object sees **both**, and the tie is broken. This
reproduces the source's own display, eq (12.20), p.61, verbatim:

> `ג∗(S̸⁶⁴_L(TY)) = (S̸²_L(TX) ⊗ S̸¹⁶_L(Nג)) ⊕ (S̸²_R(TX) ⊗ S̸¹⁶_R(Nג))`
> — overbraced *"Luminous Light Standard Model Family Matter"*
> `ג∗(S̸⁶⁴_R(TY)) = (S̸²_L(TX) ⊗ S̸¹⁶_R(Nג)) ⊕ (S̸²_R(TX) ⊗ S̸¹⁶_L(Nג))`
> — underbraced *"Dark Decoupled Looking Glass Matter"*

The `4+10` split used here is the source's own pullback along a section,
`ג∗(T∗Y) = T∗X ⊕ Nג` (eq 11.5 p.51, eq 12.19 p.61). **It is not Kaluza-Klein
and nothing here compactifies anything** — the source disavows compactification
in the same breath (`Transcript into the impossible.md:104`: *"You don't have to
compactify because you're not in a situation with a random space. You've got a
bundle."*). `Y^14` is endogenous throughout.

### 3.5 The two contrary controls

**CONTRARY A — a carrier type that provably does not exist.** On `(9,5)`,
Majorana-Weyl does not exist: the real dimension of the `J`-fixed set inside
`S^+` is exactly `0`, from an `F_p` rank of `(J-1)|_{S^+}` equal to the full
`128` on three independent primes, against `64` for `(7,7)` from the same code
path. The machinery detects ABSENCE, not merely fails to detect presence.

**CONTRARY B — a case where the centre-class protection provably FAILS.** In
**TWELVE** dimensions (`D_6`), `-w_0 = id`, the half-spinor weight multiset is
closed under global negation, and `cls(S^+) = 2` is **EVEN**, so
`cls(S^+ (x) S^+) = 0` and a same-chirality invariant is ALLOWED. The instrument
returns "not protected" there. Rank parity across `D_4 ... D_7`:
`{4: False, 5: True, 6: False, 7: True}` — the mechanism is `D_n` rank parity
(equivalently `n = 2 mod 4` versus `0 mod 4` in the ambient dimension), and
**nothing about signature**.

**This control is the sharpest correction in the file.** `Cl(6,6)` has `s = 0`,
so **Majorana-Weyl EXISTS in 12 dimensions** — and the half-spinor is
nevertheless self-dual and admits a Majorana mass. So possessing the "most
chiral" available carrier does not deliver chirality. **Carrier availability is
the wrong instrument. Centre class is the right one.** HE-2's criterion
("a single ambient Weyl or symplectic-Majorana-Weyl spinor") is sufficient at
`D_7` and is **not necessary**, and it is not even sufficient in general — it
happens to work at 14 dimensions only because `14 = 2 mod 4`.

### 3.6 The honest ceiling of the certificate — computed, not asserted

Odd class forbids a **BARE** invariant bilinear. It does not forbid one with a
bosonic insertion: a singlet in `M (x) M (x) T` with `cls(M) = 3` requires
`cls(T) = 2`. Computed:

```
    cls(Lambda^k V) = 0 for k even, 2 for k odd
    End(Delta) = sum_k Lambda^k V   spans classes {0, 2}
    eps in Omega^0(ad P)          spans classes [0, 2]   -- CAN supply the insertion
    $ (varpi) in Omega^1(ad P)    spans classes [0, 2]   -- CAN supply the insertion
```

Both of GU's declared bosonic slots contain class-2 components (via the
odd-degree part of `ad P = End(Delta)`, and for the 1-form slot via the form
index as well). **So the certificate is CONDITIONAL, not absolute: a
class-homogeneous half is exactly chiral at zero insertion, and its chirality can
only be lost through a class-2 bosonic spurion.** No stronger claim is available
and none is made.

That conditional is not a weakness discovered here — it is the source's own
statement, and the class arithmetic is what makes it exact. Draft p.52,
immediately after eq (11.6) (`SC-CHI-01`):

> "the full operator depicted decouples effectively into two separate Dirac like
> operators, **when there is no vacuum expectation value pulling the various
> sub-fields of ϖ to values significantly above zero.** Thus we assert that a
> non-chiral total theory splits at the emergent level into two separate chiral
> theories"

---

## 4. The source half — what is declared, what is graded, what is silent

Every locus below is from the register (`lab/sources/source-claim-register.yaml`,
110 claims, edition-pinned, `sha256:3f28d742...`) or from a SHA-pinned extraction.

**DECLARED (the arena).** Eq (5.2), p.31 — the linearized `Omega^{0,1}_Y x {ad,
S̸}` table with naive spins `0, 1, 1/2, (1/2, 3/2)`; eq (9.16), p.46 (`SC-OP-04`),
verbatim: *"For nu, nu-bar in Omega^0(Y,S̸) and zeta, zeta-bar in Omega^1(Y,S̸) we
can begin with operators like:"*. **`S̸` is UNSUBSCRIPTED at the point of
declaration.** Portal/Oxford `01:21:48` fixes what it is: *"a 14-dimensional
manifold has Dirac spinors of dimension two to the dimension of the space divided
by two [...] So 2¹⁴ over 2⁷ is 128."* The gauge ladder agrees — `Spin(7,7) -->
SO(64,64) --> U(64,64)` (eq 3.19, p.22), the principal bundle carrying the full
`128`-complex Dirac representation. And `Transcript into the impossible.md:173`:
*"It's zero forms and one forms valued either in add or in the spinners, and
that's it."*

**DECLARED (the grading), and it keeps BOTH halves.** Draft p.51 prints four
corners with `Spin(7,7)^±` superscripts and `832±`/`64±` dimension subscripts
(`SC-FER-06`). Eq (11.6), p.52 prints
`F±_{1/2} = (2∓ ⊗ 16₊ ⊕ 2± ⊗ 16₋)`, `Q±_{3/2}`, `Z±_{1/2} = (2∓ ⊗ 144₊ ⊕ 2± ⊗ 144₋)`
for `Spin(1,3) x Spin(6,4)` — the tie of §3.4, printed, **and HE-1's `144` is
source-attested right there**. Eq (12.20), p.61 prints both ambient halves with
their luminous/dark braces and then says: *"requiring a different view of
chirality as both Left and Right handed spinors emerge from the branching rules
of **both Weyl halves** [...] Left handed spinors on Y do not remain exclusively
Left handed on X."*

**DECLARED (the non-chirality).** §12.9 title, p.60, verbatim: *"Chirality Is
Merely Effective and Results From Decoupling a Fundamentally Non-Chiral Theory"*.
Synopsis item iii, p.64. TOE 2025 `02:36:02` (`SC-CHI-50`): *"I don't think the
world is chiral. You know, you're in GU when your theory is not chiral."*

**SOURCE-SILENT, first class.** **No reality condition anywhere.** The 110-claim
register has no row for Majorana, real, quaternionic or symplectic-Majorana
structure; the word "Majorana" appears **zero** times in every Weinstein
transcript held in the repository. And the silence is *active*: the draft treats
`nu, nubar, zeta, zetabar` as **four distinct classical fields**
(`gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md:38`), with the
standing fence *"do not replace the bars by an adjoint before constructing a
reality condition"*. `SOURCE-SILENT` is the answer, and it is load-bearing: it
means **no reality condition may be imposed on GU's carrier by this file or any
other without declaring the imposition.**

**SOURCE-SILENT, second, at the declaration locus.** No **chirality restriction
on the total field space** is imposed there. The source separately describes
effective Weyl output, but does not construct the dynamical projection or
decoupling that would select it from the four corners.

### 4.1 The layer distinction

> **GU's declared fermionic content is NOT a single ambient Weyl or
> symplectic-Majorana-Weyl spinor.** It is `Omega^0 (+) Omega^1` valued in an
> UNSUBSCRIPTED `S̸` — the full `128`-complex-dimensional Dirac bundle of the
> chimeric bundle — printed as FOUR graded corners, with no reality condition
> or chirality projection imposed at that declaration locus.

This is a statement about the **total ambient field-space declaration**, not a
global denial that the source ever speaks of a Weyl carrier. `SC-GEN-55`
independently records the source's one-Weyl-pullback-to-one-effective-generation
claim, while `SC-GEN-56` records the opposite-half package-to-three claim. These
statements coexist because they refer to different layers: ambient content,
effective pulled-back generation, and full package output.

HE-2's antecedent is therefore true of the total declaration. On that total
content the classes are `{1, 3}`, the content is class-MIXED, and the bare
chirality tie does **not** engage. The shorthand **`n_g = 0`** is only the
conventional net-chirality comparator readout, not a source-native verdict and
not a contradiction of `SC-GEN-55` or `SC-GEN-56`. This is consistent with the
standing non-chirality of the total theory; nothing moves.

> **But HE-2's fork is FALSE.** It offered "a single ambient Weyl spinor" versus
> "a full ambient Dirac or non-Weyl Majorana object" as mutually exclusive global
> descriptions. The source uses the latter at the ambient declaration layer and
> the former at an effective-generation layer. The four corners partition into
> exactly **two** class-homogeneous halves; the source declares one such package
> at L107/`SC-GEN-56`, describes a one-Weyl effective generation at `SC-GEN-55`,
> and asserts the split at `SC-CHI-01`. The governing invariant
> is **odd centre-class homogeneity**, not single-Weyl-ness — and §3.5 exhibits a
> dimension where a Majorana-Weyl spinor exists and is nevertheless self-dual, so
> the two criteria are genuinely different.

### 4.2 The fork, with both horns computed

| | **HORN DECLARED** | **HORN EMERGENT** |
|---|---|---|
| what | the total content, `S̸` unsubscripted, four corners | one class-homogeneous half |
| source loci | eq (5.2) p.31; eq (9.16) p.46; p.51 four corners; §12.9 title p.60; synopsis iii p.64; TOE `02:36:02` | `SC-GEN-55` one-Weyl effective generation; `SC-GEN-56`/L107 package-to-three; draft p.51 corner pairing; `SC-CHI-01`; L158; §12.9 eqs (12.13)–(12.17) |
| centre classes | `{1, 3}` | `{3}` (or `{1}`) |
| homogeneous | **NO** | **YES** |
| protected (odd) | — | **YES** |
| chirality tie | does **NOT** engage | **ENGAGES** |
| 4d left-handed internal content | both classes: `16 + 16bar` | one class only |
| `n_g -> n_g - 1` | **no input; `n_g = 0`** | **has an input** |
| verdict on both `(7,7)` and `(9,5)` | identical | identical |

**Both horns are computed on both signature horns, and the `Z/4` verdict is
identical on `(7,7)`, `(9,5)`, `(5,9)`, `(11,3)` and `(13,1)`,** because the class
lives in `D_7`, the complexification all of them share. The Clifford instrument
DOES move with SIGNATURE-AMBIENT (`(7,7)` Majorana-Weyl, `(9,5)` symplectic-
Majorana-Weyl) and the class instrument cannot see the fork at all — that
independence is the result's robustness, and on horn B the symplectic doubling is
uniform, multiplying every class-3 summand alike, so it cannot change a class.

### 4.3 What would settle it — and it is already a named bit

The selector between the two horns is the decoupling, and the source states its
condition twice and builds it never:

- `SC-CHI-01`, p.52: *"when there is **no vacuum expectation value** pulling the
  various sub-fields of **ϖ** to values significantly above zero."*
- `Transcript into the impossible.md:158`: *"the fermionic extension gives you
  exactly three families of chiral fermions **if you have a decreased VEV in the
  total space taking a Dirac equation into two [Weyl] equations** because the
  mass is actually a variable."*

§3.6 shows what that condition is, exactly: whether a **class-2 bosonic insertion
is switched on**. And that is not a new open question. It is
`canon/gu-forces-field-space-declaration-RESULTS.md`'s **SG4 bit 2**, verbatim:
*"Bit 2 — phase: chiral/unbroken vs massive/super-Higgs (the 'mass is a variable'
modulus)."* The carrier question terminates on an already-measured register bit,
with both of its values now computed.

**Calibration, and it is the source's own.** `Transcript into the impossible.md:155`:
*"we wasted the seventies work because we wanted to avoid indefinite signature on
the killing form, and **I don't know what to do** because we're in a maximally
compact subgroup. We're **shielded experimentally** from understanding how nature
handles the indeterminacy of the killing form."* The source declares open
problems here; it does not supply mechanisms. `SC-CHI-01` is introduced as *"The
idea being explored here"*, the register types it as **hedged strength**, and the
draft twice flags the §12.9 decoupling as *"stylized"*. Nothing in this file
credits Weinstein with a mechanism he disclaims, and the words "Krein" and
"ghost" appear zero times in the source and zero times in the load-bearing part
of this artifact.

---

## 5. What this changes, and what it does not

| item | after CR-B |
|---|---|
| HE-2's named contrary construction, `route-alive, and upstream` | **ADJUDICATED.** Its antecedent is TRUE of the declared total content, and its consequent (`n_g = 0`) holds there. Its FORK is false. |
| HE-2's premise "a single ambient Weyl or symplectic-Majorana-Weyl spinor" | **REFUTED only as a description of the total declaration** (§4.1), explicitly retained as the source-attested effective-generation description `SC-GEN-55`, and **demoted as a bare-pairing criterion** (§3.5). |
| `n_g -> n_g - 1` | unchanged as a rule; now known to have an input on the emergent horn and NO input on the declared horn |
| `CURRENT-STATE.yaml:172` ("total theory explicitly non-chiral") | **CONFIRMED, with a mechanism and six loci.** It is now a computed centre-class statement, not only a quoted one. |
| `PH-K1-KINEMATIC` | unchanged and consistent: class-mixed content is vectorlike |
| `SC-CHI-01` (the split into two chiral theories) | **given an exact representation-theoretic realisation**: the two halves are exactly the two `Z/4` centre classes, and each is protected against a BARE mass. Still hedged in the source; still not built. |
| SG4 | unchanged as the decider. The carrier question is now typed onto **bit 2** specifically. |
| SIGNATURE-AMBIENT | untouched. This file is robust to it, which is not the same as deciding it. |
| Repository count `{1,3}`, `SC-GEN-53` | untouched |
| The repo's `nu in Omega^0(S), zeta in Omega^1(S)` shorthand | **flagged.** Faithful to eq (9.16) with `S` the full Dirac bundle; when read as the same Weyl half twice it silently selects the unique class-MIXED pairing. |

---

## 6. Comparator routing — which route does this bind?

`lab/methods/source-native-comparator-routing.md` fork 1 covers exactly this
boundary. The two halves must be reported separately.

**Source-native half — this BINDS.** *"GU's declared fermionic content is
`Omega^0 (+) Omega^1` valued in an unsubscripted `S̸`, with no reality condition
and no chirality projection"* is a statement about **what the source declares**,
carried entirely by SHA-pinned primary-source extractions and the claim register.
So is *"the four printed corners partition into exactly two odd-class-homogeneous
halves"*, which is a fact about `D_7` and GU's own printed field content, common
to both horns of SIGNATURE-AMBIENT. This is a **layer-separating structural**
result in the source-native register: it prevents HE-2 from treating the total
ambient declaration and the effective Weyl-generation claim as mutually
exclusive, and supplies the invariant that prices the bare pairing on each
layer.

**Comparator half — this does NOT bind.** *"vectorlike"*, *"net chirality"*,
*"`n_g = 0`"* and *"a generation"* are fork-1's conventional comparators. Under
the boundary's **symmetric** rule, a comparator result cannot advance a GU row in
either direction — so the `n_g = 0` reading on the declared horn is **not**
evidence that GU became less favourable, exactly as the emergent horn's
engagement is not evidence that it became more so. The source's total theory is
recorded as explicitly non-chiral by its own §12.9 title, and the open burden
there is a low-curvature luminous/dark decoupling, not a net-chirality target.

**Forbidden summaries, named so they are not written.** *"CR-B shows GU has no
fermions."* No — it shows the declared total content is class-mixed, which the
source itself asserts and calls a feature. *"CR-B shows GU is chiral."* No — one
horn's content is protected against a BARE mass only, §3.6 shows both declared
bosonic slots can supply the insertion that removes even that, and which horn is
operative is unresolved. *"The carrier is decided."* Partly: the DECLARATION is
decided; the OPERATIVE reading is SG4 bit 2. *"Weinstein derives emergent
chirality."* No — he asserts it, hedged, and says *"I don't know what to do"*
about the adjacent structural problem.

---

## 7. Postflight — inline hostile review, five lenses

**Lens A — smuggled-carrier auditor (the brief's named worry).** *Have I imported
a carrier assumption from conventional model-building that GU does not declare?*
Four candidates, checked one at a time.
(i) **Minimality** — "take the minimal spinor" is the string/sugra reflex and
would have handed me Majorana-Weyl on `(7,7)` for free. It is used **nowhere**;
§3.1 reports availability and then explicitly refuses to draw a carrier from it.
(ii) **Weyl projection** — never imposed; §4 records `SOURCE-SILENT` and §4.1
reports the declaration as unsubscripted.
(iii) **A reality condition** — never imposed. This is the sharpest trap in the
area, because the draft's four independent fields `nu, nubar, zeta, zetabar`
actively block it, and every antilinear involution in the repository is a repo
construction. Instrument 2, the one that carries the verdict, uses **no reality
structure at all**.
(iv) **"Vectorlike means no generations"** — this IS a comparator import, and it
is fenced in §6 rather than used. The computed object is "no invariant bilinear
form", which is pure representation theory; the step from there to "no mass, no
generation" is the comparator step and does not bind source-natively.
**One import survives and is declared:** treating the `4+10` split as the frame
in which "the tie" is evaluated. That is the source's own eq (11.5)/(12.19)
pullback along a section, not compactification, and §3.4 says so.

**Lens B — strongest overclaim available, and where it is refused.** *"The source
declares a chiral carrier at L107, so GU is chiral after all."* Refused on three
counts. First, L107 and `SC-GEN-55` are spoken-lecture claims describing reduced
output, not the draft's total field-space declaration. They are source evidence
at their own layer; eq (9.16) and p.51 govern the different ambient-declaration
question and print all four corners.
Second, even granting the L107 half, §3.6 shows the protection is conditional on a
class-2 insertion that both declared bosonic slots can supply. Third, the source
itself titles §12.9 *"...a Fundamentally Non-Chiral Theory"* — reading L107 as a
chirality declaration puts the source in contradiction with itself, whereas
reading it as **the emergent half after the split** makes both statements true at
once and is exactly what `SC-CHI-01` says. That reconciliation is the file's
actual contribution and it must not be inflated past it.

**Lens C — strongest contrary construction against CR-B.** Not the source
reading — that is doubly attested. The live one is **the differential**. GU's
content is not a module, it is a complex with a rolled-up Dirac/de-Rham/
Rarita-Schwinger operator, and a first-order `Spin`-equivariant operator
`Gamma(E) -> Gamma(F)` needs `cls(F) = cls(E) + 2`. Both summands of the
protected pairing have the SAME class, so **no first-order equivariant operator
connects them** — while the class-MIXED pairing is precisely the one that admits
it. If GU's operator between the `0`-form and `1`-form slots is first-order and
equivariant, the protected pairing cannot be the carrier of that operator, and
the two horns of §4.2 are not symmetric. The symbol-degree
constraint is **computed, not asserted**: the probe verifies that the Dirac
operator and `d` both satisfy `cls(F) = cls(E) + 2`, that the PROTECTED pairing
admits no such operator, and that the class-MIXED pairing is exactly the one that
does. **Classified: route-alive, adjudicated only at the level of the symbol
degree, NOT settled here** — a zeroth- or second-order operator, or a
connection-dependent non-natural one, evades the constraint, and GU's actual
operator is SG4's to supply. It is the
single cheapest next gate this file can name, it is bounded, and it is not
something I can settle without SG4's operator. Recording it plainly is the point.

**Lens D — weakest seam.** Two, in order of severity.
1. **The certificate is conditional and the condition is exactly the open
   mechanism.** §3.6 is honest about this and it is not a small caveat: "chiral at
   zero insertion" is a much weaker statement than "chiral", and the whole
   difference is the VEV the source hedges. Anyone reading only §3.3 will
   overstate this file.
2. **`cls(ad P)` is computed as `End(Delta) = sum_k Lambda^k V`.** That is right
   for `u(64,64)` as an `so(14)`-module, but GU's `ad P` carries a reality
   condition and the repo has an open fork on the total grading
   (`gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`, `G = (-1)^form
   . J` recorded as `CONSTRUCTION-SELECTED-RIVAL` colliding with the §11.2
   labels). The class SET `{0,2}` is unaffected by any reality condition, so §3.6's
   conclusion holds; but a finer statement about WHICH components carry class 2
   would need that fork settled. Residual risk: low, and confined to §3.6's
   phrasing rather than its verdict.

**Lens E — verdict-typing auditor.** The standing correction is that verdicts are
claim-indexed and misaimed critiques fail. So, precisely: this file does **not**
target `SC-GEN-53`, does not target any source claim, and is not a falsification
of GU. Its target is **HE-2 §6's own contrary construction** — a repository-
internal result — and the verdict is split: **antecedent CONFIRMED, consequent
CONFIRMED on the declared horn, FORK REFUTED, criterion DEMOTED**. Against the
source it is confirmatory in one place only (`SC-CHI-01` gains an exact
realisation) and silent everywhere else. A one-word summary of this file is
guaranteed to be wrong, which is why §4.1 states the decision in two paragraphs
with a "but" between them.

---

## 8. Claim ceiling

- **Exact, and load-bearing:** the five-carrier x eight-residue admissibility
  table and its dependence on `s = (p-q) mod 8` alone; the reproduction of HE-2's
  13-row reality table and both horn rows including `dim_R` fixed sets `64` and
  `0`; the `D_7` classes `cls(S^+) = 3`, `cls(S^-) = 1`, `cls(V) = 2`; the four
  corners' classes `3,1,1,3` and the fact that exactly two of the four pairings
  are class-homogeneous and both are odd; the odd-class no-invariant-bilinear
  theorem and its two independent legs; the tie decomposition reproducing eq
  (12.20); `cls(Lambda^k V)` and the class-2 insertion requirement; the `D_6`
  contrary control and the rank-parity mechanism.
- **Standard representation theory, claimed novel by nobody:** mod-8 Clifford
  periodicity; the Frobenius-Schur trichotomy; the `Z/4` grading of the `D_n`
  representation ring; `-w_0` and the diagram automorphism. The great majority of
  §3.1 was already banked (§1) and is cited, not re-claimed.
- **Source, quoted with loci, not interpreted:** eq (5.2) p.31; eq (9.16) p.46;
  p.51 four corners; eq (11.6) p.52; eq (12.19)/(12.20) p.61; eq (12.22) p.62;
  §12.9 title p.60; synopsis iii p.64; `Transcript into the impossible.md` lines
  104, 107, 155, 158, 161, 173; Portal `01:21:48`; TOE `02:36:02`.
- **GU-native only in the selection and the use:** which content is computed on
  (GU's four printed corners), which ambient group (`D_7`, from `Y^14 = Met(X^4)`),
  which two horns are swept, and what the answer is used to conclude about HE-2's
  named contrary construction.
- **NOT claimed:** an index; a generation count; that `n_g = 3`; that GU is
  chiral; that GU is not chiral; a physical carrier; a source action; SG4; a
  reality condition on GU's spinors (the source is silent and this file imposes
  none); a dynamical, VEV, mass-matrix, scale or threshold statement; a
  resolution of SIGNATURE-AMBIENT; a Kaluza-Klein reduction; that any experiment
  must see anything.
- **Claim-status movement:** none. `canon_verdict_change: none`. The count stays
  `{1,3}`. `SC-GEN-53` remains a typed seed. `canonical_effect:
  pending_integration`.

---

## 9. Did I decide the carrier, or relocate the question? — blunt

**I decided two of the three things and relocated the third, and the relocation
landed on a bit that canon had already named.**

*Decided, at the ambient declaration layer:* GU's total fermionic field space is
not a single ambient Weyl or symplectic-Majorana-Weyl spinor. The declaration
locus is unsubscripted, the draft prints four corners, and the source titles a
section *"...a Fundamentally Non-Chiral Theory"*. This does **not** make the
one-Weyl premise globally false: `SC-GEN-55` supplies it for one effective
pulled-back generation. Reporting the layer distinction is the main correction
to HE-2's dichotomy.

*Decided, and it is a correction:* the mathematics half does **not** decide the
carrier, and the brief's hoped-for cheap route is closed — not because the
arithmetic is hard but because availability is the wrong instrument. Three
carriers exist on each horn, and the 12-dimensional control shows that even
possessing Majorana-Weyl does not deliver chirality. The invariant that governs is
odd centre-class homogeneity. That instrument is new here, it is exact and
integer, and it is blind to both open forks. It is the file's actual contribution
and it is worth more than the signature sweep, which was mostly reproduction.

*Relocated, and I will not dress it up:* **how the total field space produces the
source's claimed effective Weyl generation and package-to-three output, I did not
decide.** The source declares all three layers — the non-chiral total, one
Weyl-pullback effective generation, and the split package — and conditions the
split on a VEV mechanism it hedges as *"the idea being explored here"*, flags as
*"stylized"*, and does not build. So the question moves to the selector. What
keeps this from being motion into fog is that the selector is not a new unknown:
§3.6 shows it is "is a class-2 bosonic insertion switched on", and that is SG4
bit 2 verbatim, which `canon/gu-forces-field-space-declaration-RESULTS.md`
already measured as one of exactly two residual bits. Both of its values are now
computed. The honest score is **two decided, one typed onto an existing bit with
both horns priced** — and a fourth thing found on the way out, in §7 Lens C, which
is that the two horns may not be symmetric once the differential's symbol degree
is taken into account. That is the next gate, and it is cheaper than this one was.
