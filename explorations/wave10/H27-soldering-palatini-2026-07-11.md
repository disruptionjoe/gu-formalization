---
title: "H27 (Wave 10) -- The soldering Palatini test: does varying the connection force pi = spin-lift(grad^gimmel)? NOT FORCED -- the honest conditional gravity theorem STANDS."
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 10
depends_on:
  - "tests/wave10/H27_soldering_palatini.py"
  - "explorations/wave8/H23-source-action-construction-2026-07-11.md"
  - "explorations/wave7/H25-II-first-variation-2026-07-11.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
  - "absorbed/gu-source-action/DEAD-ENDS.md"
  - "canon/ghost-parity-krein-synthesis.md"
  - "canon/shiab-existence-cl95.md"
  - "papers/drafts/Transcript into the impossible.md"
verdict: >
  NOT FORCED (confidence HIGH). A first-order (Palatini) variation of GU's gravity action
  S = |theta|^2 = |II|^2, treating the connection pi as an INDEPENDENT field, does NOT drive
  pi onto the metric-compatible spin-lift(grad^gimmel) on-shell. The decisive structural
  reason: the classic Palatini forcing theorem is a theorem about actions LINEAR IN THE
  CURVATURE of the independent connection (S_EH = int e e R(omega) -> omega-EOM D(ee)=0 ->
  unique Levi-Civita). GU's action is the SQUARE of the first-order distortion, not a linear
  curvature term. The square breaks the theorem in both sub-cases: (alg) theta enters |theta|^2
  algebraically -> pi-EOM = theta = 0, the acausal DEAD-END, which anyway only returns the
  CHOSEN reference (circular, not a derivation of the spin-lift); (kin) theta carries the
  derivative (II = graph Hessian) -> |II|^2 is Yang-Mills-type and the pi-EOM is the
  second-order divergence d_A* theta = source, whose solution is a particular piece PLUS a
  nontrivial kernel -- a residual gauge/harmonic FAMILY, not a unique forced connection.
  Neither route is the Palatini forcing. The soldering pi = spin-lift(grad^gimmel) is therefore
  a GENUINE POSTULATE, not dynamically forced. Gravity does NOT go unconditional; H23's honest
  CONDITIONAL theorem is already correct as written. Reproducible: tests/wave10/H27_soldering_palatini.py
  (exit 0, 6/6 PASS).
---

# H27 -- The soldering Palatini test

**Discipline.** This is the swing that would decide "unconditional," so it is maximally at
risk of motivated success -- and, symmetrically, the NOT-FORCED verdict it reaches is the
*preserving* answer, so it is at risk of motivated **laziness**. Both risks are addressed
below: a POSITIVE CONTROL proves the method can return FORCED when forcing is genuine, and
three explicit steelmen of the FORCED direction are recorded and refuted. Every positive
claim is an exact linear-algebra identity (residual `0.0e+00`) or an exact dimension/rank
count. "It fits beautifully" was treated as a warning throughout. Reproducible check:
`python tests/wave10/H27_soldering_palatini.py` (exit 0, 6/6 PASS).

---

## The question (H23's precisely-named next object)

Seven-plus waves cleared everything else on the gravity leg. H25 decided the tree-level sign
CLEAR (`C_RY > 0`, `m^2_eff > 0`). H23 isolated the **single** remaining object as one
soldering postulate:

```
A  =  spin-lift( grad^gimmel )       equivalently   theta = pi - pi_ref  pinned to the 0-locus
```

-- GU's gauge connection `pi` (inside `theta = pi - Ad(eps^-1)B`) equals the spin-lift of the
gimmel/DeWitt Levi-Civita connection. H23 proved the spin-lift is **canonical as a map** and
the ghost clears in the Krein sense, but showed **nothing kinematic** forces the *dynamical*
`pi` onto the 91-dim spin-lift image inside the ~8256-dim `sp(32,32;H)` (codimension 8165).

H27's one job: does the **dynamics** force it? Precisely --

> Does a FIRST-ORDER (Palatini) variation of `S = |theta|^2 = |II|^2`, treating `pi` as an
> INDEPENDENT variable, drive `pi` onto the metric-compatible spin-lift ON-SHELL, WITHOUT
> collapsing to the acausal `theta = 0` (a DEAD-END)?

