---
title: "Primary papers for quantum positivity and scalar sector closure"
status: active_research
doc_type: primary_source_pack
created: 2026-10-07
source_grade: primary_preprints
source_return: EXTERNAL_LITERATURE
target_claim: NONE-NOT-A-KILL
claim_ceiling: primary literature and conditional transfer diagnostics only
download_receipt: lab/sources/quantum-positivity-primary-pack-2026-10-07.json
canon_verdict_change: none
---

# Primary papers for quantum positivity and scalar sector closure

Anderson, Bateman, Herzog and Turok's August 2026 paper supplies the
renormalization calculation previously announced in the July Bateman–Turok
intake. It gives an exact scalar coefficient test and an off-shell infrared
argument. Positive on-shell loop probabilities remain a separate problem.
The strongest immediate GU use is to test whether an action-owned scalar
sector has the required interaction grammar and closes under the complete
equations. The October 5 revision of a BRST composite-observable paper and a
ghost-bound-state spectral calculation supply narrower observable diagnostics.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: primary-source intake and conditional positivity transfer diagnostics
carrier: external four-derivative scalar, SU3 quartet and conjugate-mass composite carriers LAYER=toy CHIRALITY=N/A
pairing: indefinite scalar Wightman form and separately tested composite spectral form ON=each_named_external_model
real_structure: real dipole scalar; independent complex quartet fields with prescribed contour; conjugate scalar masses
grading: hidden scalar ghost parity or BRST ghost degree, with no identification between them
action_owner: comparator -- the named external authors; no equality to native I1B, I2B or observed full-II established
target: scalar coefficient and normal-Euler closure tests; no transfer map to GU yet constructed MAP-TYPE=not-a-map
```

## Verified source intake

| Exact source | Relevant primary inspection | Versioned source PDF |
| --- | --- | --- |
| Maegan Anderson, Sam Bateman, Franz Herzog and Neil Turok, **On divergences in a four-derivative scalar field theory**, [2608.12210v1](https://arxiv.org/abs/2608.12210v1), August 12, 2026 | Sections 2–5, 6.3 and 7; PDF, HTML and relevant original TeX | [PDF](https://arxiv.org/pdf/2608.12210v1), 28 PDF pages |
| Sam Bateman and Neil Turok, **Escape from Ostrogradsky via Hidden Ghost Parity**, [2607.00096v1](https://arxiv.org/abs/2607.00096v1), June 30, 2026 | Sections I, II, IV–VI and the asymptotic-map appendix | [PDF](https://arxiv.org/pdf/2607.00096v1), 6 PDF pages |
| M. M. Amaral and V. E. R. Lemes, **Background-Equivariant BRST Observables and i-Particle Propagators from an Auxiliary Quartet in SU(3) Yang-Mills**, [2605.16172v2](https://arxiv.org/abs/2605.16172v2), revised October 5, 2026 | Revised action/background scope and Sections 8–10 | [PDF](https://arxiv.org/pdf/2605.16172v2), 33 PDF pages |
| Manuel Asorey, Gastão Krein, Miguel Pardina and Ilya L. Shapiro, **Reflection positivity in a higher-derivative model with physical bound states of ghosts**, [2511.15283v1](https://arxiv.org/abs/2511.15283v1), November 19, 2025 | Sections 2–5, including the subtraction, continuum density and bound-state pole | [PDF](https://arxiv.org/pdf/2511.15283v1), 16 PDF pages |

Exact URLs, versions, byte counts, SHA-256 hashes and retrieval times are in
the [download receipt](quantum-positivity-primary-pack-2026-10-07.json).
The PDFs retain their source licenses and follow the repository's existing
`*.pdf` ignore rule. The receipt and this scope record provide durable custody;
the PDF links above resolve to the exact source versions without adding the
downloaded papers to the contribution.

## Scalar relations that can be tested exactly

In Anderson et al.'s convention, put `Q=Box(sigma)` and `X=(partial sigma)^2`.
PDF equation **2.3** is

```text
L = -Q^2/2 + lambda3 X Q + lambda4 X^2        modulo boundary terms.
```

The perfect-square branch is `lambda3=-lambda` and
`lambda4=-lambda3^2/2` (PDF **5.1**). The counterterm identities are
`Z3 sqrt(Zsigma)=Z4 Zsigma=1`, equivalently
`Z1=Z2=Zsigma` and `Z4=Z3^2=1/Zsigma` (PDF **5.8** and Section **6.3.1**).
They are checked through three loops. The gravitational all-order explanation
is attributed to a companion still listed as in preparation. Section 4's
infrared proof uses nonexceptional off-shell momenta and the soft momentum
factors of every interaction leg. Section 7 explicitly leaves on-shell soft
and collinear treatment to a future inclusive/resummed analysis.
[Primary full text](https://arxiv.org/html/2608.12210v1).

Repository-derived diagnostic, for a fixed complete scalar operator basis:

```text
L = a Q^2 + b Q X + c X^2,    a != 0
perfect-square condition:    4 a c - b^2 = 0
square parameter:            lambda = b/(2 a)
RG tangency in normalized conventions:
                            beta4 + lambda3 beta3 = 0
                            on lambda4 = -lambda3^2/2
