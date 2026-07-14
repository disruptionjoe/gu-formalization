---
artifact_type: exploration
status: exploration (W159; TEAM TACHYON-ESCAPES; five personas inline, one worker, no sub-agents; deterministic test with W126/W128/W130 positive controls)
created: 2026-07-14
wave: W159
label: W159
posture: coherence-first (Joe 2026-07-14); exploration grade; conditional register; honest grading
title: "W159 -- after the keystone FAILED (W157: a2 = -a1^2 a coincidence), do the two genuine escapes plus the sign-forcing residual render the tachyon (debit-1) benign? VERDICT: STANDS-AS-DEBIT, NARROWED. Route 1 (AF/AS branch): branch-UNSELECTED -- GU's native tree point (f_2^2,f_0^2)=(-1/4,-3/8) is off BOTH branches (both require f_2^2>0: AF by its basin gate, AS by the monotone 1/f_2^2 law), and connecting to EITHER needs the SAME strong-coupling (c_W=0) spin-2 passage that one loop cannot adjudicate; targeting AS does NOT avoid it (the obstruction is a spin-2/Weyl crossing orthogonal to the scalar AF-vs-AS coordinate), and even past it AS only PERMITS-NOT-FORCES m_0^2>=0 (W128 sign-lock; E2 stands). Route 2 (gradient saturation): OUT-OF-VALIDITY -- the gradient function is EXACT rational W(v)=2(2688v^6-544v^4+40v^2-1)/(16v^2-1)^3 with a genuine singularity (induced-metric degeneration) at v^2=1/16; the tachyonic scale |m_0^2|=1/4=4x(1/16) sits BEYOND it, and the kinetic coefficients are all POSITIVE (a DBI speed-limit, not a restoring force), so no bounded-field attractor exists in validity. Route 3 (sign-forcing): SIGN-FREE -- with the |H|^2 slice decomposition (-1,4/3,-4/9,0), det[[a1_II,a1_H],[c_R_II,c_R_H]]=4/9!=0, so (a1,c_R) are INDEPENDENT coordinates of the induced shape family and a member with a1=2/3>0 (attractive) AND c_R=+4/9>0 (healthy) exists at (alpha,beta)=(-2,1); c_R<0 is NOT forced by a1>0 (only a positive-cone correlation survives). Dispersion: the spin-block-diagonal propagator (k^2+m_0^2)(k^2+m_2^2) has NO cross-channel mixing; the scalar tachyon peaks at k=0 (homogeneous instability, band 0<=k<1/2), NO finite-k scale selection. debit-1 STANDS; bar (b) UNCHANGED (flaw count does not drop), consistent with W157."
hypothesis: "The keystone route (a2=-a1^2 structural) FAILED (W157: coincidence; only the SIGN c_R<0-iff-a1>0 survives, basis/signature-invariant, so NOT a (9,5) effect). The tachyon (debit-1) returns to the two genuine escapes plus the surviving sign question. Settle whether debit-1 is rendered benign or understood via ANY of: (1) AF/AS branch -- is the tachyon an AF-branch artifact and GU on the AS branch with a healthy scalaron; (2) gradient-sector saturation -- does the gradient quartic bound the runaway into a finite-field attractor within validity; (3) sign-forcing residual -- is c_R<0 FORCED by a1>0 covariantly. Plus the dispersion/pole k-structure."
grade: "exploration / conditional register throughout. COMPUTED (deterministic, tests/W159_tachyon_escapes.py, 16/16 exit 0, W126 + W128 + W130 positive controls first). All three route verdicts and the dispersion result are established by exact sympy computation with cited-but-not-re-derived imports, not asserted. LOAD-BEARING imports (CITED): W126 (the slice decomposition (2,1/3,8/9,-4); the potential sector EXACTLY quadratic c_3=0; the gradient series 2+16v^2+320v^4+...; the |H|^2 Route-1 machinery reused verbatim); W130 (c_R=-4/9, c_W=+2, sign maps f_0^2=1/(6c_R)=-3/8 and f_2^2=-1/(2c_W)=-1/4, native poles m_0^2=m_2^2=-1/4, the native tree point off the AF branch, the c_W=0 strong-coupling crossing, the separate TT/spin-0 sectors); W128 (the AS/Reuter sign-lock de-slaved root = eta0 g*/(kappa Phi c_C); PERMITTED-NOT-FORCED; the g-independent 1/f_2^2 law keeping f_2^2>0 on the AS trajectory; E2 fork stands); W157 (the demoted keystone; the surviving SIGN; signature-blindness). NEW here (DERIVED): the shared-spin-2-passage argument (route 1 does not avoid the strong-coupling wall by targeting AS); the closed-form gradient function W(v)=2(...)/(16v^2-1)^3 and its v^2=1/16 degeneration (route 2 out-of-validity, with the |m_0^2|=1/4=4x margin and the positive-coefficient speed-limit structural point); the |H|^2 full slice decomposition (-1,4/3,-4/9,0) and the det=4/9 SIGN-FREE result with an explicit attractive-and-healthy counterexample (route 3); the spin-block-diagonal no-band dispersion. HONEST RESIDUALS: (1) the strong-coupling (c_W=0) passage is named, not computed -- whether GU's tree data can reach EITHER branch through it is exactly the strong-coupling problem one loop cannot adjudicate (unchanged from W130); (2) the E2 AF/AS fork is CARRIED, not closed -- no GU-native selector was found here or in W128; (3) route 3's SIGN-FREE rests on the shape family alpha|II|^2+beta|H|^2 admitting alpha<0 (justified by the indefinite norms, but the pure-|II|^2 GU point remains sign-correlated); (4) magnitudes remain normalization-gated exactly as H25 graded them. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; the count is unchanged; H59/H61a OPEN; the E2 AF/AS fork carried, not closed. NO forbidden target {3,8,24,chi(K3),Ahat} assumed/inserted/hardcoded/divided-by."
construction: "program-native where the objects are GU's (the induced |II|^2 and |H|^2 actions, the conformal slice, the covariant R^2/Weyl channel split, the native tree point, the (9,5) ambient with its indefinite |II| norms). Standard-field where the machinery binds any construction (the f(R) scalaron-mass dependence on c_R; the Stelle spin-0/spin-2 channel split; the FRG Reuter fixed point and relevance sign; k-essence / DBI kinetic saturation and its speed-limit-vs-restoring-force distinction; the Lorentz-irreducible spin decomposition of a flat-space quadratic operator; Turing/Swift-Hohenberg finite-k band structure as the contrast). Every analogy PORTED and labelled; none asserted of GU. Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md."
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W128-reuter-branch-scalaron-native-2026-07-14.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W156-coherent-full-story-2026-07-14.md
  - explorations/W157-a2-equals-minus-a1-squared-keystone-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W159_tachyon_escapes.py
