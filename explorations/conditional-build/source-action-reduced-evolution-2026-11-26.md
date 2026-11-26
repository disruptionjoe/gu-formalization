---
title: Coupling-one constrained energy and the domain required for evolution
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Test actual reduced evolution and existing restrictions using completed spin6/7 constraints,
  without a new completion.
actual_delta: Both energy signs at both kappa1 roots conditional on full regular constraints; nonzero
  square-zero reduced second-order symbol excludes unrestricted equal-order Sobolev evolution. Compact
  Lie-valued local-module closure also fails. Physical quotient and propagated ghost remain undetermined.
class_covered: Held W2 K95 full-U real zero-matter candidate at both certified kappa1 roots; imaginary
  connection Hessian, closed non-null physical time. Regular full algebraic reduction with unrestricted
  reduced data; separate class of all lower terms sharing the native compact-module symbol.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-META-52
- lab/sources/source-claim-register.yaml#SC-META-53
- explorations/conditional-build/source-action-kappa1-constraints-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source motivates grammar and full U but selects neither this action nor unrestricted same-order
    Sobolev data, a compact connection truncation or a physical quotient.
kill_condition: Exclude the conjunction of full regular auxiliary constraints and unrestricted compact
  reduced-data canonical-energy positivity, or bounded equal-order Hs evolution with a compact-smooth
  core. Do not convert either domain exclusion into source falsification or propagated physical ghost.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-REGULAR-UNRESTRICTED-REDUCED-DOMAIN
internal_target_verdict: At both held roots, regular constraints cannot coexist with unrestricted compact-data
  canonical-energy positivity or bounded same-order reduced-Hs evolution.
canon_verdict_change: none
---

# Coupling-one constrained energy and the domain required for evolution

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Actual reduced evolution and existing restriction tests, without new choices.
actual_delta: Both canonical energy signs at both roots under full regular reduction; a square-zero nonzero second-order symbol and compact-module obstruction. Physical propagation remains open.
```

## Result in plain language

**Both coupling-one backgrounds have constrained canonical-energy directions of
both signs if the remaining auxiliary constraints are regular. Neither wins the
proposed stability comparison.** This is stronger than the previous large-coupling
result and stronger than a matrix-entry sign. It is still not a physical ghost:
the source-intended quotient and admissible propagation have not been supplied.

The same calculation identifies a required distinction in how initial data are
measured. If all remaining components are assigned the same unrestricted spatial
Sobolev regularity, bounded evolution is impossible. Different components may
need different derivative control, as they do for the ordinary wave equation.
This is a domain requirement, not evidence of runaway dynamics.

The reduction uses the already complete spin6/7 blocks. It does not certify the
remaining47250 auxiliary components. Instead it excludes a precise conjunction:
if those remaining constraints are singular, full regular reduction fails; if
regular, the energy and equal-order-domain obstructions follow. Neither branch
by itself excludes the candidate, GU or all admissible state spaces.

```gu-typed-objects
result: canonical constrained energy and reduced-domain exclusions at both coupling-one roots
carrier: TstarY tensor u64_64; imaginary-Clifford connection Hessian LAYER=ambient BRIDGE=physical_observation_unproved CHIRALITY=N/A
pairing: native -Re_trace_div128 with K95 one-form contraction ON=connection_forms
real_structure: full U64_64 real form; highest-weight complexification is returned to actual imaginary-U fields
grading: coefficient conjugation and geometric SO3 weights; not particle spin or physical chirality
action_owner: repository-construction fixed W2 I1B-style action with independent bars
target: reduced equation, constraint graph and canonical Hamiltonian MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING.** `INTERNAL_STRUCTURAL_ONLY`;
> [routing contract](../../lab/methods/source-native-comparator-routing.md).
> Keep K95/K77, full U/conditional Sp, source/candidate, contraction/projection,
> and geometric rotation/physical particle distinct. No physical quotient is
> inferred from Krein structure or constraint elimination.

