---
title: "RB5: the Clifford-plane soldering field cannot own the complex--Cartan flag; spectral ownership has an exact conditional calculus but no GU-native source"
status: "completed exploration; exact stabilizer obstruction and conditional finite calculus; physical Hessian ineligible"
date: "2026-07-30"
run_id: "GUH-20260731T015054Z-rb5-flag-ownership-hessian"
---

# RB5 flag ownership, spectral preflight, and Hessian eligibility

## Result

RB5 decides the first branch of the RB4 ownership trilemma.

The only explicit finite-local \(\epsilon_{\rm IG}\) realization currently
built in the repository is the unframed Clifford-plane orbit

\[
\epsilon_{\rm plane}\in\Gamma(P_G/H_{\rm Cl}),
\qquad
G=\operatorname{Sp}(32,32;\mathbb H),
\qquad
H_{\rm Cl}^0=\operatorname{Spin}_0(9,5).
\]

The corresponding global associated bundle and reduction remain conditional.
At this local homogeneous-space grade it **cannot** equivariantly determine
the complete trace-reversed
complex--Cartan flag. The obstruction appears before \(J\): the
\(\operatorname{Spin}(9,5)\) stabilizer moves even the prerequisite
\((3,1)+(6,4)\) split. A local lift can transport an arbitrarily chosen
flag, but another lift of the same Clifford plane returns a different flag.
That is seed smuggling, not ownership.

The correct homogeneous-space arrow is the reverse refinement:

\[
\boxed{
\epsilon_{\rm flag}\in\Gamma(P_G/L_{\rm flag})
\longrightarrow
\epsilon_{\rm plane}\in\Gamma(P_G/H_{\rm Cl}).
}
\]

Here

\[
L_{\rm flag}
=
\operatorname{Stab}_{\operatorname{Spin}(9,5)}
\left(
V_{3,1}\oplus V_{6,4},
P_W,J,t,\Omega_{\mathbb C}
\right).
\]

Thus the current \(\epsilon_{\rm plane}\) can be the forgetful image of a
full flag field. It cannot recover the information forgotten by that map.

The rival spectral route is mathematically viable **conditionally**. An
admissible/definitizable, real-spectral, uniformly gapped
\(G_{\rm DW}\)-self-adjoint endomorphism \(H\), with a measured
nondegenerate negative-definite sector, can define

\[
P_W=\mathbf1_{(-\infty,0)}(H),
\]

and an admissible invertible \(G_{\rm DW}\)-skew endomorphism \(Q\) for
which \(-Q^2\) has the required positive-real inverse-square-root branch can
define

\[
J=Q(-Q^2)^{-1/2}.
\]

The planted seeds intentionally encode the desired \(6+4\)/complex geometry.
The executable validates the recovery constructions, their first derivatives,
joint \(O(6,4)\) covariance, raw-Frobenius failure, gap and singularity
kills, and a local central-\(U(1)\) trace gate. But the \(H,Q\) inputs are
planted source-shaped controls. No current GU field is mapped to them by a
typed, target-free, source-owned concomitant.

The physical gauge-quotiented Hessian is therefore **not eligible**. The
finite Hessian fixture correctly distinguishes gauge zeros, strict physical
positivity, a modulus, and an instability, but the GU action still lacks a
source-derived flag map, stationary background, full coupled linearized/BV
complex, retained-mode closure, and analytic domain.

The datum ledger is unchanged. P1/P2 remains the conditional orientation
line, P3 remains separate, and a frozen complex--Cartan flag remains a new
continuous external spurion.

## Plain English

The previous swing found the object we want the theory to choose: a moving
flag containing the \(6+4\) split, the complex structure, the trace
direction, and the determinant-one information.

This swing asked whether the soldering field we already had secretly
contained that choice.

It does not. The existing soldering field remembers a fourteen-dimensional
Clifford plane but forgets the frame and reductions inside it. Many different
complex--Cartan flags give the same Clifford plane. Moving between those
flags does not change the old soldering field at all.

That is useful because it closes a false economy. We cannot say “the flag
was already in \(\epsilon_{\rm IG}\)” and avoid paying for its origin.
Instead there are now two honest construction routes:

1. refine the soldering field so that the flag is part of the field and let
   the action select or gauge its refinement directions; or
2. derive the flag from other source fields through a spectral construction.

The second route has now been made exact enough to test. If the action
produces the right kinds of \(H\) and \(Q\), the projector, complex
structure, and all their variations follow without adding independent
matrices. But the action does not yet produce them. The remaining problem is
no longer “invent a flag”; it is “find a target-blind, typed source map whose
spectral data generate this flag.”

This is still the same source-action/external-datum build. The source review
and Weinstein's \(t\mapsto Jt\) clue narrowed the target; RB4 built its
geometry; RB5 has now rejected one owner and made the rival owner's receipt
executable.

## 1. Layer 0

| phrase | RB5 object | distinct object |
| --- | --- | --- |
| source \(\epsilon\) | gauge transformation in the inhomogeneous gauge group | N1 soldering field |
| N1 \(\epsilon_{\rm IG}\) | abstract varied IG/soldering section; bundle still unspecified | an explicit homogeneous orbit |
| RB3 \(\epsilon_{\rm plane}\) | unframed Clifford-plane reduction \(G/H_{\rm Cl}\) | a full frame or flag |
| refined soldering field | \(G/L_{\rm flag}\) with a forgetful map to \(G/H_{\rm Cl}\) | data derived from the coarse quotient |
| vertical Cartan projector | \(P_W\) on the trace-reversed \((6,4)\) fibre | the ambient spinor Krein grading or the \(Sp\) compactifier |
| compatible \(J\) | orthogonal complex structure preserving \(P_W\) | the observer, trace projector, or canonical fibre tensor |
| spectral \(H,Q\) | potential composite owners in \(\operatorname{End}(V_{6,4})\) | the flag they are meant to derive |
| formal Hessian | a second derivative of a declared functional | a physical quotient spectrum |
| determinant trace | a local Lie-algebra condition | a global complex volume and central quotient |
| P1/P2 | flat real vertical-symbol orientation line | a continuous flag refinement |
| P3 | relative real-\(KO\) input | a flag dimension, spectral rank, or Hessian nullity |

The 2021 source \(\epsilon\) and N1 \(\epsilon_{\rm IG}\) remain a
Layer-0 homonym. The source object enters

\[
T_\omega=\varpi-\epsilon^{-1}d_0\epsilon
\]

as a gauge transformation. N1 uses \(\epsilon_{\rm IG}\) as a varied
soldering object intended to move the Clifford plane. No source passage
constructs their identity.

## 2. Exact \(\epsilon_{\rm plane}\)-to-flag obstruction

### 2.1 Homogeneous-space criterion

For homogeneous spaces, a \(G\)-equivariant map

\[
G/H\longrightarrow G/L
\]

is determined by an \(H\)-fixed target point. Equivalently, after conjugating
the seed if necessary,

\[
H\subseteq L.
\]

This condition enforces independence from the local lift. If
\([g]=[gh]\in G/H\), then a proposed transported seed \(g\mathfrak f_0\)
descends only when

\[
h\mathfrak f_0=\mathfrak f_0
\qquad
\text{for every }h\in H.
\]

Merely transporting one chosen seed proves covariance of a framed family.
It does not prove ownership by the quotient field.

### 2.2 The RB3 stabilizer is too large

RB3 constructs

\[
H_{\rm Cl}^0=\operatorname{Spin}_0(9,5),
\qquad
\dim H_{\rm Cl}=91.
\]

Before selecting \(P_W\) or \(J\), the target flag must preserve

\[
V_{9,5}=V_{3,1}\oplus V_{6,4}.
\]

The stabilizer of this split is only

\[
\operatorname{Spin}(3,1)\times\operatorname{Spin}(6,4),
\qquad
\dim=6+45=51.
\]

Forty generators of \(\mathfrak{so}(9,5)\) mix the two summands. The
executable constructs all 91 standard generators and obtains

```text
split-preserving generators: 51
split-moving generators:      40
```

It also computes the commutant of the full standard
\(\mathfrak{so}(9,5)\) action on \(V_{9,5}\). The commutant has dimension
one, so it contains only scalar endomorphisms and no nontrivial rank-four or
rank-ten invariant projector.

