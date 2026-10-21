---
title: "K1893: Hamiltonian shielding, fermionic parity and genuine hidden interactions"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite full/even CAR classification and a bounded continuum hidden-interaction construction; no native GU action or physical positive-energy vacuum
scripts:
  - tests/channel-swings/k1893_quantum_hamiltonian_shielding.py
  - tests/channel-swings/k1893_quantum_hamiltonian_shielding_probe.py
---

# K1893: Hamiltonian shielding, fermionic parity and genuine hidden interactions

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
result: complete finite full/even algebra Hamiltonian shielding conditions and bounded hidden CAR quartic dynamics
carrier: finite complex fermionic Fock factors and K1892 complex Hilbert source splitting LAYER=toy CHIRALITY=N/A
pairing: positive Fock and K1892 H-positive one-particle pairings ON=declared_finite_factors_and_CAR_Cstar_algebra
real_structure: complex CAR star structure imported independently of the native K/C forms
grading: fermionic parity; not source graded-IG or observed particle chirality
action_owner: repository-construction -- conditional bounded Hamiltonian perturbation of K1892 free CAR dynamics
target: exact observed automorphism and its full/even observable distinction MAP-TYPE=restriction
```

## Decision and evidence boundary

The classical nonlinear hidden flow in [K1892](k1892-causal-observation-algebra-2026-10-21.md)
is not a quantum interaction. Here a commutant calculation first classifies the
finite Hamiltonian problem, then a bounded CAR perturbation constructs an actual
interacting quantum automorphism on K1892's continuum source algebra. Restricting
to even observables makes a real difference: parity-controlled interactions can
be invisible to that algebra without being invisible to odd fields.

CAR statistics, the positive Hilbert/Fock pairing, the selected accessible algebra
and the perturbing Hamiltonian are imported. SC-OP-04 ASSERTS candidate operator
grammar; SC-MAS-01/SC-CHI-02 ASSERT a stylized mass coupling. SC-OP-05 and SC-META-53
remain UNCERTAIN. WGS05 supplies no full20 injection, separate K/C reality forms
or selected quantum interaction. LT-SM8 and AC-F1 remain NEEDS. No source, physics
ledger, canon, novelty or physical GU claim follows.

Retrieval distinguishes K1892's free CAR transfer and classical nonlinear flow,
K115's classical feed-forward detector, and finite ghost/Clifford parity results.
Those do not classify this fermionic observable algebra. The structural route
eliminates a search over polynomial Hamiltonians. The contrary controls test
both a genuine parity exception and a coupling that affects even observables.

## 1. Exact finite Hamiltonian theorem

Take n>=1 visible and m>=1 hidden complex modes. In the fixed visible-first
Jordan-Wigner order,

```
F = F_v tensor F_h,
a_v(f)=a(f) tensor I,
a_h(g)=P_v tensor a(g),
A_v = B(F_v) tensor I,
A_v^even = (B(F_v^+) direct_sum B(F_v^-)) tensor I.
```

P_v=(-1)^N_v is fermionic parity. Fix an even Hermitian target Hamiltonian H_v.
For an even Hermitian total H, the following full-algebra statements are equivalent:

1. For every X in A_v and every real t, exp(itH) X exp(-itH) is the prescribed
   target evolution exp(itH_v) X exp(-itH_v) tensor I.
2. `[H-H_v tensor I,X]=0` for every X in A_v.
3. `H=H_v tensor I+I tensor K_h`, where K_h is even and Hermitian.

Differentiate1 at t=0 to get2. Commutation with all visible matrix units forces
all off-diagonal visible blocks of the residual to vanish and all diagonal
blocks to coincide, giving3. Conversely the two summands commute and exponentiate
separately. Total parity then gives `[K_h,P_h]=0`. This is all-state equality,
not a statement about a preferred vacuum or one reduced density matrix.
No genuine visible-hidden interaction can preserve the prescribed FULL target
Hamiltonian evolution in this finite factor setting.

## 2. The even-algebra exception is exact

If only A_v^even is required to have that evolution, the residual instead is

```
H-H_v tensor I = P_+ tensor K_+ + P_- tensor K_-,
P_+=(I+P_v)/2, P_-=(I-P_v)/2, [K_+,P_h]=[K_-,P_h]=0.       (1)
```

Proof: the two central projections P_+,P_- belong to the even algebra, so a
commuting residual is block diagonal. Matrix units within each block force it
to be scalar on that visible block. Total parity imposes the hidden evenness.
Conversely (1) commutes with the entire even algebra. It can depend on visible
parity and thus record that classical central label without disturbing any even
visible observable. The hidden motion can differ in the two sectors.

For n=m=2, the complex commutant dimensions are16 for the full algebra and32
for the even algebra. Their total-even Hermitian real dimensions are8 and16.
The producer counts Pauli monomials; the independent probe computes commutation
with every visible matrix unit, separating parity blocks. These finite checks
are witnesses to the proof, not a numerical extrapolation to arbitrary n,m.

A concrete nonquadratic hidden interaction is Q=n_h1 n_h2, a norm-one projection.
The parity-controlled coupling P_v Q commutes with every even visible observable
but not a_v1. By contrast, n_v1 n_h1 changes the even hopping observable:

```
[n_v1 n_h1, a_v1^* a_v2] = a_v1^* a_v2 n_h1 !=0.         (2)
```

Replacing visible parity by total visible number also fails for the full even
algebra: pair creation/annihilation is even and changes that number by2. A
number-superselected algebra would be a different accessible algebra. A theorem
about all even observables cannot silently assume that additional restriction.

An explicit readout consumer of (1) takes one hidden mode, H=g P_v tensor X_h
with an even logical hidden qubit encoding (two hidden modes). Conditional on
visible parity p=+/-1, hidden |0> evolves by exp(-it g p X). Its Y expectation
has opposite signs, proportional to sin(2gt). At gt=pi/4 the two hidden states
are orthogonal. Every even visible observable still follows its target law.
The hidden logical X is an even bilinear in the dual-rail encoding of K1894;
a bare odd single-mode X would violate the total-even assumption.
This reveals parity, not arbitrary within-sector quantum information.

## 3. A genuine continuum hidden quartic automorphism

Now reuse the ACTUAL closed whole-space split from K1892:

```
H_s = j H_t orthogonal_sum H_h, H_h=ker V,
U_s(t) j = j U_t(t), U_s(t) H_h = H_h.
```

Choose orthonormal h1,h2 in H_h and define the bounded even CAR element
Q=g n(h1)n(h2), g real. Each n(h)=a(h)^* a(h) is a projection of norm1;
Q is self-adjoint, has norm |g| and is not a quadratic one-particle operator.
Its hidden commutator is `i[Q,a(h1)]=-ig a(h1)n(h2)`.

The bounded-perturbation cocycle of the free strongly continuous CAR group
exists in norm by the Dyson series; its nth term is bounded by
`(|g||t|)^n/n!`. It defines a strongly continuous star-automorphism group
with generator delta_0+i[Q,.] on the free generator domain. This is an actual
quantum interaction construction, unlike applying the classical nonlinear map
to one-particle vectors. It transports positive algebraic states to positive
states because star-automorphisms preserve positivity and the identity.

Every interaction-picture alpha_0(s)(Q) is hidden and even, hence commutes with
every observed a(jf), including the odd fields. The cocycle therefore fixes
alpha_0(t)(a(jf)), and

```
alpha_Q(t)(a(jf)) = alpha_0(t)(a(jf))                    (3)
```

for all f,t. By generation and norm continuity, (3) holds on the entire
observed CAR algebra. It also preserves K1892's raw differential observed
fields on their test domain, since Odagger f lies in ran j. Thus the target
unequal-time covariance, target even locality and target speed1/24 cone survive
EXACTLY. No estimate based on small g is needed.

This construction is nonempty on the actual carrier. K1892 gives a constant
four-dimensional N=intersection ker T_i with S N=0. Smooth compact source
functions valued in N satisfy O h=0; two such orthonormal functions give h1,h2.
The fixed smeared quartic is an element of a bounded source-region algebra when
these functions have common compact support. This is not a pointlike quartic
field density or a translation-invariant local QFT interaction, and no ultraviolet
limit has been taken. The free evolution need not preserve N pointwise; it
preserves the full H_h, which is exactly the hypothesis used in (3).

More generally any bounded self-adjoint even element of CAR(H_h) works, as does
an absolutely norm-summable family. This is not a claim about arbitrary unbounded
interactions, thermodynamic limits, ground-state lower bounds, Hadamard states
or physical vacuum selection. The initial free generator already has both signs;
positive algebraic states are not positive energy.

## 4. No unproved infinite parity transfer

The finite visible-parity example is not automatically an element of the infinite
quasilocal CAR algebra. If P_N is the product of the parity operators of the first
N visible modes, `||P_{N+1}-P_N||=2`. The sequence has no norm limit. Consequently
the naive global-parity controlled interaction does not extend by that norm limit.
No full continuum relative-commutant classification is claimed here. The bounded
hidden construction above requires no global visible parity and is unaffected.

## Verification, hostile review and useful next demand

The analytic proofs establish arbitrary finite mode counts and the bounded
continuum cocycle. Exact finite CAR controls and the separate occupation-basis
probe supplement those proofs; manifest fields are reporting evidence only.
Reproduce with the producer then its `_probe.py` using Python with SymPy.
The probe first validates a clean report, then changes a real interaction,
parity coefficient, leaked commutator, dimension report and input pin. Crashes
are not accepted as detection. An initial producer trigonometric comparison
needed trigsimp rather than plain expansion; no coefficients were changed.

Hostile checks: full versus even versus number-conserving algebra; logical
hidden parity; finite matrix factors versus continuum local algebras; bounded
CAR perturbation versus nonlinear one-particle map; positive states versus
positive energy; exact hidden reduction versus pointwise N invariance.
No blocking finding remains at this scope. No independent-agent, external
expert, proof-assistant or novelty certification is claimed.

The exact full-algebra theorem rules out informative Hamiltonian backaction
while keeping the entire target law unchanged, but the even center supports a
scoped exception. K1894 tests the distinct irreversible escape and its bounded continuum
extension with an explicit spatial-causality countercontrol, rather than
promoting this finite Hamiltonian statement to all quantum dynamics. A native
GU application still needs an authenticated accessible algebra and interaction.
