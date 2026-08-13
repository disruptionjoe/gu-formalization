---
title: "Eric/Curt Wave 3D-B2C2A: the ordinary tau tangent exists but is not the W131 BV differential"
status: active_research
doc_type: construction_result
created: 2026-07-31
work_item: ECW3D-B2C2A-TAU-TANGENT-BV-TYPE-AND-CURVATURE-COLLISION
registry: lab/process/eric-curt-wave3d-b2c2-tau-tangent-bv-collision.json
probe: tests/channel-swings/eric_curt_wave3d_b2c2_tau_tangent_bv_collision_probe.py
grade: "DECISIVE TYPE-AND-CURVATURE NEGATIVE for reusing the ordinary tau derivative as the missing W131 tangent/BV differential. The source-backed map d tau_A(xi)=(xi,D_A xi) is an exact nonabelian Lie-algebra homomorphism into the ordinary adjoint connection sector. D_A alone is not nilpotent on a nonflat connection, while G3's full ordinary-gauge BRST closure remains valid but has the wrong carrier for the scalar-spinor to gamma-traceless-vector-spinor W131 complex. Super-IG/RS closure and observer-descending cohomology remain open."
---

# Wave 3D-B2C2A — tau-tangent/BV type and curvature collision

## Result

The derivative-level tau homomorphism is **present**, but it is not the
missing W131 differential.

G1 already constructed the source-guided connection cocycle

\[
q_A(g)=A-g\boldsymbol\cdot A,
\qquad
\tau_A(g)=(g,q_A(g)),
\]

whose tangent at the identity is

\[
d\tau_A|_e(\xi)=(\xi,D_A\xi).
\]

The new exact two-coordinate nonabelian fixture verifies that this tangent
map is a Lie-algebra homomorphism into
`Lie(Gau(P)) semidirect Omega1(ad P)`. This corrects the B2C1 handoff's broad
wording: an ordinary-gauge derivative-level `d_aleph`/tau map is not missing.

What remains missing is much more specific: a source-derived map

\[
S\longrightarrow\ker\Gamma\subset T^*Y\otimes S
\]

for the scalar-spinor/vector-spinor W131 complex, together with its BV
closure, dynamics compatibility, physical cohomology, and observer descent.

## Homomorphism is not nilpotence

Layer 0 must separate three objects:

1. the graph homomorphism `d tau_A` into the ordinary inhomogeneous gauge
   algebra;
2. the covariant de Rham leg `D_A`; and
3. the nonlinear BRST differential with its ghost rule.

On the exact nonflat control,

\[
[D_0,D_1]\xi=[F_{01},\xi]\ne0.
\]

Therefore `D_A` by itself is not a nilpotent cochain differential. The flat
control does square to zero. This does not contradict G3: G3's full ordinary
gauge BRST completion includes `sc=1/2[c,c]`, and its closure and Jacobi tests
pass through antifield number one. The point is that full BRST closure and a
tau-graph homomorphism are different claims.

## Why the ordinary BRST complex does not remove the W131 chains

The carrier mismatch is load-bearing:

| construction | source | target | proved scope |
| --- | --- | --- | --- |
| tau tangent | `Omega0(ad P)` | `Omega1(ad P)` | ordinary inhomogeneous gauge algebra |
| G3 BRST connection leg | parity-shifted `Omega0(ad P)` | `T Conn(P) ~= Omega1(ad P)` | ordinary `Gau(P)` bulk BV |
| B2C1 required differential | scalar spinor `S` | `ker Gamma subset T*Y tensor S` | super-IG/RS physical tangent complex |

No source-derived identification `ad P = S`, no odd super-IG tangent rule, and
no soldering/current map turning an adjoint one-form into a gamma-traceless
vector-spinor is present. Choosing a matrix representation or a background
spinor now would add unpriced structure and could reproduce the target image
by construction. That move is therefore not admitted.

Because no correctly typed differential acts on W131, this swing does **not**
retest the Jordan cohomology. Forming an image from the known rank-128 Jordan
sector would repeat the target-selection error B2C1 prohibited.

## Source collision

Leading disposition: `SOURCE-CORRECTS`.

The UCSD passage at `00:18:03--00:20:57` explicitly places `tau_plus` from the
ordinary gauge group into the inhomogeneous gauge group and gives its
derivative adjoint-one-form component using the distinguished connection
`d_aleph`. It therefore corrects the scope of the missing-object statement.

The same passage is silent on a scalar-spinor/gamma-traceless-vector-spinor
map, super-IG/RS BV closure, W131 Jordan chains, and observer descent. The
source establishes attribution and type, not the new homomorphism/curvature
calculation or a physical quotient.

## Datum, Curt, and promotion boundary

P1/P2/P3 remain unused and their pricing is unchanged. None supplies the
missing carrier bridge. Joe's record/finality idea remains a
`JOE_CANDIDATE_CONTROL`, not an input or a way to change the adjoint carrier
into an RS tangent complex.

Curt remains a formally separated `(7,7)` rival inside the Eric lane. This
complex W131 collision does not transport to Curt's unbuilt real carrier.
The pre-registered rule remains

```text
TG-1 AND TG-2 AND TG-3
```

and is false. No third lane is promoted.

## Boundary and next gate

This result kills only the reuse of the ordinary tau tangent or ordinary
gauge BRST complex as the W131 quotient differential. It does not kill a
source-derived super-IG/RS odd tangent rule, changed action, nonlinear
constraint, anisotropic or pseudodifferential reduction, or ambient
ultrahyperbolic construction.

The next gate is:

`ECW3D-B2C2B-SUPER-IG-RS-TANGENT-DIFFERENTIAL-AND-OBSERVER-DESCENT`

It must build the scalar-spinor-to-`ker Gamma` differential independently of
the Jordan image, prove its full BV closure and dynamics compatibility, and
only then test whether its cohomology removes every generalized
characteristic chain while allowing observation to descend.
