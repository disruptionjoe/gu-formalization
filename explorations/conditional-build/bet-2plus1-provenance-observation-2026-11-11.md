---
title: "BET-2PLUS1: minimum provenance observation and actual sector mixing"
status: exploration
claim_verdict: conditional_internal_result
doc_type: structural-result
created: "2026-11-11"
program_target: BET-2PLUS1
tier: T1
expected_delta: "Classify minimum trace/remainder observation and test conserved-label inference on the held raw operator."
actual_delta: "Minimum linear separators classified; they realize the held dynamic quotient, whose original evolution mixes all three provenance labels. Bet remains active."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: "INTERNAL — algebraic separation of trace/remainder/scalar labels in the supplied K2236 quotient implies each is an invariant family sector; the explicit original evolution refutes this inference only."
canon_verdict_change: none
---

# Minimum information for provenance is not a physical family decomposition

**Result.** With a fixed nondegenerate horizontal/normal Clifford split, one
additional spinor-sized linear output is necessary and sufficient to separate
the observed images of ambient gamma trace and gamma remainder. Every
minimum separator is equivalent to retaining the ambient gamma trace alongside
ordinary pullback. It still forgets nine spinor-sized remainder directions.
On the supplied K2236 raw model, adding the existing scalar pullback makes this
exactly its already known rank768 dynamic quotient. Direct tests of the
original evolution show that all three provenance sectors mix.

Thus the algebraic observation repair is completely classified at this scope,
but does not supply conserved or physical families. BET-2PLUS1 remains active.
No guessed action is introduced; this preparation resolves a necessary
observation/dynamics seam before such a candidate could earn a count.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result. Classification: `INTERNAL_STRUCTURAL_ONLY`.

## Native bookends and typing

program_target: BET-2PLUS1
tier: T1
expected_delta: Minimum provenance observation plus actual operator compatibility test.
actual_delta: Complete pointwise linear classification and scoped mixing result; bet active.

```gu-typed-objects
result: minimum provenance-separating observation and original K2236 principal-sector mixing
carrier: abstract Clifford one-form module with fixed H/N split; separately K2236 real1920 raw parent LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: NONE
real_structure: supplied real Clifford module in real version; complex half-spin version has opposite-chirality trace target
grading: ambient gamma trace/remainder and independent scalar provenance, not physical family/chirality grading
action_owner: repository-construction -- no guessed action or source-owned observation augmentation
target: vector-space linear output retaining pullback, compared to original supplied evolution MAP-TYPE=homomorphism
```

### What is reused

- VZ4 already proves that the ambient RS remainder observes onto the **whole**
  observed one-form carrier. Full image is not a new discovery here.
- The August30 real-sector/leakage theorem and August31 corrected projector
  already distinguish literal pullback from trace subtraction.
- The September23 quotient-versus-slice result already distinguishes a map on
  quotient classes from a representative selector.
- K2236 already proves minimum dynamic rank768, exact fixed-plane closure,
  Jordan defect and the raw Green-descent limit. K2239 owns graph-motion
  refinements and their limitations. These are not new claims of this note.

New work classifies **all minimum static provenance separators**, identifies
their realization with that held dynamic quotient, then applies the actual
operator to the specific provenance sectors. Static distinguishability,
autonomous combined evolution and invariant sectors are three different tests.

### Source scope

SC-FER-04 supplies the gamma trace/remainder product-rule grammar; SC-FER-05
supplies the graded representation labels. SC-GEN-52 explicitly leaves the
live exchange's second-generation trace/kernel terminology uncertain. Do not
assign a physical second family from these abstract labels. SC-GEN-01
DISAVOWS simple triplication, and SC-CHI-01/51 describe a non-chiral total
with effective observed chirality. The present test changes none of these.
SC-FER-07 in the current register concerns p27 normal-spinor quantum numbers;
it is not used as a locator for the older artifact's p65 shorthand.

## 1. Fixed split and the information already lost

Work pointwise over real or complex scalars in characteristic zero. Let
`V*=H*⊕N*` be an orthogonal nondegenerate split, with dimensions `h=4,n=10`,
and let `S` be a supplied Clifford module of dimension `s`. Write

`A=(H*⊕N*)⊗S`, `B=H*⊗S`, `P(b,v)=b`,
`ΓY(b,v)=ΓH b+ΓN v`.

For a half-spin input the contraction target is the **opposite** half-spin;
write `S` as a dimension label only in formulas where those dimensions agree.
The actual maps retain their chirality types. In the real version the contraction and insertion maps
are real-linear maps supplied by the same real Clifford representation. Their
equivariance is under the corresponding split-preserving Spin action; the
arbitrary augmentation classification is linear and does not impose equivariance.