## 1. Definitions and advance outcomes

Use the actual [coupled Hessian](source-action-coupled-ghost-2026-11-25.md) and
[completed auxiliary blocks](source-action-kappa1-constraints-2026-11-25.md).
In the autonomous imaginary connection sector at either real zero-matter root,

    H = K + C,    K = sum K^a nabla_a,    C = kappa I + 2 N(T0,.).

For exact non-null physical time dt, let A=K_dt, P project to its nondegenerate
kernel N, R=I-P, and G be A inverse on R, zero on N. This is a native indefinite
pairing decomposition, not a positive physical space. The accepted closed-time
moving-projector calculation gives

    P H inclusion_N = M_N = P C inclusion_N,
    P K_xi P = 0,
    P K_beta G K_alpha P + P K_alpha G K_beta P = 0.        (1)

The symbol is parallel for the compatible reference connection. Projector,
frame, density and lower terms are included; no frozen-connection replacement
is made. All59 held background coefficients preserve the geometric SO3 types.

Before evaluation, retain Joe's outcomes: negative constrained directions at
both roots, one only, or neither. A physical obstruction additionally requires
physical quotient status and actual admitted propagation. An incomplete
calculation is UNDETERMINED. The present result reaches **both roots only in the
explicit regular-reduction/unrestricted-data category below**. It does not
silently settle those added physical requirements.

## 2. Exact energy calculation that avoids all lower blocks

Use a time-translation-invariant frame on the stationary background, so partial_t preserves R and N; the spatial/lower blocks retain all remaining projector and frame terms. Write the field a=v+n, v in R, n in N. If full M_N is locally invertible, the
actual algebraic equation determines

    n = -M_N^-1 D v,    D=P H inclusion_R.

After integration by parts on compact support, the quadratic Lagrangian has the
form

    L = 1/2 b(v,A partial_t v) + 1/2 b(v,C_RR v)
        + b(n,Dv) + 1/2 b(n,M_N n),
    L_red = 1/2 b(v,A partial_t v) + 1/2 b(v,C_RR v)
            - 1/2 b(Dv,M_N^-1 Dv).

Here C_RR includes the first-order spatial block; b is the actual imaginary-U
pairing. Its canonical energy therefore has degree-two spatial term

    E_2(v) = 1/2 b(P K_xi v, M_N^-1 P K_xi v).             (2)

Spatial/lower range terms have at most one derivative and cannot change a
strict leading high-frequency sign. The physical imaginary pairing is minus
the raw real-Clifford Engine pairing. In native highest-weight coordinates,
H_raw is the auxiliary paired matrix, b_raw the derivative source and
c=-H_raw^-1 b_raw. Thus twice(2) is **b_raw* c**, not its negative.

Use horizontal xi=theta0 and v=K_dt b_j in geometric spin7. Its derivative
source has only spin6/7: spin1 tensor spin7 permits6,7,8, and this carrier has
no8. The entire spin6 and lowered spin7 constraint spaces are already complete.
The lowered-spin7 Gram factor is14. No omitted lower-spin inverse contributes
to this column whenever full reduction exists.

### Certified principal-form signs

The table omits the common positive factor1/2 and the positive oscillatory bump
average. Rounded values explain the magnitude; acceptance uses exact rational
intervals stored in the [machine evidence](../../lab/process/source-action-reduced-evolution.json).
Root A/B are the preceding certified roots0/1, not new stationary solutions.

| Root | Range amplitude | Center | Error upper bound | Sign |
|---|---|---:|---:|---|
| A | K_dt b5 | +1,484,675.20 | 6.04 | positive |
| A | K_dt b12 | -3,943,678.64 | 16.04 | negative |
| B | K_dt b12 | +7,155,700.56 | 55.86 | positive |
| B | K_dt b5 | -3,347,101.37 | 26.13 | negative |

For each block, the published rational inverse candidate R0 and exact root-ball
bound eta=||I-R0 H||<1 give, with c0=-R0 b,

    ||c-c0|| <= eta/(1-eta) ||c0||.

