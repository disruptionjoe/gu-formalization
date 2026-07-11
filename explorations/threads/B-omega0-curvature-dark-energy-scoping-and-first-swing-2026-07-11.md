---
title: "Thread B (O(M^0) DeWitt curvature as dark energy) -- scoping + first swing"
status: exploration
doc_type: research_note
updated_at: "2026-07-11"
verdict: "B1 COMPUTED (Lambda-signature confirmed, order/structural grade); B2 SCOPED (blocked by the repo's own rate-independence finding)"
depends_on:
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
  - "explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md"
  - "explorations/source-action-constraint-intersection-2026-07-11.md"
  - "explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md"
  - "tests/threads/B_constant_section_background_curvature.py"
---

# Thread B: is the O(M^0) curvature of Met(X4) the cosmological constant?

**First swing, bounded.** Two threads off WI-068 group B (highest ceiling):

- **B1.** The `O(M^0)` intrinsic curvature of `Met(X4)` -- the "a constant section is NOT
  totally geodesic" term (`ii-s-coordinate-formula` sec 6.1) that the Willmore arc currently
  SUBTRACTS as a normalization convention -- is it actually PHYSICAL, i.e. the dark-energy /
  cosmological-constant scale?
- **B2.** Are `theta / alpha_W / c_W` simultaneously issuance/admissibility RATES of an
  observerse-non-collapse condition, with `f_0` (dark energy) the "deflationary issuance rate"?

B1 was **computed** (reproducible test, exit 0). B2 was **scoped honestly** from this repo's
own material -- and the scoping found a decisive obstruction the sibling-repo language hides.

---

## B1 -- COMPUTED: the constant-section background is Lambda-shaped

Test: `tests/threads/B_constant_section_background_curvature.py` (sympy exact, exit 0).

### The object
For a constant graph section `s(x) = (x, eta)` of `Y14 = Met(X4)` (flat base, `partial g = 0`),
`ii-s-coordinate-formula` sec 6.1 gives the vertical second fundamental form as the pure DeWitt
vertical Christoffel:

```
B^V_{mu nu, ab} = -(1/2)( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} ).
```

This is nonzero: the space of metrics is intrinsically curved, so a constant slice is not
totally geodesic. The arc subtracts this as a reference. B1 asks whether the subtracted object
is the fingerprint of a cosmological constant.

### What was computed (all exact, all PASS)
A cosmological-constant term has two algebraic fingerprints: (1) an induced stress **proportional
to the metric** `T_{mu nu} ~ eta_{mu nu}` (the defining form of a vacuum stress-energy), and
(2) a shape-energy **density that is constant over spacetime** (because `int sqrt(g) * const` is
exactly vacuum energy). Both hold:

| quantity | result | meaning |
|---|---|---|
| fiber-trace `eta^{ab} B^V_{mu nu,ab}` | **`= (1/2) eta_{mu nu}`** (exact, proportional to metric) | induced base stress ~ `eta_{mu nu}`: the vacuum/Lambda signature |
| mean curvature `H_{ab} = eta^{mu nu} B^V_{mu nu,ab}` | `= (1/2) eta_{ab}` (pure trace) | the normal points in the pure-trace / conformal direction |
| base trace-free (shear) part | **nonzero** | the section is Lambda + shear, honestly not umbilic; the Lambda piece is the isolated pure-trace part |
| DeWitt shape-energy density `|H|^2_V` | **`= -1`** (constant) | constant density = Lambda; NEGATIVE (see below) |
| DeWitt shape-energy density `|II|^2_V` | `= +2` (constant) | constant density = Lambda; positive |
| general-dimension coefficient | **`(n-2)/4`**, `=1/2` at `n=4`, `=0` at `n=2` | the `1/2` is a CONSEQUENCE of `n=4`, NOT an imported number |

**The headline:** the `O(M^0)` DeWitt background that the arc subtracts is **exactly
Lambda-shaped** -- its fiber trace is proportional to `eta_{mu nu}`, and its shape-energy
density is a nonzero constant. A cosmological-constant term arises **for free** from the
curvature of the space of metrics, before any matter, before any `M`.

