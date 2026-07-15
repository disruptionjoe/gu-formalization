---
artifact_type: exploration
label: W244
created: 2026-07-15
status: exploration
posture: independent adversarial re-verifier; try to BREAK the no-go not confirm it; re-derive every load-bearing step from own setup; exploration-tier, moves NO verdict; does NOT decide the W235 record bit; construction-fork explicit
title: "W244 independent re-verification of the chirality-safe good-stable structural no-go (W234/W237/W240/W241/W243) before canon promotion. VERDICT: SURVIVES. Every load-bearing step re-derived independently (own so(n,n) machinery, own basis, own regression tests/W244_reverify_good_stable_nogo.py, 40/40, exit 0): Z = grading = non-compact NON-ELLIPTIC boost (ad(Z) real nonzero, not conjugate into the maximal compact); the operator identity tau1(null) -> P = diag(+1,-1) under the fixed hyperbolic rotation; COMPACTIFY <=> Z2-ODD on a null pair (even bilinears -> {singlet, boost}); the adjoint no-go (Z2-even => [O,Z]=0 => Z in cent(O) => non-compact); Theorem C (no Cartan involution commutes with the non-elliptic Z); the extremal-weight nilradical closure (g_+ annihilates the top-Z-charge vector, is nilpotent, forces a non-compact stabilizer; rank-independent so(3,3)/so(4,4)/so(5,5)); the SO(2,1) non-extremal timelike reconciliation (compact stabilizer, NOT a Z-eigenvector = the open corridor); the exact 8256/4160/4096 arithmetic. ONE SUBSTANTIVE FINDING that does NOT break the promoted claim: W241's isotropy-level lemma 'good-stable = compact image <=> commutes with the SPECIFIC P' is TOO STRONG -- a tilted maximal compact k' = gKg^{-1} is compact-image (elliptic generators) yet does NOT commute with P, so 'compact image => allows the mass P' overstates. The no-go nonetheless holds by the ROBUST reason: the adjoint order parameter ~P' that reduces G to any maximal compact is itself Z2-ODD (Theorem C), so chirality is killed by the CONDENSATE directly. RECOMMENDATION for promotion: promote the W240(C)/W243 order-parameter formulation; do NOT canonize W241's compact-image<=>commutes-with-P step as a lemma (its conclusion is right, its stated mechanism is a frame-dependent overstatement that, read literally, would wrongly close the non-extremal charged corridor W240/W243 correctly keep open). Sole escapes stand: GU-non-native NON-extremal charged vectors, and denying Prop 1."
grade: "EXACT for the independently re-derived facts (own numpy/scipy regression, tests/W244_reverify_good_stable_nogo.py, 40/40, exit 0, positive controls first): ad(Z) real nonzero (max|imag|=1.1e-16, max|real|=2.00) and exp(tZ) e^t-unbounded so Z non-compact non-elliptic and not conjugate into k; the hyperbolic-rotation identity tau1(null)->diag(+1,-1)=P and tau3(null)->off-diagonal boost; the per-pair parities ({P,Z}=0, [Z,Z]=0); the centralizer arithmetic (cent(P)=12=maximal compact, cent(Z)=16, cent(I)=28) and the exact 8256/4160/4096 arena figures; the adjoint no-go [O,Z]=0 over sampled even directions; Theorem C over sampled conjugates gPg^{-1}; the extremal-weight nilradical closure and rank-independence in so(3,3)/so(4,4)/so(5,5) (raising nilradical nilpotent and annihilating the top Z-eigenvector, extremal vector beta-null, stabilizer dim 21>12); the SO(2,1) timelike compact-stabilizer non-eigenvector corridor; and the ADVERSARIAL PROBE that a tilted maximal compact is compact-image yet does not commute with P while its generating Cartan involution P' is Z2-odd. STRUCTURAL (same faithful-finite-model status as W216/W224/W234/W237/W240/W243, plus the rank-independent Lie-theory arguments) for the lift to the genuine Sp(32,32;H) arena: the arguments use only the Cartan decomposition g=k+p, Z in p semisimple, rep-theoretic extremal weights, and 'a compact real algebra has no nonzero nilpotents / is elliptic' -- all rank- and division-algebra-independent, so the quaternionic real form and rank 32+32 do not break them. CONDITIONAL on the W235 record bit for channel D availability (the whole comparison lives on the favorable, record-conserved branch). OPEN for the interacting source action, the physical state space, the observable algebra, the interior-charged residual, and the deny-Prop-1 escape. No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change; the W235 record bit is FLAGGED not decided."
depends_on:
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W237-channel-s-condensate-isotropy-2026-07-15.md
  - explorations/W240-z2even-compact-image-nogo-2026-07-15.md
  - explorations/W241-dynamical-vacuum-coincidence-escape-2026-07-15.md
  - explorations/W243-charged-corridor-closure-2026-07-15.md
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W244_reverify_good_stable_nogo.py
---

