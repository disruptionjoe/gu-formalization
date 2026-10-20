---
title: "K1860: a scale zero-mode compatibility test for a proposed I1B vacuum response"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional stationary-family compatibility theorem; global GU realization and observed-volume coupling unconstructed
---

# A proposed global vacuum response must account for the scale zero mode

The actual first-action structure gives a useful necessary test for a proposed
global completion. If its Ricci-flat, zero-distortion stationary family admits
a scale variation with zero boundary pairing, adding an observed-volume source
has **no differentiable stationary continuation** through that family. This
follows by pairing the differentiated field equation with the stationary scale
mode. It needs no inverse of the distortion operator and no positivity claim.

The local source-derived evidence and the global hypotheses are separate.
[K127](selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md)
constructs local stationary germs; it does not construct the global domain,
scale variation or observed-volume coupling assumed here. Consequently this
is a test for a future adapter, **not an adverse result about GU**, and it
does not establish or refute vacuum screening in the source theory.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: conditional compatibility test, boundary pairing requirement and exact nonsmooth countercontrol
carrier: native metric and augmented-distortion variations, plus a declared observed four-dimensional volume probe LAYER=ambient+observed BRIDGE=assumed-stationary-family-observed-volume-coupling CHIRALITY=N/A; this global bridge is a theorem hypothesis, not an authenticated GU construction
pairing: action Hessian dual pairing on its declared variational domain; observed volume is an additional probe ON=real_variations
real_structure: real metric and real source-coordinate distortion; no real-form transport
grading: metric versus connection-difference variations and differential order; no particle grading
action_owner: repository-construction -- conditional global completion and added observed-volume probe; the reused local I1B degree structure is source-action evidence
target: necessary condition for a differentiable stationary response to an independently varied volume coefficient MAP-TYPE=evaluation
```

## 1. Source, retrieval and hypothesis custody

SC-ACT-01 ASSERTS the torsion/Shiab first action, with its connection-path
coefficients 1/2 and 1/3. SC-ACT-02 ASSERTS the swervature/displasion equation
and its annotated Einstein-like interpretation. SC-COS-50/51/54 ASSERTS the
variable, VEV-capable dark-energy and curvature-covariation claims. COS54's
registered wording is a record's paraphrase, and that record does not identify
the curvature field or supply an action. SC-META-53 remains UNCERTAIN about
the unbounded-spectrum problem. Source adherence is not physical validation.

The native local action in independent coordinates is

```
varpi = B_LC(g) + T,
I(g,T) = <T,S_g(F_B)> + (1/2)<T,S_g(D_B T)>
         + (1/3)<T,S_g(T^2)> + (kappa_1/2)<T,*_g T>.
```

The metric, pairing, Shiab, frame and B_LC dependence move together. In
particular, [K128](selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md)
already proves `I(g,0)=0` and the stationary Hessian block form

```
H = [[0,A*],[A,C]].                                      (1)
```

[K129](selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md)
identifies the local mixed block `A=D_g[S_g(F_B)]` and distortion block
`C=kappa_1 K+E(D_B)`. Neither a physical Einstein Hessian nor a closed inverse
of C is imported. At local Ricci-flat T=0 germs, constant metric rescaling
preserves Ricci-flatness and the zero translation row, so the corresponding
formal scale direction lies in `ker A`.

This local statement does not prove the following global assumptions:

1. A C2 variational functional on one common field/domain chart realizes a
   **fully stationary** family `z(c)=(c^2 g0,0)`, for c near1. All other
   native fields, observation data and background identifications must be
   moved as required for this assertion; local jets alone do not suffice.
2. Its tangent `v=z'(1)` is an admissible variation, and the actual Hessian
   dual pairing has no uncancelled boundary contribution on the response
   domain. The full tangent includes any required dependent fields.
3. The proposed observed coupling really is
   `S_rho=I+rho V`, with `V=integral_X vol_g`, finite and strictly positive,
   and `V(z(c))=c^4 V(z(1))`. This is an explicitly added response probe,
   not a source-derived matter/observation coupling.
4. A candidate stationary response is C1 in rho in a topology where the
   differentiated equations and pairings below are legal. A formal local
   operator or pointwise rank does not establish this analytic assumption.

The prior global-projector calculation supplies a conditional normalized
functional and removes constant sources by construction; it does not derive
these hypotheses for I1B. K631/K632 close a different current-carrier
ownership-composition question. K723/K747--750/K799--802 concern the
highest-order response of the K127 family, not its volume-source solvability.
K1850/K1852 use explicit auxiliary top-form and wall actions. Their
compensation fields are not identified with T here. These held results are
reused, not reopened.

Preflight perspectives: variational analysis proposes the exact stationary
zero mode before a new Schur solve; global analysis tests its domain;
source criticism distinguishes the published first-action structure from an
unpublished observation coupling; the contrary-construction lens asks about
boundary flux, constrained volume and singular response. A full-I1B global
construction remains more expensive than this necessary test. Independent
Fisher endpoint work remains a separate mathematical payoff.

## 2. Conditional compatibility theorem

Differentiate `DI(z(c))=0` at c=1. With `H=D2 I(z(1))`,

```
H v = 0.                                                (2)
```

Suppose a C1 branch `z_rho`, with `z_0=z(1)`, is stationary for `S_rho`.
Differentiating its full Euler equation gives, as a covector equation,

