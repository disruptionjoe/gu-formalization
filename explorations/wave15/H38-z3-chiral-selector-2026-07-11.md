# H38 (Wave 15): the Z/3-arena chiral selector -- PRESENT but PERMISSIVE. The count decouples into a 3-primary selector and a 2-primary unitarity condition.

2026-07-11. Big-swing computation attacking H38 -- the conjecture that, after Wave 13 (H37: located-not-forced on built (9,5)) and Wave 14 (H19: the signature is 2-primary and cannot reach the count), the generation count's real decider is a signature-independent, matter-sector **Z/3-arena chiral selector**: a ghost-parity-preserving dynamics `[P_ghost, S] = 0` on GU's matter Krein space, possibly the SAME object as H26 (loop-level ghost unitarity).

Test: `tests/wave15/H38_z3_chiral_selector.py` (deterministic, exit 0, 11/11 PASS, ~40 s).

## Headline

**NARROWED, not resolved.** H38 is half-right in a way that sharpens the count question rather than closing it. The Z/3 grading it needs is genuinely **PRESENT and BUILT** in the (9,5) matter sector (Q1). But the object H38 names -- a **ghost-parity-preserving** dynamics `[P,S]=0` -- is the **wrong arena** for the count: the ghost parity `P` is order 2 (a 2-primary object), and by the same two-arena blindness that killed the signature route, a 2-primary condition cannot reach the 3-primary count. So `[P,S]=0` **PERMITS** the vectorlike 3+3 and can never **SELECT** a chiral 3. This is the exact trap Wave 14 fell into, one arena over.

The real content of H38 is a **decoupling**: the count question splits cleanly into two arena-orthogonal objects that H38 had conflated --
- a **3-primary count selector** = the Z/3 grading `W` (present; its "3" is derived), which is what must do the chiral selecting, and must be **index-changing**; and
- a **2-primary unitarity condition** = `[P,S]=0`, which **is** the same object as H26, but supplies consistency/positivity, **not** the count.

## The four verdicts

### Q1 -- Is a Z/3 grading PRESENT in the built (9,5) matter sector? YES. [COMPUTED, high confidence]

The self-dual `SU(2)+` triplet carrier is reproduced on the actual (9,5) substrate: `dim ker(Gamma) = 1664`, the top-Casimir sector is exactly `192 = 3 x 64` (spin-1, Casimir top `8.0 = 4 j(j+1)` at `j=1`). This is a genuine **dimension-3 family multiplet** [COMPUTED substrate].

- The order-3 subgroup `Z/3 < SU(2)+` acting on the spin-1 triplet has eigenvalues `{1, zeta, zeta^2}` (`zeta = e^{2 pi i/3}`), `W^3 = I` (residual `9.3e-16`); on the carrier `triplet = spin1 (x) C^64` it splits `192` into three `64`-dim eigenspaces. A genuine **Z/3 grading**, built, not imported. [COMPUTED exact]
- The `3` is **DERIVED**: `dim Lambda^2_+(R^4) = 3` (self-dual 2-forms on a 4-base) `= dim adjoint su(2)+`. The 4-dimensional base forces rank-3 self-dual 2-forms. No `3` is fit. [COMPUTED exact]
- The Z/3 is **NOT ambient triality**: the Clifford ambient `Spin(14) = D7` has Dynkin/Coxeter graph-automorphism group `Z/2` (order 2, no order-3 element); only `D4 = Spin(8)` carries the `S_3` triality. So the Z/3 originates in the self-dual `SU(2)+` on the 4-base, not in a Clifford/gauge triality. [COMPUTED exact -- brute-force graph automorphism count `|Aut(D4)|=6`, `|Aut(D7)|=2`]

This is a **decisive positive** on Q1: unlike the earlier "does GU contain X" checks that came back absent, the 3-primary Z/3 arena object is concretely located in the built structure -- and it is precisely the H1 "located" content (`3 = dim Lambda^2_+`), now read as a cyclic grading a selector could engage.

### Q2 -- Build P and S, test [P,S]=0: permissive or selective? PERMISSIVE. [COMPUTED, high confidence]

