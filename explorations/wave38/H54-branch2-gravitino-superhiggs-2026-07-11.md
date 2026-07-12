---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 38
branch: "H54 branch 2 of 5 (gravitino / super-Higgs). BLIND to the other four branches."
title: "H54-b2 -- Is GU's Rarita-Schwinger matter a SUPER-HIGGS GRAVITINO, and does that FORCE mu_DW? VERDICT: PARTIAL. GU's RS is gravitino-LIKE in field content (the ker-Gamma cure IS the gravitino's gamma-trace gauge condition; same projector type, same removed spin-1/2 part, same massive-spin-3/2 2s+1=4 on-shell content), but its mass does NOT arise via super-Higgs: GU has no established local-SUSY guardian and no goldstino, so the mass comes from the guardian-free Porrati-Rahman non-minimal cure (a finite-cutoff EFT), NOT from a gravitino eating a goldstino. Identifying mu_DW with a super-Higgs SUSY-breaking scale does NOT force mu_DW -- it trades one free scale (mu_DW) for another free scale (<F>); and pinning <F> to a vacuum energy gives a DIFFERENT power law than GU's DeWitt structure (m ~ rho^{1/2}/M_Pl vs GU's m ~ rho^{1/4}), which forces mu_DW ~ M_Pl (decoupled), not a falsifiable window. mu_DW is NOT forced. The falsifiability keystone (H53) does NOT fall via super-Higgs."
grade: "COMPUTED (exact, deterministic): the gamma-trace projector match (Pi idempotent+Hermitian to 0; rank(Gamma)=4 of 16; ker=12; massive 2s+1=4); the super-Higgs vs GU mass-vs-vacuum-energy EXPONENTS (1/2 vs 1/4, symbolic d ln m / d ln rho); the joint-identification forcing M_Pl proportional to mu_DW; the ~30-order numeric gap between super-Higgs m_3/2 and GU m_RS at the observed vacuum energy. ARGUED (structural / from GU's published record, wave34 + rs_ghost_sugra_gravitino_brst.py): that GU has no established local SUSY and no goldstino (super-Higgs guardian absent); that the cure is therefore the guardian-free Porrati-Rahman type; that GU's cure g-value is not the SUSY g=2. Reconstruction-tier, internal. No canon promotion; no mu_DW movement; H53 keystone unchanged. BLIND to the other H54 branches."
depends_on:
  - tests/wave38/H54b2_gravitino_superhiggs.py
  - explorations/wave16/H39-sourceaction-kclass-2026-07-11.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md
  - explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md
  - explorations/wave32/H53-falsifiability-audit-2026-07-11.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - tests/rs_ghost_sugra_gravitino_brst.py
scripts:
  - tests/wave38/H54b2_gravitino_superhiggs.py
---

# H54 branch 2 -- is GU's RS a super-Higgs gravitino, and does that FORCE mu_DW?

Test: `tests/wave38/H54b2_gravitino_superhiggs.py` (deterministic, no randomness, exact;
16/16 PASS, exit 0). BLIND to the other four H54 branches. Personas run INLINE.

**The branch question.** GU's spin-3/2 matter field (carrier B: index -38, gamma-trace-
constrained `ker Gamma`) needs a forced Porrati-Rahman-type massive-RS cure. Guardian-free it
is a finite-cutoff EFT; UV-completeness needs a guardian symmetry. **Is that guardian local
SUSY -- i.e. is GU's RS secretly a GRAVITINO whose mass arises via SUPER-HIGGS (the gravitino
eating a goldstino), which would set `m_3/2 = mu_DW` and FORCE the free scale, toppling the
H53 falsifiability keystone?** If yes, GU is secretly a supergravity.

**Headline verdict: PARTIAL, and mu_DW is NOT forced.** GU's RS is gravitino-*like* in field
content -- the `ker Gamma` cure IS the gravitino's gamma-trace gauge condition -- but its mass
does not arise via super-Higgs, and the super-Higgs identification does not force `mu_DW`.

---

## Per-persona takes (INLINE)