external_refs:
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum (R^2 = spin-0, C^2 = spin-2); the block-diagonal channel split"
  - "Starobinsky, PLB 91 (1980) 99 -- R^2 scalaron (healthy for +R^2)"
  - "Reuter, PRD 57 (1998) 971 -- the Reuter (AS) fixed point"
  - "Copeland, Rahmede & Saltas, arXiv:1311.0881 -- AS-Starobinsky: R^2 relevant, IR value a free boundary condition, healthy branch realized"
  - "Salvio & Strumia, JHEP 06 (2014) 080 -- agravity couplings and the mass anchors M_i^2 = f_i^2 Mbar^2/2"
  - "Silverstein & Tong, PRD 70 (2004) 103505 -- DBI / speed-limit kinetic structure (the k-essence saturation contrast)"
  - "Cross & Hohenberg, Rev. Mod. Phys. 65 (1993) 851 -- finite-wavelength (Turing-band) pattern selection, the contrast the dispersion check rules out"
---

# W159 -- the tachyon escapes: after the keystone failed, do the two genuine routes clear debit-1?

## 0. Where the load sits, and why this wave

W157 killed the keystone. The exact identity `a2 = -(a1)^2` that W155/W156 personas 6 and 10
leaned on (the tachyon as the literal R^2-channel square-shadow of attractive gravity) is a
COINCIDENCE: it holds only for the MSS-slice-reduced coefficient `a2_MSS = -1/9`, and the
covariant coefficient that actually sets the scalaron mass, W130's `c_R = -4/9`, breaks it by a
factor of four. Only the SIGN `c_R/a1 < 0` (tachyonic iff attractive) survives, and it is
basis- and signature-invariant, so it is NOT a `(9,5)`-indefiniteness effect. The keystone
conversion of debit-1 FAILS; the tachyon returns to an independent debit, and the load returns
to the two genuine escapes (the AF/AS branch fork, and gradient-sector saturation) plus the one
weaker surviving question (is the sign FORCED).

