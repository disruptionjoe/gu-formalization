---
artifact_type: conditional_build_result
created: 2026-08-06
status: TT_DENSITY_ZERO__FIXED_FRAME_HODGE_LIVE__MOVING_HODGE_AND_COFRAME_FUSED__SELECTED_ACTION_COMPOSITION_OPEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
ledger: lab/process/conditional-physics-ledger-v0.26.json
machine_registry: lab/process/moving-gimmel-hodge-frame-owner.json
probe: tests/channel-swings/moving_gimmel_hodge_frame_owner_probe.py
---

# Moving gimmel, Hodge and frame owner

## Result in plain English

One piece of the first-order queue was counted twice. When the observed
four-dimensional metric moves, the ten-dimensional trace-reversed DeWitt
fibre metric moves with it. In a fixed coordinate frame this makes the
fourteen-dimensional Hodge star move. In the corresponding co-moving
orthonormal frame, however, the metric and Hodge components are stationary.
Those are two descriptions of one functorial owner packet, not two
independent coefficients in the action.

For the exact transverse-traceless perturbation tested here, the full
fourteen-dimensional density has zero first variation even though the metric
and Hodge responses are nonzero. This removes density from this local TT
subgate and fuses Hodge with frame motion. It does **not** cancel the selected
action variation: Phi, Shiab, the Krein pairing, the soldering/observation map
and the fields must all be transported through the same frame packet before
that question is answerable.

## 1. Layer 0

| phrase | object in this wave | not identified with |
|---|---|---|
| base metric | `g` on the observed Lorentz four-plane | the full gimmel metric |
| gimmel metric | `G = g + D_g` on `T*X + Sym2(T*X)` | a positive energy or PDE symmetrizer |
| Hodge motion | coefficient response of `*_G` in a fixed coordinate coframe | an independent physical field |
| frame compensation | the infinitesimal co-moving orthonormal-frame change | gauge/BV quotient or vanishing physics |
| density zero | first variation of `vol_G` along this TT direction | density zero for conformal or arbitrary motion |
| action cancellation | a statement about the complete Euler/presymplectic owner sum | proved nowhere in this wave |

This separation is load-bearing. A coordinate component can move while the
same natural tensor has constant components in a co-moving frame. That is
covariance, not deletion of the tensor or of its coupling to other moving
objects.

## 2. Source collision

The source arena is explicit:

- the UCSD/Into the Impossible transcript says the vertical ten-plane is the
  symmetric-metric fibre, and that trace reversal changes its Frobenius
  signature from `(7,3)` to `(6,4)`;
- it combines that block with the Lorentz `(1,3)` horizontal block to obtain
  the chimeric `(7,7)` metric and spinors;
- it says an observation section pulls the upstairs data back to four
  dimensions; and
- its Levi-Civita discussion distinguishes the naked distinguished connection
  from the gauge-rotated Levi-Civita comparison used in the contorsion slot.

Disposition:

- `SOURCE-CONFIRMS` the metric-bundle, trace-reversed-fibre, moving-observation
  arena;
- `SOURCE-SILENT` on the exact TT derivative, density cancellation,
  compensator and selected-action cubic.

The calculation below is repository-derived. It is not attributed to
Weinstein or Curt.

## 3. Exact local construction

At one Lorentz frame take

```text
g = diag(1,-1,-1,-1),
h = diag(0,1,-1,0),
tr(g^-1 h) = 0.
```

On the actual ten-dimensional symmetric-tensor fibre use the trace-reversed
DeWitt pairing

```text
D_g(k,l) = tr(g^-1 k g^-1 l)
           - (1/2) tr(g^-1 k) tr(g^-1 l).
```

The exact ten-by-ten Gram matrix has determinant `64` and inertia `(6,4)`.
Together with the base `(1,3)` block,

```text
G = diag(g,D_g)
```

has exact inertia `(7,7)`. This checks Curt/Weinstein's stated reason for
`(7,7)` on the actual `Sym2` fibre; it does not merely add dimensions.

Differentiate `g^-1` by

```text
delta(g^-1) = -g^-1 h g^-1
```

and differentiate both inverse metrics in `D_g`. Calling the resulting total
metric derivative `H` and `K=G^-1 H`, the exact rational result is

```text
rank(H) = rank(K) = 8,
tr_horizontal(K) = 0,
tr_vertical(K) = 0,
tr_total(K) = 0.
```

Therefore

```text
delta vol_G = (1/2) tr(K) vol_G = 0
```

for this TT direction.

## 4. Hodge is live in a fixed frame

Zero density response does not freeze the Hodge star. For a fixed coordinate
one-form, the inverse-metric derivative is nonzero; in the executable witness
one spatial covector has norm derivative `-1`. Since the volume derivative is
zero while the form inner product moves, the defining wedge identity for
`*_G` forces a nonzero fixed-frame Hodge derivative.

The control matters: with the conformal perturbation `h=g`, the exact traces
are

```text
horizontal trace = 4,
vertical trace = -20,
delta vol_G / vol_G = -8.
```

So density zero is TT-specific, not a matcher that labels every motion zero.

An independent Sage 10.9 rational-quadratic-form route reconstructed the
ten-by-ten and fourteen-by-fourteen matrices from the definition and returned
`det(D_g)=64`, signature differences `2` and `0`, `tr(K)=0`, `rank(H)=8` and
the exact compensator identity. It did not reuse the SymPy probe output.

## 5. Hodge and coframe are one owner packet

The metric endomorphism is `K=G^-1 H`. It is exactly `G`-self-adjoint. Set the
infinitesimal vector-frame change to

```text
A = -(1/2) K.
```

Then the exact fourteen-by-fourteen identity is

```text
H + A^T G + G A = 0,
tr(A) = 0.
```

Thus the metric and Hodge components are stationary in the co-moving frame.
Equivalently, their fixed-coordinate motion is carried by the induced coframe
action. The queue must not price “moving Hodge” and “moving frame/coframe” as
two free action owners.

This is only an owner fusion. Phi, Shiab, the Krein primalizer, fields,
gauge-rotated Levi-Civita distortion and observation/soldering data also carry
frame indices or metric dependence. Their induced variations may reinforce or
cancel; none was guessed here.

## 6. Symplectic and variational fence

The symplectic lens rejects a tempting overread. A co-moving frame is a local
change of variables. It does not erase the presymplectic potential, a boundary
flux or a BFV class. The full variational bicomplex must transport the fields
and the potential along with the coefficient tensors. Likewise, pointwise
inertia `(7,7)` is not a positive symmetrizer and supplies no global
hyperbolic domain.

## 7. Ledger v0.26

```text
Ledger v0.26 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Verdicts, reason kinds, residue, quotients and P1/P2/P3 do not move. Five row
distances migrate to name one fused moving-gimmel/frame packet instead of
independent Hodge and coframe burdens.

## 8. Next gate

Compose the selected first-order action and observation map with **one** fused
moving packet containing:

```text
metric + DeWitt + Hodge + coframe + Phi + Shiab + Krein +
gauge-rotated Levi-Civita/soldering + fields.
```

The TT density subowner is zero at the tested local frame. The surviving test
is whether the complete transported Euler and presymplectic owners close,
followed by diffeomorphism/odd BV, global domain and unrestricted BFV. The
separate rank-two `I2B <-> ||II||^2` owner map is unchanged.

## 9. Claim boundary

No stationarity, action cancellation, Einstein equation, positivity,
hyperbolicity, global domain, BV/BFV quotient, cosmological prediction,
chirality, mass, index or generation count is claimed. Curt remains formally
separate; no third lane is promoted; P1/P2/P3 are unused.
