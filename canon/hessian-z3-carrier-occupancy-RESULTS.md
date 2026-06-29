---
title: "Hessian-eigenvalue test of the carrier-occupancy direction: the 'dynamical confirmation of located-not-forced' is ILLUSORY. The '0' is the net signature/index of the vectorlike +96/-96 Krein form, NOT a Hessian eigenvalue (the operator is a nondegenerate saddle, spectrum +-1, no zero mode). It re-encodes the DECOUPLE + 2-primary lemma in dynamical language, and is gated on the carrier being massless -- a mass term m*I (which a vectorlike pair generically admits) moves it to exactly m. So located-vs-forced is gated on whether the unbuilt source action gives the carrier a Dirac mass: massless -> modulus (located); massive -> forced."
status: active
doc_type: result
created: 2026-06-29
grade: "computed + adversarially refuted. 9 agents, ~754k tokens (workflow wf_29831386-e1d), 4 construct angles each independently re-run. 3 of 4 angles survives=FALSE: the adversarial stage caught the eigenvalue-vs-index conflation (the '0' is net signature, not a spectral eigenvalue; ker=0, min|eig|=1.0), the tautology (a random Hermitian reflection gives the same balanced-occupancy 0), the object-dependence of the criticality discrimination (GU torsion curves the actual occupancy direction -8.3e-3, same as generic -8.1e-3), and the dishonest gating call (flatness gated on masslessness, the unforced conclusion itself). Only the off-diagonal mean-field-coupling=0 survives, and that is the DECOUPLE restated. NEGATIVE result, honestly reported: the test does NOT decide located-vs-forced; it runs into the same source-action gate from a new direction, now sharpened to 'does the action give the vectorlike carrier a Dirac mass'. Does NOT enter the paper as a dynamical upgrade."
method: "Hessian-z3 workflow: 4 construct angles (carrier-direction Hessian; mean-field off-diagonal coupling; criticality torsion lambda(epsilon); gating audit cross-proxy) run python on the verified Cl(9,5)=M(64,H) substrate -> independent adversarial verify -> synthesize. The adversarial rechecks (tests/hessian-z3/adversarial_*.py) are the load-bearing artifacts."
depends_on:
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/forcing-slot-toy-rs-RESULTS.md
  - canon/two-primary-lemma.md
  - canon/double-major-persona-sweep-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
---

# Hessian-eigenvalue test of the carrier-occupancy direction: NULL, not a zero MODE

