---
title: "Real-packet primary reduction and the physical-selection boundary of curved I1B"
status: active_research
claim_verdict: exact_primary_reduction_with_conditional_energy_obstruction_and_unselected_escape
doc_type: native_action_reduction_result_and_source_applicability_boundary
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-real-packet-and-selection.json
probe: tests/channel-swings/native_zorro_real_packet_probe.py
---

# Real-packet reduction and what a physical selection must change

**Subsequent calculation:** the [pure metric Hessian and acceleration
result](native-zorro-real-metric-hessian-2026-10-08.md) computes the operator
left open here and proves a conditional homogeneous Hamiltonian obstruction.
Its transported boundary/metric constraint qualification remains essential;
this earlier note's primary and selection conclusions are unchanged.

**The selected curved I1B action has a two-sided classical quadratic energy
obstruction. The real packet does not cancel it: the two packets are
independent at quadratic order. Removing the imaginary packet is a consistent
nonlinear restriction, but it is an additional selection whose physical
positivity has not been established or selected by the audited source.**

This note supplies the next actual calculation: every real-distortion
primary potential is invertible, on both stationary coupling branches.
It derives the exact formal reduction with the metric source retained.
It also separates three materially different proposed repairs: changing
what is observed, restricting ambient fields to compact coefficients, and
discarding the entire conjugation-odd packet. The first has a rigorous
energy-descent obstruction, the second fails a concrete primary-recovery
test in the explicitly tested ambient split, and the third is consistent
but has an unresolved coupled physical Hamiltonian.

The result is conditional on the action, Shiab realization, stationary
background and local patch of the
[stationary construction](native-zorro-stationary-background-2026-10-08.md).
It uses the complete mixed operator from the
[algebraic reduction](native-zorro-algebraic-reduction-2026-10-08.md)
and the compact-core theorem of the
[constrained-energy owner](native-zorro-constrained-energy-2026-10-08.md).
Classification: `SOURCE_NATIVE_ROUTE` within that reconstruction. No
conventional Yang--Mills kinetic term is substituted for its action.

```gu-typed-objects
result: exact real-distortion primary reduction, conjugation-fixed nonlinear restriction, ambient compact-recovery counterexample and section-germ energy-descent obstruction
carrier: real-grade dressed Clifford one-forms coupled to a base metric on the canonical curved metric bundle; imaginary packet retained when testing the full theory LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: source action trace/Hodge Hessian and its formal bulk adjoints; occupation-state positive adjoint used only to define the tested compact projection ON=declared_local_product_patch_and_compact_phase_core
real_structure: source anti-involution slice; coefficient-conjugation plus packet has grades 1,2,5,6,9,10,13,14 and minus packet has i times grades 0,3,4,7,8,11,12
grading: coefficient-conjugation parity, primary time kernel, Clifford parity and base derivative order; no particle count inferred
action_owner: source-action -- selected comm/symi/symi I1B functional at the certified opposite-coupling stationary backgrounds
target: primary distortion elimination and limits of proposed physical selections for SA-U1; section-germ evaluation tested separately; neither a quantum spectral theorem nor a universal GU no-go MAP-TYPE=restriction
```

## 1. A nonlinear restriction that actually is consistent

Write the source real carrier as `U=R+J`, where

```text
R = Lambda^1 + Lambda^2 + Lambda^5 + Lambda^6
    + Lambda^9 + Lambda^10 + Lambda^13 + Lambda^14,
J = i(Lambda^0 + Lambda^3 + Lambda^4 + Lambda^7
      + Lambda^8 + Lambda^11 + Lambda^12).
```

Ordinary coefficient conjugation fixes `R`, reverses `J`, and fixes the
real metric. The selected Shiab has two factors of `i` in its second
summand and otherwise real coefficients. The action is real on `U`, so

```text
I(g,R+J) = I(g,R-J).                                  (1)
```

