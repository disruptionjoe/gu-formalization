---
title: "K1850: vacuum-shift response depends on the metric constraint and boundary ensemble"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: classical fixed-flux shift covariance and explicit stationary controls; no GU, quantum, causal-adjustment or magnitude prediction
---

# A metric response can be shift covariant, with an explicit global datum

A metric-independent top-form constraint supplies a conditional same-action
response to the constant-potential counterexample in [K1848](k1848-screening-shift-protection-2026-10-20.md).
With the top-form flux fixed and its multiplier allowed to vary, an affine
coupling makes the entire classical stationary problem covariant under an
additive vacuum-energy shift. Fixing the multiplier instead removes that map.
For a general coupling, exact unchanged-geometry response to arbitrary shifts
at fixed flux forces the coupling to be affine. A round-sphere solution makes
both the cancellation and its remaining dependence on supplied flux explicit;
a nonlinear coupling gives a strict nonzero curvature response.

This is **boundary-ensemble shift covariance**, not a real-time adjustment or
quantum radiative theorem. The scalar multiplier and top form are supplied
four-dimensional construction data. They are not Weinstein's ad-valued
connection distortion, its Shiab, observation map or physical boundary law.
SC-COS-50/51/54 and SC-ACT-01/02 remain ASSERTS; SC-META-53 remains UNCERTAIN.
LT-GR2c/2d/6b and LT-SM8, the source register, ledger and canon are unchanged.
No novelty or external acceptance is asserted.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: fixed-flux affine shift covariance, opposite-ensemble countercontrol, topology constraint and round-sphere solutions
carrier: real metric, matter, scalar multiplier and metric-independent four-form on an oriented four-manifold LAYER=toy CHIRALITY=N/A
pairing: metric volume for Einstein and matter terms, oriented top-form integration for multiplier coupling ON=real_classical_fields
real_structure: real scalar multiplier and real four-form; no GU real-form identification
grading: differential-form degree, not physical chirality or GU super grading
action_owner: repository-construction -- Einstein action with explicitly added top-form constraint
target: stationary metric response under constant matter-potential shifts at specified global data MAP-TYPE=evaluation
```

## 1. Question, source boundary and previous work

The downstream demand is insensitivity of the **metric equation** to an
independent constant added to the matter potential. K1848's source-conjugate
scalar readout does not meet this demand: its protected response coexists with
a changed Hilbert stress. Here the metric is varied in the same action as the
candidate compensation field, and its boundary/global data are stated before
solving anything.

The source's movable ad-valued one-form and two-field equality do not specify
this construction. SC-COS-54 does not identify the curvature field or write an
action. SC-ACT-01/02 name I1B and swervature/displasion; an Einstein-plus-top-form
action is not their derived observation. The existing [global-projector
result](selected-k77-global-projector-amplitude-layer0-2026-08-10.md) removes
constant source shifts conditionally but does not derive the present metric
constraint or select a magnitude. July unimodular reservoir discussions are
prior conceptual context. The [CBRS1T top-form discussion](selected-k77-cbrs1t-minimal-lorentz-coframe-2026-08-22.md)
prices a kinetic top-form's continuously adjustable stress; this different
metric-independent constraint does not reopen its target-fitted action class.

The standard top-form framework is already known: see [Kaloper, Padilla,
Stefanyszyn and Zahariade, equations (4)--(8)](https://arxiv.org/html/1505.01492v2).
Their two-variable sequestering theory adds a varying Planck coefficient and
a second constraint. The fixed-Planck, single-multiplier system below is not
that full theory, and the present calculation does not reproduce its quantum
claim. The relevance of boundary choices also appears in [Buchmueller and
Dragon](https://arxiv.org/abs/2203.15714).

Preflight lenses: variational analysis favors a full metric-plus-auxiliary
variation over another readout subtraction; global analysis requires the flux
sector and admissible variations; the source lens forbids identifying the new
multiplier with GU distortion. A useful-precision Fisher shape bound remains
an independent substantial alternative. The selected calculation tests a
specific missing response owner without requiring completion of all GU gravity.

## 2. Action and domain: the auxiliary constraint really is varied

Let M be a connected oriented smooth four-manifold, K>0 fixed, and sigma a C2
function with sigma' nonzero on a connected multiplier interval. Use

```
S = S_EH[g;K] + S_m[g,psi] - integral_M lambda vol_g
    + integral_M sigma(lambda) F.                          (1)
