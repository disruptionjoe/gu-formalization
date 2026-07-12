# Path-3 Branch C -- the K-theory / cobordism construction of the generation count

**Blind wave, Path 3 ("why three generations?"). Branch C = cobordism / K-theory (Garcia-Etxebarria-Montero;
Wan-Wang-Yau; Freed-Hopkins). 2026-07-11.**
Test: `tests/W57_path3_C_cobordism.py` (deterministic, exact arithmetic, no GU machinery imported, exit 0).
Grade: **argument/theorem-grade for the LOCATES verdict and the class-wide no-go; the arena facts are
cited-from-literature (Toda/Adams/Freed-Hopkins/GEM/WWY), the arithmetic on top is COMPUTED.**

This branch is run 5-persona inline (computer / referee / adversary / cross-checker / synthesizer). It is
deliberately blind to the other branches; it delivers only branch C's graded verdict.

---

## 0. Fork discipline (required by `GEOMETER-VS-PHYSICS-OBJECTS.md`)

The object "the count" has two constructions. This branch uses the **program-native / geometer side**: the
count as a **torsion cobordism class** in a 3-primary summand, **not** the standard-physics integer index.
The table's "Generation count" row settles this fork toward the torsion side and records the reason:
`Hom(Z/3, Z) = 0`, so a Z-valued index provably cannot reach the torsion arena (H6). Everything below is
derived in the **torsion-class construction**; where a claim would differ in the integer-index construction
it is flagged. The two constructions do not communicate (that non-communication is itself `Hom(Z/3,Z)=0`).

---

## 1. Persona 1 -- the COBORDISM / K-THEORY COMPUTER: the group and its 3-primary summand

**Anomaly classification (Freed-Hopkins).** Deformation classes of reflection-positive invertible field
theories in dimension `d` with symmetry type `H` are classified by the torsion of the Anderson-dual bordism
group `[MTH, Sigma^{d+2} IZ]` plus a free part -- concretely, for a 4d theory the anomaly lives in the 5d
bordism group `Omega^{H}_5(target)`. Anomaly-free fermion content = a class on which every bordism invariant
(the Dai-Freed phases) vanishes. This is the K-theory/cobordism construction of "the count": the generation
datum is a **class in this bordism group's torsion**.

**The relevant group and its 3-primary part.** For the gravitational framing channel the count is carried by
the image of the J-homomorphism in dimension 3, which is all of the third stable stem:

```
Omega^Spin_5(BG)  ⊃  (framing/im-J channel)  =  im J_3  =  pi_3^s  =  Z/24  =  Z/8 ⊕ Z/3   (CRT, Toda)
```

- `pi_3^s = Z/24` (Toda 1962; Serre finiteness). `|im J_3| = den(B_2/4) = den(1/24) = 24` (Adams, *J(X) IV*).
- CRT split `Z/24 ≅ Z/8 ⊕ Z/3` verified in the test as an explicit bijective homomorphism on all 24 classes.
- **3-primary summand = `Z/3`** (the 3-Sylow), exponent 3. **2-primary summand = `Z/8`** (the selector arena).
- The prime 3 in 24 is **von Staudt-Clausen**, not fitted: `den(B_2) = 6 = 2·3` picks up exactly the primes
  `p` with `(p-1) | 2`, i.e. `{2,3}`. It is number theory of `B_2`, provenance-distinct from `chi(K3)=24`.

**The count's class.** In the torsion construction the generation datum is a class `c ∈ Z/3` (the 3-primary
projection of the bordism/anomaly class). The physical "3 generations" is read as: `c` is a **nonzero** element
of `Z/3` (order 3). `3 = dim Λ²₊(R⁴)` (the three self-dual 2-forms in 4d) is the GU-native identification of
which `Z/3` this is; the arena arithmetic does not depend on that identification.

---

## 2. Persona 2 -- the MATH REFEREE: grade each claim, LOCATES vs FORCES

| Claim | Grade | Locates or Forces |
|---|---|---|
| `pi_3^s = Z/24 = Z/8 ⊕ Z/3`, 3-Sylow `Z/3` | THEOREM (Toda/Adams, cited) + COMPUTED arithmetic | LOCATES the arena |
| Anomaly = homomorphism `eta: Omega_5 -> R/Z` (Freed-Hopkins) | THEOREM (cited) | structural |
| exponent of `Z/3` = 3 (modulus forced) | THEOREM (trivial) | **modulus forced, value not** |
| `Aut(Z/3) = Z/2` -> no canonical generator | THEOREM (COMPUTED) | blocks FORCE |
| SM per-generation Dai-Freed anomaly `= 0` (GEM/WWY) | cited result | LOCATES only (free for all N) |
| `Hom(Z/3, Z) = 0` (no Z-lift) | THEOREM (H6, COMPUTED) | blocks class->integer |