### Persona 1 -- supergravity / gravitino theorist

The field-content match is real and worth stating plainly. A massless gravitino is the gauge
field of local SUSY, `delta psi_mu = D_mu epsilon`; its physical on-shell content is a
**gamma-traceless** (`gamma^mu psi_mu = 0`), transverse RS spinor-vector. GU carrier B is the
gamma-trace-constrained `ker Gamma` field space. **These are the same projector type.** The
test builds the exact 4D gamma-trace map `Gamma: psi_mu -> gamma^mu psi_mu` in the Dirac basis
and finds: the gamma-traceless projector is exactly idempotent and Hermitian (`||Pi^2-Pi|| =
||Pi-Pi^dag|| = 0`); `Gamma` has rank 4 of 16, so it removes exactly the spin-1/2 "gamma-trace"
part and leaves the 12-dim gamma-traceless subspace; the massive on-shell count is `2s+1 = 4`.
That last number is mechanism-agnostic: a Deser-Zumino massive gravitino and a Porrati-Rahman
cured massive RS land on the *same* 4 causal DoF. So at the level of "what field is this,"
GU's RS wears the gravitino's clothes. The repo already half-knew this: `rs_ghost_sugra_
gravitino_brst.py` explicitly built the gravitino BRST gauge leg `delta psi_a = D_a(eps)` on
the actual Cl(9,5) rep and found nilpotency `s^2=0` **requires** the gauge orbit be gamma-
traceless -- i.e. the gravitino's own gauge condition reproduces GU's `ker Gamma`. My caution:
matching the field content is necessary, not sufficient. A gravitino is not "a gamma-traceless
massive RS"; it is that field **as the gauge field of a spontaneously broken local SUSY**. The
clothes are gravitino; the question is whether there is a body inside them.

### Persona 2 -- spontaneous-SUSY-breaking / super-Higgs specialist

