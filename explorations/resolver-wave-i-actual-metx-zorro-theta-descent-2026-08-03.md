---
artifact_type: exploration
created: 2026-08-03
title: "A nonlinear Met(X) cocycle carries a Theta reconstruction and a Riesz-ported source-projector family locally"
grade: "Exact local three-chart rational reconstruction with nonzero Hessians. The metric-fibre map, full 14-dimensional first jet, observer Levi-Civita transformation, connection-induced chimeric coindex candidate, trace-reversed chosen-(9,5) gimmel metric, pointwise adapted SO/Spin frames, chosen J, raw-C* dual transport, explicit sharp/flat Riesz port, prior distortion tensor fixture, and associated rank-252 projector family pass their declared pairwise/triple tests. This is not a source-owned global Theta_Z theorem, arbitrary-X existence result, actual tilted two-connection assembly on the overlaps, source-action variation, Euler/Ward/Green/domain result, or physical no-leakage theorem."
named_gate: RESOLVER-WAVE-I-ACTUAL-METX-ZORRO-THETA-DESCENT
gate_before: LOCAL_CHOSEN_J_MOVING_REDUCTION_AND_COMBINED_PORT_FIXTURE
gate_after: LOCAL_NONLINEAR_METX_THETA_RECONSTRUCTION_AND_RIESZ_PORTED_SPIN_FIXTURE
route_disposition: CONTINUE
source_collision: SOURCE-CONFIRMS-GEOMETRIC-ROLES-SOURCE-SILENT-ON-EXPLICIT-THETA-FORMULA
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
third_lane_promoted: false
---

# Resolver Wave I: nonlinear `Met(X)`/Zorro/source-port descent

## Result first

Wave I closes the fixed-coindex limitation of Wave H on an exact local
three-chart fixture. It constructs a concrete connection-dependent candidate
for the missing Zorro/coindex map. On one arbitrary tautological fibre metric,
the adapted frame, coherent Spin lift, chosen quaternionic structure, raw
source covector, and explicitly Riesz-ported associated projector family obey
compatible pointwise overlap laws.

It does not prove that this candidate is Eric Weinstein's intended global
`Theta_Z`, nor that it exists with all required structures on every
four-manifold. The primary sources specify the role and ingredients but do
not give this formula or its overlap proof.

Use source order

\[
 C=V_{10}\oplus H_4^*,
 \qquad
 \Theta_{\Gamma,h}(v,\dot h)=(\kappa,\alpha),
\]

where

\[
 \kappa=\dot h-\Gamma(v)^Th-h\Gamma(v),
 \qquad
 \alpha=h(v,\cdot).
\]

The executable swaps the two blocks to `(alpha,kappa)` only to match the
predecessor Clifford basis order `H* plus V`. The swap is explicit; it is not
an identification of the summands.

The gate moves

```text
LOCAL_CHOSEN_J_MOVING_REDUCTION_AND_COMBINED_PORT_FIXTURE
  -> LOCAL_NONLINEAR_METX_THETA_RECONSTRUCTION_AND_RIESZ_PORTED_SPIN_FIXTURE
```

with route decision `CONTINUE`.

## Layer 0: the objects are different

| object | type | Wave I status |
|---|---|---|
| `X` | local smooth four-dimensional base | three explicit charts only |
| `Y=Met(X)` | Lorentz-signature component of the bundle of nondegenerate symmetric forms | local three-chart fixture |
| `g_obs` | observer metric used to construct `Gamma` | fixed flat metric in chart zero, nonconstant in the other charts |
| `h` | arbitrary tautological fibre metric at a point of `Y` | varied independently of `g_obs` |
| `Gamma` | Levi-Civita connection of `g_obs` | constructed and checked under nonlinear changes |
| `A0` | Levi-Civita-derived distinguished connection in the tilted source construction | which observer/Zorro/Y connection is meant remains `UNCERTAIN` |
| `Theta_{Gamma,h}` | explicit connection-dependent coindex reconstruction candidate | locally constructed and invertible; source ownership/global identity open |
| `T_omega` | difference of two connections | tensorially transported; it is not a connection |
| `J` | Wave H's chosen local right-quaternionic reduction field on the chosen `(9,5)` branch | actual `J_H` and `K` preserved by the selected native Spin cocycle; ownership source-silent |
| raw source first leg | `C*` covector | transforms by `O^-T`, not `O` |
| raised projector first leg | Riesz-raised `C` vector | related by explicit local `sharp_eta/flat_eta` |
| `Psrc_raw` | `flat_eta Psrc_raised sharp_eta` | associated family constructed and tested on all 252 image basis vectors plus representative kernel sectors |
| imposter `128` | spin-1/2 hinge representation | untouched and untested here; no count inference |
| P1/P2/P3 | external datum ledger | unchanged and unused |

