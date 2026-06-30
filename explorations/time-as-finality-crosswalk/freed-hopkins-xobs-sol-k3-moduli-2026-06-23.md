---
title: "X_obs^sol on Compact K3: Noncontractibility and KSp^0-Class Extendability of the GU Solution-Section Moduli"
date: 2026-06-23
problem_label: "freed-hopkins-xobs-sol-k3-moduli"
status: exploration
verdict: CONDITIONALLY_RESOLVED
correction: "CORRECTION XOBS-IC4-01 (2026-06-23): verdict downgraded from GENUINE_OBSTRUCTION to CONDITIONALLY_RESOLVED / lane-narrowed. The closed-GENUINE_OBSTRUCTION reading was same-session verdict inflation: the load-bearing input X_obs^sol = M_RF(K3) rests on the IC4 Einstein reduction (ic4-ricci-flat-k3-selection-2026-06-23.md), which is only CONDITIONALLY_SUPPORTED, dated the same day, with open failure conditions F3 (surviving trace-free GU source) and F5 (K3 topology not actually forced). GENUINE_OBSTRUCTION requires a proved failure with verified inputs; the load-bearing input is unproven. The lane is genuinely NARROWED (Met(X^4) and Omega^2 B Sp(64) candidates eliminated; X_obs^sol identified as the sole survivor and plausibly a gravitational-background relabel) but NOT closed. Promotion to a closed GENUINE_OBSTRUCTION is deferred to a future session after IC4 gates C/D/F (F3/F5) and the RC4 KO^4-over-orbifold lift are independently verified. Aligns this file with the already-corrected canon surface (CORRECTION FH-01, canon/no-go-class-relative-map.md). The candidate-elimination and M_RF(K3) identification math is unchanged."
scope_correction: "CORRECTION FH-03 (2026-06-25): Any use of ind_H(D_GU)=24 in this file is non-load-bearing provenance only. Generation count is OPEN. The KSp/relabeling question should be stated for a family index class, not for the numerical augmentation 24."
---

# X_obs^sol on Compact K3: Noncontractibility and KSp^0 Extendability

## 1. Problem Statement

The Freed-Hopkins observer-pairing lane survives only through Option B, and after
`explorations/time-as-finality-crosswalk/freed-hopkins-optionb-ksp-family-2026-06-23.md` (hereafter the optionb
file) only one candidate observer-state space remains uneliminated:

```
X_obs^sol = { GU solution sections s : X^4 -> Y^14 = Met(X^4) }
          = critical locus of the GU section field equation on compact K3-type X^4
```

The optionb file eliminated the other two candidates:

- **Met(X^4)** (full section space) is contractible (open convex cone in a Frechet
  space), so KSp^0_tilde = 0 -- Option B fails trivially there.
- **Omega^2 B Sp(64)** (based gauge-connection moduli over the APS boundary S^3) is
  noncontractible with nontrivial KSp^0 via Bott periodicity (pi_2 = Z), but the
  Sp(64) connection is an ordinary gauge-background field in the GU action, so its
  KSp^0 class lies in the image of the ordinary symmetry/background-extension map.
  Option B fails there by relabeling.

The two questions that decide the lane (FC1, FC2 from the optionb file):

1. **Is X_obs^sol noncontractible?** (If contractible, Option B fails: FC1.)
2. **If noncontractible, is its KSp^0 class non-extendable beyond gauge backgrounds?**
   (If the class is in the image of an ordinary symmetry/background-extension functor,
   Option B fails by relabeling: FC2.)

**Failure condition for the whole lane (from the problem header):** if X_obs^sol is
contractible OR its KSp^0 class relabels, the Freed-Hopkins anomaly lane closes.

This file identifies X_obs^sol explicitly using the now-available IC4 metric-selection
result, computes its homotopy type, and tests extendability. The result is that the
lane is NARROWED and CONDITIONALLY closes (verdict: CONDITIONALLY_RESOLVED, not a closed
GENUINE_OBSTRUCTION -- see CORRECTION XOBS-IC4-01 below): X_obs^sol IS noncontractible,
and -- *conditional on the IC4 reduction X_obs^sol = M_RF(K3)* -- its noncontractibility
is precisely the noncontractibility of the K3 Ricci-flat (Einstein) metric moduli, which
is ordinary gravitational background data. The contractibility escape is settled (NEGATIVE),
and the relabeling escape fires ONLY IF IC4 holds. Because the IC4 reduction is itself only
CONDITIONALLY_SUPPORTED (same session, open failure conditions F3 and F5), the relabeling
identification is unverified input, so the lane is narrowed but not closed.

