---
artifact_type: exploration
label: "Resolver Wave D: native 126 connection placement"
created: 2026-08-03
status: exploration
posture: adversarial; Layer-0-first; construction-first; exact exterior algebra and native finite matrices
title: "A native grade-six contraction emits a real 252 kernel; source-owned moving full-20 placement remains open"
grade: "EXACT local Spin(6,4) and full-Spin(9,5) algebra plus finite native K/right-H/C/full-20 incidence; moving full-Sp descent, total P0/Y placement, source selection, VEV, and mass remain open"
canon_verdict_change: none
route_disposition: CONTINUE
hostile_review_status: PASS_AFTER_REPAIRS
depends_on:
  - lab/specifications/six-axis/six-axis-template.md
  - explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md
  - explorations/W192-explicit-carrier-kernel-spectral-gate-2026-07-14.md
  - explorations/W194-w192-reciprocal-packet-intake-gate-2026-07-14.md
  - explorations/unified-source-datum-packet-v0-2026-07-30.md
  - explorations/unified-source-datum-variational-emission-map-2026-07-30.md
scripts:
  - tests/generation-sector/q7_native_126_connection_placement.py
  - tests/generation-sector/q7_native_126_connection_placement_sage.py
  - tests/channel-swings/resolver_wave_d_full20_126_placement_probe.py
---

# Resolver Wave D: native 126 connection placement

## Outcome first

Wave D makes the missing connection-carrier arrow concrete, but it does not
yet make a mass.

After choosing the fixed observer split, the relevant tensorial one-form
carrier contains

```text
V10* tensor Lambda6(V10*).
```

Grade six is an actual native `Sp(32,32;H)` connection grade: all 210 internal
blades are K-anti-self-adjoint and right-H-linear on the repository's actual
trace-reversed `Cl(9,5)` carrier. Metric contraction of the one-form leg gives

```text
delta : V10* tensor Lambda6(V10*) -> Lambda5(V10*).
```

This map is canonical and surjective. Its target is one real 252-dimensional
carrier, whose complex Hodge halves are the conjugate `126+` and `126-`. The
raw degree-five object is now correctly an effective K-self-adjoint kernel,
not falsely called a connection generator.

For a five-form `phi`, the exact pure-component insertion

```text
j5(phi)_i = eta_i e^i tensor (e^i wedge phi)
```

satisfies

```text
delta j5 = 5 id,       wedge j5 = 0.
```

On the full fourteen-dimensional carrier, the multiplicity-one direct
grade-six Clifford contraction summand instead gives

```text
4 phi from the horizontal legs + 5 phi from the vertical legs = 9 phi.
```

Therefore the vertical `5 phi` certificate is an honest observer-stabilizer
component, while full `Spin(9,5)` covariance locks it to a horizontal
companion. A fixed vertical-only story is not full symmetry.

The physical spinor factors are favorable but conditional:

- `K Gamma5` is Hermitian;
- both invariant C branches make `C Gamma5` alternating for an identical
  Grassmann field;
- bare grade-seven companions are K-anti and C-symmetric, so they drop from
  the corresponding bare real/diagonal bilinears.

But the existing N3 warning fires exactly: the complete densities
`Herm(P0^dagger K_G c_rho(v) Y_K P0)` and
`Alt(P0^T C c_rho(v) Y_C P0)` decide survival. A skew or anti-Hermitian
provenance factor reverses the bare grade-five/grade-seven verdicts in the
executable controls. This wave has derived the spinor factor, not the final
Yukawa matrix.

The full-20 check produces a decisive fork. A distinct map that retains the
tensorial one-form as the output vector index has, for the planted five-form
representative, one desired 144 component per source

```text
L16+ -> X2T+,   R16- -> X1T-,
L16- -> X2T-,   R16+ -> X1T+.
```

but also an unavoidable paired `imGamma` 16 and `kerGamma` 16 component. The
allowed `P_R` retains the low-`R` 16 companion as well as the 144; the repo has
no admissible `X`-only `P0` that removes it. Moreover, that useful
`S -> V tensor S` map is **not** the source packet's written contraction

```text
c_rho(v) = sum_i c(nu^i) rho(Phi_i) : S -> S.
```

A naive componentwise lift of the contracted `End(S)` kernel leaks between
the written `imGamma` and `kerGamma` sectors. Thus the repo now has both sides
of the desired 126 story but not the arrow identifying them: the written
contraction supplies the real-252 spinor kernel; the one-form-output
comparator supplies a 144 incidence together with 16-dimensional companions.
A source-derived superconnection,
soldering, or other full-20 rule must prove that relation rather than rename
one map as the other.