This wave settles all three, coherence-first: build each escape's story, then test it. Five
personas inline, one worker, no sub-agents. Deterministic test
`tests/W159_tachyon_escapes.py`, 16/16 exit 0, W126 + W128 + W130 positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| Induced action | `\|II\|^2` on the conformal family; W126 Route-1 machinery reused verbatim, plus `\|H\|^2` for the shape family | The pinned construction; every coefficient is the W126 object. |
| Scalaron coupling | the covariant `c_R = a2s + a3s/3 = -4/9` (W130), not the slice `a2_MSS` | W157 settled that the physical mass rides `c_R`. |
| Spin-2 coupling | `c_W = +2`, `f_2^2 = -1/(2 c_W) = -1/4` (W130) | The channel where the branch passage lives. |
| UV completion | none selected; both branches carried | Route 1 is the fork itself; E2 stands (W128). |
| Shape mix | `alpha\|II\|^2 + beta\|H\|^2` | Route 3's deformation family; `alpha < 0` admissible because the `\|II\|` norms are already indefinite. |

## 2. Persona 1 -- FRG/branch specialist: route 1, and why targeting AS does not avoid the passage

The strongest remaining escape: the tachyon is an AF-branch artifact, and GU actually lives on
the AS/Reuter branch where a healthy scalaron is PERMITTED (W128). The hope is concrete: W130
found GU's native tree point `(f_2^2, f_0^2) = (-1/4, -3/8)` is OFF the AF branch (both couplings
negative, failing the `f_2^2 > 0` basin gate). If GU's physical branch is AS instead, and AS
gives `m_0^2 >= 0` at GU's content, debit-1 dissolves.

It does not, and the reason is a channel-orthogonality fact that the "aim for AS" framing hides.

**Both branches live at `f_2^2 > 0`.** The AF branch gates on `f_2^2 > 0` by construction (W123
basin). The AS/Reuter branch ALSO keeps `f_2^2 > 0` at every finite scale: W128 Section 3 proved
`1/f_2^2(t) = 1/f_2^2(0) + kappa Phi b_2 t` (the Weyl coupling's flow is `g`-independent in this
truncation), which stays positive from a positive start and pinches to `f_2^2* = 0` only at the
FP endpoint. So the AF-vs-AS distinction is entirely a SCALAR (`f_0^2`) story; in the SPIN-2
(`f_2^2`) coordinate both branches sit on the same side, `f_2^2 > 0` (test R1b).

**The tree point is off BOTH branches, in the spin-2 coordinate.** GU's native tree data have
`f_2^2 = -1/4 < 0` (test R1a). Reaching EITHER branch therefore requires flipping `f_2^2` through
`f_2^2 = +/- infinity`, i.e. through `c_W = 0` -- the strong Weyl coupling wall W130 already
flagged as the AF-matching obstruction one loop cannot adjudicate. That passage is a SPIN-2
crossing; it is required identically for AF and for AS (test R1c). Choosing to aim at the AS
branch does not avoid it, because the obstruction is orthogonal to the scalar coordinate that
distinguishes the branches. The intuition "AS is healthy, so route the tree point there" fails on
the geometry: the tree point's disease is in the spin-2 channel, and both branches are on the far
side of the same wall.

