---
title: Every smooth complex-linear local same-q complement fails for the native weighted reconstruction
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-2PLUS1
tier: T1
expected_delta: Classify all same-q nonorthogonal local complements and test their full moving lower graph
  equation.
actual_delta: The completed principal family has no nonorthogonal complement except at one weight product
  per sign dictionary. Every exceptional graph factors through one spinor receiver; retaining its derivatives
  forces the opposite block to have rank at most256, contradicted by the native rank512.
class_covered: Owned completed wedge/SE family, constant nonzero real chiral weights, fixed q and LC-normal
  jets, complete compatible unitary b=H connection family, same smooth complex-linear zeroth-order right inverse on raw
  domain and codomain; actual native metric-bundle shape in the stated complex K95 and explicitly metric-flipped
  K77 ports.
premises:
- explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md
- explorations/conditional-build/bet-2plus1-unitary-dual-closure-2026-11-27.md
- explorations/conditional-build/local-dual-closure-second-fundamental-form-2026-11-24.md
- explorations/conditional-build/k2200-observed-principal-pairing-freedom-2026-10-28.md
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-CHI-04
source_bridge:
  status: conditional
  reason: Source candidate grammar and effective low-gravity separation do not require an exactly invariant
    smooth local complement of this q. Physical bars, current, state and domain remain unselected.
kill_condition: Generic principal Hom zero or the exceptional rank bound excludes the named local realization;
  failure of the sign dictionary, complete character classification, parallel-receiver or native rank
  transfer cancels the affected conclusion.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Lane C only; no result absorption without lane-B re-derivation.
---

# Nonorthogonal local complements do not remove the native shape coupling

```yaml
program_target: BET-2PLUS1
tier: T1
expected_delta: Classify all same-q nonorthogonal local complements and test their full moving lower graph
  equation.
actual_delta: The completed principal family has no nonorthogonal complement except at one weight product
  per sign dictionary. Every exceptional graph factors through one spinor receiver; retaining its derivatives
  forces the opposite block to have rank at most256, contradicted by the native rank512.
```

**Result.** In the declared reconstruction, allowing a completely general smooth
pointwise, complex-linear nonorthogonal right inverse of the fixed observation does not create
an invariant local summand. The generic principal symbol already fixes the
complement uniquely. Its exceptional alternatives all fail a lower-order rank
condition on the actual native shape. This excludes one explicit realization
class, not effective observed physics or source GU.

Basis: `c2d1ea0e4aec45971484df9bfe33795df06322c1`.

