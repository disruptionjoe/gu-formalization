---
title: "K2236 Ordinary pullback, minimal dynamic augmentation and incompatible Green descent"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-plane pullback and minimal local quotient for the supplied raw operator; no source-selected observation, gauge quotient or physical exclusion
scripts:
  - tests/channel-swings/k2236_raw_observation_closure_probe.py
---

# K2236 The supplied positive sector is invisible to ordinary fixed-plane pullback

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

```gu-typed-objects
result: minimal dynamic refinement of fixed-plane ordinary pullback and its Green/current boundary
carrier: supplied real1920 Cl77 raw carrier and real768 quotient on a fixed observed plane LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: arbitrary full raw Green pairing and separately positive local evolution-current candidate ON=declared_carrier
real_structure: ordinary conjugation in fixed real Clifford basis; Fourier consumer complexifies explicitly
grading: zero/one-form degree and copy splitting, not physical chirality or family count
action_owner: repository-construction -- fixed raw contraction, common lower coefficients and supplied observation plane
target: ordinary section pullback versus dynamically closed local quotient MAP-TYPE=intertwiner
```

## 1. Changed question and inherited inputs

K2233 exhausts the smooth raw Green pairings for its supplied mass/flavor connection. K2230 supplies a moving rank576 projector inside the positive V1152 sector. Neither selects that projector as ordinary section pullback. The new question is whether the ACTUAL one-form pullback to the declared fixed plane can serve as a closed output of the same raw operator, and what its smallest local dynamic refinement retains. K2034 already owns the V/C split and all six-slot evolution/Jordan formulas; K2200 owns principal-pairing completeness; K2206 owns the mass-only constant positive-sector maximum. These are inputs, not new classifications.

The source extraction `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` records four independent classical fields, sixteen cells and the original negative lower-left quadrant, at candidate strength. The raw real1920 construction here is a particular contraction on unbarred one-form plus zero-form slots, not a reconstruction of all source choices. The source-native observation obstruction of 2026-08-30 already proves that ordinary pullback need not preserve an ambient gamma kernel. Our result computes a different bridge: the closed evolution quotient of this specified raw operator. SC-OP-04 ASSERTS candidate grammar only; SC-OP-05 and SC-META-53 remain UNCERTAIN. LT-SM8 and LT-GR6b remain NEEDS at ledger0.263. No row distance or source verdict changes.

Use O={0,7,8,9}, U={1,2,3,4,5,6,10,11,12,13}, eta=(+1 seven,-1 seven), J=gamma0...gamma13, W=(3I-J)/2, Wbar=(3I+J)/2. Normalize raw fields by zeta_a=eta_a gamma_a u_a and nu=Wbar h. On a constant/adapted observed plane, ordinary one-form pullback retains zeta_a for a in O and annihilates the ten normal covector slots; scalar pullback retains nu. After the invertible output normalization its exact map is

    Q u=(u0,u7,u8,u9,h), rank640.

This is genuine ordinary pullback for THIS fixed plane. Neither its global geometry nor the conditional real128 parent has been selected by the source. The source metric section may move; normal derivatives and moving Clifford frames are outside this fixed-plane theorem. The additional quantity below is an explicit normalized normal-slot sum; no unsupported claim of its frame-independent source selection is made.

## 2. Exact raw data and the lost normal sum

The original raw matrices have D_k[a,c]=eta_a gamma_a gamma_k gamma_c W for distinct a,k,c<14, D_k[k,h]=I, D_k[h,k]=-eta_k I, all other blocks zero. In normalized coordinates D_k=M_k tensor Gamma_k, Gamma_k=gamma_k Wbar, with M_k[a,c]=1 for three distinct one-form indices, M_k[k,h]=1 and M_k[h,k]=-1/2. These are the original bottom returns, not fitted adjoints.

Put sigma=sum_U u_r. Then ker Q has dimension1280. Its subspace V={Q u=0,sigma=0}, dimension1152, is invariant under each observed D_k (k in O) and all K2233 lower coefficients. Q annihilates every field in V, including every supplied rank576 projector inside V. This is a precise failure to identify those supplied observations with ordinary pullback, not a failure of their positive dynamics.

