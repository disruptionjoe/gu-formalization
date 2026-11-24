---
title: 'Odd mixing after source gauge transport: a relative grading detector'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3; P1 fields/symmetry
tier: T2
expected_delta: Resolve ordinary simultaneous gauge removal of the newly identified odd relative-current
  directions; identify exact remaining constraint and physical-response burdens
actual_delta: A transported relative grading detector detects all odd relative-distortion tangents at
  zero distortion, including the full-support SM-neutral real one-form witness. The source printed NE
  block has an exact left-tilted derivative defect under a candidate pointwise field law, identifying
  a separate fermionic descent burden. No physical mode, rate or GU exclusion is inferred.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
class_covered: Source two-connection configurations with a metric-spin reference preserving an ambient
  involution, full independent fermion fields, ordinary simultaneous bundle gauge transformations and
  coherently transported observation; separately the displayed wrapped NE arrow under left tilted multiplication
  at fixed reference. K95 supplies explicit real-parent examples; no K77 reality transfer.
premises:
- "SC-GRP-02/05 and SC-GEO-55 source full-parent and gauge-rotated-reference grammar; source-prescription-current-2026-11-13.md\
  \ \xA7\xA71\u20133."
- SC-CHI-01/04/51/52 effective split; ambient grading remains a typed candidate rather than the physical
  luminous projector.
- source-small-vev-current-test-2026-11-24.md supplies odd-current parity and the actual observation graph;
  physical fluctuation support and response remain open.
source_bridge:
  status: conditional
  reason: Source gauge and primitive field grammar are authenticated. This tests a candidate relative
    grading and primitive current on their gauge quotient; physical constraints, solution space and observed
    response are unselected.
kill_condition: A source contradiction requires source-required physical modes and dynamics retaining
  nondecoupling. A nonzero covariant detector only excludes removal by ordinary simultaneous gauge transport;
  a source-owned constraint or response can still suppress it.
---