```

The discriminant tests coefficient factorization. It does not test omitted
operators, field-dependent coefficients, the sign of the physical pairing,
normal equations, or the functional domain. Its normalization must include
the paper's explicit loop factors before comparing beta coefficients.

Section 2 specifies the complete flat-space interaction grammar in this
model. With all momenta incoming and their sum zero, its vertex polynomials
and Feynman factors are

```text
V3(p1,p2,p3) = (p1.p2) p3^2 + (p1.p3) p2^2 + (p2.p3) p1^2
V4(p1,p2,p3,p4) = (p1.p2)(p3.p4) + (p1.p3)(p2.p4)
                 + (p1.p4)(p2.p3)
cubic factor = 2 i lambda3 V3;    quartic factor = 8 i lambda4 V4
propagator = -i/(p^2+i epsilon)^2
V3(p,q,-p-q) = 2(p.q)^2 - 2 p^2 q^2
```

The last identity is the cubic Gram-determinant cancellation: each cubic
leg has at least two powers of a soft momentum after momentum conservation;
each quartic leg has at least one. These factors are assumptions of the
off-shell infrared proof and must survive any proposed GU transfer.
The general shift-invariant grammar also permits a two-derivative mass term,
which this paper's massless calculation omits. Any such native term must
be carried through rather than discarded for matching.

For the renormalized couplings used in the loop tables,
`lambda3_bare=(4 pi) mu^(epsilon/2) Z3 lambda3` and
`lambda4_bare=(4 pi)^2 mu^epsilon Z4 lambda4`, with `d=4-epsilon`.
This distinguishes the loop-table convention from coefficients directly read
off an unrescaled action. [Primary interaction rules](https://arxiv.org/html/2608.12210v1#S2).

### Displayed auxiliary elimination has a normalization discrepancy

The primary PDF **5.3** gives
`L=partial Omega partial Upsilon-g(Omega Upsilon)^2/6`.
Integrating by parts and solving the algebraic `Upsilon` equation gives

```text
L = -Upsilon Box(Omega) - g Omega^2 Upsilon^2/6
Upsilon = -3 Box(Omega)/(g Omega^2)
L_eff = 3/(2g) [Box(Omega)/Omega]^2.
```

PDF **5.4** instead prints `1/(2g)`. This same coefficient appears in the
original `main.tex` and HTML equation **52**, so it is not merely an HTML
conversion error. With the stated `g=-3 lambda^2` and
`Omega=exp(lambda sigma)`, the derived coefficient gives `-1/2` times the
perfect square; the printed coefficient gives `-1/6`.
This is an exact discrepancy between displayed equations in that convention.
It does not negate the separate three-loop computations. The TeX archive and
member hashes are retained in the receipt. Domain, contour and determinant
claims of the functional integral are not established by this algebra.
[Primary equation](https://arxiv.org/html/2608.12210v1#S5.E52).

## Transfer to an actual GU scalar experiment

An observed conformally flat substitution can make an `R^2` comparator look
like the scalar perfect square. It does not identify Weinstein's native
action, the observed full-`II` functional, or an interacting physical sector.
Keep the I1B, I2B and observed action owners separate, as required by
[K117](../../explorations/conditional-build/selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate-2026-08-15.md)
and its K118 correction.

For a declared action `S`, scalar embedding `F(sigma)` and complementary
fields `z`, the next useful exact calculation has two independent outputs:

1. Pull back the complete action, retain boundary terms under stated boundary
   conditions, and compute all scalar coefficients. Evaluate
   `4ac-b^2`; retain every extra operator and every coefficient derivative.
2. Vary the complete action before restriction and evaluate
   `E_z[S](F(sigma),z=0)`. Prove that it vanishes identically, follows from
   the scalar equations by a stated differential identity, or is controlled
   by a derived constraint on the same domain. Merely setting it to zero
   when evaluating the restricted action does not prove closure.

A failed coefficient test excludes that declared scalar bridge. A passed
coefficient test with nonzero normal equations is an algebraic resemblance,
with a dynamical leak still present. Passing both would make this external
scalar mechanism a meaningful target for later pairing and quantum tests;
it would not clear the other GU sectors.

The native constraint burden remains the seven obligations in
[K1140](../../explorations/conditional-build/k1140-i1b-constraint-admission-compiler-2026-10-05.md),
including negative-block capture, propagation, a common closed domain and
a positive pairing on a nonzero physical cohomology class. The
[H59 loop gate](../../explorations/H59-krein-loop-positivity-gate-2026-07-12.md)
still requires the interacting ghost rule, regulator, inclusive observable
and projected probability calculation.

## Two later observable diagnostics

Amaral–Lemes **v2** constructs a BRST cocycle using external covariant Cartan
frames and conjugate field-strength combinations. Its lowest component has
positive leading one-loop spectral density (Sections 8–9). The authors
explicitly restrict the class to the enlarged background-equivariant theory;
the exact BRST closure is distinct from positivity of the full interacting
operator. Counterterms, insertion mixing and all-order positivity remain
unfinished. GU transfer would require its own action-derived differential,
matching real/contour structure and admissible observable, rather than an
imported frame or quartet. This is a cocycle-construction method donor, not
a positive physical Hilbert-space theorem for GU.
[October revision](https://arxiv.org/html/2605.16172v2#S9.SS3).

Asorey et al. derive a subtracted positive spectral representation for the
`phi1 phi2` composite of conjugate-mass scalar ghosts and a bubble-resummed
bound-state correlator (Sections 2–4). The concrete diagnostic separates
continuum spectral density, isolated pole residue and contact subtractions.
It is useful if a native observable and propagator actually supply that
structure. The calculation concerns the selected composite two-point function
and resummation, rather than every Schwinger function or the complete
interacting theory. It is an alternative composite-observable route, with
different masses and interactions from Bateman–Turok ghost parity.
[Primary full text](https://arxiv.org/html/2511.15283v1).

## Literature boundary

The Bateman–Turok June paper still has only `v1` in its checked version
history. Its tree positivity statement and weak ghost-symmetric process
decomposition remain distinct from loop positivity. The August follow-up
lists **The conformally flat limit of Quadratic Gravity** as reference 3 and
**Unitarity and positivity in higher-derivative QFTs with hidden ghost parity**
as reference 96, both in preparation. No separate public arXiv primary for
either companion was verified in this targeted search. Announced gauged
versions likewise do not supply a noncompact GU gauge positivity theorem.
[June conclusions](https://arxiv.org/html/2607.00096v1#S6),
[August references](https://arxiv.org/html/2608.12210v1#bib.bib96).

The solvable time-dependent model [2510.02494v1](https://arxiv.org/abs/2510.02494v1)
was inspected but not retained: it adds no sharper native transport test to
K117's already-exact form/grading compatibility and action-owner mismatch.
This pack is a targeted source intake, not a systematic literature review.
No source claim status, conditional-physics ledger row, canon result or GU
positivity verdict changes.

## Reproducible scalar diagnostics

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/quantum_positivity_scalar_transfer_probe.py
```

The exact probe verifies the complete-square residue, the normalized scalar
relation and its RG tangency condition, momentum-conserving cubic Gram
cancellation, and the auxiliary coefficient discrepancy. The auxiliary
elimination assumes `g!=0` and `Omega!=0`; its exponential-field substitution
also assumes `lambda!=0`. The polynomial perfect-square identity itself
allows `lambda=0`.

A finite-dimensional potential countercontrol has the same restricted scalar
expression and a nonzero normal derivative. It demonstrates the logical
closure gap only; it does not compute a native GU Euler equation. No loop
integral, on-shell probability or physical GU state is constructed by this
probe. Its 14 symbolic checks use SymPy 1.14.0.
