---
title: "K2438 Certifying a mixed recorded instrument"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: tested conditional average processes only; no actual data, physical calibration, optimal sample cost, future transfer or native GU identification
---

# K2438 Certifying a mixed recorded instrument

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2438
carrier: finite causal quantum combs with accessible classical flag blocks and retained quantum references LAYER=toy CHIRALITY=N/A
pairing: normalized Choi trace norm, supported Hilbert-Schmidt constraints and half strategy distance ON=declared_carrier
real_structure: complex positive Hermitian states and completely positive causal operations
grading: chronological slots, classical records and pre-batch conditional history
action_owner: repository-construction -- imported quantum instrument and process framework
target: mixed support identification and complete flagged tomography of tested process averages MAP-TYPE=evaluation
```

## Result

The original noisy recorded instrument cannot be certified by a support test, even with exact probabilities for **every** input-dependent flag. Its two bad Choi blocks are full rank. An exact competing instrument preserves those flag effects and supports but changes the output state by at least73/416 or259/2080 in the two original laws.

A complete flagged-Choi measurement resolves this gap. This note gives the necessary-and-sufficient support-identification criterion, a robust support-plus-moments theorem, and an explicit randomized tomography protocol for the original instrument and multiround processes. Arbitrary device memory and adaptive drift between tested batches are allowed under the stated experiment. Signed tomography certifies the **average tested process**, not the mean of individual distances or a future device.

This uses the standard [quantum-strategy framework](https://arxiv.org/abs/1008.4636) and the channel geometry studied by [Ruskai, Szarek and Werner](https://arxiv.org/abs/quant-ph/0101003). No novelty is claimed. The framework is imported conditional mathematics: SC-META-53 remains UNCERTAIN, ledger0.263/source polarities/canon are unchanged, and no native GU positive physical quotient or measured instrument is supplied.

## 1. Which mixed target is being tested

Distinguish three objects: the original flagged noisy instrument, its three controlled recovery decoders, and their composition. [K2428](k2428-exact-recovery-uniqueness-2026-11-01.md)'s rank-two bad decoder supports are **not** the supports of the original bad instrument branches.

For the two original antipodal laws use mean m, length l=||m||, direction n=m/l and weights(1+l)/2,(1-l)/2 on n,-n. The total instrument has good branch(1-w)id and bad branches w J_z, z=+1,-1, with

    J_z(rho)=E_n [(Tr rho+z n·r)/2 (I+v n·sigma)/2], v=1/2.        (1)

Here r is the input Bloch vector and classical z is retained. Its normalized Choi state has one rank-one good block and two rank-four bad blocks: total rank9. Each bad block is a positive mixture of two orthogonal input eigenspaces tensored with strictly positive output states.

Replace every bad prepared pointer by I/2 while keeping its input effect. The new instrument is CP/TP, has identical full support and identical branch input marginals. Thus **all** input-dependent flag probabilities agree, not merely the frequency at one calibration input. On input I/2 the flagged output distance is

    w v ||m||/2 = w||m||/4 = 73/416 or 259/2080.                  (2)

Every support failure probability is zero in this comparison. Bad conditional branches are not TP channels after a fixed normalization because their flag effects E_z=(I+z m·sigma)/2 are not scalar. Input-independent branch probabilities must be established before such normalization is allowed.

The probe reconstructs(1) from the original law data, checks all CP/TP and marginal identities and computes(2) exactly. This defeats an instrumental certification shortcut; it says nothing adverse about GU or the separate decoder theorems.

## 2. Exact support-identification criterion

Fix a real Hermitian carrier, including classical block diagonality when required. Write the normalized causal processes as

    F={rho>=0: A(rho)=b},

where A contains **all** affine causal constraints. Let sigma be the target and P its support. Then zero support leakage identifies sigma within F iff

    ker(A restricted to Herm(P) intersect carrier)={0}.            (3)

Sufficiency: positivity and Tr[(I-P)rho]=0 force rho=P rho P, and the difference from sigma lies in the stated kernel. Necessity: a nonzero supported Hermitian kernel vector H gives distinct feasible sigma±epsilon H for sufficiently small epsilon>0, because sigma is strictly positive on P. This also explains the usual channel extremality criterion. Partial trace over all outputs alone is a sufficient smaller constraint set; using only it does not give necessity for general causal combs.

The original one-slot flagged support has real dimension1+16+16=33 and TP rank4. Exactly29 supported Hermitian directions remain invisible. In contrast, the probe's mixed amplitude-damping channel at gamma=3/4 has an injective supported TP map. Tensor-product supports preserve injectivity of total-output partial trace; their minimum Hilbert-Schmidt singular values multiply. Conditioning can therefore deteriorate rapidly even when exact identification survives. The actual full instrument fails(3), so a decoder extremality theorem cannot repair its missing output observations.

## 3. Robust support plus accessible moments

For this robust statement, require compression H -> P H P to preserve the declared carrier; this holds for the full Hermitian and classical-block carriers used here. Add fixed measurable moments M and put L=(A,M). On V=Herm(P) intersect carrier, assume a proved minimum Hilbert-Schmidt singular value mu>0. Supply ell satisfying ||L(H)||_2<=ell||H||_1 for Hermitian H, and let m=rank P. For any feasible rho, let

    p=Tr[(I-P)rho], epsilon=||M(rho-sigma)||_2.

Then

    D(rho,sigma)<= (1+sqrt(m)ell/mu)sqrt(p)
                    +sqrt(m)epsilon/(2mu).                       (4)

Proof: X=P rho P-sigma lies in V and Y=rho-P rho P satisfies ||Y||_1<=2sqrt(p) by gentle projection. Since A(rho-sigma)=0,
L X=(0,M(rho-sigma))-L Y. Hence ||X||_1<=sqrt(m)||L X||_2/mu. The triangle inequality gives(4). If p=0 and epsilon=0 it reduces to uniqueness. Moment directions that do not increase supported rank cannot create a certificate.

For fixed r-slot input/output dimensions, [K2436](k2436-multiround-process-certificate-2026-11-01.md)'s normalized tester map Xi has effect norm at most

    K^2=(product_i d_Ai)(product_(i<r) d_Bi).

For any Hermitian difference, positivity gives ||Xi(H)||_1<=K^2||H||_1; therefore delta_strategy<=min(1,K^2 D). This generic bound uses K squared, unlike the sharper **pure-target** square-root argument. It requires no access to an inaccessible purification. With a qubit signal and three flags exposed at every slot, d_A=2,d_B=6 and K^2=2^r6^(r-1). Hiding all flags until the end changes the permitted adaptive testers and the operational target; it is not a free improvement to this constant.

## 4. Executed successor: full original flagged tomography

For one slot, retain every flag and measure all48 real coefficients

    c_zab=Tr[rho (|z><z| tensor sigma_a tensor sigma_b)],
    a,b in {0,x,y,z}, sigma_0=I.

Each4x4 block reconstructs as rho_z=(1/4)sum_ab c_zab sigma_a tensor sigma_b. If e_z is a vector of componentwise absolute residual bounds relative to the fixed target, the Hilbert-Schmidt identity and trace-norm inequality give

    D(rho,sigma)<= (1/2)sum_z ||e_z||_2.                           (5)

For r slots use3^r flag strings and16^r Pauli strings per flag; every quantum block has dimension4^r. Since its Pauli basis has squared norm4^r, the same factor1/2 in(5) survives. This is an explicit complete data interface, not a claim of efficient tomography. It tests the entire same-initialization process, including temporal correlations.

The Y directions are necessary. The two strict-PSD TP Choi states(I4±Y tensor Y/2)/4 agree on every I/X/Z product moment but have trace distance1/2. Their complete Pauli records differ. The probe also reconstructs all three original target blocks exactly and shows that the full moments distinguish the counterfeit instrument in section1.

## 5. A common-ensemble, stopping-safe experiment

Prepare all signal/reference Bell resources before each complete batch; keep references inaccessible to the device. Condition on recorded history before the batch and use its actual returning-memory marginal. After the complete process, choose a Pauli setting privately and uniformly from S=16^r settings, then read the quantum outcomes and all flags. The setting must not alter which process is tested. Its observable has norm at most1; identity factors can be ignored physically.

For a coefficient indexed by flag string z and setting a, record

    X_t= S 1(setting=a)1(flag=z) product(measurement outcomes).

Then E[X_t|past] is that coefficient of the actual conditional output state, |X_t|<=S, |E X_t|<=1 and conditional variance<=S. Thus all coefficients estimate the **same** average conditional output state; separate fixed-setting campaigns under drift would not generally do so. Keep every trial, including declared losses on a properly enlarged carrier; postselected success records define a different object.

For M=3^r16^r coefficients and n>=1, set

    L_n=log(2M n(n+1)/alpha),
    R_n=sqrt(2 S L_n/n)+2(S+1)L_n/(3n).                           (6)

A scalar Freedman/Bernstein martingale bound with increments bounded by S+1 and variance sum<=nS gives failure probability at most2exp(-L_n) per coefficient at n. The two-sided union over M coefficients and every n uses sum_n1/[n(n+1)]=1. Therefore, simultaneously for all n, every mean coefficient differs from its empirical estimator by at most R_n with probability>=1-alpha. Optional stopping is allowed without restarting the counts. The ordinary range-only Hoeffding radius S sqrt(2L_n/n) is a valid but weaker alternative. The concentration tool is standard; see [Tropp's statement of Freedman's inequality](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf).

A calibrated per-coefficient observable-norm error eta contributes its average to the residual radius (the random-setting estimator is centered on the implemented observable). Use e_z,a=|hat c_z,a-c_target,z,a|+R_n+mean eta_z,a in(5). Full normalized Choi data include the input marginal; no fitted target may be selected after seeing the certificate without pricing that selection.

## 6. Preparation and quantitative consumer

Let q_t be the infidelity of the **joint** pre-batch signal/reference resource to the full Bell product, including its possible correlations with device memory. [K2432](k2432-bell-preparation-memory-decoupling-2026-11-01.md) gives the trace-distance transfer to the ideal resource tensored with the same actual memory marginal:

    f(q)=(q+sqrt(4q-3q^2))/2.

With a simultaneous bound e>=mean q_t, concavity gives a mean output-state transfer at most f(e). Combine this with tomography and the tester bound to obtain

    delta_strategy(mean ideal conditional process,target)
      <=min(1,K^2[(1/2)sum_z||e_z||_2+f(e)]).                    (7)

If the calibration event fails with probability beta, coverage is at least1-alpha-beta without assuming independence. The experimentally measured state need not itself be a causal Choi state when resource and memory were correlated; transfer is applied **before** interpreting(7) as a process theorem.

For one slot, if every empirical coefficient differs from the fixed nominal target by at most1e-5, alpha=.05, n=4 billion complete trials, q-mean<=1e-8 and each readout observable error<=1e-5, the report evaluates a sufficient sub1% half-diamond allowance using(6)--(7). This is a prospective conditional example, with no actual counts or physical cost evidence and no optimal sample-complexity claim. The construction deliberately exposes the cost of identifying the full noisy instrument. Inherited decoder implementation bounds remain separate; a composed recovery certificate requires both errors.

Signed average moments can cancel: deterministic flag0 and flag1 batches can average to the fair target while every individual conditional channel is distance1/2 away. Thus(7) is distance of the mean, **not mean distance**, an exceptional-batch bound, or a guarantee for a future batch. A support-only extremal target admits stronger leakage-based mean bounds under its separate hypotheses. Future use needs independently justified transport/reset evidence or a fully specified deployment experiment.

## Verification

[Probe](../../tests/channel-swings/k2438_mixed_instrument_certification_probe.py) and [report](../../lab/process/k2438-mixed-instrument-certification.json) check original rational CP/TP instruments, exact support and effect-preserving countercontrols, the complete complex Pauli inverse, supported constraint ranks and a mixed extreme fixture. Arb256 verifies the stated prospective bounds. Universal claims are proved in sections2--6; finite physical controls and manifest checks are reported separately. Independent internal review challenged conditional normalization, inaccessible purification, visible flag dimensions, preparation coupling and averaged-moment quantifiers.

```sh
python tests/channel-swings/k2438_mixed_instrument_certification_probe.py --check
```

The probe needs SymPy and python-flint. The remaining application needs actual complete flagged records and trusted preparation/readout data, or a justified smaller observable set with a nonzero conditioning bound. No physics or hardware conclusion is supplied by prospective counts alone.
