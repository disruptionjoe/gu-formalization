---
title: "K2431 Polynomial null sections for the quintic boundary"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional null lifting and scoped boundary discriminators; no new complete Euler jet or native GU verdict
scripts:
  - tests/channel-swings/k2431_quintic_vanishing_ideal_probe.py
---

# K2431 Polynomial null sections for the quintic boundary

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
result: K2431
carrier: original 168-dimensional repeated-hook space on the fixed fourteen-dimensional curved model LAYER=toy CHIRALITY=N/A
pairing: original nondegenerate split Gram matrix and K/q contraction covectors ON=declared_carrier
real_structure: Q(sqrt2), without coefficient-field extension
grading: hook slots versus homogeneous symmetric derivative degree
action_owner: repository-construction -- inherited conditional hook model
target: polynomial null lift and simultaneous boundary compatibility inside a fixed null section MAP-TYPE=evaluation
```

## Result

The next norm condition exposed by [K2429](k2429-shared-eighth-euler-extension-2026-11-01.md) has a constructive repair route that does not divide by a coordinate polynomial. The original fourteen K/q contraction covectors span a totally isotropic dual space. An explicit constant linear section lifts **every polynomial K/q target to an identically null repeated hook**. This applies to arbitrary mixed-quartic forcing in the K targets, not just a pointwise value or a selected monomial.

A simpler proposed repair, setting the quintic to zero on Z={w0=w1=w2=0}, is impossible already at seventh order. The exact target has a nonzero 17-term obstruction to that restriction. Nonzero and null are compatible in the split Gram form; this negative test does not exclude the null-section construction.

The executed coupled-boundary test separates the real remaining issue. In one explicit null section, the seventh/eighth equations fail when its K targets are set to zero, but have a polynomial solution if those targets are freely chosen. One explicit sufficient choice of K targets is stored. **They have not been matched to an admissible shared lower quartic.** The null section therefore supplies a construction method and a concrete compatibility test, not a new common finite jet beyond K2429.

SC-ACT-01 ASSERTS the distinct first action and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. These conditional hooks have no supplied identification with that native action/displacement. Source polarities, physics ledger0.263 and canon remain unchanged; no all-order, smooth, physical or GU claim follows.

## 1. Why setting the quintic to zero cannot work

Keep the repaired cubic and W4 from K2423, digest `2632127837a3051e07e50c59bf244c1c8cd27a5af0867b0c550b791460920610`. In the literal repeated frame, let

    q(h)=G(N_W,h), t(h)=G(T_W,h), r(h)=G(R4W,h),
    J=(w0,w1,w2), ell=w3-(20736/1445)sqrt2*w4,
    I=q(repeated hooks)=(w0,w1,w2)^2+(w0*ell).

The actual seventh boundary requires

    q(R5W)=S7=-(5/3)G(T_W,R4W).

If every component of R5W belonged to J, then S7 would belong to JI. This condition is necessary even after all nonconstant polynomial syzygies are restored. Direct reconstruction of the original tensors reproduces the 830-term S7 from K2425. Its normal-degree-two part has 33 terms; substituting w3=(20736/1445)sqrt2*w4 leaves 17 nonzero terms. But the normal-degree-two part of JI is w0*ell*J. Hence S7 is not in JI.

The probe also computes the full Groebner remainder against the 21 original generators w_a*q_i, a=0,1,2, giving a second exact view of the same obstruction. This rejects vanishing on Z, not a nonzero isotropic restriction, another lower jet or every smooth solution. It does not replace K2429's whole-fiber warning with a stronger unsupported no-go.

## 2. Original isotropic covectors and a polynomial null section

Let V be the original repeated-hook vector space, dim168, with the original symmetric Gram matrix G. The seven K contractions give a matrix P_K. In coordinates (w0,w1,w2,ell,w4,w5,w6), let Q_N be the seven coefficient covectors of

    w0*ell, w0^2, w0*w1, w0*w2, w1^2, w1*w2, w2^2

in q(h). Stack L=[P_K;Q_N]. Original hook contractions, not a fitted abstract form, give

    rank G=168, rank P_K=rank Q_N=7, rank L=14,
    L G^(-1) L^T=0.                                   (1)

Choose any constant right inverse D of L and set

    A=G^(-1)L^T, M=D^T G D,
    D0=D-(1/2) A M.                                   (2)

Then

    LD0=I14,
    D0^T G D0=M-M/2-M/2+(1/4)M(LG^(-1)L^T)M=0.       (3)

For any fourteen polynomial targets F(w), R(w)=D0 F(w) therefore satisfies LR=F and G(R,R)=0 identically. Constant matrices preserve homogeneity and the coefficient field. No coordinate is inverted, no separate solution is selected at each point, and no square root outside Q(sqrt2) is introduced. This is elementary split-form linear algebra; novelty is not claimed. Its useful evidence here is the exact original identity (1) and its application to these native coefficients.

The last seven columns Dq lift arbitrary q-coefficient polynomials with K targets zero. A homogeneous original-generator lift of S7 in I yields one identically null degree-five hook satisfying the seventh boundary. Its restriction to Z is nonzero, as section1 requires. The report stores all168x14 entries of D0; the probe independently checks all pairwise Gram products and all fourteen original contractions. A mixed fixture exercises all seven K targets as well.

This also handles the full pre-eighth family abstractly: arbitrary actual K forcing can be included as the first seven entries of F. It does not preserve t/r targets of an arbitrary previously repaired quintic. Those targets must be solved jointly in the chosen section.

## 3. Execute the coupled eighth test, keeping the restriction visible

Write a quintic in the fixed null section as

    R5W=DK*k(w)+Dq*f(w).

The seven K targets k are fixed by lower mixed-quartic choices in the full problem. The seventh equation fixes q0*f=S7, where q0 is the seven-form list above. Let f0 be one homogeneous lift and Syz(q0) its complete polynomial syzygy module. Every solution is f=f0+s with s in that module; using only a constant kernel would omit legal freedom.

The eighth equation modulo I is

    [56 t(DK*k+Dq*f)+35G(R4W,R4W)]=0 in P/I.           (4)

The probe computes the full eleven-generator syzygy module and checks each original identity. Independently, the 21 pairwise LCM syzygies of the seven monomials in ell coordinates generate the complete monomial syzygy module; after substitution, their t-image ideal is checked equal in both directions to the eleven-generator image ideal. Its image under t(Dq·) gives the exact additional ideal generators for this section. With k=0, the actual fixed target

    B8=56 t(Dq*f0)+35G(R4W,R4W)

has a nonzero remainder (43 terms). Thus no choice of *any polynomial q-syzygy in this fixed K-zero section* can solve that eighth equation. This is not a claim that the real lower quartic has k=0.

As a constructive countercontrol, allow all seven k polynomials to vary and add t(DK_j) to the same ideal. B8 then has a homogeneous exact original-generator lift. Reconstructing its coefficients gives R5W and R6W with

    G(R5W,R5W)=0,
    q(R5W)=S7,
    28q(R6W)+56t(R5W)+35G(R4W,R4W)=0.

The probe directly verifies all degree-eight coefficients and records one sufficient choice of seven K polynomials. These freely selected polynomials are **not** a substitute for the lower-jet-derived K forcing. The result shows that this null section is not excluded by the seventh/eighth scalar equations alone, and supplies one explicit sufficient K target to test against the lower-quartic image. Other K targets in the full affine compatibility module remain available.

Let E=I+t(Dq Syz(q0)) and eta(k)=[56 t(DK*k)] in (P/E)_8. If admissible lower quartics give k=k0+Klin(u), the complete test is eta(Klin(u))=-[B8]-eta(k0), jointly with the existing lower constraints. Matching only the stored sufficient target could miss solutions. The complete actual question is linear after this null-section restriction: solve lower Euler/algebraic constraints, the K-forcing relation and (4) on the same lower coefficients. A success would repair the quintic-square obstruction on Z. A failure would reject this particular constant null section; different null sections and non-section polynomial null fields remain possible.

## 4. Ninth-boundary follow-through and Euler scope

The ninth source is 84t(R6W)+126r(R5W), modulo q(R7W). The old ideal I+t(Cq), with Cq the 154-dimensional constant q-kernel within the K-polar subspace (preserving both K and q), permits changes to R6W preserving its eighth equation while keeping R5W fixed. The probe tests every r(D0_j) against that ideal and tests the actual relaxed solution's ninth source separately. Nonzero generator remainders show that no automatic transfer theorem follows merely from the null section. The relaxed fixture has a nonzero seven-term ninth remainder in that restricted ideal, stored exactly in the report. This excludes a q/t(Cq)-only repair of that fixed relaxed representative; it does not exclude coupled seventh/eighth changes or the full family.

A further repair may vary R5W inside the same null section using the *coupled* seventh/eighth syzygy module, or change the section. The larger K2427 repair uses Cqt quintic corrections; applying it blindly here can leave the null section and reintroduce the norm. That is a live coupled condition, not permission to combine unrelated existential witnesses.

Once the actual boundaries have a common solution, the previously certified repeated-polar W5-zero corrections and literal frame rotations preserve its chosen inner R5W while restoring fifth Euler and seventh compatibility. Orthogonal frames preserve nullity. This reuse does not solve the unperformed lower-quartic matching or ninth/tenth equations, and no new Euler rank is counted here.

## Verification and next question

The [probe](../../tests/channel-swings/k2431_quintic_vanishing_ideal_probe.py) reconstructs original hooks, Gram and K/q covectors; checks the null section; independently reconstructs S7 and R4 norm; executes the zero-restriction obstruction; and supplies original-generator certificates for the relaxed eighth solution and the exact ninth diagnostic. The [report](../../lab/process/k2431-quintic-vanishing-ideal.json) separates those exact statements from inherited finite-jet evidence. Numerical samples and Boolean manifest assertions are not the proofs.

The next decisive test is whether a *single admissible lower quartic* supplies K forcing satisfying the null section's eighth module, then its ninth boundary. The reported relaxed K polynomials are one sufficient target, not an accepted input or a necessary unique choice; test the full admissible affine K module. Preserve the complete lower affine fiber, all nonconstant syzygies and the option to rotate the null section. K2429 remains the current complete eighth-Euler/ninth-algebraic theorem.

Reproduce with SageMath10.9, one process:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 sage -python tests/channel-swings/k2431_quintic_vanishing_ideal_probe.py
```
