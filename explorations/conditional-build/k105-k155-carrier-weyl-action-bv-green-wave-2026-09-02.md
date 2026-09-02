---
title: "K105 K155-carrier Weyl action, BV and Green completion"
status: active_research
doc_type: reverse_scaffold_K155_carrier_coefficient_complete_linear_action_BV_domain_Green_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact repository-owned free linearized action on the frozen modal K155 metric-plus-distortion carrier with mixed distortion pairing and an independently action-owned rank-one Weyl same-order correction, plus an exact raw rank-nine K152 A0 fixed-gauge Noether non-admission; no ownership of raw A0, authenticated Weinstein source action, preferred historical Shiab, nonlinear or quantum BV-BFV, global curved action, physical positive state space, local net, Born law, prediction, confirmation or GU verdict
manifest: lab/process/k105-k155-carrier-weyl-action-bv-green-wave.json
probe: tests/channel-swings/k105_k155_carrier_weyl_action_bv_green_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K105 K155-carrier Weyl action, BV and Green completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this packet constructs a repository-owned free linear action on modal
copies of K155's exact metric-10 plus distortion-448 carrier. It freezes the
K155 mixed pairing and the complete rotated-null rank-one residual as an
action-owned correction. It separately tests the raw rank-nine K152 `A_0`
rather than relabeling the composite. It does not recover Weinstein's source action or the preferred
historical Shiab, and modal completion is not a curved spacetime or local net.

```gu-typed-objects
result: one free linearized action owns the K155 mixed pairing and a rank-one rotated-null Weyl same-order correction, while the raw rank-nine K152 A0 fails standalone fixed-gauge Noether admission
carrier: rapid l2 sequences of K155 metric-10 plus third-jet-closed distortion-448 fibers, with compactly supported smooth time histories LAYER=ambient CHIRALITY=N/A
pairing: Euclidean pairing on the rank-six metric gauge quotient plus the exact K155 distortion lowerer of inertia (260,188,0) ON=repository_owned_action_control
real_structure: coefficientwise real K155 packet; no Cl(9,5) identification and no complexification repair
grading: metric h, distortion T, four diffeomorphism ghosts c and their minimal antifields; no nonlinear or source BV-BFV grading
action_owner: repository-construction -- every carrier, projector, modal coefficient and rank-one Weyl correction is frozen; the distinct raw A0 remains unowned by this action
target: K155-carrier variational ownership with a K91 action/domain/Green retract tested separately MAP-TYPE=evaluation
```

## Inline preflight bookend

The work list was rebuilt after K104 rather than inherited as a conclusion.
The substantial routes were: clear K104's inertia discriminator and test both
the raw-`A_0` and same-order-correction coefficient horns directly on K155;
test the resulting K91 retract; recover a source action; jump to nonlinear
curved BV--BFV; or move forward to state/export. Only the first two were both
executable and demand-derived. K103 bars source attribution, while the frozen
linear K155 fixture cannot support a nonlinear/global promotion.

The route-changing lens census covered real quadratic actions, Krein pairings,
Sylvester inertia, diffeomorphism complexes, Noether and minimal BV closure,
finite-rank operator pencils, closed Fourier multipliers, causal fundamental
solutions, coefficient-jet provenance, null-radical leakage and physical-
polarization selection. Retrieval found no post-K155 coefficient owner and no
later correction to its ranks. Reconstructing the exact coefficient before
writing gives a rank-one `448 x 10` rational matrix with `63` nonzero entries,
digest

```text
sha256:0c4d2849aac991ade69b2418f8f2706779a662ccdcfd8252411bb729e5fd972e.
```

Positive controls retain K155's `(260,188,0)` inertia, four gauge directions,
rank-one coefficient and flat `q=0` deletion. Negative controls alter a
coefficient, erase the Weyl term, make the pairing positive, break the gauge or
nilpotence fields, or promote source/Born credit.

## Frozen carrier, gauge and Weyl coefficient

Let `M=R^10` in K152's metric-slot order and let `D=R^448` in K155's exact
third-jet-closed basis. Let `K` be the K151 distortion lowerer on `D`; it is an
involution with

```text
inertia(K)=(260,188,0).                                      (1)
```

At K155's rotated null covector

```text
n=(1,3/5,0,4/5),
```

write `G_n:R^4 -> M` for `xi -> metric_vector(n tensor xi + xi tensor n)`.
Its rank is four. The explicitly chosen Euclidean gauge projector is

```text
Q=I-G_n(G_n^T G_n)^(-1)G_n^T,       rank(Q)=6.              (2)
```

This projector is repository construction, not a source-selected gauge slice.

Rebuild K155's complete order-four restricted coefficient on its aligned
electric Weyl background `diag(q/2,q/2,-q)` and evaluate the coordinate jets at
the frozen origin. The result is linear in `q`; define

```text
C_W(q)=q C_*,                                                (3)
```

where `C_*:M->D` is the exact `q=1` composed coefficient whose sparse-entry digest is
given above. It has rank one, nine supported output rows and

```text
C_* G_n=0,        C_* Q=C_*,        C_*^T K C_*=0.           (4)
```

The last identity says its image line is `K`-null. This packet owns (3) as an
independent same-order action correction rather than borrowing it after
variation. It does not erase K155's leakage: `C_*` is the same rank-one complete coefficient
that annihilates the reference radical and leaks the rotated radical.

