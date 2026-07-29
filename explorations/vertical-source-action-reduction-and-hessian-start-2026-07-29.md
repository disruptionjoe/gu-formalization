---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "B / vertical source-action reduction"
run: lab/process/runs/GUH-20260729T211122Z-three-route-construction-wave/run-plan.md
title: "Vertical source-action reduction and Hessian start: the carrier is real, but the written X4 action does not yet retain it"
construction: "Conditional construction, not a vacuum claim: expand an ambient Y14 connection as A=A0+a_parallel+Phi_i eta^i, compute its full adapted-frame curvature, and state the exact reduction datum required to retain Phi as an X4 Lorentz scalar. The written X4 source action and the ambient Y14 Yang-Mills action are kept as a Layer-0 domain fork."
probe: tests/channel-swings/vertical_source_action_reduction_probe.py
verdict: "VERTICAL-CARRIER-EXISTS; X4-DYNAMICAL-RETENTION-MAP-UNBUILT; FORMAL-AMBIENT-HESSIAN-BUILT; PHYSICAL-HESSIAN-UNDERDETERMINED"
grade: "FORMULA-BUILT / EXACT-COMPARATOR. No nonzero background, vacuum, sign, mass, texture, hierarchy, or T10 claim."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Vertical source-action reduction and Hessian start

## Result first

The vertical--Krein weld found a real **algebraic** channel, but it did not yet
put that channel in the written four-dimensional action.

There are presently two source-action domains in the repo:

1. `canon/source-action-seiberg-witten-construction.md` writes
   `S_SW[A,Psi]` as an integral on `X^4`, with `A` an IG connection.
2. `canon/dark-energy-theta-divergence-free.md`, W131, and W177 use a
   Yang--Mills connection, operator, and curvature on `Y^14 = Met(X^4)`.

Only the second object has an independent vertical connection component
`Phi_i`. The first has a four-dimensional connection one-form unless a
reduction map is supplied. Literal section pullback does **not** turn a
vertical one-form into a scalar: it either kills it or folds it into the
components of a four-dimensional one-form.

This is not a reason to abandon the construction. It identifies the useful
conditional experiment:

> supply one typed reduction datum, derive the `Phi` kinetic term, potential,
> and Krein-paired fermion kernel from the ambient `T1+T2`, then test whether
> the retained sector is closed under the full Euler--Lagrange operator and
> whether its physical Hessian has a selected stable orbit.

The full curvature and Hessian-start formula are built below. What remains
unbuilt is now a named map rather than a vague demand for “dynamics.”

## Pre-registered verdict and kill conditions

The run plan expected
`VERTICAL-CARRIER-EXISTS-DYNAMICAL-HESSIAN-UNDERDETERMINED`. The Layer-0
action-domain check fires one gate earlier:

`VERTICAL-CARRIER-EXISTS; X4-DYNAMICAL-RETENTION-MAP-UNBUILT;
FORMAL-AMBIENT-HESSIAN-BUILT; PHYSICAL-HESSIAN-UNDERDETERMINED`.

Before executing the probe, the following outcomes were registered:

- deleting `-C_AB^C A_C` must fail a planted non-holonomic mixed-curvature
  cancellation;
- deleting the vertical derivative `-e_i A_mu` must fail a second planted
  mixed-curvature cancellation;
- a scalar subspace not preserved by the full Hessian is a non-closed
  truncation even if its restricted quadratic coefficient exists;
- a planted gauge-breaking mass must lift an exact gauge-null control; and
- none of those exact toy checks may be read as the GU Hessian, a vacuum, or a
  sign result.

## Layer 0: name the objects before reducing them

### The action-domain fork

| shared term | object on the ambient branch | object in the written SW branch | Layer-0 mark |
| --- | --- | --- | --- |
| `A` | `A_Y in Omega^1(Y,ad P)`, W131 gimmel spin-lift background plus allowed fluctuations | `A_X in Omega^1(X,ad P_X)` in the displayed `X^4` integral | **HOMONYM until a reduction map is given** |
| `F_A` | a two-form on `Y`; W177 builds the curvature of the W131 connection | a two-form on `X` | **HOMONYM related conditionally by pullback/mode reduction** |
| `Phi_i` | vertical coefficient of the tensorial fluctuation `a=A-A0` | no independently declared field in the displayed action | **ABSENT from the written X4 field list** |
| vertical fermion carrier | `c(e_i) rho(Phi_i)` in the ambient Dirac connection term; the action kernel is `K c(e_i) rho(Phi_i)` | requires a reduced zero-order operator to be written | **channel SAME, dynamical occurrence UNCERTAIN** |
| “Hessian” in W176 | metric/section Hessian in `delta g in s^*VY ~= Sym^2 T*X` | connection-field Hessian in `Phi in s^*V^*Y tensor ad P` | **HOMONYM** |
| C10 `theta` / `II_s` | connection distortion pulled along the graph; `II_s in Sym^2 T*X tensor N_s` in the canonical gauge | vertical connection fluctuation with one vertical coindex and an `ad P` value | **HOMONYM; no identification supplied** |

