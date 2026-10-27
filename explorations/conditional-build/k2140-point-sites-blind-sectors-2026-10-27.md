---
title: "K2140: Point-site blind modes and two-site observability"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: one-dimensional conditional model; no finite-time control or parity construction
scripts:
  - tests/channel-swings/k2140_point_sites_blind_sectors_probe.py
---

# K2140: Point-site blind modes and two-site observability

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
result: K2140: Point-site blind modes and two-site observability
carrier: massive scalar L2(R,dk) one-particle space, bosonic Fock space and independent finite memory LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert and recorded-channel diamond norm ON=declared_carrier
real_structure: complex adjoint and spatial reflection
grading: boson occupation parity, no GU grading identification
action_owner: repository-construction -- K2136 point interaction protocols and their free spectral orbit
target: microscopic blind factor, full record distance and complex cyclic density MAP-TYPE=intertwiner
```

## 1. The physical point model has an exact blind sector

The nonzero response in [K2136](k2136-point-probe-recorded-field-2026-10-27.md)
is for a specifically selected even wavepacket. It does not measure arbitrary
one-photon inputs. For a source fixed at x=0, h(k), ω(k) and every switched
source displacement are even in k. Thus

    h_one=h_even direct-sum h_odd,
    Fock(h_one)=Fock(h_even) tensor Fock(h_odd).        (1)

Free evolution preserves both summands. The source Hamiltonian as a closed
form, its exact propagator, and any memory-only gates/readout act on the even
factor and memory only. Independent initialization of the apparatus is
required; it cannot already contain a copy of the tested input. Hence every
well-defined composition of these operations, including adaptive memory
operations, has the exact full recorded form

    J=J_even tensor Ad(U_free,odd).                   (2)

Protocols are compared at a common total elapsed output time. Feedback may
vary source coupling and memory controls, but does not introduce branch-dependent
free field rotations or adaptive output times. No pulse-count or duration bound
is used. Channel limits are taken after removing that common free evolution;
any such strong limit retains the same blind factor. For a source
at x0 use reflection about x0, equivalently translate the even/odd subspaces.
No bosonic parity superselection assumption is imported.

Choose a normalized odd u of finite energy, for example a normalized
k exp(-k²) wavepacket. On the code {Ω,1_u}, the record distribution is
input-independent. The odd excitation only evolves freely. This is a
structural apparatus obstruction, not a numerical zero at a selected pulse.

## 2. Sharp complete-instrument floor, not just wrong probabilities

Remove the common free output evolution. Trace out the even field output;
by(2) the actual channel becomes q_R tensor id_code. The ideal instrument is

    L(ρ)=|0><0|_R tensor P0ρP0+|1><1|_R tensor P1ρP1.

Allow any binary coarse-graining of the actual record and put q=q_R(0).
For the input |+>=(|0>+|1>)/sqrt2 the half trace distance is

    [sqrt(q²+1/4)+sqrt((1-q)²+1/4)]/2 >=1/sqrt2.      (3)

Each record block is a2x2 Hermitian matrix with determinant -q/4 or
-(1-q)/4, respectively; its trace norm is the corresponding square root.
Convexity/symmetry gives the minimum at q=1/2. Trace contraction proves this
is also a lower bound on the FULL field-plus-record half-diamond distance,
with arbitrary references allowed.

The fair random record and identity field channel attain1/sqrt2, by the
exact two-sector instrument calculation in
[K2133](k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md).
It can be realized here by zero field coupling and fair local readout.
Thus1/sqrt2 is sharp over this blind apparatus class. Reusing that distance
calculation is explicit: the new theorem is the actual microscopic
factorization forcing this class. If all coherence between the two occupation
sectors, including reference-assisted coherence, is forbidden, the restricted
optimum is1/2 instead. Neither restriction is assumed in(3).

## 3. Two distinct sites remove the exact complex blind subspace

Let b(k) be any even L2 seed nonzero almost everywhere, such as a nontrivial
triangular K2137 displacement. Its discrete frequency zeros have measure0.
For sites x1,x2, consider the **complex closed span of the all-time free
orbits** e^(itω)b_x, t in R, where b_x(k)=exp(-ikx)b(k).
This is an accessibility diagnostic, not a real-control reachable set.

Decompose k>0 into the two-dimensional frequency fiber (u(k),u(-k)).
The normalized angular site vectors are

    v_x(k)=(exp(-ikx),exp(ikx))/sqrt2.

For separation d=x2-x1≠0 the two-column determinant is i sin(kd), nonzero
almost everywhere. To prove density, suppose u is orthogonal to both
all-time orbits. Products of u with b are integrable by Cauchy--Schwarz.
Uniqueness of the Fourier transform of the resulting finite frequency
measures forces orthogonality to both fiber columns almost everywhere.
Invertibility there gives u=0. A single site instead has a one-dimensional
orthogonal fiber at almost every k, exactly the translated odd sector.

The two-site normalized angular frame eigenvalues are

    1+|cos(kd)|, 1-|cos(kd)|.                         (4)

The lower eigenvalue has essential infimum0. Wavepackets concentrated near
kd in πZ show no uniform bounded inverse, even though no nonzero L2 blind
state remains. On a compact shell separated from those zeros there is a
positive angular lower bound; the radial seed weight also needs a separate
lower bound for quantitative source inversion. The determinant's discrete
zeros cannot be turned into normalizable exactly blind states, but their
neighborhoods are genuine ill-conditioning.

Nothing here supplies finite-time real switching reachability, a complete
parity instrument, a resource bound, or nonlocal instantaneous communication
between separated memories. Two independent local probes retain their own
causal cones; a combined record needs physical communication. Moreover all
finite controlled-Weyl concatenations still obey
[K2139](k2139-finite-weyl-record-obstruction-2026-10-27.md), even with two sites.
Removing spatial blindness does not remove the algebraic exact-darkness limit.

## 4. Dimension boundary and next useful test

As a spectral statement, in spatial dimension d>=2 a finite set of point
vectors spans at most N dimensions on each sphere |k|=r, whereas L2(S^(d-1))
has infinite dimension. A radial nonzero square-integrable cutoff makes the
seeds genuine Hilbert vectors; an orthogonal angular subspace then persists
for almost every radius. This is a separate REGULARIZED spectral observation.
K2136's closed semibounded point-Hamiltonian construction cannot simply be
ported: its form condition contains ∫d^dk/ω(k)², which diverges for d>=2.
No stable singular higher-dimensional point apparatus is claimed.

The next useful apparatus attempt therefore needs both a nonblind mode
interface on its declared code and a protocol outside the finite-Weyl
exact-dark class, or an honest approximate certificate that includes complete
record, time, energy, preparation and inversion constants. Infinite-time
complex density alone is not such a certificate.

## 5. Acceptance and ceiling

The probe checks the exact fiber matrices/determinant, coincident-site
countercontrol, singular-value formula, record trace-norm formula and fair
record saturation inherited from K2133. Universal Fock factorization and
cyclic-density arguments are written proofs, independently internally
reviewed. It never infers continuum causality from a momentum cutoff or a
finite matrix. Finite checks and genuine altered-input controls are reported
separately from those proofs; no external review or proof assistant.

SC-OP-04 ASSERTS candidate operator grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN, SC-META-56 DISAVOWS an odd-action prerequisite. This supplied
positive-Hilbert scalar model changes no source polarity, LT-SM8/LT-GR6b
verdict, ledger0.263, canon or GU recovery claim. Bosonic occupation parity,
spatial reflection and native GU grading are distinct objects throughout.
