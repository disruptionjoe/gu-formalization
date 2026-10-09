---
title: "Critical Gaussian capacity and an atom-free Sobolev holonomy class"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__CRITICAL_CAPACITY_METHOD_BOUNDARY_AND_L2_HOLONOMY_SUFFICIENCY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Critical Gaussian capacity and an atom-free Sobolev holonomy class

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional harmonic spectral model.
> It is not a source-native GU action, physical state space, observed carrier,
> prediction, confirmation, or falsification of a registered source claim.
> Conventional comparator conclusions bind only the models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: profiled_gaussian_uv_shell_channels_plus_compact_absolutely_continuous_spectral_primitives
  pairing_or_form: weighted_relative_fisher_mmse_pairing_plus_fourier_plancherel_pairing
  real_structure: real_finite_q_space_and_real_finite_dimensional_spectral_values
  grading: ultraviolet_shell_channel_plus_low_high_time_split
  action_owner: repository_control_not_source_owned
  target_object: critical_information_method_boundary_and_atom_free_holonomy_l1_sufficiency
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1622 leaves an exact scale question: is its `o(N^3)` information hypothesis
merely convenient, or does order-`N^3` capacity really permit an order-`N^4`
missing-Fisher term? An exact product Gaussian channel on a fixed-ratio
ultraviolet shell answers this for the method. The information and posterior
MMSE both tensorize, so no packing estimate or asymptotic approximation is
needed.

The independent spectral arc supplies the positive complement to K1624.
Atom-freedom alone remains insufficient, but absolute continuity with an `L2`
derivative density gives precisely the weighted Fourier integrability needed
after one distributional integration by parts.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
LT-SM8, LT-GR6b, RA-F1 and AC-F1 do not move. No source, ledger, canon,
paper, prediction, confirmation, or public-posture state moves.

## K1626 — exact critical-capacity shell channel

Let `E_N` be a fixed-ratio ultraviolet shell with `d_N=Theta(N^3)` real
cutoff coordinates. On that shell let the common K1572 profile-band covariance
be diagonal with entries `s_(N,k)` bounded above and below by positive constants,
and let the free frequencies obey `omega_(N,k)=Theta(N)`. Fix `r>0` and set

```text
C_(N,k)=r s_(N,k),
M_(N,k)~N(0,C_(N,k)),
G_(N,k)~N(0,s_(N,k)),
X_N=M_N+G_N.                                                   (1)
```

All coordinates are independent. This is K1621's common-floor channel with a
single continuous Gaussian latent location and relative excess `rI` on the
shell. The exact scalar Gaussian formulas tensorize:

```text
I(M_N;X_N)=(d_N/2) log(1+r)=Theta(N^3),                        (2)
mmse(M_(N,k)|X_(N,k))=s_(N,k) r/(1+r).                        (3)
```

The weighted missing relative Fisher information is therefore

```text
Delta_N=sum_(k in E_N) omega_(N,k)
        mmse(M_(N,k)|X_(N,k))/s_(N,k)^2
       =[r/(1+r)]sum_(k in E_N) omega_(N,k)/s_(N,k)
       =Theta(N^4).                                            (4)
```

The one-quarter energy normalization used in K1606 makes the corresponding
mixing term `Delta_N/4=Theta(N^4)`. Thus the scales in K1616's
`Delta_N<=2 Lambda_N I(M_N;X_N)` are simultaneously attained up to constants.

## K1627 — what the critical example does and does not decide

K1626 proves sharpness of the information-control route at the leading energy
scale. A hypothesis allowing `I(M_N;X_N)=Theta(N^3)` cannot, by itself, turn
K1616's remainder into `o(N^4)`. Critical capacity requires an additional
cancellation, a sharper averaged frequency estimate, component coercivity, or
direct coefficient analysis.