W177's `F_A` is the same curvature needed by an **ambient** `T1` only under
the declared identification `A0 = spin-lift(nabla^gimmel)`. It is not
automatically the curvature in the written `X^4` action. It must first be
pulled back or reduced. Likewise, the DeWitt metric can identify `VY` with
`V^*Y` pointwise, but it does not erase the `ad P` factor and therefore does
not identify `Phi` with W176's metric fluctuation.

The vertical index below is the actual rank-ten
`VY ~= Sym^2 T^*X` fibre, including diagonal metric entries. It is not the
different numerical ten `Lambda^2 direct-sum Lambda^3`.

### Why the fluctuation, not the raw connection coefficient, is used

A raw vertical connection coefficient transforms inhomogeneously under a
`Y`-dependent gauge transformation. With a background connection that
transforms at the same time,

```text
a := A - A0  in Omega^1(Y,ad P)
```

is tensorial. Thus the type-correct decomposition is

```text
A = A0 + a_parallel + phi,
phi = Phi_i eta^i in Gamma(V^*Y tensor ad P).
```

Calling a raw `A_i` an adjoint scalar without either this background split or
a restriction on vertical gauge transformations would be another Layer-0
equivocation.

## First construction: the exact curvature

Choose an adapted frame and coframe

```text
e_A = (e_mu,e_i),                  vartheta^A = (theta^mu,eta^i),
[e_A,e_B] = C_AB^C e_C,           d vartheta^C = -(1/2) C_AB^C
                                                   vartheta^A wedge vartheta^B.
```

Write `a_mu` for `a_parallel` and `a_i=Phi_i`, and define
`D0_A z = e_A(z)+[A0_A,z]`. Direct expansion of
`F_A=dA+A wedge A` gives

```text
F_AB = F0_AB
     + D0_A a_B - D0_B a_A
     + [a_A,a_B]
     - C_AB^C a_C.                                      (1)
```

The three blocks are therefore

```text
F_mu nu = F0_mu nu
        + D0_mu a_nu - D0_nu a_mu + [a_mu,a_nu]
        - C_mu nu^lambda a_lambda - C_mu nu^k Phi_k,

F_mu i  = F0_mu i
        + D0_mu Phi_i - D0_i a_mu + [a_mu,Phi_i]
        - C_mu i^nu a_nu - C_mu i^j Phi_j,

F_i j   = F0_i j
        + D0_i Phi_j - D0_j Phi_i + [Phi_i,Phi_j]
        - C_i j^mu a_mu - C_i j^k Phi_k.                 (2)
```

Equivalently, if `B=A0+a_parallel`,

```text
F_A = F_B + D_B phi + phi wedge phi,                     (3)
```

but (3) is safe only if `D_B phi` retains `d eta^i`, vertical derivatives,
and the horizontal-distribution curvature. A “zero mode” does not by itself
justify dropping the `C` terms. Even with `a_parallel=0`, `Phi` can enter
`F_mu nu` through `-C_mu nu^k Phi_k`, so the scalar ansatz can source a
discarded horizontal field.

In an orthogonal adapted frame, up to the convention used for the overall
two-form normalization, ambient `T1` splits as

```text
L_T1 = alpha (
          (1/2) <F_mu nu,F^mu nu>
        +       <F_mu i,F^mu i>
        + (1/2) <F_i j,F^i j> ).
```

This formally contains a mixed kinetic block and a vertical potential block.
Because the gimmel and Krein structures are indefinite, the angle brackets
must not be silently read as a positive norm.

The ambient `T2` contribution is also explicit. The vertical zero-order
operator and the matrix appearing in the bilinear are, respectively,

```text
m_Phi = Pi_RS (sum_i c(e_i) rho(Phi_i)) Pi_RS,
K m_Phi.
```

The vertical--Krein weld establishes the relevant four-dimensional
Lorentz-scalar, nonzero, cross-chirality channel for `K m_Phi`. It does not
establish a retained mode, a background value, or a stationary orbit.

## Pullback is not scalar retention