A concrete lift-change control gives

```text
same point in G/H_Cl, different lift:
  ||h P_vertical h^-1 - P_vertical|| = 0.404397515
```

The flag therefore cannot descend from the coarse quotient.

### 2.3 Direction of the repair

Locally, ignoring discrete quotients,

\[
\dim G
=64(2\cdot64+1)
=8256,
\]

\[
\dim(G/H_{\rm Cl})=8256-91=8165.
\]

In the vertical \((6,4)\) fibre:

- a Cartan split costs 24 directions;
- a compatible \(J\) at fixed split costs another 8;
- \(U(3)\times U(2)\) has dimension 13;
- complex-volume/unimodularity reduces it locally to
  \(S(U(3)\times U(2))\), dimension 12; and
- fixing the real trace vector inside the negative complex two-plane leaves
  the evident vertical \(S(U(3)\times U(1))\), dimension 9.

Together with the abstract base \(\operatorname{Spin}(3,1)\), an evident
split-model flag stabilizer has dimension 15. The corresponding refinement
fibre inside \(H_{\rm Cl}\) has local dimension

\[
\dim(H_{\rm Cl}/L_{\rm flag})=91-15=76.
\]

This is an abstract local reduction dimension, not a physical count and not
a final N1 stabilizer. The actual symmetric-metric soldering, \(P_0\),
\(\rho\), \(Y\), domain, action tensors, and global quotient can reduce it
further.

The important fact is the arrow:

\[
G/L_{\rm flag}\longrightarrow G/H_{\rm Cl}.
\]

The existing RB3 projector, chirality, \(A_0\)-induced connection candidate,
and Clifford transport survive after composing with this forgetful map.

## 3. Action consequence of the refined field

Let

\[
q:P_G/L_{\rm flag}\longrightarrow P_G/H_{\rm Cl}.
\]

The RB3 connection candidate

\[
\Gamma^{A_0}_{\epsilon}
=
A_0-g\operatorname{pr}_{\mathfrak m}
\left(
g^{-1}A_0g+g^{-1}dg
\right)g^{-1}
\]

depends only on \(q(\epsilon_{\rm flag})\). Its derivative therefore
annihilates the flag-refinement tangent:

\[
D\Gamma^{A_0}_{\epsilon}
\big|_{\ker Dq}
=0.
\]

The existing connection/soldering action cannot select the missing flag
directions through this term.

If the full source-completed action is extended to use the flag, its Euler
covector is

\[
\boxed{
\begin{aligned}
\mathcal E_{\epsilon_{\rm flag}}
={}&
(Dq)^!\mathcal E_{\epsilon_{\rm plane}}
+(DP_W)^!\mathcal E_P
+(DJ)^!\mathcal E_J\\
&+(Dt)^!\mathcal E_t
+(D\Omega_{\mathbb C})^!\mathcal E_\Omega .
\end{aligned}
}
\]

There are then two sharply different outcomes:

1. if every term factors through \(q\), the refinement directions are
   invisible to the action and require an actual gauge/BRST quotient before
   being called redundant;
2. if Standard Model or zero-order terms depend on the refinement, those
   directions are physical order-parameter candidates and need their own
   projected Euler equation and Hessian.

The conditional fermion/full-20 bilinears cannot select a bosonic vacuum at
\(Z=\psi=0\). A source-derived bosonic dependence is still required.

## 4. Conditional spectral and polar construction

### 4.1 Cartan projector from \(H\)

Assume a smooth, admissible/definitizable, real-spectral, uniformly gapped
endomorphism satisfying

\[
H^{\dagger_G}=H.
\]

Freeze the target-blind cluster rule before reading its rank:

\[
P_-(H)=\mathbf1_{(-\infty,0)}(H)
=
\frac{1}{2\pi i}
\oint_\gamma(z-H)^{-1}\,dz.
\]

The first derivative is

\[
D_HP_-[\dot H]
=
\frac{1}{2\pi i}
\oint_\gamma
(z-H)^{-1}\dot H(z-H)^{-1}\,dz.
\]

In the deterministic fixture:

```text
minimum spectral gap:              1.100
measured negative-sector rank:     4
restriction signature:             (0,4)
complement signature:              (6,0)
joint covariance defect:           numerical zero
frozen-projector residual:          1.940205721
analytic/finite-difference error:   2.461e-11
```

