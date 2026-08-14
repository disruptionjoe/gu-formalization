---
artifact_type: exact_operator_bv_descent_and_scope_result
created: 2026-08-13
status: FIXED_J10_FAILS_CURRENT_GAUGE_DESCENT__MOVING_J10_IS_GAUGE_COVARIANT__OBSERVED_PRINCIPAL_COMPLEX_LINEARITY_SURVIVES_CONDITIONALLY__PHYSICAL_COHOMOLOGY_AND_GREEN_DOMAIN_UNBUILT
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Selected K77 J10 BV and Green-domain descent gate

## Result first

The normal ten-volume `J10` does not presently descend as a **fixed** complex
structure to the physical GU solution space.

There is nevertheless a sharp positive sub-result.  The spinor-only `J10`
must first be lifted to the owned fermion carrier

```text
Omega1(S) + Omega0(S).
```

The naive diagonal lift fails to preserve the gamma-trace projector.  The
split-natural lift

```text
Jhat = (R_split tensor J10) + J10,
```

where `R_split` is `+1` on the observed four-plane and `-1` on the normal
ten-plane, satisfies `Jhat^2=-1`, preserves the Rarita--Schwinger carrier, is
an isometry of both currently owned Spin-natural one-form action pairings, and
commutes with every observed horizontal principal symbol.  It does not commute
with any of the ten independent normal-axis ambient symbols.

The ordinary-gauge result is decisive for a fixed polarization.  The actual
selected rank-25 gauge image decomposes exactly as

```text
17 split-preserving directions + 8 mixed-split directions.
```

All eight active mixed directions break fixed `J10`.  Hence fixed `J10` is not
basic for the currently owned ordinary-gauge BRST quotient.  If `J10` is
allowed to move with

```text
sJ10 = [c,J10],
```

the covariance identity closes for all 91 Spin ghost generators.  That makes
`J10` a covariant reduction field; it does not make it a fixed polarization on
the quotient.

The repository does not own a complete physical primal-carrier BV
differential or a global physical Green domain.  Their commutator and descent
therefore cannot honestly be reported as passing.  The exact verdict is:

> Conditional observed principal complex linearity passes for `Jhat`; fixed
> `J10` descent through the owned gauge complex fails; moving-`J10` covariance
> passes; complete physical BV cohomology and Green-domain descent remain
> unbuilt.

No identification with quantum superposition follows.

## Layer 0

The computation keeps the following objects distinct:

| object | exact status | excluded inference |
| --- | --- | --- |
| spinor `J10` | normal Clifford volume, square `-1` | endomorphism of the full fermion carrier |
| `Jhat` | reflection-twisted lift to `Omega1(S)+Omega0(S)` | action-selected physical polarization |
| fixed `J10` | commutes with the split stabilizer | basic under the current full gauge image |
| moving `J10` | ordinary-gauge covariant | fixed complex structure on gauge cohomology |
| observed principal operator | `Jhat`-complex-linear | complete lower-order physical BV operator |
| ambient `Y14` operator | normal symbols break `Jhat` | observed Lorentzian Cauchy operator |
| action pairings | `Jhat`-isometric | positive physical inner product |
| trace-owned `H_q` | `J10` anti-isometric | same object as the action pairing |
| local observed `H^s` carrier | conditionally preserved | global closed Green/Calderon/BFV domain |

## Exact carrier computation

Use the source-ordered split

```text
BASE   = (0,7,8,9),
NORMAL = (1,2,3,4,5,6,10,11,12,13).
```

On the exact real `128 x 128` Clifford module,

```text
J10 = product_{a in NORMAL} gamma_a,
J10^2 = -I.
```

Spinor-only `I_14 tensor J10` does not commute with the gamma-trace projector.
The missing vector action is forced by the split parity of Clifford
multiplication: `J10` commutes with the four base gammas and anticommutes with
the ten normal gammas.  Setting

```text
R_split = diag(+1_BASE,-1_NORMAL)
```

gives

```text
[R_split tensor J10, Pi_RS] = 0,
Jhat^2 = -I.
```

Thus a claim that puts `J10` directly on the rolled `Omega1+Omega0` carrier
without `R_split` is mistyped.

## Principal operator

For the exact released-source-guided rolled symbol, the probe computes

```text
[sigma_D(e_a),Jhat] = 0       for a in BASE,
[sigma_D(e_a),Jhat] != 0      for every a in NORMAL.
```

The observed null control `e_0+e_7` also commutes exactly.  Therefore any
horizontal covector does by linearity.  This is a genuine observed-Lorentzian
complex-linearity theorem, but it is not an ambient ultrahyperbolic theorem.

The constant `Jhat` preserves the already-owned conditional local flat
observed `H^s` carrier.  A variable/global domain, an action-owned spatial
projector, the null BFV relation and the ambient `Y14` domain remain absent.

## Pairing compatibility

Let `B` and `B omega` represent the two current Spin-natural action-pairing
lines on spinors.  Exactly,

```text
J10^T B J10 = B,
Jhat^T (eta tensor B) Jhat = eta tensor B,
Jhat^T (eta tensor B omega) Jhat = eta tensor B omega.
```

This is the correct positive result for the current action pairings.  It must
not be transferred to the trace-owned Hermitian form.  For normal trace
`q_g`,

```text
J10^T B gamma(q_g) J10 = -B gamma(q_g),
```