Ghost parity `P` is modeled faithfully on the triplet's exact structure (canon/swing): the Krein form is **purely cross-chirality** (`{G5, K} = 0`, residual `0.0`), each hyperbolic (generation, mirror) pair has null `L, R` with `<L,R> != 0`, and `P` swaps `L <-> R`. `P^2 = I` (residual `0.0`), so `P` is an **order-2** object.

- Ghost-parity-preserving Krein-unitary `S` (`S^dag K S = K`, `[P,S]=0`) **exists as a large family** -- 6/6 sampled generators produce valid `S`. **PERMISSIVE.**
- The decisive selectivity test: the **chiral index of the physical (P-even) subspace is FIXED = 0** for every `[P,S]=0` dynamics (`index(bare) = -6.7e-17`; after transport by four sampled `S`: `[0.0, -0.0, -0.0, -0.0]`). Adding the Z/3 grading (`[W,S]=0`, residual `7.0e-16`) blocks `S` into three family sectors but leaves the index at `0`. **`[P,S]=0`, with or without the Z/3 grading, does not pin a chiral rank.**

Why: the index of the physical sector is a property of the pair `(P, G5)` -- because `K` is cross-chirality, every P-even physical state is exactly 50/50 `L/R`. A ghost-parity-preserving `S` maps the physical subspace to another P-even subspace of the *same* index. This is the machine-level statement of the swing no-go: **ghost parity supplies consistency, not chirality.**

### Q3 -- The H38 = H26 identity. TRUE on the unitarity leg only. [COMPUTED structural + ARGUED, medium-high confidence]

- **Coincide (unitarity):** the matter-side ghost parity and the loop-side ghost-unitarity parity (H26) are the **same order-2 Krein/Cartan involution** `P` (canon: `K` implements the Cartan involution of `so(9,5)` and equals the ghost parity on the triplet), with the **same preservation law** `[P,S]=0`. As the consistency/positivity object they are **one `Z2`**. This is real upside: the matter-sector positivity condition and the loop-level ghost-unitarity condition are the same requirement. [ARGUED from canon + P^2=I computed]
- **Differ (the count):** the count selector is the Z/3 grading `W`, which is **arena-orthogonal** to `P`: `gcd(2,3) = 1`, `3-part(2) = 1` (P blind to the 3-arena), `3-part(3) = 3` (W reaches it). So `H38 = H26` holds **only** on the unitarity leg; **neither H26 nor `[P,S]=0` supplies the count.** [COMPUTED]

### Q4 -- The decisive honest control: SELECT 3, or merely PERMIT odd? PERMIT. [COMPUTED, high confidence]

- `[P,S]=0` is a **2-primary** condition (`P` order 2). The count-3 lives in `Z/3`. `|Hom(Z/2, Z/3)| = gcd(2,3) = 1` (the zero map): a ghost-parity condition is arithmetically blind to the 3-primary count arena -- **the exact (7,7) trap, one arena over** (signature was `Z/8`; ghost parity is `Z/2`; both 2-primary, both blind). [COMPUTED]
- The Z/3 grading `W` is the **only** 3-primary object in play (`3-part(3)=3`), and it supplies the **3 slots** (`= dim Lambda^2_+`, derived). But a `P`-preserving (Krein-unitary) dynamics **conserves the chiral index at 0** (Q2b; the carrier is neutral `(+96, -96)` -- reproduced on the actual substrate), so `W`'s three slots stay **vectorlike**. `W` permits, does not chirally select 3. [COMPUTED]
- **Adversarial:** the only `3` anywhere is `dim Lambda^2_+(R^4)` (computed, derived from base dim 4); `C2 = 155.3625` unchanged; no `24`, no `24-8`, no fit. [COMPUTED]

So H38's candidate, like (7,7), **lifts nothing that selects** -- it relocates and names the arena but does not force the count.

## Honest limits (do not overclaim)

