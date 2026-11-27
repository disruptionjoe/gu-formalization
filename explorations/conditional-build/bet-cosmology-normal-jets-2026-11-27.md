---
title: Finite normal jets do not supply compact excitation charge from coclosure alone
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Determine whether finite local dependence on normal values or derivatives escapes the owned conservation-descent and compact-charge result under ambient coclosure alone.
actual_delta: Every finite ambient solution jet is expressed through finitely many freely prescribable section fields and their tangential jets. Universal conservation becomes an identity in those fields; on the admitted cutoff-closed class every background-subtracted compact excitation charge vanishes.
class_covered: All fixed smooth nondegenerate ambient metrics, nondegenerate sections of positive codimension, finite-rank coefficient bundles with fixed smooth connection, and fixed smooth positive weights independent of theta. Readouts may use every ambient derivative through any fixed finite order. The charge theorem uses one adapted collar and observed product patch, with compact free-data jets and an admitted cutoff extension.
premises:
- lab/sources/source-claim-register.yaml#SC-COS-50
- lab/sources/source-claim-register.yaml#SC-COS-51
- lab/sources/source-claim-register.yaml#SC-COS-52
- explorations/conditional-build/bet-cosmology-conservation-descent-2026-11-27.md
- explorations/conditional-build/compact-excitation-charge-2026-11-27.md
- explorations/conditional-build/source-action-theta-divergence-2026-11-27.md
source_bridge:
  status: conditional
  reason: The source asserts an automatic dark-energy identity and an adjoint one-form replacement, but does not select coclosure alone as its equations, a finite local readout, fixed geometry, a cutoff-closed physical domain or nonzero compact excitation charge.
kill_condition: Finite local normal dependence alone cannot yield a universally conserved observed current with nonzero background-subtracted compact excitation charge on the declared coclosed-germ and cutoff-admissible class.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-FINITE-AMBIENT-JET-CONSERVATION-DESCENT
internal_target_verdict: Finite normal-jet dependence alone does not repair the compact-excitation conservation bridge under the stated premises.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Finite ambient jets and compact excitation charge

```yaml
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Determine whether finite local dependence on normal values or derivatives escapes the owned conservation-descent and compact-charge result under ambient coclosure alone.
actual_delta: Every finite ambient solution jet is expressed through finitely many freely prescribable section fields and their tangential jets. Universal conservation becomes an identity in those fields; on the admitted cutoff-closed class every background-subtracted compact excitation charge vanishes.
```

## Result first

**Allowing any fixed finite number of normal derivatives does not, by itself, turn ambient one-form conservation into nonzero compact excitation charge.** The normal equation solves one flux component. Its finite derivatives are determined by finitely many independent normal Taylor coefficient fields on the section. A conserved readout therefore becomes an identity in those free fields, after the coclosure equation and its prolongations have been eliminated.

The existing compact-charge theorem then applies to cutoffs of the **free data**, followed by the exact normal ODE lift. Multiplying an already coclosed ambient field by a cutoff would generally violate the equation and is not the construction used here.

| State | Scope |
|---|---|
| ESTABLISHED by the written proof | All-finite-order ambient solution-jet parametrization, closure under observed differentiation, conservation identity in finitely many free fields, and the corresponding zero compact-charge consequence. |
| RULED OUT | Finite local normal dependence alone as a repair under coclosure alone, universal germ conservation and the stated cutoff-admissible field domain. |
| SURVIVES / OUTSIDE THE CLASS | Further equations, normal-flux restrictions, global or topological domains, nonlocal/infinite-order readouts, coupled background dynamics, and noncompact or unsubtracted background charge. |
| NOT ESTABLISHED | Source cosmology falsification, a physical stress identification, energy positivity, a full source/W2 solution space, CMB/DESI predictions or a GU verdict. |

