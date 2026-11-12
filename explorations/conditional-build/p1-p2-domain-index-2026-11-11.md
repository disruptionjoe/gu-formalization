---
title: Boundary phase, observed grading and hidden-index transfer
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P1xdomain_boundary
tier: T2
expected_delta: Derive nontrivial conditional requirements for the remaining P1/P2
  cells
actual_delta: P1/P2 domain_boundary and global_index constrained in explicit analytic
  categories
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Boundary phase, observed grading and hidden-index transfer

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P1xdomain_boundary
tier: T2
expected_delta: Conditional constraints for open matrix cells
actual_delta: P1/P2 domain_boundary and global_index constrained in explicit analytic categories

```gu-typed-objects
result: Boundary phase, observed grading and hidden-index transfer
carrier: finite Green zero-spaces and separately supplied Fredholm complexes/families LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: positive auxiliary Hermitian Green category; no transfer to indefinite GU ends ON=declared_carrier
real_structure: separately stated real or complex category; K77/K95 never silently identified
grading: linear trace grading, antiunitary reality and index grading kept separate
action_owner: N/A -- structural tests, no guessed action or class-C inhabitant
target: actual observation and declared analytic realization MAP-TYPE=restriction
```

## Source and typed scope

SC-CHI-01/51 assert a non-chiral total theory with an effectively chiral observed
world, with their own hedges. SC-GEN-01 disavows three simply repeated families;
SC-GEN-02/03/54 describe 2+1, the labeled imposter pullback summand, and a graded
extension claim. None equates ambient chirality with an observed grading or
supplies a Fredholm observation map. A balanced ambient index is therefore not
an objection to the source-native claim. Observation is section contraction,
not a freely chosen projector. Indefinite K77 and K95 remain separate.

The boundary result concerns a declared positive-Hilbert Dirac-type analytic
subclass with a valid Green identity, trace theorem, and spectral split. This is
not automatically the GU RS operator or its indefinite action pairing. The
index result concerns supplied Fredholm complexes and continuous maps on actual
graph-domain/target spaces; it does not treat pointwise pullback as a bounded
Hilbert-space quotient. No action, coefficient search, or native domain is built.

Prior work reused rather than reclaimed:
- p3-green-form-symmetry-domain-2026-11-11.md proves unitary-graph parametrization
  and antiunitary J constraints, including family bundle obstructions.
- x-p2-p3-phase-domain-index-2026-11-11.md proves integer phase invariance and
  relative finite-codimension domain index changes.
- p3-family-index-mixed-twist-2026-11-11.md shows rank-zero numerical index can
  hide a nonzero family class.
- p3-essential-end-domain-2026-11-11.md prevents importing elliptic Fredholm
  assumptions into the actual B5 full-core category.

New work is the linear-grading/common-phase boundary classification, its
intersection with antiunitary reality, the hidden/observed index exact sequence,
and extension of phase invariance to a whole supplied Fredholm family.

## 1. Linear grading on a Green-Lagrangian zero-space

Let H0 be a finite-dimensional Hermitian space and c*=-c, c²=-I. Suppose a split
selfadjoint spectral boundary prescription is available; its zero-space part L
must satisfy L=L^(omega-perp), omega(u,v)=<cu,v>. Set V+=ker(c-i), V-=ker(c+i).
The already-proved unitary-graph classification gives equal dimensions n and
L=L_U={(x,Ux)}, U:V+ -> V- unitary.

Let Γ=Γ*=Γ^-1 be a separately supplied linear grading. For Γ to grade the same
closed realization it must preserve its actual trace domain, not merely satisfy
a formal interior equation. Assume Γ preserves H0 and the nonzero spectral part.

**Anticommuting normal-flux case.** If Γc=-cΓ then
Γ(x,y)=(A*y,Ax) for a unitary A:V+ -> V-. Thus

    Γ L_U=L_U  iff  U A* U=A.

Proof: Γ(x,Ux)=(A*Ux,Ax) belongs to L_U precisely when U A*Ux=Ax for every x.
Put V=A*U. Since V is unitary, V²=I iff V=V*. Hence ALL invariant domains are

    U=A V=A(2P-I),

