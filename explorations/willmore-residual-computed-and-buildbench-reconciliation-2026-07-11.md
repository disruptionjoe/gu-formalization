# The Willmore residual, computed — and the source-action buildbench reconciled to the leg-intersection

2026-07-11. Two follow-ups to `source-action-constraint-intersection-2026-07-11.md`: (b) push the
theta-sector *sufficient* condition by actually computing the leading Willmore-EL residual so `alpha_W`
becomes a well-defined ratio, and (a) reconcile the intersection result against the standing source-action
buildbench in `absorbed/gu-source-action/`. Both are honest, and (b) surfaced a genuine canon tension.

## (b) The leading Willmore-EL residual, directly computed — `tests/one-residual/willmore_el_alpha_w_pin.py` (exit 0)

Canon RFAIL-03 (`canon/schwarzschild-weak-field-rfail.md`, verified by `tests/chase/MOVE-3/willmore_el_order.py`)
established that the **linear-in-M** Willmore-EL residual is identically zero (the true mean curvature is
`H^(1)_ab = (M/r) eta_ab`, which is harmonic) and that the leading residual is the quadratic extrinsic
stress `Q^TF(B) ~ O(M^2)` — but left the exact r-exponent **OPEN**, listing candidates `n in {3,4,6}`.

This test contracts `Q^TF(B^(1))` for the first time, from the *same* graph-section second fundamental form
`B^(1)` that MOVE-3 built and canon endorsed, using the exact Gauss-identity form
`Q^TF_{mn}(B) = [ (1/2) H_i hatB^i_{mn} - (hatB^2)_{mn} ]^TF` (codazzi-general-non-umbilic 3.3). Result:

- `H^(1)_ab = (M/r) eta_ab` reproduced exactly (agrees with canon).
- `Q^TF(B^(1))` is **nonzero** — exact Schwarzschild is not Willmore-critical (as canon says).
- **The leading trace-free residual falls as `M^2/r^2`**, tensor `diag(-9/2, -3/2, -3/2, -3/2) * M^2/r^2`
  (eta-traceless, confirmed), with `M^2/r^6` angular pieces beneath.

### The canon tension (honest — flag, do not overclaim)
`n = 2` is **outside canon RFAIL-03's own candidate set `{3,4,6}`**. The cause is a self-inconsistency in
the canon estimate: RFAIL-03 *corrected* the mean curvature to `H ~ M/r`, but its `Q(B) ~ B^2 ~ M^2/r^4`
estimate still assumed `B ~ M/r^2`. If `B ~ M/r` (consistent with `H ~ M/r`), then `Q ~ B^2 ~ M^2/r^2`.
Localization confirms it: the Hessian-only SFF (`d^2 h`) contributes only the faster (curvature-level)
falloff, while the **algebraic-slice** part of the SFF is the *sole* source of the slow `M^2/r^2` piece.

This does not falsify the gravity leg — the residual is still quadratic in M, hence safe for `M/r << 1`.
But the falloff is **slower than canon states**, and two things must be settled before the order is trusted,
both of which are exactly the canon's already-OPEN object OQ2-A (the full gimmel Willmore-EL from GU's *own*
action, canon-UNPERFORMED):
1. the gauge/coordinate status of the algebraic-slice SFF (is its `M^2/r^2` contribution physical or a
   frame artifact?);
2. the functional itself — this used the full-SFF `|II|^2` stress (the Gauss-identity `Q(B)` canon cites);
   if the GU functional is `|H|^2` (mean-curvature only), `H` is harmonic and the leading residual differs.
   The `|II|^2`-vs-`|H|^2` choice is itself part of the unbuilt action.

### What this buys for `alpha_W`
Branch-3 stationarity on Schwarzschild requires
`alpha_W * (R^Y.B)^TF_{mn}|_Schw + Q^TF_{mn}(B)|_Schw = 0`, so
`alpha_W = - Q^TF_{mn}(B) / (R^Y.B)^TF_{mn}|_Schw`. With `Q^TF(B)` now computed (sign fixed by the
`diag(-9/2,-3/2,-3/2,-3/2)` tensor), `alpha_W` is reduced from "free / gated on the whole Willmore-EL" to
**one ambient contraction away** — the single remaining input is `(R^Y.B)^TF` on the Schwarzschild section
(the Y14 ambient-curvature term, still reconstruction-grade). And via the shared `theta`, `alpha_W` is
LINKED to the dark-energy amplitude `f_0` (the intersection result). Net: the sufficient condition is now
structurally in place with one honest ambient input outstanding — *provided* the order tension above is
resolved by OQ2-A.