Multiply by the exact source row norm and sum the spin6/7 contributions.
Any rational candidate's imaginary Hermitian residual is included in the error.
Floating centers are not acceptance tests. The complex highest-weight form is
the sum of the real and imaginary coefficient energies; a strict sign therefore
supplies at least one actual real-coefficient field, multiplied by physical i.
No new pairing or complex physical field is installed.

### From a principal sign to constrained compact data

Assume full M_N regular near the point. Smoothness then gives a local inverse.
Extend the amplitude in R smoothly; use a compact spatial bump supported in a
small neighborhood and a real oscillation cos(k x0) or sin(k x0). Define n by
the **actual** differential constraint map, not by freezing its coefficients.
Cutoffs in all13 spatial/normal directions can source other N sectors at lower order; the assumed full local inverse solves those sources. They are not silently set to zero. For a complex amplitude V use the actual real field Re(exp(i k x0)V); the energy divided by k^2 tends to one quarter of the native-density integral of the Hermitian coefficient times the squared bump. The k^2 term in the integrated energy converges after normalization to the
strict-sign coefficient(2) times a positive bump average; coefficient variation
is made smaller than the sign margin by shrinking the support. Derivatives of
the bump and all lower terms give O(k) or O(1). Consequently both signs occur
for sufficiently large k on genuine compactly supported algebraically
constraint-satisfying data.

This uses a finite local integral with the existing native density. Compact
support is a test-data condition; it introduces no finite 4D reference weight,
normalization law, new background or physical state selection. Singular full
M_N instead requires residual-constraint analysis: the theorem makes no assertion
that these freely prescribed R data then extend through those extra constraints.

**RULED OUT:** full regular auxiliary reduction together with canonical-energy
positivity for all compactly supported reduced R data, at either root.
**UNDETERMINED:** a negative physical-cohomology mode, actual solution admission,
positive/negative-mode exchange, runaway or full coupled nonlinear instability.
A compact initial datum is not yet an admissible solution.

## 3. Exact reduced symbol and its separate domain obstruction

Where full M_N is regular, the actual reduced evolution is

    partial_t v = L v,
    L = -G H_RR + G H_RN M_N^-1 H_NR.

All bundle transport and lower coefficients remain. Its formal degree-two
spatial symbol and Fourier coefficient are

    D2(xi)=G K_xi P M_N^-1 P K_xi|R,    B(xi)=-D2(xi).

Equation(1) at alpha=beta=xi gives P K_xi G K_xi P=0. Hence

    D2(xi)^2=0,    B(xi)^2=0.                              (3)

No commutation of M_N with K is assumed. The four-factor sandwich identity is
checked in Lean; the native geometric premises remain written mathematics.

The actual v=K_dt b7, xi=theta0 source was solved through **both** completed
blocks. One receiver of K_xi n, exterior32/Clifford1725, is

| Root | Center | Exact error bounded above by |
|---|---:|---:|
| A | -1.67054027705 | 0.000154072 |
| B | +2.93442078734 | 0.000725787 |

K_xi n lies in R by P K_xi P=0. Since G is injective there, D2(xi)v is nonzero
at both roots. A nonzero observation response alone would not have established
this: the separate native K_xi application is necessary and was performed.

### The variable-coefficient theorem

Let L(t) be a smooth spatial differential operator of order at most2 on the
reduced bundle. Give **every R component the same H^s regularity**, for any
fixed real s. Require a locally bounded evolution family solving partial_t v=L(t)v
and satisfying Duhamel's identity for all compactly supported smooth interior
test sections. A strongly continuous autonomous semigroup extending L on such
a core is sufficient. If B(p,xi)^2=0 but B(p,xi)!=0, this category is impossible.

