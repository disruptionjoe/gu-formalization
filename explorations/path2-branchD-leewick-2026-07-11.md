# Path 2, Branch D -- the Lee-Wick / complex-pole construction of the Stelle spin-2 ghost

**Wave:** Path-2 loop-positivity blockbuster (H59), blind branch D. **Framing:** GU-INDEPENDENT (Stelle
massive spin-2 graviton as the concrete example; the verdict is meant to decide the whole Stelle/conformal/
agravity class, GU included but not required). **Grade discipline:** every claim tagged proven / argued /
assumed. **Deliverable pair:** this file + `tests/W51_path2_D_leewick.py` (deterministic, exit 0).

This branch is blind to the other branches (Cutkosky, PT/C-operator, fakeon, red-team). It reports only its
own construction's graded verdict; the orchestrator synthesizes across branches.

---

## 0. Construction forks used (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Two load-bearing objects have rival constructions. I NAME which I use and why.

- **"The ghost."** Standard construction: a *stable negative-norm asymptotic state* (the textbook Stelle
  ghost). Branch-D construction: a **Lee-Wick complex-pole resonance** -- the ghost is *not* an asymptotic
  state at all; interactions push its propagator pole off the real axis into a complex-conjugate pair, so it
  never appears in an in/out basis. I use the Lee-Wick construction. Reason: it is the only one of the two on
  which "does the ghost spoil a physical cut?" can even be posed as a computation rather than assumed -- and
  the test of the construction is precisely whether the *real dynamics* (the one-loop self-energy) actually
  realize it. This is NOT the GU-native Krein keep-and-grade object; it is a distinct physics construction
  (the pole moves; the norm question is dissolved, not graded). Stated so the orchestrator can cross-file it
  against the Krein branch.
- **"The cutting rules."** Standard construction: Cutkosky rules cutting real-axis on-shell poles.
  Branch-D construction: **Lee-Wick / Grinstein-O'Connell-Wise (GOW) cutting rules** deformed around the
  complex-conjugate poles (CLOP prescription: Cutkosky-Landshoff-Polkinghorne, Coleman contour). I use the
  deformed rules. Reason: with the poles off-axis the naive real-axis cut through the ghost line is empty; the
  physical discontinuity is carried only by real (positive-norm) intermediate states.

Note on the GU fork table: GU's own row is "keep-and-grade the ghost via the Krein form `[P,S]=0`." Lee-Wick
is a THIRD option -- neither remove (SUSY/Hilbert) nor keep-and-grade (Krein) but *dynamically destabilize*.
I do not assert Lee-Wick is GU's mechanism; I test whether the Stelle ghost *admits* it, which is a
GU-independent statement about the class.

---

## 1. The team (5 personas, run inline, sequential)

### Persona 1 -- Lee-Wick specialist: the pole-displacement computation and the GOW cut

**Setup.** In the spin-2 sector the Stelle propagator is, with `M` the massive-spin-2 mass,

```
D(p^2) = (1/M^2) [ 1/p^2  -  1/(p^2 - M^2) ]  x  P^(2)_{munu,rhosigma}
```

partial-fractioned from `1/(p^2 (p^2 - M^2))`. The massless graviton pole has residue `+1/M^2`; the massive
pole has residue **`-1/M^2`** -- the relative minus sign is the ghost (wrong-sign kinetic term / negative
Krein norm). (proven -- this is the standard Stelle decomposition.)

**Step 1: does the pole go complex, and in which direction?** Dress the massive pole with the one-loop
self-energy `Sigma(p^2)`. The dominant channel is the massive spin-2 decaying into **two massless gravitons**
(in the matter-coupled theory, also into two massless matter quanta). The one-loop bubble discontinuity of a
two-massless-line loop is the standard result

```
Im B0(s; 0,0) = 1/(16 pi)     for s > 0,   0 for s < 0.
```

The gravitational vertices are derivative (two derivatives per vertex), so the spin-2 -> 2-massless vertex
contributes a positive tensor/momentum factor `c * s^2` (c>0, a spin-2 phase-space + polarization-sum
factor). Hence