## 2. Established Context

This computation builds on:

- **optionb file** (`freed-hopkins-optionb-ksp-family-2026-06-23.md`,
  CONDITIONALLY_RESOLVED): Met(X^4) contractible; Omega^2 B Sp(64) relabels; X_obs^sol
  is the sole survivor with OPEN topology. FC1-FC5 stated there.
- **IC4 metric selection** (`ic4-ricci-flat-k3-selection-2026-06-23.md`,
  CONDITIONALLY_SUPPORTED): the GU section field equation, within the K3 topological
  class, reduces to the **source-free Einstein equation** on the selected section;
  Hitchin-Thorpe equality on K3 (2 chi = 3 |sigma|, i.e. 48 = 48) forces any Einstein
  metric on K3 to be **Ricci-flat**; Yau-Calabi then supplies the K3-Yau metric in
  each fixed complex-structure + Kahler-class. The Willmore-energy-alone selector
  fails (E[s_LC] = 0 for every Levi-Civita section); the selector is the field
  equation, and its solution set is the Ricci-flat (hyperkahler) metric family.
- **K3 holonomy** (`oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md`): Hol(K3, g_YC) = SU(2)
  (Berger); K3 Ricci-flat metrics are hyperkahler; b_2(K3) = 22, b_2^+ = 3,
  b_2^- = 19, sigma(K3) = -16, chi(K3) = 24.
- **KSp^0 = KO^4 identification** (`signed-readout-oq2a-k-theory-lift-2026-06-23.md`,
  CONDITIONALLY_RESOLVED): H-linear Fredholm families on S = H^64 are classified by
  KSp^0(X) = KO^4(X); augmentation eps: KSp^0(X) -> Z sends the GU index family to
  an integer index. Earlier drafts inserted `ind_H = 24`; that numerical generation-count
  target is currently OPEN and is not load-bearing for the KSp/relabeling analysis.
- **No-go structural lemma** (`freed-hopkins-nonforgettable-observer-2026-06-23.md`):
  any bordism-invariant observer datum either descends (metadata) or is ordinary
  tangential-structure/background data (relabeling). Option B is the only escape, and
  it requires X_obs noncontractible AND its K-class outside the image of any ordinary
  symmetry/background-extension functor.
- **Geometry:** Y^14 = Met(X^4); fiber GL(4,R)/O(3,1); Cl(9,5) = M(64,H); S = H^64;
  gauge group Sp(64); w_2(Y^14) = 0 (RESOLVED).

## 3. Identifying X_obs^sol Explicitly

### 3.1 The GU Solution Sections Are Ricci-Flat Metrics

The optionb file left X_obs^sol abstractly defined as the critical locus of the GU
section functional and could not pin down its topology. The IC4 file changes this. The
key chain (IC4 Gates B-F, CONDITIONAL but structurally fixed) is:

```
K3 topology fixed (by index/Rokhlin)
  => GU section field equation reduces to source-free Einstein:  Ric(g_s) = lambda g_s
  => Hitchin-Thorpe equality on K3 forces lambda = 0:            Ric(g_s) = 0
  => g_s is Ricci-flat; on K3 this means Hol(g_s) = SU(2) (hyperkahler)
```

Therefore the solution-section space, as a subset of Met(K3)/Diff(K3), is exactly the
moduli space of Ricci-flat (equivalently hyperkahler, equivalently Einstein) metrics on
the K3 manifold:

```
X_obs^sol = M_RF(K3) := { Ricci-flat metrics on K3 } / Diff(K3)
```

This is no longer an unknown space. It is one of the most thoroughly understood moduli
spaces in differential geometry, controlled by the global Torelli theorem for K3
surfaces (Piatetski-Shapiro-Shafarevich; Besse, *Einstein Manifolds*, Ch. 12; Anderson;
Kobayashi-Todorov).

### 3.2 The Period-Domain Description (Global Torelli)

