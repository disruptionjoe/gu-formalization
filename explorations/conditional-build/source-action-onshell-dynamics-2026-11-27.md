---
title: Actual candidate dynamics and same-solution matter interaction
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T1
expected_delta: Test the held matter current on the actual signed-energy solution germs and derive a faithful fixed-kernel dynamics reduction before transferring frozen growth.
actual_delta: At both held roots the actual non-null microlocal generator excludes same-order local Duhamel bounds on the declared first-graph core. Separately the same signed-energy analytic germs have nonzero current in the held positive matter completion; physical admission and exchange remain unproved.
class_covered: Held W2/K95 full-U zero-matter candidate at both certified kappa1 roots; actual triangular full-carrier local analytic connection solutions and the already-held canonical-injection positive finite-band matter completion. Local tests do not select a physical domain.
premises:
- explorations/conditional-build/source-action-scalar-normal-operator-2026-11-27.md
- explorations/conditional-build/source-action-full-auxiliary-map-2026-11-26.md
- explorations/conditional-build/source-action-current-receiver-2026-11-26.md
- explorations/conditional-build/source-action-receiver-strategy-2026-11-26.md
- explorations/conditional-build/source-action-variable-completion-2026-11-25.md
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-02
- lab/sources/source-claim-register.yaml#SC-META-52
- lab/sources/source-claim-register.yaml#SC-META-53
source_bridge:
  status: conditional
  reason: Source grammar motivates the action and indefinite-spectrum question but does not select W2, this matter completion, or a source-required coupled physical state and boundary domain.
kill_condition: An actual dynamical or estimate failure excludes only its named candidate domain. Nonzero localized current, frozen growth, a failed ansatz or solver failure does not falsify GU.
---

# Actual candidate dynamics and same-solution matter interaction

program_target: LB-CLASS
tier: T1
expected_delta: Test the held matter current on the actual signed-energy solution germs and derive a faithful fixed-kernel dynamics reduction before transferring frozen growth.
actual_delta: At both held roots the actual non-null microlocal generator excludes same-order local Duhamel bounds on the declared first-graph core. Separately the same signed-energy analytic germs have nonzero current in the held positive matter completion; physical admission and exchange remain unproved.

Basis: freshly fetched `629e40b3a7c12191b88d02107039afabf2d1c9b8`.

```gu-typed-objects
result: actual microlocal no-loss estimate obstruction and same-solution current
carrier: W2 K95 imaginary-U connection forms; full-carrier triangular analytic germs and held positive finite-band matter columns with independent dual rows LAYER=ambient BRIDGE=physical_admission_unproved CHIRALITY=N/A
pairing: native indefinite trace/form pairing and separately held positive matter amplitude pairing ON=declared_distinct_carriers
real_structure: physical imaginary-U coefficients; independent matter bars, native K95 real form
grading: geometric SO3 and coefficient weights, not physical spins or family counts
action_owner: fixed repository-constructed W2 action with SE=-1/2
target: held matter action-current receiver and actual linearized evolution MAP-TYPE=endomorphism
```

No new action, coupling, physical state restriction, norm, boundary prescription
or dispersion is introduced. Coordinate/frame changes below rewrite an existing
operator. A diagnostic solution family is not installed as the physical state
space. Source2+1, contraction observation, primary-minus adjoint, independent
bars, fullU/optionalC and K95/K77 remain distinct.

## 1. What still needs testing

The preceding result proves actual local analytic linearized connection
solutions with either canonical patch-energy sign. It separately proves a
positive-real-part high-frequency eigenvalue of a frozen scalar-normal jet
operator. Neither fact establishes energy exchange with positive physical
matter or a physical ghost.

Two tempting shortcuts are inadequate:

- Arbitrary independent-bar local matter germs can detect any nonzero
  connection value: on pure scalar matter input, the full vertex has one-form
  output `(a_j nu)_j`. This gives a nonzero localized cubic density by analytic
  continuation of the matter seeds. Those arbitrary germs need not belong to
  the held positive paired completion.
- Adding a visible positive-sector solution to an invisible negative-sector
  solution can give negative total energy and nonzero current even in a
  completely decoupled direct sum. That cone argument does not show that the
  negative-energy component itself interacts.

