---
title: Both printed variational identities force a fixed linear Shiab to vanish
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Classify the entire fixed-linear full-U curvature operator under the printed cubic and
  quadratic variational prescriptions.
actual_delta: The cubic/unit-endpoint identity kills every traceless curvature input. Adding the quadratic/unit-linear
  identity kills the remaining central-input map, so S=0 throughout the declared architecture.
class_covered: Dimension14 nondegenerate metric, full complex128 Dirac and full real u(H) with Spin-compatible
  nondegenerate Hermitian form; fixed pointwise real-linear Spin-equivariant S from adjoint two-forms
  to adjoint thirteen-forms, ordinary matrix curvature, trace/top-form pairing, all primitive translation
  variations. Both own1/3cubic and own1/2quadratic terms have their separately asserted unit endpoints.
  Smooth fixed coefficients and nonvanishing density are allowed.
premises:
- explorations/conditional-build/source-action-riemann-silence-2026-11-27.md
- explorations/conditional-build/riemann-realform-transfer-2026-11-27.md
- explorations/conditional-build/source-prescription-current-2026-11-13.md
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-02
source_bridge:
  status: conditional
  reason: The source supplies the printed coefficients/unit endpoint, full fixed-epsilon translation,
    displayed invariant-Phi symmetry and matrix trace pairing; owned audits fix bracket normalization.
    Attribution of existing nonzero witnesses to the exact Phi basis/product choices is still separate,
    as are broader formulas and merely on-shell equivalence.
kill_condition: Any nonzero S satisfying every declared architecture premise contradicts the theorem.
  A failure of coefficient signs, full carrier/variation, quasicentroid classification, Spin parity or
  quadratic identity invalidates that application; do not call it a source-wide kill.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-NONZERO-FIXED-LINEAR-SHIAB-MATCHED-FIRST-ACTION
internal_target_verdict: Excluded under both universal variational identities; cubic alone retains central-input
  maps.
canon_verdict_change: none
matrix_or_ledger_effect: Evidence attached to existing architecture assumption only; no scientific cell
  or ledger verdict.
---

# Both printed variational identities force a fixed linear Shiab to vanish

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Decide the whole operator class rather than another Riemann response or concrete reconstruction.
actual_delta: Cubic consistency removes all traceless inputs; quadratic consistency removes the central survivor, forcing S=0.
```

## Result first

**No nonzero fixed linear Spin-equivariant Shiab in the declared full-U architecture can simultaneously give both of the printed first-action variations.** This strengthens the earlier direct-Riemann obstruction in two steps:

1. The one-third cubic with its own unit endpoint forces S to ignore **all traceless curvature**, including nonabelian distortion curvature.
2. The one-half quadratic term with its own unit linear endpoint then removes the remaining central-input map. Hence **S=0**.

This is an off-shell variational consistency theorem. It does not say an action with its correctly computed, different Euler equation has no stationary solutions. In particular the existing W2 stationary branches remain results about W2's actual symmetrized Euler map; they do not satisfy the endpoint premise silently used here.

| State | Exact scope |
|---|---|
| **ESTABLISHED** | Entire derived-input exclusion under the cubic identity, and total operator vanishing when the quadratic identity is also required. |
| **RULED OUT** | Every nonzero S satisfying this complete fixed-linear/full-translation/Spin-equivariant matched-first-action architecture. No remaining coefficient tuning within it helps. |
| **NOT MODELED / UNDETERMINED** | Source necessity of the complete realization, different or field-dependent operators, additional terms or changed endpoints, restricted variation spaces, merely on-shell equivalence, physical state selection and GU-wide falsification. |

No action, choice family or physical restriction is added. No canon, physics-ledger, source-register or class-C verdict changes. The choice inventory stays10 families/4 grouped obligations/bookkeeping net6/0 source-selected predictions; this is not a lower bound on independent source-required choices.

```gu-typed-objects
result: full fixed-linear matched-action Shiab consistency theorem
carrier: dimension14 full Dirac128 and full real u(H) primitive one-form translations; complexification gl128 with sl128 plus trace center LAYER=ambient CHIRALITY=N/A
pairing: fixed nondegenerate trace and top-form variation pairing; fixed smooth nonvanishing density if scalarized ON=adjoint_valued_forms
real_structure: Spin-compatible Hermitian H; complex-bilinear trace after owned real-form transfer, not Hermitian adjoint identification
grading: exterior degrees only; no physical chirality/index grading
action_owner: source-action first bosonic template under explicitly matched fixed-linear universal variation hypotheses
target: all curvature-input components of S MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** This tests a stated source-shaped architecture, without importing ordinary Higgs/family counting, a positive Hilbert space or a compact gauge replacement. Full-U and optional Sp tangents, K77/K95 real forms, geometric and physical outputs remain distinct. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Hypotheses and reuse