The moduli space of Ricci-flat (Einstein) metrics on K3 is described as follows. Let
L = H^2(K3; Z) with its intersection form, the K3 lattice

```
L = (-E8)^2 (+) U^3,   signature (3, 19),   rank 22.
```

A Ricci-flat (hyperkahler) metric of unit volume determines a positive-definite,
oriented 3-plane in H^2(K3; R) = R^{3,19} (spanned by the three Kahler/holomorphic-
symplectic forms of the hyperkahler structure, i.e. the self-dual harmonic 2-forms).
The space of such oriented positive 3-planes is the Grassmannian / symmetric space

```
D = O(3,19) / ( O(3) x O(19) )   [oriented version: SO_0(3,19)/(SO(3) x SO(19))]
```

of real dimension 3 x 19 = 57. The global Torelli theorem states that the moduli of
unit-volume Ricci-flat metrics on K3 is the arithmetic quotient

```
M_RF(K3) = Gamma \ D,     Gamma = O(L) = O(3,19; Z)
```

up to a measure-zero/non-Hausdorff correction (the "small" loci where the 3-plane meets
a (-2)-root of L, which correspond to orbifold degenerations / nodal K3s). Including the
overall scale (volume) factor R^+ multiplies by a contractible R, so it does not change
the homotopy type:

```
X_obs^sol  ~_homotopy  Gamma \ D     (modulo the root-hyperplane correction)
```

This is the central structural identification. Everything below is a consequence.

## 4. Question 1: Is X_obs^sol Noncontractible?

### 4.1 The Period Domain D Is Contractible; the Quotient Is Not

The symmetric space D = O(3,19)/(O(3) x O(19)) is contractible (it is a Riemannian
symmetric space of noncompact type, diffeomorphic to R^{57}). However, the arithmetic
group Gamma = O(3,19; Z) acts on D properly discontinuously, and the quotient

```
M_RF(K3) = Gamma \ D
```

is rationally a classifying space for Gamma. More precisely, Gamma has torsion, so the
quotient is an orbifold; passing to a finite-index torsion-free subgroup Gamma' (which
exists by Selberg's lemma), the quotient Gamma' \ D is an honest aspherical manifold:

```
Gamma' \ D = K(Gamma', 1),     pi_1 = Gamma',     pi_{>1} = 0.
```

Gamma' = O(3,19; Z)-finite-index is an infinite arithmetic group (it contains free
abelian and free nonabelian subgroups; it is a lattice in the rank-3 semisimple Lie
group O(3,19)). Therefore:

```
pi_1(Gamma' \ D) = Gamma' != 0   (infinite, nontrivial)
```

