---
title: "Separated Gaussian mixtures and spectral-primitive holonomy budgets"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__SEPARATED_MIXTURE_RIGIDITY_AND_PRIMITIVE_HOLONOMY_BUDGET
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Separated Gaussian mixtures and spectral-primitive holonomy budgets

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional spectral model for the
> harmonic gauge sector. It is not a source-native GU action, physical state
> space, observed carrier, prediction, confirmation, or falsification of a
> registered source claim. Conventional comparator conclusions bind only the
> models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: fixed_finite_heterogeneous_gaussian_mixtures_plus_harmonic_spectral_primitive
  pairing_or_form: weighted_relative_fisher_form_quartic_schrodinger_form_and_background_adapted_charge_energy
  real_structure: real_finite_q_space_with_real_flat_harmonic_connection
  grading: gaussian_component_label_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: posterior_score_missing_information_and_decaying_holonomy_remainder
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1601 locates the full gap between the component-average Fisher information
and the moment-extremal lower bound, but that precision-Jensen sandwich can
have order `N^4` width under order-one covariance heterogeneity. The cheapest
next discriminator is not another moment inequality. For a finite mixture the
component label is a latent variable, and the exact loss in Fisher convexity
is its posterior score variance. This gives an identity before any Gaussian
specialization. Gaussian Hellinger overlap then controls the missing
information directly.

The decisive order-one class is a fixed finite family of centered stationary
diagonal Gaussian components. Every distinct pair differs by a fixed relative
factor on a positive fraction of cutoff modes. Their laws become
exponentially distinguishable in the `Theta(N^3)`-dimensional cutoff space, so
the mixture's only possible gain over the component average is exponentially
small even though the covariances remain an order-one distance apart. This
crosses K1602's shrinking-band restriction for a genuine but separated class.
It does not control overlapping order-one components or a component count
growing quickly enough to offset the overlap decay.

The independent PDE route asks what K1598 and K1573 actually spend. Their
adapted normal form spends the holonomy amplitude, not the time `L1` norm of
the electric field. It is therefore wasteful to impose K1603's three
derivatives on the electric spectral density merely to prove `E_h in L1`.
Dividing by frequency first and integrating the primitive density twice gives
an integrable `t^-2` holonomy remainder. A constant asymptotic flat holonomy
is absorbed into the K1579 background energy rather than forced to vanish.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
No source, ledger, canon, paper, prediction, confirmation, or public-posture
state moves.

## K1606 — exact missing Fisher information

Let `mu=N(0,I)`. For `1<=i<=M`, let `nu_i=f_i mu` have finite weighted
relative Fisher information, put

```text
nu=sum_i p_i nu_i,  f=sum_i p_i f_i,
u_i=grad log f_i,   w_i(x)=p_i f_i(x)/f(x).                     (1)
```

The mixture score is the posterior score mean:

```text
u=grad log f=sum_i w_i u_i.                                    (2)
```

Writing `|v|_Omega^2=v^T Omega v`, conditional variance gives the exact
identity

```text
U-I_Omega(nu|mu)
 =E_nu sum_i w_i|u_i-u|_Omega^2
 =(1/2)sum_(i,j)E_nu[w_iw_j|u_i-u_j|_Omega^2],                 (3)

U=sum_i p_i I_Omega(nu_i|mu).                                  (4)
```

Equation (3) is the precise missing information hidden by Fisher convexity.
It vanishes when the component score is determined by the observed point and
is large only where distinct component scores overlap under uncertain
posterior labels.

Since

```text
f>=p_i f_i+p_j f_j>=2 sqrt(p_i p_j f_i f_j),                   (5)
```

each unordered pair obeys

```text
U-I_Omega(nu|mu)
 <=(1/2)sum_(i<j)sqrt(p_i p_j)
   int sqrt(f_i f_j)|u_i-u_j|_Omega^2 dmu.                     (6)
```

For `nu_i=N(m_i,S_i)`, define

```text
A_ij=(S_i^(-1)+S_j^(-1))/2,       H_ij=A_ij^(-1),
h_ij=H_ij(S_i^(-1)m_i+S_j^(-1)m_j)/2,
B_ij=S_j^(-1)-S_i^(-1),
b_ij=S_i^(-1)m_i-S_j^(-1)m_j.                                  (7)
```

