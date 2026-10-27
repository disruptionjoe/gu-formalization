---
title: "K2139: Finite Weyl protocols and exact dark-record limits"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite Weyl circuit theorem; no exclusion of arbitrary detectors or GU
scripts:
  - tests/channel-swings/k2139_finite_weyl_record_obstruction_probe.py
---

# K2139: Finite Weyl protocols and exact dark-record limits

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
result: K2139: Finite Weyl protocols and exact dark-record limits
carrier: bosonic Fock space over a complex one-particle Hilbert space, finite memory and classical record LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: operator adjoint
grading: boson occupation, not native or fermion parity
action_owner: repository-construction -- finite controlled displacement pulses, memory gates, and recorded readout with supplied preparation
target: whole finite protocol class and fixed displacement-path probability ratio MAP-TYPE=intertwiner
```

## 1. Test the actual construction class before adding pulses

[K2136](k2136-point-probe-recorded-field-2026-10-27.md) supplies stable causal
point-memory dynamics with non-Gaussian records. This does not by itself
supply ideal parity. Here finite compositions of its controlled displacements,
finite-dimensional memory-only gates, free field evolution and readout have
an exact algebraic limitation even without locality: a click that is exactly
dark on the vacuum is dark on every state. The statement covers full recorded
instruments, not merely the unread field channel.

Freeze a finite protocol with finitely many branches/outcomes. Purify a
finite-dimensional mixed memory if needed and include discarded memory
indices among the Kraus labels. Conditional free rotations may not be added:
all free field evolution is common to the branches and can be commuted to one
output rotation, replacing displacement arguments by their freely evolved
ones. All memory control and readout resources are supplied. Continuous
measurements, infinite pulse limits and new number-dependent interactions
are outside this class.

## 2. Finite path algebra and vacuum separation

Let D(z)=exp(a*(z)-a(z)). Weyl multiplication closes up to a scalar phase.
Expanding the finite memory paths therefore gives, after removing the common
free output rotation,

    K_r=Σ_(j=1)^N c_rj D(z_j).                        (1)

Merge identical arguments first, absorbing all Weyl phases into c_rj.
The vectors D(z_j)Ω for distinct z_j are linearly independent. For a direct
proof use exponential vectors e(z)=exp(a*(z))Ω and choose v such that the
finitely many complex numbers <v,z_j> are distinct. Such a v exists outside
finitely many proper hyperplanes. If Σ d_j e(z_j)=0, taking exponential-vector
matrix elements along tv gives Σ d_j exp(t<v,z_j>)=0. Its first N derivatives
at0 form an invertible Vandermonde matrix, so every d_j=0. Normalization of
coherent states is a nonzero scalar and changes nothing. This also works in
an infinite-dimensional one-particle space because only the finite span is
used. The standard fact is documented in Neumaier's
[Introduction to coherent quantization](https://link.springer.com/article/10.1007/s13324-022-00689-3);
the elementary proof above is the argument used here.

It follows that K_rΩ=0 implies K_r=0. For a click event with several Kraus
labels, p0=Σ_r||K_rΩ||²=0 forces every term to vanish. An exact ideal
vacuum-versus-one-photon record, or full occupation-parity instrument, is
therefore unavailable to every finite protocol in(1).

A stronger disturbance consequence follows. If the entire unread channel
preserves the pure vacuum, positivity forces every K_rΩ=c_rΩ. Adjoin z=0
to(1) and apply independence again: K_r=c_r I. Thus the channel is identity
and the record is input-independent (up to the common free rotation).
This is stronger in its particular circuit class than a locality argument;
it excludes exact vacuum-preserving information extraction even for nonlocal
finite displacements. It does not exclude photodetection, a parity coupling,
or another interaction not expressible as a finite Weyl sum.

## 3. A quantitative path-dependent discriminator

Fix a normalized u and the one-photon state |1_u>. Define Gram matrices

    G0_ij=<Ω,D(z_i)*D(z_j)Ω>,
    G1_ij=G0_ij (1-|<u,z_j-z_i>|²).                  (2)

With <z_i,z_j> conjugate-linear in its first slot,
G0_ij=exp(i Im<z_i,z_j>) exp(-||z_j-z_i||²/2).
This convention follows D(x)D(y)=exp(-i Im<x,y>)D(x+y).
G0 is strictly positive for distinct paths; G1 is positive semidefinite as
a Gram matrix. Set

    R=λmax(G0^(-1/2)G1G0^(-1/2)).                    (3)

For every click event assembled from this fixed path span,

    p1<=R p0.                                       (4)

Indeed each Kraus contributes c*G1c<=R c*G0c, and sums preserve the inequality.
Thus simultaneous vacuum false-click and one-photon miss errors at most ε
require ε>=1/(1+R). This lower bound also applies to full recorded-channel
error on the frozen code because record probabilities are contractive tests.
It is not claimed sharp for the whole instrument or even for simultaneous
probability errors. R itself is the sharp likelihood-ratio constant over
the operator span: a maximizing generalized eigenvector gives a nonzero
finite Weyl sum, which can be rescaled to a contraction without changing its
ratio. Completing that contraction abstractly is not a proof that the
complement Kraus is in the finite circuit class.

## 4. Two paths and the nonuniform-complexity countercontrol

For z=±sqrt(a)u, a>0, G0 has off-diagonal b=exp(-2a), and G1 off-diagonal
(1-4a)b. They have common symmetric/antisymmetric eigenvectors, giving

    R_plus=1-4a/(exp(2a)+1),
    R_minus=1+4a/(exp(2a)-1), R=R_minus<3.            (5)

Consequently ε>1/4 is necessary for a fixed nonzero two-path alphabet.
The weak-pulse limit R->3 still cannot give zero simultaneous error. This
is a class result for the fixed alphabet, not just K2136's chosen memory
readout. The exact probability contrast of that original readout remains
as recorded in K2136.

There is no path-independent bound on R as the finite alphabet grows.
For integer n>=1 and real ε≠0, take the contraction

    L_(n,ε)=2^(-n)(D(εu)-I)^n.                       (6)

Its n+1 distinct paths are jεu. On vacuum and one photon, the spectral theorem
for Q=a*(u)-a(u) and |exp(ix)-1|<=|x| show, by dominated convergence of the
finite Gaussian quadrature moments,

    ||L_(n,ε)1_u||² / ||L_(n,ε)Ω||² -> 2n+1.         (7)

Specifically iQ has vacuum variance1 and one-photon density x² times the
vacuum standard-Gaussian density; moments are (2n-1)!! and (2n+1)!!.
This proves R is unbounded across path alphabets. Both probabilities tend
to zero in this example, so it is **not** a near-ideal detector construction.
An arbitrary finite pulse count can evade a uniform ratio cap while still
obeying the exact darkness theorem. Infinite limits require separate domain,
resource and complete-instrument analysis.

## 5. Acceptance and next decision

Exact symbolic checks cover Vandermonde separation, Weyl characteristic
functions, positive two-path Gram structure, the generalized eigenvalue
formulas, finite-difference cancellation and the moment ratio. The universal
finite-circuit and infinite-dimensional statements use the written proofs,
independently internally reviewed. Faults change phases, input matrix
elements, path separation and normalization, not check predicates.

This closes an exact construction-class question and gives a usable
path-dependent approximate test. Next compare a number-dependent/local
interaction or an infinite-limit protocol with an explicit error/resource
certificate. Adding a second site alone cannot evade the finite-Weyl
algebraic obstruction, although it removes a different blind-mode obstacle
in [K2140](k2140-point-sites-blind-sectors-2026-10-27.md).
SC-OP-04 ASSERTS candidate grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN;
SC-META-56 DISAVOWS an odd-action prerequisite. Source, LT-SM8/LT-GR6b,
ledger and canon unchanged. This boson model is neither GU's physical quotient
nor the earlier fermionic parity target; no novelty or external acceptance.