and the space is aspherical and noncontractible. The full quotient Gamma \ D is the
quotient of K(Gamma',1) by the finite group Gamma/Gamma', an aspherical orbifold whose
rational cohomology

```
H^*(M_RF(K3); Q) = H^*(Gamma; Q)
```

is the group cohomology of the arithmetic group, which is nonzero in positive degree
(by Borel's theorem on the stable cohomology of arithmetic groups: O(3,19;Z) has
nontrivial rational cohomology generated by Borel/Pontryagin-type classes).

**Conclusion (Q1):**

```
X_obs^sol = M_RF(K3) is NONCONTRACTIBLE.
```

It is an aspherical (K(Gamma,1)-type) arithmetic locally symmetric space of dimension
57 (plus the contractible scale factor). FC1 of the optionb file (X_obs^sol
contractible) is FALSE: X_obs^sol does not contract.

### 4.2 Why the Convex-Cone Argument Does Not Apply Here

The optionb file killed the *full* section space Met(K3) by the convex-cone argument:
the average (1-t)g_0 + t g_1 of two metrics is again a metric. That argument fails for
X_obs^sol because the average of two Ricci-flat metrics is generically NOT Ricci-flat
(the Einstein equation is nonlinear). The solution locus is a curved finite-dimensional
moduli, not a convex set -- this is exactly why it can be (and is) noncontractible.
This is the structural reason X_obs^sol survived the optionb file's first elimination.

## 5. Question 2: Is the KSp^0 Class Non-Extendable Beyond Gauge Backgrounds?

This is the decisive question. The lane closes if the KSp^0 class of the GU index
family over X_obs^sol is in the image of an ordinary symmetry/background-extension
functor (relabeling, FC2). I now show it is.

### 5.1 The Fredholm Family Over X_obs^sol

For each Ricci-flat metric g_s in X_obs^sol, the section pullback gives the H-linear
Dirac operator D_{g_s} = s*(D_GU) on S = H^64 over K3. By the KSp^0 = KO^4 lift
(signed-readout file), the family defines a class

```
[D] in KSp^0(X_obs^sol) = KO^4(M_RF(K3)).
```

Its augmentation is eps([D]) = ind_H(D_GU), whose numerical value is currently OPEN
(the old target was 24, corresponding to three generations). The reduced
class [D]_tilde in KO^4_tilde(M_RF(K3)) is the obstruction to stable triviality of the
generation bundle [ker D_{g_s}] over the metric moduli.

### 5.2 The Class Is Pulled Back From the Background Metric Moduli

Here is the structural fact that decides FC2. The space X_obs^sol = M_RF(K3) is, by
construction (Section 3), the moduli space of **gravitational backgrounds** on K3 --
specifically the Ricci-flat (Einstein) metric moduli. The parameter x in X_obs^sol is
literally a choice of metric g_s, which is the gravitational background field of the GU
theory (the section s IS the metric; Y^14 = Met(X^4)).

The Freed-Hopkins classification already admits the metric / tangential-structure
background as part of the input symmetry type xi. The map

```
beta : X_obs^sol = M_RF(K3) -> { space of K3 gravitational backgrounds } = M_Ein(K3)
```

is the identity (the GU observer datum IS the Einstein-metric background). The KSp^0
class [D] is the index of the family of metric-twisted Dirac operators over the metric
moduli -- exactly the family that Freed-Hopkins enrichment by a gravitational/tangential
background produces. Concretely, the extension functor

```
phi_grav : KSp^0( B(grav background) ) -> KSp^0(X_obs^sol)
```

is surjective onto [D] because X_obs^sol = M_Ein(K3) is itself the gravitational
background moduli, so phi_grav is (the identity composed with) the index map, and [D] =
phi_grav([D_universal]) sits in its image by construction.

This is the **same failure mode** the optionb file found for Omega^2 B Sp(64), but now
on the gravitational side instead of the Sp(64)-gauge side:

- Omega^2 B Sp(64): the parameter is an Sp(64) **gauge** background -> relabels via
  the gauge-background extension functor.
- M_RF(K3): the parameter is an Einstein **metric** (gravitational) background ->
  relabels via the gravitational/tangential-structure extension functor.

Both are ordinary background fields of the GU action. Neither is a non-forgettable
observer datum.

### 5.3 The Structural No-Go Lemma Applies Verbatim

The no-go lemma (`freed-hopkins-nonforgettable-observer-2026-06-23.md` Section 6, 8):
any bordism-invariant datum either (a) factors through the underlying manifold data, or
(b) depends on additional structure -- flat bundle, pin structure, metric/Einstein
background -- in which case it is ordinary background/tangential-structure data that
Freed-Hopkins classifies by varying xi. The K3 Ricci-flat metric moduli M_RF(K3)
parametrizes precisely an Einstein-metric background, i.e. case (b). There is no third
option: the Brown-representability argument forces the index family over a
background-moduli space to be classified by a map of the background type into the
spectrum, hence an ordinary symmetry/background extension.

The non-Hausdorff / orbifold subtleties of M_RF(K3) (root-hyperplane degenerations) do
not change this: even the smooth open part Gamma'\D is a moduli of Einstein backgrounds,
and the index family over it is the gravitational-background-twisted Dirac family.

**Conclusion (Q2):**

```
The KSp^0 class [D] in KO^4(X_obs^sol) IS in the image of the ordinary
gravitational/tangential-structure background-extension functor. It RELABELS.
```

FC2 of the optionb file fires.

### 5.4 Why This Is a Lane-Narrowing (Not Yet a Closed Genuine Obstruction)

> **CORRECTION XOBS-IC4-01 (2026-06-23):** this subsection originally argued the verdict
> was GENUINE_OBSTRUCTION because the two failure routes were exhaustive and both closed.
> That argument is RETAINED as the *conditional* structure of the lane, but the verdict
> label is corrected to CONDITIONALLY_RESOLVED. The reason: the entire Section-5 relabeling
> argument is load-bearing on `X_obs^sol = M_RF(K3)`, which holds ONLY IF the IC4 reduction
> (GU section field equation -> source-free Einstein on K3) holds. IC4 is only
> CONDITIONALLY_SUPPORTED (same session, 2026-06-23), with OPEN failure conditions F3
> (surviving trace-free GU source -> Einstein-with-matter, different topology) and F5 (K3
> topology not actually forced). A GENUINE_OBSTRUCTION is the strongest possible negative
> verdict and requires a *proved* failure with *verified* inputs; here the load-bearing
> input is unproven and authored the same day. Deriving the strongest negative verdict from
> a merely-conditional same-session input is verdict inflation by same-session chaining.
> The lane is therefore genuinely **narrowed** but **not closed**. See RC2 (now upgraded to
> load-bearing) and the new RC5/RC6 in Section 8.

The two failure routes are exhaustive, and CONDITIONAL ON the IC4 reduction holding, both
are closed by positive structural identifications:

1. **Contractibility route (FC1):** settled NEGATIVE -- X_obs^sol is noncontractible
   (Section 4). This does not save the lane; it merely sends the question to FC2.
2. **Relabeling route (FC2):** settled POSITIVE *conditional on IC4* -- IF X_obs^sol =
   M_RF(K3), the noncontractibility of X_obs^sol is *exactly* the noncontractibility of the
   Einstein-metric background moduli of K3, which is ordinary gravitational background data
   (Section 5.2-5.3). If IC4 fails (F3/F5), the identification X_obs^sol = M_RF(K3) breaks
   and the relabeling argument does not run.

The optionb file's summary table had the form: Met(X^4) fails by contractibility;
Omega^2 B Sp(64) fails by gauge-relabeling; X_obs^sol = UNKNOWN. This file fills the
last row CONDITIONALLY: X_obs^sol is noncontractible and, *if the IC4 reduction holds*,
fails by **gravitational-relabeling**. With that conditional, every candidate observer-
state space derivable from the GU geometry is narrowed to a single relabeling claim:

| Candidate X_obs | Contractible? | KSp^0 nontrivial? | In background image? | Verdict |
|---|---|---|---|---|
| Met(X^4) (full metrics) | YES | trivial | n/a | FAILS (contractible) |
| Omega^2 B Sp(64) (gauge moduli) | NO | YES | YES (gauge bg) | FAILS (relabel) |
| **X_obs^sol = M_RF(K3) (solution moduli)** | **NO** | **YES** | **YES (gravitational bg), IF IC4 holds** | **RELABELS *conditional on IC4*** |

The last row is CONDITIONAL: its "in background image" / "relabels" entries hold only
under the IC4 reduction X_obs^sol = M_RF(K3), which is itself only CONDITIONALLY_SUPPORTED
(open F3/F5). The structural no-go lemma (only metadata or background) had exactly two
escape doors for Option B (noncontractible + non-extendable); the only noncontractible
candidate is *conditionally* a background moduli, so the non-extendable door is held shut
ONLY as long as IC4 holds. This is a lane-narrowing, not a closed obstruction.

## 6. The One Surviving Escape Hatch (and Why It Is Outside the GU Context)

The single way the lane could reopen is FC3 of the optionb file: a **non-gauge,
non-metric Sp(64)-structure** on the observer's Hilbert space that is NOT the GU gauge
connection and NOT the gravitational background -- an independent quaternionic structure
whose moduli is noncontractible but is neither a gauge nor a metric background.

In the established GU context there is no such structure. The only Sp(64) data is the
gauge connection (relabels, optionb file), and the only metric data is the section /
Einstein background (relabels, this file). The spinor module S = H^64 carries its
quaternionic structure rigidly from Cl(9,5) = M(64,H); that structure is fixed, not
moduli. Producing a noncontractible moduli of independent quaternionic structures that
is not reducible to gauge-or-metric background data would require new GU structure not
present in the current formalization -- and by the no-go lemma it would still have to
escape being a tangential-structure enrichment, which the Brown-representability
argument makes structurally hard. This is recorded as the sole reopening condition, but
it is a *departure* from the GU observer data, not a candidate within it.

## 7. Verdict

**Self-check (mandatory triggers):**
- Word "reconstruction": NOT used as a grade claim for this file's own result (it
  appears only in citing prior files' grades; this file's own arguments are not labeled
  reconstruction).