A scalar cutoff also matters. For a conserved current and central gradient
`a=d sigma`, integration by parts gives
`integral chi j.d sigma = -integral sigma j.d chi`.
The cutoff pairing can be nonzero when the unweighted boundary-free pairing
vanishes. Local density, a genuine bulk on-shell vertex, forced response energy,
energy exchange and an observed signal must be distinguished.

This wave therefore tests the **same signed-energy connection germs** against
the **held positive matter completion**, while retaining the Ward/boundary
burden. No new generic receiver is substituted for that question.

## 2. The lower-order part of the same germ

Use the exact upper-triangular frame of the preceding result. Its lower
operator is

    C_S=C_old+Delta_S,
    Delta_S=K8 J01+K9 J02+K11 J12.

The generators act on both the form and Clifford endomorphism legs. At u=0,
the actual constraint lift of a range amplitude V and normal Fourier k is

    G_k(V)=V-M^-1(ik P K4 V+P C_S V).                 (1)

Take the already-certified negative principal-energy amplitudes
`V=K3 b3` at root A and `V=K3 b12` at root B. These are highest geometric
SO3 weight7; they are not physical particle-spin labels. Their realifications
are actual local analytic solution germs for every finite k, and their
canonical patch energy is negative for sufficiently large finite k.

Let `B(w)=q(A^t)^-1 Vertex(w) I`, with the unchanged canonical zero-normal
injection I, literal contraction q and complete SE=-1/2 vertex. The owned
normal-only/gamma-traceless lemma gives

    B(V)=B(M^-1 P K4 V)=B(M^-1 P C_old V)=0.

The last identity uses exact SO3 invariance of C_old and M; it is not a
root-center numerical zero. Hence the receiver of this exact initial value is

    B(G_k(V))=-B(M^-1 P Delta_S V),                  (2)

independent of k. The lower term can matter even though the k-leading scalar
response is invisible.

### Reuse complete certified responses

Write `F=J02-iJ12`, `Ka=K5-iK8`, `Kb=K9-iK11`, and `Kb+=K9+iK11`.
For the highest7 input, the exact native ladder identities give

    Delta_S V=-(7/2)Ka V+(1/2)Kb+ F V.

The second summand has weight7 and only spin7, so its receiver vanishes by the
same lemma. Let `a5=Pi5 P Ka V` and `b6=Pi6 P Kb V`. The owned identity
`a6=F b6/6` gives

    B(G_k(V))=(7/2)B(M5^-1 a5)+(7/12)B(F M6^-1 b6).  (3)

All N5/N6 blocks are already complete and certified at both roots. Apply F to
the **output** of the highest6 inverse; do not insert a second lowered-Gram
normalization. Exact full-source reconstruction and direct native receiver
checks authenticate the compression. No new auxiliary inverse is constructed.

## 3. The actual cross-Gram, not a raw nonzero matrix

The held matter completion uses a cross-Gram N(k_m), generally non-Hermitian,
with `||N/Vol(Omega)-I||op<1/2`. Its physical imaginary-connection diagonal
current is `-Herm(N^-1 B)`. A raw nonzero B alone is insufficient.

The old32 receiver-image trace identity is not automatically applicable:
realification of a weight5 matrix contains both weights5 and-5, so its
trace-square need not vanish. For each realification compute an exact center
B0, `b0=||B0||HS`, `h0=||Herm(B0)||HS`, and a certified error epsilon. The
sufficient strict certificate

    2 h0-b0 > 3 epsilon                             (4)

implies `2||Herm B||HS>||B||HS`. If N^-1B were anti-Hermitian, the distance
from B to the anti-Hermitian subspace relative to B would be at most
`||N/Vol-I||op<1/2`, contradicting this inequality. This uses the real
Hilbert-space angle bound, not just `||B-A|| <= c||A||`: if
`B=A+EA`, A is anti-Hermitian and `||E||op=c<1/2`, the ball of radius
`c||A||HS` about A subtends angle at most arcsin(c) at zero. Projection
onto the anti-Hermitian subspace therefore gives
`||Herm B||HS <= c||B||HS`. Equivalently, complete the square in
`||B-A||HS² < c²||A||HS²` after the orthogonal Hermitian/anti-Hermitian
decomposition. The positive scalar Vol is absorbed into A. Thus (4) tests all the
already-admitted cross-Grams without choosing a new normalization.