Any argument from this local fixture to a global field, a physical current,
an Euler equation, or a generation count must clear Layer 0 separately.

## 1. A genuinely nonlinear three-chart atlas

The exact rational coordinate changes are

\[
\begin{aligned}
 y^0&=2x^0,& y^1&=x^1+\tfrac13(x^0)^2,&
 y^2&=x^2,&y^3&=x^3,\\
 z^0&=y^0,& z^1&=y^1,&
 z^2&=3y^2+\tfrac15(y^1)^2,&z^3&=y^3.
\end{aligned}
\]

Both transitions have nonzero Hessian. Their direct and sequential maps,
inverses, and Jacobians agree exactly on the triple overlap. With

\[
 A_{ij}=\frac{\partial x_j}{\partial x_i},
 \qquad
 B_{ij}=A_{ij}^{-1},
\]

in the executable's old-to-new convention, the tautological metric obeys

\[
 h_j=B_{ij}^{T}h_iB_{ij}.
\]

The oriented base determinants are `2`, `3`, and `6`.

The full total-space map is not the base map alone. Its vertical linear block
is `Sym2(B)`, and in four dimensions

\[
 \det\operatorname{Sym}^2(B)=(\det B)^5.
\]

Consequently the forward fourteen-dimensional Jacobian has

\[
 \det D\widehat f
 =\det A\,(\det B)^5
 = (\det B)^4
 =\frac1{1296}
\]

for the composite. The commonly tempting fifth and sixth powers are planted
and rejected. The full first jets satisfy the exact chain rule

\[
 D\widehat f_{02}
 =\bigl(D\widehat f_{12}\circ\widehat f_{01}\bigr)
  D\widehat f_{01}.
\]

## 2. The connection is exactly what makes the vertical piece tensorial

Start with the flat observer metric `g_obs,0=diag(1,1,1,-1)` and zero
Christoffels in chart zero. The transformed metric is

\[
 g_j=B_{0j}^{T}g_0B_{0j}.
\]

The connection transformation is evaluated independently from the
Levi-Civita formula and from

\[
 \Gamma_{j,\alpha}
 =A\Bigl(\sum_k B^k{}_{\alpha}\Gamma_{i,k}\Bigr)B
   +A\,\partial_{x_j^\alpha}B.
\]

The two exact routes agree on both pairwise and triple overlaps. The
Christoffels are nonzero because the transitions are nonlinear.

For a total-space tangent, raw `dot h` contains the derivative-of-`B` terms
and is not tensorial. In two independent rational Lorentz-fibre fixtures,
the connection correction cancels them exactly:

\[
 \kappa_j=B^T\kappa_iB,
 \qquad
 \alpha_j=B^T\alpha_i.
\]

Freezing `Gamma=0` in the nonlinear charts fails as a planted control. This
is the information-producing content of the Zorro candidate: the connection
is not decorative bookkeeping.

## 3. Trace reversal gives the chosen Wave-H real-form branch

On a Lorentz fibre metric `h`, the vertical form is

\[
 G_V(k,l)
 =\operatorname{tr}(h^{-1}kh^{-1}l)
 -\frac12\operatorname{tr}(h^{-1}k)
              \operatorname{tr}(h^{-1}l).
\]

An exact pseudo-orthonormal basis shows

```text
raw Frobenius on Sym2:       (7,3)
trace-reversed vertical:     (6,4)
Lorentz horizontal H*:       (3,1)
chosen Wave-H total C:       (9,5)
```