The gate transition is **`OPEN -> PARTIAL_CONSTRUCTED`** and the route decision
is **CONTINUE**. No external datum is needed to make this local algebraic map,
and none is spent. P1/P2/P3 remain unchanged and unused.

## 0. Layer-0 object table

| shared phrase | typed object | ruling |
|---|---|---|
| affine connection | `A`, with `A0` another connection transforming in the same affine way | neither `A-A0` nor the effective mass kernel |
| source-packet residue | `v_s=res_s^V(A-A0)`, a tensorial ad-valued one-form | written source variable; source solution and nonzero grade-six component open |
| Weinstein distortion | `T_omega`, the gauge-rotated Levi--Civita distortion/augmented torsion, another tensorial ad-valued one-form | source-adjacent but not identified with `v_s` |
| grade-six component | `T_(V,6) in V10* tensor Lambda6(V10*)` on a chosen tensorial one-form carrier after a moving Clifford/soldering split | native at fixed stabilizer grade; source-owned nonzero value and full-Sp descent open |
| effective five-form | `delta T_(V,6) in Lambda5(V10*)` or the grade-five part of `c_rho(T)` | one real 252, K-self; not itself an Sp connection generator |
| `126+/-` | conjugate complex `star=+/-i` halves of the real 252 | not two independent real fields |
| K mass factor | `Herm(P0^dagger K_G c_rho(T) Y_K P0)` on the full-20 carrier | neither `K_G` nor the left adjoint projector is inert bookkeeping; bare `K Gamma5` parity does not settle it |
| C mass factor | the alternating projection of complete `P0^T C c_rho(T) Y_C P0` plus reality completion | bare `C Gamma5` parity does not settle it |
| RS mediator map | a map from the pure-spinor full-20 slots into the 144 vector-spinor slots without unwanted companions | the tested comparator has one desired 144 component plus `imGamma16` and `kerGamma16`; written `c_rho:S->S` is different |
| VEV/mass | a nonzero stationary source-owned background surviving observation, quotient, and domain, followed by an induced 4D block | entirely downstream |

These distinctions implement Layer 0 before the seven axes. In particular,
“the connection contains a 126” is now shorthand only for a canonical real
252 *effective isotypic component* derived from a native grade-six
connection. It does not mean a free complex 126 connection field.

## 1. Specialist pre-assessment and preregistration

Three read-only specialists were used before construction:

1. A representation/Clifford specialist classified the grade-six route,
   found the full-D7 horizontal/vertical coefficient lock, and identified an
   abstract multiplicity-one grade-ten comparator carrier.
2. A Krein/right-H/C specialist proved the scalar-phase intersection is zero
   in the native quaternionic real form and required total-kernel rather than
   operator-only tests.
3. A source/differential-geometer traced the candidate to the source-owned
   inhomogeneous distortion, found the primary-source contraction correction,
   and required the `c_rho` versus one-form-output fork to remain explicit.

The preregistered outcomes were:

- `CONSTRUCT_LOCAL_COMPONENT` if the grade-six connection coefficient is
  native and contraction is canonical, nonzero, and K/C compatible;
- `REBASE_PHASE_OR_SOLDERING` if only a phased or moving-soldering completion
  survives;
- `KILL_126_CONNECTION_ROUTE` if every admissible connection coefficient has
  zero five-form image or fails both physical pairing branches;
- retain `PARTIAL` if source selection, moving full-Sp descent, or full-20
  placement is missing.

The first and fourth conditions fired. The local construction is real; the
physical placement remains partial.

## 2. Exact exterior algebra

Let `N` have dimension ten and signature `(6,4)`. Define

```text
D = N* tensor Lambda6 N*,
delta(alpha tensor Phi) = i_(alpha sharp) Phi,
wedge(alpha tensor Phi) = alpha wedge Phi.
```

The exact basis incidence gives

```text
dim D = 10*C(10,6) = 2100,
rank delta = C(10,5) = 252,
rank wedge = C(10,7) = 120,
rank(delta,wedge) = 372,
dim ker(delta,wedge) = 1728.
```

Every five-form row has five signed preimages; every seven-form row has seven.
The canonical injections satisfy

```text
delta j5 = 5 I,   wedge j5 = 0,
delta j7 = 0,     wedge j7 = 7 I.
```

Consequently

```text
N* tensor Lambda6 N* = Lambda5 N* + Lambda7 N* + Hook1728
```

and `P5=(1/5)j5 delta` is a rank-252 idempotent. The independent Sage 10.9
D5 character calculation gives

```text
10 tensor 210 = 120 + 126+ + 126- + 1728
```

with every multiplicity one.

At full D7 grade,