Let V have dimension14 and nondegenerate metric; let E be its full complex128 Dirac module. Fix a Spin-compatible nondegenerate Hermitian H, and the full real Lie algebra u(H). Let S be a pointwise real-linear Spin-equivariant map from adjoint-valued2-forms to adjoint-valued13-forms. Its smooth coefficients, metric, density and any fixed common dressing are held during primitive connection translation T. A fixed dressing transports S, representation and pairing together; it does not turn a varying coefficient into a held one by declaration. Full Spin equivariance here means an intertwiner on each held fibre. Covariance of a family S_z with an extra tensor z transformed at the same time does not establish that stronger property at fixed z; a horizontal/normal split or another symmetry-reducing tensor must be audited rather than silently dropped.

The owned [real-form adapter](riemann-realform-transfer-2026-11-27.md) extends this exact full-u(H) problem to gl(N,C), N=128, with complex-bilinear trace and complex Spin equivariance. We reuse it, including Hodge/volume normalization. No real K77/K95 identification or new native tensor census is needed.

With all other fields held, require the two **separately asserted** identities

    I3(T) = (1/3) <T,S(T wedge T)>,
    dI3(T)[b] = <b,S(T wedge T)>                    (C)

and, on compact local tests,

    I2(T) = (1/2) integral <T,S d_B T>,
    dI2(T)[b] = integral <b,S d_B T>.               (Q)

Equation(C) is pointwise, or follows pointwise from a universal local variational identity. Equation(Q) is an actual integrated/formal differential identity, not a coefficient-transpose assumption. B is any fixed ordinary matrix connection. The real problem extends complex-linearly after polarization.

The [Riemann-silence theorem](source-action-riemann-silence-2026-11-27.md) covers only injected algebraic Riemann inputs. The uncovered question here is the entire curvature domain, including non-Riemann distortion and trace input. The proof below uses elementary Hessian symmetry and the scalar quasicentroid of sl(N), not another finite-model census.

## 2. Pairing-normalized coefficients and exact factors

Work over C after the owned transfer. Write n=14, `g=gl(N,C)`, `s=sl(N,C)`, and `B(X,Y)=tr(XY)`. Fix a volume form and a coframe e^i. Define (n-1)-forms omega_i by

    e^a wedge omega_i = delta_ai vol.

Define coefficients of S for j<k by

    S((e^j wedge e^k) tensor Z) = sum_i omega_i tensor K_i^{jk}(Z),

and extend `K_i^{kj}=-K_i^{jk}`, `K_i^{jj}=0`. The subscript i here is a component label in the top-form dual basis, not an unaccounted metric-lowered index. This definition absorbs all exterior pairing signs. If a Hodge-raised convention is used instead, it must be converted to this pairing-normalized convention before comparing coefficients.

For `T=sum_i e^i tensor T_i`, ordinary matrix wedge gives

    T wedge T = sum_(j<k) e^j wedge e^k tensor [T_j,T_k],
    F_i(T) = sum_(j<k) K_i^{jk}[T_j,T_k]
           = (1/2) sum_(j,k) K_i^{jk}[T_j,T_k],
    I3(T) = (1/3) sum_i tr(T_i F_i(T)).

The endpoint premise is exactly

    dI3(T)[b] = sum_i tr(b_i F_i(T))  for all T,b.

Therefore the Hessian is symmetric:

    sum_i tr(c_i (DF_T b)_i) = sum_i tr(b_i (DF_T c)_i).       (H)

Also

    (DF_T b)_i = sum_(j,k) K_i^{jk}[T_j,b_k].

In particular, if T has only slot j equal to Y and b has only a distinct slot k equal to Z, then `(DF_T b)_i=K_i^{jk}[Y,Z]`, with no residual factor2. The universal endpoint premise is used only through this necessary Hessian symmetry; for a quadratic F, symmetric derivative also recovers the displayed one-third potential by Euler homogeneity.

## 3. First exclude central outputs on commutator inputs

Let z be any one-form whose coefficient matrices are central. Since F depends only on commutators, `DF_T z=0`. By (H),

    <z,DF_T b> = <b,DF_T z> = 0.

Taking b=T and using `DF_T T=2F(T)` shows `<z,F(T)>=0` for every central z. Thus every output component F_i(T) is traceless. Taking T supported on exactly two slots yields

    tr(K_i^{jk}[Y,Z])=0.