Let `s:X->Y` be a section and write

```text
v_mu^i := eta^i(ds(partial_mu)).
```

Then literal differential-form pullback gives

```text
s^*phi = Phi_i(s(x)) v_mu^i dx^mu.                       (4)
```

- If `s` is horizontal, `v_mu^i=0` and the vertical form is annihilated.
- If it is not horizontal, (4) is an `ad P`-valued **one-form on X**, not a
  Lorentz scalar.

Retaining a scalar multiplet instead uses a different map:

```text
res_s^V(phi) = (Phi_i o s) eta^i|_V
             in Gamma(s^*V^*Y tensor ad P).              (5)
```

Equation (5) restricts coefficients and their vertical bundle index; it is
not `s^*phi` as a differential form. The written `X^4` source action does not
yet declare (5), its kinetic operator, or its gauge law.

The strongest constructive route is a genuine mode reduction. Supply

```text
R = (s, H, A0, H_mode, P0, nu, D_boundary, h),
```

where `H` is the horizontal split, `H_mode` and `P0` select retained vertical
modes, `nu` and `D_boundary` give a fibre measure/domain/boundary condition,
and `h` is the allowed observer-compatible gauge subalgebra. With

```text
Phi_i(x,y) = sum_n phi_i^(n)(x) chi_n(y),
Psi(x,y)   = sum_r psi_r(x) xi_r(y),
```

the reduced mass matrix is conditionally

```text
(M_Phi)_rs(x)
  = integral_fibre <xi_r,
      K c(e_i) rho(Phi_i(x,y)) xi_s> d nu.
```

This is how an ambient connection component can survive as a
four-dimensional scalar and zero-order fermion operator. On GU's noncompact
metric fibre, the measure, normalizable modes, domain, and boundary behavior
are not owned by the repo's current analytic layer. A constant “zero mode”
may be non-normalizable, so it cannot be inserted by analogy.

## Hessian start, with the gauge qualification

For the ambient Yang--Mills branch, hold the metric fixed and set
`A(t)=A0+t a`. Then

```text
F(A(t)) = F0 + t D0 a + t^2 a wedge a
```

and

```text
d^2/dt^2 [ alpha integral <F(A(t)),F(A(t))> ] at t=0
 = 2 alpha integral (
       <D0 a,D0 a> + 2 <F0,a wedge a> ).                 (6)
```

Equation (6) is a real formal Hessian start. For a pure vertical fluctuation,
`D0 a` must still be evaluated with all three blocks in (2).

It is not yet a **physical** Hessian:

- W177 supplies a nonzero, source-owned `F0`, but does not establish that its
  background solves the Yang--Mills Euler--Lagrange equation
  `D0^*F0=0`.
- Gauge-orbit directions are guaranteed null directions of the ordinary
  Hessian only at a stationary background. Off shell, gauge invariance
  cancels the Hessian against the gradient contracted with the second-order
  curvature of the gauge orbit.
- A physical spectrum additionally requires a gauge choice or quotient, the
  analytic domain, the reduction inner product, and closure of the retained
  mode space.

Most importantly, computing only
`P0 Hess P0` is insufficient. A consistent truncation requires the full
Euler--Lagrange operator to preserve the retained space, equivalently that
the off-diagonal leakage `(1-P0) Hess P0` vanish at quadratic order and that
the nonlinear equations have no discarded component. The exact probe plants
a scalar line for which the restricted coefficient exists while this leakage
is nonzero.

## What is owned, and what is not

| item | status |
| --- | --- |
| rank-ten vertical connection carrier on ambient `Y14` | **owned at algebraic/type level** |
| nonzero cross-chirality Krein bilinear `K c(e_i)` | **owned at channel level** |
| covariant operator and projector on curved `Y14` | **owned at frame/symbol level by W131** |
| nonzero curvature of the W131 background | **owned at one curved point by W177** |
| exact full curvature expansion (1)--(3) | **built here** |
| formal ambient Yang--Mills Hessian (6) | **built here** |
| independent `Phi` in the displayed `X^4` action | **not written** |
| action-domain identification `S_Y -> S_X` | **unbuilt** |
| finite, gauge-covariant mode/pushforward datum `R` | **unbuilt** |
| stationary source-owned background | **unbuilt** |
| closed scalar truncation and physical gauge quotient | **untested** |
| sign, stable nonzero orbit, unbroken subgroup, mass texture | **untested** |

No `T10` is required merely for the algebraic carrier. Conversely, nothing
here makes a `T10`-like dynamical term unnecessary if the reduction fails.

