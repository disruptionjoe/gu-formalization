---
title: "K2084: Endpoint convergence and the shrinking-root obstruction"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2084_continuum_instrument_limit.py
  - tests/channel-swings/k2084_continuum_instrument_limit_probe.py
---

# K2084: Endpoint convergence and the shrinking-root obstruction

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
result: ancilla-uniform instrument convergence, funnel limit obstruction and localization resource bound
carrier: fixed L2 R3 complex massive Dirac1408 and its CAR algebra LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: supplied positive Hilbert metric ON=declared_complex_completion
real_structure: inherited pointwise antiunitary C with C squared plus or minus identity
grading: fermion parity separate from energy sign
action_owner: repository-construction -- imported free generator and finite graph control model
target: complete instrument approximation and resource limits MAP-TYPE=intertwiner
```

[Conditional mathematical result; accepted after independent internal specialist review. No external or proof-assistant certification.]

## 1. The limit being tested

[K2081](k2081-causal-instrument-realization-2026-10-26.md) implements a whole
single-mode instrument on each finite graph and gives mesh-independent duration.
[K2082](k2082-charge-conjugate-detectors-2026-10-26.md) supplies its paired coarse
version. Here prove convergence of their endpoint operations in a fixed CAR
algebra, then test the actual funnel rather than infer a continuum apparatus.
This is a quantitative application of CAR norm continuity, not a novelty claim.
SC-OP-04 ASSERTS candidate operator grammar, OP-05 and META-53 are UNCERTAIN,
and META-56 DISAVOWS the odd-action prerequisite. LT-SM8/GR6b remain unchanged.

Let H=L2(R3,C1408), with the fixed positive metric already isometrically normalized.
For a bounded box containing normalized compact f, let P_h be orthogonal projection onto
piecewise constant cells with maximum diameter tending to zero, acting identically
on internal components. Cell averages converge to f in L2: prove for continuous
functions by uniform continuity, then use density and ||P_h||<=1. Normalize
f_h=P_h f/||P_h f|| for sufficiently small h. Write delta_h=||f_h-f||.
If e_h=||(I-P_h)f||, then delta_h<=2e_h. No claim of approximation outside
the fixed box is made. These cell functions need not be in the energy domain.

## 2. Complete instruments, uniformly over ancillas

CAR gives ||a(u)||=||u||. For unit f,g,

    ||n_f-n_g|| <= 2||f-g||,   n_f=a*(f)a(f).

For any two projections P,Q, define the flagged Schrödinger instrument

    I_P(rho)=P rho P tensor |1><1|+(I-P)rho(I-P) tensor |0><0|.

For trace-class X on system plus arbitrary ancilla, expand
PXP-QXQ=(P-Q)XP+QX(P-Q). Each branch has trace norm at most
2||P-Q|| ||X||_1. The two orthogonal output blocks add. Thus

    ||I_P-I_Q||_diamond <= 4||P-Q||,
    ||I_(n_fh)-I_(n_f)||_diamond <= 8delta_h.          (1)

The same statement is intrinsic as a completely bounded Heisenberg estimate
on CAR with a classical output register. A common representation is needed
for the trace-class version; no equivalence of varying regulator GNS spaces
is assumed. Ancilla amplification does not change any multiplication norm.

For exactly orthogonal f,Cf put E_f=I-(I-n_f)n_Cf. If f_h perpendicular C f_h,
then both number projections commute and E_fh is a projection. Product expansion gives

    ||E_fh-E_f||<=4delta_h,
    ||I_(E_fh)-I_(E_f)||_diamond<=16delta_h.           (2)

C-stability of a projection alone does NOT preserve orthogonality when C²=+I:
f=(e1+i e2)/sqrt2, C=conjugation, projected onto span(e1), is a counterexample.
Use the untouched orthogonal multiplicity factors of K2082, with P_h spatial
only; this also preserves zero sea cross covariance. For C²=-I ordinary pair
orthogonality is automatic, though the covariance property still needs its
stated multiplicity construction. No refined measurement is substituted for
the coarse binary instrument.

## 3. A genuine obstruction to the proposed funnel limit

Extend each finite one-particle funnel unitarily by identity on the orthogonal
complement of its embedded cell space. It obeys U_h f_h=r_h, where r_h is the
normalized root cell mode. Its support measure tends to zero. For every v in H,

    |<v,r_h>| <= ||1_(supp r_h) v|| ->0.

Thus r_h tends weakly to0 but has norm1 and no strongly convergent subsequence.
If U_h converged strongly, uniform boundedness and f_h->f would force
U_h f_h->Uf strongly, a contradiction. This excludes a strong limit of this
particular shrinking-root funnel; it does not exclude all continuum apparatuses.

Nevertheless U_h* |r_h><r_h| U_h=|f_h><f_h| converges in norm, and(1)--(2)
show convergence of the corresponding full CAR endpoint instruments. Singular
intermediate transport and convergent endpoint channel are compatible.
A limit of generators cannot be inferred from the bounded circuit duration.

## 4. Mean absolute energy, not only RMS

For any normalized vector-valued psi supported in a measurable set of diameter
at most ell in R3, volume is at most ell³. With unitary Fourier normalization,
Cauchy-Schwarz gives ||psi_hat(p)||²<=ell³/(2pi)³. Therefore

    integral_(|p|<=1/ell) ||psi_hat(p)||² dp <=1/(6pi²).

For the free massive Dirac generator D of this declared completion,
|D|=sqrt(-Delta+m²)I. Its extended positive expectation satisfies

    <|D|>_psi >= (1-1/(6pi²))/ell >1/(2ell).         (3)

Infinite expectation is allowed. For smooth compact roots in an ell-wide slab,
one-coordinate Dirichlet Poincare separately gives

    ||D psi||² >= m²+pi²/ell².                      (4)

Do not use(4) alone to infer a mean-energy bound: mean and RMS differ. Signed
<D> can cancel between energy signs. Neither(3) nor(4) is a theorem about
sea-vacuum excitation energy or total apparatus work. A piecewise constant
cube root is outside H1 and even has infinite <|D|> by its sinc-squared tails;
its bounded CAR effect remains valid. A physically smooth realization requires
separate energy-domain control.

## 5. Useful repair and a quantitative resource tradeoff

Keep a root region of fixed diameter ell>0, or use distributed records, rather
than concentrating every regulator into one vanishing cell. This removes the
specific weak-to-zero obstruction but does not construct a causal apparatus.
If a protocol actually transports a normalized one-particle wavefunction into
that region while imposing <|D|><=W, (3) requires ell>1/(2W).
Together with K2081, a record centered at x with radius ell_r and duration T
obeys record TV error >=||1_(outside B(x,ell_r+vT))f||²/2 under its explicit
strict-causality hypothesis. Thus spatial concentration, collection time and
accuracy cannot be discarded independently; ell (support diameter) and ell_r
(record radius) are distinct quantities. No total-work lower bound is claimed.

A repair by replacing every cell indicator with one fixed-shape smooth bump
is inadequate: on a unit cell let ||phi||2=1, c=integral phi. The projection
of a constant onto tiled rescaled copies retains only fraction |c|² of its
squared norm. If phi is not constant, |c|<1 and this error persists as h->0.
In one dimension phi=sqrt(2)sin(pi x) (smooth on the open cell and H1_0 after extension) gives |c|²=8/pi²<1. Use boundary layers
whose relative volume tends to zero or a richer approximation space, and then
prove graph/energy estimates. Endpoint L2 convergence does not grant those.

## Verification and next decision

The independent exact finite probe checks CAR projections, flagged branches
with ancilla, paired orthogonality and paired coarse projection bounds. Fourier
and Poincare arguments above carry the continuum statements; matrices do not.
Next compare an explicit fixed-radius/distributed causal apparatus with the
state-selection and thermal certificate frontiers. Do not repeat larger
finite funnels as evidence for a strong continuum limit.