Thus the raw comparator would give `(10,4)`, not the chosen Wave-H `(9,5)`
carrier. The live rival/public `(7,7)` presentation remains a named,
under-determined real-form fork; Wave I neither tests nor kills it and does
not silently identify it with the trace-reversed carrier.

Let `T_Theta` be the matrix of the swapped coindex map `(alpha,kappa)`. The
coordinate gimmel metric

\[
 G_Y=T_\Theta^T\bigl(h^{-1}\oplus G_V\bigr)T_\Theta
\]

satisfies

\[
 D\widehat f^T G_{Y,j}D\widehat f=G_{Y,i}
\]

in both independent fixtures. Its determinant obeys the induced density law

\[
 \det G_{Y,j}\,(\det D\widehat f)^2=\det G_{Y,i}.
\]

This is a finite local naturality certificate, not an analytic density/Krein
domain or a Green identity.

## 4. A pointwise overlap witness reaches Spin rather than stopping at SO

The coindex transitions are

\[
 L_{ij}=B_{ij}^T\oplus\operatorname{Sym}^2(B_{ij}),
 \qquad L_{02}=L_{12}L_{01}.
\]

At one rational triple-overlap point and an arbitrary fibre metric distinct
from the observer metric, choose exact rational, noncommuting Spin rotors

\[
 r_1=\frac54+\frac34e_{03},
 \qquad
 r_2=\frac35+\frac45e_{01}.
\]

Using local gauges `s0=1`, `s1=r1`, and `s2=r2r1`, define adapted frames

\[
 F_i=L_{0i}F_0O(s_i).
\]

Each is exactly pseudo-orthonormal for the local chimeric metric. The
residual frame transitions

\[
 R_{ij}=O(s_j)^{-1}O(s_i)
\]

intertwine the coordinate transitions and satisfy the triple cocycle. Their
chosen Spin lifts

\[
 \widetilde R_{ij}=s_j^{-1}s_i
\]

obey

\[
 \widetilde R_{12}\widetilde R_{01}=\widetilde R_{02}.
\]

The mixed-sign rotor is a rational Lorentz boost and makes `O != O^-T`; it is
therefore also the control that exposes the raw covector/raised-vector type
boundary. Flipping the sign of one pairwise lift leaves every SO/adjoint
calculation unchanged but changes the Spin triple product to `-1`. This is a
planted inconsistent lift on a contractible fixture, not a nonzero global
`w2` class. It prevents an adjoint-only test from silently proving spin
descent.

The construction is local on a contractible triple overlap. It does not prove
the vanishing of the global spin obstruction.

## 5. The raw source covector reaches the associated projector through Riesz

Wave H's projector includes:

1. the explicitly typed public-`u(K)` to chosen right-`H` fixed-locus map;
2. the exact grade-six `q6` polynomial;
3. the rank-252 exterior projector; and
4. Chevalley reinclusion into the one-form carrier.

Wave H's `OneForm` projector is natural on a **Riesz-raised** first leg. A raw
source one-form instead has first leg in `C*`. For a Spin transition `s`, the
two laws are

\[
 U_s^{\rm raised}: O(s),
 \qquad
 U_s^{\rm raw}:O(s)^{-T}.
\]

The chosen `(9,5)` metric supplies explicit local musical maps satisfying

\[
 \sharp_\eta O^{-T}=O\sharp_\eta.
\]

Define

\[
 P_{\rm raw}=\flat_\eta P_{\rm raised}\sharp_\eta.
\]

The imported previously constructed distortion **tensor fixture** remains a
raw covector and is raised only when it enters the projector. It transports
directly and sequentially. This is not a new assembly of both tilted
connections on every chart. The three associated local raw projectors are
nonzero, idempotent on the tested fixture, and obey

\[
 P_{{\rm raw},j}U^{\rm raw}_{ij}
 =U^{\rm raw}_{ij}P_{{\rm raw},i}.
\]

The executable checks every one of the 252 selected image basis vectors and
representative grade-3, grade-10, public-complement, and grade-6 kernel
sectors. The family is associated by conjugation; this is a conditional
projector-family construction, not an independently source-derived subbundle
theorem. Using `O` on the raw first leg fails as a planted control.

