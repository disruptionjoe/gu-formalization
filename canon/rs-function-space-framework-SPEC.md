---
title: "RS function-space framework: ghost-subtracted bulk controls and boundary hypotheses; geometric Q and native Krein complex remain distinct"
status: staged
doc_type: spec
created: 2026-07-02
grade: "SPEC + computed bulk. The framework is the 'specification before promotion' object (canonical claim 4). The A bulk mod-3 divisibility result (I_{3/2}=21*sigma/8, by Rokhlin) is computed/exact and cross-checked against canon (tests/rs-function-space/rs_index_harness.py, 240 asserts, exit 0). The boundary-eta and family-index steps are OPEN, stubbed with their exact obligations. Internal tier (caveat (e))."
depends_on:
  - canon/function-space-index-conservation-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/forcing-slot-toy-rs-RESULTS.md
  - canon/boundary-eta-of-mu-RESULTS.md
scripts:
  - tests/rs-function-space/rs_index_harness.py
---

# RS function-space framework (foundation for the big swing)

## Construction scope correction — Joe approved, 2026-11-20

Authority: `joe_direct_chat_2026_11_20_b`; wording correction, with existing
status and grade retained. The Nikulin order-3 **ghost-subtracted** benchmark A
has index -42 and zero rho class. The **geometric gamma-traceless** benchmark B
has index -38 and nonzero classes (0,2,1)/3. The source-native **Krein-graded**
complex remains unidentified at this invariant: retaining ghosts does not
specify their index grading or trace. A/B is a comparison, not an exhaustive
classification of source constructions. Neither residue supplies an integer
family count. Statements below about a binary or sole decider are restricted
to their declared comparison; they do not require building the source action
before testing defined structural subfamilies. Paper and released bytes are
unchanged. See the [approved-scope audit](../explorations/conditional-build/native-complex-order3-fork-2026-11-20.md)
and [follow-up benchmark and map test](../explorations/conditional-build/krein-order3-observation-label-2026-11-20.md).

The one residual keeping "external by structure" from being unconditional is the actual
Rarita-Schwinger operator on sections (APS/end + family-index). This spec builds the scaffolding so
the remaining work is plugging into machinery, not rebuilding it.

## 1. The object

- **Base:** a spin 4-manifold `X` (later, a fibered geometry `Y` with `K3` fiber for the family step).
- **RS bundle:** the gamma-traceless rank-3/2 field, sections of `(T*X (x) S)_gamma-traceless`; the
  fiber carrier is the `j=1` triplet with its cross-chirality `(+96,-96)` Krein form `K`.
  **SCOPE CORRECTION 2026-07-10:** this bundle description and the `21*sigma/8` index pin in Section
  4 name DIFFERENT published objects. The gamma-traceless bundle's honest operator (Homma-Semmelmann
  Prop 3.1(i); Baer-Mazzeo) has `ind Q = 19*sigma/8 = -38` on K3 and order-3 Nikulin rho classes
  `(0,2,1)/3` NONZERO; the `21*sigma/8 = -42` pin is the ghost-subtracted gravitino complex
  `D (x) (T_C - 1C)`, order-3 class `(0,0,0)`. They differ by exactly two reversed-chirality
  spin-1/2 units. Every computed number in this SPEC is carrier-A (ghost-subtracted) arithmetic;
  which carrier the GU generation arena names is the SG4 identification question. See
  `canon/gamma-traceless-38-adjudication-RESULTS.md`.
- **Operator:** the RS Dirac-type operator `D_RS` on `L^2`-sections; chirality grading `Gamma`, Krein
  form `K` extended fiberwise (`K Gamma = -Gamma K`, cross-chirality).
- **Count:** the net chiral index of `D_RS` (or the spectral flow of a family).

## 2. Hypotheses (the function-space setting)

`D_RS` is (i) self-adjoint (essential self-adjointness of the elliptic RS operator on the common
dense domain), (ii) **Gamma-odd** (Dirac-type), (iii) **Krein-self-adjoint** fiberwise
(`D_RS^dag K = K D_RS`), (iv) **Fredholm** (elliptic on compact `X`; APS / noncompact-end data on
`X` with boundary or ends). The finite-carrier theorems (index conservation, the antilinear
null-eigenspace bound) are the fiberwise `t = const` content; the function-space content is what the
integral / spectral flow adds.

## 3. The index decomposition (the map for the whole swing)

> `ind(D_RS) = [bulk Atiyah-Singer] + [APS boundary/end eta] + [family-index / higher-topology]`.

Each term is a separate obligation. The cross-chirality Krein structure acts on all three.

## 4. STEP 1-2 -- BULK: DONE (computed, this pass)

The bulk term is the Atiyah-Singer integral. For the ghost-subtracted gravitino comparator A on a closed spin 4-manifold the
density is exactly `7 p_1/8`, so

> **`I_{3/2}[X] = 21*sigma/8`**  (spin-1/2 companion: `A-hat[X] = -sigma/8`).

Cross-checked against canon: `K3 -> -42`, `K3#K3 -> -84`, `T^4 -> 0`, `twist-by-16 -> -672`
(`tests/rs-function-space/rs_index_harness.py`). **Bulk-even theorem:** by Rokhlin (`sigma == 0 mod 16`
for spin 4-manifolds), `I_{3/2} = 42k`, hence **`== 0 mod 3` identically**; and every integer twist
`dim(V)*I_{3/2} + 3*ch2(V)` stays `== 0 mod 3`. This establishes mod-3 divisibility for the stated A index formula and twists,
not a universal RS theorem. The integer itself is not a 2-primary torsion
class; its reduction in Z/24 has zero Z/3 component. The `3` in `-42 = -2*3*7` is
the fixed Hirzebruch `p_1 = 3*sigma`, generation-independent (identical for 1, 3, 5, ...). This
is a bulk statement about A, independent of the finite interior-even theorem.

