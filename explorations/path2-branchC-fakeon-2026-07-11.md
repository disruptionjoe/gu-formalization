# Path 2, Branch C -- the fakeon prescription (Anselmi-Piva) on the Stelle spin-2 ghost

**Status:** exploration-grade, single blind branch of the loop-unitarity wave. GU-INDEPENDENT by design
(uses the Stelle massive spin-2 graviton as the concrete example; the verdict decides the whole
Stelle/conformal/agravity class, not GU alone). No claim-status/canon/verdict file touched. This branch
was run blind to the other branches; nothing here references or synthesizes across them.

Deterministic companion test: `tests/W50_path2_C_fakeon.py` (15/15 checks, exit 0).

Ran as a single worker with a 5-persona team INLINE (specialist -> referee -> adversary -> cross-checker
-> synthesizer), per the standing personas-always-inline rule.

---

## 0. Construction forks stated up front (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Two load-bearing objects have rival constructions; I name which I use and why.

- **"The ghost."** Branch C constructs it as a **FAKEON**: a degree of freedom REMOVED from the physical
  spectrum by an average-continuation prescription on its propagator/loop integrals. This is a THIRD
  construction, distinct from **both** (i) the standard-physics "genuine negative-norm ghost" (a state in
  the Krein/indefinite space that you then have to tame) and (ii) GU's program-native **keep-and-grade**
  Krein state (`[P,S]=0`, Bateman-Turok hidden parity), which KEEPS the state and grades it. The fakeon
  and GU's Krein object give the **same tree S-matrix** but are **different objects**: the fakeon has no
  associated asymptotic state at all, GU's graded ghost does (with graded norm). Branch C deliberately
  does **not** use GU's Krein construction -- it is the rival "remove-by-prescription" route. Per the
  fork rule, this branch's result is a result *in the fakeon construction*; whether it transfers to GU's
  Krein construction is a separate question the orchestrator must not assume.
- **"Unitarity."** Constructed **by prescription**, not derived. The fakeon is *defined* to be absent from
  the cuts, so the projected S-matrix is unitary by construction. The referee persona holds this at
  arm's length throughout: the interesting content is not "is it unitary" (yes, tautologically) but
  "does a consistent, Lorentz-invariant, RG-stable such prescription exist, and what does it cost."

---

## 1. Persona 1 -- Fakeon specialist: the prescription, concretely, on the Stelle ghost

The 4th-order (Stelle) spin-2 sector propagator has the schematic partial fraction

```
      1                 1   [  1        1     ]
-------------------  =  --- [ ---  -  ------- ]
  p^2 ( p^2 - m2^2 )    m2^2[ p^2     p^2-m2^2]
```

The first term is the ordinary massless graviton; the second is the **wrong-sign** (negative residue)
massive spin-2 pole at `p^2 = m2^2` -- the ghost. Under the ordinary Feynman prescription
`1/(p^2 - m2^2 + i eps)`, this pole goes **on shell** inside loops. By Sokhotski-Plemelj,

```
  1/(x + i eps) = PV(1/x) - i pi delta(x),        x := p^2 - m2^2,
```

so the Feynman line carries an absorptive `-i pi delta(p^2 - m2^2)` -- and that delta is *exactly* the
on-shell piece a Cutkosky cut collects. Because the residue is wrong-sign, the ghost's cut contribution
enters the optical theorem with the wrong sign -> negative probability -> the textbook unitarity kill.

**The fakeon average continuation** replaces the ghost denominator by the arithmetic average of the two
continuations around its threshold:

```
   1                 1 [    1              1        ]
------- |_fakeon  =  - [ --------  +  ---------- ]  =  PV ( 1 / (p^2 - m2^2) ).
 p^2-m2^2            2 [ x + i eps      x - i eps  ]
```

By Sokhotski-Plemelj the two `∓ i pi delta` halves **cancel exactly**, leaving the pure Cauchy principal
value: a **real** function of real `p^2` with **no delta / no absorptive part**. The fakeon cannot go on
shell. Lifted to the loop amplitude as a function of the external invariant `s`, the same average is
applied at the fakeon *production threshold*: the fakeon threshold produces **no branch cut in `s`**.
That is Anselmi-Piva's defining move.

Test coverage (`W50` block A): `fakeon_denominator(x, eps)` is verified to have `Im == 0` for all real
`x` and every finite `eps` (A1, `max|Im| = 0`), while the Feynman line carries a nonzero nascent delta on
shell (A2); the two share an identical real (dispersive) part (A3). So the *entire* content of the
prescription lives in the removed absorptive part.

## 1b. Persona 1 -- the one-loop bubble (Q-cut arithmetic)

Take the one-loop scalar self-energy bubble in dispersive form, spectral density = the two-body phase
space of masses `(m1, m2)`:

```
  rho(s) = (1/16 pi) * sqrt(lambda(s, m1^2, m2^2)) / s ,   s > (m1+m2)^2 ,
  lambda(s,a,b) = (s-a-b)^2 - 4 a b   (Kallen).
  Pi(s) = \int ds' rho(s') / (s' - s - i eps) (+ subtractions),   Im Pi(s+i0) = pi rho(s).
```

Concrete numbers used in `W50` block B: `m1 = 1`, ghost/fakeon mass `m2 = 3`, external `s = 24`
(> threshold `(1+3)^2 = 16`, so a cut is genuinely open). Then `lambda(24,1,9) = 14^2 - 36 = 160`,
`rho = sqrt(160)/(16 pi * 24) = 0.010485`, `pi rho = 0.032942`.

- **phys+phys line** (ghost quantised the ordinary way): the bubble reproduces the known two-body cut,
  `Im Pi = 0.03291` vs `pi rho = 0.03294` (B1) -- standard Cutkosky/optical theorem, cut present.
- **phys+FAKEON line** (ghost quantised as a fakeon): applying the average continuation to the same
  bubble gives `Im Pi = 0.0` **exactly** (B2) -- the fakeon is absent from the unitarity cut. The `∓ i eps`
  halves cancel termwise, so this is exact, independent of `eps` and the grid.
- The two amplitudes differ **only** in the cut: their real parts agree to quadrature accuracy
  (`Re = 0.07367` both, B3). Below threshold neither has a real cut (B4), so B2 is the fakeon removing a
  cut that *would* be open, not a below-threshold artifact.

**=> Q-cut = YES, by construction, verified arithmetically.**

## 2. Persona 2 -- Math-physics referee: what is proven vs argued

- **Q-cut is TRUE BY CONSTRUCTION, not derived** (graded: *proven-but-tautological*). The fakeon is
  *defined* to have no absorptive part; B2 is a consistency check on the arithmetic of the definition, not
  a discovery that unitarity emerges. The referee's standing flag (test E1): do not let "the S-matrix is
  unitary" read as a theorem about a positive-norm state space -- there is no positive-norm asymptotic
  ghost state here at all; the state was removed. The honest, non-trivial content Branch C actually
  decides is: (a) that such a prescription *exists* and is Lorentz-invariant (block D4) and RG-stable
  (Q-pos below), and (b) its **causality price**.
- The one-loop bubble is a **scalar toy**; the Stelle spin-2 tensor algebra, gauge-fixing, and the RS
  (ker-Gamma) sector are not computed here. The *cut-removal mechanism* is tensor-structure-independent
  (it acts on the scalar denominator `p^2 - m2^2` common to every spin-2 numerator), so the Q-cut result
  is expected to survive dressing; but "expected" is argued, not proven.

## 3. Persona 3 -- Adversary: is the causality violation actually fatal? frame/regulator dependence?

Attack 1 -- **regulator/frame dependence.** Could Q-cut be an artifact of the `i eps -> average` choice or
of a preferred frame (the failure mode that sinks naive Lee-Wick contour prescriptions)? No: the average
continuation is a rule on the **Lorentz scalar** `p^2` alone, so it is manifestly Lorentz invariant and
frame independent (D4). It is also regulator-robust: the cancellation of the `∓ i pi delta` halves is
algebraic (Sokhotski-Plemelj), not a property of a particular UV regulator -- verified `eps`- and
grid-independent in `W50` (the fakeon `Im` is exactly 0 for every finite `eps`). This attack fails; the
prescription is genuinely covariant. That is precisely what makes it more attractive than Lee-Wick.

Attack 2 -- **is the causality violation fatal?** This is where the branch bleeds. The average
continuation is **non-analytic** across the fakeon threshold: it glues the two continuations rather than
selecting the causal (retarded) one, so the amplitude does **not** satisfy the Feynman analyticity that
guarantees micro-causality. Its position-space transform does **not** vanish outside the light cone.
Consequence: **local commutativity fails at spacelike separation**, inside a region of linear size

```
  Dx_acausal  ~  1 / m2      (the fakeon Compton length; W50 block D verifies the 1/m2 scaling, D1).
```

- If `m2 ~ M_Planck` (the natural Stelle spin-2 ghost mass in pure 4th-order gravity, where
  `m2^2 ~ M_P^2 / f_2^2`): `Dx ~ 1.6e-33 cm ~ Planck length` (D2). Unobservable, below any probed
  distance -> **controllable, NOT fatal to the effective theory**.
- If the fakeon is **light** (D3 uses a 1 GeV strawman): `Dx ~ 2e-14 cm`, macroscopic relative to
  Planck (1e19x larger). Micro-causality violation becomes physical -> **fatal**.

So the causality violation is **real and permanent**, but its lethality is **conditional on `m2`**. The
adversary's honest verdict: not fatal *as an EFT statement at the Planck cutoff*, fatal *as a claim of a
fundamentally micro-causal theory* and fatal outright if phenomenology ever forces `m2` down.

## 4. Persona 4 -- Cross-checker: independent derivation + the known Anselmi result

