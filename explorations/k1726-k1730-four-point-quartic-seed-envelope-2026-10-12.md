---
title: "K1726--K1730 sharp four-point quartic seed envelope"
status: active_research
document_role: exploration
claim_verdict: proved_for_regular_compact_bounded_symmetric_weak_reward_seed_paths
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-12"
---

# K1726--K1730: a four-point path attains the sharp regular quartic floor

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```yaml
gu-typed-objects:
  carrier: regular_compact_bounded_symmetric_scalar_seed_paths_on_real_cardinal_packet_coordinates
  pairing_or_form: relative_fisher_form_plus_matched_negative_fourth_cumulant_defect
  real_structure: real_scalar_gaussian_interpolation_and_conjugation_symmetric_mode_blocks
  grading: hermite_order_then_singular_seed_motion_legendre_and_packet_variational_order
  action_owner: repository_trial_functional_not_source_owned
  target_object: sharp_regular_path_quartic_scalar_and_rectangular_packet_upper_envelope
  observed_intertwiner: UNTYPED
```

## Result and boundary

K1706's eighth-order Fisher law has a sharp structural consequence beyond the
complete three-point family. For every regular compact uniformly bounded
symmetric unit-variance seed path, put

```text
u_q=-kappa_4(X_q) -> u_0>0,
t_q=sqrt(q/u_q),
kappa_6(X_q)/(u_q^(3/2)sqrt(q)) -> a,
h_8(X_q)/u_q^2 -> x.
```

Then

```text
j_(X_q)(t_q)=q^2/6+q^3/4+D(a,x)q^4+o(q^4),

D(a,x)
 = a^2/120-7a/36+x^2/5040-x/72+71/48
 = 11/108+(a-35/3)^2/120+(x-35)^2/5040.       (1)
```

Thus `11/108` is the exact quartic floor in this regular-path class. It is
attained: an exact symmetric two-radius four-point seed has `kappa_6=0` and
`h_8/u^2=35`, and a local normalized probability motion makes the scaled
sixth Hermite coefficient tend to `35/3`.

The moving three-point coefficient from K1707 is therefore not wider-class
optimal:

```text
D_3=1009/1512+5sqrt(105)/168,
D_4=11/108,
D_3-D_4=5(sqrt(105)+19)/168>0.                  (2)
```

The result is weak-reward scalar trial mathematics. It does not identify the
exact nonperturbative all-seed infimum, control support growing with reward,
cover vanishing negative defect, quantify translation-Haar saving, treat
correlated field laws, prove an unrestricted lower coefficient, or supply a
source-owned action, domain, state, quotient, observation, prediction or
confirmation.

## Preflight bookend and route choice

The compact-circle arc is now dependency-blocked at source/action selection.
The retained wider-scalar alternative became decision-grade because K1706
reduces its first open order to two scaled moment coordinates. The structural
route dominated numerical distribution search: complete the coefficient into
two squares, solve the equality moment problem exactly, and only then use
finite computation as a certificate.

The probability lens supplied the Gaussian interpolation law; the truncated
moment lens replaced a many-atom search by a two-atom law for `Y=X^2`; real
algebra isolated the unique admissible cubic root; singular perturbation
identified the `sqrt(q)` probability motion; the variational lens transported
the gap; and the hostile lens retained all finite-strength, singular-family,
correlated, unrestricted and physical boundaries. No source or physics-ledger
row moves.

## K1726: completion of squares

Substitute `t_q^2=q/u_q` into K1706. The fixed fourth-cumulant terms give
`q^2/6+q^3/4`. A sixth Hermite moment of order `sqrt(q)` contributes
`a^2q^4/120-7aq^4/36`. The base eighth-Hermite ratio contributes
`x^2q^4/5040-xq^4/72+71q^4/48`; the remaining mixed term is order `q^5`.
Compact bounded support makes K1706's remainder uniform and turns `t^9` into
`O(q^(9/2))`. Elementary completion gives (1), with equality exactly at
`a=35/3`, `x=35`.

## K1727: exact four-point equality seed

Let `u` be the unique real root in `(0,1)` of

```text
17u^3-38u^2+84u-24=0.                            (3)
```

The derivative has negative discriminant and positive leading coefficient, so
(3) is strictly increasing. Exact rational signs isolate
`3270136791/10^10<u<3270136792/10^10`.

Define