## 5. STEP 2 -- BOUNDARY / APS eta: DONE (computed, 2-primary)

On `X` with boundary / ends, add `(eta_partial + h)/2` (APS). Obligation: compute the eta-invariant
of the **RS boundary operator** and decide its parity.
- **Available:** the sector's own boundary is the `RP^3 = L(2;1)` spine, whose reduced eta is already
  computed 2-primary (`canon/boundary-eta-of-mu-RESULTS.md`). Lens-space eta invariants have closed
  forms.
- **DONE (2026-07-03, `canon/rs-boundary-eta-2primary-RESULTS.md`):** extended to the FULL RS boundary
  operator `D_RS = E + E^dag`. Its net self-dual tangent-frame charge is `0` (computed, two independent
  angles; `Pi`, `M_D`, `D_RS` all non-chiral, while the `Lambda^2_+` control registers `33.94`), so it
  carries no tangent-frame `p_1` and cannot feed the gravitational `-p_1/24` channel; the only residue
  is the charge-`q` lens type `(2q^2-4q+1)/8` (denominator 8, 2-primary), with spectral eta `0`
  (cross-chirality `(+96,-96)` balance). **Verdict: the sector's own boundary eta is 2-PRIMARY/EVEN --
  an odd count cannot come from the sector's own boundary, only from an external topological
  background.** The expected falsifiable result held. Scripts: `tests/rs-function-space/rs_boundary_eta_l21.py`
  (+ `verify/rs_boundary_eta_indep_check.py`).

## 6. STEP 3 -- FAMILY INDEX / K3 pushforward: THE CRUX (obligations 1-2 scaffolded 2026-07-03; 3-5 open)

For a family of RS operators over a base with `K3` fiber (`chi = 24`), the family index is a
pushforward `pi_!`. `family_index_pushforward_stub()` in the harness marks the interface. Obligation
(exactly what NEXT-STEPS blocks it on, **all without target import** -- no smuggling `24/8=3`):
1. the **fiber model** (the `K3`-fibered geometry as an actual bundle);
2. the **compact-support / APS pushforward** `pi_!`;
3. a `Phi`-homotopy or **symbol certificate** for the family;
4. the **`ch2` / eta correction** term;
5. the **`H`-line normalization**.
Within this A-based family scaffold, one open route is: a source-identified family invariant would constrain this
specified route, with a separate physical integer-count bridge still required;
a free value does not make a universal external-count claim unconditional. The bulk result gives mod-3 divisibility for A; it does not select the
native carrier, exclude B, or turn a residue into a count.

**Scaffold status (2026-07-03, `tests/rs-function-space/k3_family_pushforward_scaffold.py`):**
obligations **(1) fiber model** and **(2) compact-support/APS pushforward** are scaffolded at
product-family (toy) grade -- the fiberwise pushforward `pi_!` of the RS density is computed and, for a
trivial `B x K3` family, recovers `I_{3/2}[K3] = -42 ≡ 0 mod 3` (no new `Z/3` generation piece; the `3`
in `-42` is the fixed Hirzebruch `p_1`, not a count). The scaffold makes the SPEC's FLIP criterion
concrete: the generation-arena (`mod 3`) value is a **free** function of the clutching term (obligation
4), but forcing a residue would still require an integer-observable bridge to force a count. Obligations **(3) `Phi`-homotopy / symbol
certificate, (4) `ch2`/eta correction (the crux), (5) `H`-line normalization** remain **OPEN** -- they
require the actual GU `K3`-fibered source-action geometry, which is unbuilt (`absorbed/gu-source-action`).
FIREWALL held: the RS family index uses only `21*sigma/8` (`sigma(K3) = -16`), never `chi(K3)=24` or
`24/8=3`. A generation-arena probe (`tests/rs-function-space/family_generation_arena_probe.py`) confirms
the listed A-derived sample (`-42, -672, -5376, 0`) is `== 0 mod 3`; this
does not cover the geometric-Q rho or a separately defined native Krein complex;
the honest `ch2(S_X)[K3] = -5376`, not `24`. The exact data a valid GU source action must expose to
close (or kill) this crux -- and the pass criterion (`N != 0 mod 3` WITHOUT a chi-import) -- is wired to
`absorbed/gu-source-action` global objects 5(i)-(iii) in `canon/source-action-family-index-interface-SPEC.md`.

## 7. What this foundation buys the swing

- A **reusable index engine** (`rs_index_harness.py`) shared by bulk and family, cross-checked to
  canon -- Steps 2 and 3 compute *through* it, not from scratch.
- The **A bulk divisibility closed** at computed grade, so the swing reduces to the boundary eta
  (likely 2-primary, partly in hand) and the **`K3` family pushforward** (the real open crux),
  precisely itemized.
- A rigorous framework statement (the "specification before promotion" object).

## Status

Staged, **not CANON.md-promoted**; the bulk-even result AND the boundary-eta result are now
computed/exact (A bulk divisibility; separately scoped boundary torsion), leaving the `K3` family-index step (obligations 3-5) as the remaining
OPEN crux. Internal tier. Pauses for Joe. No number was fitted; the only integers are the exact index
values (`-42, -84, 0, -672`) and their `mod 3 = 0`.
