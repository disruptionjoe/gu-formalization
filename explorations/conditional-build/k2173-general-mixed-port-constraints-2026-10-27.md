---
title: "K2173 Noncommuting scalar-square mixed-port constraints"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2173_general_mixed_port_constraints_probe.py
---

# K2173 Noncommuting scalar-square mixed-port constraints

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
result: K2173 quartic Euler filter and homogeneous anticommutator/commutator class exclusion
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

A genuinely new mixed class is excluded: let the normal seven-form v and three-form
u have scalar squares, set t=iu, and require the nonzero anticommutator x=(vt+tv)/2
to have one grade, 4 or 8, and the nonzero commutator y=(vt-tv)/2 to have one grade,
6 or 10. No such pair passes the complete normalized descent equations. **The
commutator may be singular or nilpotent.** Neither commuting nor anticommuting
is assumed; those previously excluded classes are reused from K2171.

For arbitrary scalar-square pairs the full Euler filter reduces to a degree-four
noncommutative polynomial, plus a cheap scalar invariant. These are necessary only;
a survivor still owes all ten K2169 rows. General nonscalar-square ports, or
scalar-square pairs with mixed grades in x or y, remain OPEN. This is not all-port
exhaustion. The fixed conditional Cl77, W(3,1)+N(4,6), normalized zero-order adapters,
common reverse and simple contraction are unchanged. No fixed-geometry derivative
repair is reopened.

SC-OP-04 ASSERTS candidate four-field operator grammar, not this reverse/contraction.
SC-GEO-55 ASSERTS gauge-rotated Levi-Civita displacement. Full source16cell/full20/K-C,
native2+1/chirality, moving geometry, physical quotient and global domains remain
separate debts. LT-SM8/LT-GR6b/AC-F1, source polarities, ledger0.263 and canon do not
move. Layer0 retains the full real Dirac carrier and algebraic evaluation, with no
positive physical pairing or source mechanism inferred. No novelty claim.

## 1. Central algebra and the quartic filter

Work in D=Cl(N)_C≅Mat32(C), representing tangent volume by i as in K2169. Let
v²=aI, t²=cI, where a,c are real scalars (t=iu includes its i² sign). Define

    x=(vt+tv)/2, y=(vt-tv)/2, P=7v−15t,
    D0=P²=(49a+225c)I−210x.

Here D0 is a matrix, not the Clifford algebra D. The scalar-square relations imply
x commutes with v,t,y, y anticommutes with v,t, and y²=x²−acI. P is invertible for
any nonzero descent candidate by K2169, hence D0 is invertible. There is no need
to invert v, t or y.

Reversion of seven- and three-forms is negative, so x has only grades4,8 and y has
only grades6,10. Reuse K(z)=sum eta_j gamma_j z gamma_j. Substitution in K2171 gives

    A=(84a−36c)I−348x−168y−18K(x),
    B=(1092a−324c)I−60x+264y−90K(x)+144K(y),
    P⁻¹S=[(49a−135c)I−42x+168y]D0⁻¹.

Keep matrix product order. The original Euler residual is

    AW−B=−144 E D0⁻¹,
    E=fI+(42c−1470a)x+182x²+(49a+297c)y−28xy
       +K(x)[126x−(49a+315c)I/2]+21K(x)y+K(y)D0,
    f=343a²+1491ac−540c².                         (1)

Every term in E is homogeneous degree4 in the original v,t. This is a cheaper
necessary rejection filter within the scalar-square class, not a replacement for
the full general-port degree65 criterion or the ten rows.

The scalar part tau is normalized ordinary matrix trace in Mat32(C). Orthogonality
of different Clifford grades gives the further necessary condition

    f+434 tau(x4²)−574 tau(x8²)=0.                (2)

No positivity follows: these scalar squares are indefinite in Cl(4,6). Mixed-grade
products and K(y)D0 have zero scalar projection by grade, not by a positive norm.

## 2. Excluding all homogeneous x/y pairs, including singular y

