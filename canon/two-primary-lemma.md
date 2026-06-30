---
title: "The 2-primary lemma: why the generation-sector no-go is structurally blind to an odd generation count"
status: active
doc_type: theorem
created: 2026-06-28
grade: "proof-grade (elementary, given the cited results); GU-INDEPENDENT -- the airtight core that survives a hostile referee regardless of GU"
depends_on: [canon/h2-base-index-chirality.md, canon/ghost-parity-krein-synthesis.md, canon/leg3-closure-and-spinor-2smoothness.md, canon/boundary-einvariant-and-the-tangential-fork.md]
---

# The 2-primary lemma

This is the most defensible, Geometric-Unity-independent statement in the generation-sector program. It is
a meta-theorem about the program's own obstructions, and it explains, structurally, why a correct no-go can
nevertheless miss an odd generation count. It survives a referee who rejects GU outright, because it is a
statement about Clifford Rarita-Schwinger sectors and stable homotopy, not about GU.

## Definitions

Call an integer / torsion invariant **2-primary** if it is a power of two, a multiple of a power of two, or
a statement modulo a power of two (equivalently, it lives in or constrains only the 2-primary part of an
abelian group). An obstruction is 2-primary if the quantity it constrains is.

## The lemma

**Lemma.** *Every obstruction established in the generation-sector no-go is 2-primary.*

**Proof (enumeration).** The program's obstructions, with the reason each is 2-primary:

1. **Quaternionic / Kramers wall (`J^2 = -1`).** A quaternionic structure forces complex dimensions to be
   even; "the complex dimension of a quaternionic representation is even" is Kramers' theorem. This is a
   `Z/2` statement. [2-primary]

2. **Real / pseudoreal non-chirality.** A real or pseudoreal representation yields a non-chiral (vanishing
   mod-2 index) fermion content; the relevant Witten mod-2 index is `Z/2`-valued. [2-primary]

3. **Cross-chirality Krein signature.** The `so(p,q)`-invariant form on the generation triplet is purely
   cross-chirality, with signature exactly `(+96, -96)`; the even split is a power-of-two balance, and the
   net chirality it forces is `0`. [2-primary]

4. **The adjoint Dirac index `4k`.** Gauging the real self-dual adjoint by a charge-`k` instanton gives
   Dirac index `2 T(adjoint) k = 4k`, divisible by 4; over the full 16-dim multiplicity bundle the index is
   `12k` or `24k` (still even). [2-primary]

5. **Rokhlin's theorem.** The gravitational (untwisted) contribution involves `sign(X) = 0 (mod 16)`, a
   statement modulo `2^4`. [2-primary, standard theorem]

6. **The spinor 2-smoothness lemma.** A family/internal space entering as a spinor of `SO(m)` has dimension
   `2^floor(m/2)` (or `2^(k-1)` for a half-spinor): a power of two, hence 3-free; the only route to an odd
   multiplicity is a non-spinor (vector / adjoint / self-dual) family representation. [2-primary, proved]

7. **The ghost-parity no-go.** A ghost-parity / fundamental-symmetry resolution of the Krein hyperbolic
   pairs gives a physical sector that is exactly `50/50` in chirality (net `0`), and the only chiralizing
   alternative is a non-physical (non-Dirac) invariant form. The obstruction is the even cross-chirality
   structure of (3). [2-primary]

Every item is a power-of-two or mod-`2^k` statement. There is no odd-prime content anywhere in the program.
QED.

## Corollary (the blindness)

**Corollary.** *The generation-sector no-go is structurally incapable of constraining the 3-primary
(odd-torsion) part of any invariant in which the generation count might live.*

**Proof.** An obstruction that is a power-of-two or mod-`2^k` statement constrains only the 2-primary part
of an abelian group; it places no condition on the odd torsion, because the odd-torsion summand is a direct
complement (Chinese Remainder Theorem) on which every mod-`2^k` map is determined by the 2-part alone. The
generation count `3`, being odd, lies in the 3-primary summand. Concretely, the natural home of a
homotopy-theoretic generation count is the framed-bordism / `e`-invariant group `pi_3^s = Z/24 = Z/8 (+)
Z/3` (with `|Im J_3| = 24 = denom(B_2/4)`, Adams). The program's obstructions all live in the `Z/8`
(2-primary) summand; the `Z/3` summand is untouched, because `3` is coprime to `2`. QED.

## Significance

The no-go and the generation count are **complementary, not contradictory.** The program proved a large,
correct body of 2-primary facts -- the matter content is vectorlike, the native index is even, the count is
not internally forced by any mod-2 obstruction -- and, by construction, none of it could ever have
constrained an odd count. If the generation number is a homotopy / framed-bordism invariant, it lives in
the 3-primary sector that the entire program is blind to. This is why "the count is 3" was never going to
be reachable from inside the even/closed interior, and why, if a count appears at all, it must appear in a
place (a boundary `e`-invariant; see `canon/boundary-einvariant-and-the-tangential-fork.md`) that carries
odd torsion -- namely the gravitational framing channel `-p_1/24`, whose denominator `24` contains the
von Staudt-Clausen `3`.

## Why this is the GU-independent core

Nothing above mentions a specific physical theory. The lemma and corollary are statements about (i) the
obstructions of an explicit Clifford Rarita-Schwinger sector and (ii) the arithmetic of `pi_3^s = Z/24`.
A referee who rejects Geometric Unity entirely still has to accept them. They are the part of the program
that stands on its own, and they reframe the chirality-from-unification problem in a genuinely new way:
*a no-go assembled from mod-2 statements is structurally blind to an odd generation count, and the count, if
it exists, is a 3-primary boundary invariant.* The GU reading (does the boundary class actually carry the
odd part?) is then a separate, motivating question layered on top.

## Correction (hardening audit, 2026-06-28)

A web-enabled hardening audit (`lab/deep-research/hardening-report-batch-2026-06-28.md`, prompt 3) confirms the
operative spine -- no hidden odd-prime MODULAR obstruction anywhere -- but corrects two overstatements:

1. **"No odd-prime content, QED" is too strong.** The integer 3 DOES appear, as a MULTIPLICAND, in the
   dimensions (`96 = 2^5 * 3`, the bundle indices `12k`, `24k`, and `|Weyl(D7)| = 2^10 * 3^2 * 5 * 7`). The
   true, narrower statement: no obstruction is an odd-prime CONGRUENCE / modular condition; the 3 is a factor
   of even numbers, never a `mod 3` constraint. Read the lemma as "no odd-prime modular obstruction."

2. **For the two INTEGER-valued items the blindness is an invariant/group MISMATCH, not modular blindness,
   and is CONTINGENT.** For the exact adjoint index `4k` and the net-chirality `0`, the integer Atiyah-Singer
   index pins every prime; under a literal integer-index reading, `net = 0` would FORBID `3`. The "blindness
   to 3" is purchased by relocating the count to the TORSION boundary e-invariant in `pi_3^s = Z/24 = Z/8
   (+) Z/3` (the 3 entering via von Staudt-Clausen). So the COROLLARY "the no-go cannot see the count 3" is
   not unconditionally GU-independent -- it holds only under the torsion-count reading, which is the
   reconstruction-grade tangential premise. The mod-2 LEMMA itself (every obstruction is even / mod-`2^k`) is
   GU-independent and stands; the corollary's force depends on the torsion-count reading.

Net: the spine survives (the program is genuinely 2-primary, no hidden odd-prime modular obstruction); the
slogan tightens to "a no-go built from even / mod-2 statements cannot impose an odd-prime congruence, and
under the torsion-count reading is blind to the order-3 part," with the contingency stated.