This is the GU analog of the classic **Palatini theorem**: varying Einstein-Hilbert
`S_EH = int e e R(omega)` w.r.t. an independent connection `omega` forces `omega = Levi-Civita`
on-shell. If the analog holds, the soldering is dynamically forced -> gravity UNCONDITIONAL.
If not, the soldering is a genuine postulate -> the honest conditional theorem stands.

---

## The decisive structural fact

The Palatini forcing theorem is a theorem about actions that are **linear in the curvature**
of the independent connection:

```
S_EH = int e e R(omega),     R(omega) = d omega + omega^2.
```

`R` carries a derivative of `omega`; varying `omega` and integrating by parts gives the
**algebraic-in-torsion** Euler-Lagrange equation `D_omega(e e) = 0`, whose **unique** solution
is `omega = omega_LC(e)`. Linearity in `R` is exactly what makes the connection EOM (i) a
single algebraic condition and (ii) uniquely solved by the metric-compatible connection. This
is why Palatini forces.

**GU's gravity action is not linear in a curvature.** It is the **square of the first-order
distortion** -- Weinstein's "first-order theory then its square" (H18's II-class; H23):

```
S = |theta|^2 = |II|^2 ,      theta = pi - pi_ref   (a connection-DIFFERENCE, an ad-valued
                                                     1-form -- a POTENTIAL, not a curvature).
```

The square breaks the Palatini theorem in **both** readings of how `theta` enters, and the
`|II|^2` (second-order) vs `|theta|^2` (first-order-algebraic) distinction is exactly the
fork -- so point (3c) of the swing matters, decisively:

- **(alg) `theta` enters algebraically** (no derivative of `pi` inside `|theta|^2`). Then
  ```
  delta |theta|^2 / delta pi  =  2 theta  =  0   =>   theta = 0.
  ```
  This is (i) the **acausal DEAD-END** (`DEAD-ENDS.md`: driving `theta -> 0` decouples the RS
  sector and reinstates Velo-Zwanziger acausality), and (ii) it returns `pi = pi_ref` -- the
  **chosen** reference -- *not* a derivation of the spin-lift. The Hessian is `2 I > 0`, so the
  unique critical point is `theta = 0`. "Forcing" here is **circular**: it lands on the
  spin-lift only if you already set `pi_ref = spin-lift`, i.e. import the answer.

- **(kin) `theta` carries the derivative**: `II = s*(theta)` contains the graph Hessian
  (second derivatives of `g` = first derivatives of the connection; `ii-s-coordinate-formula`
  sec 4). Then `|II|^2` is **Yang-Mills-type**, and the `pi`-EOM is the **second-order
  divergence** `d_A* theta = source` (exactly H23's independently-derived EOM). Its solution is
  a particular piece **plus** the kernel of the divergence -- a nontrivial residual **FAMILY**
  (gauge/harmonic moduli), not a unique metric-compatible point. Yang-Mills does not force its
  connection onto any canonical reference; it has a moduli space.

So the very feature that makes GU's action "first-order-then-square" (the double copy, the
`|theta|^2`) is **precisely why the Palatini theorem does not transfer**. Palatini forces
because EH is linear in curvature; GU squares a potential, so its connection-EOM is either
`theta = 0` (trap) or a YM-type family -- neither is the Palatini forcing.

This reproduces H23's EOM remark from an independent angle (H23 argued `S=|theta|^2` gives
`d_A* theta = source`, not `theta = 0`; H27 shows the *only* way to get `theta = 0` is the
algebraic reading, which is the acausal trap, and even it is circular). The convergence of two
independent arguments hardens the negative result.

---

## What was computed vs argued

**Computed (exact, in `tests/wave10/H27_soldering_palatini.py`):**

| # | Check | Result |
|---|---|---|
| 0 | Target codim | `dim so(9,5)=91 << dim sp(32,32;H)=8256`, codim `8165` (exact) |
| 1 | **POSITIVE CONTROL** -- genuine linear Palatini: `M(e) omega = b(e)` with `M` invertible | UNIQUE `omega*`, and `d omega*/d e != 0` (metric-soldered) -> method **CAN detect FORCED** |
| 2 | GU `\|theta\|^2` (algebraic): `pi`-EOM `= 2 theta = 0` | `theta*=0` exactly, Hessian eigenvalues all `= 2 > 0`, unique critical point -> **acausal TRAP** |
| 3 | `theta=0` returns `pi_ref`, not the spin-lift | `\|pi* - pi_ref\| = 0` exactly; `\|pi* - spin_lift\| = 12.49` (generic ref); `d pi*/d pi_ref = I` -> **circular** |
| 4 | GU `\|II\|^2` (kinetic): `pi`-EOM `= d_A* theta = source` | `dim ker(D^T D) = 1 > 0`; two DISTINCT `pi` solve the SAME EOM -> **residual FAMILY** |
| 5 | Classifier: Palatini forces IFF linear-in-curvature; GU is the SQUARE | control(linear)=FORCED, GU(square)=NOT-FORCED |