Commutators span s, so every `K_i^{jk}` maps s into s. This step is essential: a proof using traceless variations alone would only classify the traceless projection and could miss central output. The full trace pairing on gl(N) and the allowed central translation variations supply the missing test.

From this point restrict all K maps to s. The trace form on s is nondegenerate; its adjoint is the complex-bilinear transpose, never a Hermitian conjugate.

## 4. Repeated external indices vanish

Fix j != k. Set T_j=Y, b_k=Z, c_j=X and all other components zero. Then `DF_T c=0`, because T and c share their only exterior slot. Equation(H) gives

    tr(X K_j^{jk}[Y,Z])=0  for all X,Y,Z in g.

Nondegeneracy and perfectness imply `K_j^{jk}|s=0`. Interchanging j,k gives `K_k^{jk}|s=0`. Thus a nonzero restricted coefficient requires all three external labels i,j,k distinct. This is stronger than merely annihilating a selected family of bracket values.

## 5. Distinct triples give one quasicentroid map

For distinct i,j,k, set

    A=K_i^{jk}|s,  B=K_j^{ki}|s,  C=K_k^{ij}|s.

Use (H) at one-slot backgrounds and vary the two other slots. The exact cyclic identity is

    tr(X A[Y,Z]) = tr(Y B[Z,X]) = tr(Z C[X,Y])       (CYC)

for arbitrary X,Y,Z in s. The signs are positive in this cyclic ordering: the minus from reversing an exterior coefficient cancels the minus from reversing a commutator.

Let D=A*, E=B*, F=C* be trace adjoints. Trace invariance and nondegeneracy turn (CYC) into

    [D X,Y]=[X,E Y],
    [E X,Y]=[X,F Y],
    [F X,Y]=[X,D Y]                                 (Q3)

for all X,Y. Swap X,Y in the first relation to obtain `[E X,Y]=[X,D Y]`. Comparison with the second gives `[X,(F-D)Y]=0`; s is centerless, hence F=D. The third relation is now

    [D X,Y]=[X,D Y].                                (QC)

Comparison with the first gives E=D. Thus A=B=C, and their common trace adjoint is a quasicentroid element. No derivation term or independent symmetric cubic invariant has been left in the classification.

## 6. Direct sl(N) proof: QC is scalar for N>=3

Let D:s->s satisfy(QC). Setting Y=X and using characteristic0 gives `[D X,X]=0`.

Let h be the diagonal traceless Cartan. For regular H in h, its centralizer in s is h, so DH lies in h. Since regular diagonal H form a nonempty open subset and D is linear, `D(h) subset h` for every H.

For the matrix unit E_ab with a!=b, (QC) gives

    [D H,E_ab]=[H,D E_ab]  for every H in h.

Comparing off-diagonal matrix entries for all H shows

    D E_ab = c_ab E_ab + H_ab,  H_ab in h,
    alpha_ab(D H)=c_ab alpha_ab(H),  alpha_ab(H)=H_aa-H_bb.

For distinct a,b,c, `alpha_ac=alpha_ab+alpha_bc`, with alpha_ab and alpha_bc independent. Applying the preceding eigenfunctional equations forces

    c_ac=c_ab=c_bc.

Also `alpha_ba=-alpha_ab` gives c_ba=c_ab. Connectivity of the type-A root system (or successive triples of matrix labels) gives one scalar c for every ordered a!=b. The roots span h*, so `D|h=c Id`.

Now apply(QC) to E_ab and E_cd. The c-times-bracket terms cancel, leaving

    alpha_cd(H_ab) E_cd = -alpha_ab(H_cd) E_ab.

For different matrix units the two units are linearly independent, so `alpha_cd(H_ab)=0`. For the same unit, `[D E_ab,E_ab]=0` gives `alpha_ab(H_ab)=0`. Consequently all roots vanish on each H_ab. A diagonal traceless matrix with this property is zero. Hence `D E_ab=c E_ab` and finally `D=c Id` on s.

This proves the needed classification directly for N>=3, including128. It avoids any sl2 exception discussion about quasiderivations; those are a different space from the quasicentroid used here.

## 7. Remaining external tensor and Spin equivariance

Sections4–6 imply

    K_i^{jk}|s = c_i^{jk} Id_s,
    c_i^{jk}=0 if an index repeats,
    c_i^{jk}=c_j^{ki}=c_k^{ij},
    c_i^{jk}=-c_i^{kj}.

Thus c is totally alternating in its three external labels. Intrinsically, after fixing the invariant volume and metric identifications, it is an external alternating3-tensor (equivalently a3-form); no internal nontrivial tensor remains because the identity on s is invariant under conjugation.

