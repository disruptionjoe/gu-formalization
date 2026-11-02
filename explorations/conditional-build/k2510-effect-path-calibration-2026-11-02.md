---
title: "K2510 Effect-specific angular circuit calibration"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional finite-dimensional supplied-model mathematics; no native GU realization or measured apparatus certification"
---

# K2510 Effect-specific angular circuit calibration

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
result: K2510
carrier: original C108 Q/T verifier with retained memory E and supported subspace E0 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: effect-specific angular transport and quotient calibration MAP-TYPE=evaluation
```

## Result and scope

A trusted full-memory unitary dilation admits a sharp angular modulus for each verifier effect and a stronger amplitude bound for support leakage. These bounds price the parts of a circuit that mix the measured sectors. Arbitrarily large globally invisible controller motion can be removed from the parameter cover. Raw per-gate commutators cannot establish that invisibility: an exact downstream-Hadamard counterexample reverses the conclusion.

The endpoint is a constructive calibration contract, with explicit sample and complete-record costs. This is independent supplied-Hilbert-space mathematics. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain interacting quotient and common-domain debts. Ledger0.263, source polarities, canon and physical credit are unchanged. No novelty, experimental, external-expert or proof-assistant certification is claimed.

K2508 already supplies coherent-controller sector calibration, pooled confidence, fixed-family history transfer and norm-Lipschitz nets. Those results are reused. Here the new scientific content is the effect-specific angular transport, the sharp leakage composition, and elimination of globally invisible parameter directions, including contrary controls that distinguish these from ordinary full-channel continuity.

## 1. Complete carrier and a sharp angular theorem

Let D contain every retained controller and memory register, with fixed supported subspace projector S. The original Q,T are orthogonal projectors on D, commute with S, and include identities on all ancillary retained registers. Append a fixed fresh decoupled ancilla by isometry J; a mixed fresh state can be purified into another fresh register. Let V_theta be a trusted continuously differentiable unitary family on D tensor A. Trace only A after V. A forgotten reused register is not a fresh ancilla. Finite dimensions and a common differentiable model are assumptions, not calibration outputs.

For an absolutely continuous parameter path define the output-frame Hermitian generator and projected path lengths

    G(t)=i Vdot(t) V(t)*,
    D_F=integral ||(I-F)G(t)F|| dt,
    F=Q tensor I_A or T tensor I_A.

Then the compressed effect obeys

    ||S J* [V_1* F V_1 - V_0* F V_0] J S||
       <= sin(min(D_F,pi/2)).                              (1)

Proof: for any unit vector psi, including an untouched reference, write q(t)=<Vpsi,FVpsi>. Splitting Vpsi between F and I-F gives

    |q'|<=2 ||(I-F)GF|| sqrt(q(1-q)).

For x=arcsin(sqrt(q)), |x'| is bounded by the projected generator norm wherever 0<q<1. The bound extends through the endpoints: on each component with 0<q<1 integrate up to epsilon-level endpoints, then take epsilon to zero and use continuity. Equivalently apply the argument to regularized angles and pass to the limit. Thus |x(1)-x(0)|<=D_F. For x,y in[0,pi/2] at distance at most D<=pi/2,

    |sin^2 x-sin^2 y|=|sin(x+y)sin(x-y)|<=sin D.

For D>=pi/2 the trivial bound1 applies. Supremizing the Hermitian quadratic form gives(1); fresh-ancilla expectation, support compression and identity-reference amplification do not enlarge it. A two-dimensional rank-one projector rotated through angle d has effect norm sin d for0<=d<=pi/2, proving sharpness of the modulus.

For leakage use P=S tensor I_A. If the center's worst supported-input leakage is at most b, the same angle inequality gives

    ell(theta)<=sin^2(min(pi/2,arcsin(sqrt(b))+D_P)).         (2)

The inequality is uniform over supported inputs and references. It is sharp for a rotation between one supported and one unsupported vector, beginning at angle arcsin(sqrt(b)). At b=0 it grows quadratically, sin^2 D_P, rather than linearly. A fixed supported carrier and global path bound are essential.

## 2. Circuit order, cancellation and exact contrary constructions

For V=U_L...U_1 put W_l=U_L...U_(l+1) and K_(l,a)=i(partial_a U_l)U_l*. Product differentiation gives

    G_a=i(partial_a V)V*=sum_l W_l K_(l,a) W_l* .           (3)

Thus a trusted uniform bound ||(I-F)G_a(theta)F||<=kappa_(F,a) yields along a straight path

    D_F<=sum_a kappa_(F,a)|theta_a-theta'_a|.               (4)

Keeping the norm of the sum preserves cancellations. Layerwise triangle estimates are valid but may be weaker. A layer sees the suffix-backpropagated effect W_l*FW_l, not generally the final F. Formula(3) also applies to calibrated finite controller circuits on the entire retained carrier; no branchwise reduction is silently made.

Counterexample: V_theta=H exp(-i theta Z), F=|0><0|, with H the Hadamard. Although [Z,F]=0, V_theta*FV_theta=exp(i theta Z)|+><+|exp(-i theta Z). Its difference from the center has norm |sin theta| and reaches1 at pi/2. The output generator is H Z H*=X, which has nonzero cross block. The raw-commutator shortcut fails.

Conversely, if all cross blocks (I-F)G_a F vanish throughout a connected coordinate fibre, then [G_a,F]=0 there (Hermiticity supplies the other block), so V*FV is constant on that fibre. To remove a coordinate from the calibration net, require this for Q,T and P everywhere on that fibre and a path connecting each point to its representative. No claim about complete-channel equality follows. A local vanishing derivative is insufficient: leakage sin^2 theta has derivative0 at theta0 and leakage1 at pi/2.

An explicit globally invisible family is

    V_(theta,phi)=(exp(-i M phi Z_C) tensor I_D)
                  (I_C tensor R_theta),

where all Q,T,S are identity on C. The phi-direction has zero cross blocks for every M, while its full generator norm is |M|. Its entire phi range needs no calibration mesh. A two-coordinate cover therefore reduces to one coordinate, without a dimension-free assertion for arbitrary circuits. The symmetry must be proved on the full carrier; tracing a coherent selector is not such a proof.

## 3. Uniform calibration and consumer

After removing only proved invisible coordinates, choose a finite h-net in the remaining p_eff coordinates on[0,1]^p_eff. Then N<=(ceil(1/h)+1)^p_eff; if p_eff=0 use one representative. Put kappa_E=max_R sum_a kappa_(R,a), kappa_S=sum_a kappa_(P,a). For desired0<epsilon_D,ell_D<1 choose

    a=epsilon_D-sin(min(kappa_E h,pi/2))>0,
    kappa_S h<arcsin(sqrt(ell_D)),
    b=sin^2(arcsin(sqrt(ell_D))-kappa_S h)>0.              (5)

At each center certify effect error<=a and leakage<=b. Equations(1)--(2) certify every allowed parameter, and K2508's convex transfer certifies all actual and proof-hybrid history-conditioned mixtures. Every such map must belong to this declared family or convex hull; finite tests do not establish stationarity, model membership or hidden-memory bounds.

With retained controller dimension G, supported data/memory dimension d and trusted pooled bias eta_eff, K2508's basis-control scheme has

    W_G=G(2d/a^2+d/b), v=1/W_G-eta_eff>0,
    total shots=N ceil(log(N/alpha)/[-log(1-v)]).           (6)

This is sufficient all-zero passing-data effort, not predicted observations or universal optimal sample complexity. Confidence failure alpha is separate from within-event record error. A nonpositive margin cannot be cured by more shots. The unchanged two-gap consumer is

    E<=min(1,1024epsilon_D+1024sqrt(epsilon_D ell_D)+ell_D).

For epsilon_D=ell_D=10^-6, E<=2049/10^6. If ideal acceptance>=1/2 and ideal bad-and-accepted mass0, conditional error<=2049/497951<1/200.

A concrete conservative feasible design sets a=epsilon_D/2,b=ell_D/4 and h small enough that kappa_E h<=epsilon_D/2 and kappa_S h<=sqrt(ell_D)/2. The effect inequality follows from sin x<=x. For leakage, arcsin(z)-arcsin(z/2)>=z/2 for0<=z<=1 by integrating the derivative>=1. For d=108,G=2,alpha=1/100, zero bias, kappa_E=kappa_S=1 and epsilon_D=ell_D=10^-6, take h=1/2000000. If one visible coordinate and one globally invisible coordinate exist, N<=2000001, compared with the unreduced square (2000001)^2. The pooled weight is exactly1728000864000000. This is an explicit but impractical cost, not a proposed apparatus. Angular leakage alone permits h up to sqrt(ell_D)/2 at this center allowance; the effect requirement is the active bottleneck here.

## Evidence, controls and next condition

The exact probe checks the projector/effect rotation, sharp leakage composition, circuit suffix order, coherent-controller invisibility, genuine downstream-Hadamard and local-derivative contrary controls, and rational calibration/consumer budgets. The written theorem covers all paths under its hypotheses; finite fixtures do not prove the universal result.

A physical implementation still owes trusted joint preparation/readout, complete memory support, stationary generators and global cross-block bounds. Within this conditional model the remaining optimization is an effect-weighted anisotropic cover and implementation cost, not another generic Duhamel constant. Native I1B matter/light and positive physical quotient remain separate missing constructions.

[Exact probe](../../tests/channel-swings/k2510_effect_path_calibration_probe.py), [saved report](../../lab/process/k2510-effect-path-calibration.json), [K2508](k2508-controller-coverage-2026-11-02.md), [K2506](k2506-calibration-deployment-transfer-2026-11-02.md).