```
Im Sigma(s) = (kappa^2 / 16 pi) * c * s^2 * theta(s),   c > 0, kappa real.
```

Evaluated at the ghost mass (`s = M^2`, which is ABOVE the two-massless threshold `s_th = 0` -- the massive
spin-2 is the *heaviest* state and can always decay down):

```
Im Sigma(M^2) = (kappa^2 c / 16 pi) M^4  >  0.        (RIGHT DIRECTION: nonzero, off-axis)
```

The dressed massive inverse propagator `p^2 - M^2 - Sigma(p^2)` then has its zero at

```
p^2_pole = M^2 + Re Sigma  +/-  i Im Sigma(M^2),
```

a **complex-conjugate PAIR** (`p^2_+ = conj(p^2_-)`), forced by reality/hermiticity of the Lagrangian. The
width is `Gamma = Im Sigma(M^2)/M = (kappa^2 c /16 pi) M^3`. **Result: for the Stelle graviton the ghost pole
DOES leave the real axis, in the direction that makes it a resonance (Im Sigma > 0), and it comes as a
conjugate pair.** (proven at one loop, given `c>0` and above-threshold -- both of which hold: the sign of the
massless bubble discontinuity is fixed, and the ghost is the heaviest mode.)

This is the branch's central positive finding and it is NOT automatic: had the ghost been the *lightest*
state (below all thresholds) `Im Sigma(M^2)` would vanish, the pole would stay pinned to the real axis, and
the ghost would remain a stable negative-norm asymptotic state -- Lee-Wick would be unavailable. Gravity
escapes that failure mode because its ghost sits at the top of the spectrum.

**Step 2: the GOW cut / optical theorem on real external states.** Take a one-loop physical amplitude
(matter + matter -> matter + matter with a ghost line in the loop). The physical discontinuity is

```
2 Im M(phys->phys) = SUM over real (positive-norm) intermediate states  ∫ dPi |M|^2   >=  0.
```

The would-be ghost cut -- the naive Cutkosky cut through the massive spin-2 line -- would contribute a
NEGATIVE term `-|M_ghost|^2` (negative norm). But under the Lee-Wick/GOW prescription the ghost line has NO
real on-shell pole to cut (the poles are the off-axis conjugate pair); the contour is deformed so the ghost's
contribution to the *physical-state* discontinuity is **zero**. The conjugate pole and its partner contribute
equal-and-opposite residues to the absorptive part, summing to a principal value with no net imaginary part
on real external legs. Net:

```
Im M(phys) = (positive real-state terms)  -  0(ghost, deformed away)  >=  0.
```

Optical theorem holds on real external states. (argued -- proven for the scalar GOW model; for gravity it
inherits the tensor-structure caveat below.)

### Persona 2 -- Mathematical-physics referee: what is proven vs argued

- **Sign of `Im Sigma(M^2)` > 0:** PROVEN (fixed by the sign of the massless one-loop bubble discontinuity
  and positivity of the spin-2 polarization sum; `c>0`). Not an assumption.
- **Pole is a conjugate pair:** PROVEN from reality of the action (`Sigma(p^2*) = Sigma(p^2)*`).
- **Above-threshold (so `Im Sigma != 0`):** PROVEN for the class -- the massive spin-2 is heavier than the
  massless graviton, threshold is at `s=0`.
- **The pole location is a genuine *isolated* resonance:** ARGUED, one-loop only. `Re Sigma` from the
  higher-derivative vertices grows like `s^2` and is UV-sensitive; the resummed propagator can develop
  *extra* structure. That the dressed propagator has exactly one conjugate pair (and not a smeared cut
  mimicking several) is one-loop-plausible, not proven to all orders.
- **GOW optical theorem on real states:** PROVEN for scalar Lee-Wick (GOW 2008; Donoghue-Menezes). For
  gravity it is ARGUED by analogy; the tensor numerator `P^(2)(p)` carries its own `p`-dependence whose
  discontinuity must cancel between pole and conjugate the way a scalar's does. Not independently verified
  here beyond the sign/structure check.
