---
title: "Global normal U(3,2) existence reduces to an almost-complex structure on the four-dimensional base"
status: exploration
doc_type: structural-result
created: "2026-11-24"
program_target: P2xglobal_index
tier: T2
expected_delta: "Replace an undifferentiated global-normal-complex-structure gap by an exact topological criterion on the admitted metric bundle; distinguish existence from selected reduction and relative/end data."
actual_delta: "For oriented spin Lorentz four-bases, an orthogonal complex structure on the trace-reversed normal bundle exists on the observation section iff TX admits an almost-complex structure. A base structure extends over the full metric bundle; an admitted metric section proves the converse. It exists automatically on noncompact bases without prescribed boundary/end reduction. Closed bases retain the exact integral lift/square criterion."
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

program_target: P2xglobal_index
tier: T2
expected_delta: Replace an undifferentiated global-normal-complex-structure gap by an exact topological criterion on the admitted metric bundle; distinguish existence from selected reduction and relative/end data.
actual_delta: For oriented spin Lorentz four-bases, an orthogonal complex structure on the trace-reversed normal bundle exists on the observation section iff TX admits an almost-complex structure. A base structure extends over the full metric bundle; an admitted metric section proves the converse. It exists automatically on noncompact bases without prescribed boundary/end reduction. Closed bases retain the exact integral lift/square criterion.


> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `SOURCE_NATIVE_ROUTE`.

# Global normal complex reduction

```gu-typed-objects
result: Global existence criterion for the normal pseudo-Hermitian reduction
carrier: N=Sym²(pi*TX)* over Lorentz metric bundle Y or its observed pullback; oriented spin four-base LAYER=ambient+observed BRIDGE=literal-section-pullback CHIRALITY=N/A
pairing: native trace-reversed Frobenius lambda=1/2 of signature6,4; auxiliary positive metric only for topology ON=declared_carrier
real_structure: real normal vector bundle with sought orthogonal complex structure; no K77/K95 Clifford transfer
grading: positive6 and negative4 topological splitting; no physical fermion grading
action_owner: N/A -- absolute reduction existence, no action or vacuum selection
target: U(3,2) reduction and its topological premises MAP-TYPE=not-a-map
```

Base revision: `d7bd31e050fd92a127c2e5fd55ce49f07fb3858c`.

## Result and limits

Let X be a paracompact smooth oriented spin four-manifold, let
Y=Met_(3,1)(X), and let V=pi*TX. On N=Sym²V* use the native trace-reversed
Frobenius form

    K_g(h,k)=tr(g^-1 h g^-1 k) - (1/2)tr(g^-1 h)tr(g^-1 k),

of signature (6,4). An orthogonal complex structure J_N is equivalent to a
U(3,2) reduction. For orientation-specific statements below, fix orientations
of the maximal positive and negative bundles and require the reduction in
that component-compatible SO0(6,4) frame bundle; the negative orientation
is identified with the stated base orientation through (1). If these
orientations are not fixed, the rank-four criterion instead permits either
sign of 2e. For the admitted Lorentz bases e=0 (and H4=0 in the open cases),
so this distinction does not change the existence conclusions. It does
matter when transporting a chosen component to another construction.
This concerns the rank-ten normal/vertical bundle, not an
almost-complex structure on the fourteen-dimensional total space.

**Theorem.**

1. For any Lorentz metric section g of Y, the bundle (g*N,K) admits J_N iff
   TX admits an almost-complex structure (of the matching chosen orientation).
2. If TX admits an almost-complex structure, (N,K) admits J_N over all Y,
   and likewise over the time-oriented metric cover Y^up. Conversely, existence
   over Y or Y^up implies existence on X whenever the corresponding metric
   section is admitted. For the cover this includes its time orientation.
3. If X is connected, noncompact and spin, existence is automatic in this
   absolute topological problem. A compact X with nonempty boundary has the
   same absolute conclusion. No prescribed reduction at a boundary or end is
   included.
4. If X is closed, existence on X is equivalent to an integral class c with
   rho_2(c)=w2(TX) and c²=p1(TX)+2e(TX). A Lorentz metric implies chi(X)=0,
   hence the numerical criterion is c²[X]=3 signature(X). In the spin case
   c=2a; the remaining criterion is 4 a²[X]=3 signature(X), not a requirement
   that c or the signature be zero. We do not assume this square equation is
   automatically soluble on every closed spin Lorentz four-manifold.

The theorem supplies existence/obstruction conditions, not a canonical J_N,
source action, selected vacuum, parallel/integrable J_N, SU(3,2) determinant
trivialization, global Standard Model gauge quotient or a physical weak-current
projector. It does not change a source claim or physics-ledger verdict.

## Source and already-owned results

- SC-GRP-03 asserts the intersection of maximal-compact and U(3,2) reductions
  on the same normal bundle. The reduction problem is therefore native, rather
  than an imported SU(5) or conventional Higgs model.