- Recheck/recheck-class caveat phrasing: not present anywhere in the argument.
- Explicit internal contradiction of the form "X gives Y and Z, not W": not present;
  the two questions resolve consistently (noncontractible AND relabels), which is not a
  contradiction -- it is the conjunction that closes the lane.
- **A GENUINE_OBSTRUCTION verdict requires a proved failure with VERIFIED inputs.** That
  bar is NOT met here: the FC2 relabeling step is load-bearing on X_obs^sol = M_RF(K3),
  which holds only under the IC4 reduction. IC4 is CONDITIONALLY_SUPPORTED (same session),
  with OPEN failure conditions F3 and F5. A same-session, merely-conditional input cannot
  support the strongest possible negative verdict. The verdict is therefore held at
  CONDITIONALLY_RESOLVED (lane-narrowed), not GENUINE_OBSTRUCTION. (CORRECTION XOBS-IC4-01.)

**Verdict: CONDITIONALLY_RESOLVED (lane-narrowed) -- NOT a closed GENUINE_OBSTRUCTION.**

> **CORRECTION XOBS-IC4-01 (2026-06-23):** the verdict originally read GENUINE_OBSTRUCTION.
> It is corrected to CONDITIONALLY_RESOLVED. The closure is contingent on a future-session
> verification of IC4 gates C, D, and F (failure conditions F3 trace-free GU source and F5
> K3 topology forcing), plus the RC4 KO^4-over-orbifold lift. This aligns the exploration
> file with the already-corrected canon surface (CORRECTION FH-01,
> canon/no-go-class-relative-map.md), which had already downgraded the canon row but left
> this file's own verdict untouched. The math (candidate eliminations, M_RF(K3)
> identification) is unchanged; only the verdict label and its honesty binding are corrected.

