---
artifact_type: exploration
status: exploration (pre-registered Node B2, simplex camp; five personas inline, one worker, no sub-agents; deterministic grade-decomposition probe, exit 0)
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (pre-registered Node B2: two-form/simplex test)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
title: "Node B2 (SIMPLEX camp) of the copies/simplex fork: does the trit's canonical Z/3 couple to the GRADE-2 antisymmetric (two-form) sector and is its three-ness the BOUNDARY of a 2-simplex? OUTCOME: B2-FAILS. Machine-checked Clifford grade decomposition of BOTH canonical order-3 operators of the frozen trit gives grade-2 content EXACTLY ZERO: the C-linear order-3 element omega*I is pure grade-0, and the genuinely quaternionic order-3 unit quaternion q = -1/2 + (sqrt3/2)J of Sp(1)_comm splits as grade-0 linear (-1/2 I) plus grade-6 antilinear ((sqrt3/2)C_J) -- commutant Clifford support is grades {0,6}, never grade 2. The projector is NOT blind: grade-2 genuinely hosts order-3 rotations (exp((4pi/3)Sigma_01) is order 3 and 3/4 grade-2) but the trit acts unlike them (omega*I FIXES every ray; the bivector rotation MOVES rays), matching the arena split R1-commutant (winds k=64, carries the trit) vs R2-spin/metric two-form (winds 0). SIMPLEX SHAPE also fails independently: a 2-simplex boundary is ORIENTED (transposing two vertices sends d[012] to MINUS itself) while the trit is UNORIENTED (both orderings admissible, a conjugate pair), and the trit carries no grade-2 face to bound. GRADE-3 DOOR does not rescue it: the grade-3 self-dual bridge's c=3 members are the ZERO class (order(J(192))=24/gcd(24,192)=1) so three-ness at grade 3 is trivial, and the trit's own carrier has zero grade-3 content. Control: filled 2-simplex H_1=0 vs hollow grade-1 triangle H_1=1 vs open path acyclic -- the filled-triangle/two-form signature is distinguishable from a grade-1 chain (the test has power). This is the F-NEITHER contribution on the simplex leg; B1 (copies) is the separate node."
grade: "exploration / strong on the machine content. The grade-2-zero result is exact arithmetic on the frozen rep (grade fractions 0.0 to 5.8e-34; C_J pure grade-6 to 1.000; the antilinear/linear split accounts for the full unit-quaternion norm as 1/4 grade-0 + 3/4 grade-6). The anti-blindness guard (grade-2 hosts a real order-3 element, 0.750) and the ray discriminator (0.513) are exact/near-exact. The simplex-shape and homology legs are exact linear algebra (boundary sign flip; H_1 ranks 0/1/0). The grade-3 arithmetic is exact integer (gcd). No tolerance load-bearing within ten orders of magnitude. The frozen inputs (trit = commutant twist R1, k=64, order-3 class; trit UNORIENTED; only frozen order-3 family element is omega*I) are CITED from torsion-generation-arena / trit-triage / k1-reframe, not re-derived. No claim/canon/verdict/posture movement. Zero em dashes."
construction: "Fork-typed per GEOMETER-VS-PHYSICS-OBJECTS.md. Program-native objects: the verified Cl(9,5)=M(64,H) rep e[a] and its quaternionic commutant Sp(1)_comm=span_R{I,iI,J,iJ} with J=C_J.conj; the trit character (3-Sylow {0,8,16} of Z/24=pi_3^s, from the arena's im-J computation); the so(9,5) grade-2 generators Sigma_ab=(1/4)[e_a,e_b] (rs_bicomplex). Standard machinery binding the construction: the Clifford grade (multivector) decomposition via the trace-orthonormal monomial basis; simplicial boundary maps / H_1; the S_3-orientation of a 2-simplex boundary; Adams im J = Z/24 (order arithmetic). Everything is R0_COND on the framed-reading fork, exactly as the arena and kill sequence are."
probe: tests/channel-swings/trit_simplex_node_b2_probe.py
related:
  - explorations/prereg-trit-symmetry-and-fork-2026-07-20.md
  - explorations/torsion-generation-arena-2026-07-20.md
  - explorations/torsor-k-sequence-2026-07-20.md
  - explorations/k1-reframe-pass-2026-07-20.md
  - explorations/dk-chirality-fork-2026-07-20.md
  - explorations/trit-triage-2026-07-20.md
  - tests/rs_bicomplex_spin95_connection_2form.py
  - tests/channel-swings/l1_assembly_probe.py
  - tests/channel-swings/n4_two_z3s_probe.py