- SC-META-54 is an authorial denial with semantically uncertain global-section
  wording. Nothing here turns that exchange into a universal requirement for a
  globally trivial bundle. The global-section converse is explicitly conditional
  on the metric section already declared in action class C; the forward
  existence statement over Y does not require that section.
- `canon/w2-y14-spin-structure.md` and the K77 global chimeric-spin result already
  own the Spin lift. A Spin lift and U(3,2) reduction are different problems.
- `sca-right-chain-2026-08-15.md` already reconstructs the normal reduction chain
  and leaves its global complex/determinant data unbuilt.
- TW3-C already proves associated-bundle descent **given** a component-tagged
  lifted U(3,2) reduction. The result here addresses existence of the underlying
  orthogonal complex reduction; it does not supply TW3's selected component,
  selected endomorphism, action or analytic domain.
- Physics rows RA-A2, RA-A6 and RA-A8 remain NEEDS: their action selection,
  global embedding/quotient and stationary-vacuum requirements survive.

## 1. Positive and negative bundles of the native form

Fix an auxiliary positive metric on V. The tautological Lorentz metric selects
its negative eigenspace L (a real line) and positive eigenspace E (rank three).
This is a maximal-compact reduction; its space of choices is contractible.
We have V=L⊕E, and orientation of V gives w1(E)=w1(L)=l. On a time-oriented
cover L is trivial, but the proof does not assume that on Y.

Write g=diag(-1,1,1,1) locally. A symmetric variation has temporal entry a,
mixed three-vector b and spatial symmetric matrix C, with s=tr C and
C=C_0+(s/3)I. Direct substitution gives

    K(h,h)=tr(C_0²)-2|b|²+(1/2)a²+a s-(1/6)s².

The scalar (a,s) matrix has determinant -1/3. Its negative line is the trace
direction g, norm -4; its positive line is diag(3,1,1,1), norm 12, orthogonal
to g. These scalar lines are globally trivial: their definitions depend on L,
not on a choice of sign for a unit vector in L. Consequently

    N+ ≅ 1 ⊕ Sym²_0 E*,       rank 6,
    N− ≅ 1 ⊕ (L*⊗E*) ≅ L*⊗V*, rank 4.                 (1)

The final isomorphism uses the metric trivialization L*⊗L*≅1. With a
time-oriented metric section this simplifies to N−≅TX; without a time
orientation it is L_g⊗TX. Tensoring by a real line preserves and reflects
existence of a complex structure: use 1_L⊗J, and tensor by L again for the
inverse. Thus N− has a complex structure iff V does.

A K-orthogonal J_N exists iff both N+ and N− admit complex structures. One
direction forms J+⊕J−, after making each compatible with its positive metric
(K and -K). For the other, average a positive auxiliary metric under J_N;
the positive/negative spectral subbundles of K relative to that metric are
J_N-invariant. They are isomorphic to the maximal positive/negative bundles
in (1). Therefore allowing J_N to mix a previously chosen split cannot evade
the negative rank-four obstruction.

## 2. Positive rank-six obstruction

For a real rank-three bundle E, splitting-principle calculation gives

    w1(Sym² E)=0,
    w2(Sym² E)=w1(E)²+w2(E).

Removing its scalar line does not change these classes. Since
w2(V)=w2(E)+l w1(E)=w2(E)+l², equation (1) implies

    w2(N+)=w2(V),  w2(N−)=w2(V),
    W3(N+)=pi*W3(TX)=0                                          (2)

in the admitted spin scope. Notice that the sum N has w2(N)=0 even when
neither summand has zero w2. Total Spin existence alone would not normally
be enough to establish a pseudo-Hermitian reduction; the summands matter.

For an oriented rank-six bundle, SO(6)/U(3)=CP³. Its only nonzero homotopy
group in degrees 1 through 6 is pi_2=Z. Thus over a CW complex of dimension
at most seven the only obstruction is W3. This is the rank-six case of
Albanese–Milivojević §3, which also identifies the next possible obstruction
in degree eight. No degree-eight obstruction occurs on a four-dimensional
observation section.

The full metric fibre is not contractible. Relative to an auxiliary positive
metric, deform the three positive eigenvalues of g to +1 and its negative
eigenvalue to -1, keeping L fixed. This deforms Y onto P(TX), the RP³ bundle
of unoriented lines. The time-oriented cover deforms onto S(TX), an S³
bundle. Both have a CW model of dimension at most seven. Equation (2)
therefore also discharges the positive-bundle existence obstruction on full
Y and its cover. The proof never replaces the metric fibre by a point.

## 3. The negative rank-four problem and the base criterion

By (1), N− admits an almost-complex structure iff pi*TX does. An
almost-complex structure on TX pulls back and tensors with L to give the
required one on N−. Together with §2 this proves full-Y sufficiency. A metric
section pulls a full-Y reduction back to X; tensoring by its timelike line
then supplies an almost-complex structure on TX. This proves necessity when
the section is admitted.