This is where the identification fails to force anything, and the reason is structural, not
incidental. Super-Higgs gives `m_3/2 = kappa <F>/sqrt(3) = <F>/(sqrt(3) M_Pl)`. Crucially,
`<F>` is the **free** SUSY-breaking order parameter -- super-Higgs *relates* the gravitino mass
to `<F>`, it does not *pin* `<F>`. So identifying `mu_DW` with a super-Higgs scale maps one free
symbol to one free symbol: the test confirms symbolically that `<F> = sqrt(3 m2_eff) M_Pl
mu_DW`, a plain reparametrization. **Nothing is forced; the free scale is merely renamed.** The
only way super-Higgs could force `mu_DW` is if `<F>` were independently pinned -- and the
natural candidate is a vacuum energy. Here the mechanisms diverge in a way I can compute. GU's
DeWitt-Lambda is a **single-scale quartic**, `rho_Lambda = c_L mu_DW^4` (so GU-mass `~ rho^{1/4}`).
The super-Higgs SUSY-breaking vacuum energy is a **two-scale product**, `rho_SB = |F|^2 = 3
(m_3/2 M_Pl)^2` (so super-Higgs-mass `~ rho^{1/2}/M_Pl`). The mass-vs-vacuum-energy exponents
are `1/4` (GU) versus `1/2` (super-Higgs) -- verified by `d ln m / d ln rho`. They coincide only
if `M_Pl ~ rho^{1/4} ~ mu_DW`, i.e. a Planckian `mu_DW`. Forcing both identifications at once
pins `M_Pl` proportional to `mu_DW`, which drives `mu_DW` to the **decoupled Planck default**
(H53's natural scale), NOT a falsifiable meV window. And if instead one imports the observed
vacuum energy, the super-Higgs gravitino mass (`~1e-33 eV`) and GU's RS mass (`~meV`) differ by
~30 orders. **Super-Higgs does not force `mu_DW`.** It cannot be the keystone-toppler.

### Persona 3 -- Deser-Zumino massive-gravitino specialist

Is the Deser-Zumino massive gravitino the SAME operator as GU's Porrati-Rahman cure? **No --
same on-shell content, different operator and different principle.** Deser-Zumino: the massive
gravitino obtained after super-Higgs, whose subsidiary condition `gamma^mu psi_mu = 0` is
preserved by the local-SUSY Ward identity -- the guardian keeps the constraint on-shell for
free. Porrati-Rahman: a charged massive RS in an external background made causal by adding
tuned F-dependent non-minimal vertices `A(F), B(F)` that restore secondary-constraint
invertibility **without** any gauge symmetry -- the constraint is imposed, not protected. GU's
cure (wave17/wave34) is unambiguously the Porrati-Rahman type: the built minimal `M_D` leaks
(`C2 = 155.36`, degree-1), and the fix is a non-minimal RS coupling enforcing `ker Gamma` --
imposed, revising the written `(1,0,1,0)` shiab, not descending from a broken local SUSY. The
gyromagnetic discriminator seals it: a SUSY gravitino needs `g = 2` for clean high-energy
behavior (Rahman); GU's cure lives on the RT-trace-dichotomy 1-parameter family `wedge - 6
contract` and is **not** established at the SUSY `g = 2` value in the record. Two operators that
overlap on the causal gamma-traceless massive-RS shell but are built on different principles.
The Deser-Zumino gravitino is the guardian-*present* object; GU's cure is the guardian-*free*
object. They are cousins, not twins.

### Persona 4 -- gravitino-mass phenomenologist

Numbers decide this, and they are brutal. If GU's RS were a super-Higgs gravitino with `<F>`
pinned to the observed vacuum energy `rho_Lambda ~ (2.3 meV)^4`, then `m_3/2 = sqrt(rho/3)/M_Pl
~ 1.3e-33 eV` -- a "cosmological" gravitino, wildly lighter than anything GU's `mu_DW ~ meV`
massive spin-2 sector wants. GU's RS mass, set the same way as the spin-2 (`m = sqrt(m2_eff)
mu_DW`), is `~ meV = ~2.9e-3 eV`. The ratio is `~2.3e30`. So the DE scale cannot simultaneously
be the super-Higgs breaking scale (`m_3/2 ~ 1e-33 eV`) and GU's `mu_DW`-massive scale (`~meV`):
the two mass-generation laws are incompatible at the observed vacuum energy. Conversely, if you
demand `m_3/2 = mu_DW ~ meV` via super-Higgs, you need `<F> = sqrt(3) M_Pl mu_DW ~ (1e12 eV)^2`
-- a ~TeV-ish `sqrt<F>`, a perfectly ordinary free SUSY-breaking scale that has **nothing to do
with** the DE-scale `mu_DW` and pins nothing. Either way the phenomenology refuses to force
`mu_DW`: super-Higgs is a scale-*relating* mechanism, not a scale-*fixing* one. It would only
fix `mu_DW` if GU independently supplied `<F>`, which it does not.

### Persona 5 -- philosopher of science

The seductive move here is "field content matches, therefore it IS a gravitino, therefore
super-Higgs, therefore `mu_DW` is forced, therefore GU is falsifiable." Each arrow is weaker
than it looks, and the chain is where a program talks itself into a result it did not earn.
Arrow 1 (content -> gravitino) conflates a *kinematic* match (gamma-traceless massive RS) with a
*dynamical* identity (gauge field of broken local SUSY). Arrow 2 (gravitino -> super-Higgs)
presupposes the very guardian (local SUSY + goldstino) whose presence in GU is unestablished --
the branch cannot assume what it is trying to test. Arrow 3 (super-Higgs -> `mu_DW` forced) is
false even granting super-Higgs, because `<F>` is free. The honest reading: GU's RS is
gravitino-*like* (a real, computed structural fact worth keeping), and that is genuinely
suggestive that a guardian *might* exist -- but suggestiveness is not possession. The
integrity-preserving verdict is PARTIAL, and the specific negative result -- **super-Higgs does
NOT force `mu_DW`** -- is as valuable as a YES would have been, because it removes one tempting
route to falsifiability and tells the program exactly why that route is a dead end (super-Higgs
relates scales, it does not fix them). A YES here would have required manufacturing both the
guardian and the `<F>` pin; refusing to manufacture them is the finding.

---

## Team synthesis -- the four team questions

### Q1 -- Structural match: is carrier B consistent with a gravitino? **YES (field content) [COMPUTED]**

The gamma-trace constraint `gamma^mu psi_mu = 0` that DEFINES GU carrier B's `ker Gamma` field
space IS the gravitino's on-shell subsidiary/gauge condition. Exhibited, not asserted: the
exact 4D gamma-trace projector is idempotent and Hermitian (residuals `0`); `Gamma` has rank 4
of 16 (removes exactly the spin-1/2 gamma-trace part, leaving 12); the massive on-shell content
is `2s+1 = 4`, the same shell a Deser-Zumino gravitino and a Porrati-Rahman cured RS both reach.
GU's own `rs_ghost_sugra_gravitino_brst.py` independently found that the gravitino BRST gauge
leg's nilpotency **requires** the gamma-traceless condition -- the gravitino gauge-fixing and
GU's `ker Gamma` cure are the same object. **The gamma-trace constraint IS the gravitino's
gauge condition; GU's ker-Gamma cure = the gravitino gauge-fixing, at the field-content level.**

### Q2 -- The super-Higgs scale: does identifying mu_DW with <F> FORCE mu_DW? **NO [COMPUTED]**

Super-Higgs `m_3/2 = kappa <F>/sqrt(3)` relates the gravitino mass to the **free** order
parameter `<F>`. Identifying `mu_DW <-> <F>` maps one free scale to one free scale (`<F> =
sqrt(3 m2_eff) M_Pl mu_DW`) -- a reparametrization, nothing pinned. To force `mu_DW` one must
pin `<F>` to a vacuum energy, and there the structures diverge: GU's DeWitt-Lambda is a single-
scale quartic (`m ~ rho^{1/4}`), the super-Higgs breaking energy is a two-scale product (`m ~
rho^{1/2}/M_Pl`). The exponents differ (`1/4` vs `1/2`); they agree only at Planckian `mu_DW`.
Joint identification forces `M_Pl proportional to mu_DW`, driving `mu_DW` to the **decoupled
Planck default**, not a falsifiable window; and at the observed vacuum energy the super-Higgs
`m_3/2` and GU's `m_RS` disagree by ~30 orders. **What sets `<F>` in GU? Nothing does** -- the
only candidate pins (DeWitt-Lambda / the observerse issuance rate) are the H36 identification in
disguise, which is a postulate (not a forcing) and is itself conditionally falsified (H50/H51).
**mu_DW is NOT forced.**

### Q3 -- Consistency: is Deser-Zumino the SAME operator as GU's Porrati-Rahman cure? **NO [ARGUED + COMPUTED discriminator]**

Same on-shell shell, different operator and principle. Deser-Zumino keeps `gamma^mu psi_mu = 0`
via the local-SUSY Ward identity (guardian present); Porrati-Rahman imposes it via tuned non-
minimal `F`-vertices (guardian absent). GU's cure is the Porrati-Rahman type (the minimal `M_D`
leaks `C2 = 155.36`; the fix is an imposed non-minimal `ker Gamma` coupling revising the
`(1,0,1,0)` shiab). The super-Higgs mechanism is a logical conjunction -- **local SUSY** (a
massless gravitino to start) AND **a goldstino** (the eaten mode) -- and GU's published record
establishes NEITHER (wave34; the gravitino gauge leg needs an unbuilt curvature/holonomy datum
`W` the symbol rep lacks). So super-Higgs does not reproduce GU's forced cure; the guardian-free
Porrati-Rahman cure does. And `[P,S]=0` Krein clearance is a *different* ghost mechanism (a 2-
primary Krein parity hiding the 4th-order Stelle spin-2 ghost), not the super-Higgs eating of a
gravitino helicity-1/2 mode -- the two clear different ghosts. The `g=2` SUSY value the
gravitino needs is not GU's established cure value. **Deser-Zumino massive-gravitino != GU's
Porrati-Rahman cure (Wave 34).**

### Q4 -- VERDICT: GU's RS = a super-Higgs gravitino? **PARTIAL. mu_DW is NOT forced.**

- **YES at the field-content level:** carrier B is gravitino-*like*; the `ker Gamma` cure IS the
  gravitino's gamma-trace gauge condition (Q1, COMPUTED).
- **NO at the mechanism level:** the mass does not arise via super-Higgs -- GU has no
  established local-SUSY guardian and no goldstino; the mass comes from the guardian-free
  Porrati-Rahman non-minimal cure, a finite-cutoff EFT (Q3, ARGUED from the record).
- **NO on the keystone:** identifying `mu_DW` with a super-Higgs breaking scale does NOT force
  `mu_DW` -- it trades one free scale for another, and the vacuum-energy pin gives a different
  power law that forces Planckian (decoupled), not a falsifiable window (Q2, COMPUTED).

**So GU is not secretly a supergravity *via super-Higgs*. It wears the gravitino's field
content but lacks the local-SUSY body that would make super-Higgs available and would fix the
scale. The falsifiability keystone (H53) does NOT fall through this branch.** The concrete bite:
`mu_DW` stays free; super-Higgs is a scale-relating, not a scale-fixing, mechanism, so it can
never be the object that forces `mu_DW`.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| gamma-trace projector exact (idempotent+Hermitian, residual 0); rank(Gamma)=4 of 16; ker=12 | **COMPUTED** | Q1, exact 4D Dirac basis |
| massive spin-3/2 on-shell DoF = 2s+1 = 4 (DZ == PR target shell) | **COMPUTED** | Q1 |
| ker-Gamma cure == gravitino gamma-trace gauge condition (type match) | **COMPUTED** (structural) + corroborated by `rs_ghost_sugra_gravitino_brst.py` | Q1 |
| super-Higgs `m_3/2 = <F>/(sqrt3 M_Pl)`; `mu_DW<->F` is a free reparametrization | **COMPUTED** (symbolic) | Q2a |
| GU mass-vs-vac-energy exponent 1/4 vs super-Higgs 1/2 (differ) | **COMPUTED** (`d ln m / d ln rho`) | Q2b |
| joint identification forces `M_Pl proportional to mu_DW` (Planckian, decoupled) | **COMPUTED** (symbolic solve) | Q2b |
| at observed rho, super-Higgs `m_3/2` vs GU `m_RS` differ ~30 orders | **COMPUTED** (numeric, cited constants, comparison only) | Q2b |
| GU has no established local SUSY / no goldstino (guardian absent) | **ARGUED** | wave34 §2.7; `rs_ghost_sugra_gravitino_brst.py` (needs unbuilt `W`) |
| GU cure is Porrati-Rahman type; `g` not the SUSY `g=2` value | **ARGUED** | wave17, wave34 §2.2-2.3 |
| Deser-Zumino operator != GU's Porrati-Rahman cure | **ARGUED** (principle) + COMPUTED discriminator (g-value / guardian gate) | Q3 |

## Honest limits (do not overclaim)

1. **The field-content match is kinematic, not a proof of local SUSY.** Q1 shows carrier B has
   a gravitino's *field content*; it does NOT show GU possesses local SUSY. "Gravitino-like" is
   an evidence-tier structural observation, not a claim that GU is a supergravity.
2. **The guardian-absence is ARGUED from the published record, not proven.** wave34 and the
   sugra-BRST test show local SUSY is not *established* and needs an unbuilt datum `W`; that is
   "not shown," not "proven impossible." A future GU-internal construction could in principle
   exhibit a local-SUSY / super-IG guardian on `Sp(32,32;H) + [P,S]=0` (Weinstein's own author-
   disclaimed super-inhomogeneous direction). If it did, THIS branch's Q3 would flip -- but even
   then Q2 stands: super-Higgs would still not FORCE `mu_DW` (it relates `mu_DW` to a free `<F>`).
   The `mu_DW`-not-forced result is the robust part; the mechanism verdict is record-conditional.
3. **The vacuum-energy pin I tested is the H36 identification in disguise.** The only GU object
   that could pin `<F>` is the DeWitt-Lambda / observerse issuance rate = H36, a postulate that
   is itself conditionally falsified (H50/H51). I did not manufacture a new pin; I showed the
   available one gives the wrong power law and does not force a falsifiable `mu_DW`.
4. **The 4D toy gamma-trace projector is a structural stand-in for the Cl(9,5) `ker Gamma`.**
   The type match (gamma-traceless projection) is exact in 4D and is the same operator type the
   repo's actual rep carries (rank-1664 `ker Gamma`); I did not re-derive the full Cl(9,5)
   projector here (it is established in prior waves).
5. **Numeric scales are cited comparison constants, never fitted.** `rho_Lambda^{1/4} = 2.3
   meV`, `M_Pl = 2.435e27 eV`, `c_L = 3/8`, `m2_eff = 1` -- used only to exhibit the ~30-order
   gap, not to fit anything. No target imported.

## Branch re-hypothesis (blind) + ranked next-move

**Re-hypothesis.** GU's RS is a gravitino in *field content* but not in *mechanism*: it is the
guardian-free Porrati-Rahman branch of the same object supergravity realizes with a guardian. The
super-Higgs route to forcing `mu_DW` is a **dead end regardless of whether GU has local SUSY**,
because super-Higgs relates the gravitino mass to a free SUSY-breaking scale `<F>` rather than
fixing it; and the one GU object that could pin `<F>` (the DeWitt-Lambda) has the wrong power law
(`rho^{1/2}/M_Pl` vs `rho^{1/4}`) and is the already-falsified H36 postulate. **Therefore `mu_DW`
is not forced by any super-Higgs argument, and the falsifiability keystone does not fall through
this branch.** The gravitino-like field content is a genuine hint that a guardian *might* exist,
but the scale-forcing must come from elsewhere (the source-action construction), not from super-
Higgs.

**Ranked next-move (blind):**

1. **Test the g-factor of GU's cure against the SUSY `g=2` value.** The RT-trace-dichotomy pins
   the cure to the 1-parameter family `wedge - 6 contract`; compute the effective gyromagnetic
   ratio that family implies and check whether any point hits `g=2`. If it CAN reach `g=2`, the
   gravitino/super-Higgs door reopens at the operator level (though Q2's no-forcing still holds);
   if it provably cannot, the Deser-Zumino/PR distinction is sealed by a computed number. Highest
   leverage: it is a finite computation on an object the repo already holds.
2. **Probe whether `Sp(32,32;H) + [P,S]=0` furnishes a local-SUSY / super-IG guardian.** This is
   the fork wave34 named as decisive. It is the only way Q3's mechanism verdict could flip. Heavy
   (construction-phase), but it is the load-bearing open question for the whole guardian program.
3. **Check GU's `(m2_eff in [5/6,5/4], c_L=3/8)` point against the Deser-Waldron partial-massless
   `(m^2, Lambda)` gauge lines.** If GU sits on a partial-massless line, a gauge invariance
   (a guardian) switches on for free and the causal branch is the null-propagation one -- a
   cheaper guardian than full local SUSY. A crisp finite check (wave34 §2.4).

Next-moves 1-3 are all guardian-directed; none of them can force `mu_DW` (Q2 forecloses that
via super-Higgs), so the falsifiability question stays gated on the source-action `mu_DW`-forcing
object, not on the gravitino identification.

---

*Filed 2026-07-11. Wave 38, H54 branch 2 (gravitino / super-Higgs), BLIND to the other four
branches. Reproducible: `python tests/wave38/H54b2_gravitino_superhiggs.py` (exit 0, 16/16 PASS).
Exploration-grade; not promoted to canon. No `mu_DW` movement; H53 keystone unchanged. Tree left
dirty. Integrity note: no super-Higgs identification was manufactured -- the field-content match
is exhibited (COMPUTED), the mechanism mismatch and the no-forcing result are the honest findings,
and a PARTIAL/NO on the keystone-toppling YES was reported as the valuable outcome it is.*