Consequently its derivative in every `J` direction vanishes at `J=0`, for
arbitrary `g,R`. Solving the restricted `(g,R)` Euler equations therefore
solves the full bulk Euler equations with `J=0`. This is an exact nonlinear
fixed-set restriction, provided the boundary conditions also respect it.
It contains the stationary background. It does not require discarding
cubic interactions within `R`.
Here nonlinear closure refers to the selected bosonic I1B functional.
It makes no claim about additional fermionic couplings or other source
action choices.

The reverse statement is false in general. The action has `RJJ`
interactions. In the independently implemented matrix normalization,

```text
D^3 I_TTT[F_a, i e^0 gamma_0 gamma_4 gamma_10,
                 i e^1 gamma_1 gamma_4 gamma_10] = -124/3, (2)
```

where `F_a=sum_(mu!=10) e^mu gamma_mu` is the background's `a` direction.
Thus two imaginary perturbations can source a real equation nonlinearly.
The imaginary packet's closure used in the energy theorem is linearized
closure at the real background, which is sufficient for that quadratic
theorem. Equation (1) does not make either packet a positive Hilbert space.

## 2. Every real-distortion primary variable can be recovered

Keep time `x^0` and the small fibre patch where `q=dt` has positive ambient
square. Let `C_R` be the actual distortion Hessian on `R`, `E_R(q)` its
skew derivative coefficient, and `N_R` a frame for its time kernel.
The geometric kernel lemma in the energy owner restricts to `R`: the
orthogonal transport used there preserves each Clifford grade and this
packet. In particular,

```text
N_R^T E_R^A N_R = 0,
N_R^T E_R^mu nabla_mu N_R = 0,
W_R = N_R^T V_R N_R.                                  (3)
```

There is no missing derivative-of-frame term in `W_R`. The four background
Hessians and Hodge mass give

```text
W_R = kappa M_R + a H_a + c H_c + v H_v + w H_w.        (4)
```

The probe constructs the complete primary matrix in each of the forty
quartet-label classes `(n_H,n_V)`, `0<=n_H<=3`, `0<=n_V<=9`. Their
multiplicities are `binom(3,n_H) binom(9,n_V)`. Complexified stabilizer
covariance transfers invertibility to all labels; it does not transfer
real energy signs between positive and negative axes.

With `a=kappa alpha(w)`, `c=kappa beta(w)` and the already isolated
degree-ten root for `w`, every determinant is exactly nonzero in `Q(w)`.
The congruence that multiplies even kernel vectors by `kappa` and divides
the whole matrix by `kappa` removes its remaining square root. The receipt
records every reduced determinant's coefficient hash. Under the opposite
stationary coupling branch,

```text
W_R,- = -P W_R,+ P,                                   (5)
```

where `P` is Clifford parity on the kernel. Thus both branches are covered.

| Raw coordinate quantity | Real packet | Imaginary packet, predecessor |
| --- | ---: | ---: |
| One-form coefficients | 113792 | 115584 |
| Distortion time kernel | 49310 | 49154 |
| Distortion time-form rank | 64482 | 66430 |

The first row sums to `14*2^14`. These are coordinate and presymplectic
ranks, **not physical polarizations or particle counts**. In particular,
the real time-form rank does not include the metric's constraints.

## 3. The metric-coupled reduction, without freezing the metric

Choose a smooth complement `S_R` to the time kernel, with inclusion `iota`,
and write `t_R=iota s+N_R z`. Let `u(x)` be the base-metric perturbation.
All adjoints below are formal bulk adjoints on compatible compact interior
test fields. Define

```text
D = iota^dag C_R iota,       F = N_R^T C_R iota,
J_R = iota^dag A,            B = N_R^T A.               (6)
```

Here `A=A_3+A_2` is the complete mixed operator already derived; it has
only grade-one receivers. `M` is the pure-base Hessian of
`I(g,T_*(g))` in these natural field coordinates. Since `N_R^T E_R^0=0`,
`F` contains no time derivative of `s`. Equations (3)--(4) make the real
distortion primary equation exactly