For n in ker Q, direct inversion of M0 gives, for j in{7,8,9},

    (Q D0^-1 D_j n)_0=0,
    (Q D0^-1 D_j n)_j=(11/12) Cj sigma,
    (Q D0^-1 D_j n)_l=-(1/12) Cj sigma  (l spatial, l!=j),
    (Q D0^-1 D_j n)_h=Cj sigma,
    Cj=gamma0 gamma_j, Cj^2=I.

Consequently the largest subspace inside ker Q invariant under all spatial evolution matrices is exactly V. Indeed invariance forces the last output to vanish, hence sigma=0; the converse is the inherited invariance of V. A single j is already sufficient for this necessity. This proof uses evolution matrices, not just raw symbols.

Q does not admit a deterministic first-order autonomous evolution on unrestricted output fields. For example take alpha=0 and mass m constant on a spatial torus, with initial data only in normal slots and sigma=sin(x7)s for a nonzero constant spinor s. This finite Fourier datum has an exact finite-matrix evolution. The zero-order evolution coefficient is diagonal in those slots and has no Q-output. But the displayed principal leakage yields nonzero initial time derivative of Q u. Zero initial Q therefore does not determine its future. Compactly supported data give the same initial-jet obstruction without asserting global evolution on that full carrier.

Do not call QD0 an observed time derivative. The algebraic principal-response augmentation (Q,QD0) determines sigma because (D0u)_7=Gamma0(u8+u9+sigma). It requires access to a supplied principal response. Measured partial_t(Q u) instead contains spatial derivatives of sigma. In the mass-only example spatially constant sigma remains invisible at zero momentum. Constant functions are absent from L2(R3) but present on a torus; no automatic local recovery from time data follows.

## 3. Minimal pointwise refinement and its actual dynamics

Let R(x) be ANY pointwise linear output map, possibly smooth and moving, such that Q factors through R and the original equation induces a first-order evolution quotient on R u. Its leading symbols require ker R invariant under every D0^-1 D_j. Derivatives of R only affect lower-order terms. Since ker R is contained in ker Q, the previous theorem gives ker R subset V, hence rank R>=768 at every point. This is a theorem about pointwise linear, first-order evolution quotients. It excludes neither nonlocal outputs, derivative-valued observations, higher-order elimination nor solutions with additional constraints.

The bound is attained by

    R u=(a,b1,b2,b3,v,h)=(u0,u7,u8,u9,sigma/10,h).

Its kernel is V. Embed these six slots by setting every normal u_r=v; denote the embedding E. Then R E=I and E R=I-PV. All original observed principal coefficients (k in O) and declared lower coefficients preserve V and the complementary E-space C, so the quotient is exactly the restriction to C, not an arbitrary fitted receiver. This remains true for K2233's Omega0=mA+sum a_j CjT, Omega7=b C7T, all other Omega zero; A=gamma0 J and T=product_U gamma_r.

For the quotient principal evolution every output receives Cj, multiplied by the following scalar T_j:

    a'=b_j,
    v'=(h+2v-sum_(l!=j)b_l)/12,
    b_l'=b_l-v+v' (l!=j),
    b_j'=a+sum_(l!=j)b_l+9v-h+v',
    h'=sum_(l!=j)b_l+10v.

For alpha=0 the mass-only lower evolution is exactly diagonal on these slots:

    m diag(-A,A,A,A,A,A Wbar^2/2).

For general alpha the correct quotient lower coefficient is R D0^-1 K E with the SAME original K=sum D_k diag(Omega_k). This is a finite construction, not an independent adjoint or action fit. The probe verifies full raw invariance for all five coefficient generators; the mass formula and all principal quotient formulas are separate controls.

## 4. What the minimal quotient does not inherit

