---
title: "Selected-K77 SR-1D affine first-jet parity exhaustion"
status: active_research
doc_type: exact_class_obstruction
created: "2026-08-14"
registry: lab/process/selected-k77-sr1d-affine-first-jet-parity-exhaustion.json
probe: tests/channel-swings/selected_k77_sr1d_affine_first_jet_parity_exhaustion_probe.py
grade: "EXACT LOCAL FORMAL FIRST/TWO-JET CLASS KILL OVER FIXED CANONICAL POINT CARRIER"
canon_verdict_change: none
---

# Selected-K77 SR-1D affine first-jet parity exhaustion

## Result first

The apparent distinct-first-jet reopener inside the canonical SR-1C affine
solve is closed. Both exact point branches are killed across the **complete
affine first-jet fibre and every compatible second jet**.

The action/Bianchi solve did not select a unique symmetric correction. It
selected

```text
Q = Q0 + k,                 k in ker S,
dim ker S = 5,265,
```

where `Q0` is the sparse thirteen-cell representative and `S` is the exact
`5,292 x 9,555` action/Bianchi matrix of rank `4,290`. SR-1D varied every
second jet over `Q0` but correctly left open whether a nonzero `k` could alter
the affine base of `j1(E_B-E_T)`.

It cannot. The obstruction is Clifford parity and holds on the entire
`1,274`-dimensional directionwise grade-two carrier before imposing `k in ker
S`.

## The parity theorem

A first-jet shift differentiates the connection translation into

```text
X = D_m(delta T) in Omega^1(Cl2),
```

so `X` is Clifford-even. The fixed point value `T=t Phi1`, the dual variation
`U`, and the `Lambda^13 Cl1` Euler receiver are Clifford-odd. Clifford product
adds parity, selected Shiab flips it, and Hodge preserves it. Consequently:

```text
direct:       S(XT+TX)       is even -> zero in the odd receiver,
Hodge:        *X             is even -> zero in the odd receiver,
adjoint half: <X,S(UT+TU)>   is even paired with odd -> zero,
adjoint half: <T,S(UX+XU)>   is odd paired with even -> zero.
```

Thus both `j1E_T` and `j1E_B` receive zero affine correction, and therefore

```text
delta_k j1(E_B-E_T) = 0
```

for every grade-two first-jet shift—not merely every action/Bianchi-compatible
shift. As an implementation-level check, the probe evaluates all
`1,274 x 196 = 249,704` direct coefficients and the same number of Hodge
coefficients; both supports are exactly zero. The previously owned complete
same-grade `Cl2` theorem independently gives rank zero on positive, negative
and null representatives. An excluded Clifford-odd amplitude derivative
fires fourteen Euler rows, so the differentiator itself is live.

## Joint first- and second-jet exhaustion

The thirteen-cell base already has

```text
j1E_T = j1E_B = j1(E_B-E_T) = 0.
```

The parity theorem says every `Q0+k` has the same zero affine base. For an
arbitrary second-jet correction `h`, SR-1D then supplies

```text
j1E_T = A h,
j1E_B = 2 A h,
j1(E_B-E_T) = A h.
```

Differentiated translation stationarity requires `A h=0`. Hence the complete
compatible first/two-jet fibre has zero momentum jet, zero primitive-epsilon
return and rank-zero fixed-`varpi` metric graph image. The already-computed
rank-one density trace

```text
(33703t/468-3/52)(1,0,0,0,-1,0,0,-1,0,-1)
```

is nonzero on both roots of `28392t^2+91t-351`. Both fixed canonical point
branches therefore fail total metric stationarity throughout the whole class.

## What was and was not exhausted

This closes all first- and second-jet freedom inside

```text
T=t Phi1,
F_B=F_BZ,
DT=-F_BZ+(-t/312-t^2)C+Q,
Q in Q0+ker S.
```

It does not classify a new point value of `T`, a nonhomogeneous carrier, a
different canonical connection, or a source-derived reconstruction. Those
changes can alter the parity types or the inhomogeneous metric row and require
a fresh point/action/Bianchi/source solve.

## Reverse-scaffold consequence

SR-1E must cross the point-carrier boundary. The strongest current branch
generator is the exact source instability, but its independent ownership gate
shows that it still lacks the source-to-K77 carrier bridge. The next swing is:

```text
construct the equivariant source 450D to selected-K77 1274D carrier map;
select and stabilize one source-owned nonlinear critical orbit;
lift it to a labelled canonical-B_Z compatible first jet;
then recompute translation, Bianchi, primitive epsilon and the total
fixed-varpi metric row on that same carrier.
```

No further kernel search inside the exhausted SR-1C affine family has value.
SR-1 remains `BACKGROUND-MISSING`, SR-2 remains blocked and VRS-6 lacks a
stationary-background premise. No ledger, canon, residue, quotient datum or
public posture changes. No physical cohomology, superposition law, Born rule,
spectrum or empirical prediction follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_sr1d_affine_first_jet_parity_exhaustion_probe.py
```

The exact probe passes `43/43`.
