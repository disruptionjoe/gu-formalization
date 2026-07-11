---
title: "Thread A -- higher-codim Willmore: numerical oracle + full first-variation scoping"
status: exploration
doc_type: research_note
updated_at: "2026-07-11"
verdict: "ORACLE_RUN_AND_FINDING_LANDED; FIRST-VARIATION_SCOPED_NOT_COMPUTED"
depends_on:
  - "explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
  - "tests/one-residual/willmore_curved_ambient_term.py"
  - "tests/one-residual/willmore_geometric_ii_and_ambient_curvature.py"
  - "tests/one-residual/willmore_oq2a_functional_selection.py"
  - "canon/schwarzschild-weak-field-rfail.md"
---

# Thread A -- higher-codim Willmore: numerical oracle + full first-variation scoping

**Status.** Bounded first swing on THREAD GROUP A (A1/A2/A3). Two deliverables:
1. **A2 built and run** -- an independent numerical diff-geo oracle
   (`tests/threads/A_numerical_diffgeo_oracle.py`, exit 0). It cross-checks the symbolic gimmel-metric
   `R^Y` and `|A|^2` and, being an audit not a rubber stamp, **it turned up a real finding** (below).
2. **A1 scoped, not computed** -- a concrete term-by-term map of the full higher-codimension Willmore
   first variation and what a background-subtracted linearization around the (non-totally-geodesic)
   constant section actually requires, plus the exact `O(M^0)` piece flagged in
   `willmore_oq2a_functional_selection.py`.

A3 (the `M^2/r^2`-vs-`M^2/r^6` convention as a Newtonian-scale test) is noted as the next swing; not done.

---

## Part 1 (A2) -- the numerical oracle, and what it found

### What it is
`tests/threads/A_numerical_diffgeo_oracle.py` is a SECOND, INDEPENDENT derivation of the two ambient-
curvature objects the `alpha_W` arc rests on. It builds ONLY the DeWitt/gimmel metric `G` from its
DEFINITION (block-diagonal base `(+)` trace-reversed Frobenius fiber), then runs the GENERIC Levi-Civita
machinery numerically:

```text
Gamma^A_{BC} = (1/2) G^{AD}( d_B G_{DC} + d_C G_{DB} - d_D G_{BC} )
R^A_{BCD}    = d_C Gamma^A_{DB} - d_D Gamma^A_{CB} + Gamma^A_{CE}Gamma^E_{DB} - Gamma^A_{DE}Gamma^E_{CB}
```

with every metric partial from HIGH-PRECISION FINITE DIFFERENCES (`mpmath.diff`, 40 dps). The Christoffel
derivatives `d_C Gamma` are assembled analytically from the finite-differenced 1st/2nd metric partials (via
`d_C G^{AE} = -G^{AP}(d_C G_{PQ})G^{QE}`), so there is exactly ONE finite-difference layer on the metric --
no fragile nested differencing. **It reuses none of the hand-transcribed closed-form Christoffels** that the
symbolic tests (`willmore_curved_ambient_term.py`, `willmore_geometric_ii_and_ambient_curvature.py`) depend
on. That independence is the whole point: a transcription or sign error in the closed forms would surface
here as a mismatch.

### The finding (adversarial -- the oracle earned its keep)
Running the pipeline in BOTH the geometrically HONEST coordinate basis and the symbolic tests' basis:

**CONFIRMED (convention-robust; two independent derivations agree):**
- DIAGONAL-fiber `R^Y = +/-1/4`, mixed sectional `= -1/2`; the by-hand `R^Y(d_1, E_11, d_1, E_11) = -1/4`.
- DIAGONAL `|A_00|^2 = |A_11|^2 = 1/8`.
- `R^Y` is NONZERO and Krein-signed (both signs present) -- so the `alpha_W` ambient term stays a real,
  computed object, and the "space of metrics is curved / indefinite" claim holds.

**CORRECTED (the finding):** the symbolic tests' OFF-DIAGONAL magnitudes -- the `-5/8` mixed sectional in
`willmore_curved_ambient_term.py` and `|A_12|^2 = 1/16` in `willmore_geometric_ii_and_ambient_curvature.py`
-- match **NEITHER** consistent convention. The cause is a mixed convention: those tests lower indices with
the non-doubled tensor-component metric `V_low` while their closed-form Christoffels carry a different
symmetric-pair normalization. The subtlety is the standard `Sym^2` basis one:

> a single fiber coordinate `h_ab = h_ba` (for `a<b`) drives BOTH off-diagonal matrix entries, so the true
> tangent vector is `d/dh_ab = E_ab + E_ba` -- the off-diagonal DeWitt norm **doubles**. Diagonal directions
> (`a=b`) are single-entry and unaffected, which is exactly why the diagonal numbers are robust and only the
> off-diagonal ones move.

In the HONEST (doubled) coordinate basis the invariants are:

| quantity | symbolic report | honest (doubled) | non-doubled-consistent |
|---|---|---|---|
| mixed sectional, diagonal fiber | `-1/2` | **`-1/2`** | `-1/2` |
| mixed sectional, off-diagonal fiber | `-5/8` | **`-1/8`** | `+1/4` (!) |
| `|A|^2`, diagonal (00,11) | `1/8` | **`1/8`** | `1/8` |
| `|A|^2`, off-diagonal spacelike (12) | `1/16` | **`1/8`** | `1/2` |

So the space of metrics has **uniformly non-positive** mixed sectional curvature `{-1/2, -1/8}` and a uniform
`|A|^2` magnitude `1/8` (Krein-signed). Note the non-doubled-consistent reading gives a POSITIVE off-diagonal
sectional (`+1/4`), which would VIOLATE non-positivity -- so neither the symbolic report nor a naive
non-doubled reading is the honest geometry; the doubled basis is.

