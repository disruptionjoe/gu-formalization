---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "1"
work_item: THREE-ROUTE-CONSTRUCTION-WAVE
title: "Bott--Krein full-carrier admission: the proposed S_nat=C_perp J_H is an exact complex-linear Krein involution and preserves ker Gamma, but cannot simultaneously be right-H-linear. The standard doubled H-line Bott control survives with unit finite gap, while its natural diagonal H^64 lift has 64 copies of the clutching density; obtaining one copy requires a non-natural coordinate projector. No native mirror embedding, Clifford--Morita reduction, Callias index, or physical chiral-index map is constructed."
grade: "EXACT finite matrix algebra in the same factorized Cl(9,5) realization used by the vertical--Krein weld; exact algebraic incompatibility of S_nat^2=+1 with right-H-linearity for S_nat=C_perp J_H; exact gamma-trace-kernel preservation for the induced vector-spinor reflection; exact standard H-line Bott control and exact direct-sum cubic-density scaling. STANDARD INPUT only for the statement that q->L_q is the degree-one quaternionic clutching control. OPEN for a native mirror embedding, RS-preserving Bott mass, complete Callias domain/gap, Clifford--Morita pushforward, and physical index. No index is inferred from clutching degree or multiplicity."
run: lab/process/runs/GUH-20260729T211122Z-three-route-construction-wave/run-plan.md
probe: tests/channel-swings/bott_krein_full_carrier_admission_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: "KILL-S_NAT-H-LINEAR-DECK; FULL-CARRIER-BOTT-OPEN-AT-NATIVE-MIRROR-AND-MORITA-MAP"
---

# Bott--Krein full-carrier admission

## Result

The proposed first admission map fails for a structural reason, not for lack
of analytic hardening. In the fixed program-native representation,

```text
C_perp^2 = +1,       J_H^2 = -1,       S_nat = C_perp J_H.
```

`S_nat` is complex-linear, Krein-unitary, squares to `+1`, has a balanced
complex `64+64` eigensplitting, and preserves the full gamma-trace kernel under
its induced vector reflection. But it anti-commutes with `J_H`. Since a
complex-linear map is right-quaternionic-linear precisely when it commutes
with the antilinear right-`j` action `J_H`, `S_nat` is not right-`H`-linear.
Multiplication by `i` repairs that commutation and changes the square to
`-1`; it is not a deck involution.

The standard doubled `H`-line Bott control remains valid. Its natural diagonal
extension has exactly 64 copies of the nonzero local clutching density. A
planted one-coordinate projector returns one copy but fails to commute with a
single carrier permutation, so it is not a natural full-carrier reduction.
This kills the proposed `S_nat` admission and the unnormalized unit-class/P3
weld. It does not kill every possible Bott route: the smallest surviving
question is whether an already-existing GU mirror pair supplies a different
right-`H`-linear deck involution and a functorial Clifford--Morita index map.

## Layer 0: object and map table

| shared term | program-native object | standard/control object | relation and verdict |
| --- | --- | --- | --- |
| reality | `C_perp=K J_obs`, antilinear contragredient involution | none in the bare Bott control | SAME fixed matrix object only on the GU side |
| quaternionic structure | `J_H`, antilinear, `J_H^2=-1`, commuting with `Cl(9,5)` | right-`H` scalar action on the control | SAME-OBJECT after fixing the complex realization |
| deck grading | proposed `S_nat=C_perp J_H` on `S=H^64` | `S_B=diag(1,-1)` on `H+H` | HOMONYM until an intertwiner is built; `S_nat` fails right-`H`-linearity |
| Bott mass | no admitted native full-carrier map | `C_B(q)=[[0,L_q^*],[L_q,0]]` on `H+H` | HOMONYM; the standard object uses an auxiliary doubling not yet identified in GU |
| RS preservation | native `ker Gamma` and its induced vector-spinor action | absent from the `H`-line control | `S_nat` preserves `ker Gamma`; mass preservation remains UNCERTAIN because the mass embedding is absent |
| gap | split/Krein source operator and a common native domain | positive-Hilbert finite mass gap and imported Riemannian Callias estimate | HOMONYM; no norm-resolvent or domain map |
| degree | standard degree of `q->L_q` | physical Fredholm/chiral index | HOMONYM; no index map is constructed |
| 64 | direct-sum/Dynkin multiplicity on `H^64` | generation count | HOMONYM; decomposition is not count |
| reduction to one | a possible Clifford--Morita pushforward | choosing one quaternionic coordinate | UNCERTAIN for the former; the latter is executable and non-natural |