## Constraint surplus: count it without pretending it is finite

Pre-consequence bookkeeping:

- **new numerical fit parameters introduced here:** `0`;
- **existing action coefficient carried:** `alpha` (one existing
  normalization/scale, not newly fitted here);
- **fields, not parameters:** `a_parallel` and `Phi`;
- **new structural/functional choice classes required for an X4 theory:** at
  least `6` -- split/section, background and gauge-covariant fluctuation,
  mode projector, fibre measure/domain/normalization, allowed gauge
  subalgebra, and stationary orbit/gauge quotient;
- **named constraints:** `7` -- type/gauge covariance, reproduction of the
  written action, finite normalization, full-EL truncation closure, survival
  of the Krein fermion channel, stationary-background/gauge-null behavior,
  and an admissible physical Hessian.

The constraint surplus is **UNCOMPUTED**, not `7-6=1`: several choices are
infinite-dimensional and the independence/rank of the seven constraints has
not been calculated. The appropriate response to the overdetermined-looking
interior is to write `R` and calculate its residuals, not to dismiss the fit
as content-free and not to advertise a surplus before a planted matcher
passes.

## Seven-axis register

This is a construction inside the smooth-bundle program, not a claimed
no-go escape. Layer 0 is the separate semantic precondition adjudicated in
the action-domain section above; its cell in the required one-line acceptance
summary only reports that adjudication and is not an eighth axis.

| candidate | L0 | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 loop | L7 positivity | first falsification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| conditional vertical reduction | action-domain **HOMONYM** named; retention map open | smooth principal bundle on `Y14` | extended class: graph-section plus fibre-mode projector | smooth gauge pairing; fermions Krein-paired | `X4` Lorentzian shadow; ambient `(9,5)` is multi-time and not silently identified with it | specific-object/mode truncation, not an RG claim | no closed observer loop claimed; full-EL closure is the test | indefinite gimmel/Krein; no positive-state-space claim | compute `(1-P0)E_A(P0 fields)`; any nonzero discarded component kills that truncation |

### L1--L7 detail required by the ratified protocol

| axis | class label and concrete specification | literature / repository anchor | class-assumption signature |
| --- | --- | --- | --- |
| **L1 substrate** | **(a) Smooth principal bundle on a smooth manifold.** The ambient object is `P -> Y14=Met(X4)` with connection `A_Y`; the candidate reduction is a map of its connection/associated bundles to fields over `X4`. | Kobayashi--Nomizu, *Foundations of Differential Geometry*, vol. I; `explorations/W131-covariant-operator-y14-2026-07-14.md`; `explorations/W177-build-connection-curvature-c2-2026-07-14.md`. | **Preserves** the smooth-manifold and smooth-principal-bundle premises seen by Witten-class and Distler--Garibaldi-class results. No substrate scope exit is claimed. |
| **L2 observer** | **Menu extension: geometric section plus fibre-mode projector.** The extension is necessary because the extracting object is the smooth map `s:X->Y` together with `P0` on vertical modes, not a computational-oracle or consensus observer from the existing menu. | Standard Gauss/normal-bundle reduction; `explorations/wave5/H21-theta-equals-II-2026-07-11.md`; `explorations/W176-build-reduction-x4-effective-2026-07-14.md`. | **Breaks no no-go assumption by itself.** It must carry, rather than silently alter, the relevant bundle/operator invariant; failure of that functorial map kills the candidate instead of evading a theorem. |
| **L3 pairing** | **(a) Cartesian/smooth gauge pairing.** Bosons pair through the gimmel metric and an invariant `ad P` form; fermions couple through the smooth connection and the already-built Krein kernel `K c(e_i)rho(Phi_i)`. The signature is kept for L7 rather than hidden here. | Kobayashi--Nomizu for associated-bundle connections; `explorations/sa-y8-majorana-layer0-and-vertical-krein-weld-2026-07-29.md`; W131. | **Preserves** locality and smooth gauge covariance. It does not break the representation-theoretic chirality assumptions of Distler--Garibaldi or the index assumptions of Witten/Freed--Hopkins. |
| **L4 causal order** | **Menu extension: ambient multi-time pseudo-Riemannian `(9,5)` with a `(3,1)` Lorentzian section shadow.** The extension is required because the menu's total-order Lorentzian class has one time direction, whereas `Y14` has five negative directions and no global causal order is supplied. | O'Neill, *Semi-Riemannian Geometry*; W131's computed `(9,5)=(3,1)+(6,4)` tangent signature and pointwise cone. | The ambient object is **outside the single-time Lorentzian causal class**, but the proposed observable shadow returns to it. This is a named scope difference, not an asserted evasion of algebraic chirality or anomaly results. |
| **L5 emergence** | **(a) Specific-object substrate.** `R=(s,H,A0,H_mode,P0,nu,D_boundary,h)` selects a concrete truncation and its exact coefficients; no universality, fixed-point, or attractor claim is used. | Appelquist--Chodos--Freund, *Modern Kaluza--Klein Theories*; W176. | **Preserves** the specific-object premise of the no-go comparisons. No RG/emergence escape is claimed. |
| **L6 coordination loop** | **(a) No loop.** The full Euler--Lagrange closure test checks whether the observer-selected modes form a consistent sector; it is not feedback from an observer into the substrate dynamics. | Henneaux--Teitelboim, *Quantization of Gauge Systems*; `canon/source-action-seiberg-witten-construction.md`. | **Preserves** the no-loop baseline. A nonzero `(1-P0)E_A(P0 fields)` refutes this truncation; it is not reinterpreted as adaptive selection. |
| **L7 positivity** | **(b) Indefinite Krein/gimmel signature, activation open.** The fermion kernel uses `K`, while the ambient metric has `(9,5)` and the vertical field metric `(6,4)`; no positive Hilbert completion, ghost-parity superselection, or probability rule is supplied here. | Bender--Mannheim, PRL **100** (2008) 110402; `lab/specifications/six-axis/six-axis-template.md`; W131 and the vertical--Krein weld. | **Drops** the positive-definite state-space premise relevant to ordinary unitarity/ghost objections, conditionally on a still-unbuilt physical-state rule. It does **not** evade Distler--Garibaldi's representation theorem or turn the grading-determined zero index into a chiral count. |

