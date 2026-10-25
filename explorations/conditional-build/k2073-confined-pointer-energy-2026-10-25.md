---
title: "K2073: Finite energy cost of the confined prepared pointer"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical construction only; no source physics, novelty or external certification
scripts:
  - tests/channel-swings/k2073_confined_pointer_energy.py
  - tests/channel-swings/k2073_confined_pointer_energy_probe.py
---

# K2073: Finite energy cost of the confined prepared pointer

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: uniform free-energy second moment and negative-sector first-moment bounds
carrier: full complex Dirac1408 Hilbert carrier with fixed massive projector P LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 norm and imported Born probabilities ON=declared_complex_completion
real_structure: complex completion; source real/dual field apparatus remains unproved
grading: fixed free energy sign and supplied multiplicity qubit
action_owner: repository-construction -- same symmetric cutoff pointer as K2071
target: prepared-state energy and all-outcome Bell resource bounds MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] K2071's confined control has a common H1 domain
and a uniformly bounded free-energy second moment on its SAME preparation. Combining
that bound with its small negative-sector probability now controls negative-energy
expectation as well. With the existing dimensionless radius2400, ramp width1 and
eta1/100, that expectation is at most0.24m, and the absolute change of the free
mean energy is at most0.28m. The existing all-outcome Bell lower bound remains
202263/100000>2. Arbitrarily small energy error and Bell violation coexist by increasing
the prepared control radius. This is one-particle mathematics with supplied controls;
it does not bound apparatus-field energy or establish a source physical quotient.

## 1. Same object and the missing resource question

Reuse [K2071](k2071-confined-pointer-control-2026-10-25.md), including H0=alpha.D+m beta,
m>0, fixed P=1_(H0>0), Hstar=(2/3)H0+(1/3)D1 Z, T=30/m, and
Hchi=H0+{chi,Hstar-H0}/2. Let Q=1-P. The smooth cutoff has values in[0,1],
is1 on B_(L+T+rho), vanishes outside B_(L+T+2rho), and can be chosen with
G=||grad chi||_infinity<=2/rho. Smooth a piecewise linear radial transition with
short flat margins to obtain this derivative bound. The core never approaches r=0,
so the radial formula has no singularity. Every setting uses the same scalar cutoff;
Z is any fixed unit Pauli axis during the pulse.

The state is psi=exp(iH0*20/m)phi tensor v, where K2067 fixes
phi-hat=g_m(p)u(p), ||u(p)||=1 and
|g_m|^2=(2*pi*m^2)^(-3/2)exp(-|p|^2/(2m^2)). Thus each momentum coordinate has
variance m^2. Since H0^2=(|p|^2+m^2)I, the EXACT initial rms energy is

    E2=||H0 psi||=2m.                                  (1)

This uses the Gaussian second moment, not Jensen's mean-energy bound. The free
prechirp and arbitrary multiplicity state leave(1) unchanged. The preparation
already has eta=||1_(|x|>L)psi||<=24/(mL).

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 is UNCERTAIN about rival
southeast terms; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56
DISAVOWS an odd-action prerequisite. None supplies this Hilbert/Born/tensor/control
completion. LT-SM8/GR6b, the source register, ledger and canon remain unchanged.
The source's indefinite pairing is not identified with the positive norm used here.

## 2. Domain and a uniform graph estimate

Write a=1-chi/3, b=chi/3. On Cc-infinity,

    Hchi=a H0+b Z D1+C,
    C=-(i/2)(alpha.grad a+Z partial_1 b),  ||C||<=G/3. (2)

The displayed C alone is not claimed Hermitian; it supplies the symmetric ordering
of the whole differential expression. The perturbation Hchi-H0 is symmetric and
has admissible (not claimed sharp) relative H0 bound at most2/3, with bounded remainder G/3. The Kato-Rellich theorem
therefore gives a self-adjoint operator on H1, with Cc-infinity a core. This is the
same unique closure used by K2071, whose smooth bounded symmetric-hyperbolic
coefficients also give the speed-one propagation estimate.

More sharply, since a>=2/3, b<=1/3, and ||D1 u||<=||H0 u||,

    ||Hchi u|| >= (1/3)||H0 u||-(G/3)||u||,
    ||Hchi u|| <= (4/3)||H0 u||+(G/3)||u||.            (3)

No derivative of u was discarded. Multiplication by a is bounded below pointwise;
the triangle inequality applies to aH0u before the bD1u term is subtracted. Taking
the graph closure extends(3) to all H1. The unitary Uchi(t) preserves its operator
domain and ||Hchi Uchi(t)psi||=||Hchi psi||. Hence for every t in[0,T],

    ||H0 Uchi(t)psi|| <= 4 E2+2G
                      <= 8m+4/rho =: M.               (4)

There is no exponential time factor or dependence on the volume of the controlled
region. Free evolution after the pulse preserves the same bound. An arbitrary
smooth time-dependent ramp would require a new energy estimate; static-in-time
pulses with instantaneous switches at their endpoints are exactly the model here.

## 3. Negative energy and free-energy change

K2071 proves ||Q Uchi(t)psi||<=2eta by comparing with Ustar(t) on the causal tube.
The spectral theorem and Cauchy-Schwarz now imply

    Eminus(t):=<Uchi psi, |H0| Q Uchi psi>
       <= ||Q Uchi psi|| |||H0| Q Uchi psi||
       <= 2eta M <= eta*(16m+8/rho).                  (5)

This is the first moment of the NEGATIVE free-energy sector, not the expectation of
an unbounded-below interacting field Hamiltonian. Both P and Q commute with |H0|.
More generally, the negative-sector probability above absolute energy Lambda>0 is
at most

    min(4eta^2, 2eta M/Lambda, M^2/Lambda^2).          (6)

