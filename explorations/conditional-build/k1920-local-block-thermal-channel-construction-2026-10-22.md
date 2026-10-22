---
title: "K1920: Local circuits retain collective thermal advantage"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1920_local_block_thermal_channel_construction.py
  - tests/channel-swings/k1920_local_block_thermal_channel_construction_probe.py
---

# K1920: Local circuits retain collective thermal advantage

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
result: blockwise thermal approximation with logarithmic block size and nearest-neighbor circuit bounds
carrier: four-level system and qutrit bath at each of N sites LAYER=toy CHIRALITY=N/A
pairing: positive trace pairing, diamond norm and Gibbs relative entropy ON=finite_tensor_product
real_structure: complex adjoint and positive Gibbs density; no native K/C map
grading: site and bath energy labels only
action_owner: repository-construction -- arbitrary controlled local gates, no energy conservation restriction
target: collective correlation channel implementation and resource upper bounds MAP-TYPE=intertwiner
```

## 1. A local realization, with its actual cost assumptions

[K1918](k1918-collective-thermal-preparation-threshold-2026-10-22.md) supplies
optimal spectral retained masses p_b and arbitrary endpoint unitaries for b
copies of the four-level extreme rank-two channel C. This note constructs a
block implementation on a chain, using the ORIGINAL faithful product qutrit
Gibbs state. No pure flag, clean ancilla, cooling or measurement is inserted.
Each physical site comprises its four-level system and three-level bath;
we allow arbitrary one-site U(12) and adjacent two-site U(144) gates.
These gates can mix system populations during execution and need not conserve
energy. The final channel alone approximates the specified dephasing target.
This is a strong externally supplied control model, not a bath Hamiltonian
derived from GU, a fixed-depth circuit or an experimental design.

For N=mb, independently operate the b-site blocks. Their endpoint channels
have the exact decomposition

    Psi_b=p_b Phi_C^(tensor b)+(1-p_b) R_b.

Consequently the full channel has target weight P=p_b^m and

    half-diamond(Psi_b^(tensor m),Phi_C^(tensor N))
       <=1-p_b^m<=m(1-p_b).                          (1)

Unlike a single-site error statement, this controls the entire N-system
channel including arbitrary ancilla-entangled inputs. It follows by tensor
expansion into channels and the diamond distance bound2 between channels.
If one instead prepares the truncated bath separately on each block, its
TOTAL relative entropy is-m log p_b. This is an alternative preparation
resource, not a cost incurred by the unchanged-bath circuit.

## 2. Explicit block isometries and why no clean ancilla is hidden

Let s=floor(3^b/2^b), let |j>,j=1..s, be the b-qutrit basis vectors of
largest Gibbs weight, and let e_x in C^(2^b) be the tensor Gram vectors of
C^(tensor b). Since2^b s<=3^b, fix an orthonormal output set |alpha,j> in
that SAME bath Hilbert space. For each system word x define on the input
support

    V_x |j>=sum_alpha (e_x)_alpha |alpha,j>.

V_x is an isometry because ||e_x||=1. Extend its s columns to an orthonormal
basis to obtain a unitary U_x on the original bath. The joint controlled
unitary U=sum_x |x><x| tensor U_x exists on dimension12^b. The weighted
trace of U_y^*U_x over the retained support is p_b <e_y,e_x>, independent
of j, so feeding the full Gibbs state gives the displayed channel mixture.
Use the same Gram convention as K1912; conjugating every Gram vector changes
that convention consistently, not the underlying construction.
The labels alpha,j describe a subspace, not an extra tensor-factor ancilla
initialized in a pure state. The unused complement is completed unitarily.
At finite b the tail has nonzero weight and exact realization on a faithful
bath remains excluded by K1912; this is approximation only.

## 3. Convert the endpoint into nearest-neighbor gates

Treat system plus bath as a genuine12-level site. Brennen, Bullock and
O'Leary, *Efficient Circuits for Exact-Universal Computation With Qudits*,
Quantum Information and Computation6(2006),436-454, sections3-5, give
ancilla-free exact unitary synthesis with O(d^(2b)) two-qudit gates at fixed
d. [Primary paper](https://www.cs.umd.edu/users/oleary/reprints/j75.pdf).
Its hypotheses apply to the full12^b unitary above with continuous local
gates; no tensor-factor padding or pure environment is needed.

A gate on sites i<j is made adjacent by at most j-i-1 SWAPs, applied, then
routed back by the inverse swaps. This acts identically on all other sites,
including their initially mixed states. Thus each block needs
O(b 144^b) nearest-neighbor gates; all m blocks together need
O(N 144^b). Depth is at most O(b 144^b) if disjoint blocks run concurrently.
The constants are fixed synthesis constants, not a numerical hardware quote.
No short explicit gate list for a large block is supplied; the isometry,
unitary-completion and cited exact synthesis algorithm define it constructively.
Finite-range local interaction is therefore compatible with the collective
advantage in this control class; uniformly bounded depth is not established.

## 4. Logarithmic blocks suffice for vanishing full-channel error

Write R=log(3/2), S=entropy(tau)<R, B=log(pmax/pmin)>0.
Choose0<delta<R-S and kappa=2delta^2/B^2. K1918's proved finite-copy bound
applies for every integer b>=b0=ceil(log2/(R-S-delta)):

    1-p_b<=exp(-kappa b).

For a requested whole-channel error eta in(0,1), choose

    b>=max(b0, ceil(log(N/eta)/kappa)).                (2)

When N is not divisible by b, avoid a small remainder block. If N>=b,
partition into m=floor(N/b) blocks of sizes between b and2b-1, distributing
the remainder among them (or merging it into the last block). Then

    1-product_i p_(b_i)<=sum_i exp(-kappa b_i)
        <=N exp(-kappa b)<=eta.                      (3)

All sites are covered. For N<b use a single N-site block and its exact p_N;
(2) is only a sufficient large-N guarantee, not a promise for arbitrary N.
For fixed eta, b=O(log N). For eta=N^-r, b=O(log N) again at fixed r>0.
Largest block<2b gives total gate bound O(N 144^(2b)), polynomial in
N/eta for fixed spectrum and entropy gap. The exponent can be enormous,
and diverges as the gap closes: polynomial existence is not practical cost.
This result removes the need for one N-site collective gate, but not a
slow or highly controlled circuit. Its information-processing radius is
O(log(N/eta)); its elementary interaction range is one lattice edge.

## 5. Released bounded-strength and implementation-error accounting

Every one-site or two-site unitary has a Hermitian logarithm K with
||K||<=pi. Under the admitted ability to apply any such local Hamiltonian
with norm at most J>0, it can be implemented in time pi/J by H=JK/pi
(with the sign set by U=exp(-iK)). Serial execution of G gates therefore
has time at most pi G/J. Disjoint gates can be parallelized under a PER-GATE
norm bound; a total apparatus norm bound would be a different resource model.
No energy conservation, bandwidth, switching, transport, reset or cooling
work is charged by this construction.

If each implemented unitary differs from its intended gate in operator norm
by at most epsilon, telescoping products gives ||U_actual-U||<=G epsilon.
For every purification, the induced channel half-diamond error is at most
that operator norm, and tracing the bath cannot increase it. Thus

    final half-diamond error<=thermal_tail+G epsilon. (4)

Allocate eta/2 to(3) and require epsilon<=eta/(2G). For polynomial G this
requires only O(log(N/eta)) bits of ANGLE ACCURACY in a continuous-gate model;
this is not a finite gate-set synthesis or fault-tolerance theorem. The
control precision obligation is explicit instead of silently free.

## 6. Exact finite controls and a block-scale example

For q=1/21, use the exact shell mass formula of K1918. An independently
computed b=600 mass satisfies1-p_600<1/100000000. Consequently N=600000,
m=1000 blocks have whole-channel error below1/100000 and the alternative
blockwise truncated preparation has relative entropy below1/99999, since
-m log p<=m(1-p)/p. The actual rational bound is tested before acceptance;
no asymptotic estimate certifies it. This example demonstrates finite error
accounting, not feasible gate counts: the generic synthesis bound is vast.

Independent small controls enumerate all qutrit words, explicitly build two
orthogonal support embeddings for b=2, verify their Gram compression for
all16 system words, and route a nonadjacent pair through SWAPs on arbitrary
basis states. Input faults corrupt a shell degeneracy, support embedding or
one inverse SWAP; real identities must fail after the clean baseline.

## 7. Hostile review and next construction

Strongest overclaim is a constant-time, energy-conserving or experimentally
available thermal device. The stated model grants arbitrary U(144) controls,
and the bound exposes large time and precision costs. Strongest contrary
regime S>=R is outside the useful concentration guarantee; fixed b also
cannot make the upper bound m(1-p_b) vanish as m grows. That last fact is
only a limitation of this certificate, not a universal fixed-depth lower
bound. Weakest interface is treating alpha,j as physical free ancillas;
section2 embeds them in the existing bath and never introduces a new system.
A useful next test is a structure-exploiting local circuit under a specified
energy-conserving or fixed-depth Hamiltonian class. Such a restriction needs
a new construction or lower bound, not a stronger reading of this theorem.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its nonzero southeast rival. SC-MAS-01/SC-CHI-02 ASSERT a stylized curvature
mass toy; SC-META-53 remains UNCERTAIN about indefinite spectra. None selects
the positive Hilbert bath, scalar control or physical units used here.
LT-SM8, LT-GR6b and AC-F1, source-register and canon verdicts remain unchanged.
The full20 raw/barred map, separate K/C, accessible algebra and physical domain
remain distinct constructions. These are independent mathematical results.
Analytic arguments carry universal claims; exact finite probes test identities
and examples, not expert acceptance, empirical prediction or formal proof.