**No positive local current on the complete quotient.** K2034 proves, and the exact six-slot calculation checks, that N_j=T_j^2-I has rank1, N_j!=0 and N_j^2=0. Thus T_j is not diagonalizable. Since Cj is a symmetric involution, T_j tensor Cj remains defective. A positive-definite local energy density G would require G(T_j tensor Cj) to be Hermitian at each point, making that matrix similar to a Hermitian matrix and therefore diagonalizable. Contradiction. Smooth G or lower coefficients do not change this principal condition. Positive subsystems remain possible: K2034's massless256 inside C is retained, and the original V1152 positive dynamics is retained upstairs. For constant nonzero mass and alpha=0, K2206's maximal positive invariant-sector theorem further says every constant positive invariant sector of the full system lies in V, so none nonzero lies in C.

**No nonzero inherited full raw Green form on this quotient when m is nowhere zero.** K2233 classifies every such form: C lies in its radical, all support is on V. A bilinear form descends through R only if ker R=V lies in both radicals (and for the classified forms left/right support agrees with the split). Combining these statements forces the entire form to be zero. Thus the minimal ordinary-pullback refinement erases the very sector supporting all nonzero raw Green forms. This is a descent statement for that unchanged raw pairing class, not a no-action theorem: an independently introduced action, multiplier, doubled cotangent system, altered principal operator or restricted subsystem is a different object. V is not being labeled gauge.

**Optional exact one-dimensional high-frequency consumer, massless only.** Set m=alpha=0 and restrict to fields depending on one observed spatial coordinate on a torus. Write A_j=T_j tensor Cj, N=A_j^2-I and S=A_j(I-N/2). Then S^2=I, [S,N]=0, N^2=0 and

    exp(-it n A_j)=(cos(nt)I-i sin(nt)S)(I-i nt S N/2).

The first factor and its inverse are uniformly bounded in n; choosing w with Nw!=0 proves growth bounded below by c|nt|-C. The same expression gives an upper bound C(1+|nt|). Hence the one-dimensional massless system has exactly one derivative of Fourier growth at every t!=0: bounded H^s to H^(s-1), unbounded H^s to H^s. This is a direct finite-matrix/Fourier proof, not a claim about the complete massive three-dimensional propagator. It explains concretely what the minimal refinement retains from the inherited Jordan defect.

## 5. Controls, contrary constructions and missing inputs

The strongest overclaim would make a source-native observation failure out of one conditional fixed-plane raw contraction. The actual source has not selected the bar, real carrier, contraction, section, boundary/gauge quotient, common domain or physical action. The source-admitted southeast rival also remains live. A changed principal/normal frame, moving geometric section with its own connection, source-owned constraints, or a genuinely different observation can change the theorem's premises. K2230's moving projector and K2233's positive curved V dynamics remain valid supplied constructions, now proved distinct from Q.

The weakest seam is confusing a raw principal response with an actual observed time derivative. The explicit QD0 formula, evolution leakage, finite-Fourier counterdata and zero-momentum countercontrol prevent that substitution. The other seam is assuming that quotienting a radical and quotienting the support are interchangeable: the complete Green classification puts C in the radical, whereas ordinary-pullback closure quotients V. Their opposite roles are the substantive new bridge.

The exact probe checks normalized original returns, V/C invariance for all mass/flavor generators, quotient projection/embedding, full scalar principal intertwining, hidden-sum leakage, ranks, nonzero Jordan witnesses, and the exact polynomial Fourier-factorization identities. Planted faults change return sign, scalar averaging, 11/12 leakage, a quotient matrix entry, a mass sign, or the half-factor in the Jordan decomposition. Written universal kernel/rank/current/descent proofs remain distinct from finite exact controls. Independent internal specialist review checked the kernel, minimality, current, Green descent and Fourier arguments; it required making the observed-only derivative restriction explicit. No external-expert, proof-assistant, novelty, physical recovery or GU-wide exclusion is claimed.


## Reproduction

Run `python tests/channel-swings/k2236_raw_observation_closure_probe.py`. The default recomputes all exact controls and genuine coefficient faults and rejects stale note/probe/dependency hashes. `--write` refreshes the report after review. The finite controls do not replace the written universal arguments.
