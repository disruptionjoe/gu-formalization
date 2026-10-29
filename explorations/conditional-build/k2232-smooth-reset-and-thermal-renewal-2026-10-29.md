---
title: "K2232 Smooth reset and finite-time thermal-bank renewal"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: smooth externally timed finite controls and supplied independent thermal Markov reservoirs; no microscopic bath renewal, autonomous apparatus or GU realization
scripts:
  - tests/channel-swings/k2232_smooth_reset_and_thermal_renewal_probe.py
---

# K2232 Smooth reset and finite-time thermal-bank renewal

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2232 smooth exact resonant reset, reference-uniform thermal renewal and repeated-bank resource identities
carrier: positive record qubit, finite qubit bank and arbitrary untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: binary occupation and additive energy
action_owner: repository-construction -- externally timed gap/exchange controls and supplied thermal Markov generators
target: repeated reset channel, bank renewal accuracy and heat/entropy ledger MAP-TYPE=intertwiner
```

## Independent preflight and rerank

Loaded AGENTS, geometer/physics routing T15/T16/T17, source-native comparator
routing, Layer 0, current state, research posture, verification, contribution
and path-dependency surfaces. The object is K2229's positive record and
varying-gap bank, with K2228's detector admitted only through its stated
reference-uniform input-energy estimate. Neither is a GU physical quotient,
native action, local field interaction, nor a chirality construction.

K2229 already proves exact SWAP reset and its net work, but assumes
instantaneous switching and consumes a fresh independent bank each time.
K1916 establishes finite-rate preparation limitations and zero-temperature
damping; K98 constructs finite detailed-balanced semigroups; K1221 studies
GAD affine geometry; K117 has a classical Markov-additive reservoir lift.
None of those retrieved notes supplies this 1701-cell finite-temperature,
correlation-uniform same-bank repeated consumer. Highest useful increment:
retain K2229's exact protocol, smooth its controls, construct an explicitly
supplied thermal renewal channel, and carry its error and resource ledger
through repeated uses. General SWAP, GAD and entropy-contraction mechanisms
are established mathematics; no novelty is claimed.

Primary background: [Khatri, Sharma and Wilde, generalized amplitude damping](https://arxiv.org/abs/1903.07747)
and [Carlen and Maas, detailed-balance quantum semigroups](https://arxiv.org/abs/1609.01254).
The estimates below are proved directly; the sources are background, not a
substitute for the conditional construction. In particular an exact Markov
model does not certify its approximation by a finite microscopic bath.

## 1. Finite smooth controls with exactly the same reset and work

Use K2229's beta>0, 0<v<=1/2, r>1, and x_j=log((1-v)/v)+j log r, E_j=x_j/beta,
p_j=(1+exp(x_j))^-1, j=0,...,m, q=p_m. Initially B_j is an
independent Gibbs qubit tau_j=diag(1-p_j,p_j). During a gap change the record
is isolated and H_R(t)=E_R(t)n_R. During contact j its gap is held at E_j and

    H_j(t)=E_j(n_R+n_Bj)+g_j(t)(I-S),
    g_j(t)>=0, integral g_j(t)dt=pi/2.

All Hamiltonians are positive. Since [n_R+n_Bj,S]=0, every Hamiltonian in
one contact commutes with all the others in that contact. The exact
propagator is exp(-iE_j T_j(n_R+n_Bj)) S. Thus the fresh-cell reset on the
record and arbitrary reference is exactly the same replacement by tau_j.
Finite smooth ramps introduce NO channel error in this model.

An explicit C-infinity schedule is available. Put h(u)=exp(-1/[u(1-u)])
for 0<u<1 and zero otherwise, J=integral_0^1 h(u)du, and
f(u)=J^-1 integral_0^u h(z)dz on [0,1], extended by zero/one outside.
Set E_R(t)=E_a+(E_b-E_a)f(t/T_gap) for an isolated ramp and

    g_j(t)=pi f'(t/T_j)/(2T_j).

All derivatives join smoothly, g_j is nonnegative and has exactly the
required area. The sign of h' is the sign of 1-2u, so each coupling pulse
has one crest and total variation exactly 2g_peak. If C1=max_[0,1] f' and C2=max_[0,1]|f''|, both finite,
then g_peak=pi C1/(2T_j), |dot g|<=pi C2/(2T_j^2), and
a gap ramp has |dot E|<=|E_b-E_a| C1/T_gap. Specifying positive durations
therefore supplies finite strength and finite power. Conversely a prescribed
strength/power ceiling requires choosing durations satisfying these bounds;
this theorem does not derive the controller or its power source.

On contact, <I-S> is conserved even with a correlated input, so
integral dot g(t)<I-S>dt=0 exactly. With fresh independent entry,
0<=<I-S>=1-Tr(rho_R tau_j)<=1, hence total absolute mean coupling exchange
is <=2g_peak. For arbitrary correlated entry only 0<=<I-S><=2 is guaranteed,
and the safe bound is <=4g_peak. Isolated gap ramps preserve populations,
so K2229's net-work formula survives unchanged:

    beta W = w x_0 + sum_(j=1)^m p_(j-1)(x_j-x_(j-1)) - q x_m.       (1)

The final gap lowering is essential. With a common gap-ramp duration T_gap
and contact duration T_c, one reset takes (m+2)T_gap+(m+1)T_c.
No free timing, autonomous clock or microscopic switching work is implied.

## 2. Explicit finite-temperature renewal semigroup

After reset, decouple the record and keep each bank gap fixed. Supply the
independent local generators (units hbar=1)

```text
    L_j(rho)=-i[E_j n,rho]+kappa_j(1-p_j) D[sigma_-](rho)
                               +kappa_j p_j D[sigma_+](rho),
    D[L](rho)=L rho L* - {L*L,rho}/2,  kappa_j>0.                  (2)
