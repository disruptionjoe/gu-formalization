---
title: "Pin/Smith class-realization ultimatum"
status: active_research
doc_type: exploration
lane: "1"
run_type: progress
started_at: "2026-07-22"
updated_at: "2026-07-22"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: PIN-SMITH-NOT-DEFINED
probe: tests/channel-swings/pin_smith_class_realization_gate.py
---

# Pin/Smith class-realization ultimatum

## Run plan

**Controlling question.** Does the committed GU construction canonically define a class in
`Omega^{Pin+}_14 ~= Z/2`, and if so is that class the generator or zero?

**Lane selection.** Lane 1, GU truth testing.  The ambient bordism group is already exact; this run attacks
the remaining physics-to-topology map rather than another coefficient calculation.

**Construction fork.** The target is the program-native observerse/section/deck construction.  A standard
compact Pin manifold, positive-Hilbert Dirac family, or freely selected determinant line may be used only as
an explicitly typed control.  It cannot stand in for a missing GU object.

**Required source-owned fields.** A positive class assignment must identify, from committed sources:

1. a closed 14-dimensional geometric cycle or a proper Fredholm family with the same bordism meaning;
2. its `Pin+` lift and convention;
3. the deck/real/quaternionic action;
4. the determinant, Pfaffian, spectral-flow, or domain-orientation line carrying the proposed `w1`;
5. a natural map from that object to `Omega^{Pin+}_14`;
6. a generator-detecting evaluation, directly or after the Smith reduction to `Omega^{Pin-}_12`.

**Pre-registered terminal outcomes.** Exactly one of the following will govern the run:

- `GENERATOR`: all six fields are source-owned and the detector is nonzero;
- `TRIVIAL`: all six fields are source-owned and the detector vanishes;
- `NOT-DEFINED`: the committed data do not canonically define the required class.  This outcome must name
  the first missing field and show why available alternatives are noncanonical or yield different answers.

No nonzero ambient group, candidate analogy, persona agreement, or scalar `+/-i0` branch may substitute for
the class construction.

## Working notes

## Outcome

> **`PIN-SMITH-NOT-DEFINED`.** The committed GU repository does not yet canonically define an element of
> `Omega^{Pin+}_14`.  Therefore the GU candidate is presently neither proved `TRIVIAL` nor proved to be the
> `GENERATOR`.  The ambient target is exactly `Z/2`; the input to that target is missing.

This is a terminal answer to the pre-registered question **relative to committed source**, not a claim that
no future GU construction can define the class.  It sharpens the preceding `SOURCE-GAP`: the missing item is
not another coefficient computation.  It is the class-bearing object and its map.

## Two independent realization attacks

### A. Geometric-cycle route

The obvious degree-14 candidate is the observerse total space
`Y14 = Met(X4) -> X4`, with 10-dimensional fiber `GL(4,R)/O(3,1)`.  It fails at the
first class-bearing field: **closedness/compactness**.

The test supplies the exact determinant-fixed ray

```text
g_k = diag(-2^k, 2^-k, 1, 1),  k >= 0.
```

Every `g_k` has determinant `-1` and signature `(3,1)`, while its maximum entry norm is `2^k`.
Thus even the fixed-determinant fiber contains an unbounded escape direction.  The fiber's deformation
retract to `RP3` preserves homotopy information; it does not turn the actual 10-dimensional noncompact
fiber into a compact tangent/bordism representative.  No committed compactification, relative-bordism
boundary condition, or proper pushforward supplies an absolute fundamental class for `Y14`.

There is a second independent obstruction after compactness: the current corrected canon gives
`w2(Y14) = pi*w2(X4)`, so the available Spin/Pin-plus lift is conditional on the unspecified base and is not
a canonically selected global lift.  See [`canon/w2-y14-spin-structure.md`](../canon/w2-y14-spin-structure.md).

The other geometric candidates fail even earlier by type:

| candidate | exact/native content retained | first failure |
|---|---|---|
| observer section `s(X4)` | a genuine program-native section | dimension 4, not 14 |
| regular wall `{q=0}` | the characteristic wall is meaningful | dimension 13, not 14 |
| fiber retract `RP3` | exact cover `S3 -> RP3` and its one `H1` bit | dimension 3, not 14 |
| `RP3 x Y11` | a possible 14-dimensional control shape | `Y11` is freely chosen, not GU-constructed |

The last line matters.  The earlier Stiefel--Whitney swing correctly found `sigma^4=0` on `RP3`; any
degree-14 mixed detector then needs data from an 11-dimensional complement.  Selecting that complement is
selecting the missing bordism input, not deriving it.

### B. Analytic-family route

The analytic alternative would replace a compact cycle by a proper, continuously parametrized Fredholm
realization with enough real/quaternionic structure to construct the relevant line and family class.  It
also fails at its first class-bearing field: **no source-owned Fredholm realization exists**.

The repository owns a `D_GU`/Dirac-symbol skeleton and exact local Clifford algebra.  It does not yet own,
on the noncompact observerse:

1. a frozen full differential realization with all coefficients and parameter space;
2. a domain at every end, or a proof of essential self-adjointness/Fredholmness;
3. an operator-grade deck action preserving and transporting those domains;
4. the determinant, Pfaffian, spectral-flow, or domain-orientation line;
5. a proper family index/naturality map from that line to Pin-plus bordism.

The recent operator audit makes this failure more precise rather than curing it.  For the exact timelike
Clifford matrix, the full operator is `K`-self-adjoint while its `+/-i` eigenspaces are `K`-null.  Hence the
available calculation refutes a **definite spectral cut**; it does not prove that every self-adjoint domain
is absent.  Standard boundary controls have continuous `U(n)` domain families, including swap-fixed
choices for `n >= 2`.  The scalar `+/-i0` pair is therefore only a reduced ansatz, not a derived two-point
domain bundle and not a bordism class.

