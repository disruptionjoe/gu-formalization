# K77 Wave 2: up/back/over path adapter and independent square-root target

Date: 2026-08-04
Gate: `K77_TWO_LAYER_UP_OVER_PATH_ADAPTER_AND_INDEPENDENT_SQUARE_ROOT_TARGET`
Verdict: **PARTIAL**

## Outcome

This swing constructed the strongest source-bounded two-connection square,
proved its cancellation exactly, and wrote the universal block grammar that
relates it to a coupled Bose--Fermi action. It also killed the cheapest direct
adapter: neither the plus nor the minus path admits any nonzero projective
coefficient in the existing K77 trace-`q` left/right family.

That failure does **not** kill the trace-`q` fermion operator or the two-layer
action. It identifies the missing construction more precisely: the mixed
Bose--Fermi cross maps `U,V` must be built as their own source-owned maps.

## Ten-lens preassessment

Before computation, the swing used ten lightweight specialist lenses:

1. **Differential geometry:** compare two connections before identifying their
   difference with torsion or contorsion.
2. **Representation theory:** type every block by its carrier; do not equate a
   bosonic connection difference with a fermionic Clifford insertion.
3. **Variational bicomplex/BV:** treat mixed maps as derivatives of one common
   action, not free bridge equations.
4. **Hyperbolic PDE:** distinguish cancellation of differential order from a
   physical domain or positive energy.
5. **Symplectic geometry:** regard up-and-back as a diagonal composite and
   up-and-over as an off-diagonal path in a totalized complex.
6. **Operator/Krein theory:** retain the indefinite adjoint and avoid a positive
   Hilbert replacement.
7. **Standard Model phenomenology:** forbid interpreting a formal off-diagonal
   map as a Yukawa or mass channel before observation/reduction.
8. **Topology/anomaly:** do not spend P1/P2/P3 on a missing local map.
9. **Computational algebra:** solve the finite sign and coefficient-rank
   problems exactly with planted noncommuting controls.
10. **Proof/distributed systems:** propagate only the scoped kill and leave the
    target obligation live.

The convergence was to test two things separately: the independent bosonic
square target and the proposed K77 adapter.

## Layer 0

Let `B` denote the bosonic rolled/two-connection carrier and `F` the fermionic
K77 carrier. Then:

- `d_A-d_B` lies in the bosonic endomorphism complex and is zeroth-order;
- `alpha gamma(q)A + beta A gamma(q)` is a fermionic first-order principal
  symbol;
- `U:B -> F` and `V:F -> B` are cross-complex maps;
- a coefficient of the fermion operator is not a substitute for `U` or `V`.

This clears the homonym collision around “connection square root.”

## 1. Independent two-connection target

The TOE 2025 mnemonic names, in order, `D_A`, `F_B`, identity and `D_B`, then
recalls two negative signs in the second column. The strongest matching block
operator is

\[
\mathbb D_{A,B}=\begin{pmatrix}d_A&-F_B\\1&-d_B\end{pmatrix}.
\]

With the curvature and mixed-Bianchi relations,

\[
d_A^2=F_A,\quad d_B^2=F_B,\quad d_AF_B=F_Bd_B,
\]

direct block multiplication gives

\[
\mathbb D_{A,B}^2=
\begin{pmatrix}
F_A-F_B & -d_AF_B+F_Bd_B\\
d_A-d_B & -F_B+d_B^2
\end{pmatrix}
=
\begin{pmatrix}F_A-F_B&0\\d_A-d_B&0\end{pmatrix}.
\]

Thus the square has exactly the advertised kind of obstruction: a curvature
difference and a zeroth-order connection difference, with the derivative paths
cancelled. A noncommuting `2 x 2` finite control satisfying the mixed Bianchi
identity tested all four sign placements; only `(-,-)` produced this target.

Grade: **source-bound reconstruction with exact algebra**. Weinstein explicitly
says the cyclic construction was unreleased, so the formula is not attributed
to him as a published exact definition.

## 2. The typed path adapter

For a bosonic operator `D`, fermionic operator `F`, and zero-order mixed maps
`U,V`, the total operator is

\[
\Delta=\begin{pmatrix}D&V\\U&F\end{pmatrix}.
\]

Its exact noncommutative square is

\[
\Delta^2=
\begin{pmatrix}
D^2+VU & DV+VF\\
UD+FU & UV+F^2
\end{pmatrix}.
\]

This makes the Portal wording precise:

- diagonal `VU` and `UV` are the two **up-and-back** composites;
- `DV+VF` and `UD+FU` are the two **up-and-over / over-and-up** sums;
- stress-type terms can live on the diagonal;
- Dirac/path equations can live off diagonal;
- order reduction requires equations on the mixed maps, not merely a choice of
  fermion coefficient.

This is a scaffold, not yet the GU action, because actual `U,V` have not been
stabilized or varied.

## 3. Direct K77 shortcut: exact kill

The direct shortcut set `D=F=A_K77` at principal-symbol level and tried the
existing left/right trace-`q` maps

\[
L=\gamma(q)A_{K77},\qquad R=A_{K77}\gamma(q)
\]

as the mixed path. For both candidate path signs the probe evaluated all 14
basis covectors on three deterministic real K77 fields and formed the exact
coefficient response for `alpha L+beta R`.

```text
rank(A L + L A, A R + R A) = 2
rank(A L - L A, A R - R A) = 2
```

There are only two coefficient columns, so either rank-two witness proves that
the full coefficient map has trivial kernel. Hence neither `[1:1]`, `[1:-1]`,
nor any other nonzero projective coefficient cancels the direct path.

This is a **candidate-map kill**:

```text
bare K77 middle operator + trace-q repair as the cross-complex path
```

It is not a mechanism kill for two-connection totalization, the common action,
or the trace-`q` fermion family.

## Constraint surplus

The swing found zero source-owned constraints on the one remaining projective
fermion coefficient:

\[
\text{surplus}=0-1=-1.
\]

The two-connection square is an independent bosonic target, but without typed
`U,V` it does not yet constrain that fermion coefficient. P1/P2/P3 are not
used; an external datum cannot manufacture a missing cross-map.

## What moved

- Independent square-root target: **constructed at source-bounded exact-algebra
  grade**.
- Universal up/back/over adapter: **constructed formally and type-separated**.
- Direct K77 trace-`q` adapter: **killed exactly**.
- Stabilized mixed Bose--Fermi maps: **open**.
- Fermion coefficient selection: **unchanged, surplus `-1`**.
- Wave 3: **closed**.
- Particle recovery, observed equations, domain and vacuum: **not claimed**.

## Next gate

`K77_STABILIZED_MIXED_BOSE_FERMI_CROSS_MAPS_AND_TARGET_MATCH`

Start from the previously cell-typed equation `10.10` inventory and the later
two-connection explanation. Build the smallest globally typed candidates for
`U,V`; require them to arise from the same action and to satisfy the exact
off-diagonal order-cancellation and diagonal target equations. If no candidate
survives, emit the missing representation/action slot rather than circling back
to “an external datum is needed.”

## Executable receipt

`tests/channel-swings/k77_wave2_up_back_over_target_probe.py` passes:

```text
11 source + 17 type + 15 exact + 8 planted = 51/51
```