No conclusion about higher energy moments is inferred from(4). The weaker bound
<|H0|> <= M follows immediately. A better comparison with the ideal pointer uses
its preserved H0 norm E2 and the same norm difference2eta. For A=H0 OR |H0|,
expand the quadratic-form difference between actual u and ideal v:

    |<u,A u>-<v,A v>|
       <= ||u-v|| (||Au||+||Av||)
       <= 2eta(M+E2) <= eta*(20m+8/rho).              (7)

The ideal pointer commutes with H0, so its signed and absolute mean energies equal
the initial positive mean. Equation(7) therefore bounds the change in either
mean. It is not a field-energy budget: changing and sustaining the external control
may require resources not present in this one-particle model.

Small sector probability by itself cannot yield(5). In a two-mode spectral example,
keep probability p in a negative mode with energy-N while letting N grow. Its
negative expectation is Np. Likewise a bounded mean does not bound the second moment:
probability1/N^2 at energy N^2 keeps the mean below2 but makes the second moment grow
as N^2. The finite controls include both counterexamples.

## 4. Consumed simultaneous energy and Bell requirements

At rho=1/m, M=12m. For eta=1/100, (5) gives Eminus<=6m/25=0.24m,
and(7) gives mean change<=7m/25=0.28m. K2071's complete finite detectors and supplied
tensor Bell experiment continue to give

    S >= 2*(7/5)*(183/200)^2-32eta-16eta^2 >2.         (8)

For any requested dimensionless epsilon>0, take

    eta0=min(1/100,epsilon/24),
    L=24/(m eta0), rho=1/m, T=30/m.                  (9)

Then Eminus<=epsilon*m and (8) still exceeds2. The control radius is L+32/m,
the detector radius L+30/m, and center separation greater than2L+94/m gives the
same spacelike-separated control cylinders. For example epsilon=1/100 requires
L=57600/m, rather than silently claiming the earlier radius meets this tighter
energy tolerance. These are conservative sufficient values, not minimal apparatus
sizes. For a fixed total radius R=L+T+2rho, the bound in(5) with eta<=24/(mL)
has a real ramp/localization tradeoff; shrinking rho without paying its gradient
invalidates the energy certificate.

For a fixed total control radius, this sufficient energy budget can be optimized.
Set x=mL, y=m rho and w=m(R-T)=x+2y. The bound is
Eminus/m <= (384+192/y)/(w-2y). Its derivative has the sign of
4y^2+4y-w; hence the unique minimum on0<y<w/2 is at
y=(sqrt(1+w)-1)/2, with value384/(sqrt(1+w)-1)^2. This optimizes the
stated conservative bound, not physical apparatus size; x>=2400 must still be
checked for Bell violation. At epsilon1/100, the exact convenient choice
y=100, x=38592 gives eta=1/1608 and Eminus<=m/100. Control radius38822/m,
detector38622/m and strict separation77674/m suffice, versus control radius57632/m
for the earlier rho=1/m energy certificate. The finite checks include the exact
stationary-point formula and both neighboring sides.

All estimates tensor with an untouched ancilla. The initial common spatial factor
makes(1) uniform over the entire qubit subspace, including entangled preparations.
Convexity extends the first-moment bounds to mixtures of the stated preparations.
For N supplied laboratories, each reduced state has Eminus_i<=2eta_i M_i, so the
sum is bounded by their sum. This adds no interaction or field-locality theorem.

## 5. Scope and review

This closes K2071's explicit energy-expectation gap on its declared preparation and
static confined control, with usable accuracy/radius consequences. Exact positive-sector
invariance, uniformly small errors on arbitrary translated states, a source-real
physical detector algebra, vacuum/Fock implementability and control-field energy
remain open. One-particle finite energy cannot certify vacuum particle creation;
K2064's separate fixed-sea restrictions remain relevant and unchanged.

Strongest overclaim: replacing an rms bound by a mean-energy bound is invalid; (1)
computes the second moment directly. Strongest contrary control: fixed tiny negative
probability at arbitrarily high negative energy; (4) is the needed extra hypothesis.
Weakest seam: finite spectral examples do not prove the continuum domain theorem;
the relative bound and self-adjoint spectral calculus above do. The proof uses only
standard graph-norm estimates, Kato-Rellich and Cauchy-Schwarz; no novelty is claimed.

Producer evidence is exact Gaussian/resource arithmetic over seven cases. The separate
probe has42 resource checks,115 finite spectral checks and six actual corrupted-resource
faults rejected after a passing baseline. They are same-author implementations,
not independent specialist or proof-assistant certification. Prior graph, Gaussian,
causal comparison and Bell evidence are hash-pinned reuse.

Primary reference for the inherited hyperbolic closure: Paul R. Chernoff,
[Essential self-adjointness of powers of generators of hyperbolic equations](https://www.sciencedirect.com/science/article/pii/0022123673900037),
Journal of Functional Analysis12(1973),401-414. The explicit relative-bound proof here
also places this particular cutoff on the standard Kato-Rellich domain.

## 6. Independent internal mathematical review

A separate operator/PDE review agent examined the domain, derivative correction,
Gaussian second moment, graph conservation, entangled/mixed extension and radius
optimization. It found no substantive defect. Its adversarial negative-sector
construction holds probability fixed while sending the occupied negative energy to
infinity; this confirms why the uniform second moment is essential. The probe's
Bernoulli comment is corrected to probability1/N^2 at energy N^2; its arithmetic
was already correct. The relative constant2/3 is admissible, not claimed sharp.
This is independent internal agent review, not external specialist or proof-assistant
certification. The result concerns free-energy moments of the prepared particle state,
not the energy cost of an apparatus or control field. Radius optimization concerns
only the conservative sufficient bound. No scientific source verdict changes.