Suppose K(x)=kx, K(y)=ell y, with k∈{2,−6}, ell∈{−2,−10}, and x,y nonzero.
Since x commutes with y, reversion separates E into its even and odd parts:

    g(x)=0, (beta+gamma x)y=0,
    g(X)=delta X²+alpha X+f,
    delta=182+126k,
    alpha=42c−1470a−k(49a+315c)/2,
    beta=49a+297c+ell(49a+225c),
    gamma=−28+21k−210ell.                        (3)

The four gamma values are434,2114,266,1946, all nonzero. Set r=−beta/gamma.
Then (x−r)y=0; multiplication by g(x) shows g(r)y=0, hence g(r)=0 because y≠0.
Also y²=x²−acI gives

    (x−r)(x²−acI)=0.                             (4)

If r≠0, trace(x)=0 forces some complex eigenvalue s≠r: if r were the sole eigenvalue,
its trace would be32r even for a nondiagonalizable matrix. Equations(3),(4) imply
s²=ac and g(s)=0. Therefore both scalar polynomials must vanish:

    H=gamma²g(r), R=(f+delta ac)²−alpha²ac.        (5)

For c≠0, set q=a/c. The exact roots of H/c² and the corresponding nonzero values
of R/c⁴ are:

| k | ell | roots q | R/c⁴ at roots |
|---|---|---|---|
|2|−2|27/49, −585/98|−14134824/49, 361994993595/784|
|2|−10|−585/98, 2055/1309|361994993595/784, −20714624615880/1222830961|
|−6|−2|−495/49, 69/343|133077012480/49, 1434356568/117649|
|−6|−10|−495/49, 1245/1351|133077012480/49, 424482009302520/1387488001|

When c=0, H is respectively33345088a²,201146176a²,5647152a²,51900016a², so a=0.
Then r=0, contradicting the current case. Thus r≠0 is impossible.

If r=0, beta=f=0. For ell=−2, beta=0 implies a=−153c/49 and
f=−12960c²/7. For ell=−10, a=−217c/49 and f=−416c². In either case a=c=0.
Then g(x)=delta x²=0, but D0=−210x must be invertible, a contradiction.
This proves the class exclusion without diagonalizability, definiteness or invertible y.

## 3. Original-row controls and the genuinely singular consumer

Use normal basis n1,...,n10, first four positive. The family

    v=n1234567, u=A n123+B n458, A B≠0

has scalar squares and homogeneous nonzero x4,y6, so ALL amplitudes are excluded
by the theorem, not sampled amplitudes. More decisively take

    v=n1234567, u=n123+(n4+n5)n6n8.

Here a=c=1, x is pure grade4 with x²=I, and y is nonzero pure grade6 with y²=0.
The pencil square D0=274I−210x is invertible (possible eigenvalues64,484).
Thus the new theorem excludes a case where neither the old commuting/anticommuting
argument nor the singular-pencil filter settles the candidate. The exact probe
constructs the ORIGINAL ten kernel rows for these fixtures and a third mixed-grade
x4+x8/y6 fixture with noncentral K(x), and matches their Euler
contraction to(1); it verifies nonzero full residuals, not just the new formula.

## Reproducibility and remaining work

Run `python tests/channel-swings/k2173_general_mixed_port_constraints_probe.py` in
the repository SymPy environment; `--write` regenerates its JSON. Fifty-two exact controls
cover original rows, noncommutative products, scalar projection, reversion and the
complete projective polynomial certificate. Five actual coefficient/contraction
faults fail specific checks after a green baseline. Independent review reconstructed
the universal algebra and spectral proof; these finite controls alone are not the
universal proof. The report pins dependencies and probe bytes.

Next genuinely remaining scalar-square candidates, not already excluded by K2171, must mix grades4+8 in x or
6+10 in y. General nonscalar-square v/u are also open. Apply(1)/(2) first and all
ten qj to every survivor. A classification of the full mixed-grade algebra needs
new constraints; it cannot inherit the homogeneous proof. Moving splitting/Clifford
geometry, odd/even mixtures and changed reverse remain distinct constructions.
No source, physical recovery, proof-assistant or external-expert verdict is claimed.