Full Spin equivariance of S therefore makes c invariant under Spin(14,C). There is no invariant external alternating3-tensor. One immediate proof uses `-Id` in SO(14,C): it has determinant+1, lifts to Spin(14,C), and acts by -1 on exterior degree3. The internal identity is unchanged by conjugation. Hence c=-c and c=0.

For real signatures where -Id is not in the real identity component, use the already-owned infinitesimal-equivariance complexification and connected complex Spin group. Do not falsely assert membership in every real identity component. No new real-form-preservation assumption is required.

Therefore `S|Lambda2 V* tensor s=0`. Conversely, any fixed linear S supported only on the central curvature input has `S(T wedge T)=0` and I3=0, so the cubic endpoint identity holds automatically. Spin equivariance still constrains those central-input maps; the cubic imposes no further restriction on them.


## 8. The quadratic identity eliminates the central survivor

The cubic theorem by itself says S factors through the trace of its curvature input. It does **not** say the output on a central input is central. That distinction is essential.

Now use(Q). Let T be an arbitrary compactly supported traceless matrix-valued1-form and let b=a Id be a central1-form. Matrix covariant exterior differentiation preserves trace:

    d_B T is traceless,    d_B b = da Id.

The cubic result gives S(d_B T)=0. Direct differentiation of I2 and its asserted endpoint therefore imply

    0 = (1/2) integral <T,S(da Id)>                 (8.1)

for every such T and every central b. No integration by parts is needed for this mixed test; both terms containing S(d_B T) are already zero. The trace pairing on sl(N) is nondegenerate, so the fundamental lemma with arbitrary traceless compact T forces S(da Id) to be central pointwise.

At any point, an arbitrary2-form is da for a locally chosen1-form a whose jet is realized with a cutoff. Hence **S maps every central curvature input to central output**. This works for smooth variable coefficients and any held nonvanishing density: arbitrary compact tests detect the local coefficient. No global exactness or boundary premise is used.

But the central-to-central part is a Spin intertwiner

    Lambda2(V*) -> Lambda13(V*).

The complex element -Id acts by+1 on the domain and -1 on the codomain. The matrix center is fixed by conjugation. Equivariance forces this map to equal its negative, so it is zero. Combined with the cubic result on sl(N), this proves

    S = 0.                                         (8.2)

**Equivalent full formal-adjoint check.** Put P=S d_B. Equation(Q) gives the weak symmetry integral tr(u wedge P v)=integral tr(v wedge P u) on compact tests, including every coefficient/density derivative. Both pairings keep the1-form first and13-form second; reversing their wedge order would change the sign. Equivalently, Hodge-raise P before writing P=P^!. Since P kills all traceless inputs, weak formal symmetry forces its image to be central. After the cubic factorization through central inputs, Spin parity makes every output of S traceless, so P=0. Its principal symbol S_x(xi wedge a) vanishes for every xi,a; decomposable2-forms span, hence S=0. This is a full differential adjoint argument, never a transpose of a finite coefficient matrix.

### Isolating these identities in the first action

For the matched first-action template, the reference-curvature term is linear in T and contributes Euler degree0; the quadratic term contributes degree1; the cubic contributes degree2. Scaling arbitrary T separates these degrees. The matched mass term is a symmetric zero-order pairing and cancels identically in the variation comparison; in the central/traceless mixed test its cross pairing is zero. Independent fermions can be set to zero for this necessary off-shell test. Other action terms with their own unmatched coefficients or a different endpoint change the tested architecture; they are not silently included.

Holding epsilon and metric fixed is an explicitly independent primitive variation. Adding their Euler equations cannot repair an incorrect T variation. If one asks only whether two equations happen to agree on a restricted stationary set, that is a different, weaker question and is not excluded here.

## 9. Controls and limitations

Two positive controls keep the theorem honest:

- Without full Spin equivariance, a chosen alternating external3-tensor times the invariant Lie bracket gives a nonzero cubic satisfying(C). Thus covariance is a substantive premise, not a decorative label.
- An S supported only on central curvature input always has S(T wedge T)=0 and satisfies(C), even with noncentral output. It is the **additional quadratic identity**, not the cubic alone, that removes this survivor in the Spin-equivariant class.

The exact probe checks the relevant signs, traces and small matrix identities, plus planted failures. These are calibrations, not a numerical extrapolation from sl3 to sl128. The direct matrix-unit proof supplies the universal statement for N>=3; the inherited complexification supplies the native real-form bridge. Finite Lean cores check algebraic implications, not the full source, smooth variational or representation theorem.