**Even past the wall, AS only PERMITS.** Grant the passage. W128's sign-lock theorem gives the
de-slaved Reuter root `f_0^2* = eta0 g*/(kappa Phi c_C)`, sign-locked to the ported R^2-relevance
`eta0 > 0`; and both the healthy (`f_0^2 -> +0.128`) and tachyonic (`f_0^2 -> -0.128`)
trajectories are UV-complete (PERMITTED-NOT-FORCED). `m_0^2 >= 0` on AS is a FREE relevant
boundary condition, not a derived GU consequence, and no GU-native selector picks the healthy one
(E2 fork STANDS). So AS does not deliver "GU has a healthy scalaron"; it delivers "GU is not
FORCED tachyonic on AS," which is the weaker statement W128 already banked (test R1d).

**Route 1 verdict: branch-UNSELECTED.** The tachyon is not a demonstrable AF artifact: GU's tree
data are off both branches, the AS-healthy scalaron is reachable only through the same
strong-coupling passage AF needs (one loop cannot adjudicate it), and even past it AS only
permits health. Debit-1 does not dissolve via route 1. It NARROWS to a branch-selection question
gated behind a shared spin-2 strong-coupling wall.

## 3. Persona 2 -- nonlinear-dynamics / saturation theorist: route 2, and the closed form that kills it

W126 proved the POTENTIAL sector is exactly quadratic (`c_3 = c_4 = ... = 0`), so no higher
potential invariant lifts the vacuum. The surviving hope is the GRADIENT sector, which does carry
the quartic: `W(v, s=0, E0=1) = 2 + 16 v^2 + 320 v^4 + ...` with `v = |dphi|`. The story to test:
does that gradient quartic bound the tachyonic runaway into a finite-field attractor (a rolling
scalaron that saturates)?

**The gradient function has a closed form with a genuine singularity.** Computing the full series
(not just the quartic) gives an EXACT rational function (test R2a):

```
W(v) = 2 (2688 v^6 - 544 v^4 + 40 v^2 - 1) / (16 v^2 - 1)^3 .
```

