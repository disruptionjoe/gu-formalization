---
title: The analytic W2 stationary branch fails the printed endpoint at cubic order
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Decide the first uncomputed on-shell coefficient and, if nonzero, extend two isolated
  counterexamples to a punctured analytic branch interval.
actual_delta: The horizontal theta0 gamma05 endpoint coefficient is (183/8)h^3+O(h^4). Every sufficiently
  small nonzero-h member of the owned W2 stationary branch violates the separately printed endpoint, including
  literal raised observation.
class_covered: The unique local analytic invariant stationary branch through h=0 of the fixed W2 K95 full-U
  candidate, with its held source-shaped product/dressing dictionary and product-regulator coupled variational
  class. Also every zero-preserving recovery class containing any such witness. Not all stationary fields,
  all C or source GU.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-02
- lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md#WGS-01
- explorations/conditional-build/source-action-endpoint-onshell-2026-11-27.md
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
- lab/process/source-action-deep-coefficients.json
source_bridge:
  status: conditional
  reason: SC-ACT-01 p44eq9.4 and SC-ACT-02 p45eq9.8-10 supply action and printed endpoint templates; W2
    reconstructs their selector, primary-minus K95, pairing and dressing dictionary. Source uniqueness
    and physical-state admission remain unproved.
kill_condition: A certified nonzero leading horizontal component excludes E=0 implies R_print=0 for every
  sufficiently small nonzero h on this fixed branch. No new physical boundary, state rule or alternative
  action is inferred.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-W2-ANALYTIC-BRANCH-PRINTED-ENDPOINT-IDENTIFICATION
internal_target_verdict: excluded on a punctured small-h interval, including literal raised observation
canon_verdict_change: none
---

# The analytic stationary branch fails the printed endpoint at cubic order

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Decide the first uncomputed analytic on-shell coefficient with the smallest existing receiver.
actual_delta: A nonzero horizontal cubic coefficient excludes the held endpoint implication throughout a punctured small-h interval.
```

## Result in plain English

The constructed action's stationary solutions and its separately printed source-shaped equation agreed through the first two orders near the reference connection. **They disagree at the next order.** One component that survives literal observation is

\[
\ell(R_{\rm print}(T(h)))=\frac{183}{8}h^3+O(h^4),\qquad h=1/\kappa.
\]

Thus every sufficiently small nonzero member of this actual convergent stationary branch fails the printed equation. The earlier two finite-coupling root counterexamples are no longer the only witnesses. Selecting a different sufficiently small member of this same branch cannot repair the identification.

This is a **candidate-level equation-compatibility exclusion**, not a falsification of GU. The source supplies both templates, but has not selected this reconstruction of their shared dictionary. The action's solutions remain solutions of its actual variational equations. No physical state, global boundary problem, source-selected prediction or alternative action is supplied.

| State | Finding |
|---|---|
| **ESTABLISHED** | Exact nonzero cubic receiver; inherited analytic convergence and full coupled local stationarity imply a punctured interval of counterexamples. |
| **RULED OUT** | The fixed branch's identification with the printed endpoint at sufficiently small nonzero h; zero-preserving recovery from the actual Euler tuple on a class containing one of these witnesses. |
| **NOT MODELED / UNDETERMINED** | A different source realization or physical state restriction; all stationary fields; a numerical exclusion radius; continuation to either kappa1 root; global state admission; GU falsification. |

```gu-typed-objects
result: cubic on-shell printed-endpoint obstruction on an analytic stationary branch
carrier: actual K95 full-U adjoint-valued one-form; full ambient adjoint fibre retained under literal section contraction LAYER=ambient+observed BRIDGE=raised_literal_section_contraction CHIRALITY=N/A
pairing: declared native real trace/form pairing and absolute density ON=adjoint_valued_forms
real_structure: primary-minus K95 u64,64; full complex Dirac; independent matter and bars zero
grading: exterior and Clifford coefficient receivers, no physical chirality or family index
action_owner: repository-construction fixed W2 action and its actual Frechet-adjoint Euler derivative
target: source-shaped printed endpoint under the held dictionary MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The constructed action and printed endpoint remain distinct equation owners. This is not an ordinary Higgs, repeated-family, positive-metric or Yang–Mills-square replacement. Preserve source2+1, independent bars, fullU/optionalSp, primary-minus and K95/K77. See [routing](../../lab/methods/source-native-comparator-routing.md).