- **Width magnitude:** `Gamma/M = kappa^2 c M^2 /16pi`. With the gravitational `kappa ~ 1/M_Pl`,
  `Gamma/M ~ (M/M_Pl)^2`. If the Stelle ghost sits near the Planck scale (agravity/Stelle default),
  `Gamma/M = O(1)` -- a **broad** resonance, not a narrow one. This is graded as a real weakness (see
  adversary).

### Persona 3 -- Adversary: three attacks on branch D

1. **"The pole moves the wrong way / creates an instability."** For an ordinary particle `Im Sigma>0` puts
   the pole on the second sheet (stable asymptotic states on the real axis). For the *ghost* there is no
   stable asymptotic state to begin with, so BOTH conjugate poles are retained on the physical sheet -- and
   the Lee-Wick contour must be chosen (Coleman/CLOP) so external real amplitudes do not pick up an
   exponentially *growing* mode. At one loop the sign works (Im Sigma>0, above threshold, decaying-resonance
   branch). **But** the CLOP prescription is order-of-limits ambiguous at >=2 loops, and the ambiguity is
   controlled only for *narrow* resonances in renormalizable scalar/gauge theories. Gravity's ghost is broad
   (`Gamma/M = O(1)` at Planckian `M`) and its couplings are dimensionful derivative couplings. **The attack
   lands:** the branch cannot claim the higher-loop CLOP contour is unambiguous for gravity. This is the
   one-killing-obstruction (see synthesizer).
2. **"Derivative vertices spoil the conjugate-pair structure."** Each gravitational vertex is `~ p^2`, so the
   ghost self-energy and the box/triangle numerators grow with momentum. The concern is that the deformed
   contour crosses regions where the integrand's growth produces additional pinch singularities not present
   in the scalar model, re-injecting a ghost cut. At one loop this does not happen (the single bubble is
   controlled); at higher loops it is unproven. ARGUED-open.
3. **"Renormalization moves the pole back."** Counterterms are real; they shift `Re Sigma` (the pole's real
   part / the mass) but cannot remove `Im Sigma` (an absorptive part is not a local counterterm). So
   renormalization cannot pin the pole back onto the real axis. This attack FAILS -- a point in branch D's
   favor for the Q-pos question (below).

### Persona 4 -- Cross-checker: reduce to the known scalar Lee-Wick / GOW result

**Independent check by decoupling limit.** Turn off the derivative nature of the vertices (constant coupling
`g`) and take a scalar Lee-Wick ghost of mass `M` decaying to two massless scalars. Then
`Im Sigma(s) = g^2/(16 pi)` (constant), `Gamma = g^2/(16 pi M)`, poles at `M^2 +/- i g^2/16pi`. This is
EXACTLY the GOW / Donoghue-Menezes scalar Lee-Wick setup, whose known results are: (i) the poles are a
complex-conjugate pair; (ii) the theory is perturbatively unitary on real external states (optical theorem
holds, ghost never in a physical cut); (iii) micro-causality is violated at scale `~1/M` but Lorentz
invariance is preserved. My gravity computation reduces to this in the `c*s^2 -> const`, `Gamma << M` limit
-- the sign, the conjugate-pair structure, and the empty ghost cut all match. **The DELTA that gravity adds
over the passing scalar case is exactly: (a) broad width `Gamma/M=O(1)`, (b) derivative couplings, (c) tensor
numerator.** So the cross-check confirms the *mechanism* and isolates the three gravity-specific risks -- it
does not certify them. (This is the two-derivations discipline: the scalar limit is the known result the
gravity computation must and does reproduce.)

### Persona 5 -- Synthesizer: branch verdict