The denominator factors as `(16 v^2 - 1)^3`, so `W` has a POLE at `v^2 = 1/16`. This is not a
series artifact: it is the induced metric `gbar = g + V_g(dg, dg)` degenerating (the graph
immersion's induced metric becomes singular when the gradient is large enough). The convergence
radius of `2 + 16 v^2 + 320 v^4 + ...` is therefore exactly `v^2 = 1/16`; the coefficient ratios
`8, 20, 18.4, 17.39, 16.64, 16.0, ...` confirm they approach `16 = 1/r_c` (test R2b).

**The kinetic function is a speed limit, not a restoring force.** Every gradient coefficient is
POSITIVE (`2, 16, 320, 5888, 102400, ...`). A positive, growing kinetic function is a DBI-type
speed limit: it bounds the field VELOCITY `|dphi|`, never the field EXCURSION. Since W126 already
proved the potential is exactly quadratic (no minimum exists), a speed limit on a runaway
potential yields a bounded-VELOCITY runaway to the `f' = 0` wall, not a bounded-field attractor
(test R2c). There is no restoring structure for a kinetic term to convert into a stable vacuum.

**The EFT-validity kill (the standard killer, and it bites).** Grant the k-essence framing and ask
for a kinetic-saturation balance against the tachyonic drive. Any such balance needs a kinetic
scale comparable to the tachyonic mass, `|m_0^2| = 1/4` (W130 native). But `1/4 = 4 x (1/16)`: the
required regime `v^2 ~ |m_0^2|` sits at four times the singularity radius, BEYOND the induced-metric
degeneration, where the truncated kinetic function and the entire induced-geometry derivative
expansion are invalid (test R2d). The attractor, if one existed mathematically, lives past a
geometric breakdown of the construction.

**Route 2 verdict: OUT-OF-VALIDITY** (and structurally a speed-limit, not a restoring force, so no
bounded-field attractor exists even in principle). The gradient quartic does not render the tachyon
benign. This hardens W126's Section-3 EFT-validity finding with an exact closed form for the
degeneration point.

## 4. Persona 3 -- higher-derivative-gravity theorist: route 3 (sign-forcing) and the dispersion

**Sign-forcing.** W157 left as its named residual: is `c_R < 0` FORCED by `a1 > 0` in the
covariant action, or SIGN-FREE? If forced, "tachyonic iff attractive" is a structural
sign-correlation and the tachyon is a (weak) feature: you cannot have attractive gravity in this
framework without it. The natural framework deformation is the wave-35 shape family
`alpha|II|^2 + beta|H|^2`. Compute the full slice decomposition of `|H|^2` (test R3a):

```
|II|^2 :  (a0, a1, a2s, a3s) = ( 2, 1/3, 8/9, -4),   c_R_II = a2s + a3s/3 = -4/9
|H|^2  :  (a0, a1, a2s, a3s) = (-1, 4/3, -4/9,  0),   c_R_H  = a2s + a3s/3 = -4/9
```

In the family, `a1(alpha,beta)` and `c_R(alpha,beta)` are both linear. The sign correlation
`sign(c_R) = -sign(a1)` is FORCED iff their zero-lines coincide, i.e. iff
`det[[a1_II, a1_H], [c_R_II, c_R_H]] = 0`. Computed:

```
det = a1_II c_R_H - a1_H c_R_II = (1/3)(-4/9) - (4/3)(-4/9) = 4/9 != 0 .
```

So `(a1, c_R)` are INDEPENDENT coordinates of the shape family (test R3b): the map
`(alpha, beta) -> (a1, c_R)` is invertible, and `(a1, c_R)` can be ANY pair. In particular there is
an explicit member with attractive gravity AND a healthy R^2 sector -- `(alpha, beta) = (-2, 1)`
gives `a1 = 2/3 > 0` and `c_R = +4/9 > 0` (test R3c). Attractive gravity does NOT force the
tachyon. The `alpha < 0` weight is admissible precisely because the `|II|` inner products are
already indefinite in the `(9,5)` ambient (`w2 = <II_1, II_1> = -64 < 0`), so there is no
positivity ground to exclude it.

**Route 3 verdict: SIGN-FREE.** What survives is strictly weaker than forcing: a POSITIVE-CONE
correlation -- for `alpha, beta >= 0` the sign does correlate (the counterexample needs
`alpha < 0`, test R3d) -- and the signature-blindness W157 found. A correlation on a cone is not a
structural identity. Even the weak "feature" framing of debit-1 (the tachyon as the unavoidable
companion of attraction) therefore fails: the induced-action family contains attractive-and-healthy
members, so the tachyon is a property of GU's specific point `(alpha, beta) = (1, 0)`, not of
"attractive gravity in this framework."

**Dispersion (folded in).** Does the tachyonic pole sit at a physical `k`, or is there finite-`k`
band structure (a scale selection) that reinterprets it? The quadratic operator around flat space
is BLOCK-DIAGONAL in spin -- W130 computed the TT (spin-2) and spin-0 sectors as separate
Lorentz-irreducible blocks -- so the full inverse propagator FACTORIZES as
`(k^2 + m_0^2)(k^2 + m_2^2)` with no `k`-dependent mixing between the channels (test D1). There is
therefore no cross-channel interplay to build a Turing-type band. Each sector's growth rate is its
own: the scalar tachyon has `omega^2 = -(k^2 + m_0^2)`, strictly decreasing in `k^2`, so it PEAKS
AT `k = 0` with unstable band `0 <= k < |m_0| = 1/2` (test D2). The spin-2 sector
(`m_2^2 = -1/4`, `f_2^2 < 0`) is a separate channel -- the AF-branch massive-ghost issue -- and
likewise peaks at `k = 0` (test D3); the "spin-2 coupling is the decider" concern resolves in the
negative because the coupling does not mix the channels at quadratic order. **Dispersion verdict:
the tachyon is a genuine `k = 0` (homogeneous) instability, NO finite-`k` band, NO scale selection.
The interpretation is unchanged -- it is a real long-wavelength tachyon, not a reinterpretable
pattern-forming mode.**

## 5. Persona 4 -- symbolic / numerical engineer: what the test pins

`tests/W159_tachyon_escapes.py`, 16 checks, exit 0, exact sympy, positive controls first.

- **PC1-PC5** reproduce the imports: W126 `(2,1/3,8/9,-4)`; W130 `c_R = -4/9`, the sign maps
  `f_0^2 = -3/8`, `f_2^2 = -1/4`, the native poles `m_0^2 = m_2^2 = -1/4`; and the W126 gradient
  series `2 + 16 v^2 + 320 v^4 + ...` (the object route 2 must bound). The `|II|^2` and `|H|^2`
  slice decompositions run through the verbatim W126 Route-1 `B^V` + normal-lift machinery, so the
  route-3 computation is regression-pinned to the same code that produced the imports.
- **R1a-R1d** the branch analysis: tree off both branches; the monotone `1/f_2^2` law; the shared
  spin-2 crossing (crossing count to AF = to AS = 1); the sign-lock PERMITTED-NOT-FORCED.
- **R2a-R2d** the gradient closed form `(16 v^2 - 1)^3` denominator, the coefficient-ratio
  convergence radius, the all-positive speed-limit fact, the `|m_0^2| = 4 x r_c` validity margin.
- **R3a-R3d** the `|H|^2` decomposition, the `det = 4/9` independence, the explicit
  attractive-and-healthy counterexample, the positive-cone residue.
- **D1-D3** the spin-block factorization, the `k = 0` scalar peak, the separate spin-2 channel.

## 6. Persona 5 -- adversarial skeptic: steelman TACHYON-STANDS on all three, and where it lands

**Route 1 steelman (STANDS via the strong-coupling problem).** The sharpest pro-STANDS case is
exactly the one that wins: connecting GU's tree data to any UV-complete branch requires the
`c_W = 0` passage, and at that crossing `|f_2^2| -> infinity` is strong Weyl coupling where one
loop adjudicates nothing (W130). The escape's own machinery cannot certify GU reaches the AS
branch, so it cannot certify the tachyon is an AF artifact. The skeptic wins route 1 as
branch-UNSELECTED -- not because AS is refuted, but because neither branch is reachable by a
computation the repo can do. This is honest: it is a carried fork (E2), not a closure.

**Route 2 steelman (STANDS via EFT validity, the standard killer).** The pro-benign case needs the
kinetic saturation to sit inside validity; the closed form makes that impossible (the degeneration
is at `v^2 = 1/16`, the required scale at `1/4`). The skeptic notes the deeper structural point:
even a hypothetical in-validity attractor would be a bounded-velocity runaway, not a stable vacuum,
because a positive kinetic function is a speed limit. Route 2 STANDS as OUT-OF-VALIDITY on two
independent grounds.

**Route 3 steelman (STANDS-as-feature, i.e. SIGN-FORCED).** The pro-feature case wanted the sign
correlation to be structural so the tachyon reads as a (weak) unavoidable companion of attraction.
The `det = 4/9 != 0` computation refutes it: the family has attractive-and-healthy members. The
skeptic must concede route 3 is SIGN-FREE -- which cuts BOTH ways. It denies GU the "feature"
consolation (the tachyon is not forced by attraction), and it equally denies any claim that the
tachyon is structurally inevitable. The tachyon is GU's specific-point property, neither a feature
nor a doom.

**Where the skeptic must stop.** None of the three routes is a KILL of GU; they are a KILL of the
three benign-ification stories. Debit-1 remains an independent debit, exactly as W157 left it, and
the honest overall is a NARROWING, not a movement of the count.

## 7. Synthesis -- the return data

| Route | Verdict | Basis |
|---|---|---|
| 1 (AF/AS branch) | **branch-UNSELECTED** (tachyon NOT a demonstrable AF artifact; not TACHYON-ON-BOTH by fiat, but unreachable-either-way) | tree off both branches; shared `c_W=0` spin-2 passage one loop cannot adjudicate; AS PERMITS-NOT-FORCES; E2 stands |
| 2 (gradient saturation) | **OUT-OF-VALIDITY** | closed form `W = 2(...)/(16v^2-1)^3`, degeneration at `v^2=1/16`; `|m_0^2|=1/4=4x`; positive coefficients = speed limit, not restoring force |
| 3 (sign-forcing) | **SIGN-FREE** | `|H|^2 = (-1,4/3,-4/9,0)`; `det = 4/9 != 0`; attractive-and-healthy member at `(alpha,beta)=(-2,1)` |
| dispersion | **`k=0` tachyon, NO band** | spin-block-diagonal `(k^2+m_0^2)(k^2+m_2^2)`; scalar growth peaks at `k=0`; spin-2 a separate channel |

**Overall debit-1 verdict: STANDS-AS-DEBIT, NARROWED.** The tachyon is not rendered benign by any
of the three routes. It NARROWS to a precise object: an AF-branch tree-level instability whose only
non-artifact escape is the E2 branch-selection fork, gated behind a shared strong-coupling
(`c_W = 0`) spin-2 passage that one loop cannot adjudicate -- with the gradient-saturation and
scale-selection reinterpretations both closed (out-of-validity; genuine `k=0` instability), and the
"feature" framing refuted (SIGN-FREE, so the tachyon is neither forced by attraction nor
structurally inevitable). The flaw count does NOT drop; the W156 convergent story does NOT clear
bar (b) by these routes.

**Updated bar-(b) status: UNCHANGED.** Consistent with W157: debit-1 remains an independent debit;
the substrate/record arc's convergent story is strongly unifying but still carries its three
standing debits, and bar (b) is not cleared. The one genuine remaining lever on debit-1 is the E2
fork itself -- a GU-native UV selector plus the strong-coupling passage computation -- exactly the
paper-scale item W128/W130 named, and not something one-loop machinery can settle.

## 8. Gates and honest limits

- Exploration grade; conditional register throughout. Nothing asserts GU, asserts a vacuum, or
  changes any verdict. The results are computed refutations of three benign-ification stories, with
  W126 + W128 + W130 positive controls, not assertions.
- W138 battery honored: every route verdict binds to GU-specific objects (the W130 native tree
  point and couplings, the W126 gradient closed form, the `|H|^2` decomposition, the spin-block
  structure). The tempting stories the geometry FORBIDS are recorded: "aim for AS to dodge the
  passage" (forbidden -- shared spin-2 wall), "the gradient quartic saturates the runaway"
  (forbidden -- speed-limit + out-of-validity), "attraction forces the tachyon" (forbidden --
  `det != 0`).
- Tri-repo gating held: record/finality/capability semantics stay pointers to
  temporal-issuance / time-as-finality / TaF; GU owns the induced-action math only.
- No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the debit count is
  unchanged; H59/H61a OPEN; the E2 AF/AS fork CARRIED, not closed. No forbidden target assumed or
  inserted. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by Team TACHYON-ESCAPES (W159). Coherence-first; the two genuine escapes plus
the sign-forcing residual, after the W157 keystone failed. Five personas inline in one worker
(FRG/branch specialist, nonlinear-saturation theorist, higher-derivative/dispersion theorist,
symbolic/numerical engineer, adversarial skeptic); no sub-agents. Reproducible:
`python -u tests/W159_tachyon_escapes.py` (16/16, exit 0; W126 + W128 + W130 positive controls
first). Exploration grade; conditional register; no canon movement.*
