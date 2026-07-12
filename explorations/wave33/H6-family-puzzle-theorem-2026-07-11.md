# H6 -- The GU-independent family-puzzle theorem

**Wave 33. 2026-07-11. GU-INDEPENDENT, world-facing, durable-standalone.**
Test: `tests/wave33/H6_family_puzzle_theorem.py` (deterministic, exit 0, imports nothing from the GU
machinery on purpose). Grade: **PROVEN** (elementary given the stable-homotopy census; arena-independent).

This is the durable result that survives regardless of GU's fate. Across the count campaign (H37 count
no-go, H19 the (7,7) branch, H38 the Z/3 chiral selector, the double-major sweep) one proposition kept
recurring that is true of **any** theory whose generation count is located in a torsion class: a selection
principle forcing the count into the order-3 (mod-3) class must itself be 3-primary. H6 states it cleanly,
proves it, and verifies the census.

---

## 1. The theorem (self-contained; well-posed to a stable-homotopy theorist)

**Setup.**

- A **count carrier** is a finite abelian group `A` with a nontrivial 3-Sylow `A_(3)`. The canonical arena
  is `A = pi_3^s = Z/24 = Z/8 (+) Z/3` (Toda), with `A_(3) = Z/3`.
- A **count** is a class `c in A`. It is **3-primary-nontrivial** iff its 3-primary projection
  `pi_3(c) in A_(3)` is nonzero (equivalently, the count is `!= 0 mod 3`). The physical target "3
  generations" sits exactly here: `3` generates the `Z/3`.
- A **selection principle** (selector) is a group homomorphism `phi : A -> V` into an abelian **value
  group** `V` -- the arena the selector actually measures in (a signature in `Z/8`, a Dirac index in `Z`,
  a ghost parity in `Z/2`, an `e`-invariant in `Q/Z`, ...). The selector **forces / detects** the 3-primary
  count iff it separates `pi_3(c)` from zero: `phi` restricted to `A_(3)` is nonzero on `pi_3(c)`.

**Theorem (Selector 3-primary necessity).**
> If a selector `phi : A -> V` forces a 3-primary-nontrivial count, then `phi` has **nonzero 3-Sylow
> image**: `phi|_{A_(3)} != 0`, equivalently `im(phi)` contains an element of order 3.
>
> Contrapositive (the operative no-go): a selector whose value group `V` is **(a)** a finite 2-group (any
> `Z/2^k`), or **(b)** torsion-free (a free-integer index, e.g. Dirac / Atiyah-Singer, or a signature in
> `Z`), **cannot** force a 3-primary-nontrivial count, because `Hom(A_(3), V) = 0`.

The conclusion is a statement about the **kind** of selector. It does **not** produce the integer 3 (see
Section 5).

---

## 2. The proof (COMPUTED vs ARGUED, per step)

Write the primary/CRT decomposition `A = A_(3) (+) B`, `B` the prime-to-3 part (for the canonical arena
`Z/24 = Z/3 (+) Z/8`). Let `pi_3 : A -> A_(3)` be the canonical projection.

**Step 1 -- the arena splits (COMPUTED).** `24 = 8 * 3`, `gcd(8,3) = 1`, so by CRT `Z/24 ~= Z/8 (+) Z/3`,
and the two summands intersect only at `0`. Verified in the test by constructing the explicit isomorphism
`k |-> (k mod 8, k mod 3)` and checking it is a bijective homomorphism on all 24 elements (`Q1a`, `Q1b`).
The 3-Sylow is `Z/3`, with order-3 elements `{8, 16}` (`Q1c`).

**Step 2 -- to force the count, the selector must be nonzero on `A_(3)` (ARGUED, trivial).** The 3-primary
information of `c` is `pi_3(c) in A_(3)`. Separating `pi_3(c) != 0` from `0` requires `phi|_{A_(3)} != 0`.
This is immediate from linearity: if `phi|_{A_(3)} = 0` then `phi(pi_3(c)) = 0`.