Inherited infinity-norm inverse errors use output row-sum amplification.
The evenN5 balanced one-norm bound uses its dual weighted maximum instead.
Root-independent sources leave only the owned inverse uncertainty. Exact
rational inequalities, not displayed decimal approximations, govern any
accepted nonzero current.

## 4. Exact straightening of the actual dynamics

The full-carrier equation is

    (K_tau-u K_beta) q_u+K4 q_r+C_S q=0,
    tau=theta3, beta=theta4-3 theta7.

Its covectors obey `tau²=-1`, `beta²=1/8` and `tau.beta=0`. Define

    b=sqrt(8) beta,
    gamma=theta4+beta/2=(3/2)(theta4-theta7).

Then `b²=1`, `gamma²=-3/32`, with pairwise orthogonality. Let J be the
ambient metric-skew generator with `J tau=b`, `J b=tau`, `J gamma=0`,
acting on both tensor legs. This is a computational conjugacy, not an assertion
that J preserves the background or is a physical symmetry.

Set

    u=sqrt(8) tanh v,
    x=r+(1/2)log cosh v,
    q=e^(-vJ) h(v,x).

Direct differentiation, including the x shift, gives

    K_tau h_v+K_zeta(v) h_x+D(v)h=0,
    zeta(v)=sqrt(8)sech(v)gamma-b/2,
    D(v)=sqrt(8)sech(v)e^(vJ) C_S e^(-vJ)-K_tau J.     (5)

The time kernel is now fixed. Its auxiliary block is

    M(v)=sqrt(8)sech(v)P e^(vJ)C_S e^(-vJ)P.

Only M(0)=sqrt(8)M is the old certified block. The background need not stay in
the old59-dimensional invariant family under J; its conjugation cannot be
silently omitted. The spatial norm is
`zeta(v)²=1/4-(3/4)sech²(v)`, negative near zero. This change of variables does
not turn the indefinite problem into a positive spatial comparator.

### Finite coefficient description

On the one-form/Clifford carrier J is semisimple with weights in
`{-2,-1,0,1,2}`. A Clifford blade can contain each of the two nonzero weight
lines at most once; its weight is-1,0 or1, and the form leg adds another such
weight. Therefore

    J(J²-1)(J²-4)=0,
    product_(m=-4..4)(ad J-m)=0.

The conjugated lower operator in(5) is exactly a sum of nine fixed operator
components times e^(mv). This replaces sampling u by a finite coefficient
problem; it does not assert a small invariant dynamical module or constant
M(v).

The complete geometric-spin0 carrier is an exact invariant family: all J01,
J02,J12 annihilate it, so Delta_S vanishes; K3,K4,K7 and C_old preserve it.
The straightening J also commutes with SO3. Its ambient dimension is1924,
with786 auxiliary and1138 range directions. Tiny central subspaces are not
thereby invariant. A full1138-column new lower assembly is not presumed cheap
or necessary before a sharper structural or cyclic-module test.

## 5. Actual microlocal principal matrix

The earlier scalar-jet matrix is not silently promoted to an actual generator.
Elimination and frequency-dependent polarization do not commute. Use the
owned exact factorization `L=F+Ud`, with `d:R->N` the actual first-order
constraint map and F,U first order. On the non-null constant-rank cone,
`d1 u1=0` and `d1 f1(ker d1)=0`. Choose a smooth order-zero microlocal frame
E=(E_K,E_C) with E_K spanning ker d1, and its pseudodifferential inverse B.
Then d E_K, B_C U and B_C F E_K are order zero. The conjugated generator
has block orders [[1,2],[0,1]]. The change `v=E diag(Lambda,1)w`, with
Lambda having positive homogeneous symbol |xi|, gives an actual order-one
pseudodifferential generator for w. |dr|=1 fixes its native normalization.
The first derivatives of E and B must be retained before taking its symbol.

The full constant-rank neighborhood is obtained by subtracting a time-covector
component and using orthogonal covariance fixing the non-null time covector.
Every nearby timelike transverse covector is carried to a nonzero multiple of
theta4, conjugating V=PK_xi R. Stay away from the transverse null stratum.
This proves constant rank on the full finite R, not only spin7; smooth kernel
and complement frames exist. Owned full-M regularity gives smooth F,U,d.