Referee's ruling: **every load-bearing structural fact is a genuine theorem; none of them FORCES the value 3.**
The single honest distinction the referee insists on: the group structure forces the **modulus** (the arena is
`Z/3`, arithmetic is mod 3, the number 3 appears as `|Z/3|`), and does **not** force the **value** (that the
physical count equals 3 rather than being some element `0,1,2` of `Z/3`, or a class in the `Z/8` part). This is
exactly the shape of "LOCATES, not FORCES."

---

## 3. Persona 3 -- the ADVERSARY: "the class / generator you picked is the free input"

The adversary presses on the choice. Three attacks, all of which the branch concedes as correct:

1. **"You chose the generator."** `Z/3` has two nonzero elements `{1,2}`, exchanged by the nontrivial
   automorphism `a ↦ 2a` (which is realized physically by charge conjugation / orientation reversal). A
   cobordism-**natural** invariant commutes with this automorphism, so it can only see the orbit `{1,2}` =
   "nonzero, order 3." It cannot single out one generator. **So identifying the count with a specific generator
   is an input, not an output.** CONCEDED.

2. **"You chose the Z-lift."** Even granting a generator, turning the order-3 class into the integer 3 needs a
   section `Z/3 -> Z`, which does not exist as a homomorphism (`Hom(Z/3, Z) = 0`). Reading "the order-3 class
   IS the number 3" is ill-typed. **The integer normalization is a second free input.** CONCEDED.

3. **"Anomaly cancellation won't rescue you."** The natural hope is that consistency (Dai-Freed anomaly
   cancellation) forces the generator. But the anomaly is a homomorphism, `eta(N·[1gen]) = N·eta([1gen])`, and
   GEM/WWY show `eta([1gen]) = 0` for the actual Standard Model (one generation is already Dai-Freed
   anomaly-free). Hence the anomaly vanishes for **all** N: consistency is **generation-blind**. **The free
   choice is not closed by any first-principles condition the cobordism framework supplies.** CONCEDED.

The adversary's conclusion (which the branch adopts): **the bordism class -- equivalently the choice of fermion
representation and its integer normalization -- IS the free input, and anomaly cancellation does not remove it.**

---

## 4. Persona 4 -- the CROSS-CHECKER: reproduce the GEM 3-primary location as a known result

Independent reproduction of the standard cobordism location, to confirm branch C sits on the literature:

- **Garcia-Etxebarria-Montero (arXiv:1808.00009, *Dai-Freed anomalies in particle physics*, JHEP 08 (2019)
  003).** They classify global (Dai-Freed) anomalies of the SM and its variants by computing `Omega^Spin_5(BG)`
  for `G = (SU(3)×SU(2)×U(1))/Z_k`. The 3-primary Dai-Freed data (the `Z/9`/`Z/3` odd-torsion entry in the
  family-puzzle census) is the **3-primary reach** used here. Load-bearing for branch C: **the SM per-generation
  Dai-Freed anomaly vanishes** -- their analysis finds the SM content anomaly-free including the beyond-cohomology
  invariants, so the mod-3 arena is **not** obstructed per generation.
- **Wan-Wang-Yau (2019/2020).** The beyond-cohomology `p_1` part of the SM cobordism data reaches `Z/3`; same
  3-primary arena, same generation-blindness of the cancellation condition.
- **Adams (1966).** `im J_3 = Z/24`, Adams `e`-invariant `e_KO` detects it, `e_KO(8ν) = 1/3 ∈ (Q/Z)_[3]` -- the
  concrete order-3 **locator** into the `Z/3` summand.

Cross-check verdict: the 3-primary location is **exactly** where GEM/WWY/Adams put the odd-torsion anomaly
data, `Z/3 ⊂ Z/24`. Branch C reproduces the location and adds nothing exotic. The one thing the literature is
unambiguous about and that is decisive here: **anomaly cancellation in these bordism groups does not fix the
generation number** (it cancels per generation, for any N). This matches the repo's prior FB-F4 finding (the SM
mod-3 anomaly arena is empty: `Theta_SM = 4`, integer, so `Omega^Spin_5(BG_SM) ⊗ Z_(3) = 0`).

---

## 5. Persona 5 -- the SYNTHESIZER: the graded verdict

**Construction of "the count" used:** the **torsion cobordism class** -- the count as a class in the 3-primary
summand `Z/3` of the 5d Spin-bordism/anomaly group `Omega^Spin_5(BG) ⊃ im J_3 = pi_3^s = Z/24`. (The torsion
side of the fork; NOT the integer index.)

**The group + its 3-primary summand:** `Omega^Spin_5(BG)`, framing channel `= im J_3 = pi_3^s = Z/24 = Z/8 ⊕
Z/3`; **3-primary summand `Z/3`** (3-Sylow), exponent 3.

### Q-force -- does the construction FORCE 3, or only CONSTRAIN it?
**LOCATES only.** The group structure forces the **modulus 3** (the arena is `Z/3`; the number 3 is `|Z/3|` =
its exponent = `dim Λ²₊(R⁴)`), and does **not** force the **value 3**. Reason: (i) `Aut(Z/3) = Z/2` exchanges
the two generators, so there is no canonical generator a natural invariant could select; (ii) the anomaly is a
**homomorphism** (Freed-Hopkins), so it constrains the count only up to an order (mod 3), never as a single
integer; (iii) for the SM the per-generation anomaly is 0 (GEM/WWY), so even that mod-3 constraint is empty.
Constraint delivered: "the count is a class in `Z/3`" -- i.e. it is defined **mod 3**. Nothing stronger.

