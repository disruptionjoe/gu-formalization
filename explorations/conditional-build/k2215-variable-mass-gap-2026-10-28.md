---
title: "K2215 Derivative-free variable gap and moving-principal boundary"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sufficient global gap for the fixed supplied current class; moving-frame controls do not select a source action or physical mass
scripts:
  - tests/channel-swings/k2215_variable_mass_gap_probe.py
---

# K2215 Derivative-free variable gap and moving-principal boundary

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
result: K2215 Derivative-free variable gap and moving-principal boundary
carrier: K2212 real128 spinor complexified on R3 and nine-copy V1152 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive reduced L2 current ON=declared_carrier
real_structure: real fixed-class coefficients; separate complex-unitary moving-frame control
grading: Cl77 full Dirac; no physical chirality or family count
action_owner: repository-construction -- conditional supplied operator or instrument
target: common-domain spectral gap MAP-TYPE=intertwiner
```

## Result: a global gap with no coefficient-gradient bound

Retain [K2212](k2212-mass-connection-algebra-2026-10-28.md)'s actual common-return
invariant sector, with Hermitian involutions M=-iP0 and S=-iQ, Hermitian spatial
Clifford matrices Cj, {M,Cj}={M,S}=0 and [S,Cj]=0. On L2(R3;C128), let

    H=D+c(x)S+m(x)M+S b(x).C,  D=-i sum Cj partial_j,
    Dom(H)=H1(R3;C128).

All five coefficient functions are bounded real measurable. If ONE fixed
sign sigma in {+1,-1} has

    delta=ess inf_x (sigma m(x)-|b(x)|)>0,

then (-delta,delta) is in the resolvent, and for real |E|<delta,

    ||(H-E)^(-1)|| <= 1/(delta-|E|).                     (1)

There is no derivative bound on m,c,b. In particular the correlation between
m and b matters: the two pairs (m,|b|)=(3,1),(102,100) have delta=2 while
inf m-sup|b|=-97. Arbitrary spatial interfaces between these pairs are allowed.
The theorem applies to each of the nine copies in V1152. Smooth members retain
the original raw common-return construction; measurable members are its
well-defined reduced operator extension, not an asserted classical raw solution.

## Proof and sharpness

The potential is bounded Hermitian, hence H is self-adjoint on the free H1
domain. M preserves that domain and anticommutes with D+cS, as an operator,
without differentiating c. Moreover MS b.C is Hermitian and squares to |b|².
For u in H1 the real part satisfies

    Re <sigma M u,(H-E)u>
      >= integral (sigma m-|b|-|E|)|u|²
      >= (delta-|E|)||u||².

Cauchy--Schwarz gives the lower norm estimate. Its range is closed, and its
orthogonal complement is ker(H-E)=0 by self-adjointness, so H-E is onto.
This proves (1); a lower norm bound alone would not prove surjectivity for a
nonself-adjoint operator. The exact constant spectrum in K2212 saturates the
bound. Variable coefficients may have a larger gap; no equality is asserted.
A scalar electric potential commuting with M destroys the identity: M+I has
a zero eigenvalue despite unit mass. Such contamination is outside this class.

## Static moving frames: the derivative term is necessary

For static unitary U in W1,infinity, multiplication by U preserves H1 and

    U H U† = -i sum Aj partial_j + U V U†
                -i sum U Cj (partial_j U†),  Aj=U Cj U†. (2)

The mass involution becomes U M U†. The entire transported differential
operator, including the last term, retains the same gap and anticommutation.
A coefficientwise conjugation without that term is a different operator.
This supplies a conditional global transport construction, not a selected
source observation, physical quotient or source gauge action.

Here is an exact failure of the frozen-symbol inference. With m>0 constant,
H0=D+mM, choose U(x1)=exp(i k x1 C1). Define

    Htilde=-i sum Aj partial_j+m U M U†.

A1=C1 and sum partial_j Aj=0. Formula (2) gives

    Htilde=U H0 U†+kI,
    spectrum(Htilde)=k+((-infinity,-m] union [m,infinity)). (3)

Thus every frozen symbol is conjugate to p.C+mM and has gap m, yet zero lies
in the GLOBAL spectrum whenever |k|>=m. This operator is self-adjoint on H1
by the displayed unitary identity. The complex-unitary control transports the
real-structure presentation and leaves the fixed real K2212 class; it is not
silently a new GU realization. The probe checks the derivative sign and an
exact zero-momentum-shell matrix at m=1,k=2,|p|=sqrt(3).

Time-dependent transformations need a separate warning grounded in an actual
identity: v=exp(t m P0)u removes the mass in the original evolution equation,
but rotates Cj(t). Each instantaneous Hamiltonian is gapless; the full dynamics
remain equivalent. Static spectral gaps are preserved by static transport,
not by arbitrary time-dependent re-expression.

## Inherited wall control and common-return consequence

[K1967](k1967-paired-raw-coefficient-observation-2026-10-22.md) already proves
the domain-wall mechanism. Reuse it, without claiming discovery. For
m(x1)=a tanh x1, a>0, K=iC1M=C1P0 and f=cosh(x1)^(-a),

    K²=I, rank((I+K)/2)=64,  f'=-mf,
    (-iC1 partial_1+mM)fv=0 for Kv=v.

C2,C3 preserve the normal kernel and yield tangent energies ±|p_perp|, each
multiplicity32. The newer common-return V1152 supplies nine identical copies:
normal fiber576, branch multiplicities288. On R3 normalized transverse
packets of scale R give residual O(1/R), proving zero is spectral, not a
claimed L2 zero eigenvector. On R x T2 constant transverse modes ARE L2.
The fixed-sign hypothesis of (1) fails at this wall; no contradiction occurs.

A sharper fixed-sign countercontrol uses m=a sign(x1), with a>0, and
f=exp(-a|x1|). Then f is in H1, f'=-mf almost everywhere, and
ess inf |m|=a>0. The same normal kernel and transverse packets yield zero
spectrum. Thus even a positive uniform ABSOLUTE mass bound cannot replace one
fixed sign in (1). The first-order weak derivative has no delta term because
f is continuous. This is a specified bounded-measurable variant of the inherited
wall mechanism, not a new source-selected background.

## Verification, scope and next construction

Exact faithful-Cl77 identities, a separate small Clifford representation,
a nonconstant finite derivative/potential form, and static-frame derivatives
support the written Hilbert-space proof. Baseline-first faults introduce a
commuting scalar potential, reverse the frame correction or flip the wall
projector; each must fail an actual mathematical check. Finite checks are not
a continuum spectral proof. No prior heavy bank is rebuilt.

SC-OP-04 ASSERTS candidate four-field grammar; SC-META-53 remains UNCERTAIN
about unbounded spectra; SC-META-56 DISAVOWS the odd-action prerequisite.
Ledger0.263 LT-SM3/LT-SM8/LT-GR6b and source selection are unchanged. The
next meaningful source-facing step must own the common moving operator,
observation and action or test a genuinely different coefficient class.
A local frozen gap is now explicitly insufficient; another derivative-smallness
estimate for this fixed-sign class is unnecessary. No novelty, external-expert
or proof-assistant certification is claimed.