### Coordinate facts and scope

On G_tau/SO3 the functions r=(1/4)log det L and log lambda are genuine group characters, trivial on the SO3 isotropy. In the declared exponential section their differentials are theta4 and beta=theta4-3theta7. The trace of the adapted fourth normal generator is4 and all other adapted generators have zero trace, so r=z4 exactly. The time-line character has generator values1 and -3 on axes4 and7; hence log lambda=z4-3z7 in those exponential coordinates. Replacing the translation exponential coordinate by physical t=x3 is a legitimate local coordinate change; it leaves r a coordinate. The actual frame satisfies dt=lambda theta3. Therefore, in this moving trivialization,

    K^t=lambda K3, K^r=K4,

exactly, not just at p. P,R,M and G=(K3|R)^-1 R have constant moving components. The lower coordinate operator C(x) is not assumed constant; C(p)=C0 is the owned exponential-frame lower operator.

Set a=lambda^-1. The actual spatial factorization has

    d0=M^-1 P C R,   d1=i M^-1 P K_xi R,
    U0=a G C P,      u1=i a G K_xi P,
    F0=-a G C R,     f1=-i a G K_xi R.

At fixed coordinate xi=dr, K_xi=K4 is constant throughout the chart. Choose the principal microlocal frame e=(eK,eC) so e(x,dr) is constant in x. Then partial_x e=0 at that ray. The order-minus-one symbol of its inverse vanishes there. No time-frame term occurs because all these choices are stationary.

### Kernel derivative and sign convention

Let bK,bC be the inverse rows at p and define

    V=P K4 R,
    Y=M^-1 V,
    Z=M^-1 P C0 R,
    X=bC (D_beta eK).

Use the graph chart D_beta eK=eC X. Differentiating V eK=0 gives the exact rectangular equation

    (V eC) X=-P K_beta R eK=3 P K7 R eK.             (X)

The radial K4 contribution is zero. V eC has full column rank, and the right side lies in its image by constant-rank smooth kernel continuation; both statements admit exact residual checks. X is a coefficient-kernel derivative, independent of the background M and root.

Write T_beta=D_beta bC. Inverse differentiation gives T_beta eK=-X. The principal identities ensure G K4P and G K4R eK lie in K. Kohn-Nirenberg composition, with partial mapped to i*xi, gives at lambda=1

    sigma0(dE_K)=Z eK,
    sigma0(B_C U)=bC G C0 P-T_beta G K4P,
    sigma0(B_C F E_K)=-bC G C0R eK+T_beta G K4R eK.

The signs follow from partial_x a=-a dlog lambda: u1=+i a G K4P, f1=-i a G K4R. The factor1/i in symbol composition produces the displayed minus and plus, respectively.

Let L2,L1,L0^0 denote the previously owned NAIVE exponential-frame freeze-first matrices, with NO transverse Delta0:

    L2=G K4 P Y,
    L1=-G K4R+G K4P Z+G C0P Y,
    L0^0=-G C0R+G C0P Z.

Then the genuine weighted principal matrix at p,xi=dr is

    H_mu = [[i L1_KK, -L2_KC],
            [L0^0_CK+X L1_KK, i(L1_CC+X L2_KC)]].    (H)

Equivalently, if H0 is the old NAIVE matrix (not the corrected scalar-jet matrix),

    H_mu = [[I,0],[-i X,I]] H0.

This is left multiplication, not similarity. The old positive trace sign cannot be inferred from it. The nonzero old Delta0_CK remains a correct scalar-jet calculation; it is not part of this microlocal principal because the pseudodifferential polarization corrects the transverse jets.

Both theta4 and theta7 are SO3 scalars. Thus X preserves geometric-spin7, and the existing36 K3/K4/K7 carrier supplies equation(X). All root-dependent inversions in(H) remain the owned N7 restriction of the full-M inverse. No N5/6 derivative assembly is needed for this character shortcut. The actual non-null full-carrier microlocal reduction justifies interpreting the20 highest-spin multiplicity block as a block of its principal symbol; this does not assert a closed20-component differential PDE.