```gu-typed-objects
result: all-finite-ambient-jet conservation descent and compact-excitation charge obstruction
carrier: finite jets of coefficient-bundle-valued ambient one-forms restricted to a nondegenerate section, with full coefficient fibre retained LAYER=ambient+observed BRIDGE=local_solution_jet_parametrization CHIRALITY=N/A
pairing: fixed nondegenerate ambient metric and positive scalar weight; charge uses an independently specified fixed positive observed density ON=ambient_one_forms_and_observed_current
real_structure: real coefficient bundle including an adjoint Lie algebra; complex version componentwise; no Clifford/adjoint transfer between K77 and K95
grading: exterior degree1 and finite ordinary jet order; no physical-generation grading
action_owner: repository-construction of an implication-class test; no action, stationary system or physical domain selected
target: coclosure solution jets and observed local current conservation MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** An adjoint one-form and an observed stress are distinct objects. This grants a proposed coclosure identity and tests its sufficiency, retaining normal data rather than replacing the source with a scalar cosmology. [Routing](../../lab/methods/source-native-comparator-routing.md).

The [conservation-descent result](bet-cosmology-conservation-descent-2026-11-27.md) owns the smooth normal ODE and the observed-only readout theorem. The [compact-charge result](compact-excitation-charge-2026-11-27.md) owns the locality/cutoff/Stokes argument. Both explicitly leave finite normal-jet readouts outside their prior scope. The new content is the finite prolonged-jet parametrization and its compatibility with observed differentiation and free-data cutoffs; their earlier proofs are reused.

## 1. Precise local setting

Hold fixed a smooth nondegenerate pseudo-Riemannian metric G, a nondegenerate embedded section S of positive codimension, a finite-rank real coefficient bundle with smooth connection A, and a smooth strictly positive scalar weight rho independent of theta. Complex coefficients are the componentwise complex version. Use

```
delta_A^rho theta
 = -mu^-1 [partial_i(mu G^ij theta_j)+A_i(mu G^ij theta_j)],
mu=rho sqrt(|det G|).
```

Every point of S has a non-null normal direction. Locally choose a nondegenerate hypersurface H containing S with that normal, then a Gaussian collar `(r,z)` of H, where `z=(x,y)` and `S={r=0,y=0}`. Here x are section coordinates, y are the remaining normal coordinates, and

```
G=epsilon dr^2+h_ab(r,z) dz^a dz^b, epsilon in {+1,-1}.
v^a=mu G^ab theta_b,
w=mu epsilon theta_r.
```

This is an invertible smooth fibre change, with inverse `theta_r=epsilon w/mu` and `theta_b=mu^-1 h_ba v^a`. It keeps every metric/density derivative when jets are taken. The choice of collar is a local proof coordinate, not a physical normal selection.

The equation is exactly

```
partial_r w + A_r w
 = -sum_a [partial_a v^a+A_a v^a].                    (1)
```

Thus v(r,z) is arbitrary smooth data, as is w0(z)=w(0,z). The linear parameter-dependent ODE supplies a unique local smooth w. Smoothness, not analyticity, suffices. No infinite formal Taylor convergence or CK argument is used.

For adjoint coefficients, the already-owned extension `A=B+s theta` has the same equation because `s G^ij[theta_i,theta_j]=0`. This permits prescribed smooth scalar s, with no derivative of s in this connection difference. General field-dependent connections/densities remain excluded. A finite readout written using the affine connection is still a finite coordinate-jet function after this substitution.

## 2. Finite jets and compatibility

Fix ambient readout order k>=0. Define the following finite list of independent section fields:

```
V^a_(j,beta)(x) = partial_r^j partial_y^beta v^a(0,x,0),
                  j+|beta| <= k,