```gu-typed-objects
result: complete local same-q complement classification and moving-graph obstruction
carrier: full complex Dirac S128; one-form plus scalar; H4/N10; observed6S and hidden9S normal gamma kernel LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: existing compatible nondegenerate metric-spin pairing and positive scalar density; candidate graph itself need not be orthogonal ON=declared_reconstruction
real_structure: complex proof; actual K77 and K95 arrow signs separate; metric-flip transfers complex rank only
grading: ambient chirality weights, no physical weak/family/index grading
action_owner: repository-construction -- existing wedge/SE weighted tangential reconstruction; no new action or physical quotient
target: same local right inverse intertwining the raw operator and its fixed quotient MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read
> [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> Classification: `INTERNAL_STRUCTURAL_ONLY`. The source total theory is
> nonchiral and its family claim is2+1. Neither exact local splitting nor a
> block dimension is a source-selected physical chirality or family count.

## Source custody, reuse and the tested question

SC-OP-04 ([draft p46, equation9.16](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf))
supplies four independent classical fields and candidate-strength operator
grammar. SC-OP-05 leaves southeast rivals unselected. SC-CHI-04 (draft p64)
and SC-CHI-52 (TOE2025 02:37:07) assert effective decoupling in a low-gravity or
low-mass regime. They do not assert the exact raw-operator splitting tested
here. That necessity is the weakest unproved source bridge. Class-C width
and physical representativeness remain unproved.

The complete one-way b=H unitary family, its opposite block, and native rank512
are owned. Global density jets and quotient-annihilator duality are also owned.
K2200 classifies the earlier raw southeast-zero symbol, so its scalar answer
cannot be applied to the completed southeast family. We reuse its complete
Clifford-character method and compute the changed rows, including both arrow
signs. No native512-minor computation, density search, action or weight fit is
repeated. A nonorthogonal complement is the unconsumed category.

The target is a smooth complex-linear zeroth-order right inverse r of fixed q such that
`D r = r D_O`, where `qD=D_Oq`, using the **same** r on domain and codomain.
The old orthogonal r0 is a reference for coordinates, not a restriction on r.
Independent domain/codomain maps and normalized-time evolution are different
conditions and remain outside this theorem.

### A. Authenticate both signs before normalizing

Use the actual common wedge grammar

```
D_x(z,nu)=(A_w(x) W z + x nu, sigma i_x z + c_x E nu),
W=w_+P_+ + w_-P_-,  Wsharp=w_-P_+ + w_+P_-,
p=w_+w_- !=0,  E Wsharp=c I.
```

Here `sigma` is the literal southwest coefficient sign, not the signature. Actual owned inputs are:

| Port | sigma | c | Evidence |
|---|---:|---:|---|
| K77 completed family | -1 | +11/12 | Nov25 report §§1–2; `selected-k77-wedge-shiab-southeast-completion-2026-08-11.md` displayed reciprocal equations; `tests/program-focus/chiral_weight_transport_probe.py` raw block lines98–106 has southwest `-eta[k] I`. |
| Old K95 B2C4 family | +1 | -11/12 | `tests/channel-swings/eric_curt_wave3d_b2c4_shiab_family_southeast_completion_probe.py`: `codiff` lines155–156 is `+(eta*k)`, symbol block lines263–273 uses that `codiff`, and reciprocal equations are at lines27–28 and278–279. |

The K95 and K77 sign dictionaries are not interchangeable. This algebraic proof accommodates both; any lower-term/native-rank conclusion additionally needs its own correctly transported geometry/connection binding.

The full lower family is transported with the southwest sign, not just the
principal matrix. With codifferential convention `symbol(delta)=-i_x`, the
southwest row is `-sigma delta`, and density replacement gives
`-sigma delta_f=-sigma delta+sigma i_b`. Its hidden-input scalar leakage is
`sigma [S(z)-z(H)+z(b)]`; hence its zero equation is always
`S(z)=z(H-b)`. The b=H survivor and complete F/U zero set are unchanged.
The scalar density addition is +z(b) in K95 and -z(b) in K77. Southeast E
has no hidden input. The opposite hidden-normal output B uses NW/NE only,
so neither this scalar-row transport nor SE changes B. This is the explicit
K95 binding of the one-way lower family, not a relabeling of the Nov25
minus-southwest display.


The raw covector convention is the owned one: `gamma_a^2=eta_a`, `Gamma z=sum gamma_a z_a`, `J_a=eta_a gamma_a`, `i_x z=sum eta_a x_a z_a`. For coordinate covector `e^k`, the wedge nonzero entries are `eta_a gamma_a gamma_k gamma_b W` for pairwise distinct a,k,b. Define the invertible change

```
z_a=eta_a gamma_a u_a,  nu=Wsharp h,
Gamma_k=gamma_k Wsharp.
```

For distinct a,k,b the normalized entry is
`gamma_a (eta_a gamma_a gamma_k gamma_b W)(eta_b gamma_b)=gamma_k Wsharp=Gamma_k`.
The NE entry is `Gamma_k`. The SW entry is `(sigma/p) Gamma_k`, using `W^-1=Wsharp/p`. The SE entry is `(c/p) Gamma_k`, using `E Wsharp=cI`. Thus, without a square root or a positivity assumption on p,

```
R^-1 D_k R=M_k tensor Gamma_k,
(M_k)_(a,b)=1    if a,b,k are distinct one-form indices,
(M_k)_(k,h)=1,  (M_k)_(h,k)=sigma/p,  (M_k)_(h,h)=c/p,
all other entries zero.
```

This is simultaneous conjugation of the **unnormalized** principal coefficients. No left multiplication by an inverse time coefficient occurs.

### B. Exact quotient/complement coordinates

Let O be the four horizontal indices and N the ten normal indices. In u-coordinates,
`K={u_O=0, sum_N u_r=0, h=0}` is the9-copy normal sum-zero space. Every M_k, k in O, acts as `-I` on K. The old orthogonal complement is the6-copy space C with coordinates `(u_0,u_1,u_2,u_3,x,h)`, where every normal coordinate equals x. Both are preserved by each principal coefficient.

On C, for each horizontal k:

```
(M_k u)_k=h,
(M_k u)_i=sum_(j in O\{i,k}) u_j +10x     (i in O, i!=k),
(M_k u)_N=sum_(j in O\{k})u_j +9x,
(M_k u)_h=(sigma/p)u_k+(c/p)h.
```

Any q-right inverse is uniquely `r=r0+T` with T:O_bundle -> K. Under the existing r0 identification O_bundle≅C tensor S, its principal intertwining condition is exactly
`(-Gamma_k) T=T(M_k|C tensor Gamma_k)` for all four horizontal k. T ranges over all complex-linear bundle maps, allowing arbitrary spinor, chirality and form-slot mixing with no equivariance or adjoint condition. Maps compatible with a particular real structure form a subfamily; the complex Hom dimension does not count arbitrary real-linear maps. The no-complement result extends to the latter by the averaging corollary below.

### C. All Clifford characters, without a same-chirality ansatz

The fourteen Gamma_i satisfy `{Gamma_i,Gamma_j}=2p eta_ij I`. Their ordered blades form a basis of End_C(S): even-length products are nonzero scalar multiples of the original even Clifford blades; odd-length products are the corresponding odd blades times the invertible Wsharp. Hence all16384 endomorphisms are retained.

Conjugation by each of the four horizontal Gamma_k is an involution, and these four involutions commute. Thus End_C(S) is the direct sum of sixteen character spaces
`Z Gamma_k=epsilon_k Gamma_k Z`, epsilon_k in {+1,-1}. Each has dimension1024: the four independent blade-parity equations cut the16384 blades into equal classes. This includes chirality-mixing maps. No choice of a positive square root of p or similarity between different real forms is needed.

Choose any basis of the9-copy K factor. For each output copy and each spinor character, a possible graph component has a scalar row `l=(a_0,a_1,a_2,a_3,b,d)` on C and a spinor endomorphism Z in that character. The complete intertwining equations reduce to

```
l M_k=-epsilon_k l,  for all four k.
```

This covers every graph map by direct-sum decomposition, not only factorized trial maps.

### D. Solve all scalar row systems exactly

Column k and column h give, respectively,

```
a_k=-epsilon_k sigma d/p,
[epsilon_k(p-sigma)+c]d=0.
```

If d=0, all a_k=0 and the normal column gives `(9+epsilon_k)b=0`; hence b=0. Thus any nonzero row has d≠0. Since c=±11/12 is nonzero, the four epsilons must have the same sign s: a mixed pair would force both p=sigma and c=0.

For uniform s, put a=a_k. A different horizontal column and the normal column give

```
b=-(s+2)a,
30a+(9+s)b=0.
```

For s=-1 these force `22a=0`, impossible for a nonzero row. For s=+1 they are compatible and require

```
p=sigma-c,
l is a scalar multiple of (1,1,1,1,-3,-sigma p).
```

Therefore the complete complex Hom space is zero off `p=sigma-c`. At that locus it consists exactly of nine arbitrary centralizer endomorphisms times the one row above; its complex dimension is `9*1024=9216`. In particular:

```
K77: p=-23/12;
actual old K95 dictionary: p=+23/12.
```

The all-plus centralizer includes chirality-mixing elements; the proof has not silently assumed they vanish. The complex zero result excludes any real/compatible subfamily as well. For a real-form-specific dimension claim at the exception, intersect with that port's real structure; do not relabel the complex dimension as a physical or real degree count. The identity centralizer element already shows the complex exceptional space is genuinely nonzero.

### E. Intrinsic factorization of every exceptional graph map

In the original observed variables `(b,tau,nu)`, `u_H=gamma_H b`, `x=(tau-Gamma_H b)/10`, and `h=(Wsharp)^-1nu`. The exceptional row becomes the globally meaningful bundle map

```
ell(b,tau,nu)=(13/10) Gamma_H b -(3/10)tau -sigma W nu.
```

Every exceptional principal graph T factors as `T=S ell` for a smooth bundle map S:S_spinor -> K with the centralizer restrictions supplied above. The row ell is surjective because W is invertible. Consequently S can be recovered from T by a fixed smooth right inverse of ell; this factorization is valid for smooth moving T, not only constant matrices.

Choose the existing coherent split metric-spin connection ∇⁰ along the section. It preserves the horizontal/normal bundles, Clifford contraction/insertion, r0,q and the held constant chiral weights. Thus `∇⁰ell=0`. This does **not** assert that ell is parallel for an arbitrary varied unitary connection. Instead, express the actual held tangential operator relative to ∇⁰, putting every actual connection displacement, fixed LC-normal-jet contribution and retained exterior/torsion term into its zero-order coefficient C. This is a change of description of the same operator; no normal-jet prescription is changed or discarded.

### F. The native rank can eliminate the exceptional graph too

The b=H survivor gives the actual triangular operator in K⊕O coordinates

```
D = [[D_K, B], [0, D_O]],
D_K=sum A_K^a ∇⁰_a + C_K,
D_O=sum A_O^a ∇⁰_a + C_O.
```

An invariant graph r=r0+T requires `D_K T+B=T D_O`. After the principal equations cancel, and with T=S ell and ∇⁰ell=0, it follows pointwise that

```
B = S ell C_O - [C_K S + sum A_K^a(∇⁰_a S)] ell.
```

Both summands factor through the128-dimensional complex spinor bundle. Hence

```
rank_C B <= 2*128 =256.
```

The inherited native block has rank512 for the authenticated actual metric-bundle shape and full128-spinor port: Nov27 unitary-dual report §4, importing the Nov24 opposite-block report §5 and its nonzero512-square minor mod97. Every allowed F/U correction leaves that whole B unchanged, and Wsharp is invertible. Thus that authenticated native rank contradicts the necessary exceptional-graph bound, regardless of C_K,C_O or derivatives of S.

Away from the exception, T=0 identically, so its derivatives vanish and cannot repair B at all. The old nonzero-II theorem then excludes an invariant complement on any section with II≠0 in the same class. **At the exception the stronger exclusion is only established where rank B>256 is authenticated**; do not replace this premise by arbitrary nonzero II. An arbitrary shape could have smaller rank.

### G. Explicit complex metric-flip transfer of the native shape rank

The existing native rank probe is specifically K95: `tests/program-focus/local_dual_closure_second_fundamental_form_probe.py`, lines35–36 gives normal Gram `diag(2,2,2,2,6,12,-2,-2,-2,-4)` and lines56–61 gives horizontal metric `(-,+,+,+)`. Its rank is therefore not historically a native K77 rank certificate. The selected K77 principal probe, `tests/channel-swings/selected_k77_wedge_shiab_southeast_completion_probe.py`, lines91–92 has signs `+^7,-^7` and its observed axes are0,7,8,9 (line151), with southwest minus at line147. It constructs the flat operator, not an explicit metric-bundle shape bridge.

We now define and bind the metric-flipped geometric port; this is a new transfer proof, not an inherited K77 rank computation. Let `g'=-g` on H, retain the same symmetric normal matrices v, and use the same trace-reversed DeWitt form. Since each occurrence of g inverse changes sign twice in the normal pairing, its Gram is unchanged. The owned shape formula gives

