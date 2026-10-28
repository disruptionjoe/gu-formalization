---
title: "K2177 Real scalar-square Clifford descent exclusion"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2177_exceptional_spectrum_descent_probe.py
---

# K2177 Real scalar-square Clifford descent exclusion

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
result: K2177 complete real scalar-square exclusion by tangent-grade separation
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

No nonzero REAL scalar-square mixed-even seven-form port satisfies the fixed
normalized descent equations. This closes the complete scalar-square class,
including mixed anticommutator grades, singular components and nilpotent cases.
Every remaining port in this fixed real class must have a nonscalar v² or u².
General mixed ports, changed geometry/reverse and complex extensions remain open.

The proof retains the real tangent-volume structure before complex encoding.
That separation settles the exceptional-spectrum question without a Jordan
classification. Homogeneous and commuting/anticommuting predecessor exclusions
are reused, not new results. The theorem is a necessary-filter exclusion, never
an existence theorem for surviving nonscalar candidates.

The carrier is full real Cl77 with fixed W(3,1)+N(4,6), REAL normal7 v and
normal3 u, t=Omega_W u, Omega_W²=-1, supplied common reverse, simple contraction
and normalized zero-order adapters. SC-OP-04 ASSERTS candidate four-field grammar;
SC-GEO-55 ASSERTS rotated-Levi-Civita displacement, neither selects these adapters.
No source/full16cell/full20/K-C, native2+1/chirality, physical quotient or global
claim follows. Source, ledger0.263, LT-SM8/LT-GR6b/AC-F1 and canon stay unchanged.
The real-form hypothesis cannot be dropped merely because the calculations can
be represented in complex Mat32. Perform the real tangent-degree split BEFORE
restricting to a normal-volume16-dimensional eigenspace, where the two real
subspaces can otherwise be identified. No positive spectrum or Hilbert form is assumed.

## Short universal closure of the remaining class

Let v²=a, t²=c be real scalars and x=(vt+tv)/2, y=(vt-tv)/2, U=K(x), J=y10, d=49a+225c, D=d-210x. [K2169](k2169-invertible-pencil-full-descent-2026-10-27.md) requires D invertible. [K2173](k2173-general-mixed-port-constraints-2026-10-27.md) and [K2175](k2175-mixed-grade-euler-localization-2026-10-27.md) give

E=f+(42c-1470a)x+182x²+(-49a-153c)y+392xy-8JD
  +U(126x-(49a+315c)/2+21y).

Every x,y,U,J has tangent degree4: it is Omega_W times a REAL normal Clifford element. Products of two have tangent degree0. These are independent real Clifford subspaces. The tangent-degree4 component is therefore

E4=A x-B U+beta y-8d J,
A=42c-1470a, B=(49a+315c)/2, beta=-49a-153c.

Normal reversion is even on x,U (grades4,8) and odd on y,J (grades6,10); the tangent volume reverses to itself. Taking reversion-even part yields the necessary equality

A x-B U=0.

Since U=2x4-6x8, its grade4 and grade8 parts are

(-1519a-273c)x4=0,
(-1323a+987c)x8=0.

If BOTH x4 and x8 are nonzero, the two scalar coefficients vanish. Their coefficient determinant is -1,860,432 (nonzero), so a=c=0.

At a=c=0, D=-210x is invertible, hence x invertible. The already established K2175 localization identities [U,x] (x-r)=[U,y] (x-r)=0, r=(a+9c)/6=0, force [U,x]=[U,y]=0. Thus the reversion-even part of E=0 is

182x²+126Ux=0,

and right multiplication by x^-1 gives 182x+126U=0. Its grade4 coefficient is 434 and grade8 coefficient is -574; hence x4=x8=0, contradiction. This excludes every remaining REAL scalar-square mixed-x candidate, without semisimplicity, invertible y, positive pairing, or spectral multiplicity assumptions.

Together with K2171 (x=0 or y=0) and K2175 (homogeneous nonzero x4 or x8), this closes the entire real scalar-square v/u class of these supplied adapters. General nonscalar squares are NOT excluded.

## Released rejection consumer and remaining work

For a supplied port, first check whether BOTH squares are scalar. If so, this
theorem rejects the full normalized fixed-adapter candidate before constructing
its ten inverse-pencil rows. If either square is nonscalar, the theorem supplies
NO rejection: use K2169's exact invertible-pencil and all-ten-row equations.
Thus a costly scalar-square parameter search can be removed from the frontier.