```

The upward/downward ratio is p_j/(1-p_j)=exp(-beta E_j). The dissipative
Heisenberg generator is self-adjoint in the Gibbs GNS inner product:
diagonal observables obey the reversible two-state chain, and off-diagonal
matrix units are orthogonal eigenvectors with real eigenvalue -kappa_j/2.
The Hamiltonian part is separately anti-self-adjoint and commutes with it.
This is detailed balance of the dissipator with its commuting Hamiltonian
part declared, not the false claim that the full Hamiltonian generator is
GNS self-adjoint.

Write eta_j=exp(-kappa_j t_j), s_j=sqrt(eta_j). Apart from a known free
phase, on every operator the channel Phi_j satisfies

    excited population a -> p_j+eta_j(a-p_j),
    coherence c -> s_j c.                                      (3)

It is the convex combination (1-p_j)AD_down,eta_j+p_j AD_up,eta_j,
so is completely positive and trace preserving and fixes tau_j. On arbitrary
reference-valued blocks rho_BF=[[A,C],[C*,B]], F=A+B,

    (Phi_j-Tau_j) tensor id (rho)
      = [[eta_j D, s_j C], [s_j C*, -eta_j D]],
    D=p_j A-(1-p_j)B,
    Tau_j(X)=tau_j Tr X,                                       (4)

up to the harmless phase on C. Positivity gives ||C||_1<=sqrt(Tr A Tr B)<=1/2;
||D||_1<=p_j Tr A+(1-p_j)Tr B<=max(p_j,1-p_j). Therefore

    (1/2)||Phi_j-Tau_j||_diamond
       <= d_j := min(1, s_j/2+max(p_j,1-p_j)eta_j).              (5)

The diamond statement follows because a difference of channels attains its
completely bounded trace norm on states with a reference; (4) holds for
every such state. This is a sufficient bound, not a sharp diamond formula.
It handles correlations with every other cell and arbitrary external F.

For N=m+1 cells, tensor telescoping and channel contractivity give

    (1/2)|| tensor_j Phi_j - Tau_bank ||_diamond
       <= epsilon_B := min(1,sum_j d_j),                       (6)
    Tau_bank(X)=(tensor_j tau_j) Tr X.

Thus from ANY correlated bank/reference input, the renewed bank is within
epsilon_B of the product Gibbs bank tensored with that SAME input reference
marginal. This is actual approximate decoupling, not marginal thermalization
mistaken for independence. Free rotations preserve this assertion.

No finite t_j makes (2) an exact replacement: a diagonal population a!=p_j
retains eta_j(a-p_j), and coherence retains s_j c. Exact replacement needs
the infinite-time limit or a changed resource model. The semigroup is an
externally supplied reservoir assumption; it neither builds a finite bath
nor renews the reservoir itself. Fixed positive rates across the varying gaps
are supplied too, not consequences of a bath spectrum.

## 3. Same-bank repeated detector/reset cycles

Keep the same N physical cells. Between reset contacts and renewal, arbitrary
CPTP detector/readout maps may act on the record and retained reference,
including classical feedback and copies of recorded outcomes. They may not
act on the bank. The ideal comparison replaces the bank by its product Gibbs
state before each reset and uses ideal pure reset of the working record.
Input bank is initially exact product Gibbs. A hybrid insertion of (6)
then K2229's q-uniform reset bound gives, after M resets,

    complete retained-output error <= min(1,M q+(M-1)epsilon_B). (7)

If the final renewed bank is also included in the compared output, use
min(1,M(q+epsilon_B)). No independence of intermediate detector states or
classical history is assumed. This is a full joint channel comparison;
errors may accumulate in retained history even while each newly renewed bank
has the fresh error ceiling epsilon_B relative to the current reference.
For K2228's energy-constrained detector approximation, add sum_k delta_k,
provided each compared detector input satisfies its required energy budget.
Reset does not establish those future field-energy budgets.

The ideal-reference work formula (1) is not exact on an imperfect bank.
If its actual pre-reset populations are b_j, exact SWAP and isolated ramps
instead give

    beta W_actual=w x_0+sum_(j=1)^m b_(j-1)(x_j-x_(j-1))-b_m x_m. (8)

Coherences and correlations do not alter this population identity. Immediately
after renewal, comparison with the product bank and the SAME reference
marginal changes no w. The bank work observable in (8) has spectral range
2x_m-x_0, hence

    |beta W_actual-beta W_ideal(w)| <= (2x_m-x_0)epsilon_B.      (9)

This is a per-cycle bound relative to the actual record prior w. A fixed
ideal detector's prior may itself differ: then add x_0|w-w_ideal|, with
|w-w_ideal| bounded by the appropriate full-history hybrid error. It would be
incorrect to inherit K2229's narrow prior interval for arbitrary later cycles.
The universal correlated-entry absolute coupling bound 4g_peak applies in
these renewed cycles; the old fresh-product 2g_peak bound must not be reused
silently.

## 4. Heat and correlation-aware entropy ledger

Let rho_BF enter renewal, rho'_BF=(tensor Phi_j tensor id)rho_BF,
H_B=sum_j E_j n_j and tau_B=tensor tau_j. Define heat delivered to the
supplied reservoirs, positive outward, by

    Q_res=Tr H_B(rho_B-rho'_B)
         =sum_j E_j(1-eta_j)(a_j-p_j),                         (10)

where a_j is the pre-renewal cell population. There is no work term during
the fixed-Hamiltonian ideal semigroup itself. Resource costs for establishing,
switching and maintaining (2) remain outside the model.

Contractivity of relative entropy under the bank channel gives the EXACT
correlated entropy balance

    Sigma = D(rho_BF || tau_B tensor rho_F)
            -D(rho'_BF || tau_B tensor rho_F)
          = S(B|F)_out-S(B|F)_in + beta Q_res >=0.             (11)

For arbitrary reference dimension define conditional entropy through the
finite-B relative-entropy identity, avoiding subtraction of infinite
reference entropies. This accounts for intercell and bank/reference
correlations; replacing it by sum_j binary entropies would lose that cost.
It does not assume Q_res>=0 for every arbitrary bank input. Gibbs renewal
can absorb heat from the reservoir if the bank was below equilibrium.

For an initially fresh K2229 reset, the spent cell populations are a_0=w
and a_j=p_(j-1) for j>0. With common eta, (10) gives exactly
Q_res=(1-eta)W from (1). The residual eta W stays as excess bank energy.
On subsequent uses, (8) and the general exact energy balance are safer:

    W_k=Q_res,k+E_B,after-renewal,k-E_B,before-reset,k,
    sum_k W_k=sum_k Q_res,k+E_B,final-E_B,initial.              (12)

Record endpoint Hamiltonians and coupling endpoint terms vanish. Thus bath
heat is not an extra work charge added to W; it is where the supplied reset
work goes, up to bank-energy change. With finite renewal error the bank is
not exactly cyclic. Its endpoint deviation from tau_B obeys
|E_B,final-E_B,tau|<=epsilon_B sum_j E_j, since H_B has that spectral range.
This controls the unaccounted energy remainder without claiming microscopic
reservoir or total-apparatus closure.

## 5. Exact 1701-cell consumer

Retain K2229's v=3/10, r=101/100, m=1700, N=1701 and its certified q:

    q=3*100^1700/(3*100^1700+7*101^1700)<1.930581e-8.

Choose kappa_j=kappa and renewal time t=100 log(2)/kappa for all cells,
with independent local channels running concurrently (a supplied hardware
capacity). Then eta=2^-100, s=2^-50 and

    epsilon_B <=1701(2^-51+2^-100)<7.554e-13.                  (13)

A serialized renewal has duration 1701t for the same error; concurrent
renewal takes t. Neither statement prices hardware concurrency. One full
concurrent-renewal cycle lasts 1702T_gap+1701T_c+t, finite at finite positive
chosen durations and kappa. For M=1000, including final bank,

    1000(q+epsilon_B)<0.000019306566.                         (14)

Only 1701 cell systems are reused, instead of 1,701,000 distinct fresh cells;
the external thermal reservoirs remain consumed resources. This is not a
finite closed apparatus. Since x_m<17.762861 and x_0>0, (9) is <
2*17.762861*7.554e-13 <2.684e-11 in dimensionless work per cycle, relative
to the actual prior. The endpoint bank-energy remainder in beta units is
<epsilon_B*1701*17.762861<2.283e-8. Initial ideal detector work still has
K2229's 0.616212<beta W<0.616260, now with finite smooth switching; later
cycles additionally require their stated prior/energy conditions.

These are deliberately conservative sufficient constants. For the special
first fresh-bank cycle, the later spent cells are diagonal and independent;
the general worst-case 1701-cell estimate is unnecessary but safe. No
large 2^1701 matrix calculation or finite approximation to the reservoir
was used to prove the uniform theorem.

## Hostile postflight and reproducibility ceiling

Strongest overclaim: 'bath renewal closes an autonomous reusable apparatus.'
False: (2), its stationary temperature, rates, independent noise and timed
attachment are supplied. The result closes approximate reuse of the finite
bank ONLY inside this reservoir/control model. It does not renew the
reservoir, recover GU, select a physical quotient or provide a clock.

Strongest counterconstructions and weakest seams:

1. Marginal Gibbs states can remain maximally correlated; (4)-(6), not
   marginal convergence, are required for reuse against arbitrary history.
2. Coherence decays at half the population rate. Replacing s by eta falsely
   speeds the universal renewal guarantee; a coherent qubit detects it.
3. Finite eta retains diagonal mismatch; no finite-time exact-renewal claim.
4. Smooth area alone is insufficient if the record and cell gaps differ
   during contact: [E_R n_R+E_B n_B,S]!=0. Resonance must be held throughout.
5. Coupling switch-work cancellation uses commutation, but the fresh-entry
   2g_peak absolute bound fails for antisymmetric entangled entry; use 4g_peak.
6. A retained copy of the outcome survives working-record reset. Its storage
   and eventual erasure are outside (1), and must remain in the reference.
7. Reusing the ideal prior, ignoring residual bank energy, or adding exported
   heat to net work as a second charge would each corrupt resource accounting.
8. The supremum/diamond proofs and entropy data-processing argument are written
   mathematics. Exact finite matrix-unit, Kraus, recurrence, energy and rational
   controls exercise algebra and concrete constants; they do not certify a
   physical bath or infinite-environment approximation.

The accompanying probe uses genuine mathematical-input mutations (wrong
coherence rate, upward rate, final quench, heat sign, exact finite renewal,
and unequal contact gaps). It does not mutate acceptance flags. No source
claim, ledger score, physical mapping, hypothesis vote or canon changes.

## Reproduction and evidence boundary

The [exact probe](../../tests/channel-swings/k2232_smooth_reset_and_thermal_renewal_probe.py) checks finite algebra and rational consumers; universal statements rely on the written proofs above. Run the probe with the repository Python environment. Its default run regenerates controls in memory and rejects a stale [certificate](../../lab/process/k2232-smooth-reset-and-thermal-renewal.json); `--write` refreshes that report. Note, probe and reused dependency hashes bind the report. Each planted fault changes mathematics or a supplied input and must fail an unchanged check after a green baseline. Internal independent review is not external-expert or proof-assistant certification.