The Freed-Hopkins observer-pairing anomaly lane is NARROWED, and CONDITIONALLY CLOSES only
if the IC4 reduction holds. The sole surviving Option-B candidate X_obs^sol, identified
*conditional on IC4* as the moduli space M_RF(K3) of Ricci-flat (hyperkahler/Einstein)
metrics on K3, is noncontractible -- so it passes the first test -- and IF the IC4
identification holds, its noncontractibility is exactly that of the K3 gravitational
(Einstein-metric) background moduli, an ordinary background field of the GU action, so its
KSp^0 = KO^4 index class is in the image of the ordinary gravitational/tangential-structure
background-extension functor and relabels. But the IC4 identification is the load-bearing
unproven link: it is CONDITIONALLY_SUPPORTED, same session, with open F3/F5. With Met(X^4)
(contractible) and Omega^2 B Sp(64) (gauge relabel) genuinely eliminated and X_obs^sol
*conditionally* a gravitational relabel, the lane is narrowed to a single conditional
relabeling claim -- not closed. Promotion to GENUINE_OBSTRUCTION is deferred until IC4
(C/D/F, F3/F5) and the RC4 KO^4 lift are independently verified in a later session.

## 8. Explicit Failure Conditions

This CONDITIONALLY_RESOLVED (lane-narrowed) verdict's *conditional closure* would be
falsified -- i.e. the lane would REOPEN, or the closure would never be reachable -- under
any of the following. RC1-RC4 are the original reopening conditions; RC5-RC7 are added by
CORRECTION XOBS-IC4-01 and record the unverified-input gates that block promotion to a
closed GENUINE_OBSTRUCTION in the first place. Each is a specific mathematical statement:

**RC1 (Independent quaternionic observer structure).** Exhibit an Sp(64)- or
H-structure on the GU observer Hilbert space whose moduli space M is noncontractible
and whose KSp^0 index class is NOT pulled back from either the gauge-connection moduli
(Omega^2 B Sp) or the Einstein-metric moduli (M_RF(K3)). Concretely: a class in
KO^4_tilde(M) not in the image of phi_gauge (+) phi_grav. This is FC3 of the optionb
file; in the current GU formalization no such structure exists.