```text
14 tensor Lambda6(14)
 = Lambda5(14) + Lambda7+(14) + Lambda7-(14) + R36608,
```

so the direct contraction has multiplicity one and `delta j=9I`. Splitting an
internal five-form across `4+10` gives the exact `4+5` coefficient lock.

Sage also finds an abstract multiplicity-one `Lambda5(14*)` type in
`14 tensor Lambda10(14)`. That is a distinct Hodge--wedge/chirality route, not
the direct grade-six part of the written Clifford multiplication. The Sage
certificate establishes the carrier multiplicity, not an executed
Hodge--wedge map. Such a map would require orientation/Hodge data and remains
a live comparator. This wave does not identify it with P1 or add a second
action coefficient.

## 3. Native K, right-H, and C classification

The actual repository matrices use the trace-reversed split

```text
(3,1) base + (6,4) fibre = (9,5).
```

The exhaustive internal finite check gives:

| internal grade | blades | K adjoint | right-H | role |
|---:|---:|---|---|---|
| 4 | 210 | self | yes | not a native Sp connection grade |
| 5 | 252 | self | yes | effective real-252 kernel |
| 6 | 210 | anti | yes | admissible native connection coefficient |
| 7 | 120 | anti | yes | companion of generic Clifford multiplication |

The scalar phase shortcut is killed exactly in the native real form. For a
real right-H grade-four or grade-five word `X`, K-anti-adjointness of `zX`
requires `bar(z)=-z`, while right-H requires `bar(z)=z`; therefore `z=0`.
Numerically, `iX` has zero K-anti defect and right-H defect `2`. This does not
kill the larger complex `U(64,64)` comparator; it kills only the native
`Sp(32,32;H)` shortcut.

For both invariant C branches, every real grade-five `C Gamma5` is
alternating, while every grade-seven `C Gamma7` is symmetric. The analogous K
classification makes `K Gamma5` Hermitian and `K Gamma7` anti-Hermitian.
These are full exhaustive blade statements, not samples.

The planted provenance controls are load-bearing and typed in the N1
three-generation space. A skew `Y_C in M3(C)` reverses both C transpose
outcomes on its rank-two subspace, and a full-rank anti-Hermitian
`Y_K in M3(C)` can make a grade-seven total K kernel Hermitian. Therefore the
bare spinor factor cannot close `SA-Y1` or a mass row without the actual total
ordered `P0/rho/Y` placement.

## 4. What the written source contraction now does

The N1 packet writes, for a vertical coefficient,

```text
v_s = sum_i nu^i tensor Phi_i,
c_rho(v_s) = sum_i c_G(nu^i) rho(Phi_i).
```

Take a real internal five-form `phi` and the pure grade-six connection
component

```text
Phi_i = eta_i c(e^i wedge phi).
```

The native matrices give exactly

```text
c_rho(v_s) = 5 c(phi).
```

Replacing the trace-reversed `(6,4)` musical by a raw all-positive Frobenius
identification changes the planted representative's coefficient from `+5` to
`-3`; the musical is not cosmetic.

A generic grade-six coefficient produces both degree five and degree seven
under Clifford multiplication. The pure `j5` component has no degree-seven
part, but the source action has not yet proved that its actual solution lies
in `im j5`. At the bare K/C spinor level the seven-form is projected out; at
the total `Y` level that can reverse. Both descriptions are retained.

The stronger Eric-lane variable is the gauge-equivariant displaced or
augmented torsion built from a connection and the gauge-rotated distinguished
connection. The current source packet instead writes `v_s=res_s^V(A-A0)`.
Those are source-adjacent but not yet proved identical. The grade-six map is
valid on either typed one-form carrier; source ownership requires choosing and
varying the actual one.

## 5. Full-20 fork

Three different operations were tested rather than compressed into “the
lift.”

### 5.1 Written contraction

`c_rho(v):S->S` supplies the grade-five real-252 endomorphism. It does not
retain an output vector index and therefore does not by itself instantiate
`Hom(16,144)`.

### 5.2 Naive componentwise lift

Applying the grade-five `End(S)` matrix independently to every component of
`V tensor S` is a natural-looking near miss. It has live leakage in both
directions:

```text
imGamma -> kerGamma norm 5.42105,
kerGamma -> imGamma norm 4.78091.
```

It therefore does not preserve the written `I/R` split and cannot be silently
used as the missing `End(S)->End(E20)` placement.

### 5.3 One-form-as-output comparator

Retaining the tensorial one-form covector as the vector-spinor output defines
a different map `S->V tensor S`. For the planted five-form representative,
its gamma trace is exactly `5 c(phi)` and both its imGamma and gamma-traceless
pieces have rank 128. Each source has one desired Wave-C 144 component, but it
also has a paired `imGamma` 16 component and a low-`R` `kerGamma` 16
component. Thus the comparator is not a pure `S->144` map. `P_R` does not
remove the low-`R` companion, and an `X`-only projector is not among the
allowed `P0`s.