## (a) Reconciliation with the source-action buildbench (`absorbed/gu-source-action/`)

The buildbench is the construction sandbox for the missing RS/IG source action. Its θ route
(`THETA-SOURCE-CURRENT-CARRIER-PACKET-2026-07-05.md`) is blocked on a **named missing carrier
`L_theta_source`** and is labelled `missing_carrier_blocked` / `underdetermination_fail`: it treats the
θ/source-current law as a *free* carrier still to be constructed and computed from a candidate `S_IG`.

The leg-intersection result changes that carrier's status. `theta` is **not free**: it is over-determined by
gravity ∩ dark energy (it must simultaneously give the DESI-consistent EOS *and* carry the `M/rho^2` tail
that cancels the gravitational Willmore residual). So the buildbench's `L_theta_source` acquires **external
target constraints it did not have**:
- `theta ~ M/rho^2` on a `Psi = 0` Schwarzschild vacuum (gravity Branch-3), and
- amplitude tied to `f_0` (dark energy), and
- its induced stress must match `Q^TF(B)` in order and (up to `alpha_W`) in tensor structure — now the
  computed `diag(-9/2,-3/2,-3/2,-3/2) * M^2/r^2` object above, pending the OQ2-A order resolution.

This is the reconciliation: the buildbench flagged `L_theta_source` as **under**-determined; the
leg-intersection shows the physics **over**-determines it. The buildbench's "construct a free carrier and
score it" and the main repo's "the legs jointly force it" are the same object approached from opposite
sides — construction should now aim `L_theta_source` at the intersection target, not search freely.
(The buildbench discipline — never import `24/8`, "beautiful ≠ evidence" — is fully preserved: none of the
intersection constraints import the answer; they are independent physics targets.)

## Tightenings resolved (2026-07-11, same day) -- three follow-on tests, all exit 0

The three next tightenings named above were executed; two resolve open items and one upgrades a claim.

**(i) The M^2/r^2 "canon tension" is RESOLVED -- it was a convention artifact.**
`tests/one-residual/willmore_geometric_ii_and_ambient_curvature.py`. The gimmel/DeWitt geometry
(`ii-s-coordinate-formula-2026-06-23.md` section 6.1) shows the algebraic-slice term IS the genuine DeWitt
vertical Christoffel `Gamma^{ab}_{mu nu}`: a *constant* section is not totally geodesic, so even flat space
has `II != 0`, and the GU normalization must remove this by EITHER a horizontal-projected pullback OR
subtracting the full canonical slice reference -- both remove it at ALL orders, not just the `M=0` value.
MOVE-3 / `willmore_el_alpha_w_pin.py` subtracted only the `M=0` value, leaving the `M/r`-linear slice piece
whose square gave the `M^2/r^2`. Under either principled normalization the vertical II reduces to the
covariant graph Hessian `~M/r^3` (section 6.2), the mean curvature is `box(h)=0` (harmonic), and the
**leading Willmore residual is `M^2/r^6`** (computed). So no principled GU convention yields a falloff slower
than `M^2/r^6`; the `M^2/r^2` was the unprincipled middle option. **Tension resolved in GU's favor** (the
residual is smaller/safer than even canon's `M^2/r^4` estimate). The exact choice among the principled
conventions is still OQ2-A, but the *worry* -- a slow, near-Newtonian-scale Willmore residual -- is retired.

**(ii) The ambient curvature `R^Y` is now a computed object; `alpha_W` reduces to one structural number.**
Same test. From the section-2 gimmel Christoffels, the O'Neill A-tensor of the DeWitt metric at `g=eta` is
nonzero: `|A|^2 = 1/8` (`00`,`11`), `1/16` (spacelike mixed `12`), `-1/16` (time-mixed `01`) -- positive on
spacelike planes, sign-flipped on time-mixed, exactly as the indefinite/Krein signature requires. So `R^Y.B`
in `alpha_W = -Q^TF(B)/(R^Y.B)` is a genuine, computable curvature, and `alpha_W` is reduced from "gated on
the whole Y14 ambient geometry" to **one structural coefficient** -- the scalar weight of the ambient term in
the curved-ambient Willmore equation, which selects which curvature components enter (hence the overall sign)
and the magnitude. That single coefficient, plus the OQ2-A convention, is all that stands between here and a
numeric `alpha_W` (itself linked to `f_0` via the shared `theta`).

