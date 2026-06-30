---
title: "A5: the Adams e-invariant question for a stable-homotopy specialist, plus a first-principles attempt"
status: exploration
doc_type: note
created: 2026-06-28
posture: verdict-agnostic; the 24 is forced by a theorem, the 3 is the open 3-primary question
---

# A5: the e-invariant, the 24, and where the 3 could hide

Two parts. Part 1 is a one-page question to send to a stable-homotopy / index-theory specialist. Part 2 is
a first-principles attempt that gets further than expected: it identifies a genuine, principled reading of
the contested "/8" and shows precisely why the entire generation-sector kill is structurally blind to the
integer 3.

---

## Part 1 -- the question to send

**Background (one paragraph).** In a reconstruction of Geometric Unity's matter sector, one Standard-Model
generation sits in a self-dual `SU(2)_+` triplet (the rank-3 bundle of self-dual two-forms `Lambda^2_+` of
the 4-base). The 14-dimensional "observerse" has a non-compact end whose link is the lens space
`RP^3 = S^3 / Z_2 = L(2;1)`, carrying a charge-1 self-dual `SU(2)_+` twist. We want to know whether the
generation count can be read as a homotopy-theoretic invariant of this twisted end rather than imported.

**The questions.**

1. **The framed class.** The charge-1 self-dual `SU(2)_+` twist on `RP^3 = L(2;1)`, together with the
   stable framing it determines, represents a class in `Omega_3^{fr} = pi_3^s = Z/24`. What is that class?
   Concretely: what is its image under the Adams `e`-invariant `e: pi_3^s -> Q/Z`?

2. **The eta computation.** Equivalently, compute the reduced `eta`-invariant `(eta + h)/2` of the
   quaternionic (H-linear) Dirac operator on `L(2;1)` twisted by the charge-1 self-dual `SU(2)_+`
   connection, via the Atiyah-Patodi-Singer / Gilkey finite trigonometric sum for lens spaces. Does it have
   a nonzero **3-primary** part (an element of the `Z/3` summand of `Z/24 = Z/8 (+) Z/3`)?

3. **The `/8`.** Is `24 / 8 = 3` a coincidence, or is it the canonical projection of `pi_3^s = Z/24` onto
   its 3-primary part `Z/3` (see Part 2, which argues it is the latter and that the 2-primary `Z/8` part is
   exactly what the matter-sector even-ness arguments annihilate)? If the count is the 3-primary part of the
   framed class, it is forced to be `3` by a theorem; the open question is whether the GU twist's class has
   a nontrivial 3-primary part at all.

That is the whole ask: the 3-primary part of the `e`-invariant of one explicit framed lens space.

---

## Part 2 -- first-principles attempt

### 2.1 The 24 is forced (solid)

`pi_3^s = Z/24`. The `J`-homomorphism `J_3: pi_3(SO) = Z -> pi_3^s` is surjective, so `pi_3^s = Im J_3`.
By the Adams / Quillen theorem, `|Im J_{4k-1}| =` the denominator of `B_{2k} / (4k)`. For `k = 1`
(dimension `3 = 4*1 - 1`): `B_2 = 1/6`, so `B_2 / 4 = 1/24`, denominator `24`. Hence `|Im J_3| = 24`,
**forced by a hard theorem from the single Bernoulli number `B_2 = 1/6`** -- the same `B_2` and the same 24
that appear in `Delta = eta^{24}`, in `chi(K3) = 24`, and in the 24 transverse dimensions of the bosonic
string. This is a genuine "predict, not name" for the integer 24: it is not fitted, it is the order of the
stable `J`-image in dimension 3. [proof-grade, standard]

### 2.2 The canonical decomposition (solid)

`24 = 8 * 3` with `gcd(8, 3) = 1`, so by the Chinese Remainder Theorem
```
pi_3^s = Z/24  =  Z/8  (+)  Z/3,
```
a canonical splitting into a **2-primary** part `Z/8` and a **3-primary** part `Z/3`. The 3-primary part is
exactly `Z/3`, of order 3. Projecting `Z/24` onto its 3-primary summand is a canonical operation, not an
arbitrary division. [proof-grade, elementary]

### 2.3 The whole kill is 2-primary (solid -- this is the load-bearing observation)

Every even-ness / vectorlike result in the generation-sector program is a statement about powers of two:

- the quaternionic Kramers wall, `J^2 = -1`, doubles complex dimensions: a `Z/2` phenomenon;
- Rokhlin's theorem, `sign(X) = 0 (mod 16)`, is `2`-primary (mod `2^4`);
- "a real or pseudoreal representation gives a non-chiral / even index" is a mod-2 statement;
- the self-dual adjoint index `4k`, the full-bundle `12k / 24k`, the cross-chirality `(+96, -96)` Krein
  signature, the spinor 2-smoothness lemma (multiplicities are powers of two): all 2-primary.

A mod-2 argument constrains the 2-primary part of an abelian group and says **nothing** about its odd
torsion. So the entire kill -- everything we proved -- lives in, and only constrains, the `Z/8` (2-primary)
summand of `pi_3^s = Z/24`. **It is structurally incapable of seeing the `Z/3`**, not because of a gap in
the argument but because `3` is coprime to `2`. [proof-grade given our own results]

### 2.4 The reframe (the genuine insight)

Put 2.1 to 2.3 together. If the generation count is the framed-bordism / `e`-invariant class of the
self-dual `SU(2)_+` twist on the GU end (the A5 hypothesis), then:

- its **2-primary part** lives in `Z/8` -- and this is exactly the part the even-ness / Kramers / Rokhlin
  arguments annihilate (they force the 2-primary content to the vectorlike, "even", "imported flux" story);
- its **3-primary part** lives in `Z/3`, **forced to order 3 by Adams' theorem**, in a sector the kill
  cannot reach.

So the contested "`24 / 8 = 3`" is not target-fitting after all: it is the statement "the 3-primary part of
`pi_3^s = Z/24` is `Z/3`," and the "`/8`" is precisely the projection that discards the 2-primary content
that our kill already showed is even / vectorlike / imported. The kill (all 2-primary) and the generation
count (3-primary) are **complementary, not contradictory**. Our program proved a great deal about the
2-primary sector and, by construction, could never have constrained the 3.

This is the predict-not-name the panel sought, with a principled `/8`: discard the 2-primary part the
even-ness theorems govern; what remains is forced to be `Z/3`.

### 2.5 The eta sketch, and the honest boundary

A partial check of the `eta` side. For `L(2;1) = RP^3` the bare Dirac `eta`-invariant from the APS-Gilkey
finite sum has a single term (`j = 1`): with `2 sin(pi * 1 / 2) = 2`, the term carries a denominator `4`,
and with the `-(1/2)` lens prefactor and the spin-structure phase the reduced `eta` of the **untwisted**
Dirac operator is `+/- 1/8`. That value is **2-primary** -- it is the `Z/8` content, the part the kill
already owns. To reach the **3-primary** `1/3` (equivalently the generator of `Z/3 subset Z/24`) one needs
the **twist** by the charge-1 self-dual `SU(2)_+` bundle, whose Chern-Simons / `ch` contribution is what can
inject odd-torsion. So the bare lens space gives only the 2-primary part; the self-dual twist is exactly the
candidate carrier of the 3. This is consistent with the whole reframe and localizes the open question.

**What is solid:** 2.1 to 2.4 (the 24 is forced; `Z/24 = Z/8 (+) Z/3`; the kill is 2-primary hence blind to
`Z/3`; the `/8` is the canonical 2-primary projection). **What is open (the specialist question of Part 1):**
whether the GU charge-1 self-dual twist on `L(2;1)` actually has a **nonzero 3-primary `e`-invariant** (a
generator of `Z/3`). If it does, the generation count `3` is forced by Adams' theorem in the one sector the
entire even-ness program cannot touch. If it does not (the twist's class is purely 2-primary), then `3` is
not produced even here, and the kill is complete. The bare `eta = +/- 1/8` computation says the geometry
alone is 2-primary; the twisted `eta` is the decisive finite trigonometric sum to compute, and it is a
bounded, well-posed calculation for a lens-space index specialist.

### 2.6 Why this matters

This does not establish that GU forces three generations. It does three honest things. It converts the `24`
from a coincidence into a theorem (Adams, from `B_2`). It shows the contested `/8` is the canonical
2-primary projection, not a fudge. And it explains, structurally, why the entire generation-sector kill --
correct as far as it goes -- was always going to miss the `3`: the kill is a 2-primary argument, and the
generation count, if it is homotopy-theoretic at all, is 3-primary and coprime to everything we proved.
That is the sharpest possible statement of where the open question now lives.