**RC2 (Solution moduli is NOT the Einstein-metric moduli) -- LOAD-BEARING; this is why
the verdict is held at CONDITIONALLY_RESOLVED, not GENUINE_OBSTRUCTION.** If the IC4
reduction is wrong -- if the GU section field equation does NOT reduce to the source-free
Einstein equation on K3 (e.g. if a surviving trace-free GU source, IC4 failure condition
F3, makes the solution locus an Einstein-with-matter moduli with different topology that is
NOT a pure gravitational background) -- then the relabeling identification in Section
5.2 breaks and X_obs^sol must be re-analyzed. This is load-bearing: the whole conditional
closure rests on X_obs^sol = M_RF(K3) being a *gravitational* background moduli. The input
file `ic4-ricci-flat-k3-selection-2026-06-23.md` is only CONDITIONALLY_SUPPORTED, dated the
SAME session, and carries this exact open condition as its F3 (plus F5, K3 topology not
actually forced). Because the strongest negative verdict cannot be derived from a
same-session merely-conditional input, RC2 is not just "the primary reopening risk" -- it
is the reason this file is held at CONDITIONALLY_RESOLVED. The verdict can only be promoted
to GENUINE_OBSTRUCTION after IC4's gates C (Einstein reduction), D (source-free/vacuum), and
F (Yau/Ricci-flat), and in particular F3 and F5, are independently verified in a later
session on tracked files.

**RC3 (Global Torelli inapplicable to the GU solution locus).** If the GU solution
sections are a PROPER subvariety of M_RF(K3) (a non-generic locus cut out by extra GU
constraints) whose own topology is noncontractible in a way NOT inherited from the
ambient Einstein-background moduli -- e.g. a sublocus carrying a KO^4 class that does
not extend to the ambient M_RF(K3) -- then the pullback argument in Section 5.2 would
need the extra class to be checked separately. The argument as given assumes the GU
solution locus is (an open dense part of) the full M_RF(K3), which holds if the GU
field equation imposes no constraint beyond Ricci-flatness; if it imposes more, RC3
must be ruled out.

**RC4 (KSp^0 = KO^4 lift fails over the arithmetic quotient).** The KSp^0(X) = KO^4(X)
identification (signed-readout file, CONDITIONALLY_RESOLVED) is stated for finite CW
complexes. M_RF(K3) = Gamma\D is a non-Hausdorff arithmetic orbifold (root-hyperplane
degenerations). If the Atiyah-Janich / Bott-periodicity classification fails over this
orbifold base -- so that the family does not even define a well-defined KO^4 class --
then "the class relabels" is the wrong frame and the analysis must move to equivariant
or orbifold KSp^0; the relabeling conclusion would then need re-derivation in the
equivariant setting.