### A genuinely interesting sign fact (not fit, not imported)
`|H|^2_V = -1` is **negative**. The DeWitt/gimmel metric is indefinite (signature `(6,4)` on
the fiber), and its trace-reversal makes the **conformal (trace) direction the negative-norm
direction** -- this is the well-known conformal-factor / wrong-sign-kinetic problem of the space
of metrics (Gibbons-Hawking-Perry), reproduced here from GU's own gimmel metric. The mean
curvature `H_{ab} = (1/2) eta_{ab}` lies precisely along this conformal direction, so its DeWitt
norm is negative while the full `|II|^2_V = +2` (which includes the positive-norm shear) is
positive. **This is physically load-bearing for dark energy:** the SIGN of any Lambda read off
this term depends on whether the functional weights `|H|^2` (conformal, negative) or `|II|^2`
(total, positive) -- which is *exactly the H-class vs II-class binary of OQ2-A* already isolated
in `willmore_oq2a_functional_selection.py`. So the OQ2-A functional choice does not just fix
`c_W`; it fixes the **sign of the cosmological constant** this term would contribute. That is a
new, concrete tie between OQ2-A and the dark-energy leg, and it was not assumed -- it fell out of
the DeWitt signature.

### Honest grade and caveats
**Order / structural grade, NOT a derived Einstein-Lambda stress.**
- What is solid: the algebraic Lambda signature is exact and reproducible (proportional to metric;
  constant density; coefficient `(n-2)/4` provably a consequence of dimension, not imported).
- What is NOT done: the full higher-codimension Willmore first variation (the named top technical
  task in `NEXT-STEPS.md`) that would turn "shape-energy density is constant" into an actual
  `Lambda g_{mu nu}` term in a pulled-back field equation with a physical coefficient. This swing
  computes the integrand's shape, not the varied EL.
- The SIGN and MAGNITUDE of a physical Lambda remain gated on **(i)** the OQ2-A functional scalar
  `c_W` / the H-vs-II choice (which, per the sign fact above, flips the sign), and **(ii)** the
  keep-vs-subtract convention that the arc currently resolves by SUBTRACTING this very term.
- **The actual contribution:** the object the arc subtracts as a "normalization convention" is
  exactly Lambda-shaped. So "subtract it" is **not a free gauge choice** -- it is a physical
  decision about the vacuum energy. Setting the background curvature to zero is setting `Lambda`
  (from this source) to zero by hand. That reframes sec 6.1's "(b) subtract the canonical slice
  reference" from bookkeeping into a physics commitment, and it means the dark-energy leg has a
  candidate geometric origin that costs no new field: it is the residual curvature of `Met(X4)`.

### Why this is not p-hacking
No target number is imported. The inputs are only the DeWitt metric (from GU's own gimmel
construction) and `eta`. The coefficient `1/2` is shown to be `(n-2)/4` -- forced by `n=4`, not
chosen. `|H|^2=-1`, `|II|^2=+2` are outputs, not fits. Nothing is tuned to `f_0`, DESI, `24`,
`8`, or `chi(K3)`.

---

## B2 -- SCOPED: `f_0 / alpha_W / c_W` as issuance/admissibility rates

### What the sibling-repo language claims
`NEXT-STEPS.md` lines 60-65 record the group-B conjecture: the DeWitt background curvature
"connects directly to the observerse-non-collapse condition," with `f_0` read as the
"deflationary issuance rate." The observerse/protocol-stack framing (Time-as-Finality crosswalk)
treats a physical observer as a record-issuing process, with an "issuance rate" governing how
fast records are finalized and a "non-collapse" condition governing when the record sheaf fails
to trivialize.

### The decisive obstruction -- this repo already tested the rate identification, and it FAILED
I could not confirm the identification, and the reason is **internal to this repo**, not a lack
of sibling access. The Time-as-Finality FR-series
(`explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md`) already did the
careful analysis of exactly this "issuance rate" family and found:

> **"The issuance rate" was four formally distinct objects wearing one name.** The capacity
> ceiling `lambda_max` is ABSORBED (no new field). The finalization deadline `Delta` is an L6
> coordination-loop policy. The classicality threshold `Gamma_min` is an L1<->L2 decoherence
> coupling. The filtered-sheaf obstruction `O(tau)` is a **structural** invariant -- **but
> indexed by a filtration, not a rate.** The **rate-independence finding survives intact**: no
> GU structural theorem consumes the rate `lambda`.

This is a direct problem for B2 as literally stated. `alpha_W`, `c_W`, and `f_0` enter the
**structural** field equations (the Willmore EL coefficient, the functional normalization, the
dark-energy amplitude). The FR-series established that the *rate* proper is precisely the thing
that does **not** enter structural theorems. So "`alpha_W / c_W / f_0` ARE issuance rates" runs
straight into the repo's own rate-independence result: if they were rates, they would be
rate-independent and drop out -- but they manifestly do not drop out. **The naive identification
is therefore most likely FALSE as stated**, and honesty requires saying so rather than asserting
a beautiful coincidence.