Proof: in a smooth local trivialization choose z with Bz!=0, xi!=0,
0<alpha<1, delta=k^-alpha, and a compact smooth bump chi. For fixed S>=0 use

    w_k(t,x)=k^-s delta^(-d/2) chi((x-p)/delta)
             exp(i k xi.(x-p)) exp(k^2(t-t0) B) z,
    0 <= t-t0 <= S/k^2.

The real problem may be complexified without losing boundedness. Since B²=0,
exp(uB)=I+uB. Fourier localization at frequency k xi, width k^alpha=o(k), gives

    ||w_k(t0+S/k^2)||Hs -> |xi|^s ||chi||2 ||(I+SB)z||,
    ||w_k(t0)||Hs -> |xi|^s ||chi||2 ||z||.

These estimates hold for negative/fractional s: the central Fourier region has
the stated limiting weight and smooth cutoff tails decay faster than any fixed
power. The integrated residual obeys

    integral ||(partial_t-L(t))w_k||Hs dt
      <= C_(S,s) (k^-alpha + k^(alpha-1) + k^(2alpha-2)
                  + k^-1 + k^-2) -> 0.

The terms respectively control leading-coefficient variation, cutoff derivatives,
lower terms and smooth time variation. Smooth coefficient derivatives add lower
powers. Duhamel and a single local operator bound M then imply
||(I+SB)z||<=M||z|| for every fixed S. But
||(I+SB)z||>=S||Bz||-||z|| is unbounded. Contradiction.

**Essential control:** q_t=p, p_t=Delta q has a nonzero square-zero degree-two
symbol too. It is not bounded on H^s(q) plus H^s(p), but is well posed on
H^(s+1)(q) plus H^s(p). Therefore our exclusion is a **regularity demand, not
instability**. The existing constraint graph norm ||v+n(v)||Hs already controls
some derivatives. A suitable graph or mixed norm might be derived from these
same equations; it would not automatically be a new free choice. Its actual
well-posedness and physical positivity here remain UNDETERMINED.

## 4. What is proved about observation and equation jets

Where full M_N is regular, the constraint lift J(v)=v-M_N^-1 P H v obeys exactly

    q J(fv)-f q J(v) = -q M_N^-1 P K_df v.                 (4)

The prior exact spin7 horizontal witness makes the right side nonzero at both
roots. An algebraic shielding prescription admitting all scalar localizations
of that amplitude cannot guarantee zero constrained literal readout. It must
restrict the amplitude/derivatives or provide compensating data. This rules out
a pointwise-module condition, not physical shielding or every compensating state.

The same witness extends to an equation **one-jet**: choose v(p)=0 with prescribed
spatial derivative xi tensor V; the complete spin6/7 solve fixes n(p). Compatible
spatial derivatives of n can be chosen. The remaining Euler residual lies in R,
so choose partial_t v(p)=-G H_sp(v+n)(p). The full first-order equation holds at
that point. Differentiated constraints involve second spatial jets and possible
lower rotation receivers. This is not a convergent solution, a propagation proof
or permission to use Cauchy–Kowalevski on a singular time symbol.

A numerical full-multiplicity scout suggests transfer rank14 at both rational
centers, but its smallest singular values fall below the available exact error
control. **Rank14 is not an established result or credited delta.** The exact
energy and symbol certificates above do not use that numerical rank.

## 5. Source-inspired compact truncation: a cheap whole-module test

The K95 normal metric has signature(6,4). The full adapted diagonal, with normal indices4..13, is
(1,1,1,-1,-16,8,24,48,8,8,-8,8,-8,-8). The displayed normal compact algebra is

    k=span{gamma_a gamma_b:4<=a<b<=13, d_a d_b>0},
    k = so(6) plus so(4), dimension21.

This is the compact algebra named in SC-META-53, not the maximal compact of full
U(64,64), and not a physical projector. Exact native columns give

| Input compact-valued one-form | Covector | Output receivers |
|---|---|---|
| theta0 gamma5 gamma6 | dt=theta3 | (exterior2,Clifford107):+2; (4,109):+2 |
| theta3 gamma5 gamma6 | theta0 | (2,107):-2; (4,109):-2 |
| theta4 gamma5 gamma6 | theta0 | (2,115):-1/8; (4,117):-1/8 |