### Reflection and trace

Choose kernel/complement frames compatible with the owned full-base reflection B. K4 and K7 commute with B; G anticommutes with it; C0 and M commute. Equation(X) and injectivity of V eC imply B_C X=X B_K. Therefore the left shear commutes with the split reflection. Since H0 anticommutes with that reflection, H_mu also anticommutes, and tr H_mu=0 exactly. This is subject to the same native parity/basis conventions as the old reflection controls, not a floating trace-zero test.

A strict positive Re tr(H_mu^2) consequently certifies an eigenvalue with positive real part. The dimension20 quantitative bound remains Re tr H_mu^2 <=20*19*(max Re eigenvalue)^2. No diagonalizability is required. Both signs are certified below.


### Certified spectral result

On the 20-dimensional highest-geometric-spin7 multiplicity block:

| Held kappa1 root | Outward interval for Re tr(H_mu²) |
|---|---|
| A | [1.2598031661, 1.2598031679] |
| B | [1.3089274030, 1.3089274076] |

Exact rational centers/error envelopes, not the displayed decimals, govern
these signs. Reflection gives trace zero over the full certified root boxes.
For the 20 eigenvalues counted algebraically, let m be the maximum real part.
Their real parts sum to zero, lie between -19m and m, and have squared sum
at most 20*19*m². Subtracting imaginary-part squares only lowers Re tr(H²).
Both lower bounds exceed19/80, so m>1/40. No diagonalizability is assumed.
This is a normalized principal-symbol bound, not a physical growth rate.

The old nonzero transverse Delta0 is correct for the published scalar-jet
operator. It cancels from the present leading symbol after microlocal
polarization. No published floor is withdrawn or regraded: these are different
operators. The actual spin7 **symbol block** closes; the triangular spin7 PDE
does not. The larger spin0 assembly is unnecessary for this result.

## 6. Actual-coefficient no-loss estimate obstruction

**Theorem (scoped candidate domain).** At either held kappa1 root, on a
non-null conic neighborhood of the timelike normal ray dr, the actual reduced
connection equations admit no uniform local same-Sobolev-order Duhamel bound
on the compact microlocal first-graph test core defined below. This is a
necessary-estimate obstruction, not an exact growing-solution theorem.

Let A be the properly supported order-one microlocal generator above, H* its
full principal symbol at (p,dr), and v an eigenvector with Re lambda>0 from
the certified invariant block. In13 spatial dimensions take

    w_k(t,x)=k^(13/4) chi(k^(1/2)(x-p))
               exp(ik dr.(x-p)) exp(kt H*)v,

with nonzero smooth compact chi. A bounded real estimate complexifies
boundedly, so these complex tests suffice. For each fixed finite Sobolev index
s, divide all norms by k^s. Initial norm tends to ||chi||2||v||, while the
norm at t=S/k tends to exp(S Re lambda)||chi||2||v||. For each FIXED S,
symbol Taylor expansion gives

    k^(-s) integral_0^(S/k) ||(partial_t-A)w_k||H^s dt
         = O_S(k^(-1/2)) -> 0.

Spatial variation k|x-p| and frequency spread both cost O(k^1/2). Order-zero
remainders cost O(1); time variation over S/k, if present, also costs O_S(1).
Proper support and an enclosing cone/chart cutoff leave rapidly decreasing
errors. Thus a putative uniform estimate

    ||w(t)||H^s <= C (||w(0)||H^s
                    + integral_0^t ||(partial_t-A)w||H^s dt),
    0<=t<=T,