### Q-extra -- minimal extra input that pins 3; first-principles or free?
The minimal extra input is a **choice of bordism class**: concretely **(a)** a distinguished **generator** of
the `Z/3` summand (equivalently, the choice of fermion representation whose anomaly class is that generator)
**plus (b)** an integer **Z-lift / normalization** turning the order-3 class into the integer 3. Neither is a
first-principles consistency condition: anomaly cancellation vanishes for all N (generation-blind), so it does
**not** pick the generator; and `Hom(Z/3, Z) = 0` means no cobordism invariant supplies the Z-lift. **The extra
input is a FREE MODEL-BUILDING CHOICE, not forced by anomaly cancellation.** (The lone way it could become
first-principles: a target whose Dai-Freed anomaly is a **nonzero** order-3 element -- then cancellation would
force `N ≡ 0 mod 3` -- but the SM's is zero, and even a nonzero one pins only a residue class, not the integer
3; see the positive control in the test.)

### Q-nogo -- can you prove no selector of your kind forces 3?
**Yes, class-wide, for cobordism/K-theory selectors of the anomaly-homomorphism kind.** A cobordism selector is
a natural homomorphism from the bordism group to a value group. Three independent obstructions each block
FORCING the integer 3:
1. **No canonical generator.** `Aut(Z/3) = Z/2` (realized by charge conjugation / orientation reversal) exchanges
   `{1,2}`; a natural invariant is fixed by it and sees only the orbit -- it detects **order 3**, never a value.
2. **No Z-lift.** `Hom(Z/3, Z) = 0` (and `Hom(Z/24, Z) = Hom(Q/Z, Z) = 0`, one level up): no Z-valued index
   reaches the torsion; the order-3 class has no integer preimage.
3. **Linearity.** The anomaly homomorphism `N ↦ N·eta([1gen])` constrains N only modulo the order of
   `eta([1gen])` -- at best a residue class mod 3, never a single positive integer, and for the SM the constraint
   is empty (`eta([1gen]) = 0`).
Therefore **no cobordism/K-theory anomaly selector forces the integer 3.** (Scope: this is a no-go for selectors
that are homomorphisms out of the torsion bordism group -- the class-as-count reading. It does **not** touch an
**integer-by-construction** relative/equivariant index, which lives in the free-abelian world where these
homomorphism obstructions are silent; that object is the other fork and is out of branch C's scope.)

### Confidence, load-bearing assumption, one overturning thing
- **Confidence: HIGH** for Q-force (LOCATES) and Q-extra (free choice); **MODERATE-HIGH** for the class-wide
  Q-nogo. The high-confidence legs rest only on Freed-Hopkins linearity, `Aut(Z/3)=Z/2`, `Hom(Z/3,Z)=0`, and
  GEM/WWY generation-blindness -- all standard.
- **Load-bearing assumption:** that "the count" is the **torsion cobordism class** (the fork choice). If instead
  the count is an integer index (the other construction), the no-go's leg (2) becomes the whole story
  (`Hom(Z/3,Z)=0` says the two forks do not communicate) and the analysis is different -- that is a different
  branch's object.
- **The one overturning thing:** exhibit a **first-principles consistency condition** in the relevant target --
  a Dai-Freed anomaly whose invariant is a **nonzero** element of the `Z/3` summand -- **together with** a
  separate condition fixing the Z-lift (e.g. a minimality/positivity bound forcing the count to the smallest
  positive representative). That would upgrade LOCATES to a genuine mod-3 forcing (and, with the bound, to the
  integer 3). The current literature shows the opposite (SM anomaly is generation-blind), so this is not in hand
  -- but it is the precise, falsifiable thing that would overturn branch C's verdict.

---

## 6. Bottom line

The cobordism / K-theory construction places the generation count exactly where GEM / Wan-Wang-Yau / Adams put
the odd-torsion anomaly data: the `Z/3` summand of `Omega^Spin_5(BG) = im J = pi_3^s = Z/24`. The **group
structure forces the modulus 3** (the arena is `Z/3`) but **not the value 3**. Pinning the value needs a free
model-building choice -- a generator of `Z/3` plus an integer normalization -- and **anomaly cancellation, the
only first-principles condition the framework supplies, is generation-blind (GEM/WWY) and does not force it.**
Class-wide, no cobordism selector of the anomaly-homomorphism kind can force the integer 3 (`Aut(Z/3)=Z/2` +
`Hom(Z/3,Z)=0` + linearity). **Verdict: LOCATES, does not FORCE.** This corroborates the repo's standing
"located, not forced" posture from the specific vantage of the cobordism construction; it changes no canon,
status, or verdict.