```
S'_v=-(1/2)(g')^-1 v=-S_v.
```

Choose Clifford generators `c'_H=i c_H`, `c'_N=c_N`. They have horizontal signature(+,-,-,-) and the unchanged(6,4) normal signature, hence total(7,7). The normal gamma trace/insertion/projector are unchanged. In

```
A_II(b)(v)=sum_mu eta_mu c(e_mu) b(S_v e_mu)
```

both eta_mu and S_v change sign, while c(e_mu) acquires i. Thus `A'_II=i A_II`, and exactly `P'_K A'_II=i P_K A_II`. The inherited rank512 is unchanged. Scaling all four horizontal generators multiplies their total volume product by `i^4=1`; with the same ordered basis the ambient chirality operator and W are unchanged. If one subsequently reorders axes to the flat K77 probe's convention, transport the orientation/chirality labels as well; a possible exchange of w_+,w_- leaves p and the whole already-owned family unchanged.

No explicit large conjugating matrix is necessary for the representation-independence statement: the complex Clifford algebra in14 nondegenerate dimensions is Mat128(C), so any two faithful irreducible ordered-generator realizations of this same metric are isomorphic, and the polynomially constructed shape map has the same rank under that simultaneous transport. This transfers a complex rank statement, not a preferred real structure, Hermitian isometry, source choice of signature, physical field map or particle count.


