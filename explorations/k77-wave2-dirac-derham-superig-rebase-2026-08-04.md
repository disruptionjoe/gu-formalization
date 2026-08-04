---
title: "K77 Wave 2: the missing Dirac--de Rham operator and super-IG requirement rebase"
date: 2026-08-04
status: construction
verdict: PARTIAL_DIRAC_DERHAM_SYMBOL_BUILT__SOURCE_SELECTED_ACTION_AND_DOMAIN_OPEN
run: RUN-20260804-180800-gu-formalization-k77-wave2-superig-rebase
registry: lab/process/k77-wave2-dirac-derham-superig-rebase.json
probe: tests/channel-swings/k77_wave2_dirac_derham_superig_rebase_probe.py
claim_status_change: none
canon_verdict_change: none
---

# K77 Wave 2: the missing Dirac--de Rham operator

## Result first

The de Rham version of the GU Dirac operator was present in the repository,
but it was not inside the current K77 action/Euler construction.

There were actually five nearby objects being treated as if they were one:

1. the ordinary connection-coupled Hodge--de Rham Dirac `d_A+d_A*` on all
   differential forms;
2. Weinstein's truncated chain
   `Omega0(S) -> Omega1(S) -> Omega13(S) -> Omega14(S)`;
3. the rolled two-by-two Dirac--Rarita--Schwinger seesaw operator on
   `Omega1(S)+Omega0(S)`;
4. the 2021 draft's displayed slash-`D_omega` matrix on four signed
   `zeta/nu` fields; and
5. Weinstein's unreleased cyclic two-connection `D^2` proposal.

Layer 0 says that these are not interchangeable. In particular, the older
repo reconstruction

```text
D_GU = d_A + d_A* + Phi
```

is a `(9,5)` reconstruction which treats `Phi` as an additive zero-order
term. The modern source-native middle arrow is instead

```text
Omega1(S) --d_A--> Omega2(S) --Phi--> Omega1(S) --star--> Omega13(S),
```

so `Phi o d_A` contributes to the **first-order principal symbol**.

This swing constructs that K77 principal operator exactly. After using Hodge
star to identify the output with `Omega1(S)+Omega0(S)`, its frozen symbol is

\[
\sigma_\xi(\mathscr D_A)=
\begin{pmatrix}
 A_\xi & B_\xi\\
 C_\xi & 0
\end{pmatrix},
\]

where

\[
(A_\xi\zeta)_a
=\gamma^b(\xi_b\zeta_a-\xi_a\zeta_b),
\qquad
(B_\xi\nu)_a=\xi_a\nu,
\qquad
C_\xi\zeta=-\xi^a\zeta_a.
\]

The southeast zero is Weinstein's stated seesaw slot. It is retained as a
source constraint, not inferred from the rank calculation.

On the exact real `Cl(7,7)=M_128(R)` carrier:

- positive non-null covector: rank `1920`, kernel `0`;
- negative non-null covector: rank `1920`, kernel `0`;
- null covector: rank `1024`, kernel `896`.

The null result has two independent exact routes. A nonzero `1024` minor was
certified modulo the prime `1000003`, hence over the rationals, and an
explicit `896`-coordinate kernel was constructed. Sage independently returned
the same ranks `1920,1920,1024`. Thus the characteristic set of this frozen
principal candidate is exactly the K77 null cone.

This is a real advance, but it does not yet identify the complete GU fermion
operator. The bare `Phi d_A` middle symbol is neither self-adjoint nor
skew-adjoint under the frozen K77 `B` pairing. A variational action can pair
`D` with its Krein adjoint across the opposite nonchiral sector, and the
draft's four `zeta/nu` signs make that a source-guided completion. The exact
global Hodge/Krein adjoint, draft-9.16 block placement, coefficients, boundary
pairing, and common domain remain open.

## Source reconciliation, including Curt's iceberg

### Curt's role

Curt Jaimungal's complete 30-step iceberg is the detailed secondary
derivation witness. The preserved commit-qualified crosswalk is
`gu-formalization@0aa539214e6082ad2ad9d4697c90da7e73c0e070` at
`lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md`.
Its relevant steps are:

| step | Curt's construction role | present disposition |
|---:|---|---|
| 19 | put fermions in `Omega0(S)+Omega1(S)` with a DRS operator | carrier built; operator now built at principal K77 grade |
| 20 | use the deformation/cohomological complex | released curved operator is not a complex; global/BV complex open |
| 21 | use the southeast-zero seesaw | zero retained; mass hierarchy and spectrum open |
| 22 | reduce `Spin(7,7)` toward `Spin(1,3)xSpin(6,4)` and SM containers | representation containment built; vacuum selection open |
| 23 | label `Omega0`, gamma-trace `Omega1`, and gamma-traceless `Omega1` as families | three kinematic pieces located; physical chiral count not derived |

This uses Curt as requested: as a worked construction map rather than as the
ultimate truth surface. Weinstein's subsequent conversation confirms much of
the geometry but corrects the architecture in places, notably the separate
Einstein--Dirac and Yang--Mills--Higgs action layers.

### Weinstein primary locators

- *Into the Impossible*, `00:34:27--00:36:13`: a de Rham--Dirac--Einstein
  complex, minimally coupled exterior derivative, two-form-to-one-form Shiab,
  and rolled Dirac--Rarita--Schwinger gadget.
- *Theories of Everything: 40 Years*, `02:38:12--02:43:30`: curved
  connection destroys `d_A^2=0`; roll `d_A` and `d_A^*` into an operator;
  truncate `0 -> 1 -> 13 -> 14`; contract and Hodge-star the middle; keep a
  southeast zero.
- Same conversation, `02:44:06--02:45:43`: a new cyclic two-connection
  construction exists but is explicitly unreleased. It is not reconstructed
  here from the spoken mnemonic.
- 2021 draft, p.46 eqs. 9.16--9.20 and p.51: the four-field slash-`D_omega`
  matrix and the rolled `nu/zeta` diagram are the closest displayed source
  surfaces. The repo's rendered transcription does not supply a stable exact
  coefficient/sign matrix adequate to identify it with this completion.

The source collision is therefore `SOURCE-CONFIRMS` for the carrier, chain,
middle-map grammar, and southeast zero; `SOURCE-SILENT/UNRELEASED` for the
global selected operator, cyclic closure, and action/domain completion.

## The chain is not automatically a complex

For a connection `A`,

\[
d_A^2=F_A\wedge(-).
\]

So the curved de Rham sequence is already not a complex. At principal level,
the first adjacent composition does vanish:

\[
A_\xi B_\xi=0,
\]

because `xi wedge xi=0`. The second adjacent composition is generically
nonzero. This is exactly the point at which the unreleased cyclic/two-
connection construction would matter. The present result is therefore a
rolled **operator**, not an on-shell or off-shell cochain complex.

## Conditional nonchiral action placement

The smallest action-compatible completion does not force the middle block to
be self-adjoint. It uses the fundamental nonchiral pair:

\[
I_F(\chi_-,\chi_+;A)
=\operatorname{Re}\int_Y
\langle\chi_-,\mathscr D_A^+\chi_+\rangle_K,
\]

with the conjugate/real partner understood. Equivalently, the doubled Hessian
has the standard cross-paired form

\[
\widehat{\mathscr D}_A=
\begin{pmatrix}
0&(\mathscr D_A^+)^{\dagger_K}\\
\mathscr D_A^+&0
\end{pmatrix}.
\]

An exact finite control verifies this is Krein self-adjoint. Variation with
respect to the connection emits its current once, so it is compatible in
architecture with the already-frozen no-separate-bridge `J_D+J_F` policy.

This is a **conditional completion generated by the action burden**, not a
claim that the draft literally prints this matrix. Closing that identification
requires the exact global `rho(epsilon)`, Hodge, reality, form-degree, and
lower-right placements from the displayed source operator.

## Super-IG requirement correction

The previous Wave-2 gate demanded a full odd action and odd Ward/BV identity.
The source does not demand this:

- TOE `01:42:19--01:44:14` describes fractional-spin fields whose products
  land in the connection/gauge-potential sector, then explicitly declines the
  question “Do you have an action?” as unnecessary for doing GU.
- Portal 2020 `01:29:47` says spinorial products should land in the **linear**
  sector and says mapping them into the nonlinear sector is not wanted.

So the honest source burden is an algebraic super-extension: odd module,
symmetric bracket into the linear connection sector, equivariance, Jacobi,
global descent, and compatible real structures. An odd Noether identity is
required only if an odd action symmetry is separately asserted.

The exact K77 bracket also improves. With `J` ambient chirality, `B` the split
symmetric invariant pairing, and `Omega=BJ`, opposite-half inputs give