The exact Layer-0 target is therefore a commuting naturality packet, not a
numerical equality:

```text
iota_-q S_B = S_mirror iota_q
iota_q C_B^64(q) = M_GU(q) iota_q
Gamma M_GU(q) P_RS = 0
Ind_Cl(M_GU) --Morita--> a named physical index
```

No arrow in the last line is supplied by clutching degree alone.

## Ratified Layer-0 + L1--L7 candidate contract

This is a typed candidate record under the ratified seven-axis protocol. It
does not turn the failed admission map into a surviving candidate.

| candidate | L0 semantic alignment | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | L7 positivity | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full-carrier Bott--Krein weld | HOMONYMS NAMED; `S_nat` relating map KILLED; replacement mirror map UNCERTAIN | (a) smooth bundle on `Y14` and its double cover | (a) finite observer using a supplied GU observer section | (a) smooth spin/RS channel with the Krein form composed into bilinears | (a) smooth Lorentzian base order | (a) specific-object substrate | (a) no dynamical coordination loop | (b) indefinite Krein, proposed deck/ghost `Z/2` | require `S_nat^2=1` and `[S_nat,R_H]=0`; the probe falsifies their conjunction |

| axis | class and concrete specification | literature/source anchor | no-go assumption signature |
| --- | --- | --- | --- |
| Layer 0 | The control deck involution, native contragredient coflip, Bott mass, clutching degree, physical index, multiplicity, and generation count are distinct objects. Their required intertwiners are displayed above. | Ratified Layer-0 protocol; existing Bott--Callias, torsion-arena, and vertical--Krein explorations cited by this run. | Prevents a false escape: neither degree nor 64-fold multiplicity is a physical chiral count. The proposed coflip-to-deck map fails. |
| L1 substrate | **(a), smooth principal/Clifford bundle.** Sections of the `Cl(9,5)` spinor and gamma-traceless RS bundles over the smooth metric total space `Y14`, pulled to the metric-fibre double cover for deck equivariance. The positive complete Riemannian end remains a standard control, not native substrate data. | Weinstein, *Geometric Unity* draft (2021); Braverman--Cecchini and Braverman--Shi for the imported Callias control. | Preserves the smooth-bundle substrate assumed by the ordinary index/no-go results; this route claims no substrate-class exit. |
| L2 observer | **(a), finite observer.** A finite computational observer evaluates the bundle data after a supplied geometric observer section fixes the `4+10` split. The observer section is geometric input, not a hypercomputational observer class. | Weinstein (2021) for the Observerse/observer-section construction; finite-observer baseline from the ratified protocol. | Preserves the finite-observer assumption. The supplied section may reduce symmetry but does not itself evade an index theorem. |
| L3 pairing | **(a), smooth tensor-product channel.** Spinor/vector-spinor fields pair through the program-native Krein form `K`; physical bilinears use `K M`, and `C_perp=K J_obs` is a duality map rather than a bare symmetry operator. | Lawson--Michelsohn, *Spin Geometry* (1989), for smooth spinor bundles; the repository's vertical--Krein weld for the exact finite realization. | Preserves a smooth local pairing channel. Its indefinite signature is isolated at L7 rather than hidden here. |
| L4 causal order | **(a), total-order Lorentzian.** The observed base is the supplied Lorentzian `X4`; no partial, causal-set, or multiway order is introduced. A global Cauchy/domain completion remains open. | Bär--Ginoux--Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization* (2007), for the standard Lorentzian operator setting. | Preserves the smooth Lorentzian causal-order assumption. |
| L5 emergence | **(a), specific object.** The candidate uses the fixed `Y14`, its fixed `Cl(9,5)` carrier, and one proposed equivariant Fredholm cycle; no RG universality class or attractor supplies the class. | Weinstein (2021) and the repository's frozen carrier specification. | Preserves the specific-object assumption. |
| L6 coordination loop | **(a), no dynamical loop.** The metric-fibre deck loop is a topological loop in parameter space, not feedback between substrate dynamics and observer extraction. No mean-field, consensus, or self-stabilizing selector is posited. | None imported; this is the protocol's baseline class. | Preserves the no-coordination-loop assumption. |
| L7 positivity | **(b), indefinite Krein.** The 128-complex spinor realization has a `64+64` Krein split. The proposed deck/ghost parity is the candidate superselection datum; a nonnegative probability rule and common physical domain are not reconstructed here. | Bognár, *Indefinite Inner Product Spaces* (1974); Azizov--Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (1989); repository anchor-scale Krein result. | Breaks a hidden positive-Hilbert premise where such a premise is used. It does not evade grading-determined index conservation or turn multiplicity into generations. |

