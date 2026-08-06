---
artifact_type: conditional_build_result
created: 2026-08-06
status: PURE_FRAME_SELECTED_ACTION_NATURAL__PHYSICAL_SOLDERING_FIELD_OBSERVATION_DERIVATIVE_OPEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
ledger: lab/process/conditional-physics-ledger-v0.27.json
machine_registry: lab/process/selected-action-comoving-frame-naturality.json
probe: tests/channel-swings/selected_action_comoving_frame_naturality_probe.py
---

# Selected action in the co-moving gimmel frame

## Result in plain English

The previous wave showed that moving the metric and moving the frame are two
descriptions of one local owner. This wave carried that result through the
actual fourteen-dimensional Hodge star, the low-grade Phi tensors and the
Clifford scalar pairing used by the selected action.

The complete **pure-frame** response cancels exactly. This is real progress:
Hodge, Phi, the low-grade Clifford pairing and the frame Jacobian no longer
sit on the first-order queue as independent action terms. It is not the
physical action result. The gauge-rotated Levi-Civita/soldering field changes
relative to the frame, and the observation map changes which upstairs field
is read downstairs. Those derivatives remain the load-bearing owner.

## 1. Layer 0

| phrase | object computed | not identified with |
|---|---|---|
| pure frame transport | infinitesimal isometry between the varying gimmel fibres | a physical metric or matter perturbation |
| Hodge naturality | transformation of `*_G` under that isometry | `dot(*)=0` in fixed coordinates |
| Phi naturality | transport of the repository's tautological low-grade `Phi1` and derived `Phi2` | source derivation of the historical Shiab selector |
| Clifford scalar pairing | algebraic grade-one/two pairing transported with `G` | a positive Hilbert metric or global Krein domain |
| selected-action derivative | derivative caused only by co-moving-frame transport | the full Euler derivative through soldering, fields and observation |
| frame quotient | no quotient; merely a change of local trivialization | BRST/BV/BFV reduction |

The last separation is decisive. A natural scalar cannot depend on which
orthonormal frame writes its components. It can still respond to a physical
field that moves relative to that frame.

## 2. Source collision

Weinstein's released material confirms the arena: the gimmel metric and
observation section move; the displayed low-grade Phi forms move by the
epsilon/adjoint orbit; Shiab is intended to be equivariant; and the
gauge-rotated Levi-Civita connection occupies the contorsion comparison slot.

It does not publish the GL co-moving-frame calculation below or the selected
action's complete physical derivative. Disposition:

- `SOURCE-CONFIRMS` the moving metric/Phi/Shiab/connection arena;
- `SOURCE-SILENT` on exact frame naturality and the full Euler/presymplectic
  composition;
- the theorem and selected low-grade realization are repository-derived.

## 3. Exact Hodge calculation on the actual gimmel metric

Retain the predecessor's exact local gimmel metric `G`, its TT derivative `H`
and

```text
K = G^-1 H,
A = -(1/2)K,
H + A^T G + G A = 0,
tr(A)=0.
```

For each degree `p`, the probe constructs `*_G` directly from the compound
matrix of `G^-1` and the volume `sqrt(|det G|)=8`; it does not assume a
diagonal Euclidean star. It differentiates every minor exactly.

If `rho_p` is the infinitesimal exterior representation and `X=A^T` is the
pullback generator, naturality requires

```text
dot(*) = * rho_p(X) - rho_(14-p)(X) * .
```

This identity passes coefficientwise for `p=1` and `p=2`, on matrices of
sizes `14` and `91`. In both degrees `dot(*)` has nonzero rank in the fixed
frame. Freezing Hodge therefore produces a planted nonzero defect; the
cancellation is not vacuous.

## 4. Phi and the Clifford scalar pairing

In the selected exact low-grade realization,

```text
Phi1 = sum_i e^i tensor gamma(e_i)
```

is the tautological identity. The two slot responses cancel:

```text
dot(Phi1)_frame = -A Phi1 + Phi1 A = 0.
```

Freezing either slot leaves the rank-eight `A` response. Since
`Phi2=(1/2)Phi1 wedge Phi1`, its pure-frame derivative also vanishes by the
derivation rule.

The grade-one and grade-two Clifford scalar pairings were checked separately.
Writing `G^[p]` for the compound metric,

```text
dot(G^[p]) + rho_p(A)^T G^[p] + G^[p] rho_p(A) = 0
```

holds exactly for `p=1,2`. Freezing the pairing makes both controls fail. This
closes the algebraic low-grade pairing owner, not the physical Krein
fundamental symmetry, common domain or interacting positivity problem.

## 5. Selected action composition

The selected branch remains `comm/symi/symi`. An exact sparse field witness
gives the nonzero intrinsic action value

```text
I_selected(T) = -7/2.
```

Thus the subsequent zero is not the action evaluated on zero. With Hodge,
Phi, Clifford scalar pairing, field components and top form all transported
by the same infinitesimal isometry, the pure-frame derivative is exactly zero.
The TT top-form Jacobian contributes `tr(A)=0`.

This removes only coordinate/trivialization motion. The physical derivative
has the schematic remaining form

```text
D I_selected [
  delta_LC/soldering T,
  delta_observation T,
  delta_fields relative to the co-moving frame
].
```

The earlier exact gauge-rotated Levi-Civita first jet and observation first
jet are inputs for the next gate; they were not silently set to frame motion.

## 6. Symplectic and PDE fence

The symplectic lens rejects “the action variation cancels.” A local frame
change is neither the presymplectic characteristic quotient nor a boundary
reduction. The full physical potential and flux must be varied with the
soldering/field/observation response. Likewise, pointwise naturality supplies
no positive energy, Green domain or hyperbolic evolution theorem.

## 7. Ledger v0.27

```text
Ledger v0.27 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances migrate. Verdicts, reason kinds, residue, quotients and
P1/P2/P3 do not change.

## 8. Next gate

Insert the already-exact gauge-rotated Levi-Civita/soldering and observation
jets into this co-moving selected-action packet. Compute the resulting Euler
and presymplectic class without reintroducing Hodge/Phi/frame as independent
owners. Then add diffeomorphism/odd BV, global domain and unrestricted BFV/Q1.

The separate second-layer `I2B <-> ||II||^2` owner map remains rank two.

## 9. Claim boundary

No full action cancellation, stationarity, Einstein equation, cosmological
prediction, positive state space, global domain, BV/BFV quotient, mass, index,
chirality or generation count is claimed. Curt remains formally separate; no
third lane is promoted; P1/P2/P3 are unused.