All ten terms in each column are outside the compact bivector algebra; the shown
horizontal receivers survive literal section pullback. They are in the actual
full-U real form. Thus H Gamma(T*Y tensor k) subset Gamma(T*Y tensor k) fails
for **every smooth lower term sharing this symbol**: apply the Leibniz identity
to fv with f(p)=0 and prescribed df(p). Derivatives of a moving compact projection
cannot cancel the witness at f(p)=0.

Native Clifford/Hodge covariance transports this exclusion to every normal
Spin(6,4) conjugate of the displayed embedding; horizontal covectors are fixed.
This is principal covariance, not symmetry of every lower background coefficient
or an assertion about arbitrary full-U Cartan projections.

SC-META-53 is UNCERTAIN and does not demand that the entire connection be an
arbitrarily localized compact-valued module. Accordingly this excludes a naive
sufficient truncation, **not the source's proposed compact shielding**, restricted
solutions, effective decoupling or a quotient. SC-CHI-52 concerns a fermionic
curvature/VEV/mass mechanism; the bosonic spin7/6 map is not that mechanism.

## 6. Source, physical and choice accounting

| Question | State |
|---|---|
| Both signs of the exact native derivative-source canonical form | ESTABLISHED at both roots |
| Compact constrained data of both signs | ESTABLISHED conditional on full M_N regularity locally |
| Positive canonical energy for all such unrestricted data | RULED OUT in that regular category |
| Bounded equal-order reduced-Hs flow with compact-smooth core | RULED OUT in that regular category |
| Remaining47250 auxiliary components and singular residual constraints | UNDETERMINED |
| Physical Q, exact/nonclosed/physical cohomology of negative data | UNDETERMINED; not proved nonexistent |
| Actual admitted propagation, coupling to positive modes, runaway exchange | UNDETERMINED; vertices or equation jets are insufficient |
| Mixed/graph regularity derived from the existing equations | UNDETERMINED; not automatically an added choice |
| Quantum state ontology or observer-as-agent interpretation | NOT MODELED by this diagnostic |

SC-ACT-01/05 and SC-GEO-51 motivate ingredients, not this action's uniqueness.
SC-META-52 supplies no equal-order Sobolev rule; SC-META-53 supplies no physical
Q/domain. Source necessity is absent and class-C representativeness unproved.
LT-GR1, LT-SM8, all ledger/canon/paper verdicts remain unchanged. The real
metric/connection sector and the selected positive linear matter completion
are distinct from this imaginary connection calculation.

Choice inventory remains **10 grouped families /4 grouped compatibility bundles
/bookkeeping net6**, with0 new families,0 new successful full-viability bundles
and0 source-selected predictions. This subtraction is neither a lower bound on
GU-required choices nor an independence theorem or physical parameter count.
No background is selected, no finite reference weight or new completion is added.

## 7. Verification and next discriminator

The native probe reconstructs the necessary highest-weight basis/source columns,
uses the published exact root-ball certificates, and evaluates the independent
energy and K_xi-response intervals. It also checks compact-module columns and
finite countercontrols. Four Lean lemmas check the square-zero sandwich,
unbounded affine-ray core and universal-jet algebra; the PDE packet argument,
source typing and root matrices remain independently reviewed written work.
See the [review](../../lab/process/hostile-reviews/2026-11-26-source-action-reduced-evolution-review.md).

The next useful science compares the **existing constraint graph/mixed regularity**
with the actual reduced equations and checks whether any already specified
physical restriction excludes the negative data while remaining preserved.
A singular full-constraint branch instead needs its actual residual constraints.
Do not automatically invert every lower block or add a tuned positive completion.
The shared missing physical input remains the source-typed Q/domain/pairing;
ordinary eligible work and LC cadence continue independently.