### Impact (honest, non-alarmist)
**No `alpha_W`/Willmore-arc CONCLUSION breaks.** Every downstream claim rests on (a) `R^Y` being nonzero and
Krein-signed -- CONFIRMED -- and (b) `alpha_W` collapsing onto the single OQ2-A scalar `c_W` regardless of
the specific off-diagonal magnitude. The correction actually **strengthens** the qualitative statement (the
"nonpositive curvature of the space of metrics" is now uniform and clean, `-1/2` and `-1/8`, rather than the
mis-normalized `-5/8`). The concrete numeric edits owed to the two symbolic tests: their off-diagonal
component/sectional printouts (`-5/16`, `-5/8`, `1/16`, `-1/16`) should be relabeled as
convention-dependent, with the honest invariants `-1/8` (sectional) and `1/8` (`|A|^2`). **Recommended:** add
a one-line convention note to both tests pointing at this oracle, rather than silently changing printed
numbers. (Not done here -- those files are the symbolic arc's, and the finding should be Joe-reviewed first.)

Runtime ~32 s; exits 0. The exit-0 assertions encode the verified picture (confirmations + the localized
artifact), not a copy of the symbolic numbers.

---

## Part 2 (A1) -- scoping the full higher-codimension Willmore first variation

### Setup
The section is `s: X^4 -> Y^14 = Met(X^4)`, `s(x) = (x, g_{ab}(x))`, an immersion of `n=4` into `m=14`, so
**codimension `k = 10`** -- genuinely high. The normal bundle is (a lift of) the vertical `Sym^2 T^*X`. The
second fundamental form `B = II_s` and its vertical representative `B^V_{mu nu, ab}` are given in closed form
in `ii-s-coordinate-formula` sec 4; the ambient Christoffels/`R^Y` are sec 2 (and now numerically
cross-checked, Part 1). The Willmore functional GU extremizes is the OQ2-A binary: `E = int |H|^2` (H-class)
or `E = int |II|^2` (II-class).

### The higher-codim Willmore EL, term by term (Weiner / Guo-Li structure)
For an `n`-submanifold with mean curvature vector `H` and SFF `A=II` in ambient `(Y, G)` with Riemann `R^Y`,
the first variation of `int |H|^2` gives an EL of the schematic form (normal-bundle valued):

```text
  W(H)  =  Delta^perp H                                   [T1: normal-Laplacian of H]
        +  ( <A_{ij}, H> A_{ij}  -  (1/2)|H|^2 H )        [T2: Simons / |II|^2-type extrinsic stress = Q^TF(B)]
        +  T3(R^perp)                                     [T3: normal-bundle curvature term]
        +  T4(R^Y)                                        [T4: ambient-curvature term = the alpha_W term]
        =  0.
```

Concretely, term by term, and what each needs on the gimmel background:

- **T1 `Delta^perp H`.** `Delta^perp = -(nabla^perp)^* nabla^perp` is the connection Laplacian of the
  NORMAL connection `nabla^perp` (induced by the lift `N`, `ii-s` sec 5). Needs: `H` as a section of the
  normal bundle, and `nabla^perp` from the ambient Christoffels + `N`. Leading derivative term (2 normal
  derivatives of `H`).

- **T2 Simons / `|II|^2` term `= Q^TF(B)`.** The purely-extrinsic quadratic stress, exactly the
  `Q^TF_{mn}(B) = [ (1/2) H_i \hat B^i_{mn} - (\hat B^2)_{mn} ]^TF` already computed
  (`codazzi-general-non-umbilic 3.3`; `willmore_geometric_ii...py` -> `M^2/r^6` under the principled II).
  For the `|II|^2` functional this term is replaced by the full `|A|^2` Simons operator (Guo-Li), which also
  contracts the FULL `B`, not just `H`.

- **T3 normal-bundle curvature `R^perp`.** In codimension `k=10` the normal connection is NON-flat:
  `R^perp(e_i, e_j) = [nabla^perp_i, nabla^perp_j] - nabla^perp_{[i,j]}` is generically nonzero (Ricci
  equation `R^perp_{ij}^{alpha beta} = <[A_i, A_j] e^beta, e^alpha> + (R^Y)^{perp}_{ij}`). It enters the EL
  through the commutators inside `Delta^perp H` and directly via the Ricci equation. **This term is absent
  in the current arc** (codimension-1 intuition), and is the honest new object A1 must carry. Its two pieces:
  the extrinsic `[A_i, A_j]` commutator (quadratic in `B`) and the ambient `(R^Y)^perp_{ij}` mixed component.

- **T4 ambient term `T4(R^Y)` = the `alpha_W` term.** The genuine ambient-curvature contribution. For the
  `|H|^2` functional (Weiner) it is the tangentially-traced ambient Riemann acting on `H`:
  `T4 = sum_i ( R^Y(H, e_i) e_i )^perp  +  (nabla^Y R^Y)-type terms  +  ( Ric^Y|_{tangent} )-pieces`. This
  is what `c_W (R^Y . H)^TF` (H-class) or `c_W (R^Y . B)^TF` (II-class) abbreviates in the arc. `R^Y` is now
  the Part-1 computed/audited object.

### The background subtraction the constant section forces (the crux)
`ii-s` sec 6.1: a CONSTANT section (`partial g = 0`, flat `g = eta`) is **not totally geodesic** for the
gimmel metric. Its vertical SFF is the pure DeWitt slice term
`B^V_0{}_{mu nu, ab} = -(1/2)( eta_{a(mu}eta_{nu)b} - (1/2)eta_{ab}eta_{mu nu} )`, and its mean curvature
vector is (computed here, exact sympy):

```text
H_0^{ab} = g^{mu nu} B^V_0{}_{mu nu}{}^{ab} = (1/2) eta^{ab}          (n = 4).
```

So `H_0 = (1/2) eta` -- **nonzero, `O(M^0)`, and PROPORTIONAL TO THE METRIC** (a vacuum-energy / `Lambda`-like
fingerprint; this is exactly the object Thread B is testing as a cosmological-constant term). Consequently:

> The Willmore EL evaluated on the constant background is NOT zero. `W(H)|_{s_0}` is an `O(M^0)` residual
> built from `H_0 = (1/2)eta`, `B_0` (the slice term), `R^perp_0`, and `R^Y|_{g=eta}` (Part 1). A physically
> meaningful `M`-linearization MUST subtract this background: expand `s = s_0 + M\,delta s` and study
> `W(H)|_{s} - W(H)|_{s_0}` (or, equivalently, adopt one of the `ii-s` sec-6.1 normalizations (a)
> horizontal-projected pullback / (b) subtract the canonical slice reference -- both kill `B_0`, hence `H_0`,
> at all orders). Only after this subtraction is the leading residual the genuine `M`-dependent
> `Q^TF(B) ~ M^2/r^6` the arc reports.

### The exact `O(M^0)` piece flagged in `willmore_oq2a_functional_selection.py`
That test's caveat reads: "In higher codimension the `|H|^2` ambient term ALSO carries H-independent pieces
(ambient Ricci restricted to the tangent), `O(M^0)` around the background section ... demand a
background-subtracted linearization." Made concrete here, the `O(M^0)` piece is precisely

```text
  W(H)|_{s_0}  =  Delta^perp H_0            (H_0 = (1/2)eta constant  =>  Delta^perp H_0 has only the
                                             connection/curvature part, no base-derivative part)
              +  Q^TF(B_0)                  (Simons stress of the DeWitt slice term -- O(M^0))
              +  T3(R^perp_0)               (normal-bundle curvature of the constant section -- O(M^0))
              +  c_W ( R^Y . {H_0 or B_0} )^TF   (ambient term on the background; R^Y|_{g=eta} is O(M^0),
                                                  H_0/B_0 are O(M^0)  =>  O(M^0)).
```

Every factor here is `O(M^0)` and now computable: `H_0 = (1/2)eta` (above), `B_0` (sec 6.1), `R^Y|_{g=eta}`
and `|A|^2` (Part 1, audited), leaving `R^perp_0` (the one genuinely new object, from the Ricci equation) and
`c_W`. This `O(M^0)` term is the "constant sections are not totally geodesic" curvature; it is what the
background subtraction removes, and separately it is the candidate `Lambda` term Thread B is probing. The
order-selection argument of `willmore_oq2a_functional_selection.py` (H-class balances `Q^TF(B)` at `O(M^2)`;
II-class needs the `O(M^1)` `theta`-source) is only rigorous once this `O(M^0)` background is subtracted --
which is exactly why that test graded itself "order-grade map, NOT a closed selection theorem."

### What a rigorous A1 computation requires (the concrete to-do)
1. Compute `R^perp_0` (normal-bundle curvature of the constant section) via the Ricci equation from the
   Part-1 machinery -- the one term the arc has never carried. (Numerically tractable with the same oracle.)
2. Assemble `W(H)|_{s_0}` (the `O(M^0)` piece above) explicitly and confirm it is `~ eta` (pure `Lambda`),
   which would tie A1 directly to Thread B.
3. Do the background-subtracted `M`-linearization `W(H)|_{s_0 + M delta s} - W(H)|_{s_0}` and read off the
   leading `M`-order in each of H-class / II-class -- turning `willmore_oq2a_functional_selection.py`'s
   order-grade map into a computed selection.

---

## What was NOT done (bounded first swing)
- The full first-variation is **scoped, not computed**: `R^perp_0` and the assembled `O(M^0)` EL are named,
  not evaluated. T3 (normal-bundle curvature) is the genuinely new object and remains open.
- A3 (the `M^2/r^2` vs `M^2/r^6` Newtonian-scale falsification test) is untouched.
- The oracle covers `R^Y` (mixed base-fiber sectional) and `|A|^2`; it does NOT yet compute the full section
  `II`/`H` of a NON-constant (Schwarzschild) section numerically -- that is the natural A2 extension.
- The convention correction to the two symbolic tests is **reported, not applied** (Joe-review first).

## Grade
- **Part 1 (oracle): computation-grade**, reproducible, exit 0, and it produced a genuine adversarial
  finding (the off-diagonal convention artifact) with two-way cross-checks. Confidence high on the
  confirmations and on the artifact diagnosis (the doubling argument is elementary and the numbers are
  exact rationals).
- **Part 2 (first-variation): structural / scoping-grade.** The term inventory (T1-T4 + `R^perp`), the
  background-subtraction requirement, and the exact `O(M^0)` piece (`H_0 = (1/2)eta`, verified sympy) are
  concrete and correct; no EL was solved and `c_W`/`R^perp_0` remain open.
- No claim/canon movement. Feeds WI-068, the `alpha_W` route, and Thread B (the `O(M^0)` = `Lambda` question).
