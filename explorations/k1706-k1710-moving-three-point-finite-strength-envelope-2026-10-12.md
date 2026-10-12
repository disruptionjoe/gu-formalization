---
title: "K1706--K1710 moving three-point finite-strength envelope"
status: active_research
document_role: exploration
claim_verdict: proved_for_complete_negative_kurtosis_symmetric_three_point_family_at_weak_reward
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-12"
---

# K1706--K1710: the cubic equality seed moves at finite strength

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
  carrier: symmetric_three_point_scalar_seeds_on_real_cardinal_packet_coordinates
  pairing_or_form: relative_fisher_form_plus_matched_negative_fourth_cumulant_defect
  real_structure: real_scalar_gaussian_interpolation_and_conjugation_symmetric_mode_blocks
  grading: hermite_interpolation_order_then_scalar_legendre_and_packet_variational_order
  action_owner: repository_trial_functional_not_source_owned
  target_object: complete_three_point_weak_reward_scalar_and_rectangular_packet_upper_envelope
  observed_intertwiner: UNTYPED
```

## Result and boundary

K1702's law is the unique cubic equality seed in the negative-kurtosis
symmetric three-point family, but it is not the exact finite-strength seed.
Writing `q=-kappa_4t^2`, the first omitted Hermite term is linear in
`kappa_6` at order `q^(7/2)`. The exact minimizing atom probability therefore
moves according to

```text
p(q)=p_*+beta sqrt(q)+O(q),
beta=(35/3)u_*^(3/2)/kappa_6'(p_*)>0.                (1)
```

After this motion the matched-defect law is

```text
j_3pt(q)=q^2/6+q^3/4+D_*q^4+O(q^(9/2)),
D_*=1009/1512+(5sqrt(105))/168
   =0.9722968151... .                                  (2)
```

Holding the K1702 seed fixed instead gives
`d_*=227/126+(5sqrt(105))/168`; optimizing `p` lowers that coefficient by
exactly `245/216`. The complete negative-kurtosis three-point family has one
global small-reward branch, so seeds with `p -> 1/3` and vanishing fourth
defect do not escape this theorem. The corresponding Legendre profile is
lower than the fixed-`p_*` profile by `(735/8)r^4+o(r^4)`, and every fixed
nondegenerate K1683 packet gains
`5880g^4ell_g(C)^4/tau_g(C)^3+o(g^4)`. Compact shape control gives a strict
order-`g^4` gain after rectangular optimization, though this Run does not
identify its exact global quartic shape coefficient.

This is not the exact finite-strength infimum over all bounded symmetric
seeds. Growing support, general vanishing-defect families, nonrectangular
packets, correlated cumulant tensors, translation-Haar saving, arbitrary
stationary lower control and the physical action/domain/state/observation
tuple remain open.

## Preflight bookend and route choice

The frontier compared the next Hermite order, the complete three-point
vanishing-defect boundary, quantitative translation-Haar saving, correlated
tensors, nonrectangular packets and an unrestricted lower bound. The Hermite
route won because it directly tests whether the newly proved cubic equality
seed persists at finite strength and because the same calculation controls a
complete compact seed family. Haar saving still lacks a cutoff-uniform
posterior-score estimate; the tensor and lower-bound routes lack a transfer
principle from the scalar product class.

The probability lens supplied the exact Gaussian-interpolation density ratio.
The algebra lens reduced every coefficient to Gaussian Hermite contractions.
The singular-perturbation lens recognized that the optimizer moves on the
`sqrt(q)` rather than `q` scale. The variational lens transferred the result
through the Legendre profile and packet functional. The hostile lens preserved
all all-seed, correlated, Haar, unrestricted and physical boundaries. No
source or physics-ledger row moves.

## K1706: exact symmetric expansion through interpolation order eight

For one bounded symmetric centered unit-variance seed put

```text
kappa_4=E H_4(X),  kappa_6=E H_6(X),  h_8=E H_8(X).
```

Mehler's formula gives, in the weighted spaces needed for the score,

```text
p_t/phi=1+(kappa_4/24)t^2H_4
          +(kappa_6/720)t^3H_6
          +(h_8/40320)t^4H_8+O_X(t^5).
