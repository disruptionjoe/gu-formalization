---
title: "K77 I1B gauge-invariant mixed-residue selector wave"
status: active_research
doc_type: reverse_scaffold_i1b_cross_null_gauge_invariant_selector_result
date: 2026-09-01
claim_ceiling: exact gauge-invariant coefficient-identifiability classification for the local two-dimensional I1B mixed-residue normal form; no source-owned cross-null tensors, physical bundle, prediction, confirmation, or GU verdict
manifest: lab/process/k77-i1b-gauge-invariant-mixed-residue-selector-wave.json
probe: tests/channel-swings/k77_i1b_gauge_invariant_mixed_residue_selector_probe.py
---

# K77 I1B gauge-invariant mixed-residue selector wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: gauge-invariant decision-power classification for the I1B trace-free cross-null residue and mixed-curvature selector
carrier: real degenerating Darboux two-plane inside the native rank-24 to rank-22 I1B Green quotient jump LAYER=conditional CHIRALITY=N/A
pairing: J_u=uJ_2 with an H-oriented tangential splitting and punctured-stratum compatible connection ON=native_rank_changing_normal_form
real_structure: real two-dimensional symplectic endomorphisms
grading: scalar trace residue plus trace-free sp(2,R) residue; not a BV-BFV grading
action_owner: native ranks are source-adjacent I1B data; C, M, H and the invariant selector theorem are repository-derived unless independently supplied
target: coefficient magnitude and sign in M=a[C,H] modulo the H-preserving symplectic stabilizer MAP-TYPE=classification
```

## Coordinate equation and its gauge seam

On the degenerating plane the prior packet writes

```text
R=-I_2/2+C,       C=[[p,q],[r,-p]],
H=diag(1,-1),     D=[C,H]=[[0,-2q],[2r,0]],
M=aD.                                                   (1)
```

The coordinate ratios `a=-rho/(2q)=sigma/(2r)` are exact when the named rows
are nonzero, but `q,r,rho,sigma` are not individually invariant. For every
nonzero real `s`, the `H`-preserving symplectic change of frame

```text
G_s=diag(s,s^-1)
```

sends

```text
q -> q/s^2,   r -> r s^2,
rho -> rho/s^2,   sigma -> sigma s^2.                 (2)
```

Thus no single off-diagonal coordinate is physical data without an owned
trivialization. The full tensor equation `M=aD` is equivariant, and the row
ratios survive because numerator and denominator carry the same weight.

## Nonnilpotent horn: an invariant magnitude selector

When `q r!=0`, the commutator is nonnilpotent and

```text
tr(D^2)=-8 q r !=0,
tr(M^2)=a^2 tr(D^2).                                  (3)
```

Therefore

```text
a^2 = tr(M^2)/tr(D^2).                                (4)
```

Equation (4) is invariant under every simultaneous conjugation of `C,H,M`,
not merely the diagonal stabilizer. It removes the unowned basis scale and
distinguishes the positive candidates `log(2)` and `log(3)` whenever `C,H,M`
are independently owned and satisfy (1). If the measured ratio matches
neither squared candidate, both are rejected in this normal form.

The trace ratio selects magnitude only. A signed coefficient additionally
uses the oriented tensor equation `M=aD`, or equivalent owned coorientation.
This sign ceiling does not obstruct the present positive `log(2)` versus
`log(3)` comparison.

## Nilpotent and commuting horns

If exactly one of `q,r` is nonzero, then `D!=0` but `D^2=0`. The trace ratio is
`0/0` and has no decision power. Nevertheless the full owned tensors still
identify a unique scalar through `M=aD`; any nonzero component or linear
functional on the one-dimensional span gives the same `a`, and simultaneous
`H`-stabilizer scaling cancels. A scalar trace-only summary loses this
information.

If `q=r=0`, then `D=0` and compatibility forces `M=0` for every `a`. This
commuting horn cannot select either magnitude or sign. The forced scalar
residue, diagonal trace-free coordinate `p`, determinant matching and bounded
mixed curvature all remain nonidentifying.

## Ownership theorem and hostile review

The selector requirement is now basis-free:

1. independently own the tangential splitting `H`, trace-free residue `C`, and
   mixed residue `M`;
2. verify the tensor equation `M=a[C,H]` rather than matching one row in a
   chosen frame;
3. use (4) in the nonnilpotent horn, full tensor proportionality in the
   nilpotent horn, and report nonidentifiability in the commuting horn; and
4. own an orientation only if the sign of `a` matters.

The strongest overclaim would call the invariant formula source-selected; no
current source packet supplies `C,H,M`. The strongest contrary construction is
the commuting horn, where every coefficient survives. The weakest
reproducibility seam is collapsing a nilpotent tensor equation to polynomial
traces and incorrectly reporting no selector.

This packet does not create a physical cross-null connection or bundle. It
states the exact gauge-invariant data a future source/action evaluation must
return. With those tensors, the positive `log(2)`/`log(3)` alternative becomes
decidable; without them, both remain repository-owned controls and no held-out
credit follows.