## 1. What is inherited, and what is new

[The on-shell comparison](source-action-endpoint-onshell-2026-11-27.md) already proves:

- the exact action-owned equation and its eliminated endpoint defect;
- full ambient first and second defect coefficients equal zero;
- a complete 59-coordinate receiver polynomial with exact native controls;
- two certified kappa1 stationary roots with nonzero endpoint residuals.

[The analytic existence result](source-action-homogeneous-analytic-vacuum-2026-11-25.md), §§A4/B1, gives an actual local convergent branch in the full216-dimensional invariant space. The owned reflection/reality symmetry calculation places this branch automatically in the compatible59-dimensional fixed space. Uniqueness near zero makes these the same branch; this is not an optional Sp physical-parent restriction or a smaller ansatz replacing the fullU problem. Its base-metric equation vanishes for compact base variations in the fixed product regulator, while zero independent matter and the dressed epsilon redundancy solve their respective variational equations. This is not an unrestricted14D metric variation or global physical domain.

The new computation is **only the cubic endpoint discrepancy**. It reuses the accepted series coefficients and receiver, checks their dependencies, and compares the relevant small forms against native differential/Clifford operations. It does not re-search roots or regenerate the59-dimensional quadratic tensor.

## 2. Use the eliminated endpoint, not an incomplete substitution

With all geometry and conventions as in the predecessor, write

\[
E(T)=\kappa T+S+KT+N(T,T),\qquad
R_{\rm print}(T)=\kappa T+S+PT+\Phi(T\wedge T),
\]

where K is the actual formal-adjoint symmetrization of P and N is the actual symmetric quadratic Euler term. Let

\[
A=P-K,\quad Q(U,V)=\tfrac12\Phi(U\wedge V+V\wedge U)-N(U,V).
\]

For every actual stationary field, exactly

\[
R_{\rm print}(T)=AT+Q(T,T).
\]

The normalized equation is T+h(S+KT+N(T,T))=0, giving

\[
t_1=-S,\quad t_2=KS,\quad t_3=-K^2S-N(S,S).
\]

Thus C3=A t3+2Q(t1,t2). Substituting a branch truncated at h3 into the original endpoint would miss t4/h at this order. Eliminating E first avoids that error.

## 3. Three exact entries decide the question

Use the existing receiver `KS_pivot_4`, the coefficient of theta0 gamma05 at the held homogeneous point. Its exterior mask is1 and Clifford mask33. The native pairing weight is8, already divided out in the stored receiver polynomial. Optional4D index raising on this horizontal slot has factor+1.

The **entire linear row is zero** on the invariant59-space, not merely its value on t1 or t2. Therefore ell(A t3)=0 and this receiver does not need t3. The only supported coordinates of the first two branch terms are

\[
t_1=(21/4)e_0+(21/4)e_1+(15/4)e_2,\qquad t_2=(3/8)e_4.
\]

The inherited symmetric matrix entries are Q04=4/3, Q14=2/3 and Q24=16/3. Upper-triangle entries represent Qij in x^TQx, so an off-diagonal monomial has twice that coefficient. Consequently

\[
\begin{aligned}
\ell(C_3)
&=2(3/8)\left[(21/4)(4/3)+(21/4)(2/3)+(15/4)(16/3)\right]\\
&=183/8\ne0.
\end{aligned}
\]

There is **no second division by8**. These are actual one-form coefficients, not raw pairing numerators. Positive/negative energy, norm or spectrum is not being inferred from the sign of this coordinate.

The exact probe cross-checks the receiver against the actual native maps and accepted branch recurrence. The full ambient C3 is cheap to evaluate as well: it has34 nonzero components,25 horizontal, in the held frame; these support counts are diagnostics, not invariant physical dimensions. The coefficient is not inferred from decimal fitting or a finite-difference derivative.