W_beta(x) = partial_y^beta w0(x,0),  |beta| <= k.
```

Call this list U. Each entry is a smooth coefficient-vector-valued function on S. Multiindices already impose the ordinary symmetry of commuting coordinate derivatives. One does not independently prescribe noncommuting covariant derivative slots; their curvature compatibility follows from conversion to coordinate jets with fixed backgrounds.

Every theta jet of total ambient order<=k on S is a finite differential expression in U and its tangential x-jets of order<=k, with fixed background coefficients. To see this explicitly, put `w_p(z)=partial_r^p w(0,z)` and `v_p^a(z)=partial_r^p v^a(0,z)`. For p>=1, equation(1) yields

```
w_p = -sum_(ell=0)^(p-1) binom(p-1,ell)
           (partial_r^ell A_r)|0 * w_(p-1-ell)
      -sum_a partial_a v_(p-1)^a
      -sum_a sum_(ell=0)^(p-1) binom(p-1,ell)
           (partial_r^ell A_a)|0 * v_(p-1-ell)^a.       (2)
```

This is triangular in p. Applying partial_y^beta with p+|beta|<=k requires free v normal derivatives of order at most p-1+|beta|+1<=k, and W derivatives of order at most k. For a requested mixed derivative of total ambient order at most k, only the corresponding tangential derivatives are applied, within that bound. Multiplication by mu^-1,h and their derivatives completes the reconstruction of theta. All varying connection, density and metric coefficients are retained.

Conversely, every smooth list U is realized. Choose a normal cutoff chi(r,y) identically1 near(0,0), and set

```
v^a(r,x,y)=chi(r,y) sum_(j+|beta|<=k)
                   r^j y^beta/(j! beta!) V^a_(j,beta)(x),