\[
\mu_\Omega(u_+,v_-)
=u_+v_-^T\Omega+v_-u_+^T\Omega.
\]

This nonzero map simultaneously preserves `B` and `Omega` and commutes with
`J`. The simultaneous infinitesimal stabilizer is conditionally
`gl(64,R)` after choosing the perfect cross-half pairing. This closes the
previous **pointwise simultaneous-pairing** question on that reduced group.
It does not identify that group with Weinstein's full `H` or `U(64,64)`, nor
does it construct a global supergroup or a generation count.

## Inline specialist pre-assessment

Ten lenses were applied before disposition:

1. **Differential geometry:** keep `star Phi d_A` distinct from `Phi`; type
   every form degree before rolling.
2. **Operator theory:** compute the full first-order block symbol and its
   characteristic set before discussing index or spectrum.
3. **Hyperbolic PDE:** treat the null rank defect as propagation data, not as
   a failure of non-null invertibility; domain remains a later theorem.
4. **Representation theory:** use the real K77 carrier and opposite-half
   pairing; refuse block-to-generation inference.
5. **Krein geometry:** a mass/fermion term is a bilinear; cross-pair `D` with
   its Krein adjoint instead of demanding bare self-adjointness.
6. **Variational bicomplex/BV:** retain even action Ward ownership; do not
   manufacture an odd Noether identity not required by the source.
7. **Symplectic geometry:** intersect the `B` and `Omega` stabilizers and test
   the actual mixed moment map, yielding conditional `gl(64,R)`.
8. **Standard Model phenomenology:** preserve family-shaped representation
   slots while holding masses, poles, chirality, anomaly, and count open.
9. **Source archaeology:** use Curt's all-30-step derivation, Eric's later
   corrections, and draft displays as separate grades.
10. **Computational/proof engineering:** require a prime-minor certificate,
    an explicit complementary kernel, a Sage replay, and planted operator
    confusions.

The council synthesis was unanimous on ordering: the Dirac--de Rham operator
must precede observation/external datum, because the datum needs an actual
operator/domain on which to act. The odd-action requirement was a superseded
target. The source-selected global action placement is the remaining native
Wave-2 gate.

## What this changes

Wave 2 remains partial, but for a different and much narrower reason.

**Built now:**

- source-typed `0 -> 1 -> 13 -> 14` K77 chain;
- exact first-order rolled seesaw symbol;
- exact non-null invertibility and null rank/kernel;
- off-diagonal `d_A/d_A^*` Krein-adjoint incidence;
- conditional cross-paired nonchiral action architecture;
- pointwise mixed bracket landing in the simultaneous `B/Omega` stabilizer;
- formal removal of full odd action/Ward as a source requirement.

**Still needed before Wave 3:**

1. reconstruct or obtain the exact draft-9.16 global block placement and
   decide the lower-right/source-coefficient fork;
2. construct the global `Hodge/Krein/reality/rho(epsilon)` adjoint and
   preboundary pairing;
3. place the operator and the already-frozen bosonic action/current on one
   admissible field domain and rederive the coupled Euler/current/Ward packet;
4. keep algebraic super-IG global descent as a GU structural obligation, but
   do not block the action on an unasserted odd symmetry.

Only after those steps should Wave 3 construct the observation/BV groupoid and
typed receivers for P1/P2/P3.

## Held-out wall

No on-shell cyclic complex, global closed domain, self-adjoint evolution,
vacuum, four-dimensional observation theorem, Standard Model field equation,
mass, pole, residue, anomaly, dark-sector prediction, chirality value,
generation count, P1/P2/P3 use, lane change, canon change, or public-posture
change is claimed.

## Successor advance and correction (2026-08-04)

`explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md`
visually transcribes the complete draft-9.16 four-field matrix, types it as a
density-dual bilinear, fixes the K77 Hodge signs, and builds exact finite or
general templates for the required primalizer, moving-pairing formal adjoint,
Green density, overlap descent, southeast fork, and candidate variational
core. Hostile review rejected promoting those templates to the actual global
K77 operator. Wave 2 therefore remains `PARTIAL` until all sixteen D916 blocks,
the actual primalizer, multi-index adjoint, `rho(epsilon)` descent, and common
connection variation are assembled on the same core. A closed physical
evolution domain, observation theorem, and physical family index remain later
and separate gates.