# W244 independent re-verification of the chirality-safe good-stable no-go

## THE VERDICT (top): SURVIVES

The structural no-go under re-verification is **canon-promotable**. Attacking it to break it, I
re-derived every load-bearing step from my own setup (independent `so(n,n)` machinery, my own
basis conventions, a regression authored from scratch that does NOT import the originals' code:
`tests/W244_reverify_good_stable_nogo.py`, 40/40, exit 0). Nothing in the chain is false. I found
**one substantive imprecision** in the WEAKEST of the five explorations (W241), and it does **not**
break the promoted claim -- but it changes what should be canonized. Details in Section 7.

The claim, restated as I verified it: in `Sp(32,32;H)` a chirality-safe good-stable requires a
compact-image (Prop 1) isotropy whose reducing DIRECTION is intrinsically Z2-ODD, because the
grading `Z` is a non-compact non-elliptic boost that no Cartan involution commutes with. Hence no
NEUTRAL, ADJOINT, or charged-EXTREMAL order parameter (everything GU builds) delivers a
chirality-safe good-stable interior. Sole escapes: GU-non-native NON-extremal charged vectors, and
denying Prop 1 (the firewall boundary). **All of this holds.**

## 1. Construction fork (mandatory)

The load-bearing object is a general order parameter / isotropy in the non-compact real form
`Sp(32,32;H)`, the program's recurring Krein/native fork. I adopt the native reading throughout:
the arena is the non-compact real form whose non-compactness IS the Krein form
(GEOMETER-VS-PHYSICS-OBJECTS, gauge-group row); the grading `Z = tau3(null) = sigma1(definite)` is a
genuine boost in `p`, not a compact charge; and "good-stable" is the Krein positive-majorant / ghost
keep-and-grade notion (Prop 1), not a positive-Hilbert projection. My job was to check whether the
kill survives in the native construction (it does) and whether the kill is an artifact of the
majorant definition (it is explicitly conditional on it, and that conditionality is flagged, not
hidden -- Section 6).

## 2. Re-derivation 1: Z is a non-compact NON-ELLIPTIC boost (attack 1)

Independently: `Z = [[0, I],[I,0]]` per the definite basis; it is `beta`-symmetric off-diagonal,
so it lies in the non-compact part `p` of the Cartan decomposition. My own `ad`-matrix build (not
the originals') gives `ad(Z)` eigenvalues **real, nonzero** (`max|imag| = 1.1e-16`,
`max|real| = 2.00`), and the operator 2-norm of `exp(tZ)` grows like `e^t`
(`||exp(5Z)||_2 / ||exp(1Z)||_2 > 20`). A block-diagonal (compact) generator, by contrast, gives a
purely imaginary `ad`-spectrum. Because the `ad`-spectrum is conjugation-invariant and `Z` has a
nonzero real part, **no conjugate of `Z` is elliptic**, so `Z` cannot be conjugated into the maximal
compact `k`. The grading is genuinely a boost. (checks 1a-1d.) Note this is the honest crux: the
discrete gen/mirror `Z/2` is generated by a hyperbolic rescaling of the null partners
`u, v` (`exp(t*tau3(null)) = diag(e^t, e^{-t})` preserving `eta(u,v)=1`) -- a boost, not a rotation.

## 3. Re-derivation 2: tau1(null) = P, and P is the compact-reduction direction (attack 2)

Independently, with the explicit rotation `R = (1/sqrt2)[[1,1],[1,-1]]` (columns `u,v` in the
`e`-basis), `R^2 = I`, orthogonal: `R tau1 R^{-1} = diag(+1,-1) = P` (the Cartan involution,
DIAGONAL) and `R tau3 R^{-1} = [[0,1],[1,0]]` (an off-diagonal BOOST). So the good-branch pairing
`tau1(null)` IS the compactifier `P` and the grading `tau3(null)` is a boost, exactly as claimed.
(checks 2a-2c.) Uniqueness of the compact-reduction direction: every maximal compact is
`Z_G(theta)` for a Cartan involution `theta`, all Cartan involutions are a single conjugacy class,
so the compact-reduction directions form one orbit; per pair the unique traceless compactifier is
`P`, and it is Z2-ODD (`{P, tau3}=0`, check 2d). No second independent compact-reduction direction
was found.

## 4. Re-derivation 3: COMPACTIFY <=> Z2-ODD, and the adjoint no-go (attacks 3, 4)