### H. Real-linear nonexistence corollary on the same underlying bundles

Although the Hom classification above is complex-linear, its nonexistence
conclusion also excludes smooth real-linear right inverses on the underlying
real bundles of these same complex carriers. Let J_E,J_O denote multiplication
by i. The held q,D,D_O are complex-linear, including their lower-order terms.
If a real-linear r satisfied qr=I and Dr=rD_O, its complex-linear part

```
r_C=(r-J_E r J_O)/2
```

would satisfy `r_C J_O=J_E r_C`, `q r_C=I` and `D r_C=r_C D_O`.
These follow from J²=-I and commutation of q,D,D_O with J. Smoothness and
zeroth order are preserved. This contradicts the already-proved complex-linear
nonexistence. No real-linear Hom dimension is asserted. This does not cover
a different real carrier, an antilinear operator, a changed observation or
a new physical quotient/domain.

## Effective elimination is a distinct surviving mechanism

The conclusion does not say that every reduced description needs a two-way
invariant pointwise split. For an admitted invertible hidden block D_K, the
same triangular quadratic equations give

    h=-D_K^-1 B o,      bar_h=0,
    S_reduced=bar_o D_O o.

The observed block of an inverse is D_O^-1 when both inverses and compatible
domains exist. This is standard block elimination. The lifting operator is
generally differential/nonlocal and need not be the same algebraic map on
input and output. It is outside the excluded category, with no contradiction.