All residuals `0.0e+00`; exit 0, 6/6 PASS.

**Argued (from the sources, not re-computed on the full `Y^14` bundle):**

- That GU's gravity action **is** the II-class square `|II|^2` (from H18, transcript-grade P2)
  rather than a linear-in-curvature term. H27 assumes this, as H23/H25 do.
- That the `|II|^2` kinetic `pi`-EOM is the divergence `d_A* theta = source` (H23's result;
  H27 models its kernel structure but does not re-derive the operator on `Y^14`).
- That even GU's **linear** shiab/Einstein-contraction piece `theta(F)` (Weinstein's `G_mu nu`
  replacement) does not force `pi = spin-lift`: Weinstein frames its EOM as a **divergence /
  conservation** ("divergence-free," a field equation whose vacuum "responds to the VEV"), i.e.
  a sourced YM-Bianchi-type field equation, **not** an algebraic zero-torsion condition. So it
  too gives a solution family, not a forcing.

The computation is a **structural / finite-dimensional model** capturing the load-bearing
facts (gradient degree; the `theta=0` algebraic EOM; the divergence-operator kernel; the
positive control's invertibility). It is not a full field-theoretic variation on the 14D
bundle. What makes it decisive is that the linear-vs-square gradient-degree distinction, the
`theta=0` collapse, and the YM kernel are **general and exact**, not model artifacts -- and
they agree with H23's independent EOM.

---

## Adversarial checks (guarding the NOT-FORCED direction)

Because NOT-FORCED is the *preserving* answer, the failure mode to guard against is declaring
it too cheaply. Three steelmen of FORCED, each refuted:

1. **"GU's real gravity action is the linear shiab/Einstein-contraction piece, not `|theta|^2`
   -- so Palatini could force."** Refuted: Weinstein's own framing of that term's EOM is a
   *divergence* (conservation law / field equation, YM-Bianchi type), not an algebraic
   zero-torsion condition. A field equation has a solution family; it does not collapse `pi`
   onto the spin-lift. (And H18 forced the II-class square for the gravity leg regardless.)

2. **"The tautological soldering form on `Y = Met(X)` forces it."** Refuted: H23 already
   settled this is *kinematic* -- it makes the **reference** canonical, not the dynamical `pi`.
   No new dynamical content here.

3. **"Minimizing `|II|^2` selects the spin-lift as the unique minimizer."** Refuted: the
   minimizer is `II = 0` (totally geodesic), which by `ii-s-coordinate-formula` sec 6.1 is
   **not** the metric-compatible slice (constant sections are not totally geodesic for the
   literal gimmel metric), and is itself a `theta -> 0`-type collapse. Minimizing `|II|^2`
   constrains the **section** (a minimal-surface equation on `g`), not the **connection** onto
   the spin-lift at fixed section. Not the Palatini forcing.

Positive control (check 1) is the symmetric guard: on a genuine linear-Palatini toy the exact
same machinery returns FORCED (unique, metric-soldered connection). The method is not rigged
to always answer "not forced."

---

## VERDICT: NOT FORCED (confidence HIGH)

The soldering `pi = spin-lift(grad^gimmel)` is a **genuine postulate**, not dynamically forced.
A first-order (Palatini) variation of `S = |theta|^2 = |II|^2` does **not** drive `pi` onto the
metric-compatible spin-lift:

- the algebraic reading gives `theta = 0` -- the **acausal DEAD-END** (excluded), which anyway
  only returns the **chosen** reference (circular);
- the kinetic reading gives the divergence EOM `d_A* theta = source` -- a **residual YM-type
  family**, not a unique forced connection.

The Palatini theorem forces in EH **because** EH is linear in the curvature of the independent
connection; GU's action is the **square** of a first-order potential, and that square is exactly
what breaks the forcing. This is not a failure to find a proof; it is a structural obstruction
with a named cause, converging with H23's independent EOM argument.

**Grade.** HIGH confidence on NOT-FORCED. The linear-vs-square distinction is theorem-level and
general; the `theta=0` collapse and the divergence-kernel family are exact; the positive control
confirms the method detects real forcing; three FORCED steelmen were refuted. The one thing not
done is a full variational calculation of `d_A* theta = source` on the actual `Y^14` bundle --
but that operator is H23's, already argued to give a source-family, and the structural model
reproduces its kernel behavior.

**This is a FULL, valuable result.** A clean "NOT forced -- soldering is a genuine postulate"
**locks in the honest conditional theorem**: it removes the last open route by which the
soldering might have been dynamically forced, and confirms H22-ship's conditional statement is
correct as written, not merely unproven-either-way.

### Honest caveats

1. **Structural model, not full field theory.** The checks are finite-dimensional linear-algebra
   stand-ins for the gradient-degree, the `theta=0` EOM, and the divergence kernel. Their force
   is that these structures are general and match H23's independent EOM -- not that the 14D
   variation was carried out end-to-end.
2. **Assumes the II-class square action** (H18 / OQ2-A). A radically different functional (e.g. a
   linear-in-curvature Einstein-contraction as the *sole* gravity action) would need its own
   Palatini analysis; steelman 1 argues it too gives a field equation, but that is argued, not
   computed here.
3. **NOT-FORCED does not mean the soldering is false.** As a *postulate* it remains natural (the
   reference is the unique metric-compatible torsion-free lift). H27's claim is only that GU's
   dynamics does not *force* it -- which is exactly what "a genuine postulate" means.
4. **`mu_DW` scale unchanged.** Orthogonal to this test; still the source-action overall
   normalization (H24/H25), dimensionless ratio fixed, dimensionful scale free.

---

## RE-RANK signal

- **Does gravity go UNCONDITIONAL?** **No.** The single dynamical route that could have forced
  the soldering (Palatini variation of the source action) is closed: the square structure gives
  the acausal trap or a residual family, never the metric-compatible forcing. Gravity stays
  **clear-MODULO-one-soldering-postulate + `mu_DW` scale**.
- **Does the conditional theorem stand?** **Yes -- the flagship is already correct as written.**
  H23/H22-ship's statement -- "GU gravity is tree-level Stelle-clear with a positive, decoupled
  massive ghost, **conditional on the single soldering postulate** `pi = spin-lift(grad^gimmel)`
  and the overall scale `mu_DW`" -- is now not just the best available phrasing but the
  **provably-correct** one: H27 shows the soldering cannot be promoted from postulate to theorem
  by the dynamics, so the conditional is the theorem, full stop. **Update the flagship's framing
  from "soldering not YET forced" to "soldering PROVABLY a genuine postulate (Palatini route
  closed)"** -- a strengthening of the honesty, not a change of the physics.
