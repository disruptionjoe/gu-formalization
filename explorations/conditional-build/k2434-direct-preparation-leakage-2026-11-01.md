---
title: "K2434 Direct preparation-to-leakage transfer with returning memory"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no new complete Euler jet, physical calibration or native GU identification
---

# K2434 Direct preparation-to-leakage transfer with returning memory

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
result: K2434
carrier: joint Bell input/reference and arbitrary finite returning device memory LAYER=toy CHIRALITY=N/A
pairing: half diamond distance and exact failure effects ON=declared_carrier
real_structure: complex positive Hilbert density matrices
grading: conditional trials, actual memory and retained outcomes
action_owner: repository-construction -- conditional mathematical model
target: tested conditional decoder support leakage MAP-TYPE=evaluation
```

## Result

[K2432](k2432-bell-preparation-memory-decoupling-2026-11-01.md) gives a sharp trace-distance decoupling bound, then converts it to decoder error. The particular support-leakage consumer permits a stronger direct argument. If p is the actual true failure probability and q the joint Bell infidelity, the ideal test on the counterfactual channel built from the **actual memory marginal** obeys the convenient bound

    p0 <= min(1,p+2sqrt(pq)+2q).                       (1)

This replaces the previous sufficient fourth-root dependence on preparation infidelity by square-root dependence in decoder distance. It does not invalidate K2432's sharper statement about its different metric. At true p=0, the exact sharp boundary is

    p0 <= 2q-q^2.                                    (2)

No physical calibration, uniform future transfer, GU probability model or native identification is supplied. SC-META-53 remains UNCERTAIN; source polarities, ledger0.263 and canon are unchanged. The exact leakage bound is proved sharp below; the full statistical experiment and decoder constant are not claimed globally optimal. No novelty or external certification is claimed. Purification and measurement fidelity are standard tools; see [Watrous's fidelity exposition](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/purifications-and-fidelity/fidelity). The operational bounds here are proved below on the declared objects.

## 1. Direct amplitude proof

Let A=SR be the input/reference pair, phi_A its rank-one Bell projector, and M every returning memory degree of freedom. The actual operation V acts on signal and memory, leaving reference untouched. Define

    C(X)=Tr_M V(X tensor rho_M),
    q=1-Tr(phi rho_A).

Purify the preparation, including the purification register in M for the proof and acting trivially on that register. Write

    psi=c phi*u+s v, c=sqrt(1-q), s=sqrt(q),
    (bra(phi) tensor I)v=0, ||u||=||v||=1.

The purified memory marginal is c^2 uu*+q Rv. Dilate V and its failure effect to an isometry W and failure projector Q. Triangle inequality gives

    c ||QW(phi*u)|| <= sqrt(p)+sqrt(q).

The counterfactual ideal failure is a mixture using exactly that memory marginal. Its second component has probability at most one, hence

    p0 <= c^2 ||QW(phi*u)||^2+q
       <= (sqrt(p)+sqrt(q))^2+q.

Partial trace of the proof-only purification preserves the physical counterfactual channel. Endpoints q=0,1 follow directly. The argument holds for every failure effect, so the full complex candidate-support tests inherit it without assuming a real or planar channel.

## 1a. Executed follow-through: the sharp general bound

The effect-specific geometry resolves the whole probability square. Define

    G(p,q)=(sqrt((1-q)p)+sqrt(q(1-p)))^2, if p+q<=1,
           1,                           if p+q>=1;
    B(p,q)=q+(1-q)G(p,q).

Then **p0<=B(p,q)**, sharply for every p,q. To prove the upper bound, put u0=phi*u and a0=<u0|E|u0> for the pulled-back failure effect. Cauchy--Schwarz applied to E and I-E gives

    sqrt(1-q)=|<u0|psi>|
       <=sqrt(a0*p)+sqrt((1-a0)(1-p)).

Write a0=sin²(beta), p=sin²(alpha), q=sin²(gamma), with all angles in [0,pi/2]. Then |beta-alpha|<=gamma. Below p+q=1, alpha+gamma<=pi/2, so a0<=G(p,q). Else a0<=1. The actual-memory mixture gives p0<=q+(1-q)a0.

For saturation below the boundary, use the same prepared psi_q as section3 and

    D_g=[[sqrt(1-g)I,sqrt(g)Z],
         [-sqrt(g)X,sqrt(1-g)XZ]], g=G(p,q).

This is unitary. Its actual failure amplitude is sqrt(g(1-q))-sqrt((1-g)q)=sqrt(p). Ideal Bell input with memory0 fails with probability g, and with memory1 fails with probability1. Thus p0=(1-q)g+q. The probe checks an interior rational fixture p=25/169, q=9/25, sqrt(g)=56/65, sqrt(1-g)=33/65, p0=88201/105625.

Above the boundary, a memoryless X decoder on the Bell-diagonal preparation with weights (1-q),(1-p),(p+q-1) on Phi,Phi_X,Phi_Z has the prescribed p,q and p0=1. Thus the plateau is also attained. This is sharpness over the stated arbitrary-device class; a specific decoder's support witness may permit improvement.

B is jointly concave by a physical argument: mix any two saturated experiments with an orthogonal classical flag in memory and a flag-controlled operation. Both p and q, and the actual-memory counterfactual p0, mix linearly. Applying the universal bound to that physical mixture proves B(mean p,mean q)>=mean B(p,q). B is coordinatewise nondecreasing: the angle expression increases below the boundary, q+(1-q)G increases when q increases, and the plateau is constant. Hence the sharp adaptive bound is **mean p0_t<=B(a,e)**. This improves the simpler bound below without a numerical Hessian assumption.

For a<=v<1, its exact preparation threshold is

    h=sqrt(1-v), k=(v-a)/(sqrt(1-a)+h),
    x=2k/(sqrt(a)+sqrt(a+4hk)), e_max=x²/(1+x²).       (4)

At a=v set e_max=0 directly, including a=v=0. Derive (4) by putting x=sqrt(e/(1-e)) in

    sqrt(1-B(a,e))=(1-e)sqrt(1-a)-sqrt(ae(1-e)).

Below the boundary its right-hand side is nonnegative. The target equality becomes h*x²+sqrt(a)*x+h-sqrt(1-a)=0; rationalizing its positive root yields (4). Monotonicity proves necessity and sufficiency for this sharp universal leakage certificate. At a=0 it reduces to e_max=1-sqrt(1-v). The decoder constant C may itself remain conservative.

## 2. Adaptive averages and a usable preparation budget

Condition every trial on its recorded past, with predictable selection and all outcomes retained. Let u_n be K2430's stopping-safe upper bound on the average observed conditional failure probability; eta_t bounds the readout-effect error; q_t is true conditional joint preparation infidelity. On the simultaneous calibration event define

    a=min(1,u_n+mean eta_t), 0<=e<=1 with e>=mean q_t.

Any supplied upper bound on the conditional mean infidelity may be clipped at one. Cauchy--Schwarz bounds mean sqrt(p_t q_t) by sqrt(mean p_t mean q_t), yielding

    mean p0_t <= b=min(1,a+2sqrt(ae)+2e).

For the same target channel as K2428/K2430, both the distance of the tested mean channel and the mean tested-channel distance are at most min(1,C sqrt(b)). The inherited constants are C_bad=2(1+sqrt2/mu), mu^2>0.0522306, and C_good=2. Probability coverage is at least1-alpha-beta if the simultaneous trusted calibration event fails with probability at most beta. Independence between these events is unnecessary.

For distance target tau, put v=(tau/C)^2. If a>v this sufficient certificate cannot pass. If 0<=a<=v, the simple direct theorem permits

    e <= (sqrt(2v-a)-sqrt(a))^2/4
       = (v-a)^2/(sqrt(2v-a)+sqrt(a))^2.              (3)

This follows by solving 2x^2+2sqrt(a)x+a-v<=0 with x=sqrt(e). The second form is numerically stable. At a=v only e=0 passes; at infinite trials and zero readout allowance it becomes e<=v/2, quadratic in tau. The theorem still needs actual calibration evidence; more trials do not remove a fixed systematic floor.

For prospective tau=0.01, alpha=1/60 per branch, zero recorded failures and zero readout allowance, Arb256 encloses the following sharp preparation thresholds. The original three-branch union bound gives at least95% statistical coverage before any added calibration failure probability.

| Branch | Retained trials | Sharp joint infidelity threshold, approximately | Conservative tested value |
| --- | ---: | ---: | ---: |
| Bad sign | 9,000,000 | 4.32915909e-10 | 1e-10 |
| Good | 170,000 | 8.386623018e-09 | 1e-9 |
| Bad sign, expanded | 20,000,000 | 4.4319509114e-8 | 1e-8 |

The report contains rigorous intervals and verifies each conservative value against the distance target. The nine-million branch improves the prior8.37e-16 sufficient threshold by more than five orders of magnitude. It still assumes a trusted joint preparation bound and the same decoder constants.

These are prospective sufficient requirements, not measured fidelities or observed zero counts. Finite zero counts mean u_n=log(1/alpha)/n>0, never true p=0. An unconditional fidelity of a different ensemble, postselection or marginal input calibration does not establish e for these retained conditional trials. A simultaneous bound on their true conditional mean is sufficient; no unproved history-wise maximum is inferred from an unconditional average.

## 3. Sharp true-zero boundary and physical saturation

For true p=0, the pulled-back effect E obeys E psi=0 and 0<=E<=I. Since |<phi*u|psi>|^2=1-q,

    <phi*u|E|phi*u> <= q.

The actual-memory mixture therefore gives p0<=(1-q)q+q=2q-q^2. This is universally sharp, not just a leading-order estimate.

Take Pauli X,Z on a qubit and memory-block unitary

    U = [[cI,-sX],[sZ,cZX]], D=U^dagger,
    psi=U(phi tensor |0>).

Then D psi=phi tensor |0>, so p=0, while the actual memory is diag(1-q,q). The counterfactual decoder has Kraus operators

    c^2 I, -cs X, s^2 Z, cs XZ.

Only the first has Bell overlap; p0=1-c^4=2q-q^2. The probe verifies the complete eight-dimensional state/unitary and Kraus channel exactly at c=4/5,s=3/5. Replacing the actual memory by the normalized Bell-projected memory |0> changes p0 to q; that is a different channel and cannot justify the false p0<=q shortcut.

The cross term in (1) also matters. With the real unitary rotation R=[[12/13,5/13],[-5/13,12/13]], prepare (R^-1 tensor I)phi and apply R^2. Then p=q=25/169 but p0=14400/28561>p+2q. Applying R instead gives true p=0 and channel half-diamond distance sqrt(q), ruling out a uniformly better preparation exponent for arbitrary channels. To justify the distance directly, write R=cI+isY. For every pure input/reference state the output overlap squared is c²+s²〈Y tensor I〉²≥c², so the trace distance is at most s; |0〉 attains equality. Convexity covers mixed states, giving half-diamond distance exactly s=sqrt(q). The probe checks the entanglement-infidelity identity; this analytic argument establishes the diamond distance.

## 4. Deployment scope and next useful input

This result strengthens preparation robustness for **tested conditional channels**. It does not supply K2432's uniform memory-decoupling/reset or fixed-reference deployment assumptions. Shared random errors across uses and independent errors have the same one-use channel but different joint outputs; the exact two-use contrary control remains. A process guarantee still needs justified uniform transfer or a stronger directly tested multiround object.

The next physical step is trusted conditional preparation and readout at the relaxed budget, plus measured complete instrument costs and a declared transfer/reset model. For mathematical continuation, test an instrument-specific relation between its support witness and preparation errors, or a complete multiround tester. Another nominal objective decimal does not address these missing inputs.

## Verification

[Probe](../../tests/channel-swings/k2434_direct_preparation_leakage_probe.py) and [report](../../lab/process/k2434-direct-preparation-leakage.json) check exact unitaries, density matrices, actual memory, Kraus normalization, contrary controls and symbolic inversion; Arb256 certifies sufficient numerical budgets. Universal claims rest on the proofs above, not sampled agreement.

```sh
python tests/channel-swings/k2434_direct_preparation_leakage_probe.py --check
```
Dependencies: SymPy and python-flint. Internal independent review is not external-expert or proof-assistant certification.
