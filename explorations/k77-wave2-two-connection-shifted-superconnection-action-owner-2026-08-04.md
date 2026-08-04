# K77 Wave 2: shifted two-connection operator and action-shell ownership

Date: 2026-08-04
Gate: `K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER`
Verdict: **PARTIAL — BOTH PARITY ARROWS ARE BUILT BY ONE SHIFTED OPERATOR;
THE FULL OFF-SHELL SQUARE HAS A MIXED DEFECT; THE SOURCE ACTION IS LOCATED AS A
TRANSGRESSION; THE NAIVE IG-PAIR SHELL DOES NOT MATCH ITS EULER SHELL.**

## Plain result

The old “missing reverse arrow” was partly a grading mistake. Put the second
de Rham summand one internal degree higher. Then

\[
 \mathcal D_{A,B}=
 \begin{pmatrix}
 d_A&-F_B\\
 1&-d_B
 \end{pmatrix}
\]

has total degree one on
`Omega*(E0) plus Omega*(E1)[1]`. One odd operator therefore restricts to both
the even-to-odd and odd-to-even arrows. No second formula needs to be invented.

That does **not** yet make Eric's “on-shell complex” agree with the released GU
action. Exact noncommutative exterior algebra gives

\[
 \mathcal D_{A,B}^2=
 \begin{pmatrix}
 F_A-F_B&-d_AF_B+F_Bd_B\\
 d_A-d_B&0
 \end{pmatrix}.
\]

For the IG identification `A=B+T`, the exact control has a nonzero northeast
term `-T wedge F_B` as well as the augmented-torsion southwest term. A scalar
commuting toy erases this defect and is therefore an invalid control.

On the diagonal `A=B`, the whole square vanishes. But the released action has
Euler equation `Upsilon=S-T=0`, and on a curved background its derivative is
generally nonzero at `T=0`. Thus the diagonal complex shell and the action
shell are different objects.

The constructive next step is not another external bit. It is a bosonic
Euler primalizer and pair lift

\[
 R_B:\Omega^{13}(Y,\operatorname{ad}P)^!\longrightarrow
 \Omega^1(Y,\operatorname{ad}P),
 \qquad A-B=R_B\Upsilon,
\]

followed by recomputation of the square, Ward identity and observation
descent.

## 0. Layer 0: the six objects

| object | type | relation established here |
|---|---|---|
| IG bi-connection | pair in `A(P) x A(P)` from one IG element | source-confirmed |
| augmented torsion `T` | `A-B in Omega1(ad P)` | source-confirmed/definition-level |
| shifted cyclic operator | total-odd operator on `Omega*(E0) plus Omega*(E1)[1]` | algebraically constructed |
| operator curvature `D^2` | total-even endomorphism | exactly computed |
| bosonic Euler row `Upsilon` | density-dual adjoint-valued thirteen-form | source-owned, distinct from `T` |
| scalar action `I1B` | first-order density integral | source-owned, pre-existing |

The words “two connections,” “curvature,” “on shell,” and “action owner” do
not identify these objects by themselves.

## 1. Source collision changed the requested work

The immediate TOE passage supplies the four-block mnemonic but withholds its
construction and shell. The older Portal and Into the Impossible sources do
supply a bi-connection pair whose difference is augmented torsion. Separately,
the 2021 draft already supplies the actual first-order bosonic action.

This corrects two inherited assumptions:

1. the reverse parity arrow is not necessarily missing once the internal shift
   is written;
2. the bosonic action owner was not missing, although an action specifically
   owning the 2025 cyclic operator remains source-silent.

The full receipt is
[`gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md`](../lab/sources/gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md).

## 2. Why all four blocks are odd

Assign internal degree zero to `E0` and internal degree one to `E1`:

| block | form-degree change | internal-degree change | total |
|---|---:|---:|---:|
| `d_A` | `+1` | `0` | `+1` |
| `-F_B` | `+2` | `-1` | `+1` |
| `1` | `0` | `+1` | `+1` |
| `-d_B` | `+1` | `0` | `+1` |

The executable builds the total parity matrix, proves
`P D + D P=0`, and verifies that both parity restrictions are nonzero. This is
the full algebraic even/odd pair. It is not yet an analytic complex, a K77
closed domain or a physical Hamiltonian.

## 3. The full square, without a made-up mixed Bianchi identity

Direct block multiplication gives

\[
 \begin{aligned}
 (D^2)_{11}&=d_A^2-F_B=F_A-F_B,\\
 (D^2)_{12}&=-d_AF_B+F_Bd_B,\\
 (D^2)_{21}&=d_A-d_B,\\
 (D^2)_{22}&=-F_B+d_B^2=0.
 \end{aligned}
\]