where P is an orthogonal projection on V+. Under the graph identification x ->
(x,Ux), the grading Γ restricts to V, so its ± eigenspace dimensions are
rank(P) and n-rank(P). These dimensions are boundary trace data, not index or
physical-family multiplicities. All n+1 possible ranks occur at a point; no
rank is dynamically selected.

**Commuting normal-flux case.** If Γc=cΓ then Γ=diag(G+,G-) with Hermitian
involutions G± on V±. The condition is U G+=G- U. Such U exists iff the + and -
eigenspace dimensions match separately on V+ and V-. For a smooth constant-rank
family, the precise condition is unitary isomorphism of the corresponding
positive/negative eigenbundles, not equal pointwise ranks alone. Necessity is
restriction of U; sufficiency uses the direct sum of two unitary isomorphisms.
Any supplied bundle isomorphism can be made unitary by polar normalization.

Neither case asserts that the ambient Γ is the observed chirality. This is a
necessary-domain test only for a proposed physical realization carrying Γ.

## 2. A fixed domain for a rotated normal phase

In the anticommuting case define

    Tθ=exp(iθΓ/2),   cθ=Tθ c Tθ^-1=exp(iθΓ)c.

Then cθ*=-cθ and cθ²=-I. This is a conjugated normal symbol, not a whole-operator
scalar multiplication. A fixed c-Green-Lagrangian L is Green-Lagrangian for all
θ if and only if ΓL=L. In fact θ=0 and θ=π/2 suffice.

Sufficiency: Γ-invariance implies TθL=L, and conjugation transports both Green
form and maximality. Necessity: at θ=π/2, cθ=iΓc. Isotropy says ΓcL⊂L-perp.
At θ=0 maximality says cL=L-perp. Hence ΓcL⊂cL; dimensions make equality, and
anticommutation with c gives ΓL=L.

This classifies a real burden on a phase-preserving COMMON domain. Transporting
Lθ=TθL always gives a compatible moving domain, but that is not the same claim
as keeping L fixed. Whether P2 is represented by this operation must be proved
on the actual native normal symbol and pairing. Class C covariance alone does
not identify it. Full ellipticity, infinity estimates, and the nonzero spectral
part remain separate from this finite zero-space statement.

**Reality is not automatic.** If an antiunitary J obeys Jc=σ cJ and JΓ=τ ΓJ,
with signs σ,τ, then

    Jcθ = σ c_(-τ θ) J.

Thus τ=-1 preserves the same σ relation along the phase circle, whereas τ=+1
generally transports θ to -θ. A fixed real/quaternionic category can restrict
the allowable phases. This does not discard the reality condition to gain a
phase path, and does not assert arbitrary complex phases belong to real C.

## 3. Hidden and observed index balance

Let D:E -> F be a bounded Fredholm map, where E is the actual domain with its
graph norm. Let qE:E -> Eo and qF:F -> Fo be continuous surjections onto Banach
spaces, with closed kernels Kh and Lh. Suppose a bounded observed operator
Do:Eo -> Fo satisfies qF D=Do qE. This entails D(Kh)⊂Lh and defines Dh:Kh -> Lh.
Assume all three maps D,Dh,Do are Fredholm (this may be weakened using extra
split hypotheses, but is not needed here). The exact sequence of complexes
induces

 0 -> ker Dh -> ker D -> ker Do --δ--> coker Dh
   -> coker D -> coker Do -> 0.

Explicit connecting map: for observed zero mode v, lift e with qE(e)=v. Then
D e∈Lh; let δv=[D e] modulo Dh(Kh). A different lift differs by an element of
Kh and gives the same class. All other maps are induced inclusions/quotients.
Exactness is direct: δv=0 precisely when its lift can be corrected by a hidden
vector to a total zero mode. Finite-dimensional alternating dimensions give

    ind D = ind Dh + ind Do.

Consequences:
- If total index is zero, an observed index N requires hidden index -N.
  This is compatible with a nonchiral total, not an exclusion of it.