program_target: X-P1-P2-P3; P1 fields/symmetry
tier: T2
expected_delta: Resolve ordinary simultaneous gauge removal of the newly identified odd relative-current directions; identify exact remaining constraint and physical-response burdens
actual_delta: A transported relative grading detector detects all odd relative-distortion tangents at zero distortion, including the full-support SM-neutral real one-form witness. The source printed NE block has an exact left-tilted derivative defect under a candidate pointwise field law, identifying a separate fermionic descent burden. No physical mode, rate or GU exclusion is inferred.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: relative grading detector and source cross-current transformation
carrier: full complex Dirac scalar and one-form spinors with independent bars LAYER=ambient+observed BRIDGE=actual-contraction CHIRALITY=S-FULL-DIRAC
pairing: nondegenerate independent density dual; K95 sharp only for explicit real example ON=declared_carrier
real_structure: K77/K95 separately typed; added quaternionic restriction not source-full-U requirement
grading: transported ambient involution; physical weak grade unselected
action_owner: source-printed candidate derivative arrow and primitive two-connection grammar; no complete action constructed
target: source gauge-relative current MAP-TYPE=intertwiner
```



# Result

**The new odd mixing direction is not removed by a simultaneous gauge change of the source's two connections and grading.** There is a covariant tensor that detects it even when the connection is flat. At zero relative distortion its linearization annihilates genuine gauge tangents and the already-known tilted kernel, but detects every nonzero odd relative-distortion tangent. The actual horizontal observation retains the two previously identified whole one-form witnesses, including the new real witness `c_H(X) omega_H`.

This is a constraint on a proposed *gauge-only* explanation for decoupling. It is not a proof that these directions propagate or produce an observed interaction. A field equation, physical constraint, small normalized fluctuation, response kernel, or coupling may suppress them. The source has not selected the complete physical map that decides this.

Evidence base: `6ef984a3f04b40c98724d7442e6bd2f119a56a21`. Internally reviewed conditional structural result; no physical quotient is asserted.

## 1. Source and prior-result custody

The source data are

    A = A0[g] + varpi,
    B = A0[g]^epsilon,
    T = A − B.

SC-GRP-02/05 ASSERTS the full U(64,64) parent and inhomogeneous gauge grammar; SC-GEO-55 ASSERTS the relative displacement from gauge-rotated Levi-Civita. SC-CHI-01/04/51/52 requires effective low-VEV/curvature separation, not an exact universal off-shell split. The source's four independent barred/unbarred scalar and one-form fields are retained. No connection component is retyped as a scalar field.

The evidence contract's `standing_ledger.source_gauge_bv_image_directive`, the August13 source-gauge/BV-image result, and November13 `source-prescription-current` already prove the primitive variation/tilted-kernel distinction. In particular, arbitrary varpi translation is not automatically gauge; the selected K77 196-cell adjoint/Euler calculation is already owned. We do not repeat its ranks or claim a new theorem that all source translations are physical modes.

The November24 small-VEV result already proves nonzero odd primitive current and its fixed-port bound. The new contribution here is the *relative grading detector on the coherently moved gauge tuple* and its application to those current directions, with a flat-connection contrary control and an explicit inventory of possible physical restrictions.

## 2. Objects and exact gauge convention

Let S be the full complex Dirac bundle and let `Omega0²=I` be the chosen ambient spinor involution. Assume explicitly

    D_A0 Omega0 = 0.                                          (G1)

This holds for the metric-spin reference and its Clifford volume. It is not assumed for an arbitrary full-unitary connection or an independently prescribed physical chirality projector. Put

    Omega = epsilon^-1 Omega0 epsilon,
    P_± = (I ± Omega)/2.

The source conjugated-tensor prescription gives

    D_B Omega = epsilon^-1(D_A0 Omega0)epsilon = 0.            (G2)

All identities below work over the complex carrier for any such involution. Real-parent membership of the explicit mixing witnesses is supplied in K95, separately from source K77. The indefinite pairing is not replaced by a positive physical norm.

Use the standard right connection convention

    A^h = h^-1 A h + h^-1 d h.

The genuine **simultaneous two-connection bundle gauge transformation** at fixed reference A0 is

    A → A^h,       epsilon → epsilon h,
    B → B^h,       T → h^-1 T h,
    Omega → h^-1 Omega h.                                  (G3)

In primitive coordinates this changes varpi to `h^-1 varpi h + h^-1 D_A0 h`. It is right multiplication by the tilted element `(h,h^-1 D_A0 h)` in the documented convention `(e1,w1)(e2,w2)=(e1e2,Ad_(e2^-1)w1+w2)`.

In unwrapped spinor coordinates `psi → h^-1 psi`, independent density rows transform as `barpsi → barpsi h`. In source wrapped coordinates `chi=epsilon psi` and `barchi=barpsi epsilon^-1`, the corresponding components stay fixed. Clifford multiplication, contraction, grade and actual observation must move with this same frame law. This is covariance of the supplied field tuple, not a choice of physical observables.

## 3. Relative grading detector and proof

Define the End(S)-valued one-form

    K := D_A Omega.

By (G2), and with `T_o=(T−Omega T Omega)/2`,

    K = [T,Omega] = 2 T_o Omega,
    T_o = (1/2) K Omega.                                    (G4)

Consequently `K=0` exactly when the relative connection is Omega-even. The maps in (G4) are inverse on the odd subspace, without positivity or an inner-product choice. Covariant differentiation of `Omega²=I` also gives `{K,Omega}=0`.

Under (G3),

    K → h^-1 K h.                                          (G5)

For proof, apply connection covariance to `D_A Omega`; equivalently conjugate both entries in `[T,Omega]`. The derivative of h in the connection cancels the derivative from `h^-1 Omega h`. Freezing Omega after changing only A drops exactly this cancellation.

**Finite consequence.** No invertible simultaneous gauge transformation turns a nonzero K into zero. For any fixed covector evaluation, its rank is invariant. This rules out diagonalizing T and then silently retaining the original grade as a gauge-removal argument. It does not provide a gauge-invariant positive size or physical amplitude: U(64,64) can change an auxiliary Euclidean operator norm arbitrarily.

**Meaning of the constraint.** Imposing `D_A Omega=0` is a genuine reduction to grading-preserving relative connections under (G1), not an ordinary gauge choice: every orbit either satisfies it everywhere on that orbit or nowhere. The source's declaration of a small or vanishing background VEV does not impose this restriction on all fluctuations.

### Complete linearization at zero relative distortion

The owned primitive formula, with `eta=epsilon^-1 delta epsilon` and `beta=delta A0`, is

    delta T = alpha + (I−Ad_(epsilon^-1))beta − D_B eta.     (G6)

At `T=0`, variation of (G4) gives

    delta K = [delta T,Omega].                              (G7)

The term `[T,delta Omega]` vanishes at this background; it has not been omitted at finite T. Thus any tilted kernel `delta T=0` is annihilated. Every nonzero odd component of delta T is detected. At `epsilon=I`, the two beta contributions cancel, so this remains true under a simultaneous variation of the source metric-spin reference, with its grade transported.

For a genuine infinitesimal gauge change with parameter lambda,

    delta A=D_A lambda, delta B=D_B lambda,
    delta T=[T,lambda], delta Omega=[Omega,lambda],
    delta K=[K,lambda].                                  (G8)

At T=0 this has zero delta K. By contrast, the primitive variation `alpha=D_B lambda` **with epsilon held** has `delta T=D_B lambda`, and generally nonzero delta K. The same connection-coordinate expression therefore represents two different full field variations. This is the new detector's application of the old source tangent distinction.

At a point the projection of the quotient by the tilted kernel onto relative distortion is the already-owned surjection (G6). Equation (G7) identifies its odd image with K by the invertible map `v_o → 2v_o Omega`. It is a statement about field jets and an associated tensor; it is not BRST cohomology, an on-shell phase-space count or a number of particles.

### Double-coset ceiling

SC-GEO-54 ASSERTS a two-sided tilted/double-coset construction. We do not equate every left/right coordinate operation in that construction with the simultaneous frame action (G3). In the displayed semidirect convention, left tilted multiplication can keep T fixed while changing epsilon and therefore the relative grade unless reference tensors also move. At finite nonzero T, K is not claimed invariant under that operation with other data frozen. Whether the complete source action/current and observation identify such configurations requires the complete transformation law.

At T=0 the tilted `delta T=0` kernel is still annihilated by (G7) regardless of grade motion. This is the robust linear conclusion used here. No full physical double-coset/BV reduction is constructed or silently identified with the elementary gauge quotient.

## 4. New odd current, actual observation and the real witness

On a section with horizontal subbundle H, write the source scalar input as nu and its primitive NE output as `e alpha nu`, with the source nonzero cross coefficient e. Because B preserves Omega, the off-diagonal connection transport is exactly

    P_- D_A(P_+ nu) = P_- T P_+ nu.                        (G9)

The derivative of the projected section is included in (G9); this is not a frozen projector shortcut. The other direction has the analogous formula. Thus K detects the same odd relative coefficient that supplied the November24 current. In the complete `(zeta,nu)` grade `G=diag(Omega,−Omega)`, the odd-parent NE variation is field-grade even and its independent barred bilinear has opposite-sector support, as already proved. Spinor Omega and the full form/scalar grading are not conflated.

The existing complex witness is `alpha_i(X)=i lambda c_H(X)` with lambda real, and zero normal component. For a nonnull horizontal X,

    K_i(X)=2i lambda c_H(X)Omega.

The parallel reality analysis supplies a stronger witness needing no normal complex structure:

    alpha_R(X)=lambda c_H(X)omega_H,                      (G10)

where omega_H is the **real** oriented horizontal Clifford volume in signature(3,1), `omega_H²=−I`, and `omega_H` anticommutes with every horizontal vector. In the stated K95 convention `c_H(X)^sharp=c_H(X)` and `omega_H^sharp=omega_H`, so `(c_H(X)omega_H)^sharp=−c_H(X)omega_H`. It is real with respect to the specified Clifford-commuting antilinear structure, Omega-odd, proper-Lorentz covariant and normal-Spin neutral. These representation facts do not say the source restricts its full U parent to a reality-preserving subgroup.

The detector gives

    K_R(X)=2 lambda c_H(X)omega_H Omega.                   (G11)

This is invertible for lambda≠0 and nonnull X. The observation calculation uses its actual one-form graph, not a scalar substitution. Let `J_H nu=(X↦c_H(X)nu)` and `Gamma_H J_H=4I`. In receiver coordinates `(b,tau,nu)` the NE response is

    e lambda (J_H omega_H nu, 4 omega_H nu, 0),

and in `(b,sigma=tau−Gamma_H b,nu)` it is

    e lambda (J_H omega_H nu, 0, 0).                      (G12)

Because omega_H is invertible and Gamma_H J_H=4I, this graph has full complex rank128 on the actual full spinor carrier, with rank64 from either ambient half. These are ranks of a primitive local vertex, not physical state counts. Under gauge transport, `c_H`, `omega_H`, nu and q all transform, and (G12) transforms by the invertible receiver frame. The nonzero graph cannot disappear through that coherent transport.

A sigma-only or scalar-output-only receiver row can still annihilate this horizontal graph; the earlier fixed-port result already supplies these controls. Actual physical input restrictions or a physical output map are not assumed to be full. The conclusion is therefore a nonzero *algebraic observed graph after gauge transport*, not a detected experimental response.

## 5. A flat-connection contrary control

On a local one-dimensional coordinate x inside a larger patch, let B=0, epsilon=I, Omega constant, and Q a constant admissible odd matrix. Take

    A_t=t Q dx,       T_t=t Q dx.

It is flat: `dA_t+A_t∧A_t=0`. Nevertheless `K_t=t[Q,Omega]dx` is nonzero for t≠0 and Q≠0. The pair `(A_t,B=0)` is not obtained from `(A=0,B=0)` by a simultaneous gauge change, since such a change sends both equal connections to the same connection. A gauge trivialization of A_t alone necessarily transforms B and Omega if it is a genuine frame change, preserving nonzero K.

For the true-gauge control start instead with A=B=0 and transform by `h=exp(t x Q)`. Then A'=B'=tQdx, epsilon'=h, Omega'=h^-1 Omega h, and K'=0 exactly. The nonzero A coefficient cancels the derivative of the moving grade. Thus a test which reports mixing for this pure gauge control has frozen part of the source tuple incorrectly.

This defeats “flat connection” or “locally exact alpha” as sufficient explanations for erasing the *relative* mixing tensor. It does not assert that the flat example solves the source equations, is normalizable or propagates.

## 6. Printed NE operator under left tilted multiplication

This tests a different part of the two-sided construction from ordinary simultaneous bundle gauge. Fix the source metric-spin reference `A0` and its differential operator `D0=d_A0`. In the source semidirect convention, left multiplication by `tau(h)=(h,h^-1 D0 h)` gives

    E' = h E,
    A' = A + E^-1(h^-1 D0 h)E,
    B' = B + E^-1(h^-1 D0 h)E,
    T' = T.                                               (L1)

Here `D0 h=dh+[A0,h]`; it is an endomorphism-valued one-form. Equation(L1) is the already-owned left-tilted grammar, not a new result. The new test applies it to the actual source NE arrow and its displayed wrappers. Define

    Dhat = E d_A E^-1 = D0 + U,       U = E T E^-1.

The equality follows from `E d_B E^-1=D0`, including the derivative of E. Then

    Dhat' = D0 + h U h^-1,
    Dhat' − h Dhat h^-1 = (D0 h)h^-1.                  (L2)

This is an identity of operators from scalar spinors to spinor one-forms. A bare coefficient conjugation of a connection misses its second term. It has no Shiab contraction or adjoint ambiguity in this NE block.

Write chi for the wrapped scalar input in this NE calculation and barchi for its independent barred one-form density row, rather than for the entire form/scalar multiplet. There are two precise conditional consequences:

1. **Wrapped fermions held fixed.** With the same independent barred row and unbarred scalar, exact NE bilinear invariance for all their inputs holds iff `h U_mu h^-1=U_mu` in every covector component. At `T=0` it holds for every h: `Dhat'=D0`. If it is demanded for *every* full-U(64,64) h at a point, each `U_mu` must lie in the complex scalar commutant of its defining representation (and in `i R I` if it is Krein-skew). Nonzero odd U therefore fails this particular universal fixed-field law. This does not say the source chooses that law.
2. **Candidate pointwise spinor covariance.** If instead `chi'=h chi` and `barchi'=barchi h^-1`, then

       (Dhat' h − h Dhat)chi = (D0 h)chi,                 (L3)

   and the NE bilinear defect is `barchi h^-1(D0 h)chi`. On the full independent input/density pairing, it vanishes for every input iff `D0 h=0`. The other source quadrants cannot cancel this isolated off-shell coefficient: set the unbarred one-form and barred scalar to zero and retain the barred one-form/scalar pair. This polarization does not apply after an unbuilt physical constraint relates those fields. In particular, at `T=0` the fixed-field control above passes while a generic local h still fails this candidate transported-field law.

The infinitesimal coefficient check is `delta Dhat=[lambda,U]=[lambda,Dhat]+D0 lambda`. This agrees with the already-owned differential wrapper commutator in `source-prescription-current` §7; the finite left action plus the isolated NE compatibility alternatives are the additional consequence.

### Finite curvature control: no pointwise spinor intertwiner in this category

There is a counterexample to *every* invertible pointwise scalar-spinor intertwiner for this isolated NE operator, not just the candidate law `chi'=h chi`. Its category is precise: fixed reference connection and fixed geometric form leg, the full independent scalar/one-form pairing, no mixing with the other source slots, and no derivative-valued field transformation. Take a local two-coordinate patch `(x,y)` with `A0=0`, `E=I`, and

    U = Q dx,
    Q = i [[0,1],[1,0]],       N = [[0,i],[0,0]],
    h(y) = I+yN,              K_pair = [[0,1],[1,0]].

Both Q and N are `K_pair`-skew, `N²=0`, and h(y) is `K_pair`-unitary for real y. This neutral two-dimensional block embeds in the full U(64,64) parent (or tensors with `I_64`); it is an algebraic full-parent control, not a new real-form identification or a source solution. The initial wrapped NE connection `Dhat=d+Q dx` has zero curvature. By (L2), the left-tilted connection is

    Dhat' = d + h Q h^-1 dx,
    F_Dhat' = h[N,Q]h^-1 dy∧dx,
    [N,Q] = −diag(1,−1) ≠ 0.                            (L4)

If an invertible pointwise spinor map M intertwined the isolated operators, `Dhat' M=M Dhat`, extending that connection relation to forms would imply `F_Dhat' M=M F_Dhat=0`, contradicting (L4). Thus no such M exists on a neighborhood. Allowing separate invertible pointwise input and density-row maps does not evade this within the stated category: equality of the identity NE principal symbol for every covector forces the row map to be `I_form⊗M^-1`, hence the same intertwining equation. If x,y are horizontal, the source's full horizontal b readout retains these two form components. A smaller physical readout or a field law mixing source slots is not covered.

The displayed flat-reference pair is an algebraic control, not a claim that the native reference connection is flat. The same local obstruction applies to any fixed compatible reference if arbitrary off-shell full-parent relative connections are admitted: in a local compatible trivialization choose the wrapped total connection d+Q dx, so That=Q dx−A0; at a point take a reference-normal frame, h=I and dh=N dy. The transformed curvature there is [N,Q]dy∧dx while the original total connection is flat. This extension uses the full primitive connection freedom, not a source solution or a selected admissible physical fluctuation.

This rules out universal left-tilted descent of the displayed NE connection by same-slot pointwise spinor frames at fixed reference. It does not rule out an authenticated full two-sided source transformation that moves reference data, mixes slots, changes the candidate operator or acts beyond this category. The source has not supplied that transformation by the assertions cited here; it must not be inferred from the isolated counterexample.

**Custody and ceiling.** SC-OP-04 ASSERTS the displayed operator only at candidate strength; SC-OP-05 keeps unselected operator rivals. SC-GEO-54's double-coset claim does not by itself authenticate either fermion transformation above. The PW2D result already owns the bosonic transported-Shiab left/right grammar and structural Ward calculation; it does not establish this fermionic left-tilted descent. The source's wrappers are a covariance ansatz, with global descent unproved by the primary extraction. Thus (L2) identifies an exact compatibility burden, not a source contradiction. Moving A0, using a different source-authenticated field/reference law, or changing the candidate operator remains a distinct possibility. No such change is silently supplied here.

The next finite source test is therefore to authenticate the fermion/density/reference law required by the actual two-sided quotient and test its NE intertwining equation (L2) on the actual observation. Repeating the generic statement that a left tilt fixes T, or importing the bosonic Ward identity as a fermionic descent proof, does not address this coefficient.

## 7. Actual constraint inventory and remaining physical alternatives

| Candidate removal mechanism | Established source/repository status | Consequence for the new detector |
|---|---|---|
| Ordinary simultaneous bundle gauge | Explicit connection and epsilon laws | Transports K; no removal of a nonzero K |
| Tilted kernel in primitive first jets | Already owned by the evidence contract | delta T=0 ⇒ delta K=0 at T=0; it does not identify nonzero odd delta T with zero |
| Full IG translation module | Source field/Euler variation, not a supplied redundancy | Cannot quotient its entire odd part by calling it gauge |
| Source epsilon Euler row / Noether identity | November13 chain contains reference, moving Shiab and independent-fermion wrapper terms | An equation/identity is not an independently selected physical tangent restriction. Its full linearized solution map on these modes is not supplied |
| Source finite epsilon moment map and BFV models | K941–K945 own finite reductions; source-selected value and functional domain remain missing | Cannot import their zero-dimensional or84-dimensional quotient into the present current |
| K132 principal null directions or G3 ordinary BRST | Owned selected-germ results; proper full physical quotient not derived | Principal nullity or ordinary adjoint BRST is not a spinor-mode/odd-current removal map |
| Exact grading-parallel field constraint | Mathematical subfamily `D_A Omega=0` is well typed | Removes odd relative connection by (G4); source selection of this subfamily is not established |
| Physical constraints, heavy modes, response projection or small normalization | Remain possible and explicitly retained | Require an action/domain/observable-owned map; no primitive rank proves their absence |

The necessary new datum can be written without inventing an action. If Z is the space of allowed linearized solutions at the stated background, R is its true gauge image, and `pi:Z→Z/R` is well defined, a physical mixing test requires the induced response on that quotient. Equation(G7) is gauge compatible on ordinary/tilted kernel directions at zero T; it does **not** determine Z, its positivity, its closed domain, or the inclusion/readout/propagator. A constraint-selected Z may lie in its kernel. Conversely, merely naming gauge covariance does not prove that containment.

## 8. Scope and validation

No action is constructed, no source-grade identification is promoted, no mode is shown to propagate, and no SC/physics ledger verdict or class C is changed. The precise advance is that a gauge-only removal claim now has a covariant, complete-tuple countertest, including a real, SM-neutral full-support one-form. The remaining alternatives must act on the physical tangent/response, rather than repeat a frame change.

`source_gauge_mixing_quotient_probe.py` is an exact small-matrix control for connection/grade derivative covariance, true-gauge versus primitive variations, a flat relative connection, the horizontal real Clifford witness/observation graph, and the left-tilted NE derivative. The written identities supply the all-rank statement; the small Clifford control does not replace the actual14D representation proof or verify a physical quotient. All114 exact controls pass, including the appended left-tilted derivative and curvature cases. Six planted gauge/readout/derivative/curvature mistakes are rejected. Independent mathematical/source review accepted the identities and their scope.

### Reused evidence

- `lab/methods/research-evidence-contract-v1.0.json#standing_ledger.source_gauge_bv_image_directive`
- `lab/sources/source-claim-register.yaml`: SC-GRP-02/05, SC-GEO-54/55, SC-CHI-01/04/51/52
- `source-prescription-current-2026-11-13.md`, `source-small-vev-current-test-2026-11-24.md`, `source-weak-action-transport-2026-11-13.md`
- `selected-k77-i2b-source-gauge-bv-image-2026-08-13.md`
- `selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md`
- `pw2d-actual-y14-transported-shiab-right-tilted-ward-2026-08-02.md`, `g1-derivative-cocycle-moving-reference-2026-07-31.md`
- `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`: source candidate, wrappers and independent fields
- `lab/process/k945-source-epsilon-gauge-ownership-boundary.json`, `lab/process/k1206-current-gauge-bfv-custody-ceiling.json`