If D_K has closed range and a cokernel, lifting a particular observed solution
requires `[Bo]=0` in coker(D_K). Kernel bars can feed the observed adjoint
equation. A finite Grassmann Gaussian with unsaturated hidden zero modes has
zero partition function; its normalized cancellation is undefined. Neither a
global inverse nor a physical quantum measure is supplied here. In particular,
the principal expression `c(xi)W` is invertible away from the null cone, but
that fact alone decides no global gap or boundary-domain question. A resonant
hidden solution can grow polynomially in time while the observed solution
stays constant; failure of a same-frequency algebraic lift is not failure of
all local solutions. These are scope controls, not new GU predictions.

## Three-state result, verification and continuation

- **ESTABLISHED:** all principal graph maps, their two sign-correct exceptional
  loci, the moving-graph rank bound, and complex metric-flip transfer of the
  already-certified native512 rank.
- **RULED OUT:** smooth complex-linear zeroth-order same-q invariant complements of the raw
  operator throughout the declared completed/weighted/unitary native shape
  class. Orthogonality is not assumed. At an arbitrary different shape the
  exceptional argument requires rankB>256, not merely II nonzero.
- **NOT MODELED / UNDETERMINED:** independently chosen input/output maps,
  normalized-time invariant graphs, differential/nonlocal reductions,
  source-selected barred readout, physical state/domain and effective
  low-energy chirality or realized family count.

The probe reconstructs the normalized blocks from Clifford products, solves
all16 finite row systems and checks exceptional and contrary controls. These
finite controls support the universal written proof; they do not replace it.
Lean checks only finite rank/algebra implications, not the native Clifford
geometry or a physical field interpretation. The native rank certificate is
hash-pinned and reused, with its old carrier and the new transfer specified.
Two independent specialists and a separate hostile review are required before
internal acceptance. Execution receipts give the actual results.

This is **lane-C evidence only**. No matrix or physics-ledger conclusion is
imported without a separate lane-B re-derivation. No source/canon verdict,
new action, choice family or family-count claim is made. Choice budget stays
10 families /4 grouped obligations /net6 /0 source-selected predictions.
No world novelty is claimed for the standard module and rank methods.

The consumed successor is another pointwise same-q shear in this completed
family. Remaining mechanisms must keep their changed map/domain/effective
meaning explicit; a generic off-diagonal rank cannot exclude all of them.