- **The selectivity no-go is model-faithful, not full-operator-space.** Q2/Q4 are computed on the exact cross-chirality hyperbolic-pair model of the triplet (`{G5,K}=0`, `P^2=I`, neutral index -- all reproduced on the real (9,5) substrate for the Krein signature). The index-conservation statement is exact for **Krein-unitary, ghost-parity-preserving** `S`. It does **not** exclude an index-changing (non-Krein-unitary) selector -- indeed that is exactly what the re-rank points to. The claim is precisely: *ghost-parity preservation is what forbids chiral selection*, not that no selector exists.
- **`W`'s "3" is derived; `W`'s order-3-ness is a choice of subgroup.** The `3` as `dim Lambda^2_+ = dim(adjoint su(2)+)` is genuinely forced by the 4-base. Choosing the order-3 cyclic subgroup of the continuous `SU(2)+` is a choice, but its three eigen-slots number `3` for the derived reason. No circularity: the count of slots equals the derived triplet dimension.
- **H38 = H26 is structural, not a built dynamics.** Both sides remain conditional on GU's unbuilt source action realizing the ghost parity at all (`[P,S]=0` cannot be checked against an `S` GU has not supplied). The identity is between two *conditions*, not two computed operators.
- **The RS/generation carrier is the hard case.** The one existing 3-primary spectral object in the repo (the order-3 equivariant Dirac rho, class `(0,1,2)/3` NONZERO) lives on the **spin-1/2** carrier; the **RS (spin-3/2) generation carrier** is structurally 2-primary (class `(0,0,0)`, twist character `-3 == 0 mod 3` at every fixed point). So even the 3-primary geometry that exists does not, as currently pinned, act on the generation arena. This is the crux the next object must resolve.

## What H38 changes

H38 is the fermion-sector analog of the H29 -> H37 sharpening: it does not close the count, it **splits it correctly**. Before H38 the "ghost-parity Z/3 selector" was one hoped-for object. After H38 it is provably **two** arena-orthogonal objects:

1. **Unitarity** = `[P,S]=0`, `P` order-2, 2-primary, index-preserving. **Same as H26.** Supplies positivity/consistency. Blind to the count.
2. **Count** = the Z/3 grading `W`, order-3, 3-primary, and -- to actually select -- must be **index-changing**. Present in the built structure as the slots; missing as a chiral selector.

The value: the count decider is now known to be a **3-primary, index-changing operator on the generation (RS) carrier** -- not a ghost-parity/unitarity condition, and not a signature. That is a strictly sharper target than "a ghost-parity-preserving Z/3 dynamics."

## RE-RANK signal

**H38: NARROWED.** (Present-but-permissive, exactly the H29->H37 / Wave-14 shape: a veto/arena is correctly located, no selector is supplied.)

**Single next object:** SG4 -- **which K-class the unbuilt GU source-action operator names on the RS/generation carrier.** The two candidates are already computed:
- geometric-complete gamma-traceless carrier: `ind = -38 = 19 sigma/8` (Homma-Semmelmann), order-3 Nikulin rho `(0,2,1)/3` **NONZERO** (3-primary, index-changing -- the kind Q4 says is needed);
- ghost-subtracted carrier: `ind = -42 = 21 sigma/8` (AGW gravitino), order-3 rho `(0,0,0)` **ZERO / 2-primary** (the kind Q4 says permits but cannot select).

The count's fate is this binary. It is signature-independent (confirming Wave 14's steer), matter-sector, and 3-primary (confirming H38's arena) -- but it is a **source-action K-class selection**, not a ghost-parity condition. That is the one object to attack next.

## Provenance

- Test: `tests/wave15/H38_z3_chiral_selector.py` (exit 0, 11/11).
- Load-bearing inputs: `canon/ghost-parity-krein-synthesis.md`, `canon/swing-ghost-parity-no-chiral-selection.md` (index-0 no-go), `tests/family-puzzle/primary_partition_lemma.py` (the 3-primary-reach lemma), `canon/order3-equivariant-rho-RESULTS.md` + `canon/gamma-traceless-38-adjudication-RESULTS.md` (the SG4 binary), `tests/wave13/H37_count_nogo.py`, `tests/wave14/H19_seven_seven_branch.py`, `explorations/seven-axis-count-map-L0-L7-2026-07-11.md`.
- No target number imported (`3` = `dim Lambda^2_+`, derived; no `24`, no `24-8`); `C2 = 155.3625` unchanged. Working tree left dirty for orchestrator verification.