Independent recomputation of the fakeon amplitude as a genuine Cauchy **principal value**, via a
symmetric subtracted quadrature that never uses any `i eps` at all (skips the singular cell so its
symmetric neighbours cancel the pole): `PV = 0.07370` reproduces the fakeon bubble's real part
`Re = 0.07367` to quadrature accuracy (`W50` C1), and is real by construction (C2). This is exactly
Anselmi's characterisation: **the fakeon loop integral is the average = the principal value of the
ordinary integral**, i.e. the cut-free real part. Two independent routes (the `∓ i eps` average and the
PV quadrature) agree -> the arithmetic is not an artifact of one method. This is the two-derivations
discipline the gravity arc adopted after the `M^2/r^2` bug.

Known-result anchor: in Anselmi-Piva's scalar/Yukawa fakeon models the prescription (i) gives a unitary
`S`-matrix on the physical subspace (fakeons never in cuts) and (ii) violates micro-causality only within
`~1/m_fakeon`. Our toy reproduces both features qualitatively and the cut-removal exactly.

## 5. Persona 5 -- Synthesizer: the branch verdict

**Q-cut -- YES, BY CONSTRUCTION (verified).** Confidence HIGH on the mechanism, but explicitly
tautological: the fakeon is *defined* cut-absent; the bubble arithmetic confirms the definition is
self-consistent and covariant. Grade: *proven-but-by-construction* (scalar toy; spin-2 dressing argued).

**Q-pos -- YES (ARGUED).** The particle-vs-fakeon classification is fixed by the **sign of the pole
residue / quadratic term**, which counterterms do not flip in the relevant scheme; hence the prescription
is renormalization-group stable and can be imposed order by order (Anselmi's "the fakeon stays a
fakeon"). One-loop explicit; all-orders inherited from the theory's power-counting renormalizability (the
UV arc's H58). Confidence MEDIUM-HIGH. Caveat: this is *survival of a prescription* under RG, **not** the
existence of a positive-norm Hilbert space -- there is no ghost state to make positive; it was removed. So
Q-pos here means something weaker than in the keep-and-grade constructions: "the removal is RG-consistent,"
not "a positive physical inner product survives renormalization."

**Q-caus -- NO (the price), but BOUNDED.** Micro-causality (local commutativity at spacelike separation)
is **violated**; Lorentz invariance is **retained**. The a-causal region has linear size `Dx ~ 1/m2`.
CONTROLLABLE / unobservable (Planck-scale) **iff** `m2 >~ cutoff/Planck`; **FATAL** if the fakeon is
light. This trade -- **buy loop unitarity by construction, pay with micro-causality at `~1/m2`** -- is
Branch C's central finding, and the by-construction unitarity must not be allowed to hide it.

**The trade, precisely:** the fakeon does not *rescue* the ghost's unitarity so much as *trade* the
ghost's unitarity problem for a causality problem of controlled size. Whether that is a cure or a
relabeling depends entirely on whether `1/m2` is below every scale you will ever probe.

- **Load-bearing assumption:** `m2` (the Stelle spin-2 fakeon mass) sits at or above the cutoff/Planck
  scale, so `Dx ~ 1/m2` is sub-Planckian and unobservable.
- **One-killing-obstruction:** any physics that forces `m2` **below** the cutoff makes the a-causal
  region macroscopic and the micro-causality violation observable -> the construction dies. (In GU
  specifically, note that the induced-`|II|^2` sector's rotation-curve fit engages a particular
  gravitational scale; if that or any RS/phenomenology constraint pins the spin-2 mass low, Branch C's
  fakeon is falsified on causality. This is the obstruction to watch.)
- **The one computation that would firm it:** the spin-2 + ker-Gamma-RS one-loop self-energy with the
  fakeon prescription on the *actual* Stelle numerator (not the scalar toy), confirming (a) cut-removal
  survives the tensor/gauge structure and (b) the induced value/range of `m2` relative to the cutoff --
  which decides whether the causality price is Planckian or fatal.

**Fork note for the orchestrator:** this verdict lives in the *fakeon* construction of the ghost
(remove-by-prescription), NOT GU's *keep-and-grade* Krein construction. The two agree at tree level and
diverge at loops. Do not port Branch C's "Q-cut YES" onto the Krein object without a separate check: in
the Krein construction the ghost state still *exists* (graded), so its loop cut is a genuinely different
question. Branch C decides the fakeon route; it is silent on whether GU's native Krein route needs it.

---

## Deliverables
- This exploration: `explorations/path2-branchC-fakeon-2026-07-11.md`
- Deterministic test: `tests/W50_path2_C_fakeon.py` (15/15 checks, exit 0) -- encodes the prescription,
  the Sokhotski-Plemelj cancellation, the one-loop bubble (cut present phys+phys / cut absent
  phys+fakeon), the PV cross-check, and the quantified `Dx ~ 1/m2` causality scale as assertions.
