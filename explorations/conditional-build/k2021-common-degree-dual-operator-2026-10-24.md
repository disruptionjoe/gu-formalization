---
title: "K2021: One common degree-dual operator, including moving density and reality"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional full-carrier construction; no source selection, positive physical quotient, GU verdict, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2021_common_degree_dual_operator.py
  - tests/channel-swings/k2021_common_degree_dual_operator_probe.py
---

# K2021: One common degree-dual operator, including moving density and reality

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
result: explicit common density dual and complete local formal Green identity
carrier: full real1920 K77 rolled carrier, complexified without removing either64-dimensional spinor half LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: rho times C transpose H C, real symmetric inertia960/960 ON=full_zero_and_one_form_spinors
real_structure: ordinary conjugation on the complexified real Cl(7,7) representation; optional invertible antilinear density-dual map
grading: actual ambient Clifford volume labels on external fields, not total form grading
action_owner: repository-construction -- supplied flat background, non-null q and density
target: full local density-valued differential operator MAP-TYPE=intertwiner
```

## 1. New construction, inherited inputs, and scope

The August [source-sign reconciliation](../k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md)
already found the two degree-sensitive parity assignments, the need for an odd
covector, and explicit q-modified symbols. This is **not a new parity solution**.
The [August10 graph test](selected-k77-degree-duality-pair-graph-gate-2026-08-10.md)
rejects a canonical q on its proposed W/mirror RS graph; it expressly retains
q as a map on the full one-form carrier. No retired graph is reopened here.

The new result completes a particular full-carrier assignment with one common
nondegenerate symmetric form, its involutive formal adjoint, every derivative
of q and density, an optional antilinear density dual, and its Green current.
It uses the actual weighted triple-gamma principal matrices from
[K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md), not a compressed
positive core or a substituted one-gamma contraction. It is a local conditional
construction on a flat K77 patch. The freely supplied q and density are not
selected by the source, an action equation, or observation.

The reverse demand is a single real variational pairing compatible with the
whole differential operator before claiming a positive physical state. K2022
then tests that stronger dynamical demand; formal adjoint compatibility alone
is not its answer. No source action is required as an eligibility condition.

## 2. Actual matrices and common flat pairing

Let gamma_k be the real128 Cl(7,7) matrices, eta=(+1 seven times,-1 seven
times), J=gamma_0...gamma_13, W=(3I-J)/2 and

    B=gamma_7...gamma_13,
    B^T=B, B^2=I, BJ=-JB, gamma_k^T B=-B gamma_k.

B has inertia(64,64): J exchanges its positive and negative eigenspaces.
On E=(V* tensor S) direct-sum S, ordered (zeta,nu), set

    H=diag(eta_0 B,...,eta_13 B,B).

H has inertia(960,960). Keep EXACTLY K1951's constant matrices:

    (D_k)_(a,c)=eta_a gamma_a gamma_k gamma_c W
                  if a,k,c are pairwise distinct, otherwise0;
    (D_k)_(a,nu)=delta_(a,k) I;
    (D_k)_(nu,c)=-eta_c delta_(c,k) I;
    (D_k)_(nu,nu)=0.                                      (1)

The matrix conventions in(1) control all signs. They are a repository
realization, not a silent identification of the printed source star.
Direct multiplication on all1920 coordinates proves

    D_k^T H+H D_k=0 for every k.                          (2)

Analytically, the triple gamma is B-self-adjoint, swapping a and c changes
its sign, and W passes through the odd triple with J's sign reversed.
The eta factors supply the form metric; the off-diagonal blocks in(1) satisfy
(2) together. Thus D=sum D_k partial_k is formally self-adjoint for H on
compactly supported fields. This is an integration-by-parts assertion,
not a coefficient transpose shortcut.

## 3. Explicit degree-dependent maps without changing external labels

Supply any smooth real covector q on the patch with g(q,q) nowhere zero,
and any smooth positive density rho dx. Let Q=gamma(q), so
Q^2=g(q,q) I and Q^-1=Q/g(q,q). Set

    C_1=I on one-forms, C_0=Q on zero-forms,
    C=diag(I_(1792),Q),
    R=rho C^T H,
    h=rho C^T H C.                                      (3)

The output row maps are explicitly

    R_1=rho(g^-1 tensor B),   R_0=rho Q^T B.

C_0 is ambient-odd and C_1 even; R_1 is odd and R_0 even.
They implement one of the August sign assignments. External zeta+/- and
nu+/- remain the original ambient J half bundles. C is a **declared map to
auxiliary raw coordinates**, not a renaming of the source one-form labels.
All three density-valued principal blocks R D_k C preserve those external
half labels: odd+odd in the upper-left, odd+even+odd in the upper-right,
and even+even in the lower-left. In the extracted row order
(bar-zeta-,bar-zeta+,bar-nu-,bar-nu+) and column order
(zeta+,zeta-,nu+,nu-), this is precisely the six derivative-cell locations.
The southeast block stays zero. The same C and R are used in every cell.

These are not independent fitted row maps: R=rho C^T H, and h is their
common pairing. In particular Q^T B Q=-g(q,q)B, so

    h=rho diag(eta_0 B,...,eta_13 B,-g(q,q)B).             (4)

It is real symmetric and nondegenerate with inertia(960,960). The variable
norm of q does not change that inertia. A concrete patch is |x7|<1 with
q=dx0+x7 dx7 and rho=exp(2x7). This supplies an explicit local assignment,
not an existence statement waiting on an unknown coefficient.

## 4. All lower-order terms and the genuine formal adjoint

Write ell_k=partial_k log(rho), and define

    D_rho=D+(1/2)sum ell_k D_k,
    L_q=C^-1 D_rho C
       =sum A_k partial_k+V,
    A_k=C^-1 D_k C,
    V=C^-1 sum D_k(partial_k C)+(1/2)sum ell_k A_k.       (5)

Only the zero-form block of partial C is nonzero. The first term in V cannot
be omitted or commuted through D_k. h in(3) includes the density, so all
integration below uses dx rather than charging rho a second time.

For any operator L=A_k partial_k+V, its formal adjoint for h is

    L^{dagger_h}v=h^-1[-sum partial_k(A_k^T h v)+V^T h v]. (6)

Equations(2)--(5) give, for ALL smooth supplied q and rho,

    A_k^T h=-h A_k,
    hV-V^T h=sum partial_k(h A_k),
    L_q^{dagger_h}=L_q.                                 (7)

A short proof is U=rho^(1/2) C: h=U^T H U and
L_q=U^-1 D U. Applying the constant H integration-by-parts identity to Uu,Uv
proves(7) without assuming that q is constant or commuting coefficients.
Equivalently, expanding both sides yields the second equation in(7), the
coefficient identity checked by the probes.

For compactly supported complex fields, replace transpose of field values
by conjugate transpose; all coefficient matrices are real. The exact Green
identity is

    u^dagger h L_q v-(L_q u)^dagger h v
      =sum partial_k(u^dagger h A_k v).                  (8)

The induced formal adjoint is involutive because h is Hermitian and
nondegenerate; positivity is unnecessary. An optional antilinear duality is
u -> u^dagger h, with inverse alpha -> h^-1 conjugate(alpha)^T. Their
composition is the identity on E and its density dual. Ordinary complex
conjugation also gives a real structure commuting with this real operator.
This is a **supplied reality branch**; the four independent classical barred
and unbarred source fields are not thereby identified as source truth.

A simultaneous smooth change of spin frame transports the operator, C, H and
q and adds the usual derivative of that frame by operator conjugation.
Freezing q while rotating its Clifford/background data is not that transport.
No curved source connection, overlap cocycle, global non-null section or
closed physical domain is asserted.

## 5. Null fence, verification, and useful next test

At a nonzero null q, Q^2=0 and this Clifford multiplication has rank64; C is
not invertible. Equation(5) therefore does not extend this construction
through the null stratum. A line-valued, enlarged or nonlocal replacement
would be another branch. q=0 erases the zero-form map and is also excluded.

The producer verifies196 Clifford relations, all14 full raw Green matrices,
common pairing and inverse identities, all56 transformed half-support and
pairing instances at four rational points of the concrete moving example,
and the full Green coefficient including q' and rho'. The368 recorded checks
include eight actual omitted-q'/omitted-density failures. A separate tensor
column-action implementation imports no producer code: it verifies14 raw
identities,28 full transformed half-support identities and two moving Green
identities, and rejects14 wrong-lower-sign plus four omitted-term faults.
Three hashes verify provenance separately. The universal differential claim
rests on(2)--(8), not the four evaluation points.

Strongest overclaim: this is the source-selected bar or a positive physical
state. Neither follows. Strongest contrary evidence: the old restricted
W/mirror graph fails and the full raw system has Jordan growth; neither is
removed by a degree map. Weakest seam: missing derivatives of maps/density;
(5)--(8) and actual fault controls cover it. All checks are internal and
same-author; no independent expert, proof assistant or novelty acceptance.

SC-OP-04 ASSERTS candidate grammar; SC-OP-05 remains UNCERTAIN about the rival
southeast choice. SC-META-53 remains UNCERTAIN about physical positivity;
SC-META-56 DISAVOWS an odd-action prerequisite. The result does not test the
H210 superposition branch of CB7A or its internal144 slot, choose a source
mass, derive a physical quotient, or move LT-SM8/LT-GR6b, source, ledger or
canon. K2022 consumes this SAME completion to test the existing mass and
positive-evolution requirements before any stronger inference.