## 4. Why this excludes an interval of actual stationary fields

The branch and fixed receiver are real analytic near h0. Full C1=C2=0 and the nonzero receiver C3 give

\[
f(h)=h^3\left(183/8+h r(h)\right)
\]

with r analytic near zero. Continuity gives some delta>0 within the existence interval such that |h r(h)|<183/16 for |h|<delta. Hence

\[
0<|h|<\delta\quad\Longrightarrow\quad
|f(h)|>\frac{183}{16}|h|^3>0.
\]

For positive h this includes all sufficiently large positive kappa. Delta is existential here; no numerical radius or threshold kappa is certified. h0 is the normalized limit kappa=infinity, not a finite-coupling background newly proved to solve both equations.

First form the ambient raised one-form R_print=*G^{-1}Upsilon, then contract its form slot along the constant-g0 section, retaining the full ambient adjoint fibre. The theta0 component survives. Pulling degree13 Upsilon directly to a4D section would vanish dimensionally and is a different map. This is literal observed nonvanishing, not a derived physical Einstein equation.

At any chosen nonzero h in the interval, every component of the owned coupled Euler tuple vanishes in its admitted local variational problem. A regular zero-preserving map of that tuple and its local jets must therefore vanish. It cannot equal this nonzero endpoint, ambient or literally observed. This reuses the previous recovery-class theorem with a new interval of witnesses; it does not independently refute every possible field redefinition or physical restriction.

## 5. Source relevance and choice dependence

The registered source is explicit about the path coefficients1/2 and1/3 in SC-ACT-01 (2021 draft p44eq9.4), and prints the unit-weight swervature/displasion equation in SC-ACT-02 (p45eq9.8–9.10). The shared template is source-asserted. The minus/conjugation adjoint sign is source-fixed (draft section3.5 eq3.27); plus is a comparator, not a coequal source convention. The selector comm/i-Jordan/i-Jordan, displayed-block K95 realization of the native pairing, and two-frame dictionary are the held repository reconstruction. Their unique source necessity remains unproved. SC-ACT-06's separate assertion about a deformation complex on Upsilon=0 is not an assertion about every stationary field of our constructed action.

Dependency scope: **fixed-build result**, with geometry-real-form, Shiab recipe and variational domain held. Persistence across other source-admissible choices is **UNDETERMINED**; this calculation exhibits no countervariation and does not earn a structural-across-all-choices label. The nonzero result does hold over a punctured large-kappa interval in the existing coupling family. Fermion, bar contour, spectral-window, observed-dispersion and lift choices do not enter this zero-matter bosonic calculation. No universal statement over all source-admissible variations is made.

The choice budget remains10 families /4 grouped mathematical obligation bundles / bookkeeping net6 /0 source-selected predictions. This subtraction is a monitoring convention, not a lower bound on source-required choices or a count of independent parameters. No new choice, positive viability bundle or prediction is credited.

No same-branch higher-order computation is needed to decide this implication. Other equation dictionaries, other stationary branches, different source real forms and genuine source-selected physical loci remain outside the tested claim; none is installed as a repair. The source labels the first coupling kappa_1; that subscript does not set it numerically to1. The repository's two backgrounds at kappa=1 and a path connecting either to this branch remain separate.

## Verification scope

The [probe](../../tests/program-focus/source_action_endpoint_cubic_probe.py), [certificate](../../lab/process/source-action-endpoint-cubic-certificates.json), [evidence](../../lab/process/source-action-endpoint-cubic.json) and [review](../../lab/process/hostile-reviews/2026-11-27-source-action-endpoint-cubic-review.md) record fresh checks separately from inherited results. Finite Lean cores do not formalize the whole native geometry, implicit-function theorem or coupled variational/source bridge. No external review, world-novelty claim, canon promotion or paper release is implied.

```sh
python3 tests/program-focus/source_action_endpoint_cubic_probe.py --verify
```
