---
title: "Selected-K117 RSAP TT symbol-order custody and moving-Hessian gate"
status: refined_by_k118_action_layer_gate
doc_type: exact_symbol_order_correction_variable_kinetic_spectral_packet_and_full_moving_hessian_underdetermination_gate
created: "2026-08-15"
registry: lab/process/selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate.json
probe: tests/channel-swings/selected_k117_rsap_tt_symbol_order_custody_and_moving_hessian_gate_probe.py
grade: "K116 CORRECTED THE COORDINATE FRAME BUT NOT THE DIFFERENTIAL ORDER: THE INHERITED theta h^2 BLOCK IS d*z*E_hh AT A FIXED TT SYMBOL, BECAUSE IT COMES FROM a->a+beta theta IN THE EINSTEIN KINETIC COEFFICIENT. IT IS NOT A ZERO-ORDER MASS INSERTION. THE OBSERVED hh-ONLY HORN HAS K(r)=[[r,1],[1,0]], C=[[1,2/r],[0,-1]], ONE WALL r=0, AND UNIQUE K/C-COMPATIBLE CONNECTION A_*=diag(1,-1)dlog(r)/2; ITS LITERAL DIVERGENCE-FORM EULER CONNECTION IS METRIC-COMPATIBLE BUT NOT C-COMPATIBLE. THE COMPLETE Y14 MOVING HESSIAN REMAINS UNDETERMINED BECAUSE AN EXACT FULL-PENCIL FIELD-REDEFINITION COMPLETION SHARES THE SAME INHERITED hh BLOCK BUT HAS DIFFERENT h-v RESPONSE AND FIXED SPECTRUM. NO ACTION-OWNED TRANSPORT FINGERPRINT IS YET SELECTED."
target_claim: K116_CORRECTED_ZERO_ORDER_PENCIL_IS_THE_LITERAL_ACTION_DERIVED_MOVING_TT_HESSIAN_TARGET
target_verdict: NO__FIXED_SYMBOL_KINETIC_RESPONSE_WAS_RETYPED_AS_ZERO_ORDER_MASS__OBSERVED_HH_HORN_BUILT__COMPLETE_MOVING_Y14_HESSIAN_REMAINS_UNDERDETERMINED
canon_verdict_change: none
---

# Selected-K117 RSAP TT symbol-order custody and moving-Hessian gate

> **K118 ACTION-LAYER CORRECTION (2026-08-15):** K117's symbol-order result
> remains exact, but “full moving `D3 I_selected`” is not yet one typed object.
> The observed scalar horn, `I1B`, `I2B`, and observer `||II||^2` functional
> are distinct, and no stationary observed-to-native two-jet identifies their
> cubic tensors. Use K118 before attempting K117's proposed K118 assembly.

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> variational-symbol, Krein and action-Hessian question. Ordinary Higgs/VEV,
> family-index, net-chirality, anomaly, symmetry-breaking and familiar
> four-dimensional gauge-model constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K116 fixed one real error—the coordinate frames—but inherited a second one.
The recorded cubic `theta h^2` was never a momentum-independent mass term. It
was obtained by holding `theta` constant, choosing a nonzero TT symbol `z`,
and varying the Einstein coefficient `a -> a+beta theta`. Before the symbol
was frozen, the owned response was proportional to `z h^2`.

K116 dropped that `z` and inserted the result into the lower-order mass
matrix. Its one-wall algebra is correct for that hypothetical mass-deformed
pencil, but that pencil is not derived by the inherited action block.

Restoring differential order gives an exact result for the observed
`hh`-only scalar horn. It changes the kinetic form, not the mass matrix. That
horn has a simple positive spectral fundamental symmetry and a unique
connection preserving both the moving Krein form and the spectral grading.
But its literal divergence-form Euler operator induces a different
connection, which fails to preserve the grading whenever the background
moves.

The complete selected `Y14` action remains less determined than the observed
horn. An already-banked full-pencil field-redefinition completion has the same
inherited `hh` derivative and a different `h-v` response; it is isospectral
and EOM-exact on the compact free shell. The repository therefore still has
no selected action-owned moving transport fingerprint. K118 must construct
the missing full moving third derivative before another spectral owner match.

## 1. Layer-0 owner packet

```text
carrier:        real two-field observed TT fluctuation x=(h,v)
symbol:         z, the scalar TT wave symbol / differential-order marker
form:           K0=[[alpha,1],[1,0]] at the free point
lower order:    M0=[[0,0],[0,b]]
background:     theta_bar; write r=alpha+d theta_bar
real structure: ordinary real two-component field
grading:        spectral fundamental symmetry of the declared pencil
known owner:    fixed-symbol hh derivative from the observed (a+beta theta)R horn
missing owner:  full moving Y14 D3I including h-v and geometric responses
target:         distinguish kinetic, mass and field-redefinition completions
assumptions:    alpha>0, b>0; locally r>0; nonzero inherited coefficient d
controls:       z=0, moving r, field-redefinition completion, K116 mass insertion
claim ceiling:  exact observed two-field horn plus underdetermination theorem
```

The `2D` TT horn is not the conditional `98D` balanced phase/BFV carrier.

## 2. The missing symbol

The free pencil is

```text
J0(z)=z K0+M0=[[alpha z,z],[z,b]].                     (1)
```

The inherited response is stated in the earlier owner artifact as

```text
delta J_hh(z)=d z E_hh,                                (2)
```

and is explicitly described as the constant-`theta` `hh` block at a fixed TT
symbol. Equation (2) follows from replacement of the Einstein coefficient
`a -> a+beta theta`. It vanishes at `z=0`.

K116 instead used