On a null pair the traceless bilinears are `{tau1, tau2, tau3}`; only `tau3` (= the grading `Z`)
commutes with `Z` (Z2-EVEN), and it maps to an off-diagonal BOOST in the definite basis, never to
the diagonal compactifier `P`. `tau1, tau2` are Z2-ODD. So every Z2-EVEN bilinear is
`{singlet, boost}` and the unique compactifier is Z2-ODD. I hunted for a Z2-even direction that
compactifies and did not find one (checks 3a-3b). Lifting to all adjoint ranks: a Z2-even adjoint
`O` satisfies `[O, Z] = 0`, i.e. the non-compact boost `Z` lies in `cent(O) = stab(O)`; `Z`
non-elliptic then forces the stabilizer image non-compact (checks 4a-4b over 15 sampled even
directions). W237's bilinear theorem is the rank-2 case; the adjoint no-go is genuinely
rank-independent. **No break.**

## 5. Re-derivation 4: the extremal-weight nilradical theorem (attack 5)

Independently in `so(n,n)`: `ad(Z)` grades `g = g_- + g_0 + g_+`. I extracted `g_+` as the positive
`ad(Z)`-eigenspace, verified every nonzero element is matrix-nilpotent (hence ad-nilpotent), and
confirmed `g_+` **annihilates the top `Z`-charge vector** of the vector rep (raising past the maximum
lands in the zero weight space). Since a real subalgebra containing a nonzero nilpotent cannot be
compact (a compact real algebra is elliptic: `ad` has purely imaginary spectrum, so a nilpotent `ad`
is zero), `stab(extremal)` is non-compact. Reproduced rank-independently in `so(3,3)`, `so(4,4)`,
`so(5,5)` (nilradicals of dim 3, 6, 10). The extremal charged vector is `beta`-NULL and its
stabilizer has dim 21 > 12 in `so(4,4)` -- it contains the nilradical (checks 5a-5d).

The `SO(2,1)` reconciliation is correct and honestly left OPEN: the timelike escape vector `t = e_3`
has a COMPACT stabilizer `SO(2)` (dim 1) yet is NOT a `Z`-eigenvector (a boost sends `t` off its own
ray; it straddles the `+/-1` weight spaces), so the theorem -- which needs an extremal
EIGENVECTOR -- does not apply. This non-extremal charged class is the surviving corridor, and W243
does not sweep it: it is named as the open residual (interior/non-eigenvector charged vectors) and
flagged GU-non-native (checks 5e-5f). **No break; the residual is genuinely open, not swept.**

## 6. Re-derivation 5: Theorem C and the finite -> full lift (attacks 6, 7-lift)

Theorem C (no Cartan involution commutes with the non-elliptic `Z`): if `[Z, P'] = 0` for a Cartan
involution `P'` then `Z in cent(P') = k'` (compact), forcing `Z` elliptic -- contradiction. I
verified the contrapositive over 12 sampled conjugates `gPg^{-1}`: none is simultaneously a
maximal-compact compactifier AND Z2-even (check 6a). The reducing direction is intrinsically Z2-ODD.

**The finite -> full `Sp(32,32;H)` lift (attack 6, the flagged hiding place) is sound.** Every
load-bearing argument uses only: (i) the Cartan decomposition `g = k + p`; (ii) `Z in p` semisimple
(so `ad(Z)` grades the algebra -- note the extremal-weight argument needs only SOME grading, not a
`|1|`-grading, so a longer restricted-root string in the quaternionic form does not break it); (iii)
rep-theoretic extremal weights; (iv) "a compact real algebra has no nonzero nilpotents." None of
these depends on the rank or on the division algebra `H`. The quaternionic structure changes which
reps are quaternionic, not the Lie-theoretic no-go skeleton; rank 32+32 only sets the exact
8256/4160/4096 figures (independently reproduced, check 8). I did not find a rank-specific or
quaternion-specific break.

## 7. The one substantive finding (attack 4 pushed hard, and attack on W241)

**W241's isotropy-level lemma is too strong, though its conclusion is right.** W241 argues
"good-stable = compact image `<=>` commutes with `P` `<=>` allows the mass `~P` `<=>` kills
chirality," concluding the `{good-stable AND chirality}` corner is empty **for every dynamical
isotropy**. Pushing on the middle step, I built a **tilted maximal compact** `k' = g K g^{-1}` (with
`g = exp(0.5 Z)` a genuine boost): its generators are still elliptic (compact-image, spectrum is
conjugation-invariant) yet they do **not** commute with the specific `P` (check 7a-7b). So "compact
image `=>` commutes with `P`" is **false**: compact-image isotropies that are NOT `Z_G(P)` exist,
and they do not allow the specific mass `~P`. Read literally, W241's blanket statement would also
close the non-extremal charged corridor (whose compact stabilizer likewise does not commute with the
grading) -- which would CONTRADICT W240/W243, which correctly keep that corridor open.