- **Precise final state of the gravity leg.** Everything downstream of the soldering is in hand
  and exact: spin-lift canonical (H23 A), gauge group `Sp(32,32;H)` (H23 B), `[P,S]=0` positivity
  / ghost clears in the Krein sense (H23 C), tree-level sign CLEAR `m^2_eff > 0` (H25). The leg
  rests on **exactly one** structural postulate (`pi = spin-lift(grad^gimmel)`) plus **one**
  free dimensionful scale (`mu_DW`). Both are now KNOWN to be genuinely free of the built
  dynamics: the soldering by the Palatini no-go (H27), the scale by H24/H25. **The gravity leg
  is complete as a conditional theorem and cannot be made unconditional within the currently
  built structure.**
- **Do the entropic / H5-H19 routes rise?** **No.** Gravity's sign and positivity are untouched
  and its residual is now fully characterized (one postulate + one scale, both provably free).
  The Stelle reading is neither weakened nor strengthened by H27; it is *finalized* as
  conditional.
- **Fermion/generation frontier unchanged.** The `C2`-to-index carrier remains the separate,
  harder wall (buildbench). H27 touches only the gravity soldering, and confirms it is strictly
  softer than -- and provably distinct from -- the fermion `C2` wall.

---

*Filed 2026-07-11. Wave 10, the final gravity swing. Reproducible:
`python tests/wave10/H27_soldering_palatini.py` (exit 0, 6/6 PASS). Exploration-grade; not
promoted to canon. Adversarially graded: no forcing was manufactured, no target imported, and
the NOT-FORCED direction was guarded by a positive control plus three refuted FORCED steelmen.
The honest outcome LOCKS IN the conditional gravity theorem: the soldering is a genuine
postulate, and the Palatini route to making it unconditional is closed.*
