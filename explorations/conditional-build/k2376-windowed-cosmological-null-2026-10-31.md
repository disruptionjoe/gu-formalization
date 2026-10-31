---
title: "K2376 Which window operators preserve the cosmological density null"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite observation mathematics; no measured cosmological null
scripts:
  - tests/channel-swings/k2376_windowed_cosmological_null_probe.py
---

# K2376 Which window operators preserve the density null

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
result: K2376
carrier: finite joint two-epoch real potential vectors and density observations LAYER=toy CHIRALITY=N/A
pairing: ordinary finite real covariance and supplied noise covariance ON=declared_carrier
real_structure: real linear finite mode model
grading: classical scalar observation channels; no fermion grade
action_owner: repository-construction -- fixed conditional quadratic metric f(R) with conserved dust
target: observation-window factorization and exact minimal measurement repair MAP-TYPE=evaluation
```

## Scope

[K2373](k2373-two-epoch-cosmological-observability-2026-10-31.md) supplies a derivative-free density row g_k on four potential readouts at each mode, conditional on its invertible two-epoch matrix. This note does not change the background, fit or state equations. It tests whether a **supplied joint observation** preserves that relation. SC-COS-50/51/54 ASSERTS retain their meaning; LT-GR2e remains open. No lightcone kernel, tracer law, statistical homogeneity, primordial spectrum or physical calibration is supplied. The source connection displacement is not identified with metric f(R).

## Exact transfer and failure theorem

Stack y in R^(4m), D=blockdiag(g_1,...,g_m), observed potentials p=Uy, observed densities d=VDy. A seed-independent linear predictor d=Kp exists exactly when

    VD=KU  iff  ker U subset ker VD
            iff row(VD) subset row(U)
            iff rank([U;VD])=rank U.                       (1)

Necessity follows by taking a seed in ker U. Sufficiency defines a well-defined map Uy -> VDy on im U, then extends it to the observed potential space. No covariance or invertibility of U is needed. Every deterministic relation among all observed channels is a left null of H=[U;VD]; (1) tests the stronger requirement of predicting every density row.

For a common single window p=sum a_k y_k and d=sum a_k g_k y_k, restrict to modes with nonzero a_k. A predictor exists iff all supported g_k coincide: varying one mode independently forces K=g_k. If two differ, H has row rank five (the four potential rows are independent and density adds one). With **unrestricted joint latent covariance**, every five-channel PSD covariance then occurs: choose a right inverse J of H and set latent covariance J Sigma J^T. This is not a theorem with independent modes or a fixed primordial covariance imposed.

Thus matching windows alone does not preserve the latent null. A concrete two-mode example has g1=(1,0,0,0), g2=(2,0,0,0), U=[I I], V=[1 1]. Choosing y1=e1, y2=-e1 gives p=0,d=-1. An exact right inverse sends (p,d) to y2=e1(d-p1), y1=p-y2. This is signal information loss, not noise or numerical conditioning.

## Minimal repair, including the useful successor

The minimum number of arbitrary new noiseless linear potential measurements needed to predict all density outputs is

    r_add = rank([U;VD])-rank U.                           (2)

Each added scalar row increases the span by at most one. Conversely add a basis of row(VD) modulo row(U); the span then contains every required row. This is an algebraic minimum, not a claim that any physical instrument measures those rows.

In the fixture one extra scalar c=y1,1-y2,1 suffices:

    d=(3/2)p1-(1/2)c,
    n=(-3/2,0,0,0,1/2,1),  n[p;c;d]=0.                   (3)

For any two modes, writing gbar=(g1+g2)/2 and Delta=(g1-g2)/2 yields d=gbar p+Delta(y1-y2). Thus only the response-weighted contrast is needed, not separate recovery of all eight latent components. If its instrument is absent, a pseudoinverse cannot create it.

## Noise, wrong null, and calibration boundary

For latent Cov(y)=I8 the fixture gives Cov(p)=2I4, Var(c)=2, Cov(p,c)=0, Var(d)=5, Cov(p,d)=3e1 and Cov(c,d)=-1. Hence n Sigma=0. Supplied independent noise N=I6 gives n N n^T=7/2. Omitting c and testing d=(3/2)p1 leaves de-noised variance1/2 in a valid model: a false rejection caused entirely by an invalid observation bridge.

More generally set E=VD-KU and R=[-K,I]. For observed z=Hy+epsilon and uncorrelated signal/noise,

    Cov(Rz)-RNR^T=E Cov(y) E^T.                            (4)

With cross covariance C=Cov(y,epsilon), add E C R^T+R C^T E^T. For an **exact** true null E=0, Rz=R epsilon identically even with correlated noise. Thus exact-null residual noise remains valid; a mismatched-model excess requires its cross-covariance assumption. Singular latent covariance may hide E on unexcited directions; no universal test power follows from nonzero E alone. If calibrated bounds Cov(y)<=P and ||E||<=epsilon are available, residual signal covariance<=epsilon^2||P||I; absent a covariance bound, arbitrarily small nonzero mismatch has unbounded possible power.

The optimal supplied-noise metric projection onto a full-row-rank exact constraint Rz=0 has cost (Rz)^T(RNR^T)^(-1)(Rz) when N positive definite. This reuses K2373's projection principle on the actual repaired window relation; it is not an observed chi-square law without a sampling model.

## Actual stored-history consumer and limits

The probe reads K2373's saved density rows at k r_d=0.1,1,10, keeps their finite precision explicit, and constructs the two-mode common-window obstruction and response-weighted contrast repair from the first two rows. Their third coefficients differ by about1025.698056. For y1=e3,y2=-e3 the aggregated potentials vanish while the stored density does not. This verifies the information-loss mechanism on the already computed witness, rather than a new fit or ODE. Exact rational calculations on decimal storage do **not** certify the underlying numerical continuum coefficients. A true observational conclusion still requires validated kernels, noise/cross-covariance, excitation and transfer error bounds.

## Evidence and next condition

The exact probe tests factorization, full-row-rank covariance saturation via an explicit right inverse, the minimal scalar repair, covariance/noise algebra, a wrong-window control, unchanged-coefficient escape, singular-excitation escape, and signal/noise correlation countercontrol. Finite stored coefficient arithmetic is separately labeled. Universal conclusions use the written linear-algebra proofs; internal specialist review is not external expert or proof-assistant certification.

Next instantiate actual finite survey/mode/tracer operators U,V and their admissible measurement rows, then test (1) before fitting a null. A failed factorization identifies exactly which contrast or physical prior is missing. A passed factorization still owes calibration and uncertainty. No source, ledger or canon verdict changes.