```text
W_R z+F s+B u=0,
z=-W_R^-1(F s+B u).                                   (7)
```

This is a smooth algebraic recovery of `z` from the displayed jets. It is
not an inversion of the whole differential Hessian. The principal
compensator `A_3(q)u=E_R(q)y(q,u)` also gives
`N_R(q)^T A_3(q)=0`: the pure third-time-derivative coefficient in `B`
vanishes. Mixed time/spatial terms and `A_2` must still be retained.

Completing the square gives the exact formal quadratic action

```text
I_R,red^(2) = 1/2 <s,D s> + <s,J_R u> + 1/2 <u,M u>
              -1/2 <F s+B u, W_R^-1(F s+B u)>.         (8)
```

Its remaining equations are

```text
(D-F^dag W_R^-1 F)s+(J_R-F^dag W_R^-1 B)u = 0,
(J_R^dag-B^dag W_R^-1 F)s+(M-B^dag W_R^-1 B)u = 0.    (9)
```

Every adjoint ending in the base equation includes integration over the
fibre patch `V`, because `u=u(x)` has no independent fibre argument.
Boundary data must be transported through `T=T_*(g)+t` and (7). Replacing
that integral by section evaluation, treating `u` as an arbitrary
ambient field, or setting `u=0` without its equation changes the problem.

Equations (7)--(9) are the real-packet reduction achieved here. They do
**not** compute `M`, solve all coupled metric constraints, prove their
propagation, or determine the physical real-packet energy sign. Those are
computable further questions once a particular physical restriction and
domain are chosen. A frozen-metric sign scan would not answer them.
In contrast, the imaginary packet has no mixed metric term at quadratic
order. Whatever (9) eventually does, the full quadratic action still
contains its already certified indefinite direct summand.

## 4. A compact coefficient projection is not a free constraint reduction

For a concrete test, use the positive occupation-state matrix inner product
of the independent coefficient verification. The gamma matrices obey
`gamma_a^dag=eta_aa gamma_a`. A phased blade has adjoint sign

```text
(i^epsilon gamma_I)^dag
  = (-1)^(epsilon+|I|(|I|-1)/2) product_(a in I) eta_aa
      (i^epsilon gamma_I).                            (10)
```

Within the source real algebra, the minus and plus signs are its compact
and noncompact matrix directions for this chosen positive adjoint. This
is an explicitly tested ambient split. It is **not identified** with the
source's `Spin(6,4)` subgroup or its compact shielding mechanism.

The free imaginary field `i e^10 f` is compact. The vertical receiver
`i e^0 gamma_0 gamma_4 gamma_10` is also compact, while the spatial receiver
`i e^0 gamma_0 gamma_1 gamma_10` is noncompact. For a spatial `x^1` profile,
the complete primary source at the reference point is `2 partial_1 f`
on that last receiver. Its primary potential column is `-kappa` times
the unit column and all four cubic columns vanish. Hence its leading
recovered coefficient is

```text
z_noncompact = (2/kappa) partial_1 f.                  (11)
```

The source direction is not a time-kernel coordinate. Symmetry of `W`
and its isolated column prevent another primary auxiliary from canceling
this row. Lower-order curved terms cannot cancel it for arbitrary
high-frequency profiles. Thus allowing these arbitrary compact free data
while requiring every recovered coefficient to remain compact fails the
actual primary equation. A projected action that discards this equation
is a different variational problem. Additional restrictions on the free
data might work, but must themselves be specified and checked.

This is a bounded counterexample to the naive ambient compact restriction,
not a no-go for every subgroup embedding, nonlinear breaking mechanism or
physical selection. The source's narrower subgroup statement supplies no
automatic identification with this test.

## 5. Section readout and ordinary boundary conditions cannot hide the energy

