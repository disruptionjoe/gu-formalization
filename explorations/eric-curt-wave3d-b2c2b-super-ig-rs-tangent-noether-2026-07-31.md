---
title: "Eric/Curt Wave 3D-B2C2B: the unique natural RS tangent fails off-shell Noether and unchanged-observer descent"
status: active_research
doc_type: construction_result
created: 2026-07-31
lane: "1"
work_item: ECW3D-B2C2B-SUPER-IG-RS-TANGENT-DIFFERENTIAL-AND-OBSERVER-DESCENT
registry: lab/process/eric-curt-wave3d-b2c2b-super-ig-rs-tangent-noether.json
probe: tests/channel-swings/eric_curt_wave3d_b2c2b_super_ig_rs_tangent_noether_probe.py
grade: "DECISIVE BOUNDED NEGATIVE in the parity-neutral metric/Clifford-only first-order class. Gamma-tracelessness leaves one projective scalar-spinor-to-RS symbol, the twistor map T(k)=Pi_kerGamma(k tensor 1). Its W131 composition is Q(k)T(k)=(12/14)T(k)c(k), so it is not an off-shell Noether/BV differential; on a null covector only a rank-64 parameter half is characteristic-exact. The unchanged observer sees rank 128 on the full image and rank 64 on that half. An enlarged mixed-carrier super-IG action, representation, and Ward/master identity remain open."
claim_status_change: false
canon_change: false
public_posture_change: false
---

# Wave 3D-B2C2B — natural super-IG/RS tangent and Noether gate

## Result

The still-open guided gate now has a precise bounded negative.

Freeze the parity-neutral local first-order class using only the admitted
covector `k`, metric, Clifford multiplication, and gamma trace. Before looking
at the W131 Jordan or observer targets, any such scalar-spinor-to-vector-spinor
symbol lies in the span

\[
K(k)=k\otimes 1,
\qquad
\Gamma^\dagger c(k).
\]

Because

\[
\Gamma K(k)=c(k),
\qquad
\Gamma\Gamma^\dagger=14\,1,
\]

gamma-tracelessness has rank one on the two coefficients. It leaves the unique
projective member

\[
\boxed{
T(k)=\Pi_{\ker\Gamma}K(k)
=K(k)-\frac1{14}\Gamma^\dagger c(k).
}
\tag{1}
\]

No background spinor, soldering map, Jordan projector, spectral projector,
P1/P2/P3 datum, or fitted target coefficient enters this freeze.

Collision with the compressed W131 symbol `Q(k)` gives the exact identity

\[
\boxed{
Q(k)T(k)=\frac{12}{14}T(k)c(k).
}
\tag{2}
\]

For a non-null covector both `T(k)` and `Q(k)T(k)` have complex rank 128.
Therefore the only nonzero natural member fails the off-shell Noether identity

\[
Q(k)T(k)=0
\quad\text{for every }k.
\]

This closes the frozen class. It does not close enlarged actions.

## Characteristic exactness is strictly weaker

For the tested null covector `k=e_y+e_t`,

\[
c(k)^2=0,
\qquad
\operatorname{rank}c(k)=64.
\]

The full natural map still has rank 128 and its W131 composition has rank 64.
Only the parameter half

\[
T(k)\ker c(k)
\]

is characteristic-exact, with rank 64.

That half is not a source-selected ghost module. It depends on the
characteristic covector and is obtained by restricting parameters after the
symbol is known. Promoting it to an off-shell BV differential would repeat the
same characteristic-versus-Noether collapse that B2C1 prohibited.

## Why the conditional mixed super-IG bracket does not fill the gap

The strongest existing conditional algebraic predecessor uses

\[
Q_{\rm mix}=S\oplus(T^*Y\otimes S)
\]

and

\[
\beta((u,\psi),(v,\chi))(X)
=\mu_\Omega(u,\chi(X))+\mu_\Omega(v,\psi(X)).
\]

That bracket is valuable: it is symmetric, tensorial, and
full-complex-symplectic equivariant at the stated reconstruction scope. But its
target is an adjoint-valued connection one-form,

\[
\Omega^1(\mathfrak{sp}(S_\mathbb C)),
\]

not `ker Gamma`. A bracket on an odd module is also not yet a representation
of the superalgebra on the rolled physical fields.

Four missing objects remain distinct:

1. a source-fixed odd parameter/ghost module rather than reusing physical
   `nu` and `zeta`;
2. a native real-form projection and action on the full rolled carrier;
3. a scalar-spinor-to-RS transformation law; and
4. an off-shell Ward/master identity whose cancellations may use the enlarged
   coupled equations.

Equation (2) shows that the minimal natural RS leg cannot supply item 4 by
itself.

## Observation does not descend unchanged

The admitted section observation selects the `y,x,z,t` one-form components.
On `k=e_y+e_t`, the executable gate finds

\[
\operatorname{rank}(O\,T(k))=128,
\]

and on the characteristic-exact half,