The excluded class requires full primitive translations, full complex Dirac, fixed pointwise linear S, full Spin equivariance, ordinary matrix curvature, the trace pairing and both universal matched endpoints. Restricted tangents, extra tensor backgrounds reducing the symmetry, derivative-valued or genuinely T-dependent operators, a changed functional/endpoint, or only on-shell equivalence alter these assumptions. None is constructed or credited as a viable source repair. Optional Sp is not automatically covered by a full-U proof.

## 10. Source relevance and the remaining bridge

Source custody is reused from [the November13 primitive-prescription audit](source-prescription-current-2026-11-13.md), [WGS-01](../../lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md#wgs-01--weinstein-did-write-a-concrete-first-order-bosonic-action) and SC-ACT-01/02. The primary2021 draft p44 equation(9.4) prints the1/2 and1/3 terms; equation(9.7) claims the fixed-epsilon translation variation, with the unit curvature endpoint displayed in(9.8)–(9.10). Sections3.6 and5 supply full U(64,64) and all adjoint-valued1-form translations. The coefficients alone do not establish the claimed derivative: their joint consistency is exactly what is being tested.

The source-defined Phi tensors depend on metric and epsilon, held in this variation; they are not functions of primitive varpi on the displayed slice. Merely mentioning moving epsilon/metric therefore does not evade the theorem. A genuinely translation-dependent or derivative-valued construction would require its actual source and variation formula. The theorem does not declare all such possibilities impossible.

**What changed:** a non-Riemann direct-curvature channel no longer survives inside the same fixed-linear architecture, and the central-input survivor disappears once the printed quadratic identity is required too. No assumption of a nonzero direct Einstein/Ricci response is needed for this total-zero conclusion.

**The displayed grammar supplies its symmetry premise.** Definition8.1, equation(8.7), on printed p42 explicitly defines Phi_i as Spin(7,7)-invariant tensors; p43 equation(9.3) uses their wedge/Hodge contractions and coefficient products. Every well-typed product choice therefore gives a fixed-fibre intertwiner at epsilon=1. Fixed common epsilon conjugation transports the Spin action with it. No additional horizontal/normal projector occurs in this displayed tree. The missing product selector does not make its symmetry unknown. [Primary draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf#page=42).

**Pairing and bracket custody are already available.** The expanded first action in equation(9.4) explicitly uses matrix trace. The owned K77-B normalization audit fixes q(T)=T wedge T and the unhalved coefficient operations. The residual-norm ambiguity for the second action I2B does not make the first action's matrix pairing unknown. Equation(9.12) belongs to I2B and is not a repetition of the first-action variation(9.7). The remaining formula-specific step is attribution of existing nonzero witnesses to the displayed Phi basis/product choices and their common typed operator, not another trace or bracket calculation.

**What remains unproved here:** that final nonzero source-formula attribution, and that every broader faithful realization must retain the same complete architecture. A different endpoint or a different formula is not covered automatically. Extra-tensor covariance is a general scope boundary, not an unresolved tensor hidden inside the displayed Phi1/Phi2 tree. Consequently the accepted ceiling is a conditional architecture exclusion, not GU falsification or an empty class-C intersection. No physics-ledger verdict is changed.

The result consumes further fixed-linear full-U endpoint-map searches under identical premises, including different coefficients and signature-only retests. The actual W2 Euler map remains outside the matched-endpoint premise. Its prior stationary/instability results are neither erased nor upgraded by this theorem.

## 11. Prior art and verification

The algebraic ingredient is classical: Burde–Dekimpe, [section5 Theorem5.4 and Corollary5.5](https://homepage.univie.ac.at/dietrich.burde/papers/burde_44_postlie_der.pdf), states the perfect-centerless quasicentroid theorem of Leger–Luks and its scalar-simple consequence. Section6 above supplies a direct matrix-unit proof for the required sl(N) case, so no unread original proof is an operative dependency. The source-architecture application is new relative to the owned Riemann restriction; no claim of world novelty is made without a separate prior-art assessment.

Fresh root replay passed33 grouped exact controls, including512 cyclic trace triples and64 three-map residual identities, in0.174301875seconds. The deterministic certificate is5,683bytes. A central-input fixture has action derivative−1/60 versus unit endpoint−1/30; changing the variation labels does not repair that factor. This is a calibration outside the fullSpin class, not a substituted native source witness.

Exact controls, finite Lean scope, independent acceptance and gate results are recorded in [evidence](../../lab/process/full-shiab-consistency.json) and [review](../../lab/process/hostile-reviews/2026-11-27-full-shiab-consistency-review.md).

```sh
python3 tests/program-focus/full_shiab_consistency_probe.py --verify
```