sources:
  - "Adams, J.F., On the groups J(X) IV, Topology 5 (1966) 21-71 -- im J in pi_3^s = Z/24; the arena receptacle whose 3-Sylow {0,8,16} is the trit character (cited from the arena, not re-derived here)."
  - "Standard Clifford/multivector grade decomposition: Cl(9,5) = M(64,H), Lambda^*(R^14) as Spin(9,5)-module; the grade-p projector via the trace-orthonormal monomial basis."
  - "Simplicial homology: the oriented boundary maps d_1, d_2 and H_1 = ker d_1 / im d_2; a 2-simplex boundary is odd under vertex transposition (S_3-orientation)."
---

# Node B2 (simplex camp): is the trit a two-form / a 2-simplex boundary? B2-FAILS

## 0. The charge and the one-paragraph answer

The pre-registration (`prereg-trit-symmetry-and-fork-2026-07-20.md`, commit
cafcbc7) split the surviving trit readings into a copies camp (B1) and a
simplex camp (B2). B2 is the hypergraph persona's dissent, and the only reading
that would EXPLAIN the trit's three-ness rather than classify it: if the trit's
Z/3 couples to the grade-2 antisymmetric (two-form) sector and is the boundary
of one 2-simplex (a filled triangle), then its three-ness is a single
2-dimensional object and ties directly to the program's grade-3 transport door
and the torsion three-form. This node machine-checks that hypothesis on the
frozen material. **Outcome: B2-FAILS.** The trit's canonical Z/3 does not couple
to grade 2, is not the boundary of an oriented 2-simplex, and is not rescued by
the grade-3 door. Nothing moves in canon.

## 1. What "the trit's canonical Z/3" is, as a frozen object

Imported, not rebuilt (arena + triage): the trit's Z/3 is the order-3 class
`J(k=64)` in `im J = Z/24 = pi_3^s`, delivered by the COMMUTANT twist R1 on the
quaternionic carrier `H^64`; the metric / spin-lift sector (R0 = R2), where the
grade-2 so(9,5) rotations live, winds ZERO. The trit is UNORIENTED (both
character orderings `(0,8,16)` and `(0,16,8)` admissible, a complex-conjugate
pair) and its only order-3 element inside the frozen family-preserving structure
is the commutant scalar `omega*I`, a global phase that FIXES every ray
(`trit-triage`, af7425f).

The commutant is `Sp(1)_comm = span_R{I, iI, J, iJ}` with `J = C_J.conj`,
`C_J = e_1 e_3 e_5 e_7 e_10 e_12`. So there are exactly two types of order-3
element of the trit's own group:

- **Type 1 (C-linear):** `omega*I` (the only C-linear order-3 element; a phase).
- **Type 2 (quaternionic):** a genuine order-3 unit quaternion
  `q = -1/2 + (sqrt3/2) J` in `Sp(1)_comm` (`q^3 = 1`), whose linear matrix
  piece is `-1/2 I` and whose antilinear matrix piece is `(sqrt3/2) C_J`.

## 2. Leg (a): the grade decomposition -- grade-2 is EXACTLY zero

The Clifford grade-`p` content of an operator `X` is computed exactly against
the trace-orthonormal monomial basis `{E_A / ||E_A|| : |A| = p}` (probe function
`grade_frac`, power-validated on pure monomials: `I -> g0`, `e_0 -> g1`,
`e_0 e_1 -> g2`, `e_0 e_1 e_2 -> g3`, each reading 1.000 at its own grade, 0
elsewhere -- the two-form projector demonstrably fires on genuine bivectors).

Result, both types:

| Operator | g0 | g1 | g2 | g3 | g6 |
|---|---|---|---|---|---|
| Type 1 `omega*I` | 1.000 | 0 | **5.8e-34** | 0 | 0 |
| Type 2 linear `-1/2 I` | 1.000 | 0 | **0.0** | 0 | 0 |
| Type 2 antilinear `(sqrt3/2) C_J` | 0 | 0 | **0.0** | 0 | 1.000 (C_J) |

The quaternionic order-3 element's norm is fully accounted: `1/4` in grade 0
(the `-1/2 I` linear part) plus `3/4` in grade 6 (the `(sqrt3/2) C_J` antilinear
part, `C_J` a pure grade-6 monomial to 1.000). **The commutant's Clifford
support is grades {0, 6}. Grade-2 content is exactly zero on both order-3
operators.** This is the load-bearing kill of the simplex hypothesis: the trit's
Z/3 does not live in, and does not couple to, the antisymmetric two-form sector.

### 2.1 Anti-blindness guard (the test is not blind to grade 2)

