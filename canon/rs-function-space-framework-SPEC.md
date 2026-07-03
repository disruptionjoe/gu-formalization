---
title: "Rarita-Schwinger function-space framework: the foundation for closing WC-FUNCTION-SPACE-EXT. Sets up the RS-section Krein-Hilbert space, the operator and its hypotheses, and the index decomposition ind(D_RS) = bulk + APS-boundary-eta + family-index. STEP 1-2 DONE (computed): the BULK RS index I_{3/2} = 21*sigma/8 is 2-primary by Rokhlin (== 0 mod 3 for every spin 4-manifold and every twist -- it never reaches the Z/3 generation arena). A reusable characteristic-class / index harness reproduces the canon values (K3 -42, K3#K3 -84, T^4 0, twist-16 -672) and is the shared engine for the bulk and the family index. STEP 2 (boundary eta) and STEP 3 (K3 family-index pushforward -- the crux) are precisely scoped stubs."
status: staged
doc_type: spec
created: 2026-07-02
grade: "SPEC + computed bulk. The framework is the 'specification before promotion' object (canonical claim 4). The bulk-even result (I_{3/2}=21*sigma/8, 2-primary by Rokhlin) is computed/exact and cross-checked against canon (tests/rs-function-space/rs_index_harness.py, 240 asserts, exit 0). The boundary-eta and family-index steps are OPEN, stubbed with their exact obligations. Internal tier (caveat (e))."
depends_on:
  - canon/function-space-index-conservation-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/forcing-slot-toy-rs-RESULTS.md
  - canon/boundary-eta-of-mu-RESULTS.md
scripts:
  - tests/rs-function-space/rs_index_harness.py
---

# RS function-space framework (foundation for the big swing)

The one residual keeping "external by structure" from being unconditional is the actual
Rarita-Schwinger operator on sections (APS/end + family-index). This spec builds the scaffolding so
the remaining work is plugging into machinery, not rebuilding it.

## 1. The object

- **Base:** a spin 4-manifold `X` (later, a fibered geometry `Y` with `K3` fiber for the family step).
- **RS bundle:** the gamma-traceless rank-3/2 field, sections of `(T*X (x) S)_gamma-traceless`; the
  fiber carrier is the `j=1` triplet with its cross-chirality `(+96,-96)` Krein form `K`.
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

The bulk term is the Atiyah-Singer integral. For the gravitino/RS operator on a spin 4-manifold the
density is exactly `7 p_1/8`, so

> **`I_{3/2}[X] = 21*sigma/8`**  (spin-1/2 companion: `A-hat[X] = -sigma/8`).

Cross-checked against canon: `K3 -> -42`, `K3#K3 -> -84`, `T^4 -> 0`, `twist-by-16 -> -672`
(`tests/rs-function-space/rs_index_harness.py`). **Bulk-even theorem:** by Rokhlin (`sigma == 0 mod 16`
for spin 4-manifolds), `I_{3/2} = 42k`, hence **`== 0 mod 3` identically**; and every integer twist
`dim(V)*I_{3/2} + 3*ch2(V)` stays `== 0 mod 3`. So the **bulk RS index never carries a 3-primary
(generation) piece** -- it lives entirely in the `Z/8` selector arena. The `3` in `-42 = -2*3*7` is
the fixed Hirzebruch `p_1 = 3*sigma`, generation-independent (identical for 1, 3, 5, ...). This
lifts the finite "interior even" to the actual operator's **bulk**.

## 5. STEP 2 -- BOUNDARY / APS eta: SCOPED STUB

On `X` with boundary / ends, add `(eta_partial + h)/2` (APS). Obligation: compute the eta-invariant
of the **RS boundary operator** and decide its parity.
- **Available:** the sector's own boundary is the `RP^3 = L(2;1)` spine, whose reduced eta is already
  computed 2-primary (`canon/boundary-eta-of-mu-RESULTS.md`). Lens-space eta invariants have closed
  forms.
- **To do:** extend that to the full RS boundary operator; the expected (falsifiable) result is that
  the sector's *own* boundary eta is 2-primary/even -- so an odd count cannot come from the sector's
  own boundary either, only from an external topological background.

## 6. STEP 3 -- FAMILY INDEX / K3 pushforward: THE CRUX (scoped stub)

For a family of RS operators over a base with `K3` fiber (`chi = 24`), the family index is a
pushforward `pi_!`. `family_index_pushforward_stub()` in the harness marks the interface. Obligation
(exactly what NEXT-STEPS blocks it on, **all without target import** -- no smuggling `24/8=3`):
1. the **fiber model** (the `K3`-fibered geometry as an actual bundle);
2. the **compact-support / APS pushforward** `pi_!`;
3. a `Phi`-homotopy or **symbol certificate** for the family;
4. the **`ch2` / eta correction** term;
5. the **`H`-line normalization**.
This is the ONLY piece that can *flip* the verdict: if the `K3` family index is GU-forced to a
specific value, GU forces a count; if free, "external by structure" becomes unconditional. The bulk
result already says the fiberwise-integrated piece is `Z/8`; the family/pushforward is where a
`Z/3`-piece would have to come from -- and the harness is ready to receive it.

## 7. What this foundation buys the swing

- A **reusable index engine** (`rs_index_harness.py`) shared by bulk and family, cross-checked to
  canon -- Steps 2 and 3 compute *through* it, not from scratch.
- The **bulk term closed** at computed grade (2-primary), so the swing reduces to the boundary eta
  (likely 2-primary, partly in hand) and the **`K3` family pushforward** (the real open crux),
  precisely itemized.
- A rigorous framework statement (the "specification before promotion" object).

## Status

Staged, **not CANON.md-promoted**; the bulk-even result is computed/exact, the boundary and family
steps are OPEN. Internal tier. Pauses for Joe. No number was fitted; the only integers are the exact
index values (`-42, -84, 0, -672`) and their `mod 3 = 0`.