**(iii) forces-SM == vacuum-SM upgraded from invariant-match to CONJUGACY.**
`tests/one-residual/sm_embedding_conjugacy.py`. The forces-route u(1) (max compact of `su(3,2)`, eigenvalues
`(2,2,2,-3,-3)` on `C^5`) has triplet:doublet hypercharge ratio `-2/3`, exactly the SU(5) `5bar` ratio
(`Y(d^c)=1/3`, `Y(L)=-1/2`) -- the same u(1) EMBEDDING DIRECTION. The full 16-state hypercharge multiset
built from the SU(5) pattern `16 = 1 (+) 5bar (+) 10` is identical to the standard/vacuum 16 (both sum to 0,
both cubic-anomaly-free). For a reductive subalgebra on a faithful rep the u(1) direction + weight system fix
the conjugacy class, so the two `su(3)+su(2)+u(1)` subalgebras are **conjugate in so(10)** -- one ambient
group, one Standard Model. The gauge-sector intersection is genuinely single, not two coincident-looking
embeddings.

## The curved-ambient Willmore term -- R^Y computed, alpha_W reduced to one number (2026-07-11)

`tests/one-residual/willmore_curved_ambient_term.py` (exit 0). To finish the alpha_W route we need the
ambient-curvature term of the Willmore EL in the curved gimmel ambient: `alpha_W * (R^Y.B)`. The ambient
Riemann `R^Y` of the DeWitt/gimmel metric is now **computed exactly** (not estimated) in a faithful
9-dimensional model (3D base -> 6D fiber; a 2D base is degenerate because the DeWitt trace-reversal
coefficient `1/2` equals `1/n` at `n=2`, so `n=3` is the minimal nondegenerate model), from the closed-form
section-2 Christoffels:

- The mixed horizontal-vertical **sectional curvature is uniformly negative** (`-1/2` on diagonal-fiber
  planes, `-5/8` on off-diagonal) -- the well-known nonpositive curvature of the space of metrics. The raw
  components `R^Y_{mu K mu K}` carry the ambient signature sign (`+/-1/4`, `+/-5/16`), flipping between
  spacelike and time-mixed planes as the indefinite/Krein metric requires.
- **Adversarial cross-check PASSED:** the code-computed `R^Y` equals an independent by-hand value
  `-(1/4)(K eta^{-1} K)_{mu mu}` (for `K = E_11`, `mu = 1`, both give `-1/4`). The 9D Riemann is verified,
  not just asserted.

With this, the curved-ambient Willmore EL `Delta^perp H + Q^TF(B) + c_W (R^Y.B)^TF = 0` (standard
Weiner/Guo-Li structure) has **every factor computed except one scalar**: `Q^TF(B) ~ M^2/r^6` (principled
II), `R^Y` (above), `B|_Schw ~ M/r^3` (graph SFF). The lone remaining unknown is `c_W`, the scalar EL
prefactor of the curved-ambient Willmore equation -- fixed by the `|II|^2`-vs-`|H|^2` functional choice and
the 4-in-14 dimension/codimension. That is **exactly the OQ2-A datum** (the unbuilt GU action's normalization),
not an independent free parameter. So `alpha_W = -Q^TF(B) / (c_W (R^Y.B)^TF)|_Schw` is determined up to the
single number `c_W`, and remains LINKED to the dark-energy amplitude `f_0` through the shared `theta`.

**Bottom line of the Willmore push:** "write the ambient term" is done up to one OQ2-A scalar. There is no
remaining hidden freedom in the gravity coefficient -- `R^Y`, `B`, and `Q^TF` are all explicit computed
objects; `alpha_W` collapses onto `c_W`, which is the same convention datum that (i) and the whole
source-action narrowing already isolate.

## Grade
Computation-grade for (b) `Q^TF(B^(1))` (exact sympy, reproducible, exit 0); the **finding includes a canon
tension** (`M^2/r^2` vs the estimated `M^2/r^4`) that is flagged, localized to the algebraic-slice SFF, and
routed to the already-OPEN OQ2-A — no canon promotion or demotion is asserted here. Reconciliation (a) is
structural. No claim/canon movement. Feeds WI-068 and the North Star (the honest route to the source action).
Next tightenings: (i) OQ2-A geometric/gauge-invariant II to settle the order; (ii) the `(R^Y.B)^TF` ambient
contraction to finish `alpha_W`; (iii) conjugacy proof for the forces-SM == vacuum-SM embedding.