The rank and signature are outputs of the predeclared sign rule in the
fixture. The planted seed intentionally encodes the desired sign geometry.
A real source computation may return another rank, complex or Jordan
spectrum, an indefinite selected sector, or no uniform gap.

### 4.2 Complex structure from \(Q\)

Assume

\[
Q^{\dagger_G}=-Q,
\]

with \(Q\) invertible and \(-Q^2\) admitting the required positive real
functional-calculus branch. Define

\[
R=(-Q^2)^{-1/2},
\qquad
J=QR.
\]

For

\[
\dot A=-(\dot Q\,Q+Q\dot Q),
\]

\[
\dot J
=
\dot Q\,R
+Q\,D(A^{-1/2})[\dot A].
\]

The executable obtains:

```text
J^2 + 1:                           numerical zero
J^T G J - G:                       numerical zero
[J,P_W]:                           numerical zero
frozen-J residual:                 2.173961650
analytic/finite-difference error:  7.216e-11
```

The controls reject singular \(Q\), invalid square-root spectrum, and raw
Frobenius \((7,3)\). On the raw comparator the same planted rank-four plane
has signature \((1,3)\), and the odd--odd metric inertia forbids an
orthogonal real \(J\).

### 4.3 Why this is not yet ownership

The planted \(H,Q\) deliberately contain a compatible \(6+4\) and complex
pairing pattern. They validate the recovery calculus and its failure gates.
They do not explain why GU produces those inputs.

This does not contradict VG-V3. That result forbids a \(J\) compatible with
the unbroken trace-line projector and the named Lorentz/isotropy data. The
RB5 plant does not commute with the trace-line projector: it sends
\(t\) to the distinct direction \(Jt\). It is therefore an explicit
symmetry-breaking input, exactly as the Into the Impossible reading suggests,
not a native \(J\) extracted from the old invariant data.

A genuine source-owned candidate must provide a typed natural concomitant

\[
(A,U,P_{\rm IG},\epsilon_{\rm IG},s,\text{curvature},\ldots)
\longrightarrow
(H,Q)\in\operatorname{End}(V_{6,4})^2
\]

without using \(P_W,J,\Omega_{\mathbb C}\), a chosen four-plane, or a
target-labelled basis in the adapter.

## 5. Target-blind source-concomitant audit

| candidate owner | native carrier | missing step before \(H,Q\) |
| --- | --- | --- |
| \(\epsilon_{\rm plane}\) | \(G/H_{\rm Cl}\) | exact stabilizer obstruction above; cannot even select the \(4+10\) split |
| \(\Gamma^{A_0}_{\epsilon}\) | connection built from the coarse quotient | factors through \(q\) and is flat along the flag-refinement fibre |
| distortion \(\theta\) | \(\Omega^1(Y,\operatorname{ad}P)\) | no target-free form/adjoint contraction and real representation to \(\operatorname{End}(V_{6,4})\) |
| curvature \(F_A\) | \(\Omega^2(Y,\operatorname{ad}P)\) | requires a typed contraction/Hodge/Riesz map, vertical restriction, and stationary background |
| mixed vertical connection | vertical one-form/coindex plus adjoint value | retained-mode map and complete off-diagonal Euler closure absent |
| section Hessian / second fundamental form | symmetric base coindices plus normal/vertical value | not the connection-field Hessian; no natural endomorphism adapter supplied |
| spinless gauge-potential component | source \(\Omega^1(\operatorname{ad})\) role | exact representation and full-20/vertical placement absent |
| pure trace mode | decomposable trace coefficient | its wedge square vanishes; it cannot produce its own Yang--Mills quartic |

No row currently emits a type-complete \(H\) or \(Q\).

This is not a proof that no natural concomitant exists. It is a repository
ownership result: the required adapters are unbuilt. Equally natural
contractions must be compared because W246 already shows that faithful,
equivariant self-adjointization choices can reverse a downstream selector.

## 6. Extra-\(U(1)\) gate

At compatible-flag grade, \(J\) itself generates the central
complex-linear direction. For a complex-linear generator \(X\), the finite
fixture uses

