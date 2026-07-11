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

## Grade
Computation-grade for (b) `Q^TF(B^(1))` (exact sympy, reproducible, exit 0); the **finding includes a canon
tension** (`M^2/r^2` vs the estimated `M^2/r^4`) that is flagged, localized to the algebraic-slice SFF, and
routed to the already-OPEN OQ2-A — no canon promotion or demotion is asserted here. Reconciliation (a) is
structural. No claim/canon movement. Feeds WI-068 and the North Star (the honest route to the source action).
Next tightenings: (i) OQ2-A geometric/gauge-invariant II to settle the order; (ii) the `(R^Y.B)^TF` ambient
contraction to finish `alpha_W`; (iii) conjugacy proof for the forces-SM == vacuum-SM embedding.