Branch D used the **Lee-Wick complex-pole construction of the ghost** and the **GOW deformed cutting rules**.
The one-loop self-energy computation shows the Stelle spin-2 ghost pole **does** acquire a complex-conjugate
pair in the right direction (`Im Sigma(M^2) > 0`, above threshold) -- the necessary condition for Lee-Wick is
MET for gravity, and it is met *because* the ghost is the heaviest mode. On real external states the optical
theorem is satisfied at one loop (ghost deformed out of the physical cut). The cost is micro-causality
violation at `~1/M` with Lorentz invariance preserved.

**The branch is a qualified PASS at one loop with a genuine higher-loop obstruction for gravity specifically.**

---

## 2. Graded verdict on the three sub-questions

| Sub-question | Verdict (this construction) | Grade |
|---|---|---|
| **Q-cut** (ghost decoupled from unitarity cuts at one loop) | **YES at one loop.** The dressed ghost pole is off the real axis (`Im Sigma(M^2)>0`, proven sign), so the naive ghost cut is empty and the deformed GOW cut carries only positive-norm real states -> optical theorem holds on real externals. | one-loop PROVEN for the sign/structure; the tensor-cut cancellation ARGUED (inherited from scalar GOW). **Grade: B (strong one-loop, not all-orders).** |
| **Q-pos** (physical prescription survives renormalization) | **REFRAMED, and survives at one loop.** Lee-Wick has no positive-definite Krein subspace to preserve; the "prescription" is the complex-pole contour + exclusion of the ghost from asymptotic states. Counterterms are real and cannot cancel the absorptive `Im Sigma`, so renormalization cannot pin the pole back on-axis (adversary attack 3 fails). BUT all-orders stability of the CLOP contour is unproven for gravity. | one-loop PROVEN (pole cannot return); all-orders ARGUED-open. **Grade: C+ (mechanism robust at one loop; higher-loop prescription unproven).** |
| **Q-caus** (Lorentz invariance + micro-causality) | **Lorentz invariance YES; micro-causality NO.** Unitarity is bought at the price of causality: acausality on scales `~1/M` (Planckian for the Stelle ghost), argued not to produce macroscopic paradoxes (Coleman/GOW), Lorentz-covariant conjugate pair. For gravity the acausal region is Planck-sized and field-dependent -- the weakest but not fatal point. | Lorentz-invariance PROVEN (covariant pair); micro-causal violation is a KNOWN intrinsic feature (argued-tolerable). **Grade: C (causality is traded, honestly priced).** |

---

## 3. Confidence, load-bearing assumption, the one obstruction

- **Overall confidence:** MODERATE. The mechanism is real for gravity at one loop and the pole-displacement
  sign is *proven* (not assumed) -- that is the hard, checkable part and it comes out favorably. The verdict
  is capped at one loop and by the gravity-specific caveats.
- **Load-bearing assumption:** that the **CLOP / Lee-Wick contour prescription remains unambiguous and pinch-free
  at two loops and beyond for a BROAD (`Gamma/M = O(1)`), derivative-coupled, tensor gravitational resonance.**
  This is proven for narrow scalar/gauge Lee-Wick resonances and *assumed* (not proven) for gravity.
- **The ONE obstruction that would kill this construction:** a demonstration that at >=2 loops the
  higher-derivative gravitational vertices create a **pinch of the deformed contour** (or a CLOP
  order-of-limits ambiguity that does not cancel), re-injecting the ghost into a physical cut -- i.e. the
  complex-pole prescription is not well-defined for the broad gravitational resonance, so "unitarity on real
  states" becomes prescription-dependent. If that pinch exists, branch D fails *for gravity* even though the
  scalar Lee-Wick model passes. The one-loop computation cannot see it; a two-loop CLOP-stability computation
  would decide it.

**Bottom line, GU-independently:** the Stelle spin-2 ghost **genuinely admits the Lee-Wick treatment at one
loop** -- the pole goes complex in the right direction and the optical theorem holds on real states -- but
whether the gravitational derivative vertices preserve the complex-pole unitarity proof beyond one loop is
the open, potentially fatal, question. Branch D is a one-loop proof-of-concept, not an all-orders proof, and
the honest risk is concentrated at the broad-resonance / higher-loop CLOP contour.