```

F is a real smooth four-form independent of the metric off shell. There are
two legitimate domain realizations:

- On a compact region with boundary take F=dA with a global three-form A and
  fix its tangential boundary value. Then Phi=integral F=integral_boundary A
  is fixed. Compact interior variations of A are unrestricted. Fix induced
  metric data and include the usual Einstein boundary term; matter variations
  obey their chosen fixed boundary conditions.
- On a closed compact manifold take F in a specified de Rham cohomology class,
  and vary F by d a, where a is an arbitrary globally defined three-form.
  A potential for F need exist only locally; **no global A is assumed**.
  For a connected closed oriented four-manifold, fixing the integral fixes
  the real top-degree cohomology class. No flux quantization is imposed.

The top-form term's first variation is

```
delta integral sigma(lambda)F
 = integral sigma'(lambda) delta_lambda F
   - integral d sigma(lambda) wedge a
   + integral_boundary sigma(lambda) a.                   (2)
```

The boundary term vanishes for the first domain's fixed tangential A and is
absent in the closed domain. With the matter stress convention chosen so that
S_m -> S_m-C integral vol_g gives T -> T-Cg, the field equations are

```
K G_munu = T_munu - lambda g_munu,
d sigma(lambda)=0,
vol_g = sigma'(lambda) F.                                 (3)
```

The form term has no separate metric variation: substituting its on-shell
value before varying the metric would incorrectly erase the multiplier
stress. Since sigma' never vanishes, lambda is constant. At finite positive
volume, integrating the last equation gives

```
V = sigma'(lambda) Phi,       V=integral vol_g >0.          (4)
```

These are statements about stationary solutions, conditional on their
existence. No Lorentzian initial/boundary well-posedness theorem is imported.
The subsequent sphere supplies an explicit nonempty solution class.

## 3. Arbitrary constant shifts classify the fixed-flux coupling

Add a constant C to the matter potential. The matter equations are unchanged,
but its stress becomes T-Cg. At unchanged metric and matter configuration,
the first equation in(3) requires precisely

```
lambda_new = lambda-C.                                    (5)
```

Keeping Phi and the metric fixed in(4) requires

```
sigma'(lambda-C)=sigma'(lambda).                          (6)
```

Phi cannot be zero in this finite-volume class. Requiring(6) for all small C
and all lambda in a connected interval gives sigma''=0 there. Conversely,
for sigma(lambda)=alpha lambda+beta with alpha!=0, all three local equations
are preserved with F unchanged. More strongly, at fixed flux the full action
obeys the off-shell identity

```
S_new[g,psi,lambda-C,F]-S_old[g,psi,lambda,F]
 = -alpha C Phi.                                          (7)
```

The right side is constant on the admitted configuration space. Thus the
stationary problems map exactly, including their allowed variations. This is
an if-and-only-if classification of **arbitrary-shift covariance with unchanged
geometry and fixed flux in this one-multiplier class**. It does not say every
nonlinear sigma fails for every isolated shift: a periodic derivative can
agree at isolated separated arguments. Both lambda and lambda-C must remain
inside the stated interval.

In the affine class(4) fixes V=alpha Phi, requiring alpha Phi>0. It does not
fix the residual curvature independently of boundary and flux data. The
multiplier may be determined by a specified global stationary problem;
calling it an integration constant alone neither predicts its value nor
proves a dynamical screening process.

## 4. The opposite ensemble changes the conclusion

For the boundary-region realization, add the Legendre boundary term

```
B=-integral_boundary sigma(lambda) A.                     (8)
```

Combining its variation with(2) leaves
`-integral_boundary sigma'(lambda) A delta_lambda`.
This permits fixed lambda at the boundary while A varies there. The bulk
Euler equations remain(3). Connectedness then fixes the same constant lambda
throughout the region.

The map(5) is not an allowed variation between problems with the same fixed
lambda boundary datum. The metric equation instead responds to T-Cg as in
Einstein gravity with that fixed cosmological multiplier. A constant-curvature
vacuum obeys R=4(lambda+rho)/K, so at fixed lambda its algebraic derivative is
`dR/drho=4/K`. This is a local vacuum relation, not an existence assertion for
every choice of Dirichlet metric boundary data.

Transforming the prescribed lambda datum too would compare different
boundary problems. It cannot establish response at fixed original data.
Likewise, changing Phi to rescue a nonlinear sigma changes the fixed-flux
experiment. Boundary conditions belong in the theorem, not in its footnotes.

## 5. Released consequence: a complete round-sphere calculation

Use the Euclidean stationary continuation with equations(3) and no matter
excitations beyond vacuum potential rho. Take the standard round S4 with
`s=r²>0`, put `c=8 pi²/3`, and choose a nonzero fixed cohomology class for F.
The metric curvature and volume are