This is not an actual coefficient-changing variational construction. The law
in (1) is itself Gaussian with covariance `S_N+C_N`; the component/translation
energy and quartic term remain present, and K1572 makes the profiled Gaussian
the stationary-diagonal minimizer. K1626 isolates a leading-order
missing-Fisher term; it does not prove that this term survives the other energy
contributions, lower the true ground energy, or identify the unrestricted
coefficient. The critical-capacity boundary is therefore classified as
**method-sharp but variationally undecided**.

## K1628 — an atom-free `L2` derivative is sufficient for holonomy `L1`

Fix the Fourier convention
`widehat f(t)=int exp(-it omega)f(omega)d omega`. Let `G` be compactly
supported, absolutely continuous, scalar or finite-dimensional vector valued,
with weak derivative `g=G' in L2`. Compact support makes `G in L1`, and
distributional integration by parts gives

```text
widehat G(t)=widehat g(t)/(it),  t != 0.                       (5)
```

For `R>0`, the low-time part is bounded by

```text
int_(|t|<=R)|widehat G(t)|dt <= 2R ||G||_1.                   (6)
```

For the tail, Cauchy--Schwarz and Plancherel give

```text
int_(|t|>R)|widehat G(t)|dt
 <= ||widehat g||_2 (int_(|t|>R)t^(-2)dt)^(1/2)
 = 2 sqrt(pi/R) ||g||_2.                                     (7)
```

Hence `widehat G in L1`. The derivative measure `DG=g d omega` is atom-free,
so this gives a broad sufficient subclass strictly on the positive side of
K1624's obstruction. It does not cover arbitrary atom-free singular measures.

## K1629 — explicit quantitative holonomy budget

Combining (6)--(7), for every `R>0`,

```text
||widehat G||_1 <= 2R||G||_1+2sqrt(pi/R)||G'||_2.              (8)
```

When both norms are nonzero, the minimizing split is

```text
R_*=[sqrt(pi)||G'||_2/(2||G||_1)]^(2/3),                     (9)
```

and

```text
||widehat G||_1
 <=3(2||G||_1)^(1/3)(sqrt(pi)||G'||_2)^(2/3).                (10)
```

The same proof holds for finite-dimensional vector values with Euclidean norm:
vector Plancherel and vector Cauchy--Schwarz replace their scalar versions.
This is an explicit conditional holonomy-amplitude budget. It does not supply
electric-field `L1`, curvature/current/radial remainders, nonlinear scattering,
a physical domain, or a source-owned spectral representation.

## K1630 — protected integration and hostile bookend

The bridge census is now 345 rows: 266 satisfied, ten conditional, 65 excluded,
and four missing. K1626--K1627 settle the critical information threshold only
as a sharp boundary of the Gaussian-channel proof method. K1628--K1629 give a
positive atom-free regularity class and an explicit holonomy budget.

Hostile review rejects interpreting the shell channel as an actual lowering of
the unrestricted coefficient, dropping the fixed-ratio shell or profile-band
hypotheses from the scaling statement, promoting atom-freedom alone to
sufficiency, or transferring the Fourier-amplitude bound to electric fields or
nonlinear GU dynamics. None is licensed.

The next quantum wake is a direct coefficient calculation with a genuine
non-Gaussian/nonstationary competitor or a global Fisher/defect coercivity
theorem that controls all energy terms, not just mixing. The next PDE wake is
deriving an absolutely continuous `L2` primitive derivative and integrable
curvature/current/radial remainder from one source-owned nonlinear action and
domain. The source-owned action/measure/Hamiltonian tuple remains separate.

## Postflight bookend

The quantum result prevents misuse of the subcritical theorem: critical
capacity can carry leading-order missing Fisher information, so coefficient
rigidity at that scale needs new structure. It also prevents the opposite
overclaim: leading missing Fisher alone is not an energy-lowering trial.

The spectral result identifies a simple positive side of the atom-free
boundary with a quantitative norm budget. Source, ledger, canon, paper,
prediction, confirmation, and public posture remain unchanged.
