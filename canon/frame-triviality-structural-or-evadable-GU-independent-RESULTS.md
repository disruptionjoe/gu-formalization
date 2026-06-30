---
title: "GU-independent: is the chiralizer's frame-triviality structural or evadable? REFINED NO-GO. Frame-triviality is EVADABLE -- the carrier's self-dual V-S entanglement gives a LINEAR operator O=L_SD(x)X_L that is BOTH net-chiral (+16=2^4) and frame-active (NET-SD +2), with NO extra ingredient (this CORRECTS canon's clean 'structural decouple'). But every such channel is 2-primary AND linear (index-conserving, non-forcing); the genuine ANTILINEAR loophole the index-conservation theorem leaves does NOT exist on this class (every antilinear candidate is chirality-reversing, carrier-leaking, or a gauge dressing with topological p_1=0). Net: an odd/order-3 count is NOT forceable by ANY operator (linear or antilinear) on the bare sector. GU's located-not-forced is a SPECIAL CASE of a class-level structural law. Forcing an odd count needs an EXTERNAL net-self-dual chiral background (int Ahat ch) -- natural (SM chirality / instantons / K3-CY) but an INPUT, and it still does not pin 3."
status: active
doc_type: result
created: 2026-06-29
grade: "computed + adversarially verified, with construct/verify DISAGREEMENTS productively resolved (the clean one-line 'orthogonal supports' metatheorem was reached-for by 2 constructs and REFUTED by 2 verifies, which found the counterexample O=L_SD(x)X_L via the carrier V-S entanglement). 9 agents, ~1.09M tokens (workflow wf_5eecfa73-d52). Decisive computations reproduced (O net-chiral +16 / frame-active NET-SD +2; antilinear escape collapse: gauge dressing continuous-to-0, p_1=0, identical +96; ||X_L||=2.0 SD / ~0 ASD). Honest caveats: two broad confirmatory searches (50k chirality-odd; 4k random frame-coupled) TIMED OUT under stdout buffering and are NOT relied upon; the verdict rests on the fully-reproduced decisive computations + the airtight linear backbone. No fabricated 3 (counts 16/32, 3-part=1); no fitted chiralizer (apparent escapes self-caught as gauge artifacts). This CORRECTS the canon 'clean decouple' (a 2-primary V-S cross-term exists) while STRENGTHENING the ultimate conclusion from GU-specific to a class-level structural law."
method: "GU-independent forcing workflow: 4 angles (structural metatheorem; hard antilinear escape hunt; non-GU source action; minimal ingredient) each genuinely TRYING to force three (steelman the constructive side) -> adversarial verify (refute both no-go and escape) -> synthesize."
depends_on:
  - canon/two-primary-lemma.md
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/carrier-dirac-mass-capstone-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - published-papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
---

# Frame-triviality of the chiralizer: structural or evadable? The GU-independent verdict

This reopens, GU-independently, the question the located-not-force campaign closed for GU: GU does not force a
chiral generation count because its antilinear chiralizer `C = J_quat . G = id_14 (x) U` is frame-trivial
(tangent-frame charge exactly 0.00), so it lands in the 2-primary selector arena and never reaches the
tangent-frame sector where the order-3 carrier lives. The forcing question is whether that frame-triviality is
a GU accident or a structural law. Four angles attacked it -- two adversarially defending a structural no-go,
two genuinely trying to CONSTRUCT a frame-non-trivial antilinear chiralizer that forces a count. Each construct
was then independently recomputed and adversarially refuted on the verified `Cl(9,5) = M(64,H)` 192-dim
`Lambda^2_+` j=1 carrier (Krein `+96/-96`, net chirality 0). The honest result is a refined no-go, not a clean
binary, and it is the deliverable.

## The verdict in one paragraph