so `J10` is an anti-isometry of `H_q=iB gamma(q_g)`, as the v0.194 correction
already records.

## Ordinary-gauge BRST obstruction

For all 91 Spin generators:

```text
[spin(BASE,BASE),J10]     = 0,
[spin(NORMAL,NORMAL),J10] = 0,
{spin(BASE,NORMAL),J10}   = 0.
```

This gives `51` commuting split generators and `40` noncommuting mixed
generators.  More importantly, the obstruction is present on the **actual**
selected background rather than only in the parent algebra.  Reconstructing
the exact source gauge map on the 196-cell `Cl1` bank gives

| selected gauge component | rank |
| --- | ---: |
| split-preserving | 17 |
| mixed, fixed-`J10` breaking | 8 |
| total | 25 |

Consequently, for a matter field `psi`,

```text
s(J10 psi) - J10 s(psi) = [c,J10] psi
```

is nonzero on an eight-dimensional active ghost image.  Fixed `J10` cannot be
an endomorphism of the ordinary-gauge quotient unless the gauge complex is
reduced to the split stabilizer by an independently owned mechanism.

When `J10` moves, the same calculation gives

```text
s(J10 psi) = [c,J10]psi + J10(c psi) = c(J10 psi).
```

This is exact covariance of the universal moving family, not descent of one
fixed member.

## Assessment of the Willmore/coherence hypothesis

The strongest defensible geometric hypothesis is narrower than

```text
D_varpi J=0 iff II_s=0 iff E[s]=0.
```

Three bridges are missing.

### 1. Raw versus horizontal-normalized second fundamental form

For an ambient Levi-Civita connection in an adapted frame, the mixed
Gauss--Weingarten block is the **raw** second fundamental form.  But the repo's
operative `II_s^H` subtracts a reference slice term.  Its own moving-frame
calculation gives, at the tautological LC section,

```text
II_s^raw = nonzero algebraic slice term,
II_s^H   = II_s^raw - II_s^ref = 0.
```

The commutator `[varpi,J10]` senses the mixed block of the connection supplied
to it.  It therefore detects raw `II` only under the ambient-LC/soldering
hypotheses; it does not automatically detect the reference-normalized
`II_s^H`.  To close the proposed equivalence one must construct a normalized
connection `varpi^H` and prove

```text
(varpi^H)_mixed = II_s^H,
D_{varpi^H}J10 = 0 iff II_s^H = 0,
```

with `varpi^H` also the connection used by the action and physical operator.

### 2. Action ownership and positivity

The released source supports a norm-square architecture but does not select
the repository's full `|II|^2` completion.  The fundamental curvature-linear
law and the geometric bending shadow remain separately typed.  Moreover the
normal DeWitt metric is indefinite on K77.  Without a positive majorant,

```text
|II_s^H|^2 = 0
```

does not imply `II_s^H=0`; a nonzero null tensor can have zero quadratic
density.  The older `E[s]>=0` assertion cannot be imported into this horn
without proving the relevant positivity.

The K3 endpoint is also not selective as stated.  The repo records
`E[s_g]=0` for every tautological LC section and says the functional is flat
in that metric direction.  Therefore the zero is not special to the K3 Yau
metric and does not by itself select one metric or topology.

### 3. Coherence versus a decoherence rate

Even if the normalized geometric equivalence is completed, it establishes a
compatibility/obstruction density.  A physical law

```text
Gamma_decoherence = lambda |II_s^H|^2
```

still needs a quantum state space, positive or Krein physical quotient,
coupling `lambda` with units, reduced/open-system dynamics, and an observable
visibility functional.  None is produced by a Willmore integrand alone.

Accordingly, the best steelman is:

> On a source/action-owned split-preserving normalized connection locus, the
> reflection-twisted `Jhat` could define a complex-linear symmetry of the
> observed physical operator.  A positive Willmore-type norm of the same
> normalized mixed intrinsic torsion could then measure departure from that
> coherence-compatible locus.

That is a strong, exact research program.  It is not yet a decoherence theory,
and the current fixed-`J10` gauge obstruction means the moving-reduction/BV
formulation is mandatory rather than optional.

## Next decisive gates

1. **Raw/normalized bridge.** Construct `varpi^H` and decide whether its mixed
   block is exactly `II_s^H`, including the nonzero reference slice term.
2. **Positive norm gate.** Classify the null cone of the K77 `II_s^H`
   quadratic form or supply an action-owned positive majorant.  Test whether
   zero energy really forces zero mixed obstruction.
3. **Moving-BV gate.** Extend the owned BV complex by the moving reduction
   field `J` and its stabilizer/ghost data, then compute whether `Jhat` acts on
   physical cohomology without fitting a gauge reduction.
4. **Closed-domain gate.** Only after gate 3, test the moving `Jhat` against
   the graded Green fixed locus and a variable/global closed observed domain.
5. **Rate gate.** Only after the physical quotient exists, derive rather than
   posit an open-system generator and its coefficient.

## Executable receipt

`tests/channel-swings/selected_k77_j10_bv_green_descent_gate_probe.py` passes
`112/112` exact, prior-art, Layer-0, Clifford, principal, pairing, gauge,
selected-image, moving-family, domain and scope checks.

No ledger row, verdict, residue, quotient, datum, canon claim or public posture
moves.