Let `P` be the compact phase core of the energy theorem and let `O` depend
only on the smooth germ of the field along the observing section. This
includes bare pullback, any finite or infinite collection of section
jets, and any further compact projection or function of those data.

For either coupling branch, the negative-energy oscillatory family can be
supported in a small fibre patch disjoint from the section, while staying
inside the positive-time patch. The exact primary recovery is local, so
the entire recovered field vanishes on a neighbourhood of the section.
Consequently `O(t_n)=O(0)`, but `H(t_n)->-infinity` and `H(0)=0`.
There can be no function `h` with `H=h composed with O` on `P`.
This proof applies even to the whole smooth section germ; adding more
local jets or postcomposing a compact projection does not repair it.

Likewise, boundary conditions satisfied by every compactly supported
interior datum leave these witnesses in the phase space. Any extension
of the quadratic Hamiltonian whose domain contains this core remains
unbounded below. Boundary terms vanish on these data. This includes the
usual homogeneous local boundary conditions at this level. It does not
cover a nonlocal admissibility condition that actually excludes the core,
or a separately defined physical constraint with a proved narrower domain.

These statements concern descent of **this Hamiltonian** and this phase
core. They do not prove that no observed theory can be defined by another
source-justified construction. They show exactly why merely declaring
unobserved directions to be absent does not produce one.

## 6. The source-specific endpoint and its unresolved alternative

The audited source explicitly leaves the treatment of unbounded spectra
unresolved and suggests maximal-compact shielding: see the transcript at
[01:22:30--01:24:07](../../lab/sources/transcripts/toe-weinstein-gu-40-years.md)
and the [source-custody record](../source-uncertainty-custody-wave-2026-08-27.md).
Its source register distinguishes `SC-META-53` (`UNCERTAIN`) from the
first-order moduli/Euclidean deformation-complex claim `SC-ACT-06`
(`ASSERTS`). Neither selects `J=0`, gives
a physical map imposing it, or proves positivity of (8).

The underdetermination is concrete. Retaining the full declared phase
core has a proved two-sided energy obstruction. Restricting to `J=0`
is a distinct, interaction-consistent bulk problem that removes these
particular witnesses, but whose coupled energy is not determined by the
imaginary calculation. These two choices cannot be identified by section
readout, and the naive ambient compact restriction fails (11). The source
has not supplied a dynamical rule choosing a successful alternative.
This is a demonstrated gap in physical selection, **not** a proof that
a positive alternative exists or a claim that the remaining metric Hessian
is uncomputable.

For a candidate repair, the decisive object is a specified admissible
sector and map from the native fields, with its action and common domain.
It must exclude the exhibited negative family, satisfy the remaining
equations and interactions, define its observed quantities and Hamiltonian
consistently, and establish a conserved positive pairing and energy bounded
below on that same sector. A choice of group name alone supplies none of
these implications. A nonlinear restriction such as (1) supplies only one.

Applying the [claim-indexed doctrine](../claim-indexed-verdict-doctrine-2026-08-12.md)
and [banked-mathematics register](../nguyen-objection-banked-mathematics-register-2026-08-13.md):
Nguyen--Polya's complexification argument fails to establish a universal
GU no-go. The two-sided **classical quadratic energy obstruction is now
proved for this selected curved I1B reconstruction and core**, so the
physical energy concern is realized on this object independently of that
argument. This result strengthens the criticism at its properly bound
target; it supplies no vindication of GU positivity. No source polarity,
H59 vote, canon status or quantum spectral claim changes.

## 7. Reproduction and verification scope

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_real_packet_probe.py
```

The forty real-potential classes use the same sparse Clifford/action
engine as their predecessors and exact number-field arithmetic. The
compact-projection and `RJJ` witnesses use the separate occupation-state
implementation. This is an implementation distinction, not an independent
later research review. The nonlinear fixed-set argument, Schur reduction
and germ/boundary obstruction are analytic proofs above. The probe does
not certify a completed metric-coupled Hamiltonian or a global PDE domain.