Forcing an ODD / order-3 / exactly-three chiral generation count from inside a Clifford-RS sector is
structurally out of reach -- but the clean one-line "structural no-go" two of the constructs reached for is
NOT the reason, and is in fact false as stated. The sharp facts that survived independent adversarial
recomputation are these. (i) The naive trace-factorization argument -- "net chirality couples only to the
frame-trivial `id_V` trace component while frame charge couples only to traceless `so(4)`, orthogonal supports,
so no covariant operator can be both net-chiral and frame-active" -- holds on the full `1792`-dim space but
FAILS on the carrier, because the carrier projector entangles `V` (frame) and `S` (spinor) through
`J3 = id(x)sgen + lvec(x)id`. The carrier-projected chirality grading `G_P` therefore carries genuine self-dual
spinor content `X_L` (`||X_L|| = 2.000` on each self-dual frame generator, `~1e-14` on anti-self-dual -- the
asymmetry IS the `Lambda^2_+` direction). (ii) Consequently a covariant LINEAR operator that is BOTH net-chiral
and frame-active genuinely EXISTS: `O = L_SD (x) X_L` has frame charge `+2.0` (NET-self-dual), chiral trace
`+16`, and forces a chirally-imbalanced selected half of `+32`. So frame-triviality is evadable at the level of
"can a covariant operator couple chirality to the framing" -- yes, it can, through the carrier's own
self-dual `V`-`S` entanglement, with NO extra ingredient. (iii) BUT every such channel is 2-primary: the forced
quantities are `+16 = 2^4` and `+32 = 2^5`, 3-part computed `= 1`, no factor of 3 anywhere; and the operator
that achieves it is LINEAR, so it is caught by the index-conservation backstop (every linear Krein-isometry
conserves the net index at 0) -- its `+32` is a generic subspace-restriction artifact, not a forced index, and
the full carrier index stays exactly 0. (iv) The ONE genuine loophole the index-conservation theorem leaves
open -- a frame-non-trivial ANTILINEAR (AZ-CII) chiralizer -- was hunted hard and does NOT exist on this class:
every antilinear candidate is either chirality-reversing (net 0), carrier-leaking, or a gauge dressing
continuously deformable to the frame-trivial identity (connected stabilizer, topological `p_1 = 0`, forces the
identical vectorlike `+96`). Net: a 2-primary count is forceable for free, an odd/order-3 count is NOT forceable
by any operator -- linear or antilinear -- on the bare sector. GU's frame-trivial chiralizer is one instance of
a broader fact: nothing interior to a Clifford-RS sector of this class forces an odd chiral count. Forcing
three needs an EXTERNAL net-self-dual chiral background fed through the index / anomaly-inflow channel, and even
that does not by itself pin three.

## The numbers per angle

All counts and charges are COMPUTED on the substrate unless tagged analytic. Anchors reproduced everywhere:
`bare = 58.7215`, `C2 = 155.3625`, carrier dim 192, signature `(+96, -96)`, net chirality 0.

**Angle 1 -- structural meta-theorem (is every net-chiral antilinear op frame-trivial?).** Construct claimed
EVADABLE: built `O = L_SD (x) X_L`, computed (all on substrate) frame charge `fc = 2.000`, chiral trace
`+16 = 2^4` (3-part `= 1`), selected-half count `+32 = 2^5`, frame-trivial part of the count exactly `0`,
`||X_L|| = 2.000` on self-dual / `~1e-14` on anti-self-dual generators. Independent recomputation reproduced
every number exactly. **Adversarial refutation: the escape framing collapses (finding_confirmed = partial,
survives = false).** The index-conservation theorem's loophole is ANTILINEAR; the construct's `O` is NOT
antilinear and NOT Krein-isometric (`O^dag O = I` rel-dev `0.068`; `C = O.K` gives `C^2` rel-dev `~1.0` from a
scalar -- a clean AZ-CII would be `C^2 = +-1`; the construct itself reported `C^2` rel-dev `0.926`). Its
`+32` is not a conserved/forced index: the full carrier index stays exactly 0 under `O`, and frame-TRIVIAL
random Hermitian selectors also produce nonzero half-counts (`3.6, -1.8, -2.1, ...`), so `+32` is a
subspace-restriction artifact. With respect to the actual meta-theorem question, NO antilinear counterexample
was exhibited; the structural no-go for genuine antilinear chiralizers is un-refuted; the word "EVADABLE"
overclaims. No fabrication flags. **Escape did not survive.**

**Angle 2 -- hunt hard for the frame-non-trivial antilinear chiralizer.** Construct claimed STRUCTURAL no-go,
and the verdict CONFIRMED it (survives = true). Of 10 genuinely frame-active antilinear candidates, exactly one
family (`B = exp(theta * su(2)_+) . C_GU`) passed all proxy gates -- antilinear, `C^2 = -1`,
chirality-preserving, carrier-preserving (leakage `2.6e-13`), net-self-dual frame charge nonzero
(`+5.99/+14.79/+13.31` at `theta = 0.3/0.7/1.2`). Stage 2 demolished it as a gauge artifact (all computed):
(D1) its net-SD charge is CONTINUOUS in `theta` with `net-SD(0) = 0` -- a topological `p_1` is an integer and
cannot be tuned continuously to 0; (D2) it forces the IDENTICAL net count `96.0` as the frame-trivial baseline
(C-invariance `1.0000` for both) -- the vectorlike `+96` half, never a pinned integer; (D3) the whole net-SD
charge lives in the constant frame rotation `F` (`net-SD(C_GU) = 0.00`, `net-SD(F) = 18.35`), a connected-group
element, curvature-free, `p_1 = 0`. The independent pass WROTE its own from-scratch script and confirmed the
corrected mechanism: chirality is frame-blind (`Gamma = id_14 (x) omega`, every `so(4)` generator traceless,
`max|Tr L| = 0.00`), and every carrier-preserving frame rotation lives in a CONNECTED compact stabilizer
(`su(2)_-` frame / diagonal `su(2)_+`), hence deformable to identity with `p_1 = 0`. **Fabrication flags
(genuine defects, conclusion unaffected):** the construct MISREPORTED its own data, narrating candidates E/F as
"chirality-REVERSING (net 0)" when its own printout shows them chirality-PRESERVING (they actually fail on
carrier leakage `0.22-0.49`); and a mechanism overreach claiming the inside-slot route "provably destroys
net-chirality." Both corrected by the independent pass; the no-go SURVIVES.