```text
delta J_K116=u E_hh,                                   (3)
```

inside the lower-order mass block. Equation (3) does not vanish at `z=0`.
Identifying (2) and (3) would require the spacetime background parameter to
depend on the Fourier variable, `u=d theta z`, which changes its type. Thus
the K116 pencil is not the literal successor of the owned response.

## 3. Exact observed hh-only horn

For the observed scalar horn alone, absorb normalization into
`r=alpha+d theta_bar` and keep

```text
K(r)=[[r,1],[1,0]],              M0=[[0,0],[0,b]],
J_hh(z;r)=z K(r)+M0.                                  (4)
```

The normalized lower-order dynamics is

```text
L(r)=K(r)^-1 M0=[[0,b],[0,-r b]].                     (5)
```

For `r>0`, `b>0`, the positive spectral fundamental symmetry is

```text
C(r)=[[1,2/r],[0,-1]],
K(r)C(r)=[[r,1],[1,2/r]].                             (6)
```

It obeys `C^2=1`, `[C,L]=0`, `C^T K=KC`, and the majorant in (6) is positive
with determinant one. The spectral gap is `|rb|`; the single wall is `r=0`.
This is the correct constant-background spectral packet for the `hh`-only
kinetic horn. It is not yet the full selected-action packet.

## 4. Moving form: the unique K/C-compatible connection

Because `K` now moves, K111's constant-form formula `(1/2)C dC` is not the
simultaneous compatibility connection. Requiring

```text
dK=A^T K+K A,                 dC+[A,C]=0              (7)
```

fixes all four entries uniquely:

```text
A_*=(1/2) diag(1,-1) dlog(r).                         (8)
```

It is flat on the one-background family. Its parallel transport is

```text
T(r,r0)=diag(sqrt(r0/r),sqrt(r/r0)).                  (9)
```

Equation (9) has determinant one and exactly transports both `K` and `C`.
It diverges at the one wall `r=0`.

## 5. Literal observed-horn Euler operator does not own A_*

The literal `hh`-only quadratic is in divergence form,

```text
I_hh[x]=(1/2) integral (dx)^T K(r) dx -(1/2)x^T M0 x. (10)
```

After normalization by `K(r)^-1`, its first-order coefficient is

```text
B=K^-1 dK=[[0,0],[dr,0]].                             (11)
```

Equivalently `A_lit=B/2` is a metric-compatible connection. But

```text
dC+[A_lit,C] != 0,                                    (12)
B-2A_*=[[-dr/r,0],[dr,dr/r]],
det(B-2A_*)=-(dr/r)^2.                                (13)
```

For every moving background with `dr!=0`, the mismatch is rank two. No
zeroth-order term can repair a first-order coefficient mismatch. Therefore
even the literal observed `hh` horn does not own the connection that would
parallelize its instantaneous spectral sectors.

This is not a failure of the action: an operator with a moving kinetic form
need not preserve its instantaneous eigenspaces. It is a negative answer only
to the proposed transport-ownership hypothesis.

## 6. Full-action completion fork remains binding

The earlier moving-numerator gate already constructed a second completion.
Let

```text
S(t)=diag(1+d t/(2 alpha),1),
J_fr(t,z)=S(t)^T J0(z) S(t).                           (14)
```

At `t=0`,

```text
dJ_fr/dt=[[d z,d z/(2 alpha)],[d z/(2 alpha),0]].      (15)
```

Equation (15) has the same inherited `hh` entry as (2), but a nonzero `h-v`
entry. Its normalized dynamics is similar to the free dynamics, so its poles
and discriminant remain fixed. On the compact free shell it is an EOM-exact
field redefinition.

The `hh`-only completion (4) moves the massive pole to `r b`. The
field-redefinition completion (14) does not move it. The fixed-symbol `hh`
datum cannot decide between them. The selected intrinsic augmented-torsion
third derivative supplies additional exact summands, but its full moving
direct-curvature, soldering, pairing, observation, compensator and
preboundary completion is still open.

## 7. Status and reverse-scaffold correction

| prior packet | K117 status |
| --- | --- |
| first perturbative background `C` | superseded: mixed frame and wrong differential order |
| K110--K115 | structural statements only; no current action-derived concrete pencil |
| K116 | coordinate correction retained as an audit method; its mass-deformed spectral packet is hypothetical, not inherited-action-owned |
| observed `(a+beta theta)R` horn | exact `hh`-only kinetic packet (4)--(13); fails transport ownership for moving `r` |
| complete selected `Y14` action | moving Hessian and transport target underdetermined by the current owner data |

The reverse scaffold must now begin one layer earlier:

```text
R0 known datum:  fixed-symbol derivative dJ_hh=d z E_hh
R1 missing owner: full moving D3 I_selected, especially h-v response
R2 unique pencil: only after R1, construct K(theta), M(theta), C(theta)
R3 transport:    solve simultaneous form/grading compatibility
R4 owner match:  compare the literal Euler first/zero-order coefficients
R5 later gates:  stationarity, domain, BFV attachment
```

Next swings:

1. **K118 (executed):** the requested derivative is not one typed action
   object; four action layers and the observed/native scalar lift remain
   distinct.
2. **K119:** select one primitive action layer and construct a stationary
   observed-to-native two-jet.
3. **K120/K121:** compute the pullback cubic, then test spectral ownership only
   if one pencil results.
4. **K122/K123:** stationarity/domain and attachment remain last.

The correction changes no canon, ledger verdict, public posture, particle or
phenomenology claim. It retracts a reconstruction target and restores the
older moving-completion fork as the controlling dependency.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k117_rsap_tt_symbol_order_custody_and_moving_hessian_gate_probe.py
```