**Step 3 -- the two blindness facts (COMPUTED).** A homomorphism out of the finite 3-group `A_(3)`:
- into a finite 2-group: `|Hom(Z/3^a, Z/2^b)| = gcd(3^a, 2^b) = 1` -- only the zero map (`Q2a`).
- into a torsion-free group: `Hom(finite, Z) = 0`, because a finite-order element maps to a finite-order
  element of a torsion-free group, and the only such element is `0` (`Q2b`).

Both are `Hom(A_(3), V) = 0`. Note the **direction is load-bearing**: the vanishing is `Hom(3-group -> V)`,
not the reverse. `Hom(Z, Z/3) = Z/3 != 0`, so the statement is genuinely about the value group's primary
type, and the free-group leg uses finite-to-free (not free-to-finite).

**Step 4 -- assemble (ARGUED).** If `V` is 2-primary or torsion-free, Step 3 gives `phi|_{A_(3)} = 0`,
so by Step 2 the selector cannot force the count. Contrapositive: forcing it requires `phi|_{A_(3)} != 0`,
i.e. a nonzero 3-Sylow image. **QED.**

**Step 5 -- verified on the concrete arena, both legs (COMPUTED).** Modelling selectors as the actual
homomorphisms `Z/24 -> Z/target` (a hom is fixed by the generator's image, valid iff `24*t = 0 mod target`),
the test confirms:
- **No-go leg:** every selector into `Z/2^k` and into `Z` fails to separate the mod-3 class `c3 = 8`
  (`Q3a`, `Q3b`).
- **Positive control:** a 3-primary-reaching selector `Z/24 -> Z/3, Z/9, Z/24` does separate it, and the
  concrete Adams witness `e_KO : pi_3^s -> Q/Z` with `e_KO(nu) = 1/24` gives `e_KO(8 nu) = 1/3`, a genuine
  order-3 element of `Q/Z` (`Q3c`). The e-invariant is the **locator**: the tool that reaches the `Z/3`.
- **Theorem** (`Q3d`): exactly the 3-primary-reaching value groups can force the mod-3 count; all
  2-primary / free ones cannot.

The positive control matters: it shows the no-go is **not a universal wall** but a property of the value
group's primary type. A correct no-go that could still *never* be evaded would be a red flag; this one is
evaded exactly by the 3-primary tools the census identifies.

---

## 3. The census, verified against primary sources (Q4)

The theorem's canonical arena rests on standard stable-homotopy / K-theory facts. Each is stated with its
primary source; the arithmetic (denominators, Sylow orders, CRT) is COMPUTED in the test, the group
identifications are ARGUED-from-literature (cited, not re-derived from spectra).

| Fact | Value | Status | Primary source |
|---|---|---|---|
| `pi_3^s = pi_{n+3}(S^n) = Z/24` (`n >= 5`) | `Z/24` | cited; `24 = 8*3` COMPUTED | Toda, *Composition Methods in Homotopy Groups of Spheres*, Ann. Math. Studies 49 (1962); Serre finiteness; Ravenel, *Complex Cobordism and Stable Homotopy Groups of Spheres* (1986/2004), stable-stem tables |
| `pi_3^s = Z/8 (+) Z/3` (CRT) | split | COMPUTED (explicit iso) | CRT, `gcd(8,3)=1` |
| `J : pi_3(SO) = Z -> pi_3^s` is onto; `|im J_3| = den(B_{2}/4) = 24` | `24` | denominator COMPUTED (`B_2 = 1/6`) | J.F. Adams, *On the groups J(X) IV*, Topology **5** (1966) 21-71 |
| the prime `3` divides `24` by von Staudt-Clausen (`(3-1) = 2 \| 2`) | `den(B_2) = 6` | COMPUTED | von Staudt (1840), Clausen (1840); Adams' Bernoulli-denominator formula |
| 3-Sylow of `pi_3^s` (`= im J`) is `Z/3` (nonzero) | `Z/3` | COMPUTED | above |
| Adams `e`-invariant detects `im J`; `e_KO(8 nu) = 1/3 in (Q/Z)_[3]` | `1/3` | COMPUTED | Adams, *J(X) IV* (1966) |

The image of `J` is **all** of `pi_3^s = Z/24` (Adams: the `J`-homomorphism in dimension `4k-1` has order
`den(B_{2k}/4k)`; for `k=1`, `den(B_2/4) = den(1/24) = 24`). The prime 3 is not fitted -- it is forced into
the denominator by von Staudt-Clausen (`den(B_2) = prod` of primes `p` with `(p-1) | 2 = {2,3}`), pure
number theory of `B_2`.

**Census partition of the family-puzzle toolkit (Q4d), each entry a standard result:**

| Tool | Value group | 3-Sylow reach | Force odd/mod-3 count? | Source |
|---|---|---|---|---|
| Dirac / Atiyah-Singer index | `Z` (free) | none | **no** | Atiyah-Singer 1963 |
| per-generation anomaly cancellation | `Z` (free) | none | **no** | Adler-Bell-Jackiw (std) |
| mod-2 Witten `SU(2)` anomaly | `Z/2` | none | **no** | Witten 1982 |
| Rokhlin invariant | `Z/16` | none | **no** | Rokhlin 1952; Kirby-Taylor |
| spinor 2-smoothness (dim `2^k`) | `2^k` | none | **no** | Atiyah-Bott-Shapiro 1964 |
| cross-chirality Krein signature | `Z` (free) | none | **no** | campaign (2-primary lemma) |
| **Adams `e`-invariant / `J`-homomorphism** | `Z/24` | **`Z/3`** | **yes** | Adams 1966 |
| **Garcia-Etxebarria-Montero Dai-Freed `Z/9`** | `Z/9` | **`Z/9`** | **yes** | GEM, JHEP 08 (2019) 003, arXiv:1808.00009 |
| **Wan-Wang-Yau beyond-cohomology `p_1` part** | reaches `Z/3` | **`Z/3`** | **yes** | Wan-Wang-Yau 2019/2020 |
| **equivariant Spin/KO `G`-index (order-3 rho)** | `Z/3` | **`Z/3`** | **yes** | campaign exhaustiveness |

The partition is **exact and predictive**: every tool that has ever constrained the generation number
reaches the 3-Sylow; every tool that fails is 2-primary or free. This is not a coincidence -- it is the CRT
disjointness of `Z/8` and `Z/3`. (Note: the GEM `Z/9` and Wan-Wang-Yau entries are cited as the standard
3-primary Dai-Freed / beyond-cohomology results; their exact physics content is literature, the 3-primary
*reach* is the load-bearing arithmetic and is what the census uses.)

---

## 4. Scope and status

- **Status: PROVEN, arena-independent.** The proof uses only the primary decomposition of a finite abelian
  group and coprimality (`Hom(Z/3, Z/2^k) = 0`, `Hom(finite, Z) = 0`). It holds for *any* finite abelian
  carrier with a nontrivial 3-Sylow -- re-verified in the test on `Z/12 = Z/4 (+) Z/3` as a second,
  unrelated arena (`Q5c`). It is not tied to GU, to `Z/24`, or to any particular theory.
- **Which class of theories it applies to:** any theory whose generation count is located in a torsion class
  carrying a `Z/3` (equivalently, any homotopy-theoretic / bordism / Dai-Freed setting whose count arena has
  nontrivial 3-Sylow). The GU instantiation (`A = pi_3^s`, the `-p_1/24` gravitational framing channel) is
  one instance; the theorem does not need it.
- **What it says:** it constrains the **kind** of selector -- a selection principle that forces a mod-3
  count *must* be 3-primary (must have nonzero 3-Sylow image). It thereby explains the entire success/
  failure pattern of the family-puzzle literature as CRT arithmetic, and predicts that any future 2-primary
  or free-integer construction is a dead end for forcing an odd/mod-3 count.
- **What it does NOT say:** it does not derive the number 3, and it does not assert that any tool *does*
  force the count. It is a necessary-condition (type) theorem, not an existence theorem.

---

## 5. Honest limits (the informal-to-rigorous gap, and what stays conjectural)

**(a) "Odd" is the wrong prime.** The campaign slogan was "forces an ODD count => nonzero 3-Sylow image."
Read literally this is **false**: oddness is a `mod 2` (2-primary) condition, and a `mod-2` selector detects
it *without any 3-Sylow content*. The test makes this concrete (`Q5a`): the parity selector
`Z/24 -> Z/2, phi(1) = 1` is a valid homomorphism that separates odd from even, yet sends the 3-Sylow class
`8` to `0` -- it is entirely 2-primary and blind to the mod-3 arena. The **rigorous theorem is the mod-3
(3-primary) statement**, not parity. In the family puzzle the target `3` is simultaneously odd *and* the
prime 3, which is where the loose "odd" language came from; the honest statement borrows the prime, not the
parity. This is the single most important informal-to-rigorous correction, and the theorem above is stated
in the correct (mod-3) form.

**(b) The theorem does not derive 3 (the order-3-class -> integer-3 gate stays OPEN).** A nonzero class in
`Z/3` is `mod-3` information; it is not the integer 3. Formally `Hom(Z/3, Z) = 0` (`Q5b`), so there is no
canonical map from an order-3 class to an integer count -- the identification "the order-3 carrier *is* the
number 3" is ill-typed. This is a genuine, separate open gate. H6 constrains the selector's kind; it leaves
the class -> integer reading untouched and unproven. (This is consistent with the campaign's standing
verdict: **located, not forced.** H6 hardens the "located" half into a clean theorem; it says nothing new
about "forced.")

**(c) What is cited vs proven-here.** The *theorem* is proven-here (elementary). The *arena* facts
(`pi_3^s = Z/24`, `im J = Z/24`) are proven-in-literature (Toda, Adams) and cited, not re-derived from
spectra; the arithmetic on top of them (denominators, Sylow orders, CRT, the Hom-vanishings, the census
partition) is COMPUTED in the test. The two "campaign" census rows (Krein signature, equivariant rho) are
this program's own results, flagged as such.

**(d) A subtlety in the conclusion's exact form.** The clean statement is about the selector's restriction
to `A_(3)`. If one instead takes a count class `c` with mixed primary parts (`c = c_3 + c_3'`), a selector
can have `phi(c) != 0` purely through the `c_3'` (prime-to-3) part without seeing `pi_3(c)`. The theorem is
therefore correctly stated as "forces the **3-primary** count `pi_3(c) != 0`" -- i.e. resolves the mod-3
residue specifically -- not merely "`phi(c) != 0`". The test's `phi_to_cyclic_sees_c3` isolates exactly the
3-primary class `c3 = 8` to make this precise.

---

## 6. Bottom line

`pi_3^s = Z/24 = Z/8 (+) Z/3` is a Chinese-Remainder splitting into disjoint arenas. Any selection principle
that forces the generation count into the order-3 arena must have nonzero 3-Sylow image; equivalently, no
2-primary (`Z/2^k`) or free-integer (Dirac-index / signature) selector can ever force a mod-3 count. This is
**PROVEN**, GU-independent, arena-independent, and it explains -- as pure CRT arithmetic -- why every
family-puzzle tool that ever constrained the generation number (`e`-invariant, GEM `Z/9`, Wan-Wang-Yau,
equivariant KO) is 3-primary-reaching and every one that failed is not. It constrains the **kind** of
selector; it does not derive the number 3 (that gate, `order-3-class -> integer-3`, stays open). The clean,
honestly-scoped proposition is the deliverable.