### Conditional chirality bridge claim

Had the admission square passed, the substrate-level object would have been
one equivariant, Clifford-compatible Bott--Callias Fredholm cycle on the
metric-fibre double cover. Its deck/Pfaffian line would be the proposed
`P1/P2` shadow, while a separately typed Clifford--Morita index, tensored with
a genuine triplet, would be the only permitted route toward `P3`. Forgetting
the deck, domain, and coefficient structure returns the ordinary smooth
gamma-traceless bundle shadow, whose grading-determined index remains
unchanged. The bridge is not constructed because `S_nat` fails the
right-`H` deck gate and no replacement mirror intertwiner or physical-index
map exists.

### First falsification test

The first test is executable by this probe: in the fixed native matrices,
require the proposed linear map `S_nat=C_perp J_H` to satisfy both
`S_nat^2=1` and `[S_nat,R_H]=0`. The conjunction fails exactly. Therefore this
specified candidate is falsified at admission; any successor is a new,
named-map candidate beginning with the source-owned B5 mirror intertwiner
below, not a phase repair of this one.

## Program-native choices and hostile controls

| component | program-native choice used | standard or planted control |
| --- | --- | --- |
| carrier | full `Cl(9,5)=M(64,H)` complex realization, then gamma-trace kernel | one `H` line and its conventional `H+H` double |
| pairing | indefinite Krein `K`, composed into `C_perp` | Euclidean transpose/adjoint in the finite Bott mass |
| deck candidate | `C_perp J_H` with no inserted phase | conventional `diag(1,-1)`; planted `i S_nat` |
| naturality | invariance under the full carrier, tested by a mixing permutation | planted rank-one coordinate projector |
| topology | full `H^64` direct-sum density | one-line degree-one clutching is a standard input |
| count | left OPEN as a physical Fredholm/chiral index | copy count `64`, and `192` after a formal rank-three tensor, are not called generations |

## Executed admission gate

### 1. Native algebra

The probe reconstructs the factorized signed Clifford representation

```text
Cl(9,5) = Cl(3,1) hat-tensor Cl(6,4),
```

the same finite realization used by the vertical--Krein weld. It obtains the
full quaternionic reality by composing full chirality with the raw real-gamma
product. The resulting `J_H` squares to `-1` and commutes antilinearly with all
14 Clifford generators. `C_perp` squares to `+1`.

For two antilinear maps `C` and `J`, their linear product has unitary part
`S=C J`. Here the matrices give

```text
S_nat^2 = +1,
S_nat J_H = - J_H S_nat,
(i S_nat)^2 = -1,
(i S_nat) J_H = J_H (i S_nat).
```

This is also algebraic, independent of the chosen matrices. If
`C^2=+1`, `J^2=-1`, and `(CJ)^2=+1`, then `CJ=-JC`, hence `CJ`
anti-commutes with `J`. Conversely, if `CJ` commutes with `J`, then
`C` commutes with `J` and `(CJ)^2=-1`. A phase can exchange the two
conditions but cannot satisfy both.

**Gate verdict: `KILL` for `S_nat` as a right-`H`-linear deck involution.**

### 2. RS preservation, honestly bounded

Conjugation by `S_nat` returns every Clifford generator with a sign:

```text
S_nat gamma_a S_nat^-1 = r_a gamma_a,    r_a in {+1,-1}.
```