- If hidden cohomology is acyclic (Dh invertible), the observed and total
  indices agree. Removing only an acyclic hidden complex cannot create a
  nonzero observed index from a balanced total.
- The connecting map may be nonzero: observed zero modes need not lift to
  total zero modes. Counting images of kernels alone is insufficient.
- No map on the pointwise field bundle or numerical rank proves this exact
  sequence on a closed operator domain. Verify trace regularity, surjectivity,
  kernel invariance, and the analytic domains. If q is not onto, use its actual
  image with justified topology and redo the argument rather than silently
  claiming a quotient.

This is the conditional requirement for P1xglobal_index in the subclass that
realizes effective chirality through such a graded Fredholm observable. It is
not a premise that every acceptable GU chirality must be an ordinary index.

## 4. Whole-family phase cannot create an index bundle

Let Db:Eb -> Fb be a continuous Fredholm family over a compact base B, with a
continuous graph-domain bundle and fixed source/target grading. Let Vb:Fb -> Fb
be a continuous boundedly invertible bundle automorphism. Then the Fredholm
family D'b=Vb Db has exactly the same family index in K^0(B).

Proof with no constant-kernel assumption: choose a finite-dimensional auxiliary
bundle Z and continuous j:Z -> F so (D,j):E⊕Z -> F is onto. The kernel bundle
K is finite-dimensional, and Ind D=[K]-[Z]. Use j'=Vj for D'; the augmented map
is V(D,j), so its kernel is literally K. The same representative gives the
same index. The finite stabilization exists in the standard compact-base
Fredholm-family framework; equivalently its availability may be included in
the analytic contract. This statement is about the supplied family, not a
construction of a GU family or end.

In particular a global nonzero scalar function z:B -> C* preserves the whole
index bundle even if its phase has nonzero winding. No globally chosen logarithm
or homotopy from z to1 is required. This rules out the mistaken inference that
phase winding alone changes a family index. A phase acting on only one coupled
principal block, changing the closed domain or end component, reversing the
grading, or existing only in local charts of a nontrivial line bundle is outside
the theorem and needs its actual gluing map. Pointwise index equality alone
would have been weaker; today's mixed-family result explains why.

P2xglobal_index can therefore be constrained by requiring the actual full
family operation: pure invertible codomain phase has zero family-index effect;
any claimed index consequence needs a nontrivial symbol/domain/end/grading or
gluing change. It neither fixes the initial index nor decides P2/P3 for C.

## 5. Exact controls, distinct from universal proofs

A. Boundary n=1: c=diag(i,-i), Γ=[[0,1],[1,0]], A=1. L1=span(1,1) obeys Γ and is
isotropic for every cθ. Li=span(1,i) is isotropic at θ0 but has nonzero Green
self-pairing -2i at θ=π/2 (using <cu,v> conjugate-linear in first slot).
U=±1 are exactly the Γ-invariant scalar graphs; U=i is a contrary control.

B. Commuting Γ: n=2, G+=diag(1,-1), G-=diag(1,-1) permits U=I. If G-=I then no
unitary intertwiner exists, despite balanced flux dimensions. Exact unknown
2x2 linear intertwiner equations have rank restriction excluding invertibility.

C. Reality: J=complex conjugation with c=diag(i,-i), Γ=σ1 gives σ=-1,τ=+1;
verify J c_(π/2) differs from -c_(π/2) J. An abstract relation control with
τ=-1 verifies unchanged σ. This is not a K77/K95 assignment.

D. Hidden compensation: D=0:C² -> C². Let qE project to a one-dimensional
observed space and qF map onto the zero space. Then Do:C ->0 has index+1,
Dh:C ->C² has index-1, total0. All finite maps are Fredholm. This is an exact
complex-level control, not an action or chirality witness.

E. Nonzero connecting map: D=I:C -> C, hidden Kh=0,Lh=C, observed Eo=C,Fo=0.
Then ker total0, ker observedC, coker hiddenC, and δ=I. The naive claim that
every observed zero mode lifts to a total zero mode fails.

F. Acyclic hidden: total D=diag(1,0):C² -> C², qE=qF=second coordinate;
Dh=1,Do=0:C->C. All indices0 and connecting map0. Alter qF independently to
break commutativity as a negative test; index-transfer theorem is then inapplicable.