**RC5 (IC4 gate C/D not verified -- Einstein reduction unproven) [added by XOBS-IC4-01].**
The identification X_obs^sol = M_RF(K3) requires IC4 Gate C ("IC4 reduces the GU section
field equation to the Einstein equation," CONDITIONAL PASS at reconstruction grade only,
with residual gates: component-level CAS verification of `[G^Y_T]^{TF}`, fiber-localization
proof for `C_Gauss = 1`, IC3 torsion corrections, Weitzenboeck sign in the (6,4) normal
bundle, O(theta^3) distortion corrections, IC2 positivity) AND IC4 Gate D ("source-free /
vacuum section," CONDITIONAL PASS). Until Gates C and D are upgraded from conditional/
reconstruction grade to a verified derivation, the reduction `GU field equation -> source-
free Einstein` is not established, and the whole Section-3 identification is unverified
input. This blocks promotion to GENUINE_OBSTRUCTION independently of RC2's F3 branch.

**RC6 (K3 topology not actually forced -- IC4 F5 / Gate B) [added by XOBS-IC4-01].** The
identification X_obs^sol = M_RF(K3) presupposes the solution sits in the K3 topological
class. IC4 Gate B ("K3 topology already fixed") is only a CONDITIONAL PASS, resting on the
index split `ind_H(D_GU) = 8*Ahat + 8`, the RS `+8` contribution, index-additivity, Rokhlin
assumptions, and a vanishing/cancelling `ch_2(S(6,4))[K3]` correction (IC4 F5). If any of
these fail, the solution locus is not K3-type at all, M_RF(K3) is the wrong target space,
and the period-domain / global-Torelli machinery of Sections 3-4 (hence the entire
noncontractibility-via-arithmetic-quotient argument) does not apply. This is an unverified
input gate, distinct from RC2/RC5, and independently blocks closure.

**RC7 (Same-session circular promotion guard) [added by XOBS-IC4-01].** Even if RC2/RC5/RC6
were each individually plausible, the verdict must NOT be promoted to GENUINE_OBSTRUCTION
while every load-bearing input file (`ic4-ricci-flat-k3-selection`, `freed-hopkins-optionb-
ksp-family`, `signed-readout-oq2a-k-theory-lift`) is authored in the SAME session and none
is VERIFIED, and while the structural root (`freed-hopkins-nonforgettable-observer`, the
Option-B no-go lemma) is itself verdict OPEN. A closed GENUINE_OBSTRUCTION -- the strongest
possible negative verdict -- cannot coexist with an OPEN root and unclosed same-session
conditional gates. Promotion requires (a) the root lemma resolved, (b) IC4 C/D/F (F3/F5)
verified, and (c) the RC4 KO^4-over-orbifold lift established, each in a later session on
git-tracked files. Until then the disposition is CONDITIONALLY_RESOLVED / lane-narrowed.

## 9. Open Questions

1. **OQ-FH-Bsol-1 (Equivariant refinement).** Compute KO^4_{Gamma}(D) (Gamma-equivariant
   KO^4 of the contractible period domain D) and confirm that the GU index family's
   class is the image of the assembly map from the gravitational background -- i.e. that
   the relabeling holds equivariantly, not just rationally. This would upgrade the
   relabeling argument from the structural/Brown-representability level to an explicit
   equivariant-K-theory computation.

2. **OQ-FH-Bsol-2 (Borel class identification).** H^*(M_RF(K3); Q) = H^*(O(3,19;Z); Q)
   has explicit Borel generators. Identify which (if any) the Chern character ch([D])
   lands on, and verify each is a gravitational characteristic class (Pontryagin class
   of the metric moduli), confirming no "extra" observer-specific class appears.

3. **OQ-FH-Bsol-3 (IC4 vacuum gate).** Close IC4's vacuum/trace gate (F3: no surviving
   trace-free GU source on the selected K3 section) so that RC2 above is ruled out and
   X_obs^sol = M_RF(K3) is established rather than conditionally supported.

## 10. Cross-Reference and Lane Status

This file narrows the last open row of the optionb file's summary table (X_obs^sol)
and thereby advances -- but does NOT close -- the question opened as OQ-FH-1 in
`freed-hopkins-nonforgettable-observer-2026-06-23.md` Section 12 (verdict OPEN) and
OQ-FH-B1 in the optionb file.

The lane-narrowing statement (CONDITIONAL on IC4), extending both prior files:

> The Freed-Hopkins observer-pairing lane is narrowed: Met(X^4) is contractible (eliminated)
> and Omega^2 B Sp(64) relabels as gauge background (eliminated). The sole survivor
> X_obs^sol is noncontractible and -- *conditional on the IC4 reduction X_obs^sol = M_RF(K3)*
> -- relabels as gravitational (Einstein-metric) background. The two escape doors of the
> structural no-go lemma (noncontractible + non-extendable) appear not to open
> simultaneously, but only IF IC4 holds: the only noncontractible candidate is *conditionally*
> a background moduli. The conditional closure rests on IC4, which is only
> CONDITIONALLY_SUPPORTED (open F3/F5), so the lane is narrowed, not closed. It would reopen
> via an independent quaternionic observer structure (RC1), and it is not yet closed because
> the IC4 metric-selection reduction (RC2/RC5/RC6) and the KO^4-over-orbifold lift (RC4) are
> unverified.

The Freed-Hopkins anomaly lane is CONDITIONALLY_RESOLVED / lane-narrowed -- NOT closed at
GENUINE_OBSTRUCTION. Promotion to a closed GENUINE_OBSTRUCTION is deferred to a future
session, contingent on independent verification of: the Option-B no-go root lemma (currently
OPEN), IC4 gates C/D/F including F3 and F5 (RC2/RC5/RC6), and the KO^4 lift over the
arithmetic orbifold base (RC4). See CORRECTION XOBS-IC4-01 in DERIVATION-PROGRESS.md.