The other analytic candidates fail by type:

| candidate | first failure |
|---|---|
| full section space `Met(X4)` | infinite-dimensional; no degree-14 cycle or frozen family parameterization |
| solution-section moduli | full equations, global analytic moduli object, and topology are unconstructed |
| `D_GU` family | no proper Fredholm realization on the noncompact ends |
| scalar `+/-i0` branches | not domains, not a line bundle, and not a cycle/family class |

The older Option-B note already identifies solution moduli as the only potentially non-ordinary observer
space, but its construction requires the full action/PDE and global moduli theory.  The compact Riemannian
section-space toy cannot be silently substituted for the Lorentzian GU problem.  See
[`freed-hopkins-optionb-ksp-family-2026-06-23.md`](time-as-finality-crosswalk/freed-hopkins-optionb-ksp-family-2026-06-23.md).

## Smith typing result

The Smith route remains exact and useful:

```text
Omega^{Pin+}_14  ~=  Omega^{Pin-}_12  ~=  Z/2.
```

But the Smith homomorphism consumes a specific cycle/background line and returns its codimension-two
Pin-minus Smith locus.  It does not manufacture the input cycle.  The exact spin-cover bit on `RP3`, the
ambient group order, and the label `Pin+` inferred from a local square convention are individually
insufficient to specify that input.

This also explains why `TRIVIAL` is not the answer.  `TRIVIAL` would require a defined natural class whose
detector evaluates to zero.  Here the evaluation has no argument.  Zero and undefined are different
scientific results.

## Source and alternative audit

A direct term audit of `lab/sources/` found no primary-source construction named as a Pin-plus lift,
Smith input, determinant/Pfaffian line, or operator-grade deck action.  This is evidence about the current
corpus, not a proof of impossibility.  Repository-native alternatives were then enumerated above so the
result does not rest on lexical silence alone.

The conventional abstract generator of the now-proved `Z/2` target is retained as a positive control.  If
an external oracle supplies the closed Pin-plus object, action, line, class map, and detector, the interface
can classify it.  It fails only the GU-native provenance field.  This prevents the gate from confusing
"the target group has no classes" with "GU has not supplied its class."

## Process finding

The triple-diamond process worked best when it separated two questions that previous swings had mixed:

1. **What is the receptacle?** This is now exactly answered: `Z/2`, with an exact Smith cross-check.
2. **What GU object maps into it?** The ultimatum shows this is a construction/type problem, not a harder
   bordism-table problem.

The useful process advance is a stop rule: once the six-field class interface fails, more personas,
ambient-group computations, or invariant guesses cannot move the class.  Future work should begin with a
frozen representative packet, not with a detector.

## Reopener: one complete packet

Reopen this leg only when one of the following packets exists.

- **Geometric packet:** a specific compact closed 14-manifold (or explicitly typed relative cycle), a
  source-selected map relating it to the observerse, a Pin-plus lift, the time/deck line, and a natural
  bordism-class construction.
- **Analytic packet:** a specific parameter space and full `D_GU` family, end/domain conditions, a
  Fredholmness proof, operator-grade deck/real/quaternionic action, and the constructed orientation line.

Only after either packet exists is the final one-bit evaluation worth running.  NumPy is not needed for
this gate; the decisive checks are exact rational arithmetic and object typing.

### 2026-07-22 Mannheim--Callias follow-through

The most natural analytic reopener was tested against the committed candidate action.  It fails admission:
on the full determinant-fixed diagonal Cartan escape family, the displayed source-action terms vanish at
`A` flat and `Psi=0`, while the horizontal-normalized tautological LC section has `II_s^H=0`.  Thus the
source-owned Callias left-hand side remains zero on an escaping sequence.  The unspecified compensator and
VZ guardian cannot be assigned a coercive value by assumption.  This is
`MANNHEIM-CALLIAS-NO-END-POTENTIAL`, not an impossibility theorem: a new explicit asymptotic term or a
source-selected PT/Stokes/domain construction can reopen the route.  See
[`mannheim-callias-deamp-lean-orchestrated-swing-2026-07-22.md`](mannheim-callias-deamp-lean-orchestrated-swing-2026-07-22.md).

### 2026-07-22 Bott--Callias construction follow-through

The strongest conditional analytic reopener is now explicit.  After importing a complete positive
Riemannian end and an elliptic right-`H` Dirac operator, the scalar mass `sqrt(1+r^2) I` satisfies a Callias
estimate but is homotopic through uniformly admissible masses to a constant, so it is class-silent.  A
continuous deck-odd real scalar cannot stay gapped on the connected `S3` cover.

The first nontrivial control is matrix-valued: left quaternionic multiplication `q -> L_q`, doubled to a
self-adjoint involution on `H (+) H`.  It is exactly right-`H`-linear, deck-equivariant, and gives a positive
Callias bound after radial scaling; its normalized mass is the degree-one quaternionic Hopf/Bott clutching
map.  This materially narrows the reopener, but does not change `PIN-SMITH-NOT-DEFINED`: the actual `D_GU`
descent, global positive completion, orientation line, and natural equivariant `KSp/KR -> Pin+` pushforward
are not constructed.  See
[`fredholm-end-clutching-big-swing-2026-07-22.md`](fredholm-end-clutching-big-swing-2026-07-22.md).

## Reproduction receipt

Run:

```bash
python3 tests/channel-swings/pin_smith_class_realization_gate.py
```

The probe enumerates nine native candidates plus one external positive control, verifies the explicit
noncompact ray, checks the Smith degree/flavor target, validates every candidate's first missing field, and
emits `PIN-SMITH-NOT-DEFINED`.  It uses only the Python standard library.