But it is a comparator, not yet the source insertion. A source-derived
superconnection, soldering map, or odd extension must show why this map rather
than the written contraction enters the action, how its reciprocal block is
completed under K/C reality, and which `P0` retains it. Until then the durable
status is:

```text
WRITTEN_REAL252_KERNEL_CONSTRUCTED;
ONE_FORM_COMPARATOR_144_PLUS_16_COMPANIONS_CONSTRUCTED;
IDENTIFICATION_AND_TOTAL_FULL20_PLACEMENT_OPEN.
```

## 6. Primary-source collision

The source review changes the ordering but does not supply the missing arrow.

| primary passage | disposition | consequence |
|---|---|---|
| TOE `01:35:23-01:36:08` | `SOURCE-CONFIRMS` the Higgs-like object comes from an ad-valued one-form | the connection carrier, not a free five-form, is the right starting point |
| TOE `01:36:35-01:36:56` | `SOURCE-CORRECTS` projection to contraction in Eric and Curt's curvature-map discussion | motivates care with terminology but does not establish this wave's `delta` or its ordering |
| TOE `02:18:17-02:20:33`; UCSD `00:17:01-00:25:03` | `SOURCE-CONFIRMS` gauge-rotated Levi--Civita/distortion and its inhomogeneous equivariance | the eventual source variable should be the equivariant displaced connection object |
| UCSD `00:42:42-00:43:47` | `SOURCE-CONFIRMS` vertical ten, trace-reversed Frobenius `(6,4)`, and minimal/Yukawa coupling identification | the exact musical and the written Clifford contraction are source-relevant |
| named sources above | `SOURCE-SILENT` on `V* tensor Lambda6 -> Lambda5`, the real 252/126 split, and the `c_rho`/one-form-output identification | these are reconstruction results, not claims attributed to Weinstein |
| TOE `02:52:38-02:54:14` | `SOURCE-CONFIRMS_OPEN` on masses for the 16/144 sectors | no VEV or mass may be imported from the transcript |

## 7. Exact evidence and controls

The direct Wave-D packet passes **59 exact/boundary assertions plus 11 planted
or hostile near-miss controls = 70/70**:

- exact signed exterior algebra: `31/31`, including four planted route errors;
- independent Sage D5/D7 characters: `12/12`, including one multiplicity
  plant;
- actual native 128-by-128/full-20 matrices: `27/27`, including scalar-phase,
  provenance, wrong-musical, and naive-lift near misses.

The planted controls reject an unnormalized projector, coefficient `1/4`, a
free horizontal/vertical coefficient, raw `Lambda5 subset ad(P)`, a second 126
copy, both scalar phases, C/K provenance transfer, raw Frobenius musical, and
the naive full-20 lift.

## 8. Construction consequence and next gate

The next named gate is
**`RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT`**:

1. choose the actual varied source one-form—current `v_s` or the
   gauge-equivariant `T_omega`—and compute the grade-six tangent image;
2. dress the `4+10` and grade-six projections by the moving
   `epsilon_IG`/soldering field and prove overlap descent;
3. derive or kill the map identifying the written `c_rho:S->S` insertion with
   a full-20 operator, and remove or physically account for the comparator's
   `imGamma16`/`kerGamma16` companions while retaining its 144 component;
4. construct the complete K and C reciprocal/reality blocks and test every
   `P0` and the actual ordered `Y_K/Y_C` factors;
5. retain the abstract grade-ten multiplicity-one carrier as an
   orientation-priced comparator and do not claim a Hodge--wedge map or spend
   P1 without constructing the natural map;
6. vary the actual source term and require a nonzero coefficient plus Ward
   identity before asking for a stationary VEV.

Only if that gate closes should the campaign proceed to a VEV, Pati--Salam
neutral direction, or induced four-dimensional mass calculation.

## 9. Boundaries

- No source equation selects a nonzero grade-six component.
- No moving full-`Sp(32,32;H)` grade projection or global overlap descent is
  proved.
- No total `P0/rho/Y_K/Y_C/C` full-20 kernel is built.
- The one-form-output comparator is not a pure 144 map and is not identified
  with written `c_rho`.
- No stationary vacuum, normalizable 4D mode, Yukawa coefficient, mass,
  seesaw scale, or generation count is derived.
- P1/P2/P3 remain unchanged and unused.
- No claim, canon, protected verdict, public posture, count, lane, Eric/Curt
  separation, or third-lane status moves.