The earlier source-bounded square set the northeast block to zero under a
mixed-Bianchi relation. The exact matrix-valued exterior-DGA control shows why
that relation cannot be imported from ordinary Bianchi. Ordinary Bianchi
cancels the `B`-only part. With `A=B+T`, the remaining left-module term is
`-T wedge F_B`, which is nonzero in the planted active fixture.

This is a **candidate formula correction**, not a kill of the two-connection
mechanism. A compensating term, a different module convention or an
Euler-derived pair could alter the block; each must be constructed.

## 4. What owns the `1/2` and `1/3`

In the source-normalized wedge convention,

\[
 F_{B+tT}=F_B+t,d_BT+t^2T\wedge T.
\]

Hence

\[
 \overline F(B,T)=\int_0^1F_{B+tT}\,dt
 =F_B+\frac12d_BT+\frac13T\wedge T.
\]

The action's coefficients are therefore the exact connection-path average,
not a fit to an observed particle or cosmological target. In a closed
three-dimensional cyclic trace control,

\[
 2\langle T,\overline F\rangle
 =CS(B+T)-CS(B),\qquad
 \delta\langle T,\overline F\rangle
 =\langle\delta T,F_{B+T}\rangle.
\]

Automatic differentiation verifies the first variation in three independent
noncommuting directions. Adding the source-shaped
`1/2<T,T>` term through a nondegenerate indefinite primalizer gives a symmetric
Hessian. This validates the transgression/action grammar. It does not select
the actual moving K77 Shiab; the K77-B2/B3 obstructions still apply.

The two coefficient constraints fix two coefficient parameters, so this
particular construction is unique with **surplus zero**, not positive surplus.

## 5. Why the shells differ

The naïve IG pair says

\[
 A-B=T.
\]

The shifted square is certainly zero when `T=0` and `A=B`. The source action,
however, varies to the swervature/displasion row. In the exact cyclic control,
the derivative at `T=0` is the curved-background response `F_B`, and is
nonzero. Therefore

```text
D(A,B)^2 = 0 at A=B
```

does not mean

```text
d I1B = 0.
```

This is the key negative result of the swing. It is a Layer-0 shell mismatch,
not evidence that GU has no action.

## 6. The constructive lift now demanded

The smallest action-first repair is to build a moving bosonic pseudo-musical

\[
 R_B:\Omega^{13}(\operatorname{ad}P)^!\to
 \Omega^1(\operatorname{ad}P)
\]

from the same Hodge, Shiab, active `epsilon`, adjoint/Krein form and density
used by `I1B`, then set a candidate pair difference to `R_B Upsilon`.

This would make the diagonal of the pair coincide with the action shell by
construction. It still has to pass:

1. full source-group/tilted-gauge naturality;
2. right codomain and nondegeneracy on the action-derived restricted domain;
3. moving-pairing terms in the first variation;
4. the corrected northeast square and Bianchi/Ward identity;
5. observation descent and no leakage;
6. a Green/domain check before any physical equation is claimed.

An external datum cannot replace this map. P1/P2/P3 can only be tested after a
natural receiving slot exists.

## 7. Seven-axis mapping after Layer 0

| layer | status |
|---|---|
| Layer 0 | pass with correction: `T`, `Upsilon`, `D^2`, and `dI1B` separated |
| L1 source | four tokens, signs, IG pair and I1B located; pair/shell identification source-silent |
| L2 algebra | shifted total-odd operator, both parities and exact full square built |
| L3 geometry | IG pair local grammar available; actual moving K77 Euler primalizer open |
| L4 variation | finite cyclic first/Hessian checks pass; actual moving Shiab variation open |
| L5 covariance | ordinary DGA/Bianchi exact; full active-`epsilon` descent open |
| L6 analytic | no closed Green/evolution domain claimed |
| L7 physics | no particle, generation, mass, gravity or cosmology row moves |

## 8. Constraint accounting and disposition

- transgression parameters: `2`;
- independent path-average coefficient constraints: `2`;
- transgression constraint surplus: `0`;
- trace-`q` projective parameters: `1`;
- new trace-`q` selection equations: `0`;
- trace-`q` surplus remains `-1`;
- P1/P2/P3: unchanged and unused;
- Curt: formally separate guidance inside the Eric lane;
- `TG-1 AND TG-2 AND TG-3`: not promoted;
- Wave 3: closed.

Final executable receipt:

```text
14 source + 20 type + 22 exact + 12 planted = 68/68 PASS
```

Next gate:

```text
K77_BOSONIC_EULER_PRIMALIZER_AND_ACTION_SHELL_TWO_CONNECTION_LIFT
```