Metric-normalized Clifford insertions satisfy
`ΓH jH=1`, `ΓN jN=1`, and

`jY ψ=(h/(h+n) jH ψ, n/(h+n) jN ψ)`.

Let `T=im jY`, `R=ker ΓY`; then `A=T⊕R`. In particular
`PjY=(2/7)jH` is injective. Since `ΓN` is onto, every `b∈B` lifts to
`(b,-jNΓH b)∈R`. Hence `P(R)=B`, while `P(T)=im jH`. This reuses VZ4's
full-image fact. Ordinary pullback cannot identify trace provenance even on
that trace-sized observed subspace.

The held correction `QH=1-jHΓH` kills `P(T)` and sends `P(R)` onto
`ker ΓH`. It repairs output tracelessness, but cannot on that output retain
the lost trace provenance. Appending the already computable `ΓH P` does not
help: it is a function of `P` and adds no information about the input.

## 2. Necessary and sufficient separation criterion

Consider any linear augmentation `Q=(P,L):A→B⊕W`. Separation means exactly

`Q(T)∩Q(R)={0}`.

It is not injective recovery of all of `A`. Because `P|T` is injective,
separation is equivalent to `ker Q⊂R`: for `a=t+r` in `ker Q`, the common
image `Qt=-Qr` vanishes exactly when `t=0`.

Set `K=ker P=N*⊗S`, `KR=K∩R=ker ΓN`. Since `ker Q=ker(L|K)`, the criterion
becomes

`ker(L|K)⊂KR`.

Equivalently, the induced map

`S ≅ K/KR → W/L(KR)`, `[v]↦[Lv]`,

is injective. Indeed `Lv∈L(KR)` means `L(v-k)=0` for some `k∈KR`, which
forces `v∈KR` under the criterion; the converse follows by taking `Lv=0`.
Therefore

`dim W ≥ s + dim L(KR) ≥ s`.

Retaining hidden remainder information costs extra capacity; it cannot share
one of the minimum channels while preserving complete trace provenance.
This is a theorem about finite-dimensional **linear pointwise** outputs. It
makes no nonlinear, derivative-valued or nonlocal information lower bound.

## 3. All minimum repairs, not only one candidate

If `dim W=s`, the preceding inequality forces `L(KR)=0`, and the induced
map `A0:S→W` is invertible. Thus exactly the minimum separators are

`L(b,v)=M b+A0 ΓN v`,

for arbitrary linear `M:B→W` and invertible `A0`. Conversely each such map
satisfies the kernel criterion. The invertible output change

`(b,w) ↦ (b, ΓH b+A0^-1(w-Mb))`

turns it into `F=(P,ΓY)`. This proves classification up to an explicit output
isomorphism, not a unique physical choice of receiver or pairing.

The map `F` is onto `B⊕S`: for any `(b,ψ)`, choose
`v=jN(ψ-ΓH b)`. Its kernel is exactly `KR`, of dimension `(n-1)s=9s`.
The images are

`F(R)=B⊕0`,
`F(T)={( (2/7)jH ψ, ψ): ψ∈S}`.

They intersect only at zero and together span the output. The image of `R`
still includes all `B`, but it is now distinguished by its second coordinate.
The missing `9s` directions remain genuinely unrecovered. Global smoothness,
gauge covariance, source selection and physical access require additional
bundle/dynamic data; this pointwise theorem supplies none of them.

## 4. Identification with the held raw dynamic quotient

Now specialize only to K2236's supplied, fixed-plane real Cl(7,7) parent.
It is not asserted to be the source's uniquely selected operator. Its
normalization is

`ζa=ηa γa ua`, `ν=Wbar h0`, `O={0,7,8,9}`, `U=O-complement`.

Because `γa²=ηa`, ambient gamma trace is `Σ_(a<14) ua`. Ordinary pullback
retains the four observed `uμ` and scalar `h0`. Appending gamma trace therefore
recovers `σ=Σ_U ur`, and conversely. This is exactly the held quotient

`R0 u=(a,b1,b2,b3,v,h0)=(u0,u7,u8,u9,σ/10,h0)`.

The spinor dimension is128 real: one-form augmented output has dimension640;
including scalar gives768; the hidden remainder kernel has dimension1152.
K2236 already establishes that this output closes under its original observed
principal and declared lower coefficients. Its entire rank768 output has the
known Jordan/positive-current and Green-descent limitations. No calculation
here upgrades those to a source/action verdict or builds a physical quotient.

## 5. Actual evolution does not preserve the separated labels