G. Family: use D=diag(1,0), V(θ)=diag(exp(iθ),1), same kernels and coker for all
θ. An augmented j into the second coordinate has identical kernel before and
after rotation. Symbolic Laurent z with z!=0 suffices; no finite sampling is
claimed to prove the family theorem. Complex winding adds no numeric or K index.

## Matrix requirements

P1xdomain_boundary: constrained -- a proposed graded spectral realization must
preserve the actual trace domain. In the stated positive-Hilbert zero-space
category the full linear-grading classification above gives exact unitary graph
conditions, separate from formal bulk grading and antiunitary reality.

P1xglobal_index: constrained -- for a surjective compatible Fredholm observation
complex, total=hidden+observed index; zero total allows nonzero observed only
with compensating hidden index, and acyclic hidden removal preserves index.
No requirement that the native chirality claim itself be an ordinary index.

P2xdomain_boundary: constrained -- for a proposed phase realized by conjugation
cθ=exp(iθΓ)c, a common maximal Green zero-space exists for all phases precisely
when its trace subspace preserves Γ; transported domains and real structures
are different requirements. Native phase-operation identification remains open.

P2xglobal_index: constrained -- global invertible full-family codomain phase
preserves family index, including phase winding; a phase-to-index claim must
specify the nontrivial operator/domain/end/grading/gluing operation beyond it.

These are independently reviewed conditional structural constraints, not four complete
physics decisions. Their precise structural subfamilies remain explicit in the matrix.

## Independent source-fidelity correction from orientation specialist

Observed one-sided weak-current coupling does NOT require a nonzero Fredholm
index. Exact finite countercontrol: O+=O-=C, D=0 has index0, while an admitted
weak-current coefficient W=diag(1,0) on O+⊕O- is one-sided. This supplies neither
a gauge theory nor a GU witness, but disproves the abstract implication
"observed weak chirality => nonzero index". Therefore the P1 global-index
entry is a conditional transfer requirement ONLY where the proposed mechanism
uses a graded Fredholm count. It must not make index nonzero a new P1 condition.
Similarly, a reality pairing can force index balance only if it preserves the
actual hidden/observed complex and relevant domains. Do not import it from the
balanced ambient fibre alone.

## Trace-domain and family-stabilization precision


1. A boundary grading is an actual domain test only with a trace intertwiner:
let τ:Dom_max -> T be the continuous surjective graph trace, let Γ preserve
Dom_max, and suppose τΓ=γτ. For D_W=τ^-1(W), invariance ΓD_W=D_W is equivalent
to γW=W. Surjectivity onto T gives the necessary direction; the intertwining
identity gives the sufficient direction. The finite classification applies to
the zero-space component only after this bridge and invariance of the nonzero
spectral component have been supplied. No statement is made that an observed
weak grading extends as a Green-orthogonal grading of every ambient field.

2. Family-index stabilization can be justified directly in the declared compact
base Hilbert/Fredholm category: near each b choose finitely many target vectors
spanning the cokernel complement, extend continuously in a trivialization, then
use a finite subcover and partition-of-unity cutoffs. Their union gives j from a
finite trivial Z so (D,j) is onto at every b. Local continuous right inverses
make its finite-dimensional kernels a vector bundle. Applying V changes j to
Vj and leaves that kernel bundle exactly unchanged. This avoids assuming kernel
ranks of D itself are constant.

## Evidence, acceptance and residual

Universal proofs above are separate from finite exact supporting/contrary controls in
[the probe](../../tests/program-focus/matrix_remaining_constraints_probe.py) and
[the report](../../lab/process/matrix-remaining-constraints.json). Independent internal
specialist review checks mathematics and source scope; this is not external review
or a Lean-certified class decision. RA-F1, AC-F1 and LT-SM8 remain NEEDS under physics
ledger0.263. Source register, class C, all canon and physical prediction grades are
unchanged. A constrained matrix entry records a useful necessary condition within
its explicit structural category; it does not establish that C inhabits that
category or settle all possible realizations.