```
H w + DV = 0,                 w=(d z_rho/d rho)|0.        (3)
```

Pair with v. Symmetry of the actual action Hessian on the stated domain
and (2) imply `<v,Hw>=<Hv,w>=0`. However,

```
DV[v] = (d/dc)(c^4 V0)|c=1 = 4 V0 > 0.                  (4)
```

Equations (3) and (4) contradict one another. Thus no such C1 stationary
branch exists. The sign convention `I-rho V` changes the sign, never the
nonzero conclusion. In observed dimension d, the factor is d, and for the
alternative tangent `g_c=c g0` it is d/2; mixing these conventions would
produce a spurious coefficient disagreement.

For the two-field block (1), (2) reads `A v_g=0`. Equation (3)'s metric row
is `A* w_T + DV=0`, and pairing with `v_g` proves the same result. The
value, signature, kernel or invertibility of C is irrelevant. Allowing the
metric itself to move does not fix the compatibility condition because the
pure metric Hessian vanishes on this stationary family. The theorem neither
requires nor supplies a Fredholm property, a selected Riesz identification,
positive physical states, a global GU solution or a source variation of a
four-dimensional Einstein action.

More generally, *every* tangent to a stationary manifold must annihilate
the perturbing functional for a differentiable stationary branch to start
there. Scale and volume make that necessary condition explicit in this case.
The general variational argument is not claimed as new mathematics.

## 3. Released domain and counterexample tests

### Boundary flux is an exact missing datum

If one uses a bulk formal differential operator instead of the true Hessian
domain, define its Green defect by

```
B(v,w) = <v,Hw> - <Hv,w>.
```

At `Hv=0`, the differentiated bulk equation requires

```
B(v,w) = -4 V0.                                         (5)
```

For an infinitesimal source increment `delta rho`, the unnormalized response
has defect `-4 V0 delta rho`. This is a necessary flux budget, not existence
of a boundary solution. A moving boundary, boundary action or changed
boundary ensemble must be varied in the full action before applying the
theorem. Local K127 fixed-boundary germs cannot silently be assigned the
global scale test, since constant rescaling generally changes fixed metric
boundary data.

### Fixed volume changes the admissible question

On a fixed-volume configuration space `DV` vanishes on every admissible
variation; the scale direction in (4) is excluded. Then this compatibility
test gives no obstruction. Equivalently a supplied Lagrange multiplier for
`V=V0` can absorb rho into that multiplier. This does not show fixed volume
is selected by GU, nor does it make its multiplier a native distortion field.

### A continuous branch can evade a differentiable-branch theorem

An exact finite-dimensional countercontrol has metric-scale coordinate c>0,
distortion coordinate t, and action

```
I(c,t) = -(c-1)t^2/2 + t^3/3,    V(c)=c^4.
```

Its entire t=0 line is stationary. At `(c,t)=(1,0)` the Hessian is zero
and `DV[v]=4`; the theorem excludes a C1 response in rho. Nevertheless,
for every sufficiently small nonzero real x with1+x>0,

```
c=1+x,   t=x,   rho=x^2/[8(1+x)^3]                     (6)
```

solves both exact stationary equations of `I+rho V`:

```
-(c-1)t+t^2=0,        -t^2/2+4 rho c^3=0.
```

Each side x>0 and x<0 parametrizes a continuous small positive-rho branch.
Since `rho/x^2 -> 1/8`, its displacement is proportional to sqrt(rho),
so it is not differentiable at rho=0. This is an algebraic countercontrol,
not an I1B global solution; its singular normal Hessian is deliberate.
It prevents upgrading the theorem to absence of all nearby solutions.

## 4. Review, verification and consequence

Postflight hostile review:

- Strongest overclaim: declaring GU unable to screen vacuum energy from local
  T=0 jets. Rejected: global stationary scale-family, domain and observed
  coupling premises remain explicit and unproved.
- Strongest contrary construction: boundary pairing, fixed-volume variations,
  nonzero-distortion backgrounds, extra action terms or non-C1 branches. The
  first two and the exact square-root branch are analyzed above; the others
  change hypotheses rather than contradict the theorem.
- Weakest reproducibility seam: finite block tests do not verify a global
  field-theory Hessian or an actual physical domain. The written dual-pairing
  argument owns the conditional theorem; exact rational checks only verify
  scaling, block pairing and the countercontrols. No proof-assistant,
  external-expert or complete source-action verification is claimed.

The immediate successor is now specific: for a proposed *same-action*
observed-volume response, construct the global stationary tangent and
evaluate its actual boundary pairing, or explicitly show which of the
stationary-family, coupling, domain or regularity hypotheses changes. A
second pointwise Shiab rank computation cannot answer that test. A nonzero
T branch is not judged by this T=0 result.

LT-GR2c/2d/6b and LT-SM8, the ledger's88 active targets/91 stored records,
all source polarities and canon remain unchanged. This records a conditional
adapter requirement, not a recovered physical mechanism, new physical
exclusion, radiative-stability result or numerical magnitude prediction.

Reproduce the narrow controls:

```
python3 tests/channel-swings/k1860_i1b_vacuum_zero_mode.py
python3 tests/channel-swings/k1860_i1b_vacuum_zero_mode_probe.py
```
