---
title: "K2230 Time-dependent same-pairing obstruction and a massive transported observation"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional fixed-gamma time-dependent pairing obstruction and supplied massive raw lift; no source action, physical quotient or family inference
scripts:
  - tests/channel-swings/k2230_time_dependent_pairing_compatibility_probe.py
---

# K2230 Time dependence does not repair the optional same-pairing condition

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
result: time-dependent compatibility obstruction and all-row massive transported observation
carrier: real128 Cl77 spinor parent and supplied sum-zero V1152 on R time x R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: arbitrary nonsingular spinor G in theorem; original B trace pairing and distinct positive reduced L2 current in construction ON=declared_carrier
real_structure: ordinary conjugation in the fixed real Clifford basis
grading: fixed Clifford blades; no physical chirality or family interpretation
action_owner: repository-construction -- optional common-pairing requirement and supplied raw coefficients
target: time-dependent connection compatibility and propagated observation MAP-TYPE=intertwiner
```

## Preflight: rerank the exact gap and the strongest repair

The operational demand is conservative massive evolution with a genuinely
moving local observation. The candidate uses K2221's enlarged raw coefficient
class; it does not reconstruct a source action. Layer 0 separates connection
parallelism, an algebraic normal trace test, a reduced positive current and
source observation. They are different objects unless a bridge is proved.
T02/T04/T10/T11/T15/T16 remain operative; the septuple substrate/no-go template
is not a claim that this internal coefficient calculation supplies a new
chirality substrate candidate.

K2227 leaves time-dependent K outside its static temporal theorem. Three
routes were reranked: (i) use arbitrary time derivatives to cancel its static
obstruction; (ii) allow arbitrary nonsymmetric invertible G rather than a
special B anchor; (iii) retain the two distinct predecessor pairings and
construct a massive moving observation with its necessary temporal term.
The first two are settled together below; the third survives explicitly.

Local predecessor search also found K1879 and K2124: a time-dependent frame
requires its time-connection term, and transported propagators are already
known mechanisms. The incremental construction here is their realization
with K2221's grade12 raw lift, all fifteen original rows and unchanged lower
returns on V1152. K2126 is an all-grade obstruction on a different selected32
carrier and common-H upper class; it does not exclude this enlarged V1152
construction. No novelty claim follows from this local search.

## 1. Exact temporal equations with variable coefficients

Use the fixed real matrices of K2221--K2227:

    B=gamma7 ... gamma13, A=gamma0 J,
    T=product of the ten normal gammas,
    Cj=gamma0 gamma_j, Xj=Cj T, j=7,8,9,
    V(t,x)=sum a_j(t,x) Xj, K(t,x)=m(t,x) A+V(t,x).

A and Xj are real-transpose skew, square to -I and mutually anticommute.
B is a symmetric involution, commutes with A and anticommutes with Xj.
Every fixed invertible normal gamma conjugates K to Kbar=mA-V.
Let m,a be real C1 coefficients; allow arbitrary spatial connection
components. Suppose a C1 nonsingular real spinor pairing G satisfies BOTH

    G_t=K^t G+G K=[G,K],
    K^t G gamma_r+G gamma_r K=0.                         (1)

One fixed invertible normal gamma is sufficient. The second equation is
the optional SAME-G coefficient trace condition, not a differential Green
identity, not the derivative of G gamma_r, and not an established source
requirement. It is equivalent to

    G Kbar=K G.                                          (2)

Differentiating gives the actual variable-coefficient identity

    G Kbar_t-K_t G+G[K,Kbar]=0.                          (3)

Dropping the first two terms would incorrectly reuse the static proof.
Nevertheless they cannot cancel the obstruction in this fixed Clifford class.

## 2. Polar normalization proves m(t,x)V(t,x)=0

Fix x and put H=GB. Equations (1)--(2) become

    [H,K]=0,             H_t=-2 H V.                    (4)

Because V^t=-V, P=HH^t has P_t=0. P is positive definite since H is
nonsingular. Transposing [H,K]=0 and using K^t=-K shows that H^t, hence P,
commutes with K. Its positive square root also commutes with K. Therefore

    Q=P^(-1/2) H

is orthogonal, commutes with K and satisfies Q_t=-2 Q V. P may depend on x;
it is constant in t, which is all the proof needs. Differentiating [Q,K]=0
and multiplying by Q^-1 gives

    Q^-1 K_t Q=K_t+2[K,V]=K_t+4m A V.                   (5)

The ordinary Frobenius norm is invariant under this orthogonal conjugation.
K_t lies in the four-vector span {A,X7,X8,X9}; AV lies in its Clifford
bivector span. These spaces are Frobenius-orthogonal in the faithful real128
representation. Explicitly, the relevant trace products are zero; moreover

    ||AV||_F^2=128 sum a_j^2.

Taking squared norms in (5) yields

    0=16 m^2 ||AV||_F^2=2048 m^2 sum a_j^2.             (6)

Hence mV=0 pointwise. Wherever m is nonzero every a_j vanishes. This proof
allows arbitrary time and space dependence, arbitrary invertible nonsymmetric
G, and arbitrary spatial connections; no spatial equation was used. For
everywhere nonzero m it excludes every nonzero flavor profile under (1).
At zeros of m it asserts only mV=0; sufficiency or arbitrary gluing across
zero-mass regions is not claimed. Singular G is outside the polar argument.

The ordinary positive form in this proof is a finite-dimensional auxiliary
norm, not a physical positivity assumption on G. No signature restriction
on G has been introduced. The simpler symmetric-G proof is a useful control:
m[G,A]={G,V} has symmetric left side and skew right side, so both vanish;
on an open nonzero-mass interval differentiating [G,A]=0 forces V=0.
The polar proof is needed to cover nonsymmetric G as well.

## 3. Constructive surviving branch: massive moving observation, distinct pairings

Remove only the optional identification of the trace pairing with a parallel
pairing. Keep the numerical raw D_k, all original returns, the B trace test,
the positive reduced current, and constant nonzero m. Let theta(t,x7) be C2
with bounded first derivatives on finite time intervals. Set

    Omega0=m A+theta_7 X7, Omega7=theta_t X7,
    Omega_k=0 otherwise, U=exp(theta T).

Every Omega is ordinary-transpose skew, so G_parallel=I is parallel for
this raw connection. Every component also obeys

    Omega_k^t B gamma_r+B gamma_r Omega_k=0

for every normal r. B is generally not parallel; I generally fails the
normal trace test. Those are two explicitly distinct parent pairings.
The theorem says they cannot be replaced by one nonsingular G wherever
m theta_7 is nonzero while retaining the same fixed normal gammas.

All fifteen original raw rows preserve the predecessor sum-zero V1152.
For a normal-slot difference c minus c0, using R_c=eta_c gamma_c,
R_h=Wbar and inverses gamma_c,W/2, the mass term contributes

    -gamma0 Wbar mA (delta_row,c-delta_row,c0),

and a term Omega_k=b X7 for any observed k contributes

    +gamma_k Wbar bX7 (delta_row,c-delta_row,c0).

The actual bottom return remains D_k[14,k] Omega_k=-eta_k Omega_k.
These are raw matrix identities, not a refit from the desired reduced
equation. The resulting equation is

    Etheta u=0,
    Etheta=partial_t+sum Cj partial_j+N,
    N=m A-theta_7 X7-theta_t T.                         (7)

The new -theta_t T comes from the SPATIAL raw Omega7; using T directly
as a raw component would fail the original B trace test. N^t=-N, so
the positive density and flux satisfy

    partial_t(u* u)+sum partial_j(u* Cj u)=0.            (8)

T commutes with every Cj and A. Product differentiation therefore proves

    Etheta=U E0 U^t, E0=partial_t+sum Cj partial_j+mA.   (9)

This is covariance of the reduced V1152 equation. Some full raw D_k do
not commute with T; no full raw frame covariance is asserted.

## 4. Actual propagated projector, temporal failure control and domains

Let E=(I+gamma1)/2 on each spinor copy, and P(t,x)=U E U^t. It is a real
orthogonal projector of spin-rank64 and V-rank576, commuting with Cj and A.
It satisfies the full time-dependent reducing equation

    P_t+sum Cj P_j+[N,P]=0.                             (10)

Thus initial data in Ran P(s) evolve into Ran P(t). Checking only the
instantaneous spatial commutator is insufficient. If the -theta_t T term
is omitted while theta_t is nonzero, the residual in (10) is
theta_t[T,P], which is nonzero for this projector. This is the concrete
failure of the naive time-dependent extension of K2221's static projector.

For theta and its first derivatives smooth and bounded on finite time
intervals, U(t) is unitary on L2 and preserves H1. With
H0=-i sum Cj partial_j-i m A, the exact propagator is

    W(t,s)=U(t) exp(-i H0(t-s)) U(s)^t.                 (11)

The actual instantaneous Hamiltonian is

    Htheta(t)=U(t) H0 U(t)^t+i theta_t T.

Its last term is Hermitian. Formula (11) establishes unitary evolution,
real-data preservation and the propagated projector on the common H1 domain.
No static spectral equality is inferred from a time-dependent unitary
frame. In particular instantaneous energy and a selected positive-energy
observation are different claims. The rank576 observation still contains
both frequency signs of the free massive reference system.

A global nonconstant example is theta=epsilon sin(t) sin(x7), epsilon!=0.
All its relevant derivatives are bounded. Its effective spacetime connection
-dtheta T is flat, but the raw curvature is

    F07=(theta_tt-theta_77)X7+2m theta_t A X7
       =2m theta_t A X7,

which is nonzero on open sets. This supplies a useful exact control against
identifying raw and effective curvature. It is not a physical curvature or
source-geometry statement. Nonconstant phase and nonzero mass have been
supplied; they were not dynamically selected.

## Hostile postflight: strongest false claims and weakest seam

The strongest false negative is that a time-dependent massive flavor model
is impossible. Section 3 constructs one with all original raw rows and
current, while keeping B-trace and parallel-I roles distinct. The strongest
false repair is that coefficient time derivatives evade the optional same-G
obstruction: the positive norm defect (6) excludes that claim. Singular
pairings, moving numerical gammas/principals, a larger raw-slot pairing and
a different trace/action condition remain outside the theorem.

The weakest algebraic seam is normalizing an arbitrary nonsymmetric H:
P_t=0 and [P,K]=0 must BOTH hold before using a time-independent square root.
The weakest construction seam is omitting the temporal compensator or
silently calling reduced covariance full raw covariance. Exact controls
test the positive norm defect with independent mass/flavor jets, all raw
rows and bottom returns, original B trace versus parallel I, moving
projector conservation, the omitted-term failure, and raw/effective curvature.
Genuine faults alter the differentiated commutator, norm identity, temporal
coefficient, trace lift, bottom return, coefficient order or curvature term.
Universal polar, transport and domain arguments remain distinct evidence
from finite exact sparse-Clifford controls.

SC-OP-04 remains ASSERTS at candidate four-field grammar strength; SC-OP-05 and SC-META-53 remain
UNCERTAIN. There is no source requirement for the optional same-G premise,
no selected physical quotient, empirical or family credit, source verdict,
ledger change, canon promotion, external-expert, proof-assistant or novelty
certification. Next useful work must change a named premise or provide a
source-selected interpretation of the already distinct pairings, rather than
repeat temporal or arbitrary-spatial repair within the excluded class.

## Reproduction and evidence boundary

The [exact probe](../../tests/channel-swings/k2230_time_dependent_pairing_compatibility_probe.py) checks finite algebra and rational consumers; universal statements rely on the written proofs above. Run the probe with the repository Python environment. Its default run regenerates controls in memory and rejects a stale [certificate](../../lab/process/k2230-time-dependent-pairing-compatibility.json); `--write` refreshes that report. Note, probe and reused dependency hashes bind the report. Each planted fault changes mathematics or a supplied input and must fail an unchanged check after a green baseline. Internal independent review is not external-expert or proof-assistant certification.
