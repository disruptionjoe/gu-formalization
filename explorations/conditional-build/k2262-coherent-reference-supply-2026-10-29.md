---
title: "K2262 Fresh coherent reference supply and whole-stock limits"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2262_coherent_reference_supply_probe.py
---

# K2262 Fresh coherent reference supply and whole-stock limits

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2262 Fresh coherent reference supply and whole-stock limits
carrier: finite charged reference registers, arbitrary detector input/history, neutral record and environment, and isolated spent resource stock LAYER=toy CHIRALITY=N/A
pairing: positive tensor Hilbert structure and half trace distance ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: copy, charge and record labels, not observed physical chirality
action_owner: repository-construction -- supplied conditional operator and apparatus
target: conserving replenishment, complete process error and finite coherent-stock limits MAP-TYPE=intertwiner
```

## 1. Supply the missing phase resource explicitly

[K2260](k2260-coherent-replenishment-bound-2026-10-29.md) bounds a detector supplied only invariant charged donors. It also allows exact recharge of coherently translated packets. Here the apparatus receives fresh coherent packets rather than disguising them as heat or charge. The target is the actual complete field-plus-record instrument of [K2253](k2253-full-instrument-reference-reuse-2026-10-29.md), E=1_(b*b=0), b=(5/3)a1+(4/3)a2*, with Kraus E,I-E, and energy-growth bound C=81. All conservation statements concern oscillator NUMBER, not a nonuniform physical Hamiltonian.

Let B and D be isomorphic finite registers with charges0,...,H. W=SWAP_BD is Hermitian, unitary, and commutes with N_B+N_D. The positive generator g(t)(I-W), g>=0, gives W exactly when integral g=pi/2. With the globally C1 pulse g(t)=sin²t for0<=t<=pi and zero outside, its peak added norm and derivative norm are both2; g and its first derivative vanish at the endpoints. A common onsite drift omega(N_B+N_D) commutes with W. The result is a SWAP with known phase rotation; use the corresponding rotating frame and phase-programmed fresh packet, or explicitly compensate that known phase. Arbitrary unequal drift is not covered.

For an arbitrary used-reference/history state rho_BF and a fresh pure sine packet beta_D,

    W(rho_BF tensor beta_D)W* = beta_B tensor rho_DF.    (1)

This is a FULL joint identity: B is restored and decorrelated, while D inherits every old correlation. Spent D is isolated from future service; accessible outputs/history may be processed by the stated adaptive controller. Freshness means joint independence, not correct marginals. The SWAP is local to two registers but may require an arbitrarily complex interaction between their internal levels; no geometrically local oscillator or restricted gate synthesis is asserted.

## 2. Complete adaptive detector service and actual stock cost

For Q>=0,R>=Q,L>=2, K2253 supplies a number-conserving shell unitary and reference packet

    H=R+L-1+Q,
    |beta> = sqrt(2/(L+1)) sum_(j=0)^(L-1)
               sin((j+1)pi/(L+1)) |R+j>.

The packet's maximum OCCUPIED charge is R+L-1 and mean charge is R+(L-1)/2. H is register capacity, including empty boundary margins. Its initial phase bandwidth is L-1; margins and offsets do not add phase coherence. Full input/output and neutral-workspace truncation and end-shell completion are inherited from K2253, not replaced by a truncated nonunitary shift.

Use K packets total: the initial B and K-1 fresh replacements between K detector calls. No final replenishment is counted. If the entire actual initial stock plus accessible input/history differs by at most delta from its ideal jointly independent product, the complete adaptive field/record/history error is bounded by

    epsilon_K <= min(1, delta + K e(B0;Q,R,L) + sum_j eta_j),
    e=2sqrt(B0/(Q+1)) + sqrt(2C(B0+1)/(R+2))
                         +(Q+R)pi/(L+1).               (2)

B0 bounds the mean input number at EACH ideal call, averaged over records. Controllers act only on accessible field/records/history, not the battery or spent stock. Their own resource costs are separate. In the ideal-prefix/actual-suffix hybrid, each replaced reference is exactly fresh by(1), arbitrary history is already covered by K2253, and later actual channels contract trace distance. Initial joint delta is charged once. eta_j is the integral norm error of a gate's Hamiltonian, by Duhamel; the sum includes detector and replacement errors. Conservation-based lower bounds require actual errors/controls themselves to respect covariance; arbitrary symmetry-breaking perturbations supply an extra resource. No normalized rare-history guarantee follows.

**Explicit finite consumer.** Take K=10,B0=1,C=81,

    Q=15999999, R=5183999998, L=99999999999999.

The one-call terms are1/2000,1/4000, and less than0.000164. Thus10e<0.00914. With delta<=0.0001 and sum eta<=0.0001, epsilon_10<0.00934. There are10 prepared coherent packets and9 replenishment pulses, duration9pi in the stated pulse units, plus the separately supplied detector synthesis time. Each register capacity is100005199999995, occupied maximum100005183999996, mean50005183999997; total nominal initial charge mean500051839999970 and occupied maximum1000051839999960. Ideal stock is pure; spent stock carries displaced correlations and need not be pure. These very large finite resources are an existence construction, not an efficient improvement over K2253's shared reference.

Equation(1) closes replenishment of the working reference, not production of fresh coherent stock or recycling all waste. Calling it a closed regenerative device would be false.

## 3. Followthrough: charge offset does not increase the coherent-stock lifetime

Consider M independent sine packets of length L, with any charge offsets and empty margins. Let

    p_j=2 sin²((j+1)pi/(L+1))/(L+1),
    g_L(theta)=sum_j p_j exp(-ij theta),
    v_L=sum_j p_j (j-(L-1)/2)².

For the whole pure stock its orbit trace distance is EXACTLY

    D_stock(theta)=sqrt(1-|g_L(theta)|^(2M))
                   <=min(1, |theta| sqrt(M v_L)).       (3)

Offsets add only a global phase to the overlap. For iid X,X' with law p,1-|g|²=E[1-cos(theta(X-X'))]<=v_L theta². Then1-x^M<=M(1-x) proves(3). No variance formula or Gaussian approximation is needed.

For the lower-bound tester, retain and isolate each old field/record output pair. Assume vacuum service inputs, joint invariant independent extra donors, and covariant controls, counting all asymmetric resources in the M packets. The ideal one-call recorded output tau has K2260 root fidelity

    f(theta)=|p²/(1-r exp(-2i theta))|
             +|1-2p+p²/(1-r exp(-2i theta))|,
    p=9/25, r=16/25.

By covariance, contractivity, and triangle inequality, the actual K-output error obeys

    epsilon_K >= [1-f(theta)^K-D_stock(theta)]_+/2.       (4)

This counts the whole stock, not merely one working reference. Independent preparation is essential to(3); entangled/correlated coherent stock requires its actual orbit distance.

**Linear stock-count example.** For L=2 each packet is a shifted |+>, v=1/4. Take theta=1/(2sqrt(M)). Then D_stock<=1/4. K2260's rational sine estimate gives f<=1-18/(181M), hence

    epsilon_K >= [3/8-(1/2)exp(-18K/(181M))]_+.           (5)

For K>=20M the bound is strictly above1/4, using1+x+x²/2>4 at x=360/181. Arbitrarily high charge offsets or invariant charged supply do not evade it. This improves the O(M²) lifetime obstruction from total bandwidth alone to O(M) for this independent two-level stock. It is a necessary resource bound, not an achievable rate, and the large-L construction in section2 is not the L=2 example.

## 4. Returning the entire phase stock independently cannot be exact

Let sigma be any finite resource state, even mixed, and all additional donors be invariant and independent. Suppose a covariant process on vacuum inputs returned exactly sigma tensor tau^K on resource plus retained outputs. For sufficiently small nonzero theta set a=F(sigma,sigma_theta)>0, where F is root fidelity. Continuity gives a>0, while the actual detector has f(theta)<1. Monotonicity of fidelity under the channel requires output root fidelity at least a. The proposed product return has root fidelity a f(theta)^K<a, a contradiction. The argument applies even with unlimited invariant charge donors and additional discarded invariant stock.

Quantitatively, if joint actual resource-plus-output state is within epsilon of sigma tensor tau^K, root-fidelity continuity gives

    a[1-f(theta)^K] <= 2sqrt(2epsilon),
    epsilon >= a²[1-f(theta)^K]²/8.                      (6)

One can derive the continuity inequality by purifying nearby states with overlap F>=1-epsilon, choosing purification vector distance at most sqrt(2epsilon), applying the triangle inequality to overlaps and optimizing Uhlmann purifications, once for each argument. This controls the JOINT product-return target. It does not prove a marginal-only no-catalysis theorem when resource-output correlations are allowed. Broader finite-dimensional no-broadcasting results exist, e.g. [Lostaglio and Mueller](https://arxiv.org/abs/1812.08214); only the explicit product-return argument and bound above are used here.

The supply construction evades exact return by leaving the consumed information in spent packets; its very accurate approximate restoration is compatible with finite errors and enormous resources. The next physical interface is a specified phase-stock preparation/transport and waste recovery protocol or a restricted synthesis of the shell unitary, with those resources counted. No source-owned physical detector has been constructed.

## Scientific ceiling and reproduction

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These supplied constructions do not resolve those source claims. Ledger0.263 and LT-SM8/LT-GR6b/AC-F1 remain unchanged: action ownership, physical quotient and observed-domain bridges remain absent. Preserve full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings.

Universal statements are written proofs; finite exact probes test the declared algebra and resource controls, not continuum completeness. Internal independent review is distinct from Lean, external-expert, novelty or remote-CI certification. Run the script listed above, adding `--write` only to regenerate its report.