### What DOES survive scoping (the salvageable, non-rate reading)
The FR-series points to the one object in the family that is genuinely structural: the
**filtered-sheaf non-collapse obstruction** `O(tau) = H^1(X, F_tau)`
(`fr3-filtered-sheaf-non-collapse-example-2026-06-22.md`). It is cohomology of the observer's
record subsheaves, not a rate. The honest B2 reformulation is therefore:

> **Not** "`f_0` is the issuance *rate*" (rate-independence kills that), **but** "the constant
> section's nonzero background curvature is the geometric shadow of a non-trivial
> non-collapse *obstruction*." A totally-geodesic (flat, `II=0`) constant section would be the
> "collapsed" vacuum; the DeWitt curvature forcing `II != 0` (B1) is the geometric statement
> that the vacuum record sheaf does **not** collapse. The Lambda density (B1) would then be the
> energy cost of non-collapse -- a *filtration/obstruction* quantity, not a rate.

This is a conjecture, not a result. It is at least **consistent** with both the B1 computation
(a nonzero, constant, metric-proportional background) and the repo's rate-independence discipline
(because the obstruction is structural, not a rate).

### What a REAL theorem connecting DeWitt curvature to non-collapse would have to prove
For B2 to become more than an analogy, a theorem would need ALL of:
1. **A precise map** from the observer's record sheaf `{F_tau}` on `X4` to a section (or a family
   of sections) of `Met(X4)` -- i.e. define which geometric datum on `Y14` the filtration `F_tau`
   IS. (Currently absent; the FR3 object lives on a record space, not manifestly on `Met(X4)`.)
2. **A collapse <-> totally-geodesic equivalence:** prove `O(tau) = H^1(X, F_tau) = 0`
   (record sheaf collapses) **iff** the corresponding section is totally geodesic (`B^V = 0`).
   B1 shows the constant section is NOT totally geodesic, so this direction would need to match
   a NON-vanishing `O(tau)` for the vacuum -- a specific, falsifiable prediction.
3. **A quantitative identity, not a coincidence:** derive the dark-energy amplitude `f_0` from the
   DeWitt shape-energy density `|II|^2_V` (or `|H|^2_V`) times the OQ2-A coefficient `c_W`, and
   show the resulting number matches the DESI-consistent `f_0 = 0.125` used in
   `dark_energy_desi_sign.py` -- WITHOUT fitting. This is the only step that would make it physics
   rather than storytelling, and it is currently blocked on `c_W` (OQ2-A) exactly as `alpha_W` is.
4. **Rate-independence compliance:** show the connecting object is the *filtration* `O(tau)`
   (structural, allowed) and NOT the rate `lambda` (forbidden by the standing finding). Any
   derivation that smuggles in a rate would be refuted by the FR-series on arrival.

### What is missing / not available
- I do **not** have the sibling observerse/protocol-stack repos in this workspace; B2 was scoped
  entirely from this repo's `explorations/time-as-finality-crosswalk/` and `NEXT-STEPS.md`. If a
  sibling repo has upgraded the rate-independence finding (e.g. found a structural theorem that a
  rate DOES enter), that would change the verdict -- but as of this repo's canon, it has not.
- The map in step (1) does not exist. Without it, steps (2)-(4) cannot even be stated precisely.
  This is the single highest-leverage missing object for B2.

---

## Bottom line

- **B1 is a real, reproducible result** (order/structural grade): the `O(M^0)` DeWitt curvature
  of `Met(X4)` that the Willmore arc subtracts is **exactly cosmological-constant-shaped** (fiber
  trace `= (1/2) eta_{mu nu}`, constant shape-energy density), with the extra live finding that
  the H-vs-II (OQ2-A) choice **fixes the sign of that Lambda** via the DeWitt conformal-mode
  negative norm (`|H|^2 = -1` vs `|II|^2 = +2`). "Subtract the background" is thereby exposed as a
  physical choice about the vacuum energy, not a free gauge. Next step: the full higher-codimension
  Willmore first variation (already the arc's named top task) to promote "constant density" into a
  varied `Lambda g_{mu nu}` with a coefficient.
- **B2 as literally stated is most likely FALSE** (the repo's own rate-independence finding kills
  "`f_0 / alpha_W / c_W` are issuance *rates*"), but a **non-rate reformulation survives**: the
  background curvature as the geometric shadow of a filtered-sheaf **non-collapse obstruction**.
  Turning that into a theorem needs the currently-absent map from record filtrations to sections
  of `Met(X4)`, plus the same `c_W` (OQ2-A) that gates `alpha_W`. Named honestly: the missing
  object is the filtration->section map, not sibling-repo access.

No canon movement. Feeds WI-068 group B and the North Star (honest route to the source action).