Because these selected native Spin gauges are real, the chosen fixed-frame
`rho_J` commutes with their conjugation. An independent 128-by-128 check also
preserves Wave H's actual `J_H` and Krein `K`. This is chosen-`J` native-Spin
naturality; it is not source ownership or invariance under the entire public
`U(K)` family.

The central sign plant is decisive: the adjoint source and projector cannot
see `s -> -s`, while the Spin cocycle can. The spinor lift must therefore
remain an explicit gate.

## 6. Primary-source collision

The bounded source pass returns:

- `SOURCE-CONFIRMS`: Portal `01:12:17` types the chimeric bundle as vertical
  ten plus horizontal cotangent four;
- `SOURCE-CONFIRMS`: Portal `01:13:00` says the `C <-> TY` identification is
  missing exactly the data of a connection;
- `SOURCE-CONFIRMS`: Portal `02:22:27-02:23:52` gives the Mark of Zorro role;
- `SOURCE-CONFIRMS`: Portal `02:25:46-02:33:13` gives the tilted/two-connection
  construction;
- `SOURCE-CONFIRMS`: the 2025 conversation at `00:20:51-00:29:16`
  explicitly restores trace reversal after the raw `(7,3)` fibre result; the
  coefficient `1/2` used in the reconstruction is standard/repo-owned, not
  quoted from that passage;
- `SOURCE-CORRECTS`: the 2025 Curt-Eric conversation at `01:36:35-01:36:56`
  corrects “projection operator” to “contraction operator”; and
- `SOURCE-SILENT`: neither transcript supplies the explicit
  `Theta_{Gamma,h}` formula, nonlinear overlap proof, Spin cocycle, or
  rank-252 port descent constructed here.

The source correction is respected: `Theta_{Gamma,h}` is an isomorphism or
coindex reconstruction candidate, not the Shiab contraction, and `Psrc` is a
separate projector. These three maps are not called the same object.

## Controls with power

The executable plants and rejects:

- affine/zero-Hessian charts;
- the wrong fifth/sixth total-Jacobian powers;
- raw `dot h` tensoriality;
- an omitted Hessian term and a wrong Christoffel sign;
- raw Frobenius in place of trace reversal;
- commuting Spin gauges;
- an SO-valid but Spin-invalid sign choice;
- the vector law `O` in place of the raw-covector law `O^-T`;
- adjoint detection of the central sign; and
- `RL=1` plus observed-equation transport as a proof of no-leakage.

The repaired exact run passes `77/77` checks: 43 exact, 1 numerical
128-by-128 check, 7 bounded source receipts, 13 type/boundary checks, and 13
planted controls.

## Remaining boundary and next gate

Wave I establishes a local reconstruction carrier and pointwise associated
port witness. It leaves open:

- a global Lorentz `Met(X)` atlas and observation section for arbitrary `X`;
- spin-structure existence and the global Spin cocycle;
- which observer/Zorro/Y Levi-Civita-derived connection is the tilted
  distinguished `A0`;
- source ownership or uniqueness of `Theta_{Gamma,h}`;
- the moving Shiab contraction and its metric dependence;
- variation of the actual source action through every occurrence of
  `Theta`, `J`, `Psrc`, density, connection, and spinor;
- total bosonic/fermionic Euler tangency and the coset correction;
- Ward identity, Green current, BV quotient, and one common closed domain;
- physical observation no-leakage, stationarity, VEV, mass, index, count,
  or cosmological prediction.

The next high-information gate is

**`RESOLVER-WAVE-J-DESCENDED-SOURCE-ACTION-TOTAL-EULER-AND-WARD`**:

write the displayed source action on this descended local carrier, take the
full first variation including the moving `Theta/J/Psrc` and density terms,
then test total Euler tangency, the diffeomorphism/gauge Ward identities, and
whether one boundary/Green domain can carry the result. A fixed-coefficient
or density-only variation is a planted near-miss, not completion.

P1/P2/P3 remain unchanged and unused. Curt remains formally separate. No
third lane, claim status, canon verdict, or public posture moves.

## Reproduction

```bash
uv run --with sympy==1.14.0 --with numpy python \
  tests/channel-swings/resolver_wave_i_actual_metx_zorro_theta_descent_probe.py
```