```text
S=2(6-7u)/(2-u),  R=S-(3-u),
A=(S-sqrt(S^2-4R))/2,  B=(S+sqrt(S^2-4R))/2,
p=(B-1)/(B-A).
```

The isolating interval proves `0<A<1<B` and `0<p<1`. Let `X` put probability
`p/2` at each of `+-sqrt(A)` and `(1-p)/2` at each of `+-sqrt(B)`. For
`Y=X^2`, the quadratic relation `Y^2=SY-R` and `E[Y]=1` give

```text
E[Y^2]=3-u,
E[Y^3]=15-15u,
E[Y^4]=105-210u+35u^2,
```

where the last identity is exactly (3). Hence `kappa_4=-u`, `kappa_6=0`
and `h_8=35u^2`.

## K1728: moving-path attainment

Hold `A,B` fixed, vary the lower-radius total probability `p`, and renormalize
the squared radii by `v(p)=pA+(1-p)B`. At the equality weight `p_0`,

```text
kappa_6'(p_0)=(A-B)T(u),
T(u)=2(7u^3-18u^2+84u-24)/(u-2)^2.
```

The integer resultant of the cubic in (3) and the numerator of `T` is
`589824000`, so the derivative is nonzero. Applying the implicit-function
theorem in `s=sqrt(q)` therefore produces one local path satisfying

```text
kappa_6(X_(p(q)))/u(p(q))^(3/2)=(35/3)sqrt(q).
```

Its first motion is

```text
p(q)=p_0+beta sqrt(q)+O(q),
beta=(35/3)u^(3/2)/kappa_6'(p_0)
    =-0.480253485638498... .
```

The support remains in one compact set, `u(p(q))->u>0`, and
`h_8(p(q))/u(p(q))^2->35`, so equality holds in (1). Equation (2) then
strictly excludes the moving three-point branch as the quartic optimizer over
this wider regular class.

## K1729: Legendre and packet transfer

K1708 gives `Phi_D(r)=...+81Dr^4+O(r^(9/2))`. Therefore

```text
Phi_4pt(r)=Phi_3pt(r)
 -[135(sqrt(105)+19)/56]r^4+o(r^4).              (4)
```

Using `F=(tau_g/4)Phi(4g ell_g/tau_g)` gives

```text
F_4pt(C,g)=F_3pt(C,g)
 -[1080(sqrt(105)+19)/7]
   g^4 ell_g(C)^4/tau_g(C)^3+o_C(g^4).           (5)
```

K1697's compact interior minimizer neighborhood makes the coefficient in (5)
uniformly positive, so rectangular shape optimization preserves a strict
order-`g^4` gain. Shape motion still prevents claiming the exact optimized
quartic constant.

## K1730: protected integration and next frontier

The scalar bridge census becomes 430 rows: 351 satisfied, ten conditional,
65 excluded and four missing. `SC-ACT-01/02/06` remain `ASSERTS`,
`SC-META-53` remains `UNCERTAIN`, the standing physics ledger remains
33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED, and K1145/K1150 remain
0/7. No source, ledger, canon, paper, prediction, confirmation or public
verdict moves.

The next scalar question is nonperturbative: determine the exact finite-
strength infimum or find a singular escape through growing support or
vanishing negative defect. Independent fronts remain the translation-Haar
saving scale, correlated cumulant tensors, nonrectangular packets, and an
arbitrary-stationary lower bound. The compact-circle/positive-quotient route
still requires its source/action-owned physical tuple.

## Postflight hostile review

- **Strongest overclaim:** the floor is sharp for regular compact bounded
  weak-reward paths with `u_0>0`, not for all coupling-dependent seeds or
  finite strength.
- **Strongest contrary route:** a singular path with growing support or
  vanishing defect, a correlated tensor, or Haar score cancellation can still
  lower the relevant trial or unrestricted coefficient.
- **Weakest algebraic seam:** exact attainment uses a local implicit path,
  not a closed-form global finite-strength optimizer.
- **Weakest variational seam:** (5) proves a strict optimized gap, not the
  exact shape-relaxed quartic coefficient.
- **Weakest physical seam:** this is covariance-matched scalar trial
  mathematics and supplies no source-owned Hamiltonian, domain, state,
  quotient, observable, prediction or confirmation.

The completion of squares, exact algebraic moment seed, nonzero implicit-path
tangent and Legendre composition—not the executable controls—carry
K1726--K1729.