```
V=c s²,    R=12/s,    G_munu=-(3/s)g_munu,
lambda+rho=3K/s.                                         (9)
```

The form `F=vol_g/sigma'(lambda)` satisfies its local equation and has the
specified flux exactly when `c s²=sigma'(lambda)Phi`. It is not globally exact.
This verifies the entire auxiliary and metric system, not only its trace.

### Affine exact cancellation and the residual datum

For sigma=alpha lambda+beta and alpha Phi>0,

```
s=sqrt(alpha Phi/c),
R=12 sqrt(c/(alpha Phi)),
lambda=3K/s-rho.                                         (10)
```

The radius, scalar curvature, metric and F are unchanged when rho is shifted
and lambda compensates. The result demonstrates a nonempty fixed-flux
stationary family. Its curvature is nevertheless chosen by the supplied
alpha Phi and geometry; a large volume/small curvature is not predicted.
It is neither a Lorentzian universe nor evidence of causal late relaxation.

### Nonlinear same-flux countercontrol

Choose sigma=lambda²/2 on lambda>0, Phi>0 and rho>=0. Equations(9) become

```
lambda=c s²/Phi,
3K=rho s+(c/Phi)s³.                                      (11)
```

The right side is continuous and strictly increasing from zero to infinity,
so there is a unique positive solution for each K>0. Implicit differentiation
at fixed K,c,Phi gives

```
ds/drho=-s/[rho+3(c/Phi)s²],
dR/drho=12/{s[rho+3(c/Phi)s²]} >0.                        (12)
```

Thus unchanged-geometry response fails even though the multiplier remains a
constant and the metric equation permits the formal subtraction(5). The
second variational equation matters. At the rational algebra control
`s=2,c=3,Phi=6,K=2,rho=1,lambda=2`, (11) holds,
`ds/drho=-2/7`, `dR/drho=6/7`. Here c=3 is only a rational algebra fixture;
the geometric sphere always uses c=8pi²/3. The proof is symbolic in positive c.

## 6. Topology, local variation and what has not been supplied

If M were compact boundaryless and F=dA globally, Stokes would give Phi=0,
contradicting(4). The closed-sphere construction explicitly uses nonexact F;
the region construction explicitly has a boundary. Flux quantization, charged
membranes, and a measure over sectors have not been supplied.

On the conserved matter shell, the Bianchi identity in(3) also requires
dlambda=0, consistent with the auxiliary equation. A varying *pure-trace*
auxiliary source cannot be obtained from this model. If the imposed potential
shift is C(x), the proposed compensation lambda-C(x) fails its form equation
unless dC=0. A genuine phase transition carries additional dynamical fields,
exchange stress and matching data; it cannot be modeled by silently replacing
a constant C by C(x) in(7). No finite-time relaxation or interacting response
has been established.

The source-native next task remains an actual observation/metric/constraint
adapter or a specified different dynamical mechanism. A four-form is not an
ad-valued one-form; an independent classical global datum is not a GU-derived
normalization. This example neither resolves nor excludes the source claim.

## 7. Reproduction, hostile checks and resulting frontier

Run `sage -python tests/channel-swings/k1850_metric_screening_ensembles.py`
and `python3 tests/channel-swings/k1850_metric_screening_ensembles_probe.py`.
The symbolic producer checks the vacuum/multiplier signs, affine and nonlinear
action differences, Legendre boundary variation, trace coefficients, sphere
equations, response derivatives and certificate values. The independent
Fraction probe uses separately evaluated rational stationary families,
polynomial coefficient translations, finite action changes and derivative
residuals; planted coefficient/sign/fixture faults are distinct from scope
reporting mutations. Dependency hashes pin K1848; its tests are not counted as
a fresh replay. The written variational, topology and arbitrary-shift proof
owns the continuum conclusion. Finite algebra tests do not prove those steps.

Postflight lenses: full variation rejects on-shell substitution before metric
variation; global analysis rejects a globally exact form on closed S4; boundary
analysis distinguishes fixing A from fixing lambda; cosmology rejects a
Euclidean stationary fixture as causal adjustment; source fidelity leaves all
GU verdicts unchanged. The affine proof, nonlinear countercontrol, opposite
ensemble, topology consequence and solved sphere exhaust the immediate
consequences selected here. The useful remaining branches are a native
constraint/domain adapter, quantum preservation with a specified measure, or
an actual dynamical relaxation construction. Another formal trace subtraction
would not settle any of them.