**Angle 3 -- build a non-GU Clifford-RS source action and compute its count.** Construct claimed STRUCTURAL
no-go; verdict CONFIRMED (survives = true, no fabrication). Computed: every genuine chirality grading whose
trace IS the count is frame-trivial (volume/internal/base all factor `id_14 (x) gamma_S`, frame charge 0,
e.g. base grading `id_14 (x) g5b` gives net `-192` at frame 0); the RS-slash operators that DO carry frame
charge (`16, 48`) have net count exactly 0 and fail `Gamma^2 = 1`; the single frame-charged carrier grading,
the `Lambda^2_+` self-dual sign-lift (frame `6.928`), is exactly vectorlike (net 0); the apparent escape
`Rrot_base (x) (U om)` (operator frame `7.288`, net `+96`) is ILLUSORY -- its actual re-grading conjugates
`id_14` and cancels to frame charge `2.5e-16` (the construct caught this itself); the explicit source action's
chiral index is non-integer spectral noise (`+0.030` kinetic), no integer forced. The independent pass found a
genuine GAP (the construct's frame-charged slash gradings were built additively, breaking `Gamma^2 = 1`) and
tested the strongest un-tried object -- a grading CONJUGATED by an entangling frame-charged unitary,
`Gamma' = U (id_V (x) gamma) U^dag`, which automatically preserves `Gamma^2 = 1`. Result: frame-charged
(`frame = 6.000`) but net `Tr = 0.000` -- the escape COLLAPSES exactly as predicted. **No-go survives.**

**Angle 4 -- pin the minimal extra ingredient.** Construct claimed STRUCTURAL via a "one-line trace identity":
net chirality `= Tr(id_V (x) omega . Delta)` factorizes as `Tr_V . Tr_S`, so frame-active (traceless `so(4)`)
and net-chiral (`id_V` trace) supports are orthogonal. **Adversarial refutation (finding_confirmed = partial,
survives = false): the identity holds on the full `1792`-dim space but FAILS on the 192-dim carrier.** The
independent probe computed: tracing out `S` gives `Tr_S(G_P) = 0` (`~1e-14`) -- this is what lulled the
construct -- but the carrier-projected grading's S-side content along the SELF-DUAL frame generators is
nonzero (`||X_L|| = 2.0` SD vs `~1e-14` ASD). The interior covariant LINEAR operator `O = L_SD (x) X_L` is BOTH
net-chiral (`Tr(G_P . O_herm) = +16.0`, the construct's own metric) AND frame-active (NET-SD `+2.0`), with
`X_L` orthogonal to the bare grading `omega` (overlap 0 -- not circular). So the headline "no covariant
Clifford-RS operator can be both net-chiral and frame-active" is mathematically FALSE. The finding is only
PARTIAL, not fully overturned, because `O` is LINEAR -- it does not beat the index-conservation backstop, its
`+16` is a normalization-dependent overlap, not a forced index, and emphatically not 3. Part C (index /
anomaly-inflow, `int_X Ahat(R) ch(F)`) is honestly tagged analytic/textbook; it gives a nonzero chiral index
from a net-self-dual background but the value is a background input and does not pin 3. No fabricated number;
flags are mathematical overreach, not invented values.

## The minimal ingredient

Inside the bare Clifford-RS sector, forcing a NONZERO chiral count needs NO extra ingredient -- the carrier's
own self-dual (`Lambda^2_+`) `V`-`S` entanglement supplies a natural frame-active chiralizing operator
`O = L_SD (x) X_L` that forces `+32`. But that is a dead end for generations: it is LINEAR (index-conserving,
not a forced index), and it is locked to 2-primary (`2^5`, no factor of 3). To force an ODD / order-3 count the
operator route is provably insufficient -- every operator-level channel found, linear or antilinear, is
2-primary, consistent with the 2-primary lemma, and the genuine antilinear loophole does not exist on this
class. The minimal extra ingredient is then exactly one thing: a NET-SELF-DUAL (chiral) background curvature
coupled to the RS field through the index / anomaly-inflow channel `int_X Ahat(R) ch(F)`. This is NATURAL, not
contrived -- it is how chirality arises in every known chiral theory (the Standard Model's own chiral gauge
coupling, instanton zero modes, K3 / Calabi-Yau compactification index counts). The structural cost is honest:
it is EXTERNAL to the bare sector (a background input, not a carrier endomorphism), and even with it in hand,
getting exactly THREE requires additionally the order-3 boundary e-invariant (`e_R = -p_1/24 = 1/12`) and the
still-open order-3-class -> integer-3 bridge. So: a 2-primary count, free and interior; an odd/order-3 count,
external and not by itself pinned to three.

## What this means for the program

This does NOT hand the program a constructive escape -- no source action that forces three -- and it does NOT
hand it the clean GU-independent metatheorem "every net-chiral antilinear operation is frame-trivial" either.
That metatheorem, in the literal form two constructs reached for, is false: the carrier's self-dual `V`-`S`
entanglement DOES let a covariant operator couple chirality to the framing. What it hands the program is a
sharper and still GU-independent law: no operator interior to a Clifford-RS sector of this class -- linear or
antilinear -- can force an ODD chiral count; the only frame-active chiralizing channels are 2-primary, and the
single genuine loophole (a frame-non-trivial antilinear AZ-CII chiralizer) does not exist on the carrier (every
candidate is chirality-reversing, carrier-leaking, or a topologically trivial gauge dressing). GU's
"located, not forced" is therefore a SPECIAL CASE of a structural law, not a GU accident: GU's chiralizer is
frame-trivial, but even the broader class that includes frame-NON-trivial operators cannot reach an odd count
from inside. The escape GU lacked was looked for hard, in the full space of antilinear operations and the
carrier's genuine self-dual handle, and it is not there. The constructive direction does NOT close to "a source
action forces three"; it closes to "the count, if it exists, is not an operator on the carrier -- it lives in
the external index / anomaly-inflow sector, in the odd-torsion arena the 2-primary lemma is blind to," which is
precisely where the located-not-force campaign already placed it. The frame-triviality result is upgraded from
"GU's chiralizer happens to be frame-trivial" to "no Clifford-RS operator forces an odd count, and the only one
that could -- a frame-non-trivial antilinear chiralizer -- does not exist," with the honest correction that
frame-non-trivial chirality coupling DOES exist (it is just linear and 2-primary).

## Integrity

Nothing fabricated. No fabricated 3: every forced quantity is reported honestly as `+16` and `+32` and
explicitly factored as `2^4` and `2^5` with the 3-part COMPUTED to be 1 -- no factor of 3 anywhere, and the
source-action indices were reported as non-integer spectral noise rather than rounded into a fake count. No
fitted frame-non-trivial chiralizer: `X_L` is the genuine self-dual S-content of the carrier-projected grading
(computed by partial contraction, orthogonal to the bare grading, not tuned to any target), and the one
antilinear proxy-positive candidate was RUTHLESSLY exposed as a gauge artifact rather than sold as the escape.
None of the four caught fabrication patterns recur: no disguised `chi(K3) = 24` (16 and 32 carry no chi route),
no reverse-engineered `+8`, no circular rank-4 (the "4" is nowhere assumed), no fitted holonomy. Two genuine
adversarial fabrication_flags were raised and handled: Angle 2's construct MISREPORTED its own E/F data
(narrated chirality-reversing where its printout shows chirality-preserving) and overreached on the inside-slot
mechanism -- both corrected by independent from-scratch recomputation, conclusion unaffected; Angles 1 and 4's
constructs OVERCLAIMED the framing ("EVADABLE" / "structural one-line identity") and the adversarial verdicts
corrected both to partial. Computed-versus-analytic honesty was maintained throughout: all charges, traces,
counts, leakages, `C^2` defects and the `theta`-continuity sweep are COMPUTED on the verified substrate; only
the index / anomaly-inflow route (`int_X Ahat ch`) is tagged analytic/textbook, since the Atiyah-Singer index
cannot be reproduced on a finite 192-dim substrate without a manifold. Two of the broadest confirmatory random
searches (50k chirality-odd selectors; 4000 frame-coupled selectors) timed out under output buffering and are
NOT relied upon -- the verdict rests only on the decisive computations that were fully reproduced or
independently rewritten. Finally, this was a genuine attempt to FORCE three, not a confirmation pass: Angles B
and C steelmanned the constructive side hard -- the full space of antilinear operations, the RS vector index,
frame-coupled reality structures, conjugation gradings, a non-GU source action -- and a frame-non-trivial
chirality coupling WAS found (`O = L_SD (x) X_L`); it simply turns out to be linear and 2-primary, forcing an
even count and never the odd generation number.