Thus no no-go assumption is advertised as evaded. The candidate earns
admission only conditionally, with its load-bearing homonym and map visible.

## Kill / fallback tree

1. **Literal pullback only.** If this is the intended reduction, independent
   `Phi` is erased or becomes part of `A_mu^s`.
   **Kill:** the four-dimensional scalar route through that map.
   **Fallback:** coefficient restriction or a genuine mode projection; the
   ambient channel survives.
2. **No finite gauge-covariant mode datum.**
   **Kill:** a local X4 scalar action from ambient `T1+T2`.
   **Fallback:** keep the claim and dynamics fourteen-dimensional and stop
   making X4 VEV statements.
3. **Full equations leak out of the retained modes.**
   **Kill:** the proposed scalar truncation even if its restricted potential
   looks good.
   **Fallback:** enlarge the retained multiplet or report that no
   observer-compatible closed branch exists.
4. **The W177 background is not stationary.**
   **Kill:** interpreting its quadratic form as a physical mass Hessian.
   **Fallback:** solve the ambient Euler--Lagrange equation or find a
   source-owned stationary background first.
5. **Stationary, quotient Hessian has no stable selected nonzero orbit.**
   **Kill:** tree-level dynamical selection from `T1`.
   **Fallback:** a supplied branch datum remains conditional; loop selection
   may be asked only after the propagator/regulator exists.
6. **A bounded stationary orbit with closed modes survives all controls.**
   **Advance:** compute its stabilizer, the `K m_Phi` spectrum, and only then
   ask magnitude and texture. This is still not a vacuum claim until the
   global/domain analysis lands.

## Smallest next source-owned dynamical computation

Use the explicit W177 gimmel spin-lift connection on a local patch, not an
invented negative-curvature potential:

1. compute the Yang--Mills residual `D_A0^*F_A0`;
2. only if it vanishes (or after solving to a nearby stationary connection),
   evaluate (6) on a complete observer-compatible set of vertical
   `ad P` directions, retaining every non-holonomic term in (2);
3. compute the off-diagonal closure block between vertical retained modes and
   discarded/horizontal modes; and
4. quotient or gauge-fix before reading eigenvalues, verifying the expected
   gauge nulls as a control.

That calculation is smaller and more informative than proposing a potential:
it decides whether the source-owned curvature actually generates a closed
vertical dynamical sector. A pass would justify building the external
reduction datum `R`; a fail would locate the exact missing source action term
without erasing the already-computed carrier.

## Reproducibility and scope

Run:

```text
python tests/channel-swings/vertical_source_action_reduction_probe.py
```

The probe uses exact rational arithmetic and contains planted controls for an
omitted non-holonomic term, an omitted mixed vertical derivative, a nonclosed
scalar truncation, and a lifted gauge-null direction. It tests the comparator,
not GU's unbuilt reduction or Hessian.