The geometric mean `sqrt(dnu_i dnu_j)` is the Bhattacharyya coefficient
`BC_ij` times `N(h_ij,H_ij)`. Also
`u_i-u_j=B_ij x+b_ij`. Therefore the pair integral in (6) is exactly

```text
BC_ij {Tr[B_ij^T Omega B_ij H_ij]
       +|B_ij h_ij+b_ij|_Omega^2}.                              (8)
```

The quartic potential is linear in the probability law. For positive
amplitudes with constant phase,

```text
Q_N(nu)=sum_i p_i Q_N(nu_i)-[U-I_Omega(nu|mu)]/4.               (9)
```

Thus component overlap, not the coarser precision-Jensen width, is the exact
mixing benefit.

## K1607 — order-one separated covariance rigidity

Let `S_N^*` be K1572's profiled covariance and let the cutoff dimension be
`d_N=Theta(N^3)`. Fix `M`, `c_->0`, `c_+<infinity`, `delta>0`, and
`kappa>0`. Consider centered stationary diagonal Gaussian components with

```text
c_- S_N^* <= S_(N,i) <= c_+ S_N^*.                             (10)
```

For every distinct pair require a set of at least `delta d_N` modes on which

```text
|log(s_(i,k)/s_(j,k))|>=kappa.                                 (11)
```

For one centered diagonal mode the Gaussian affinity is

```text
[2 sqrt(s_i s_j)/(s_i+s_j)]^(1/2)
 =[sech((log s_i-log s_j)/2)]^(1/2).                            (12)
```

Hence, with `q_kappa=sqrt(sech(kappa/2))<1`,

```text
BC_ij<=q_kappa^(delta d_N)=exp[-c_(delta,kappa)d_N].             (13)
```

The score prefactor in (8) is also exact:

```text
Tr[B_ij^T Omega B_ij H_ij]
 =sum_k 2 omega_k(s_(i,k)-s_(j,k))^2
   /[s_(i,k)s_(j,k)(s_(i,k)+s_(j,k))].                         (14)
```

The fixed relative band (10) bounds (14) by a constant times
`Tr[Omega(S_N^*)^(-1)]=O_g(N^4)`. With fixed `M`, equations (6), (13), and
(14) give

```text
0<=sum_i p_iQ_N(nu_i)-Q_N(nu)
 <=C N^4 exp(-cN^3)=o(1).                                      (15)
```

K1572 bounds each component below by `lambda_N^prof`, and the class contains
the profiled Gaussian itself. Consequently

```text
lambda_N^prof-o(1)<=inf Q_N(nu)<=lambda_N^prof,
inf Q_N(nu)/N^4 -> h_g^prof.                                   (16)
```

This is an order-one heterogeneous theorem, but separation is load-bearing.
When two covariance profiles differ on only `o(N^3)` modes or converge to the
same macroscopic profile, their Bhattacharyya overlap need not be small.
Likewise, a growing mixture can accumulate pairwise bounds. Those classes and
all non-Gaussian/nonstationary routes remain open.

## K1608 — two-derivative primitive decay

Retain K1603's exact exclusion of pure-point harmonic-electric spectral mass.
Assume the absolutely continuous densities `F_+` and `F_-` are supported away
from `omega=0`. For arbitrary constant flat holonomy `a_infinity`, define

```text
G_+(omega)= iF_+(omega)/omega,
G_-(omega)= F_-(omega)/(i omega),

tilde a(t)=int[e^(it omega)G_+(omega)
               +e^(-it omega)G_-(omega)]domega,
a(t)=a_infinity+tilde a(t).                                    (17)
```

Then `-partial_t tilde a=E_h`. Suppose `G_+,G_- in W^{2,1}` and their values
and first derivatives vanish at every support endpoint. Two integrations by
parts give, for `t>=1`,

```text
|tilde a(t)|<=t^(-2)B_G2,
B_G2=||G_+''||_1+||G_-''||_1.                                  (18)
```

The direct Fourier bound is

```text
|tilde a(t)|<=B_G0,
B_G0=||G_+||_1+||G_-||_1.                                      (19)
```