would imply exp(S Re lambda)<=C. First let k tend to infinity for each fixed
S (so S/k<T), then vary S. This contradicts Re lambda>0. No differential-system
wellposedness theorem is silently extended to a pseudodifferential system.
For comparison, the classical necessity setting is discussed by
[Matsumoto–Yamahara](https://www.numdam.org/article/JEDP_1989____A8_0.pdf)
and [Metivier](https://arxiv.org/pdf/1310.4760); the packet argument here
supplies the precise local no-loss scope used.

### Exact original constraint graph and forcing norm

Reconstruct range data v_range=E diag(Lambda,1)w and define n=-d v_range
using the actual differential constraint map. Every such field satisfies the
primary constraint exactly. The tested original norm is

    ||(v_range,-d v_range)||_(H^(s-1) direct_sum H^(s-1)).

On this non-null cone it is equivalent, modulo lower-order microlocal terms,
to ||w||H^s: v_range controls the weighted K amplitude, and d1 e_C is
injective on the complement and controls its amplitude. Forcing is measured
in the **same graph norm of the range residual** `(f,-df)`,
`f=(partial_t-L)v_range`. This is not an assertion about an unweighted full
original-PDE forcing norm. The original first-order equation residual has range row K_dt f; it is
distinct from this induced graph-evolution forcing. The leading graph
embedding has top columns [|xi|e_K,0] and bottom columns
[-|xi|sigma0(d E_K),-d1 e_C], which proves the stated injectivity even when
the lower constraint term on K is nonzero. Parametrix/smoothing errors vanish
in the packet limit. Properly supported reconstruction keeps tests in a fixed compact chart.

**Ceiling:** no same-order bounded Duhamel evolution in this stated class.
Finite derivative-loss estimates, analytic restricted evolution, global/L2
state admission, physical cohomology and a different source-selected domain
are not ruled out by this proof. It neither constructs exact exponentially
growing solutions nor proves nonlinear runaway.

## 7. Current result, three-state finding and next discriminator

For the same negative-energy analytic germs in§2, both real components pass
(4), with margins at least169.0079411 at A and581.1579763 at B. Their native
receivers contain3680 and3232 terms respectively; direct original four-arrow
checks agree with the compressed formula. The result holds for every admitted
cross-Gram of the held positive finite-band matter completion. These are
pointwise local current tests. The selected source support has geometric
spin>=5 and cannot be a pure central gradient (central one-forms have spin<=2),
but that does not settle general gauge/Ward cancellation or boundary flux.

- **ESTABLISHED:** same signed-energy solution germs have nonzero selected
  matter current; the actual non-null microlocal principal has positive real
  spectrum at both roots; the specified no-loss estimate fails.
- **RULED OUT:** uniformly bounded same-order evolution on the declared
  unrestricted compact first-graph core; complete pointwise current blindness
  of those two selected germs in the held matter completion.
- **NOT MODELED / UNDETERMINED:** source-required physical admission,
  derivative-loss or restricted analytic dynamics, physical BRST/cohomology,
  a boundary-free Ward-nontrivial vertex, forced negative-mode excitation,
  nonlinear exchange/runaway and GU falsification.

The next useful discriminator is whether a source-supplied physical
admissibility/quotient removes this concrete microlocal channel **and** the
signed-energy current witnesses. An absent prescription is an explicit missing
input, not permission to invent one. Separable candidate work can test the
same-germ Ward/on-shell coupling with its actual boundary functional; nonzero
cutoff density alone cannot settle it. Repeating fullM inversion, frozen
scalar assembly, generic receiver scans or a large spin0 census adds no
required evidence for the result now proved.

Choice budget unchanged:10 choice families,4 obligation bundles, net6,
zero source-selected predictions. No source/physics/canon/class-C/paper verdict
or schedule/governance change. Nov26g remains proposal-only; its qualitative
time-saved order remains1,6,targeted2,3,7,5,4. This wave's mathematical
compression is ordinary authorized science, not adoption of a new VOI gate
or execution of the proposed comparator suites.

## 8. Verification

Six authenticated native records were recomputed in a fresh cache in46.37s:
complete same-germ sources, current/cross-Gram bounds, boost controls, spin0
scope samples, K7/projector derivative, and both intrinsic spectral intervals.
The expensive inherited auxiliary inverses were authenticated, not regenerated.
No full spin0 lower matrix was assembled. The probe and data-only bundle are
repository-native; no scratch modules are needed for reproduction.

Finite Lean core: left shear blocks, reflection preservation, positive real
entry from trace-zero/positive moment, scalar moment bound, and conservative
rate arithmetic. Native geometric identification, spectral trace/eigenvalue
bridge, root boxes, pseudodifferential construction and the packet proof remain
separately reviewed inputs. This is not a full-PDE Lean formalization or external
peer review. Exact artifacts and review receipts are linked in the evidence.
