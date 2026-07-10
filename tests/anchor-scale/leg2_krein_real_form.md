# LEG-2: the real / Krein form of the scalar-spinor odd channel at anchor scale

**Leg of:** anchor-swing (corners campaign named gap 2 — the real/Krein form; + gap 3 shadow),
2026-07-10.
**Script:** `LEG-2-krein-real-form.py` (`leg2_run2.log`, exit 0, 35 checks). Exact Gaussian-rational
arithmetic (`GC` pairs of `fractions.Fraction`); **no floats anywhere in any assert path** — this
leg needed no rank scouts at all (symbolic `*`-word certificates + exact 128-dim witnesses +
standard representation theory replace every rank computation).
**Ports (so the two anchor legs compose):** the exact `GC` arithmetic, the sparse 128×128 matrix
engine, the Cl(9,5) Jordan–Wigner gammas `GAM`, and the Krein metric `BETA` are copied **verbatim**
from LEG-1 (`LEG-1-anchor-super-jacobi.py`), which in turn ports the generation-sector
`ghost_parity_krein.py` conventions. Same `beta_S`, same `u_beta`, same odd pairing `M(Q,P)`.
**Question decided:** does the scalar-spinor closure (LEG-1's minimal-ansatz graded IG on the
Cl(9,5)/u(64,64) fiber) survive the honest **real/Krein** form — β-compatible brackets and the
quaternionic structure of `M(64,H)` — or does it **require complexification** (which would grade the
toy result complex-only)? Plus (gap 3) the derivative-level odd `tau_plus`: exact requirement +
finite shadow, or honest BLOCKED.
**NOT decided here:** SG4 (whether GU's unbuilt action realizes any of this, and which gauge algebra
— u(64,64) with its u(1) center, or the centerless quaternionic `g_H` — GU intends); the full
super-Jacobi closure (that is LEG-1's, composed with here); the derivative-level homomorphism itself
(BLOCKED, structure named).

## The objects (all ported exact)

- Cl(9,5) gammas `GAM_a` (a=0..13), signature `eta` = +1 spacelike {0,1,2,3,9,10,11,12,13}, −1
  timelike {4,5,6,7,8}; `{GAM_a,GAM_b} = 2 eta_ab` exact (196 pairs). Spacelike Hermitian, timelike
  anti-Hermitian.
- Krein metric `beta_S` = product of the 9 spacelike gammas: Hermitian, `beta_S^2 = I`,
  `tr beta_S = 0` ⇒ eigenvalue balance (64,64) ⇒ the anchor gauge algebra
  `u_beta = {X : beta X + X^dag beta = 0}` is of `u(64,64)` type (Sylvester).
- Odd pairing (LEG-1's): `M(Q,P) = i(Q P^dag beta + P Q^dag beta)` (sesquilinear/Krein), its
  traceless part `M_sl`, and the central `M_0 = i s(Q,P) Id` with `s = Q^dag beta P + P^dag beta Q`.

## RESULT — Q2: the closure SURVIVES the real/Krein form; NO complexification

### R1. β-compatibility is EXACT and AUTOMATIC (PART 3; exact-certified)

The compatibility condition — that every odd-odd bracket value is pseudo-anti-Hermitian w.r.t.
`beta_S` (i.e. lands in the **real** form `u(64,64)`, not merely in its complexification
`gl(128,C)`) — is proved as a free `*`-word-algebra identity **valid for all spinors `Q,P`** from the
single premise `beta^dag = beta`:

- **CERT K1** (symbolic): `beta·M + M^dag·beta = 0` for all `Q,P`, from `beta^dag = beta` **alone**
  — no Clifford identity, no complexification enters. So `M(Q,P) ∈ u(64,64)` for **every** pair.
- **CERT K2** (symbolic): `s(Q,P)^dag = s(Q,P)` ⇒ `s` real ⇒ `M_0 = i·s·Id ∈ u_beta` (`i·Id` central,
  anti-Hermitian × real).
- **CERT K3** (symbolic): `M(Q,P) = M(P,Q)` — the odd bracket is symmetric, as a `{odd,odd}` bracket
  must be.
- Instantiated **exactly** on the honest 128-dim fiber (6 random spinor pairs; `M, M_sl, M_0 ∈ u_beta`;
  symmetric; `s` real).

The reality of the odd bracket therefore needs nothing but `beta` Hermitian. This is the load-bearing
fact: **the odd-odd bracket lands in the real Krein form for every pair, provably, with no
complexification.** Composed with LEG-1's super-Jacobi closure (verified over the real S_R with
rational witnesses), the graded IG is a **real super-Lie algebra** on `u(64,64) ⊕ S_R`.

### R2. The anchor's u(1) center SELECTS the real (sesquilinear) form (PARTS 5–6; exact inputs)

`i·Id` acts as `+i` on `S` (exact). Hence:
- `Sym^2 S` carries central charge `±2`; the complex-**bilinear** channels `Sym^2 S → u_beta` (the
  toy's channel, built from a charge-conjugation/transpose pairing) are **dead** by center
  equivariance: any equivariant `B` obeys `[i·Id, B(·)] = 2i·B` while `[i·Id, ·] = 0` on the
  charge-0 gauge algebra, forcing `B = 0`.
- Only the **sesquilinear** channel `S-bar ⊗ S` (charge 0) can map to the charge-0 `u_beta` — and
  that channel is exactly the Krein pairing `M, M_0`, which is intrinsically real.
- Exact witnesses: the constructed spin(9,5)-invariant bilinear form `b(u,v) = u^T C_bilin v` (with
  `C_bilin` the exact charge-conjugation intertwining `GAM_a ↦ GAM_a^T`) satisfies
  `b(iu,v) + b(u,iv) = 2i·b ≠ 0` — charge 2, killed over `u(64,64)`; while
  `[i·Id, M(Q,P)] = 0` — the surviving Krein bracket is neutral.

So at anchor scale the real form is **forced by the fiber, not imposed**: complexification is not
available because the complex-bilinear brackets are dead over `u(64,64)`. This **resolves the toy's
honest-limit #2** ("complexified; real forms not selected"): the toy `so(4)` had no center and its
bilinear C-pairings carried the channel; the anchor's `u(1)` center selects the sesquilinear/real
channel automatically.

### R3. The quaternionic `M(64,H)` structure, exact — and the u(64,64) vs g_H fork (PARTS 4–5)

The quaternionic structure is **constructed exactly**: `J(v) = C·conj(v)` with
`C = ∏_{a: eps_a = −1} GAM_a` (the 8 gammas whose complex conjugate flips sign; `eps` computed, not
assumed). Then:

- `J^2 = C C^* = −I` **exactly** ⇒ `S` is **quaternionic** (matches Cl(9,5) = M(64,H); classification
  `q−p = 4 mod 8` → M(H); the `−I` sign, not `+I`, is the invariant). `J` antilinear,
  `GAM_a C = C GAM_a^*` for all 14 a ⇒ **`J` commutes with the whole Clifford algebra** (β, every
  `sigma_ab`, hence preserves the Krein form).
- **`J` ANTI-commutes with the central charge `i·Id`** (`J(iv) = −i·J(v)`, antilinearity): the u(1)
  center is **not** quaternionic-linear.

The reality verdict then forks, both sides **real** (neither complexified):

- **Over the full `u(64,64)`** (WITH center): a generic `X ∈ u_beta` does **not** commute with `J`
  (exact witness `J(Xv) ≠ X(Jv)`). Structurally, the standard rep `C^128` of `u(64,64)` is
  irreducible of **complex type** (no antilinear commutant), so the only `u_beta`-compatible real
  structure on the odd space is the **underlying real `S_R`** (dim_R 256) — exactly LEG-1's odd
  module. No half-size real (`tau^2=+1`) or quaternionic (`tau^2=−1`) module is `u(64,64)`-compatible.
  The super-algebra is real, no complexification; `J` is present on `S` but is **not** a gauge
  symmetry.
- **Over the H-respecting subalgebra `g_H = u_beta ∩ gl(64,H)`** (a quaternionic-unitary, sp(p,q)-type
  algebra; **contains spin(9,5), EXCLUDES the u(1) center** — exact witnesses): `J` **is** a symmetry,
  and the spin-invariant **bilinear** charge-conjugation channel `b` also survives (it is only killed
  by the center, which `g_H` lacks). This is the honest **quaternionic real form**, with **both** a
  sesquilinear (Krein) and a bilinear odd channel available.

**Honest tension surfaced (understanding, not a verdict):** the same `J` that realizes the M(64,H)
reality anticommutes with the central charge that forces the sesquilinear reality. The
"central-charge-forced" real form (needs the u(1)) and the "quaternionic" real form (needs `J`,
excludes the u(1)) are **different real forms** — each consistent, each complexification-free, and
they do **not** coincide. Which one GU intends (u(64,64) with center, or the centerless quaternionic
`g_H`) is an **SG4** selection, not decided here.

## RESULT — Q3: derivative-level odd `tau_plus` (PART 7; finite shadow closes, homomorphism BLOCKED)

**Exact requirement.** The even `tau_plus` embeds the gauge group as `tau_+(g) = (g, g^{-1} d_aleph g)`
in `IG = G ⋉ Omega^1(ad)`; at Lie level `d tau_+(xi) = (xi, d_aleph xi)`, whose homomorphism property
is the Leibniz 1-cocycle `d_aleph[xi,eta] = [xi, d_aleph eta] − [eta, d_aleph xi]`. The **odd**
`tau_plus` (steelman S3) sends `eps ∈ Omega^0(S)` to `(eps, D_aleph eps) ∈ Omega^0(S) ⊕ Omega^1(S)`.
A derivative-level closure check requires three things the pointwise bracket cannot see:
- **(D1)** `D_aleph` a β-**compatible** covariant derivative — so `D_aleph eps` is a legitimate Krein
  spinor-valued 1-form (reality preserved);
- **(D2)** a Leibniz identity making the Clifford pairing of `D`-images match `d_aleph` of the pairing
  (the odd 1-cocycle);
- **(D3)** the curvature `F_aleph = d_aleph^2` controlled (the second-order obstruction).

**Finite shadow (exact, executed).** Freeze the derivative to constant β-compatible fiber operators
`D_mu ∈ u_beta` (LEG-1's `[transl, Omega^0(S)] → Omega^1(S)` slot with the derivative frozen). Then:
- (D1) `D_mu ∈ u_beta` ⇒ `D_mu eps` stays a Krein spinor — reality preserved (exact).
- (D2, reality layer) the derivative-twisted Krein pairing `M(Q, D_mu P) + M(D_mu Q, P)` stays in
  `u(64,64)` (exact). Note this closes **because K1 is universal in the spinor arguments** — precisely
  the robustness the reality layer adds; the full Leibniz cocycle is part of the BLOCKED content.
- (D3) `[D_0, D_1] ∈ u_beta` and `≠ 0` (exact): the two frozen derivative directions do **not**
  commute — `d_aleph^2 = F_aleph` is generically nonzero.

**Verdict (Q3): BLOCKED, with the exact missing structure named.** The finite (frozen, flat,
β-compatible) shadow of the odd `tau_plus` 1-cocycle **closes exactly and preserves the Krein
reality**. The genuine derivative-level homomorphism is BLOCKED on: the connection `aleph` on the base
`Y`, the covariant `d_aleph` as a **first-order differential operator** (not a fiber endomorphism), and
the identity `F_aleph = d_aleph^2` tying `{odd,odd} ∈ Omega^1(ad)` to the base curvature — all
infinite-dimensional / geometric, outside a single-fiber model. This is the honest boundary: **real/
Krein form DECIDED (survives); derivative-level odd `tau_plus` BLOCKED.**

## What is exact-certified vs structural

- **Exact-certified** (symbolic `*`-word or exact 128-dim witness): K1/K2/K3 β-compatibility and
  symmetry; signature (64,64); `J` construction, `J^2 = −I`, `J` commuting with the Clifford algebra
  and anticommuting with `i·Id`; `J` not commuting with generic `u_beta`; `g_H ⊇ spin(9,5)`,
  `g_H ∌ i·Id`, `g_H` bracket-closed; the bilinear form `b` spin-invariant, nonzero, charge-2; the
  Krein bracket charge-0; `i·Id` acting as `+i`; the Q3 finite-shadow checks.
- **Structural / representation-theoretic (float-free, standard, not brute-forced):** "`S` is
  complex-type over `u(64,64)` ⇒ only real form is `S_R`" (uses irreducibility + non-self-conjugacy
  of the `u(p,q)` standard rep; the specific `J ∤ commute` witness is exact, the "no antilinear
  commutant at all" is the standard rep-theory step); the center-equivariance kill of `Sym^2 S`
  (inputs `i·Id → +i` and `b` charge-2 are exact, the "⇒ channel dead" is the equivariance argument);
  the identification of `g_H` as sp(p,q)-**type** (its exact quaternionic signature is not computed).
- **No float scouts used anywhere.**

## Honest limits

1. **Composition, not re-derivation, of closure.** This leg decides the **reality/form** question; the
   super-Jacobi **closure** it relies on is LEG-1's (verified over `S_R` with rational witnesses). The
   two compose because they share `beta_S`, `u_beta`, and `M(Q,P)` verbatim.
2. **Two real forms, one undecided.** Both the `u(64,64)`-with-center and the centerless quaternionic
   `g_H` readings are consistent real forms; this leg does not select between them (SG4). The M(64,H)
   quaternionic structure is a genuine symmetry only in the `g_H` reading.
3. **`g_H` signature not computed.** `g_H` is certified a proper, centerless, spin(9,5)-containing
   subalgebra of quaternionic-unitary type; its exact `Sp(a,b)` signature was not determined.
4. **Q3 is a single-fiber shadow.** The finite frozen/flat check certifies only that the reality layer
   transfers; the derivative-level homomorphism (Leibniz cocycle + curvature) is BLOCKED, structure
   named.
5. **Does not touch SG4, b2, or the bare commutator.** No claim that GU's action is invariant under
   any of this.

## Firewall compliance

No `chi(K3)`, no 24, no /8 manufacture, no `A-hat = 3`, no topology imports (only `sys, time, random,
fractions`). The bare 58.72 commutator is never formed. All load-bearing arithmetic exact.
