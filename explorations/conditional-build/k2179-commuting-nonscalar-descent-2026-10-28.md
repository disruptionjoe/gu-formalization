---
title: "K2179 Homogeneous-product nonscalar Clifford exclusion"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2179_commuting_nonscalar_descent_probe.py
---

# K2179 Homogeneous-product nonscalar Clifford exclusion

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2179 commuting homogeneous-product nonscalar exclusion and mixed centrality filters
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

No real commuting normal7/normal3 port with homogeneous product h=vt in normal
grade4 or grade8 satisfies the fixed normalized descent equations, even with
nonscalar squares. The zero product is included. The proof exhausts the actual
32-dimensional algebraic multiplicities, including singular ports and Jordan
blocks. It does not assume positive spectra or invert the individual ports.

Every remaining commuting candidate must have BOTH product grades4 and8 and at
least one nonscalar square. Its grade components must commute with both ports;
new polynomial and trace constraints below are necessary only. Noncommuting
nonscalar ports, changed geometry/reverse, and the native full operator remain open.

The carrier is full real Cl77 with fixed W(3,1)+N(4,6), normal7 v, normal3 u,
t=Omega_W u, Omega_W²=-1, supplied common reverse, simple contraction and
normalized zero-order adapters. SC-OP-04 ASSERTS candidate four-field grammar;
SC-GEO-55 ASSERTS rotated-Levi-Civita displacement; neither selects these adapters.
Source/full16cell/full20/K-C, native2+1/chirality, physical quotient, ledger0.263,
LT-SM8/LT-GR6b/AC-F1 and canon do not move. This is conditional internal mathematics,
not a source falsification, novelty claim, or external-expert certification.

## Necessary equations and new centrality

Retain [K2177](k2177-exceptional-spectrum-descent-2026-10-28.md)'s real tangent
split BEFORE passing to complex matrices. Write

    V=v², T=t², a=<V>0, c=<T>0, h=vt, U=K(h),
    F=10V+16T+4a−12c, G=142V+36T+68a−108c.

For [v,t]=0 the denominator-cleared necessary Euler equations are

    Fv+3Ut=0,                  Gt+7Uv=0.                 (1)

Here P=7v−15t must be invertible by
[K2169](k2169-invertible-pencil-full-descent-2026-10-27.md).
Reversion fixes F,G,U and negates v,t. F,G already commute with both ports.
Reverse each equation and subtract to obtain [U,t]=[U,v]=0. Therefore
h4=(U+6h)/8 and h8=(2h−U)/8 commute with both ports. This is a necessary
consequence of(1), not an automatic identity of commuting forms.

## Complete homogeneous-product exclusion

If h is homogeneous, U=k h with k=2 or−6. Equation(1) becomes

    (10V+(16+3k)T+4a−12c)v=0,
    ((142+7k)V+36T+68a−108c)t=0.                         (2)

Complexify the normal Clifford algebra faithfully as Mat32(C) and represent
Omega_W by i. Scalar extraction equals normalized trace: every nonidentity
normal blade has zero trace by conjugating with a suitable normal generator.
Thus tr(V)=32a and tr(T)=32c. This uses the FULL32 representation, never a
16-dimensional volume eigenspace. The real tangent projections establishing(1)
were made before this encoding. No Hilbert positivity is invoked.

Commuting complex matrices v,t are simultaneously upper triangularizable:
a common eigenspace of one is invariant under the other and has a common
eigenvector; induction on the quotient supplies a full common flag. Let the
paired diagonal entries be lambda,mu and put r=lambda²,s=mu². Since P is
invertible,7lambda−15mu is never zero. Every diagonal position belongs to
exactly one case:

| Case | r | s |
| --- | --- | --- |
| mu=0, lambda nonzero | (−2a+6c)/5 | 0 |
| lambda=0, mu nonzero | 0 | −17a/9+3c |
| both nonzero, k=2 | (−169a+243c)/384 | (7a+99c)/384 |
| both nonzero, k=−6 | −a/2+81c/70 | −a/2−3c/14 |

The two mixed-system determinants are−3072 and560, respectively. Let m,n and
32−m−n be the integer algebraic multiplicities of the first, second and mixed
cases. Averaging the table must reproduce(a,c). The determinant of this
normalized2×2 trace system is

    k=2:  (32mn+329m−2935n+32480)/30720,
    k=−6: (mn−30m−132n+2304)/960.                       (3)

