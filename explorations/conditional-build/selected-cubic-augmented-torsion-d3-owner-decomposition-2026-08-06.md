---
artifact_type: construction_result
created: 2026-08-06
status: INTRINSIC_AUGMENTED_TORSION_D3_CLOSED__Q0QM_ZERO__QMQM_NONZERO__FULL_MOVING_AND_PREBOUNDARY_OPEN
source_return: SOURCE-SILENT
ledger_rows: [LT-GR2b, LT-GR5, LT-SM8]
scripts:
  - tests/channel-swings/selected_cubic_augmented_torsion_d3_owner_probe.py
  - tests/channel-swings/selected_cubic_augmented_torsion_d3_owner_independent.sage
registry: lab/process/selected-cubic-augmented-torsion-d3-owner-decomposition.json
---

# Selected-cubic augmented-torsion D3 owner decomposition

## Result first

One previously unassembled part of the full-moving selected cubic is now
exact. For the selected non-cyclic K77 augmented-torsion action

\[
 I_T(T)=\frac13\langle T,\mathscr S(T\wedge T)\rangle
       +\frac{\kappa_1}{2}\langle T,*T\rangle,
\]

the complete fixed-geometry third derivative on the gravitational Gauss
carrier has two different irreducible coefficients:

\[
 \frac{D^3I_T[\Phi_1,e_{\rm tr},e_{\rm tr}]}
      {\langle e_{\rm tr},*e_{\rm tr}\rangle}=\frac{136}{3},
 \qquad
 \frac{D^3I_T[\Phi_1,e_{\rm TT},e_{\rm TT}]}
      {\langle e_{\rm TT},*e_{\rm TT}\rangle}=-\frac{56}{3}.
 \tag{1}
\]

Both values hold exactly on positive and negative normal directions, and the
TT value agrees on diagonal and off-diagonal representatives. Direct
trilinear differentiation, an eight-corner polarization of the scalar action,
the derivative of the previously certified Hessian coefficients, and an
independent Sage route all agree.

On the exact free-pencil modes

\[
 q_0=(h,0),\qquad q_m=(h,-\alpha_{II}v),
\]

the intrinsic `T`-only contribution is therefore

\[
 D^3I_T[\theta_{\rm rad},q_0,q_m]=0,
 \qquad
 D^3I_T[\theta_{\rm rad},q_m,q_m]
 =-\frac{56}{3}\alpha_{II}^2\langle v,*v\rangle .
 \tag{2}
\]

Here `theta_rad` means the conditional invariant radial perturbation
`delta T=delta t Phi1`. It is not silently identified with Weinstein's full
movable dark-energy field or an observed scalar.

Equation (2) moves the named full-moving gate without closing it. The mixed
`q0-qm` class cannot come from the intrinsic augmented-torsion cubic. Its
remaining possible owners are now the direct curvature/`|II|^2`/defect action
terms, metric-induced gauge-rotated Levi-Civita response, moving Hodge/Shiab/
DeWitt/Krein pairing, observation/soldering jets, and the unrestricted
preboundary class. The nonzero `qm-qm` summand can still cancel against those
owners after the physical quotient.

No Q1 pole, physical transition, dark-energy scalar identification, positive
Fock space or native-`Y14` quantum theory is claimed.

## Plain English

We have begun replacing “compute the entire moving cubic” with an actual
term-by-term answer.

The part of the action that depends only on GU's connection distortion cannot
make the mixed ordinary-graviton/new-partner process happen by itself. The
ordinary graviton has no independent distortion component, so that intrinsic
three-leg term is exactly zero. The same action does directly couple the
radial distortion to two massive partners, and its coefficient is fixed rather
than fitted.

This tells the next builder where not to look. The mixed interaction, if it
exists, has to be created when the ordinary metric perturbs the Levi-Civita
reference connection, the curvature/embedding terms, the moving contraction
and pairing, the observation map, or a boundary charge. Those are fewer and
more structured owners than the predecessor's undifferentiated list.

## 1. Layer 0