On a four-dimensional CW base, an oriented rank-four bundle first has the
W3 obstruction; after that, a choice of integral lift c of w2 has a final
obstruction o4 in H⁴(X;Z), satisfying

    4 o4 = p1 - c² + 2 e.                                    (3)

For a closed oriented connected four-manifold H⁴(X;Z)=Z, so vanishing of the
right-hand side is equivalent to vanishing of o4. This is the Wu criterion.
It must not be used as a sufficient criterion on an arbitrary CW complex
with four-torsion in H⁴. The integral class c and its reduction include any
H² torsion; checking a numerical square on free cohomology does not by itself
check rho_2(c)=w2.

For a connected noncompact oriented four-manifold, H⁴(X;Z)=0; the same is
true for a compact connected oriented four-manifold with nonempty boundary.
Here W3=0 in the spin scope and the last absolute obstruction vanishes.
This proves the positive existence statement without a closed-spacetime
compactification. If a particular J is fixed at infinity or on a boundary,
obstructions instead belong to relative groups and this conclusion does not
settle extension of that specified J.

For a closed Lorentz base, chi=0. The signature theorem gives
p1[X]=3 signature(X), so (3) becomes c²[X]=3 signature(X). Spin implies that
c=2a for an integral a, by the exact coefficient sequence. The signature is
a multiple of sixteen, but that divisibility is only a necessary arithmetic
compatibility check; it is not a supplied solution a of the square equation.

## 4. Controls and nonclaims

- Flat R⁴ and T⁴ have trivial tangent bundles and supply positive controls:
  constant complex structures on the 6+4 splitting give J_N. Over the full
  metric bundle their existence follows from §§2–3, without a canonical
  Lorentz-natural selection.
- On K3 # 12(S¹×S³), chi=0 and signature=-16. Its K3 intersection lattice
  contains a hyperbolic pair e,f with e²=f²=0 and e·f=1. Take
  a=e-6f and c=2a: a²=-12 and c²=-48=3 signature. This is a compact spin
  Lorentz positive control with nonzero signature, so neither signature zero
  nor c1=0 is a necessary condition for U(3,2) existence. This is a topological
  example, **not** a construction of a K3-fibered family or source action.
- Outside the admitted spin scope, 2 CP² # 2(S¹×S³) has chi=0 and signature=2.
  On its free diagonal intersection form an integral lift of w2 has both
  coordinates odd; its square is 2 mod 8, whereas 3 signature=6 mod 8.
  Thus it has no almost-complex structure and no normal U(3,2) reduction on a
  metric section. This is a control showing that Lorentz signature and
  pointwise (6,4) alone are insufficient. It is not a GU-spin counterexample.
- No Lorentz-equivariant pointwise J can be built from g alone on all of
  Sym²T*X: its unique invariant trace line would have to be preserved by J,
  while a real line cannot satisfy J²=-1. This is a selection/covariance
  distinction, not an obstruction to a covariantly transforming additional
  reduction field. Existence does not select the reduction used by dynamics.
- The auxiliary positive metric used in the proof is a topological device;
  it does not authenticate compact symmetry of the native operator (T13).
- No projection is substituted for observation contraction (T04), no family
  count is read from a Chern class (T14), and no change to K77/K95 occurs.

## Matrix consequence

At P2xglobal_index (secondary X-P1-P2), the global normal-complex requirement
can be typed by (1)–(3). In the absolute noncompact spin subclass its mere
existence is no longer an unexplained topological obstruction. On closed
backgrounds the exact missing input is the integral lift c with the stated
square, or an equivalent almost-complex structure on TX. On specified
boundary/end reductions the exact missing input is their relative extension
class. Selection, matching the actual weak projector and operator covariance
remain separate. No class-C decision, ledger change, physical prediction,
SC-GRP-03 proof or packet unblocking follows solely from this result.

## Primary reference and reproducibility

Michael Albanese and Aleksandar Milivojević, *Obstructions to almost complex
structures following Massey*, §3.1–3.3, especially the rank-six CP³ case and
rank-four final obstruction:
https://arxiv.org/html/2406.05518v2 . Its ordinary oriented-bundle obstruction
theory is applied separately to the positive and negative bundles after (1);
no unproved direct transfer to an indefinite bundle is made.

The companion exact probe checks the native rational form, signatures and
splitting, mod-two characteristic polynomial identities, and the arithmetic
controls. It does not certify the topological obstruction theorem, which is
proved by the argument and primary theorem above.

Reproduce with `python tests/program-focus/global_normal_complex_reduction_probe.py --selftest`; evidence in `lab/process/global-normal-complex-reduction.json`. Independent T2 review accepted the result after the component/orientation clarification above. The exact probe passes115 controls and detects3 planted false assertions; see the [review](../../lab/process/hostile-reviews/2026-11-24-structural-compatibility-review.md).