w0(x,y)=chi(0,y) sum_(|beta|<=k) y^beta/beta! W_beta(x).
```

Solve the exact ODE(1). It preserves all the prescribed free normal coefficients and imposes the dependent w coefficients through(2). This is an actual smooth solution near S, not merely a formal solution jet.

Equivalently, at each point the k-jets satisfying the coclosure equation and all its coordinate prolongations of order<=k-1 are parametrized by the free v jets and the r-free w jets. Equation(2) gives every dependent coefficient; differentiating it supplies all cross-derivative compatibilities. There is no further formal integrability condition. The U list may contain tangential jets unused by a particular order-k readout, which is harmless redundancy, not an extra equation.

**Important closure point:** tangential differentiation of the reconstructed readout requires higher x-jets of this same finite list U, not new normal coefficient fields. Thus divergence of an order-k readout is a finite-order differential expression, of order at most k+1, on the U fields. The list does not grow into an infinite tower merely because conservation differentiates the readout once.

## 3. What the identity theorem says

Let a smooth observed current/stress readout depend locally on the full ambient k-jet of theta along S, and on fixed background jets:

```
J[theta](x)=F(x,j_M^k theta|S).
```

Its substitution by(2) is a finite-order local readout `Jbar[U]`. If a claimed observed differential conservation law holds for **every** local coclosed germ, it holds for every smooth U, because every such U has an exact lift. Hence it is an off-shell differential identity in these finitely many free fields. Conversely an identity for every U holds for every coclosed germ by extracting its free data.

This is an identity **after eliminating coclosure and its prolongations**. It is not an identity on unrestricted ambient theta jets. The distinction matters: readouts proportional to the ambient equation vanish on its jet locus but need not vanish off that locus. Gauge covariance or tensoriality of F can be additional restrictions; neither is needed for the implication.

The result applies on the full free-data jet domain, or on an explicitly stated restricted domain with its actual realizability. A restriction on theta jets becomes a restriction on U jets; it cannot be erased by calling U free. Arbitrary additional equations, boundary laws, physical domains and topological sectors are not covered.

## 4. Support and compact charge

Work first on a section product cylinder P=I_t times O_x contained in one such collar/trivialization chart. Use a smaller closed slab and spatial compact K in the interior. The full-domain version admits all smooth U with the relevant finite jets; zero is admitted. A restricted version requires the exact compact extension below to remain admitted.

Because the equation is homogeneous, zero data lifts to theta=0. Define the background-subtracted readout

```
Delta Jbar[U]=Jbar[U]-Jbar[0].
```

Where U vanishes on a neighborhood in S, all required x-jets vanish and Delta Jbar vanishes. Background coefficients may vary arbitrarily; this locality statement is unchanged. The ODE construction also does not spread support in x: if U vanishes on an x-neighborhood, the displayed extensions, source and initial w vanish there, hence w does as well. The lift may nevertheless extend indefinitely in the selected normal direction, so compact ambient support is not claimed.

Assume the conserved current satisfies `partial_mu(nu Delta Jbar^mu)=0` with fixed smooth positive observed density nu. For compact compatible slice jets at t0, realize the required time derivatives of each free field by finite temporal Taylor polynomials multiplied by a compact time cutoff equal1 near t0. Keep all spatial coefficient data supported in K. This preserves the readout on the entire slice and makes the free data zero at a nearby terminal time and near the spatial side boundary.

The already-owned Stokes argument now applies to Jbar: final charge and side flux vanish, so

```
integral_O nu(t0,x) Delta Jbar^t(t0,x) dx = 0.
```

The compactness requirement is on the admitted free-data slice jets (or compatible solution jets having such an extension), **not merely accidental compact support of J itself**. Cutting noncompact data can create extra current in the cutoff region. For a full jet domain, any compactly supported compatible ambient solution jet has the needed free-data extension: its relevant free coefficients are compactly supported and unused Taylor coefficients can be set to zero.

This proof is local on an observed cylinder. No global ambient solution or physical evolution is required, because the substituted identity holds pointwise for arbitrary smooth U. A global section charge needs actual globally defined readout/current data and a compatible global cutoff construction; local collar choices alone do not prove that. Nontrivial normal topology or physical boundary restrictions cannot be silently removed by partitioning a global lift. Homogeneous/noncompact and unsubtracted background charges remain outside.

## 5. Positivity and the sharp solution-jet ceiling

If the real excitation density relative to an actual positive slice measure is nonnegative for every admitted compact free-data test, its zero integral forces it to vanish pointwise on every such test. A strictly positive value would persist on an open set and give positive integral. On the full free-data domain, polynomial jets times a bump realize every compatible finite coclosed solution jet. The density therefore vanishes on that prolonged solution-jet locus. It need not vanish on arbitrary ambient jets failing coclosure.

For a restricted domain, only compactly realizable solution jets are covered. For a stress-to-energy statement, retain the owned assumptions: a symmetric conserved observed stress, an actual Killing/translation contraction giving a conserved current, and for energy a spacelike slice, timelike generator and consistent flux orientation. Covariant stress conservation on an arbitrary time-dependent background is insufficient to manufacture coordinate energy. Zero charge or one zero energy density is not zero local stress.

## 6. Sharp countercontrol and calibration scope

In a codimension-one flat collar with observed(t,x), trivial connection and mu=1, take tangential free flux `v^t=v^x=f(x-t)` with f smooth, compactly supported, nonnegative and nonzero, and w=0. It is coclosed and the tangential current has strictly positive compact slice charge. This does not contradict the theorem: tangential current conservation is only guaranteed on the **additional** zero-normal-flux domain, not for every coclosed germ.

Here the extra restriction is w identically zero throughout the collar, not merely w|S=0; the latter alone does not force tangential conservation. In higher codimension, this countercontrol sets every normal flux identically zero and takes tangential fields independent of all normal coordinates. Setting just one normal flux to zero leaves other compensating normal channels.

A time cutoff v -> chi(t)v produces tangential divergence chi'(t)f(x-t). The unrestricted coclosure equation repairs it with

```
w(r,t,x)=-r chi'(t) f(x-t),  w0=0.
```

The repair leaves the zero-normal-flux domain, explaining exactly why the positive-charge restricted example evades the theorem. This is a same-one-form boundary control, not a scalar cosmology replacement.

Relevant finite controls are both normal signs; nonconstant mu and nonabelian A in recurrence(2); independent mixed y/r derivatives and one extra x derivative; finite Taylor realization without demanding an infinite series; zero-data/support locality; the zero-flux cutoff failure just shown; and a nonzero differential improvement depending on a normal coefficient, with zero compact charge. The final execution record identifies which fixtures were run. Finite checks calibrate the written all-k proof rather than exhaust it.

## 7. Source, reuse and decision

The result holds at the stated local, fixed-background, full-coclosed-germ scope. It extends the expressly observed-only prior class to **every fixed finite ambient-jet order**, including normal values and derivatives. It can retire finite normal dependence alone as a compact-charge repair under coclosure alone. It does not classify all currents as global superpotentials, provide a bound on a fixed tube, establish norm continuity, or identify source/W2 solutions with these test fields.

Source SC-COS-50/51/52 does not select coclosure alone, the readout, fixed geometry or a cutoff-closed physical domain. The source bridge remains conditional; no source/GU/physical-energy/CMB verdict follows. The strongest remaining scientific branch needs an already-owned additional equation or boundary/physical-domain law that actually restricts the independent free coefficients. Merely replacing one finite normal-jet formula by another cannot evade the proved class. No new action, selector, Green operator, or domain is installed.

### Exact source footing

SC-COS-50 (`ASSERTS`) is the TOE2025 automatic-identity claim at02:14:44, with02:15:25–02:16:02 continuation and the conditional continuing-DESI framing. SC-COS-51 (`ASSERTS`) gives the adjoint-one-form replacement at02:22:20–02:23:28, with its spoken-formula qualification. SC-COS-52 (`ASSERTS`) is the UCSD2025 seminar claim at00:02:05, completed at00:25:56–00:27:00; it must not be attributed to the interview. [The source register](../../lab/sources/source-claim-register.yaml) and [primary pack](../../lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md) retain custody.

Those clauses do not identify this one equation with the full source system. The [canon reconstruction](../../canon/dark-energy-theta-divergence-free.md) also retains the unproved identification of theta with the relevant Euler sector. A coupled Noether identity can involve other equations. Granting coclosure for this sufficiency test does not promote that identification or repeat the [actual-candidate divergence test](source-action-theta-divergence-2026-11-27.md).

This is an LC BET-COSMOLOGY implication-class extension. It installs no new action, potential, weight choice, physical restriction or choice family. It is not imported into a lane-B matrix or a physics-ledger verdict. Homogeneous dark energy and cosmological background charge are not compact excitations, and a general evolving cosmology has no timelike Killing energy supplied by default.

## 8. Standard inputs and verification ceiling

The linear-ODE existence and smooth-parameter input are standard; see Conrad's [linear ODE notes](https://math.stanford.edu/~conrad/diffgeomPage/handouts/linearode.pdf) and [integral curves and smooth dependence](https://math.stanford.edu/~conrad/diffgeomPage/handouts/intcurve.pdf). His [Stokes notes](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokesthm.pdf) explain the metric-independent compact differential-form statement. The weighted indefinite bundle equation, finite recursion and support hypotheses used here are displayed explicitly. No world-novelty claim is made.

[NormalJetRecursion.lean](../../Lean/GUFormalization/NormalJetRecursion.lean) proves uniqueness for a sequence whose next coefficient depends on a supplied right-hand side and arbitrary lower-history map, plus the recurrence rearrangement. It does not formalize smooth ODE existence, Gaussian collars, finite-jet realization, the cutoff construction, Stokes, positivity or source applicability. The existing [CompactCharge finite cores](../../Lean/GUFormalization/CompactCharge.lean) are reused rather than presented as a new Stokes formalization.

The separately owned exact probe calibrates signs, variable coefficients, mixed derivatives and domain countercontrols. The written proof covers all finite k; finite fixtures do not establish that quantifier. The report author ran no local tests or Lean compilation. Final execution counts, hashes and independent T1 review are recorded separately; internal review is not external-expert certification.