It is not K152's raw Weyl `A_0`. Reconstruct that object separately on the
same packet:

```text
rank(A_0^raw)=9,       nnz(A_0^raw)=24,
sha256=7967815e29bdd29f9c017936f5653fb24855b550c3b6495d298f788eaaa1b083,
rank(A_0^raw G_n)=4.                                      (5)
```

Thus the raw `A_0` alone is not an admissible cross coefficient for the fixed
gauge complex: it breaks the Noether identity. It requires a gauge-completed
full differential `A_2+A_0` owner with background-dependent gauge and lower
terms. Calling `C_*` the raw `A_0` would hide precisely this missing owner.

## Coefficient-complete action and BV complex

Let `Omega e_m=(m+1)e_m` on the sequence index. For compactly supported smooth
time histories `h in s(M)` and `T in s(D)`, set

```text
S_q(h,T)=1/2 integral_R [
  ||partial_t Qh||^2-||Omega Qh||^2
  + <partial_t T,K partial_t T>-<Omega T,K Omega T>
  - 2q <T,K C_* Qh>
] dt.                                                       (6)
```

No coefficient is implicit: the modal kinetic coefficients are one, the
mode-`m` potentials are `-(m+1)^2`, the metric slice is exactly (2), the
distortion form is exactly (1), and the only mixed coefficient is (3).

The abelian gauge action is

```text
delta_c h=G_n c,             delta_c T=0.                   (7)
```

Equations (2) and (4) make (5) gauge invariant. On the quotient
`QM direct-sum D`, use `J=diag(I_6,K)`. The field-like Euler operator is

```text
L_q=partial_t^2+Omega^2+q B,
B=[[0,C_*^T K],[C_*,0]].                                    (8)
```

The dual Hessian is symmetric and (7) is `J`-formally self-adjoint. The
Noether identity is explicit: `G_n^T E_h=0`. With four odd ghosts,

```text
s h=G_n c,       s T=0,       s c=0,                         (9)
```

so `s^2=0`, and the minimal classical action

```text
S_BV=S_q+integral_R <h*,G_n c> dt                           (10)
```

satisfies the classical master equation. This is free abelian classical BV,
not gauge-fixed quantum BV or a nonlinear source complex.

## Closed history realization and exact causal pair

Equation (4) gives

```text
B^2 != 0,                 B^3=0.                            (11)
```

Fourier transformation in time makes (7) multiplication by

```text
(Omega^2-xi^2)I+qB.                                       (12)
```

Because `B` is a bounded finite-fiber perturbation, the maximal multiplier is
closed on the free graph domain. Schwartz time functions tensored with finite
sequence modes and the finite `QM direct-sum D` fiber form a common invariant
core.

For mode frequency `omega=m+1`, put

```text
f_tau(z)=sin(tau sqrt(z))/sqrt(z),
f_tau(omega^2 I+qB)
 =f_tau(omega^2)I+q f_tau'(omega^2)B
  +(q^2/2)f_tau''(omega^2)B^2.                             (13)
```

The series stops exactly by (10). Multiplying (12) by the future or negative
past step function gives retarded and advanced kernels with opposite temporal
support and both test-space inverse identities. Their Green boundary form is

```text
beta_t(Phi,Psi)=<Phi,J partial_t Psi>-<partial_t Phi,J Psi>.(14)
```

This is a constant-coefficient modal history theorem. It is not curved-
spacetime Green hyperbolicity, microlocal spectrum, a local algebra or a
Hadamard-state result.

## What closes and what does not

K104's inertia discriminator is cleared at repository-construction grade, and
the alternative action-correction horn is constructed: the action lives on the
K155 carrier with its exact mixed pairing and owns `C_*` in its Hessian.
Gauge/Noether-BV, weighted adjoint, closed domain/core and causal Green data are
also explicit. The raw-`A_0` horn does not close: (5) is its exact fixed-gauge
Noether obstruction and reopener.

This does not select a positive physical quotient. The ambient carrier keeps
all 188 negative directions, and the exact K91 retract is a separate question.
K155's rank-one rotated-radical leakage is unchanged because the action owns,
rather than cancels, the leaking coefficient.

## Inline postflight bookend

- **Strongest overclaim:** calling (6) the recovered GU action or calling
  `C_*` K152's raw `A_0`. Refused: it is
  built backward from K91/K155 demands and uses a repository-selected gauge
  projector and modal completion.
- **Strongest contrary construction:** a nonlinear or differently gauge-fixed
  action could own the same linear coefficient while changing the global
  complex. Preserved; this packet proves only the displayed free action.
- **Weakest reproducibility seam:** finite matrices do not prove infinite
  closedness or core density. Those use bounded perturbation of the maximal
  Fourier multiplier and graph-norm cutoff; the probe certifies the exact
  carrier, coefficient, gauge and nilpotence identities.

The exact probe passes `25/25`; its baseline-first hostile selftest catches
`22/22` mutations. No source, K155 verdict, physical-state, Born, prediction,
confirmation, canon or public-posture state moves.

## Reproduction

```bash
uv run --offline --with sympy python \
  tests/channel-swings/k105_k155_carrier_weyl_action_bv_green_probe.py
uv run --offline --with sympy python \
  tests/channel-swings/k105_k155_carrier_weyl_action_bv_green_probe.py --selftest
```