| phrase | object computed here | not identified with |
| --- | --- | --- |
| `theta_rad` | coefficient of `Phi1` in an invariant radial `T` perturbation | full olive/varpi field, observed Higgs, or derived dark-energy scalar |
| intrinsic `T` cubic | third derivative of `I_T` at fixed metric, epsilon, section and pairing | complete moving `Y14` source action |
| `q0=(h,0)` | exact massless mode in the independent metric/distortion free pencil | zero variation of the dependent Levi-Civita reference connection |
| `qm=(h,-alpha v)` | exact massive partner mode on one TT polarization | full massive multiplet or asymptotic particle |
| intrinsic zero | zero `T`-only summand in the mixed channel | zero full numerator or zero preboundary charge |
| intrinsic nonzero | nonzero algebraic summand in the massive channel | nonzero reduced Hamiltonian class |

Dispositions:

- scalar horn versus invariant `Phi1` radial line: `UNCERTAIN`;
- independent distortion zero versus dependent Levi-Civita response:
  `HOMONYM` if both are called “the T leg”;
- intrinsic cubic versus full moving numerator: `HOMONYM` if both are called
  “the selected cubic”; and
- density versus physical transition: `HOMONYM`.

The calculation is useful precisely because it retains these forks. The mixed
zero is representation/owner information even before the scalar
identification is settled.

## 2. Divergent preassessment

| lens | demand | result |
| --- | --- | --- |
| variational PDE | polarize the scalar action, not its old fixed Hessian label | exact D3 constructed |
| differential geometry | isolate intrinsic T variation from metric-induced connection variation | mixed owner split |
| representation theory | test trace and traceless Gauss irreps separately | `136/3` versus `-56/3` |
| Krein/operator theory | use exact `q0/qm` legs and native pairing | no Hilbert inference |
| symplectic geometry | require a reduced Hamiltonian/preboundary class | physical verdict withheld |
| source criticism | locate the numerator or return silence | `SOURCE-SILENT` |
| breadth archaeology | inspect the unmerged active-`(9,5)` mixed-jet work | useful method comparator, wrong real form for import |
| exact computation | demand a route independent of the written D3 formula | Sage corner polarization passes |

Preregistered result:
`INTRINSIC_MIXED_ZERO__MASSIVE_SUMMAND_NONZERO`.

## 3. Exact third derivative

Only the cubic term contributes to `D3`. For arbitrary directions `u,v,w`,

\[
\begin{aligned}
D^3I_T[u,v,w]=\frac13\{&
 \langle u,\mathscr S(vw+wv)\rangle
+\langle v,\mathscr S(uw+wu)\rangle\\
&+\langle w,\mathscr S(uv+vu)\rangle\}.
\end{aligned}
\tag{3}
\]

The executable proof constructs (3) in the complete sparse K77 Clifford/
exterior evaluator. It checks three normal directions and both diagonal and
off-diagonal TT representatives. It then reconstructs the same derivative as

\[
 \sum_{a,b,c\in\{0,1\}}(-1)^{3-a-b-c}
 I_T(au+bv+cw),
\tag{4}
\]

which guarantees that no quadratic `kappa_1` contribution or missing
symmetrization factor contaminated (1).

There is a second independent check. The selected Hessian at
`t_*=-kappa_1/312` was already certified as

\[
 H_{\rm tr}=\frac{100}{117}\kappa_1,
 \qquad H_{\rm TT}=\frac{124}{117}\kappa_1,
\]

while the quadratic mass term contributes `kappa_1`. Dividing the residual
linear-in-`t` part by `t_*` gives

\[
 \frac{(100/117-1)\kappa_1}{-\kappa_1/312}=\frac{136}{3},
 \quad
 \frac{(124/117-1)\kappa_1}{-\kappa_1/312}=-\frac{56}{3}.
\]

The coefficient does not consume `kappa_1`; the third derivative of the
quadratic term is zero.

## 4. Why the mixed intrinsic term is zero

At frozen metric and section, the `T`-only action sees only the independent
distortion coordinate. The exact massless free eigenvector has distortion
entry zero. Trilinearity then gives

\[
 D^3I_T[\Phi_1,0,-\alpha_{II}v]=0.
\]

This is stronger than saying a tested coefficient happened to vanish. It is an
owner theorem: any nonzero mixed answer must enter through a map that turns
the metric component of `q0` into a primitive action variation, through a
different direct action term, or through the boundary.

The repository already constructs the linear observed gauge-rotated
Levi-Civita derivative modulo connection gauge. That is a live candidate for
the missing metric-induced `T` response. But its full nonlinear chimeric
second jet and composition with the K77 action have not been assembled, so it
is not substituted here.