**Why the no-go survives anyway (the robust reason).** The adjoint order parameter `~P'` that reduces
`G` to any maximal compact `k' = Z_G(P')` must have `[P', Z] != 0` (else `Z in k'`, non-compact); by
Theorem C every such `P'` is Z2-ODD (check 7c-7d). So the CONDENSATE `~P'` itself pairs gen with
mirror and kills chirality directly -- independent of whether `k'` "allows" the fixed `P`. The
chirality obstruction is a fact about the **reducing order parameter** (W240 Theorem C / W243
extremal nilradical), not about post-hoc `P`-commutation of the residual group. The genuinely-open
escape is exactly a compact stabilizer that does NOT commute with the grading, realized only by a
NON-extremal charged vector (`SO(2,1)` type), GU-non-native (check 7e) -- consistent with W240/W243
and with the promoted claim.

**Recommendation for promotion.** Canonize the **W240(C)/W243 order-parameter formulation** (the
reducing direction is Z2-odd; extremal charged vectors carry a nilradical). Do **not** canonize
W241's "compact image `<=>` commutes with `P`" as a lemma: its conclusion (the coincidence escape is
closed) is fine, but its stated mechanism is a frame-dependent overstatement that is literally false
and, taken at face value, mis-describes the residual as "deny Prop 1 only" when W240/W243 (correctly)
also list the non-extremal charged corridor. The promoted claim should list BOTH escapes, as the
brief's statement already does.

## 8. What I independently re-derived vs inherited

- **Re-derived from my own setup (not inherited):** Z non-elliptic boost + not-conjugate-into-k;
  `tau1(null)=P` via my own hyperbolic rotation; COMPACTIFY<=>Z2-ODD and the even->{singlet,boost}
  map; the adjoint no-go over sampled even directions; Theorem C over sampled conjugates; the
  extremal-weight nilradical closure and its rank-independence (so(3,3)/so(4,4)/so(5,5)); the
  SO(2,1) non-extremal reconciliation; the tilted-maximal-compact counterexample to W241's lemma;
  the 8256/4160/4096 arithmetic. My test shares no code with W234/W237/W240/W241/W243.
- **Inherited (not re-derived here):** Proposition 1 itself (invariant positive majorant exists iff
  relatively compact image; HARDENING-REPORT) -- I treated it as the definition of good-stable and
  checked the no-go is honest about being conditional on it; the upstream rep-theory that channel S
  = `(16bar)^4` is Z2-even with additive charge `-4` and has zero `SO(10)`-singlet bilinear (W231);
  the identification of `Z` with W173/W235's ghost-parity grading and the W235 record bit.

## 9. Residuals honestly still open (unchanged by this re-verification)

1. **Deny Proposition 1** (the firewall-boundary escape): the no-go is conditional on the
   Krein positive-majorant definition of good-stable. This is load-bearing and explicitly flagged in
   W241/W224, not hidden. A GU-native non-majorant positivity (PT / boundary) is untested.
2. **The non-extremal charged corridor** (interior `Z`-eigenvectors and non-eigenvector timelike
   vectors): mathematically open, shown GU-non-native under the assumption that GU condensates are
   extremal tensor components. The "extremal only" assumption is itself a flagged open item (W243
   follow-up 1).
3. **The W235 record bit**: the whole comparison lives on the favorable record-conserved branch; not
   decided here.
4. **The interacting source action, physical state space, observable algebra**: unbuilt (W219/W224).

## 10. Endorsement

**I endorse canon promotion of the structural no-go, with one editorial condition:** promote the
W240(C)/W243 order-parameter formulation and the two named escapes (GU-non-native non-extremal
charged vectors; deny Prop 1). Do not promote W241's "compact image `<=>` commutes with `P`" step as
a stated lemma (correct conclusion, overstated mechanism; fix per Section 7). With that substitution,
nothing in the chain is false and the no-go is promotable at STRUCTURAL grade (finite faithful-model
+ rank-independent Lie theory), conditional on the W235 record bit and modulo denying Prop 1.

## 11. Machine receipt

```
python -u tests/W244_reverify_good_stable_nogo.py
```

40/40 checks passed, exit 0. Positive controls run FIRST (nilpotent/non-compactness detector fires
on a real nilpotent and stays silent on `so(2)`; parity detector calls `P` ODD and `Z` EVEN;
centralizer detector calls `cent(P)` maximal-compact and `cent(Z)` not; escape detector fires on a
planted (chirality-safe, compact-image) pair so the no-go has teeth). The actual checks then
re-derive Sections 2-7 independently.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, `bar(b)`, `H59`, or generation-count
change. The W235 record bit is flagged and coupled, not decided. No cross-repository identity
asserted; the reservoir Krein sign and the Y14 spectral-section / record datum stay gated
temporal-issuance / time-as-finality objects. `bar(b)` and `H59` remain OPEN. This is independent
re-verification (characterization), verdict-relevant and Joe-gated; no verdict is moved. No Lean/Lake
run (machine-wide serialized-build rule). Zero em dashes.