A zero is only evidence if the projector could have seen a nonzero. It can:
grade-2 GENUINELY hosts order-3 elements. `g3 = exp((4pi/3) Sigma_01)` with
`Sigma_01 = (1/4)[e_0, e_1]` (a pure so(9,5) two-form, `grade_frac = 1.000`) has
`g3^3 = I` and lies `0.750` in grade-2. So a two-form order-3 object exists; the
trit simply is not one. The grade-2 = 0 is a real decoupling.

### 2.2 The discriminator (the trit is a different object than a bivector)

The bivector order-3 rotation `g3` and the trit's `omega*I` are categorically
different. `omega*I` FIXES every ray (`|<psi, omega psi>| = 1.000`, projectively
trivial); `g3` MOVES rays (`|<psi, g3 psi>| = 0.513`). The trit does not act as
any bivector rotation. This is exactly the arena split made concrete: the trit
rides R1 (the commutant, winds `k = 64`, carries the order-3 class), while every
grade-2 so(9,5) rotation rides R2 (the spin/metric sector, winds 0). A two-form
that carried the trit would have to act like the trit; none does.

## 3. Leg (b): the 2-simplex boundary is the wrong shape, twice

Two independent obstructions, both exact:

1. **Orientation.** A 2-simplex boundary `d[012] = [12] - [02] + [01]` is
   ORIENTED: transposing two vertices sends it to MINUS itself (an odd
   permutation of `S_3`), so the subgroup preserving the oriented boundary is
   only the cyclic `A_3 = Z/3`, and the boundary carries a native orientation.
   The trit is UNORIENTED (both orderings admissible). An unoriented Z/3 cannot
   BE the boundary of an oriented 2-simplex. (This dovetails with Node A: the
   unoriented trit is the full `S_3` on three interchangeable things, not the
   orientation-carrying `Z/3` of a filled triangle's boundary.)
2. **No face to bound.** By Leg (a) the trit carries zero grade-2 content, so
   there is no two-form "face" for a 3-cycle to bound in the first place.

## 4. Control (bound): the test distinguishes a filled triangle from a chain

Required demonstrated power: a genuine grade-1 chain must NOT present the
closed-triangle/two-form signature. Simplicial `H_1 = ker d_1 / im d_2`,
computed exactly:

- **Filled 2-simplex** (3 vertices, 3 edges, 1 face): `H_1 = 0` -- the 3-cycle
  bounds the face. This is the two-form signature.
- **Hollow grade-1 triangle** (3 edges, no face): `H_1 = 1` -- an unfilled
  1-cycle; a closed chain of grade-1 objects that bounds nothing.
- **Open 3-edge path** (three 1-forms in a path): acyclic, `H_1 = 0` but for the
  trivial reason (no 1-cycle at all).

The test tells a filled triangle (`H_1 = 0` with a 2-cell) from a grade-1 chain
(`H_1 = 1` hollow, or acyclic path). The trit, carrying zero grade-2, patterns
with the UNFILLED side: no face exists. The control has teeth and the trit fails
the filled signature.

## 5. Leg (c): the grade-3 door does not rescue the simplex reading

The simplex hypothesis hoped to tie the trit to the program's open grade-3
transport door and the torsion three-form. It does not:

- The grade-3 self-dual record bridge's `c = 3` members are the ZERO class:
  `order(J(64*3)) = 24/gcd(24, 192) = 1`, while `c = 1` gives `order = 3`.
  Three-ness AT grade 3 is the trivial class (`k1-reframe-pass`, this is exactly
  its KILL 2). The grade-3 door delivers order-3 only at `c = 1`, and that grade-3
  bridge was already killed as non-native (fixture/pin-dependent class).
- The trit's own carrier has zero grade-3 content (commutant grades {0, 6}). The
  grade-3 dressing `e_0 e_1 e_9` (`grade_frac = 1.000` at grade 3) is a
  different, non-native object.

So neither the two-form (grade 2) nor the three-form (grade 3) sector is a home
for the trit's Z/3.

## 6. Five-lens council (inline, answered in writing)

**Representation theorist.** The kill is one algebraic fact: every order-3
element of `Sp(1)_comm` is `z1 + z2 J` with `J = C_J.conj`, and `C_J` is a pure
grade-6 monomial while `I` is grade-0; there is no grade-2 term available in the
commutant, period. The two-form sector is `so(9,5) = Lambda^2`, a DIFFERENT
summand of the algebra that acts on the carrier by rotations, not by the
commutant right-action. Reach and home are complementary here exactly as in the
k1-reframe dichotomy. Signed off.

**Hypergraph / simplex advocate (the required defense).** My best case was that
the trit's unoriented three-ness is a filled triangle whose Z/3 is its cyclic
symmetry, tying to the torsion three-form. Given a real test it did not survive:
the trit carries zero grade-2 face (Leg a), a 2-simplex boundary is oriented
while the trit is not (Leg b), and the grade-3 tie gives the trivial class at
`c = 3` (Leg c). I claim one honest residue: grade-2 DOES host an order-3 object
(the guard, 0.750), so "the trit is not a two-form" is a real decoupling, not a
blind test. But a two-form that does not act like the trit (fixes rays) and
winds zero is not the trit. No mechanism qualifies.

**Topologist / homologist.** The homology control is standard and decisive:
filled `H_1 = 0`, hollow `H_1 = 1`. The orientation obstruction is the
`S_3`-sign of the 2-chain, exact. A filled 2-simplex genuinely IS a
2-dimensional object whose boundary is a 3-cycle, so the hypothesis was
well-posed; it simply does not match a frozen object that lives in grades {0, 6}
and is unoriented. Signed off.

**Numerical analyst.** Every decisive quantity is exact or near-exact: grade-2
fractions `0.0` to `5.8e-34`; `C_J` grade-6 `1.000`; guard grade-2 `0.750`; ray
defect `0.513` vs `1.000`; `H_1` integer ranks; `gcd` integer arithmetic. No
tolerance is load-bearing within ten orders of magnitude. Two imported probes
re-ran live, exit 0. Deterministic; ~25 s. Signed off.

**Adversarial referee.** Three attacks. (1) "You decomposed the wrong operator."
Answered: BOTH order-3 elements of the trit's own group were decomposed (the
C-linear phase and the quaternionic unit), and the guard shows the projector
sees grade-2 when it is there. (2) "A homotopy class has no single grade, so a
grade decomposition is category-confused." Partly sustained as a caveat and
handled honestly: the test decomposes the trit's operator-level CARRIER (the
commutant elements that implement R1's twist), not the abstract `im J` class;
the finding is that the carrier's algebra support is {0, 6}, and the ray/winding
discriminator separately shows the grade-2 rotations are the wind-0 R2 sector.
(3) "The 2-simplex Z/3 is oriented but you could symmetrize it." Answered: an
unoriented (symmetrized) 3-cycle is precisely NOT a 2-simplex boundary -- it is
the `S_3`-invariant, which has no grade-2 face and no canonical filling. Verdict:
B2-FAILS, no branch smuggled.