```

Expanding `int phi (r_t')^2/r_t` and using probabilists' Hermite
orthogonality yields

```text
j_X(t)
 = (kappa_4^2/6)t^4
 + (kappa_6^2/120-kappa_4^3/4)t^6
 - (7/36)kappa_4^2kappa_6 t^7
 + [h_8^2/5040-kappa_4kappa_6^2/12
    -kappa_4^2h_8/72+71kappa_4^4/48]t^8
 + O_X(t^9).                                           (3)
```

The load-bearing contractions are
`E[H_4H_3H_5]=1440`, `E[H_6H_3^2]=720`,
`E[H_4H_5^2]=14400`, `E[H_4H_3H_7]=5040`,
`E[H_6H_3H_5]=10800`, `E[H_8H_3^2]=0` and
`E[H_4^2H_3^2]=30672`. Equation (3), not numerical fitting, carries the next
optimizer calculation.

## K1707: the moving three-point optimizer

For the symmetric three-point law with total nonzero mass `p`,

```text
u(p)=3-p^(-1),
kappa_6(p)=p^(-2)-15p^(-1)+30,
h_8(p)=p^(-3)-28p^(-2)+210p^(-1)-315.
```

On `p in (1/3,1]`, matched substitution in (3) has the form

```text
j_p(q)=q^2/6+c(p)q^3+e(p)q^(7/2)+d(p)q^4+O(q^(9/2)),
c(p)=1/4+kappa_6(p)^2/(120u(p)^3),
e(p)=-(7/36)kappa_6(p)/u(p)^(3/2).
```

At `p_*=(15+sqrt(105))/60`, `c'(p_*)=e(p_*)=0`, while

```text
c''(p_*)=kappa_6'(p_*)^2/(60u_*^3)>0,
e'(p_*)=-(7/36)kappa_6'(p_*)/u_*^(3/2)<0.
```

The scaled implicit equation therefore gives (1). Substitution gives

```text
D_*=d(p_*)-e'(p_*)^2/[2c''(p_*)]
   =d(p_*)-245/216,
d(p_*)=227/126+(5sqrt(105))/168,
```

which proves (2). Thus K1702 remains the unique cubic equality seed, but a
coupling-dependent three-point seed strictly beats the fixed K1702 law at the
first distinguishing quartic order.

## K1708: Legendre and packet transfer

If `j(q)=q^2/6+q^3/4+Dq^4+O(q^(9/2))`, its small-reward Legendre profile is

```text
Phi_D(r)=-(3/2)r^2+(27/4)r^3
          +(81D-2187/32)r^4+O(r^(9/2)).               (4)
```

The moving branch lowers `D` by `245/216`, so

```text
Phi_moving(r)=Phi_p*(r)-(735/8)r^4+o(r^4).            (5)
```

For the K1683 objective `F=(tau_g/4)Phi(4gell_g/tau_g)`, (5) becomes

```text
F_moving(C,g)=F_p*(C,g)
 -5880g^4ell_g(C)^4/tau_g(C)^3+o_C(g^4).              (6)
```

On the compact interior neighborhood containing all small-`g` rectangular
minimizers, the coefficient in (6) has a positive lower bound. Hence the fully
rectangularly optimized moving-three-point envelope is strictly lower than the
fixed-`p_*` envelope by at least `c_*g^4+o(g^4)` for some `c_*>0`. Shape motion
can affect the exact quartic constant, which is not claimed here.

## K1709: complete weak global branch in the three-point family

The closed parameter interval `p in [1/3,1]` has uniformly bounded support.
For every fixed `t>0`, its Gaussian convolution has positive relative Fisher,
including the zero-defect endpoint `p=1/3`; as `t -> 1`, discrete component
separation prevents a remote minimizer. Thus every global minimizing sequence
for reward `r -> 0` has `t -> 0`.

The uniform expansion in `(p,t)` then resolves the remaining boundaries. If
`u(p)` tends to zero, the positive term
`kappa_6(p)^2t^6/120`, with `kappa_6(1/3)=-6`, makes the first correction larger
than the fixed interior branch; if `p` stays away from `p_*`, K1702's strict
cubic square makes the branch larger at order `r^3`. Therefore every global
minimizer converges to `p_*`. The scaled Hessian from K1707 is positive and
gives one local branch, which is consequently the unique global branch for all
sufficiently small positive reward. This closes vanishing fourth defect only
inside the complete symmetric three-point family.

## K1710: protected integration and next frontier

The bridge census becomes 425 rows: 346 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains
`UNCERTAIN`; the standing physics ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger,
canon, paper, prediction, confirmation or public verdict moves.

The next scalar question is whether the moving three-point branch remains
optimal at nonperturbative strength or against wider bounded and
coupling-dependent seed families. Independent coefficient routes remain the
translation-Haar saving scale, a correlated fourth-cumulant tensor, a
nonrectangular packet and an arbitrary-stationary lower bound.

## Postflight hostile review

- **Strongest overclaim:** global means the complete negative-kurtosis
  symmetric three-point family at sufficiently small reward, not every scalar
  seed or finite coupling.
- **Strongest contrary route:** a four-or-more-point law, growing support,
  nonproduct cumulant tensor or Haar score cancellation can still lower the
  trial envelope.
- **Weakest analytic seam:** the boundary exclusion uses uniform bounded
  support and the nonzero sixth Hermite coefficient at `p=1/3`; it does not
  transfer to general vanishing-defect seed families.
- **Weakest variational seam:** (6) proves a strict order-`g^4` optimized gap,
  not the exact global quartic shape coefficient.
- **Weakest physical seam:** this is covariance-matched trial mathematics and
  supplies no source-owned Hamiltonian, physical quotient, state, prediction
  or confirmation.

The Hermite contractions, singular optimizer scale, boundary comparison and
Legendre composition—not the executable controls—carry K1706--K1709.