The exact probe exercises two actual real Clifford fixtures with both x4 and x8,
including the order-sensitive K2173 fixture and a decomposable three-tilt u.
It computes the tangent4 projection of the original ordered quartic, its
reversion-even projection and both normal-grade coefficients. It independently
constructs all ten original residual rows and checks their Euler contraction
against that quartic, then verifies that the new filter and original rows reject
these inputs. This is transfer verification; the finite fixtures do not prove
the universal theorem.

Seven genuine faults alter the linear x/U coefficients, tangent projection,
reversion parity, square-defect grade weight, cleared polynomial factor or
square-only elimination coefficient. The scalar-square hypothesis itself is
tested directly on the fixtures. The degenerate conclusion uses algebraic
invertibility and the previously proved localization identity, not a sampled
nilpotent search.

Run `tests/channel-swings/k2177_exceptional_spectrum_descent_probe.py` with the
repository SymPy environment; `--write` regenerates its report. The written proof
and actual artifacts receive independent internal review. This is not Lean,
external-expert or novelty certification.

## Further successor: correct nonscalar-square polynomial filter

The remaining square defects are tightly typed. A real normal3 or normal7 form
in dimension10 has square supported only in grades0 and4. Products of two
3-blades have grades0,2,4,6. Two7-blades have overlap at least4, so their products
have the same possible grades. Reversion makes either square even, eliminating
2 and6. This argument applies by bilinear expansion to nondecomposable forms.
Thus write V=v²=a+V4 and T=t²=c+T4. The scalar-square closure says a survivor
requires at least one nonzero4-form defect; it does not say those defects work.

For the separately supplied subclass [v,t]=0 set h=vt and U=K(h). Here h has
grades4/8, and K(V)=2V+8a, K(T)=2T+8c. The GENERIC K2171 Euler filter is AW-B,
with P=7v-15t, S=7v+9t, W=P^-1 S and

    A=60V-252T+(24a+216c)-348h-18U,
    B=780V+324T+(312a-648c)-60h-90U.

Scalars multiply the identity. If P is invertible, [P,S]=0 gives the exact
necessary-filter equivalence AW-B=0 iff AS-BP=0. Its two real tangent degrees are

    (AS-BP)_0=-504[(10V+16T+4a-12c)v+3Ut],
    (AS-BP)_4=  72[(142V+36T+68a-108c)t+7Uv].

U remains on the LEFT: no commutation of K(h) with v or t is presumed.
These two polynomial equations remove the inverse from this Euler test only;
they do not replace all ten descent equations. Substituting matrix-valued a,c
into the scalar-square quartic would be invalid because K weights the square
4-form defect by2, whereas the scalar part has weight10.

A further released necessary test eliminates K(h). Right-multiply the normalized
first equation by v and the second by t; subtract three times the second from
seven times the first. Since tv=vt=h, the21K(h)h terms cancel. Division by2 yields

    Q=35V²-157VT-54T²+(14a-42c)V+(-102a+162c)T=0.

This requires neither invertible v/t nor commutation of K(h) with either port.
V and T commute because v and t do. The scalar specialization is
49a²-301ac+108c², half the known K2171 scalar polynomial. Q is a cheap necessary
square-defect filter, never a sufficiency condition.

Take normal basis n1,...,n10 with the first four positive and set

    v=n1234567+(2/3)n1234589,
    u=n123+(1/5)n145.

Then [v,t]=0 and

    V=13/9-(4/3)n6789, T=24/25-(2/5)n2345.

Both squares are nonscalar, so the scalar-square theorem REFUSES applicability.
The separate generic polynomial and square-only filters reject this fixture.
The probe computes A/B independently through the existing generic Euler code,
checks both tangent projections, square-only elimination and the invertible
pencil, then verifies nine of ten original rows are nonzero with the expected
Euler contraction. This is a genuine next-class test, not a counterexample to
the exclusion or an exclusion of the whole nonscalar class.

The strongest next algebraic test is the nonscalar-square normal7/normal3 system
with genuinely shared original ten equations. A scalar-square approximation to
it cannot decide that problem. Moving splitting/Clifford geometry, mixed odd/even
ports, a different supplied reverse or native full operator remain distinct
alternatives with their own explicit input and observation obligations.