Neither numerator in(3) can vanish. For k=2, reduction modulo32 gives
9(m+n)=0 modulo32, so m+n is0 or32. The zero sum gives32480. Substituting
n=32−m gives−32(m²−134m+1920); its discriminant is4·2569, and
50²<2569<51², so there is no integer root. For k=−6, a zero requires
(132−m)(30−n)=1656=23·72. The first factor lies in[100,132]. Any divisor
there must contain23 (otherwise it divides72); writing it23e forces e=5,
which does not divide72. Thus no integer multiplicities work.

The exact probe additionally enumerates ALL561 pairs for each case,
independently constructs the rational trace matrix, and verifies(3). The
minimum absolute determinants are21/10240 and1/240. Its report retains all1122
integer numerator rows. This exhaustive transfer control supplements the
arithmetic proof; it is not numerical sampling.

Consequently a=c=0. Every row of the table now gives r=s=0, hence lambda=mu=0
over C, contradicting invertibility of P. Jordan blocks do not escape: they
would leave P strictly upper triangular and nilpotent. Neither v nor t was
individually inverted. Together with K2177, all remaining commuting candidates
need nonscalar squares AND a genuinely mixed h4+h8 product.

## Released mixed-product polynomial consumer

On any surviving commuting candidate, all of v,t,U,F,G commute. Eliminate
between(1): (FG−21U²)v=(FG−21U²)t=0. Multiplying the combination7v−15t by
its inverse gives the new necessary matrix identity

    FG=21U².                                            (4)

Also FV+3Uh=0, GT+7Uh=0. Their linear combination reproduces K2177's square
filter

    35V²−157VT−54T²+(14a−42c)V+(−102a+162c)T=0.          (5)

This supplies a division-free rejection consumer before the ten full rows.
It is NOT sufficient: Clifford grade support, off-diagonal equations, P
invertibility and every original descent row remain required.

In a common triangularization of v,t,U let nu be U's diagonal entry. With
A=10r+16s+4a−12c and B=142r+36s+68a−108c, the remaining spectral conditions are

    A lambda+3nu mu=0, B mu+7nu lambda=0,
    AB=21nu², nu lambda mu=−Ar/3=−Bs/7,
    sum r=32a, sum s=32c, sum lambda mu=0, sum nu=0.

The last two traces vanish because h,U have no scalar normal grade. These
are necessary constraints with integer algebraic multiplicities, not an
existence certificate or a class exhaustion of the mixed case.

## Transfer controls and hostile counterconstruction

The probe uses real normal basis n1,...,n10 (first four positive) and exact
Clifford multiplication. Two nonscalar fixtures have homogeneous h and an
invertible pencil:

- grade4: v=n1234567+(2/3)n1234589, u=n123;
- grade8: v=I_N(n123+(2/3)n145), u=n124.

Both pass the class hypotheses and fail the actual Euler and original ten-row
conditions. A third fixture v=I_N n123,
u=n124+(1/3)n567+(1/5)n589 has nonscalar T and mixed h4+h8. The homogeneous
theorem refuses applicability. Its nonzero [U,t] violates the new centrality
condition and its original rows independently reject it. This demonstrates
that the centrality consumer is substantive, not true by construction.

Continuous spectral weights would invalidate the finite proof. For k=−6,
weights m/32=0,n/32=6/11 and mixed weight5/11 solve trace closure with a=3,c=7:
the pure-T square is46/3 and mixed squares are33/5,−3. This abstract spectral
relaxation is not a Clifford solution and cannot have denominator32. It also
shows why replacing real/complex squares by positive numbers is invalid.

Genuine equation/data mutations change grade weight, mixed coefficients,
trace dimension, polynomial coefficient, reversion sign and original-row
contraction. The clean baseline passes before each fault is required to fail.
Exact fixture checks supplement the universal argument; they do not prove it.

## Reproduction and remaining frontier

Run `tests/channel-swings/k2179_commuting_nonscalar_descent_probe.py` with SymPy;
`--write` regenerates the dependency-hashed JSON report. Independent internal
review reconstructs the proof and inspects actual notes/probe/report. No
proof-assistant or external acceptance is claimed.

The next algebraic question is a genuinely mixed h4+h8 nonscalar candidate
satisfying centrality,(4),(5),trace conditions and all ten original equations.
Noncommuting nonscalar squares require a different ordered reduction. Moving
geometry and a changed reverse are distinct hypotheses, not rescues of this
excluded class. Do not repeat a scalar-square or homogeneous-product search.

Simultaneous triangularization is standard; see Pryde,
[Algebras of matrices](https://maths.anu.edu.au/files/CMAProcVol20-Pryde.pdf).
That fact does not establish the adapter-specific coefficients or Clifford
transfer above; the explicit proof and rational certificate carry those burdens.
