---
title: "K2217 Entire Spin orbit of the prescribed adapter excluded"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-K2217-SPIN-ORBIT-Y0
claim_ceiling: entire genuine Spin04_6 conjugacy orbit excluded; arbitrary similar matrices and general noncommuting adapters remain open
scripts:
  - tests/channel-swings/k2217_spin_orbit_adapter_exclusion_probe.py
---

# K2217 Entire Spin orbit of the prescribed adapter excluded

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2217 Entire Spin orbit of the prescribed adapter excluded
carrier: real Cl46 grade coefficients on auxiliary complex normal spinor32 with both complex chiral16 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: alternating reconstruction form and Clifford trace ON=declared_carrier
real_structure: real grade coordinates; quaternionic bar exchanges chiral halves
grading: normal grade3 and grade7; not physical chirality
action_owner: repository-construction -- conditional supplied operator or instrument
target: real nonsingular prescribed-factor reconstruction MAP-TYPE=intertwiner
```

## Result

Let G=Spin_0(4,6), acting in the fixed normal Clifford algebra, and let
(w0,u0,Y0) be the exact [K2214](k2214-prescribed-adapter-fibers-2026-10-28.md)
fixture. For every g in G, all real nonsingular grade3/7 ports realizing
Yg=gY0g^-1 are exactly

    (w,u)=c(Ad_g w0,Ad_g u0),  c in R, c!=0.           (1)

Every one fails the necessary ordered Euler contraction and hence the full
ten original equations. The factor orbit has real dimension45, and the
union of reconstructed ports has dimension46 after nonzero real scaling.
These dimensions do not assert a globally unique parameter g: discrete
stabilizers and central redundancies may remain.

Verdict against `INTERNAL-K2217-SPIN-ORBIT-Y0`: **excluded**. This is not an
exclusion of every similar or isospectral factor, let alone all GU adapters.

## Covariance and complete-fiber proof

Spin conjugation preserves real Clifford grades, normal volume I_N, the
metric contraction K(X)=sum eta_j gamma_j X gamma_j, and quaternionic bar.
The group is even and therefore preserves both chiral halves; bar exchanges
them with the inherited real relation. Transporting a realization of Yg back
by g^-1 gives a realization of Y0. The COMPLETE real kernel theorem of K2214
then forces the transported port to equal c(w0,u0). Conversely every such
scaled transported port realizes Yg. This proves (1), not just containment.

K2214's Euler coefficients A,B are ordered quadratic polynomials in the
original v=I_N w, t=i u and their bars, including K. Hence

    E(v,t,Y)=4 A(v,t)Y-(5 B(v,t)-A(v,t)),
    E(c Ad_g v0,c Ad_g t0,Yg)=c² Ad_g E(v0,t0,Y0)!=0.   (2)

The nonzero K2214 rational residual is reused with pinned dependency bytes.
Its rank119 proof need not be repeated for each group element. Nonzero
conjugation cannot turn this residual into zero. This disposes an entire
continuous family without an unrestricted nonlinear solve.

For clarity, the original row law retains the metric placements. If
Ad_g gamma_j=sum_i L_ij gamma_i, then L^T eta L=eta. The contraction ports
transform with L^-1, while the unique adapters and final reduced original
residuals transform with L:

    T'_j=sum_k L_jk Ad_g T_k,
    q'_j=sum_k L_jk Ad_g q_k.                          (3)

Indeed T_j=-eta_j P^-1 port(R)_j, and
eta_j (L^-1)_kj eta_k=L_jk. The full raw maps are compositions of Clifford
multiplication, contraction and the same lower return, so this establishes
covariance of all ten original equations, with their upper rows retained by
the existing exact gamma-lower identity. No equation is replaced by its trace
for accepting a solution; the necessary contraction is enough for rejection.

## Exact orbit dimension

Use the ten normal labels of K2214, signature++++------. In lexicographic
bivector coordinates the map

    X -> ([X,w0],[X,u0])

is a240-by45 integer matrix: each output has120 ordered triple coordinates.
The probe rebuilds it from Clifford products. Its stated45-square minor has
determinant893116 modulo the prime1000003. The row indices and complete
certificate are in [the report](../../lab/process/k2217-spin-orbit-adapter-exclusion.json).
A nonzero modular minor proves real rank45; no floating rank threshold occurs.

If X stabilizes Y0 infinitesimally, its one-parameter subgroup preserves Y0.
The complete one-dimensional fiber implies Ad_exp(tX)(w0,u0)=c(t)(w0,u0).
The scalar components of w0² and u0² are respectively -38 and -208; scalar
parts are conjugation-invariant. Thus c(t)²=1, and near t=0, c(t)=1.
The pair-stabilizer rank forces X=0. Therefore the Y0 stabilizer Lie algebra
is zero and its orbit has dimension dim Spin(4,6)=45. The scaling tangent is
independent of the orbit by the same scalar-square argument, giving46.
The scalar parts are not claims that these full squares are scalar.

## Countercontrols, evidence and scope

The rational rotation g=(3+4 gamma1 gamma2)/5, boost
h=(5+3 gamma1 gamma5)/4, and hg test metric, grades, bar, volume and ordered
A,B covariance on the ACTUAL w0,u0. Original all-ten raw residual and unique
adapter covariance are recomputed independently on a smaller invertible
fixture; this is a control of the general law, not a claim that every arbitrary
port was enumerated. Signed nonunit scales test quadratic homogeneity.
An even invertible matrix 1+(gamma1 gamma2 gamma3 gamma4)/2 fails vector-grade
preservation; arbitrary real even or GL similarity is not allowed by (1).

Baseline-first faults duplicate a rank-minor row, invert the row transport,
change the normal metric, or corrupt an ordered Euler coefficient. Each must
fail a genuine coefficient or rank check. Universal proof, finite controls
and unchanged inherited fiber evidence are distinct. No external-expert,
proof-assistant or literature-novelty certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-GEO-55 ASSERTS displacement
from rotated Levi-Civita. These statements neither select this normalized
adapter nor promote its internal Spin action to physical source gauge symmetry.
Ledger0.263, source assertions and canon remain unchanged. Future construction
must leave this orbit, not rotate or rescale the same failed port. General
noncommuting factors, other Clifford-real-form positions and changed principal
or return constructions remain open.