## 7. Outcome, typing, boundary

- **Type: B2-FAILS**, feeding **F-NEITHER** on the simplex leg of the fork (the
  trit's interchangeability is real, but the two-form/2-simplex structural home
  does not fit). B1 (identical copies) is the separate node that decides
  F-COPIES vs F-NEITHER overall; this node only closes the simplex option.
- No claim-status, canon-verdict, or public-posture change. The order-3 arena
  result (`located, not forced`) is untouched; this node removes one candidate
  structural interpretation of the location, it does not move the location.
- Boundary: the node decomposes operator-level carriers of the frozen trit; it
  does not decide the framed-reading fork (R0_COND) and inherits the (9,5)
  H-class conditionality of the whole spine. It does not test B1. A physics-side
  occupant across the GEOMETER-VS-PHYSICS fork is out of scope.

## 8. Receipts

- Probe: `tests/channel-swings/trit_simplex_node_b2_probe.py` -- deterministic,
  exit 0, `5 [E] + 1 [F] = 6` (setup `[T] = 3` excluded), ~25 s. HEADLINE:
  **B2-FAILS**. Grade-2 content of both trit order-3 operators exactly zero
  (commutant support {0,6}); grade-2 hosts a real order-3 element (guard 0.750)
  the trit is not; 2-simplex boundary oriented vs unoriented trit; grade-3 door
  trivial at `c = 3`. Control: filled `H_1 = 0` vs hollow `H_1 = 1` vs path
  acyclic.
- Imported live, exit 0: `l1_assembly_probe.py` (the frozen Cl(9,5) rep, `C_J`,
  the commutant), `n4_two_z3s_probe.py` (the trit character, admissible pair).
- Frozen facts cited: `torsion-generation-arena-2026-07-20.md` (trit = R1
  commutant twist, `k = 64`, order-3 class; R2 winds 0),
  `trit-triage-2026-07-20.md` (unoriented; only frozen order-3 family element is
  `omega*I`, ray-fixing), `k1-reframe-pass-2026-07-20.md` (grade-3 bridge `c = 3`
  is the zero class; non-native), `rs_bicomplex_spin95_connection_2form.py`
  (`Sigma_ab = (1/4)[e_a, e_b]`, the grade-2 generators).