\[
\operatorname{rank}\bigl(O\,T(k)|_{\ker c(k)}\bigr)=64.
\]

Thus the unchanged observation map does not annihilate either proposed gauge
image. A future physical quotient must derive both the bulk image and any
observed-side quotient from one action/Ward/BFV system. Quotienting the
observed rank merely to make descent hold is not admitted.

Right-`H` invariance of the natural image passes exactly. It does not repair
the Noether or observation failure; compatibility is not selection.

## Source collision

Leading disposition: `SOURCE-SILENT` at the decisive tangent/Noether scope.

The local sources do confirm the construction context:

- the Portal transcript at `01:30:19` and `02:23:52` describes a fermionic
  extension of the inhomogeneous gauge group and the zero-form plus one-form
  spinor carrier;
- the UCSD transcript at `00:49:16--00:50:09` again names the super-extension
  and the zero/one-form adjoint-or-spinor field content; and
- the 40-years transcript at `01:38:35--01:44:14` says fractional-spin fields
  should pair into the group Lie algebra/gauge-potential sector and associates
  the construction with good characteristics.

Those passages do not supply an odd parameter module, transformation law on
the rolled fields, W131 tangent map, native `(9,5)` real-form action, or
Noether/Ward/BV identity. The last passage explicitly declines to supply an
action at that point. Source speech fixes attribution and scope; it is not
mathematical evidence for equation (1), equation (2), or the negative result.

## Layer 0 dictionary

| shared phrase | object here | must not be identified with |
| --- | --- | --- |
| physical zero-form | `nu in Omega0(S)` at ghost number zero | parity-shifted scalar-spinor ghost |
| physical one-form | `zeta in Omega1(S)` at ghost number zero | RS gauge field without a derived representation |
| mixed super-IG bracket | bilinear into connection translations | linear `S -> ker Gamma` tangent rule |
| natural twistor symbol | unique metric/Clifford first-order candidate | source-derived Noether map |
| characteristic half | `T(k) ker c(k)` for null `k` | off-shell ghost image |
| right-`H` compatibility | invariant quaternionic image | action or Ward identity |
| observer descent | observation kills/quotients the derived image | post hoc deletion of observed modes |
| generation | observed chiral/index object | coefficient count, rank, or Dirac kernel |

## Seven-axis read

| axis | result |
| --- | --- |
| L1 algebra | two raw natural coefficients, one gamma-trace constraint, one projective twistor symbol; exact W131 intertwiner |
| L2 representation | active `Cl(9,5)` and right-`H` exact; conditional mixed bracket remains adjoint-one-form valued |
| L3 geometry | active trace-reversed `(9,5)` section only; Curt's literal `(7,7)` port remains open |
| L4 dynamics | off-shell Noether fails in the frozen class; enlarged action/Ward cancellation open |
| L5 observation | unchanged observation sees ranks 128 and 64 on the candidate images |
| L6 physics | physical `nu` is not retyped as a ghost; no physical quotient is promoted |
| L7 empirical | no prediction, fit, mass, index, generation count, or SM recovery claimed |

The constraint-surplus count is honest. There are two raw coefficients, one
gamma-trace condition, and one irrelevant projective normalization. No target
parameter was fitted. The unique candidate then fails the off-shell condition,
leaving zero survivors in this class.

## Non-regression, datum, and rival boundary

- B2C1's failure of the prior projected quotient is retained.
- B2C2A's ordinary adjoint tau/BRST carrier mismatch is retained.
- The conditional mixed super-IG bracket is retained as an algebra candidate,
  not promoted to a field action.
- P1/P2/P3 remain unused and unchanged; none supplies the missing
  representation or Ward identity.
- Curt remains a formally separate `(7,7)` rival inside the Eric lane.
- `TG-1 AND TG-2 AND TG-3` remains false. No third lane is promoted.
- Claim status, canon, public posture, Lane control, scheduler state, and
  publication state do not change.

The executable probe passes `19 exact + 12 planted = 31` checks.

## Next gate

`ECW3D-B2C2C-MIXED-CARRIER-SUPER-IG-ACTION-REPRESENTATION-AND-WARD-IDENTITY`

Do not search another scalar multiple of the twistor symbol. Instead:

1. freeze whether the source-stated physical mixed carrier is also the odd
   parameter module or whether a distinct parity-shifted copy is required;
2. project the conditional complex-symplectic bracket to the active native
   real form without identifying full `Sp` covariance with frozen Clifford
   covariance;
3. construct the super-IG action on every rolled field and equation block,
   including any extra field needed for off-shell cancellation;
4. derive the Ward/master identity before looking at the W131 Jordan image;
   and
5. only if the identity closes, compute physical cohomology and derive the
   observer-side quotient from the same BFV boundary data.

If that enlarged action cannot be built from source-authorized ingredients,
the guided gauge-quotient route should close at its exact bounded scope while
the separate B2C4 Shiab-family/source-constraint alternative remains open.
