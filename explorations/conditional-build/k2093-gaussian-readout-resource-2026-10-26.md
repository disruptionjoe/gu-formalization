---
title: "K2093: Gaussian resource floor for coherent coarse readout"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, continuum apparatus, GU verdict or external certification
scripts:
  - tests/channel-swings/k2093_gaussian_readout_resource_probe.py
---

# K2093: Gaussian resource floor for coherent coarse readout

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
result: conditional apparatus and state theorem with explicit countercontrols
carrier: two-mode complex CAR and declared fermionic environment LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: supplied positive Hilbert metric ON=declared_complex_completion
real_structure: supplied particle-hole symmetry where invoked, not source derived
grading: parity, charge, energy sign and representation remain separate
action_owner: repository-construction -- free dynamics and explicitly supplied controls
target: conditional operational constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS a candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
The supplied positive massive CAR model is not source operator9.16. LT-SM8 and
LT-GR6b retain their actual action/observation/quotient/state debts. K2021 already
constructs local R0/R1; it does not source-select the present dynamics or controls.
Source-register, physics-ledger and canon verdicts remain unchanged. These are
conditional reverse-scaffold constraints, not GU predictions, novelty claims or
external/proof-assistant certification. No new substrate pathway is asserted.

## 1. A fixed Gaussian environment cannot implement the channel

Use K2090's two orthogonal modes f,g=bf and occupation basis (00,01,10,11).
E=diag(1,0,1,1), F=I-E and Phi(rho)=E rho E+F rho F. This is the
NONSELECTIVE system channel; the readable instrument has an additional record.
A Gaussian state here commutes with fermion parity; it need not be supported
in the even parity sector. The odd pure Slater state

    psi=(|01>+|10>)/sqrt(2)

is Gaussian, while Phi(|psi><psi|)=rho*=diag(0,1/2,1/2,0).
Its occupations are1/2, cross and anomalous contractions vanish, but
<n1 n2>=0 instead of Wick's1/4. Thus it is not Gaussian.

A fixed initially uncorrelated even Gaussian fermionic environment, any
quadratic parity-preserving joint unitary (including pairing), and partial trace
map Gaussian inputs to Gaussian outputs. One can see this without a dynamical
approximation: the unitary rotates Majoranas linearly, preserving Wick
factorization, and restriction selects a submatrix of contractions. Include all
ancillary fermionic modes in the environment. This model excludes external
classical mixing, intermediate measurement/feedback, bosonic conditional controls,
nonGaussian initial resources and initial correlations. It therefore cannot
implement Phi. Finite restrictions of an infinite quasifree bath obey the same
Wick argument when the assumed quasifree evolution/restriction exists; no
implementability theorem for arbitrary infinite Bogoliubov maps is inferred.

## 2. Sharp state separation, hence a channel/resource lower bound

Every two-mode parity-even Gaussian density has a Gaussian normal form with
independent occupations p,q in[0,1]. Its diagonalizing even unitary preserves
parity and leaves rho*=I_odd/2 invariant, including in the pairing case.
The odd-block eigenvalues can be written a=p(1-q), b=(1-p)q. Therefore

    T(rho*,sigma)=1-min(a,1/2)-min(b,1/2),
    sqrt(a)+sqrt(b)<=1.                                  (1)

The second assertion is Cauchy for (sqrt(p),sqrt(1-p)) and
(sqrt(1-q),sqrt(q)). Assume a>=b. If a>=1/2, then
b<=(1-sqrt(a))^2<=(1-1/sqrt(2))^2. If a<=1/2 and a<=1/4,
a+b<=1/2. In the remaining range1/4<=a<=1/2,
a+b<=a+(1-sqrt(a))^2, an increasing function on this range.
Thus in all cases the capped sum in(1) is at most2-sqrt(2).
The product state with p=1/sqrt(2), q=1-1/sqrt(2) saturates:

    inf_Gaussian_sigma T(rho*,sigma)=sqrt(2)-1.             (2)

No optimization over samples replaces this proof. Consequently any channel
in section1 has half-diamond distance from Phi at least sqrt(2)-1, already
witnessed without a reference. The same lower bound applies to its recorded
instrument after forgetting the record, if that instrument has such a marginal.
State-distance sharpness does NOT prove optimal channel-distance sharpness.

If the actual fixed bath tau is within trace distance delta of a Gaussian
bath tau_G on the same apparatus, contractivity under the same unitary/trace
makes the two output channels at most delta apart in half-diamond norm.
Triangle inequality therefore gives

    epsilon >= max(0,sqrt(2)-1-delta).                     (3)

Equivalently the distance of tau to the Gaussian set is at least
sqrt(2)-1-epsilon for an epsilon-accurate implementation within this model.
This is a resource necessity, not a sufficiency theorem or work/energy cost.

## 3. Random quadratic phases are a real scope-changing counterroute

Do not extend(2) to arbitrary convex mixtures of Gaussian channels. Define

    W=exp[i*pi*(n_g-n_f)/2]=diag(1,i,-i,1),
    Psi=(id+Ad_W)/2.

For every parity-commuting system density, Psi equals Phi exactly: it preserves
the entire even block, dephases the odd offdiagonal, and fixes populations.
In particular it produces the nonGaussian rho* from the Slater witness.
External classical randomness is an extra resource absent from section1;
a nonselective number measurement also need not preserve Gaussian states.
This construction supplies no input-dependent readable E/F record: its random
choice is independent of the input. It is not K2090's complete instrument.

On the FULL two-mode matrix algebra, no mixture of Gaussian unitaries equals
Phi. Write R=2E-I and Phi=(id+Ad_R)/2. The rank-two Choi support is span{I,R},
so every nonzero unitary Kraus in any mixture lies there (positivity forces
zero support on its orthogonal complement). Such a unitary is diag(z,z0,z,z).
Every even two-mode quadratic unitary has equal determinants on even and odd
parity blocks: the traces of its quadratic Hamiltonian on those blocks agree,
and determinant multiplicativity preserves this identity under products.
Thus z^2=z0*z, requiring z0=z. Only scalar I remains, inconsistent with rank2.
The argument also applies to continuous mixtures almost everywhere.

There is no contradiction: local even-state agreement does not determine the
full extension. A fermionic reference can expose it on a TOTAL-even state:
(|00>_S|0>_R+|01>_S|1>_R)/sqrt(2). Phi kills its cross term, whereas Psi
multiplies it by (1-i)/2. The output trace distance is1/(2sqrt(2)).
A locally parity-even system with a bosonic reference does not expose that
particular odd system direction. Operational algebra and reference must be stated.

## 4. Consequence, checks and prior art

K2089's smooth quadratic transfer remains valid, but composing only fixed
Gaussian fermionic resources cannot finish the coarse readout. K2090's bosonic
controlled-number flags are outside that class; their locality remains open.
Use the exact random-phase counterroute only for its unrecorded even-algebra
scope. The next apparatus construction must declare its nonGaussian/hybrid
resource, readable record and operational algebra before invoking this bound.

The exact probe checks the CAR witness/Wick defect, saturating product state,
parity-block phase determinants, every even matrix unit for Psi and the total-even
reference counterexample. Mutants change state, channel, or pulse phases, never
the predicate. Universal Gaussian normal form and closure are standard background;
the explicit optimizations above carry the claimed bounds. See Sergey Bravyi,
[Lagrangian representation for fermionic linear optics (2004)](https://arxiv.org/abs/quant-ph/0404180).
No novelty is asserted; finite checks are separate from the written universal proof.