Therefore

```text
||tilde a||_infinity<=B_G0,
int_0^infinity|tilde a|dt<=B_G0+B_G2,
int_0^infinity|tilde a|^2dt<=B_G0(B_G0+B_G2).                   (20)
```

This does not prove `E_h in L1`. It proves exactly the weaker primitive
budget needed by the corrected bare-energy normal form.

## K1609 — shifted normal form and radius composition

The constant `a_infinity` should not be spent as an infinite raw amplitude
budget. Put

```text
q_(sigma,k)=k-sigma e a_infinity                               (21)
```

and define `E_infinity` by replacing `|k|^2` in K1598's bare energy with
`|q_(sigma,k)|^2`. Expanding around `a=a_infinity+tilde a` gives

```text
E_infinity=H_a+e tilde a dot D_infinity
             -(e^2/2)|tilde a|^2M,
E_infinity'=e tilde a dot D_infinity'
             -(e^2/2)|tilde a|^2M'.                            (22)
```

The same mass inequality as K1598 yields

```text
|E_infinity'|
 <=[2|e||tilde a|+(e^2/m)|tilde a|^2]E_infinity.               (23)
```

With

```text
B_a=B_G0+B_G2,    B_a2=B_G0 B_a,                               (24)
```

Gronwall gives

```text
E_infinity(t)
 <=E_infinity(0)exp[2|e|B_a+(e^2/m)B_a2].                      (25)
```

If the background-adapted hierarchy has

```text
B_A(t)<=|e||tilde a(t)|+R(t),   B_R=int_0^infinity R<infinity, (26)
```

then K1573 gives

```text
rho_infinity>=rho_0-(C_m/4)(|e|B_a+B_R).                       (27)
```

The strict budget

```text
(C_m/4)(|e|(B_G0+B_G2)+B_R)<rho_0                              (28)
```

preserves a positive limiting radius. The result absorbs arbitrary static
`a_infinity`, but remains conditional on the atom-free representation, the
adapted hierarchy, and integrability of the nonlinear remainder.

## K1610 — protected integration and hostile bookend

The bridge census is now 325 rows: 246 satisfied, ten conditional, 65
excluded, and four missing. K1606 identifies the exact missing information
left by Fisher convexity. K1607 proves coefficient rigidity for fixed finite
macroscopically separated centered covariance mixtures, not all order-one
heterogeneity. K1608 weakens the spectral regularity needed for the holonomy
budget but does not prove electric-field `L1`. K1609 absorbs nonzero static
asymptotic holonomy only inside the declared background-adapted conditional
hierarchy.

The hostile quantum check merges components until the Hellinger exponent
vanishes, lets their count grow, or calls the theorem unrestricted. The
hostile PDE check restores a spectral atom, removes endpoint conditions,
asserts `E_h in L1`, or promotes the conditional background-adapted estimate
to a nonlinear source-owned flow. None of those transfers is licensed.

The next quantum wake is an overlap-free theorem for macroscopically
overlapping order-one covariance mixtures, a controlled growing-mixture
entropy bound, or a genuinely non-Gaussian/nonstationary Fisher-defect
inequality. The next PDE wake is to derive the primitive spectral measure and
integrable remainder from one source-owned nonlinear action/domain. The
source-owned action/measure/Hamiltonian tuple remains a separate admission
gate.

## Postflight bookend

The information-geometric route changed the operative quantity from the
precision-Jensen width to posterior score variance. Its positive result closes
one true order-one covariance class; its negative boundary is equally useful,
because overlap and mixture entropy are now the exact remaining Gaussian
obligations. The spectral route removes one derivative and the artificial
zero-holonomy normalization from the conditional amplitude budget, while
preserving the atom exclusion and nonlinear remainder debts.

Strongest overclaim: treating macroscopic separation as automatic under
order-one heterogeneity. Strongest contrary construction: two order-one
profiles that coincide on all but `o(N^3)` modes can retain nonvanishing
overlap, and a growing number of components can offset pairwise exponential
decay. Weakest propagation seam: the background-adapted coefficient (26) is
an explicit hypothesis; neither the source action nor the nonlinear coupled
flow supplies it here.