\[
c_J(X)=-\frac1{10}\operatorname{tr}(JX)
\]

and subtracts

\[
X_{\rm uni}=X-c_J(X)J.
\]

This exactly removes the planted central direction and leaves a balanced
complex-linear generator.

That is only a local Lie-algebra control. A physical determinant-one result
still requires:

1. global triviality of the complex determinant line;
2. a selected unit parallel complex-volume section;
3. a connection preserving that section;
4. the correct determinant action \(3\alpha+2\beta\) on the same complex
   rank-five bundle;
5. the global central kernel giving the \(\mathbb Z_6\) quotient; and
6. the actual lift and charge normalization on the fermion representation.

Thus RB5 does not claim the Standard Model gauge group or hypercharge.

## 7. Hessian eligibility and the finite discriminator

A physical flag Hessian is not an independent matrix if the flag is
composite. If

\[
\mathfrak f
=
\mathfrak f(H(\phi),Q(\phi)),
\]

then the original field \(\phi\) must be varied:

\[
\begin{aligned}
\mathcal E_\phi\mapsto\mathcal E_\phi
&+(D_\phi H)^!(D_HP_W)^!\mathcal E_P\\
&+(D_\phi Q)^!(D_QJ)^!\mathcal E_J+\cdots.
\end{aligned}
\]

Adding a separate flag Hessian would double-count the composite directions.

The prior vertical-Hessian owner already establishes that gauge-orbit
directions are Hessian-null only at a stationary background. Off shell, the
gradient times the curvature of the gauge orbit participates in the
invariance identity.

The eventual physical object is the cohomology of the full coupled
linearized/BV complex at a stationary, domain-equipped solution. It must
include:

- \(A,U,P_{\rm IG},\epsilon,s,Z\) and the flag composite;
- connection--Goldstone and section--flag mixing;
- constraints, ghosts, antifields, and boundary conditions;
- moving Hodge, density, pairing, and domain;
- retained/discarded off-diagonal leakage; and
- right-\(\mathbb H\) and P3 compatibility.

RB5's seven-dimensional fixture is deliberately smaller. It proves that the
classifier has power:

```text
explicit gauge kernel dimension:       2
stable quotient eigenvalues:           0.8, 1.4, 2.1, 2.9, 3.8
modulus quotient eigenvalues:          0, 1.4, 2.1, 2.9, 3.8
unstable quotient eigenvalues:        -0.6, 1.4, 2.1, 2.9, 3.8
```

A positive quartic stabilizes the planted zero-Hessian modulus at fourth
order, while the negative quadratic direction still wins locally in the
unstable control. The action is exactly invariant along the planted gauge
directions.

These are control eigenvalues, not GU masses or multiplicities.

## 8. Five-leg disposition

| leg | RB5 result | still required |
| --- | --- | --- |
| SM/Yukawa/provenance | complete flag type and local central-\(U(1)\) detector retained | global volume/\(\mathbb Z_6\), \(P_0/\rho/Y_K/Y_C/C\)-reality placement, retained modes, charges |
| quantum/Krein/BV | native DeWitt/Krein functional calculus and composite chain rule explicit | stationary full BV complex, gauge cohomology, CME, physical inner product/domain |
| gravity/cosmology | trace reversal remains load-bearing; flag stress is named | source-derived background, section/Hodge response, Gauss terms, cosmological solution/value |
| UV/causality | moving Clifford-plane construction survives through the forgetful map | refined-soldering subprincipal symbol, \(g=1\) retest, common curved cone and boundary |
| P3/index/count | right-\(\mathbb H\) and P3 remain mandatory interfaces | common global domain, twisted family/pushforward, no count before index receipt |

Finite pointwise matrices cannot close any of these global legs. They can
only prevent a later candidate from silently violating their local algebraic
interfaces.

The W240/W243 ambient compactification boundary also remains active. The
vertical flag is not automatically the ambient
\(\operatorname{Sp}(32,32;\mathbb H)\) good-stable, and its Cartan component
is not a chirality-safe even order parameter under the no-go's hypotheses.
No RB5 calculation upgrades the surviving non-extremal timelike corridor to
a GU-native condensate.

## 9. Datum and action ledger