Let the vector factor transform by `R=diag(r_a)`. The probe verifies block by
block

```text
Gamma (R tensor S_nat) = S_nat Gamma.
```

Therefore `R tensor S_nat` preserves `ker Gamma`. This is a positive native
result, but it is a statement about the deck candidate, not a Bott mass.
Because no map embeds the doubled Bott mass into the existing GU carrier, the
tests

```text
[M_GU(q), P_RS] = 0
and
gap(P_RS M_GU(q) P_RS) > 0
```

are not yet expressible. They are reported OPEN, not failed and not passed.

### 3. Standard Bott control and planted comparator

On one quaternionic line the probe independently reproduces

```text
C_B(q)^*=C_B(q),       C_B(q)^2=1,
[C_B(q),R_H]=0,
S_B C_B(q) S_B^-1=C_B(-q),
min singular value(C_B(q))=1
```

at `q=(1,1,1,1)/2`. This shows the harness does not reject the conventional
construction merely because the native admission fails.

For the clutching map `q->L_q`, the alternating local cubic trace on the
three quaternionic tangent generators is nonzero. The diagonal `H^64`
extension scales it exactly:

```text
density(H line) = -24,
density(H^64)   = -1536 = 64(-24).
```

This is direct-sum multiplicity. The probe does not integrate it into a new
degree calculation and does not infer any Fredholm index. A planted
one-coordinate projector gives the one-line density, but its commutator with
a carrier permutation is nonzero. Thus “take one copy” is precisely the
non-natural move the gate was designed to catch.

## Choice count and constraint surplus

The proposed `S_nat` has one conservative relative `U(1)` phase choice before
normalization. Two independent expressible constraints were preregistered:

1. square `+1` as a deck involution;
2. right-`H`-linearity.

The gate-level surplus is therefore

```text
2 independent constraints - 1 phase choice = +1.
```

The positive-surplus fit fails: phases `1` and `i` satisfy opposite
constraints, and the algebra proves no phase satisfies both.

For the whole Bott--Krein construction, surplus is
`SURPLUS-UNCOMPUTABLE`. The native mirror embedding, Bott mass, common
domain, Clifford--Morita map, and physical-index normalization have not been
declared, so neither their parameter count nor the rank of their constraints
can be counted without hiding choices.

## Typed verdict

```text
KILL-S_NAT-H-LINEAR-DECK
FULL-CARRIER-BOTT-OPEN-AT-NATIVE-MIRROR-AND-MORITA-MAP
```

Proved by the probe:

- the proposed product is an involutive Krein symmetry but not right-`H`-linear;
- its induced action preserves the gamma-trace kernel;
- the standard doubled `H`-line control remains sound;
- the natural diagonal carrier has 64 copies of the local clutching density;
- selecting one coordinate is non-natural.

Not proved:

- a Callias or Fredholm index;
- an RS-preserving native Bott mass;
- a physical generation count;
- a canonical division by 64;
- an identification of the auxiliary Bott double with a GU mirror pair.

## Next smallest source-owned map

Do not begin a Callias-domain proof yet. First construct or fail to construct
an intertwiner from the conventional Bott double to an already-existing GU
mirror pair:

```text
iota : (H+H) tensor_H S  ->  E_mirror subset E_GU
```

with no new degrees of freedom, such that

```text
iota S_B = S_mirror iota,
iota C_B^64(q) = M_GU(q) iota,
[S_mirror,R_H]=0,
Gamma M_GU(q) P_RS=0.
```

The source-owned candidate for `E_mirror` is the normalized B5 dual-slot
pairing, because it already owns the mirror provenance. If no such
right-`H`-linear involution and dimension-matched embedding exist, the
full-carrier Bott route is killed without spending an analytic-domain swing.
If they do exist, the next gate is the compressed mass gap, followed only
then by a named Clifford--Morita pushforward and a common Callias domain.

## Reproduction

```bash
python3 tests/channel-swings/bott_krein_full_carrier_admission_probe.py
```

The probe uses NumPy, is deterministic, performs no writes, and prints a JSON
receipt. Exit zero means all controls reproduced the typed kill/open boundary;
it does not mean the candidate was admitted.