Use the **original** scalar15-slot coefficient matrices `Mk`, with
`Mk[a,c]=1` for distinct one-form indices `a,k,c`, `Mk[k,h0]=1`,
`Mk[h0,k]=-1/2`, and all other cells zero. The supplied Clifford factor is
`Γk=γk Wbar`. The exact normalized spatial evolution is `M0^-1 Mj` times
`Cj=γ0 γj`, an invertible spinor map. Restrict through K2236's fixed `E,R0`;
the probe derives `Tj=R0 M0^-1 Mj E` from these raw matrices.

Writing `other=Σ_(l≠j) bl`, its known six-slot formula is

`a'=bj`, `v'=(h0+2v-other)/12`,
`bl'=bl-v+v'` for `l≠j`,
`bj'=a+other+9v-h0+v'`, `h0'=other+10v`.

Let `g=a+b1+b2+b3+10v` be the one-form gamma trace coordinate. The following
three actual inputs each carry an arbitrary nonzero spinor; all outputs carry
the common invertible `Cj` factor.

| Input provenance | Six-slot input | Exact output evidence |
| --- | --- | --- |
| Pure ambient trace | `(1,1,1,1,1,0)/14` | `a'=1/14`, `bj'=12/14`, other `b'=v'=0`, `h0'=12/14` |
| Pure remainder | `(1,0,0,0,-1/10,0)` with `g=0` | `a'=0`, every `b'=1/12`, `v'=-1/60`, `h0'=-1`; `g'=1/12` |
| Pure scalar | `(0,0,0,0,0,1)` | `a'=h0'=0`, `bj'=-11/12`, other `b'=v'=1/12`; `g'=1/12` |

Each sector fails invariance under an actual spatial principal generator.
Thus autonomous evolution of their **combined** output is not conservation
of the three labels separately. For fields with arbitrary spatial first jets,
lower-order coefficients cannot cancel this principal mixing universally.
This is not a statement about every constrained solution subset, another
moving/projected output, or a changed operator or action. It does not exclude
energy-dependent effective sectors, which are part of the source's proposal.

## 6. Bet disposition and exact remaining test

BET-2PLUS1 remains **active**; one research run is charged, leaving23 of24.
No guessed action variant was tried. The new invariant is an algebraic
provenance separator, not a physical family invariant. The observation map is
typed as a pointwise linear quotient with kernel `KR`; a map to realized count
is still absent. Hence neither a discovery nor the bet's full kill criterion
is declared satisfied.

For this fixed raw realization, enlarging the output while retaining ordinary
pullback does not erase its inherited K2236/K2239 Jordan obstruction to a
positive-definite conserved current. The zero-descended-Green result belongs
to the minimal quotient: larger outputs can retain hidden directions and
recover nonzero raw Green forms, as the full-parent identity output illustrates.
For this pointwise first-order refinement route, useful successors include a
genuinely changed operator/action or a specified invariant physical subspace,
tested against the same observation and principal-mixing identities. Nonlocal,
derivative-valued or different moving observations remain separate routes
outside this result; their own closure and physical-readout tests are still owed. Arbitrary relabeling, an output shear, or another
rank census does not provide that change. The source-selected carrier,
variation, constraint complex, domain and physical readout remain substantive
open inputs, not filled by the algebra above. No result enters the action
constraint matrix or physics ledger without its required separate derivation.

## Evidence and review boundary

The probe uses a small real Cl(2,1) control with nontrivial hidden remainder
kernel, classifies correct and false augmentation fixtures, and independently
extracts the six-slot matrices from original15-slot coefficients. Genuine
faults change the coefficients consumed by the trace and remainder tests.
The finite Lean file checks the rational input types and mixing for one
spatial direction. The universal linear classification is the written proof;
Lean does not certify it, the Clifford model, a PDE or an action.

Two independent specialists and a distinct hostile review inspect these
hypotheses and the actual inference. All review is internal. Prior full image,
projector, closure, Jordan, Green and graph results are reused at unchanged
scope; only their directly consumed finite coefficient identities are replayed.

- [Exact probe](../../tests/program-focus/bet_2plus1_provenance_probe.py).
- [Structured evidence](../../lab/process/bet-2plus1-provenance-observation.json).
- [Finite Lean mixing](../../Lean/GUFormalization/ProvenanceMixing.lean).
- [VZ4 full observation image](../../lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md).
- [Held corrected projector](../source-native-corrected-observation-projector-2026-08-31.md).
- [Quotient/slice distinction](corrected-observation-quotient-slice-compatibility-2026-09-23.md).
- [K2236 fixed-plane dynamic quotient](k2236-raw-observation-closure-2026-10-29.md).
- [K2239 graph closure](k2239-moving-observation-closure-2026-10-29.md).
