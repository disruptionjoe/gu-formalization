---
title: "K2439 Minimal measurements for the original recorded instrument"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: linear-moment minimum on exact support only; conditional average instrument certification, no measured data or native GU identification
---

# K2439 Minimal measurements for the original recorded instrument

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
result: K2439
carrier: original three classical flag blocks on a complex qubit reference and qubit output LAYER=toy CHIRALITY=N/A
pairing: normalized Choi trace norm and half diamond distance ON=declared_carrier
real_structure: complex positive Hermitian states and completely positive maps
grading: classical flag blocks and pre-emission conditional history
action_owner: repository-construction -- imported finite quantum operations
target: dimension-minimal supported identification with explicit noisy inverse MAP-TYPE=evaluation
```

## Result

The original instrument has a 29-dimensional supported trace-preserving affine family. Exactly **29 real linear moments** identify every member, and no smaller linear-moment list can identify its strictly supported target. An explicit reconstruction below supplies a stable inverse without a numerical singular-value claim. Away from support it needs an additional leakage bound; that bound is not free. All required Pauli moments and the leakage witness can be measured with **nine local axis settings**, exploiting simultaneous marginal readout rather than sixteen separately sampled Pauli strings.

This reduces K2438's full 48-coefficient interface. It does not prove optimal sample complexity, minimum physical settings, identification from flags alone, or an actual experimental result. This is imported quantum process mathematics. SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b and ledger0.263 remain unchanged; no positive native GU quotient is constructed.

## 1. Fixed carrier and the 29-coordinate inverse

All displayed formulas and the new probes use tensor order reference R then output B. The older K2419/K2438 probe bank uses output B then reference R; the new original-law construction explicitly swaps that convention rather than reusing its coefficient indices.

Use normalized Choi blocks rho=(rho_g,rho_+,rho_-) on reference R and output B, both qubits, with Tr_B sum_z rho_z=I/2. The good support is Phi=|Phi+><Phi+| and the two bad supports are full C4. These are exactly K2438's original laws with positive good weight and strictly positive bad blocks, not the rank-two supports of their recovery decoders.

Let P_ab=sigma_a tensor sigma_b, a,b in {0,x,y,z}. Declare

    g=Tr rho_g,
    x_ab=Tr(P_ab rho_+)                       (all16),
    y_ab=Tr(P_ab rho_-)                       (b!=0:12).

On support rho_g=g Phi. Trace preservation supplies the four missing coefficients:

    c_-,a0=(1-g) delta_a0 - x_a0.                              (1)

Hence the exact affine reconstruction is

    R_g=g Phi,
    R_+=(1/4) sum_ab x_ab P_ab,
    R_-=(1/4)[sum_(b!=0) y_ab P_ab
                   +sum_a ((1-g)delta_a0-x_a0)P_a0].           (2)

It retains complex Y directions and the input-dependent flag effects. It is an algebraic inverse; noisy inputs need not reconstruct a positive matrix and are not silently projected onto a fitted target.

The supported Hermitian carrier has dimension33 and its TP constraint map has rank4 (K2438). Its tangent therefore has dimension29. The original target is relatively interior on its support. Any fewer than29 real linear functionals leave a nonzero tangent direction H; sufficiently small target±epsilon H are distinct CP/TP instruments with the same observations. This proves minimality **among real linear moment coordinates on this exact support**. It is not a bound on settings, POVM outcomes, nonlinear priors, or rank-changing families.

The probe builds the original33-column carrier and TP matrix, then checks that appending these29 moments has full column rank33. Removing any one moment restores a nonzero null direction; all29 resulting tangents are explicitly checked against TP and the retained observations. These linear witnesses become physical by the interior argument, not by assuming a random small epsilon works.

## 2. Explicit robust bound and leakage

For supported TP differences with coordinate errors dg, dx, dy, Pauli orthogonality and ||H||_1<=2||H||_2 on a4-dimensional block give

    B(dg,dx,dy)=1/2 [ |dg| + ||dx||_2
        +sqrt(||dy||_2^2+||dx_a0+dg delta_a0||_2^2) ],
    D(R(data),R(target)) <= B.                                (3)

For componentwise bounds e_g,e_x,e_y replace |dg| by e_g, ||dx|| by ||e_x||, and the final a0 components by e_x,a0+e_g delta_a0. This is a usable conditioning estimate, not merely a nonzero determinant.

Now let rho be any normalized positive flag-block state. Put

    p=Tr[(I-Phi)rho_g],
    E=Tr_B sum_z rho_z-I/2.

Writing Delta=rho_g-g Phi gives ||Delta||_1<=2sqrt(g p). In the missing minus input marginal, the error in(2) is E-Tr_B Delta. Thus

    D(rho,R(data)) <= 2sqrt(g p)+||E||_1/2,
    D(rho,target) <= B+2sqrt(g p)+||E||_1/2.                    (4)

Proof of the first estimate: good-block difference is Delta, plus-block difference zero, minus-block difference is (E-Tr_B Delta) tensor I/2. Triangle and partial-trace contraction prove(4). The subnormalized pure-state estimate follows by normalizing rho_g; g=0 is immediate. No hard exact-support assumption is hidden inside a small-noise theorem.

With exact Bell preparation, E=0. With K2438's correlated preparation transfer D(rho_actual,rho_ideal)<=F, where F=f(e) from the joint infidelity mean and actual memory marginal, ||E||_1/2<=F. Transfer back to the ideal average process costs another F. Therefore

    D(rho_ideal,target) <= B+2sqrt(g p)+2F.                     (5)

A separately measured TP defect can improve the first F. For the input qubit, half diamond distance is at most twice the Choi trace distance. Clip only final physical trace/diamond distance bounds at1; signed reconstructions in(3) need not be positive and their norms cannot be clipped. A trusted physical readout tolerance enters the moment and leakage intervals before(3)--(5).

The leakage functional is

    p=(3g-c_g,xx+c_g,yy-c_g,zz)/4.                             (6)

It vanishes identically on support, so does not count as one of the29 identifying coordinates; off support it is a necessary extra witness. A good-flag coherent phase rotation psi=cos(theta)Phi+ + i sin(theta)Phi- remains maximally entangled and preserves all29 coordinates and TP. Yet p=g sin(theta)^2 and its true distance is sqrt(g p). The exact cos=3/5,sin=4/5 control verifies this; the same symbolic family reaches arbitrarily small p. Thus the square-root dependence itself is necessary, not merely an artifact of this upper bound.

## 3. Nine settings and common-ensemble confidence

After each completed signal/reference experiment, independently choose A,B uniformly from {x,y,z}. Measure both qubits in those bases and retain both signs and every flag. The device must not receive the choices before emitting the state. From the same trial obtain unbiased estimators:

- for nonidentity a,b: 9 1(A=a,B=b,flag=z) s_R s_B;
- for exactly one identity factor: 3 1(relevant axis chosen,flag=z) s;
- for both identity: 1(flag=z).

Second moments are bounded respectively by9,3,1, rather than the16 of K2438's uniform16-setting estimator. The nine-setting scheme is informationally complete even for complex Y moments. Equal allocation is explicit and is not claimed optimal. Readout outcomes for identity factors are ignored, not separately measured.

Measure the29 coordinates and the three good correlations in(6), M=32 scalar quantities. For a coordinate with importance factor w in {1,3,9}, centered increments have magnitude<=w+1 and conditional variance<=w. For all n simultaneously, with probability at least1-alpha, its empirical mean is within

    R_w(n)=sqrt(2w L_n/n)+2(w+1)L_n/(3n),
    L_n=log(2 M n(n+1)/alpha),                                (7)

of the mean of its conditional expectations. This is the K2438 Freedman proof with the actual second moments; the union includes the three correlations needed for leakage. Correlations among reused trial estimators do not invalidate a union bound. It is distance of the average conditional instrument, not mean distance, a product-channel guarantee, or future behavior. For leakage use the upper endpoint of(6), intersected with simultaneous physical intervals for 0<=p<=g<=1; propagate an upper endpoint g_U (or use g<=1), never plug in the empirical good fraction; report inconsistency if physical intervals cannot intersect.

## 4. Executed quantitative and operational follow-through

The report compares the explicit widths and propagation constants with K2438 on a common hypothetical record. A small leakage confidence interval enters as sqrt(p), so this dimension-minimal scheme can be **worse** than full tomography for finite samples. It must not replace the complete48 interface solely because29<48. A measured Bell-support test with a rare-event upper confidence bound can outperform the signed correlation reconstruction of p; that requires an additional measurement choice and its own common-ensemble weights.

The important distinction is structural minimum versus statistical efficiency. Use the smaller design only when its actual leakage/calibration bound makes(5) competitive. Otherwise the existing full tomography bound is the certified fallback. K2440 independently supplies hidden test/use routing using the complete observable interface; it does not assume exact support or silently borrow these29 coordinates.

## 5. Released successor: avoid the support penalty with 44 coordinates

When leakage uncertainty dominates, keep all16 good coefficients and all16 plus coefficients, and the12 minus coefficients with b!=0. TP reconstructs the remaining four by

    c_-,a0=delta_a0-c_g,a0-c_+,a0.                             (8)

For three block residual vectors dg,dx,dy the explicit bound is

    B44=1/2[||dg||_2+||dx||_2
                  +sqrt(||dy||_2^2+||dg_a0+dx_a0||_2^2)].      (9)

It has no sqrt(leakage) penalty. For imperfect correlated preparation the same TP-defect argument gives D(ideal,target)<=B44+2F. Alternatively use all48 measured moments and K2438's direct B48+F, which may be tighter because it needs no inferred marginal. The nine-axis data already supply all48; selecting the best valid bound afterward needs no additional confidence budget if a single simultaneous event covered all48 coefficients from the start. In that comparison set M=48 in(7), rather than32.

The full flag-block Hermitian space has dimension48; TP rank4 leaves44. Thus44 is the minimum number of real linear coordinates that identify **every** full-carrier TP instrument, proved by an interior full-rank reference plus the same kernel argument. It is not the minimum for the particular rank9 original target:29 coordinates plus an exact zero-leakage witness already identify that boundary target globally by positivity. The probe verifies the rank48 augmented map, all44 one-deletion directions and exact original-law reconstruction, independently of the support-based design.

The finite-sample comparison is an executed route decision: simultaneous Pauli marginal reuse improves K2438's variance without an unsupported optimality claim; small coordinate count alone does not justify discarding its robust full tomography route. No new experiment is represented as performed.

The executed hypothetical comparison at4 billion trials, simultaneous48-coordinate coverage and empirical/readout allowances1e-5 each gives B48 about0.002529 and B44 about0.002654, before preparation transfer. The29-coordinate bound including its signed leakage interval is above0.046; this concrete comparison favors complete tomography unless a stronger support test is supplied. These are state-distance bounds, not measured performance or already-converted diamond bounds.

## Verification and ceiling

[Probe](../../tests/channel-swings/k2439_minimal_flagged_tomography_probe.py) and [report](../../lab/process/k2439-minimal-flagged-tomography.json) reconstruct the original two laws, exact full/deleted measurement ranks, algebraic inverse, explicit error inequalities, off-support and complex controls, and the nine-setting estimator. Arb256 supplies rigorous prospective widths; no counts are observations. Universal minimum and stability claims rest on the proofs above. Independent internal review is not external-expert or proof-assistant certification.

```sh
python tests/channel-swings/k2439_minimal_flagged_tomography_probe.py --check
```