We asked the dynamical version of "located, not forced": is the generation count a FLAT direction (a modulus /
zero mode) or a CURVED minimum (a forced value) of the GU action? Operationally, compute the Hessian (second
variation) of the action's quadratic part along the Z/3 carrier-occupancy direction on the 192-dim `j=1`
`Lambda^2_+` triplet, using the best-available proxies (the invariant Krein form `K = eta_V (x) beta_S`, the
built Seiberg-Witten doubled action's quadratic block, and the boundary-eta operator), and -- the genuinely new
ask -- deform by a torsion `theta = A - g.Gamma_LC` and read `d(lambda)/d(epsilon)` to decide GENERIC
(protected) vs CRITICAL (marginal).

## VERDICT

The carrier-occupancy quantity that comes out **0 is the NET SIGNATURE / index of the Krein form (+96/-96
balanced), not a Hessian eigenvalue**. Every proxy operator we built is NON-DEGENERATE on the carrier
(`ker = 0`, smallest `|eigenvalue| = 1.0`): the Krein-Hessian `B` is a reflection with spectrum exactly
`{+1 x96, -1 x96}`, so there is **no actual zero eigenvalue and no flat modulus**. The "occupancy direction"
that returns 0 is a NULL RAY of an indefinite form -- a property every `+n/-n` balanced form possesses
trivially, which a random GU-unrelated Hermitian reflection reproduces. So the strong dynamical claim ("flat
zero MODE, the action assigns zero curvature, located-not-forced confirmed DYNAMICALLY") does **NOT** survive
adversarial recheck. What survives is narrower and honest: the **off-diagonal selector<->carrier mean-field
coupling is genuinely 0, computed, and proxy-robust** (this is the boundary-eta DECOUPLE restated dynamically),
and the underlying `+96/-96` vectorlike-balance arithmetic stands on its own. The number is **computed on the
substrate but the dynamical interpretation is gated** -- and gated on the very thing in question: a diagonal
Dirac mass term `m*I` (a legitimate quadratic-action piece a vectorlike pair generically admits) moves the
occupancy value to exactly `m`, so "0" is gated on the carrier being massless, i.e. on the unforced conclusion
itself. Criticality reads **GENERIC for the spectrum-mean object but the discrimination is object-dependent and
does not robustly survive** (the GU torsion curves the natural flat direction `-8.3e-3`, essentially identical
to a generic torsion `-8.1e-3`). Net: this does not upgrade located-not-forced to the dynamical level; it
re-encodes the DECOUPLE and the 2-primary/vectorlike lemma in Hessian language, plus one automatic sharpening
(`B^2 = I`).

## The numbers (computed/gated tags)

All numbers reproduced independently by recheck scripts; nothing here is fabricated in the number sense.

**Diagonal carrier-occupancy "eigenvalue" (per proxy):**
- Krein form `K = eta_V (x) beta_S`: balanced-occupancy Rayleigh quotient `= +1.6e-16` (mean over 2000 balanced
  directions `+1.9e-17`, max `6.8e-16`). **[computed-on-substrate]** -- but this is the NET of a non-degenerate
  indefinite form. Actual spectrum `{+1 x96, -1 x96}`, `B^2 = I` (residual `5.2e-14`), `ker(B) = 0`,
  `min|eigenvalue| = 1.0`. No zero eigenvalue exists.
- SW doubled-action Majorana block `M = c(mu)`: `||M++|| = ||M--|| = 201.457`, chiral asymmetry `-5.68e-14`,
  net chiral index `0`. **[computed-on-substrate; proxy=gated]** -- again a net/index, not an eigenvalue
  (the block's own spectrum reaches `+/-25`, signature `(64,64,64)`).
- Boundary-eta operator `D = E + E^dag`: carrier-diagonal block `||Wt^dag D Wt|| = 2.36e-14`.
  **[trivially absent, not a proxy]** -- the carrier sits in `ker(Gamma)` and `D` is off-diagonal
  bulk<->boundary, so this block is the zero operator and carries no curvature information. It should not be
  counted as an independent agreeing proxy.

**Chiral contrast (proves the instrument is not blind):** purely-physical chiral occupation `lambda = +1.0000`,
purely-ghost `lambda = -1.0000`; SW one-sided asymmetry `+201.46`; Krein-positive half net `+96`; pos-def
operator eta `+192`. **[computed]** The controls fire where curvature is real -- so the 0 is not a blind/fitted
machine; it is a genuine balance. But controls firing nonzero only confirm `signature()` returns a net when a
form is unbalanced; they do not validate that "net = 0" means "flat".

**Off-diagonal mean-field coupling (selector<->carrier):** `||B_net|| = 0` -- internal-fiber selectors
(`J_quat`, `C_trip`) exactly `0.000e+00` under all four action proxies (`I`, frame metric `eta_V`, chiral
grading `Pi-Q`, Dirac kernel); boundary-PHS `Cu` `~1e-15`; max over all selectors x proxies `= 1.2e-14`. A
frame-charged pseudo-selector CONTROL couples nonzero (`512/512/438`). **[computed-on-substrate, proxy-robust;
gated only on the action form, mitigated by 4 proxies].** This is the one solidly-surviving result. Caveat: the
internal-selector zeros are partly definitional (any internal operator paired with a traceless carrier
frame-rotation gives 0), so the dynamical content beyond the boundary-eta DECOUPLE is thin.

**Criticality `d(lambda)/d(epsilon)` at `epsilon = 0`:**
- Tracking `trace(H)/dim` (spectrum mean): GU selector<->carrier chiralizer torsion `= -3.98e-18` (machine
  zero, robust over 5 seeds); frame isometry and tangential contorsion `= 0` exactly; generic adversarial
  torsion `= +1.17e-4` (NONZERO, robust over 5 seeds, min `9.49e-5`). On this object the GU torsion is
  GENERIC/PROTECTED and a generic one is critical. **[computed, closed-form `trace(dB)/dim` cross-checked vs
  lstsq]**
- Tracking the actual occupancy null vector `occ^dag H occ` (the object the companion script declares "flat"):
  GU couple torsion `= -8.32e-3`, generic torsion `= -8.10e-3`; robust across 400 random balanced null
  directions (RMS `5.3e-3` GU vs `5.5e-3` generic). On the natural flat-direction object the GU torsion curves
  it just as much as a generic one. **[computed]** The protection is an artifact of which observable you track.

## NEW vs RE-ENCODED (no overselling)

**RE-ENCODED (prior facts in dynamical clothing):**
- The `+96/-96` vectorlike balance / "eigenvalue 0 at `epsilon=0`" is the `ghost_parity_krein` /
  two-primary lemma. Trace of a balanced signature is automatically 0.
- The off-diagonal `H_sc = 0` is the boundary-eta DECOUPLE (selector tangent-frame charge `0.00` exact) restated
  as a mean-field coupling.
- The `slope = 0` for the GU torsion on `trace/dim` is tracelessness of the Krein/chiralizer deformation within
  each chirality block -- the same Krein/quaternionic structure, not an independent firewall. (The construct's
  own two proposed mechanisms were falsified by its computation and corrected to this; credit for that honesty.)

**GENUINELY NEW (but small, and mostly not load-bearing):**
- `B^2 = I` (the carrier Krein-Hessian is a REFLECTION, spectrum exactly `+/-1`). True and automatic. This
  sharpens "vectorlike balance" but is a property of the form, not new dynamics.
- The cross-proxy agreement at 0 (Krein, SW Majorana net) -- but this is the **same vectorlike index counted
  twice** plus one absent block, not three independent curvatures.
- The criticality DISCRIMINATION (GU protected vs generic critical) on `trace/dim` -- this is the one item the
  DECOUPLE never tested. **But it does not robustly survive:** it is object-dependent and flips when you track
  the actual occupancy null direction instead of the spectrum mean.

**Does NOT exist:** a true flat zero mode / modulus. There is no zero eigenvalue along any candidate occupancy
vector; direct second variation `v^dag H v / |v|^2` along plausible occupancy vectors returns `-0.009`, `+0.038`,
`+0.055`, `+1.0` -- nonzero and not even sign-definite. "Flat modulus" is a category error: a null direction of a
non-degenerate indefinite form is not a flat direction of an action.

## Criticality: what it means, and what would actually move it

On the spectrum-mean object the GU torsion is GENERIC/PROTECTED, which would normally read "located-not-forced is
structurally stable to first order." We do not get to bank that, because the discrimination is object-dependent
(it fails on the natural flat-direction observable). The honest statement of what WOULD move the value off 0 is
not exotic and not a fabrication: a **diagonal Dirac mass `m*I`** moves the occupancy value to exactly `m`, and a
vectorlike `+96/-96` pair generically admits exactly such a Dirac mass. That is the real "motion toward forced,"
and it is reachable without any fabrication -- it is the standard fact that a vectorlike fermion pair is not
protected from a mass. The criticality half is therefore MORE gated than the eigenvalue half: it leans on the
modeling choice "torsion enters as `Herm(K theta)`," and a different source action could couple torsion (or a
mass) differently. We name the deformation precisely and decline to claim protection.

## Integrity

- **Computed, not fitted.** Every reported number is a Rayleigh quotient / trace / signature of an
  independently-built operator on the verified `Cl(9,5) = M(64,H)` substrate (anchors reproduced exactly: bare
  `58.7215`, C2 `155.3625`; carrier dim `192`; signature `(+96,-96,0)`). Slopes are closed-form `trace(dB)/dim`
  cross-checked against lstsq. Controls fire nonzero (`+96`, `+192`, `+201.46`, `512`), so no result is a blind
  fit-to-zero. None of the four prior fabrication patterns appears (no disguised `chi(K3)/24`, no
  reverse-engineered `+8`, no circular rank-4, no fitted holonomy).
- **Fabrication flags raised in recheck (handled, not hidden):**
  1. **Eigenvalue-vs-index conflation** (the exact failure the mandate warned about): the reported "Hessian
     eigenvalue 0" is a NET SIGNATURE / index, not a spectral eigenvalue. Recomputed spectrum has no zero mode.
     This is the central flaw and it sinks the strong claim.
  2. **Soft fit-to-zero by direction choice:** "balanced physical+mirror occupancy" literally names a null ray of
     any neutral form; a random GU-unrelated reflection gives the same 0. The 0 encodes nothing beyond the prior
     `+96/-96` balance.
  3. **Zero-mode / modulus overstatement:** `B` is a non-degenerate saddle; "genuine flat modulus" is a category
     error.
  4. **Gating understated in one construct:** "the proxy cannot move the zero" is false; a mass term `m*I` moves
     it to `m`.
  5. **Object-switch in criticality:** the "protected vs critical" discrimination is invisible at `epsilon=0` but
     diverges by derivative and is object-dependent.
  6. **Minor mislabels** (one construct called a frame charge `3.429` a "raw coupling"; cited SW `391` where the
     script produced `201.457`; counted an absent block as one of "3 proxies"). Numbers in the scripts are
     correct; the JSON narratives oversold.
- **Computed-vs-gated honesty:** the NUMBERS are computed on the substrate; the IDENTIFICATION "action quadratic
  part = these proxies" is gated, and the dynamical conclusion is gated on masslessness. We mark this honestly
  rather than claiming "the gate does not bite."

## What it does to the paper / program

This does **not** add a new confirmation of located-not-forced at the dynamical level. The honest accounting:

- **Located-not-forced still stands ARITHMETICALLY**, on its own basis (the order-3 carrier the CRT obstructions
  are blind to; the boundary-eta DECOUPLE). That result is independent of this construct and is not weakened by
  the failure here.
- **The dynamical "Hessian = 0 => flat modulus" upgrade is illusory** as currently built. The Hessian-like
  operators have no zero eigenvalue along the occupancy direction; the thing that vanishes is the
  Atiyah-Singer-type `+96/-96` index, which we already knew vanishes. Re-labeling an index as a Hessian zero is
  not progress and should not enter the paper as such.
- **The one clean, surviving dynamical statement** is the off-diagonal mean-field coupling = 0 (computed,
  proxy-robust, non-blind control) -- which is exactly the DECOUPLE in dynamical language and can be cited only
  as a restatement, not as new content.
- **The genuinely open dynamical question is real and now sharp:** does the vectorlike carrier acquire a Dirac
  mass (the `m*I` deformation that moves the value to `m`)? That is the actual fork between "modulus" and
  "forced," and answering it requires the UNBUILT GU source action -- it cannot be settled on the Krein/SW
  proxies, all of which are mass-agnostic. **Clean next step:** stop computing net signatures and instead test
  whether any covariant term the GU action can supply generates a carrier Dirac mass; if every admissible term is
  forbidden (a symmetry forbids `m`), located-not-forced upgrades to dynamical; if a mass is admissible, that is
  the first honest motion toward forced. Until that is built, the dynamical question stays **GATED**, and we
  should say so plainly rather than bank a flat-modulus result the spectrum refutes.