| object | current ownership |
| --- | --- |
| P1/P2 | one conditional flat real orientation line \(L_\sigma\) |
| P3 | separate relative real-\(KO\) input |
| \(\epsilon_{\rm plane}\) | constructed moving Clifford-plane orbit at finite local grade; global associated reduction conditional |
| complete flag from \(\epsilon_{\rm plane}\) | **refuted** |
| refined \(\epsilon_{\rm flag}\) | typed new field/reduction; action/gauge status unbuilt |
| \(H,Q\) spectral composites | exact conditional calculus; source inputs unbuilt |
| frozen flag | new section-valued continuous external spurion |
| physical flag Hessian | ineligible |

RB5 therefore does not add a new item to the accepted external-datum ledger.
It proves what would be added if construction fails.

## 10. Constraint-surplus boundary

The spectral route introduces no fitted numerical coefficient in the finite
calculus, but its source adapter is not yet typed. Every unresolved
contraction, Riesz map, representation, functional-calculus branch,
background, and boundary condition consumes construction freedom.

Therefore the honest surplus verdict is

```text
SURPLUS-UNCOMPUTABLE:
  source-to-(H,Q) adapter and independent constraint rank are unbuilt.
```

The planted fixture is useful because it freezes those choices and shows
that the downstream consequences are highly constrained. It is not evidence
that the upstream choices are free of fit.

## 11. Fired and retained kill conditions

Fired:

1. direct \(\epsilon_{\rm plane}\to\)flag ownership;
2. local-lift-independent descent;
3. source-owned \(H,Q\) at the current repository grade;
4. physical quotient Hessian at the current action/background/domain grade;
5. global Standard Model determinant-one claim;
6. raw-Frobenius replacement;
7. gapless \(H\), singular \(Q\), and frozen-flag controls.

Retained:

1. refined \(\epsilon_{\rm flag}\) as a candidate dynamical field;
2. source-derived spectral/polar ownership after a type-complete target-blind
   concomitant is built;
3. local extra-\(U(1)\) rejection as a necessary control;
4. the quotient-Hessian classifier for use only after stationarity and full
   BV/domain closure.

No rank, dimension, nullity, flag component, support block, or transcript
phrase is a physical count.

## 12. Next highest-information construction

Run RB6 as a target-blind source-concomitant and stationarity gate:

1. Freeze a small grammar of natural \(H,Q\) candidates from the existing
   distortion, curvature, mixed vertical connection, moving-section
   Hessian, and spinless source fields.
2. Forbid \(u,P_W,J,\Omega_{\mathbb C}\), a chosen \(6+4\) block, rank four,
   and target-labelled gamma matrices from every input and cluster rule.
3. Type every form/adjoint/representation/Hodge/Riesz/vertical-restriction
   adapter. If no row reaches \(\operatorname{End}(V_{6,4})\), stop with
   `SPECTRAL-OWNERSHIP-BLOCKED-BY-TYPE`.
4. On the already source-owned W177 curvature background, compute
   \[
   D_{A_0}^*F_{A_0}.
   \]
   A nonzero residual kills physical Hessian use at that background.
5. For each type-correct survivor, compare at least one equally natural
   contraction and measure, rather than prescribe, spectral rank,
   signature, gap, polar admissibility, and stabilizer fixed set.
6. Only after a stationary, unique, smooth, uniformly gapped composite
   survives, compute retained/discarded Hessian leakage and the full
   linearized/BV quotient.

This sequence advances the source action directly. It does not add an
arbitrary flag potential or repeat the conclusion that an action is needed.

## Validation

Passing:

```text
python3 -B tests/channel-swings/rb5_epsilon_flag_ownership_spectral_hessian_probe.py
python3 -m py_compile tests/channel-swings/rb5_epsilon_flag_ownership_spectral_hessian_probe.py
git diff --check
```

The direct probe contains powered failures for stabilizer descent, local
lift ambiguity, raw Frobenius, frozen \(P/J\), gap closure, singular polar
data, central \(U(1)\), a physical modulus, and instability.

No source-derived flag, physical compactification, stationary vacuum,
Standard Model identification, mass, cosmological value, anomaly/CME
closure, common domain, index, or generation count is claimed.