## 5. Pullback jet-order theorem

Let `F` be the observation/soldering lift and `I` the primitive action. At a
stationary background,

\[
\begin{aligned}
D^3(I\circ F)[u,v,w]={}&D^3I[DFu,DFv,DFw]\\
&+D^2I[D^2F(u,v),DFw]+\text{cyclic}.
\end{aligned}
\tag{5}
\]

The `DI[D3F]` term vanishes. A symbolic planted control restores it when a
nonzero tadpole is added. Thus, on the stationary flat branch used by the
free `q0/qm` modes, the compact-core bulk cubic needs at most the first and
second observation/soldering jets. It does not require an unspecified third
jet.

This reduction does not apply off shell or at the algebraic nonzero branch
until full stationarity is proved. It also does not remove the unrestricted
preboundary problem.

## 6. Remaining full-moving owner packets

The predecessor's broad list can now be reorganized into four packages:

1. **Direct non-T action:** curvature, full `|II|^2`, defects and any other
   primitive terms with one scalar and two TT variations. `LT-GR3` stays open
   because this wave does not compute them.
2. **Induced geometry:** first and second jets of the gauge-rotated
   Levi-Civita/soldering map, including the exact linear rank-ten owner already
   built and its nonlinear chimeric continuation.
3. **Moving contraction:** Hodge, selected Shiab, DeWitt/Krein pairing,
   density/coframe and observation jets through the order allowed by (5).
4. **Physical descent:** Ward/BV characteristic quotient, Green current,
   boundary generators and unrestricted preboundary class.

The co-moving epsilon compensator is not a free fifth packet: complete gauge
covariance must make it cancel into the Ward/characteristic owner. An isolated
connection compensator cannot be dropped before that identity is checked.

## 7. Source and real-form fence

The existing primary-source reinspection returns `SOURCE-SILENT` on the
numerator, full moving `h-v` response, Q1 and BFV prescription. It confirms
only the nearby moving connection/observation arena.

The separate `agent/null-clifford-omega1-repair` branch contains exact mixed
operator jets on a conditional active `(9,5)` port. That work is valuable as a
method and coverage comparator. It is not imported: the public/source-directed
K77 carrier has signature `(7,7)`, while the active branch itself records the
real-form port as absent. Complexification does not transport the real
pairing, right-H structure, soldering or physical domain.

## 8. Symplectic disposition

Equation (2) is a primitive bulk action summand. A physical transition
requires the induced covariant presymplectic current to descend to a nonzero
Hamiltonian class after quotienting the characteristic gauge kernel and exact
boundary generators. The intrinsic mixed zero does not exclude an
unrestricted boundary charge. Conversely, the nonzero massive summand may be
EOM-, Ward- or boundary-exact after all packages are assembled.

No fifth quotient is counted. The four previously ranked scoped quotients
remain the complete ledger claim.

## 9. Constraint surplus and datum accounting

```text
new fields: 0
new coefficients: 0
new selectors: 0
P1/P2/P3 consumed: 0
new real-form identification: 0
```

The calculation uses `alpha_II` only as the existing massive-mode coordinate
and reports the homogeneous `alpha_II^2` scaling. It does not select or fit it.

## 10. Ledger v0.20

```text
Ledger v0.20 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Exactly three distances migrate: `LT-GR2b`, `LT-GR5` and `LT-SM8`. Their
verdicts and reason kinds do not change. `LT-GR3` deliberately does not move,
because the direct curvature-squared third derivative remains uncomputed.

Next Build gate:

```text
ASSEMBLE_THE_REMAINING_MIXED_Q0QM_PACKAGES:
DIRECT_CURVATURE_II_DEFECT_D3
+ GAUGE_ROTATED_LC_SOLDERING_FIRST_AND_SECOND_JETS
+ MOVING_SHIAB_HODGE_PAIRING_OBSERVATION
+ WARDBV_PREBOUNDARY_REDUCTION
```

Then combine them with the exact intrinsic zero and evaluate the unique
reduced class on the mixed shell. In parallel, combine the nonzero intrinsic
`qm-qm` summand with the same packages before making a Q1 or positivity claim.

Curt remains formally separated inside the Eric lane; no third lane is
promoted. P1/P2/P3, canon, claim status and public posture do not move.
