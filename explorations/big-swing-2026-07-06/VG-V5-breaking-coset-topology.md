---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing VG-V5 (T2' coset topology): the candidate breaking coset D = positive lines in C^(3,2) deformation-retracts onto CP^2 by an explicit verified flow, and CP^2's discrete invariants are MEASURED with a full anti-import provenance chain -- chi = 3 (cellular AND Gauss-Bonnet quadrature 3.000000, S^4 control 2.000000), c1(T CP^2) = 3h, <c1^2> = 9, H^2 = Z free (NOT the RP^3 Z_2 / 2-torsion profile). Every 3 is an eigenvalue or cell COUNT descending from dim X = 4 + one time direction via measured (7,3) -> trace-reversed (6,4) [g -> -g invariant] -> Hermitian (3,2) [invariant over 21 sampled complex structures]. HONEST OUTCOME: the coset-topology legs (a)-(c) are THEOREM-grade, but whether the coset's 3 ever reaches the generation index is CONSISTENT_UNCOMPUTED: the twist enters only through the rk*c1(L)^2/2 term (absent in every GU-native channel), stays EVEN on spin X (respects the 12k/2-adic wall -- it cannot make the count odd), and is guaranteed 3-divisible only if the condensate couples through the anticanonical O(3) = K^(-1), which is an unperformed equivariant computation; the section itself needs the unbuilt dynamics."
grade: "exploration / (a)-(c) THEOREM (explicit constructions, machine-verified, with negative-line, Euclidean-base, S^4, and CP^1/CP^3 controls all showing the checks can fail); (d) index leg CONSISTENT_UNCOMPUTED; overall route CONSISTENT_UNCOMPUTED. Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, or divided by; every printed 3 carries a printed provenance line; the only inserted geometric data are dim X = 4 and 'the base is Lorentzian'. Anchors reproduced first: triplet Krein signature (+96,-96,0) in (9,5), beta_S residual 0.0e+00, rank(Gamma) = 128, ker = 1664."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - canon/h2-base-index-chirality.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
scripts:
  - tests/big-swing/vg_v5_breaking_coset_topology.py
---

# VG-V5: T2' coset topology — does the breaking channel carry a 3-divisible discrete invariant?

**The leg (revised statement, Section 5.3 of the persona doc):** exhibit a nonconstant map from the
breaking vacuum-manifold's homotopy to a 3-divisible class in the relevant bordism/Dai-Freed group,
against standing adverse evidence attached to the leg itself: RP^3 is Z_2, native indices are 12k,
inflow is mod-2, C-07 forces even signatures — "the CP^2/c1 = 3h candidate enters flagged as
numerology until derived."

**What this route did:** derived the CP^2 candidate's topology honestly — explicit retraction, measured
invariants, printed provenance chain for every 3 — and then stated exactly which computation is still
missing before the 3 can be said to reach the generation index. All numbers below are printed by
`tests/big-swing/vg_v5_breaking_coset_topology.py` (run from repo root, exit 0).

**Honest outcome in one line:** the coset topology is now THEOREM-grade and it is genuinely NOT the
2-adic profile of every previously named channel — but the invoice is not paid: the 3-divisible class
exists in the coset, and no computation yet connects it to the count.

---

## 0. Anchors (reproduced first, reusing `tests/generation-sector/ghost_parity_krein.py`)

- Triplet Krein signature in (9,5): **(+96, −96, 0)** — vectorlike, hyperbolic (generation, mirror)
  pairs. `beta_S` pseudo-anti-Hermiticity residual **0.0e+00**.
- `rank(Gamma) = 128`, `dim ker(Gamma) = 1664` on the 1792-dim carrier.

These bound everything below: the native count datum is vectorlike and even-typed; nothing in this
route moves that.

## 1. The anti-import certificate: where the 3 comes from (every step measured)

Inserted data — the only inserted data: **dim X = 4** and **the base is Lorentzian** (one time
direction). Everything else is measured by the script:

| step | object | measured result |
|---|---|---|
| 1 | fiber = Sym^2(T*X), dim | 10 (basis constructed) |
| 2 | Frobenius form on Sym^2, Lorentzian base | signature **(7,3)** |
| 3 | trace-reversed Frobenius (repo form, `V = F − (1/2) tr tr`) | **(6,4)**, and **(6,4) again under g → −g** (mostly-plus vs mostly-minus does not matter for the fiber) |
| 4 | total = fiber + base | **(9,5)**, p − q = 4 (the repo's Cl(9,5)) |
| 5 | compatible complex structure J on the measured R^(6,4) (canonical J + 20 random O(6,4)-conjugates) | Hermitian signature **(3,2)** every time — J-independent |
| 6 | maximal positive complex subspace | **C^3** (3 = positive-eigenvalue COUNT) → positive lines retract to **CP^2** |

Controls (the chain is signature-selective, not a tautology):

- **Euclidean base (4,0):** Frobenius (10,0) → trace-reversed **(9,1)** — p odd, **no compatible
  complex structure exists** (a compatible J complexifies both inertia subspaces, forcing p and q
  even; conjugate the circle group exp(tJ) into the maximal compact O(p)×O(q) to see it). The entire
  CP-coset channel is absent for a Euclidean base: it exists *because* the base is Lorentzian.
- **eta(8,2):** Hermitian (4,1) → CP^3, chi would be 4. **eta(10,0):** (5,0) → CP^4, chi 5.
  Different inputs give different n — the machinery does not always output 3.

## 2. (a) The coset and the explicit retraction — THEOREM

**D = { positive complex lines in C^(3,2) }**, an open subdomain of CP^4 (openness: strict inequality
`<v,v> > 0` in a continuous function of the line).

**Homogeneity, verified at the Lie-algebra level:** the 25-generator basis of u(3,2)
(`A = iHM`, M Hermitian; max residual `|A†H + HA| = 0.0e+00`) gives orbit dimension **8 = dim_R CP^4**
at `e1` and at **50 random positive lines** — every orbit is open, D is connected (it retracts, below),
so D is a **single orbit**. Stabilizer dimension in su(3,2): **16 = dim s(u(1) × u(2,2))**
(= 1 + 16 − 1), i.e. D = SU(3,2)/S(U(1) × U(2,2)) as assigned.

**The retraction, as a construction (not a citation):** split v = (v₊, v₋) ∈ C^3 ⊕ C^2 along the
maximal positive subspace and flow

```
r_t([v]) = [(v₊, (1−t) v₋)],   t ∈ [0,1].
```

Well-defined on lines (scaling-covariant), continuous, r₀ = id, r₁(D) = P(C^3) = CP^2, r_t = id on
CP^2 for every t. Domain preservation is an inequality, not a hope:
`<v(t),v(t)> = |v₊|² − (1−t)²|v₋|² ≥ |v₊|² − |v₋|² = <v,v> > 0` (and v₊ ≠ 0 on D since
`<v,v> > 0` forces `|v₊|² > |v₋|²`). So D deformation-retracts onto CP^2; D ≃ CP^2.

**Numerical verification:** 2000 random positive lines, 201 time steps each — minimum over all
trajectories of `<v(t),v(t)>/|v(t)|²` = **0.001914 > 0** (never leaves D), Hermitian norm
nondecreasing on every trajectory, every endpoint lands in CP^2.

**Control:** the same flow on 500 random **negative** lines crosses the null cone **500/500** times —
the "stays in domain" check fails where it must, so the verification has discriminating power.

## 3. (b) chi(CP^2) = 3, computed, not recalled — THEOREM

**Cellular:** stratify CP^n (n = 2 **measured** in step 6) by last nonvanishing homogeneous
coordinate: one cell in each real dimension 0, 2, 4. No odd cells → every cellular differential has
zero source or target → all differentials vanish → Betti numbers **b₀..b₄ = 1, 0, 1, 0, 1** →
**chi = 3**. Provenance printed by the script: chi = n + 1 with n = 2, and n = 2 because the maximal
positive subspace of C^(3,2) is C^3 (measured), and THAT descends from fiber (6,4) = trace-reversed
(7,3), which descends from dim X = 4 plus one time direction (total p − q = 4).

**Independent differential-geometric measurement (a check that could fail):** 4d Chern-Gauss-Bonnet
`chi = (1/32π²) ∫ (|Riem|² − 4|Ric|² + R²) dV` [standard math, from memory — normalization certified
empirically by the S^4 control] on the Fubini-Study metric, with the metric itself verified against
nested finite differences of the Kähler potential (residual 7.1e−11), curvature by nested 5-point
finite differences, volume by quadrature:

- CP^2: GB scalar 191.999985 / 191.999996 at two points (homogeneity 6.0e−08), Vol = 4.93480220
  (= π²/2), **chi_GB = 3.000000**.
- **S^4 control (same pipeline, different metric): chi_GB = 2.000000.** Non-tautological.

## 4. (c) c1(T CP^2) = 3h via the Euler sequence — THEOREM

Truncated-polynomial arithmetic (sympy), n = 2 measured:

```
c(T CP^2) = (1+h)^3 mod h^3 = 1 + 3h + 3h^2
c1 = 3h        c2 = 3h^2
<c2,[CP^2]> = 3 = chi   (top Chern = Euler class; agrees with cellular 3 and GB 3.000000)
<c1^2,[CP^2]> = 9
```

Annotated consistency note (not used to derive anything): intersection form [⟨h,h⟩] = [1] →
σ(CP^2) = +1; ⟨p1⟩ = c1² − 2c2 = 3 = 3σ (Hirzebruch). Controls: CP^1 gives c1 = 2h, chi = 2; CP^3
gives c1 = 4h, chi = 4.

So the breaking coset candidate carries, canonically: **H^2(D;Z) = Z (free, torsion-free)** generated
by h, and a **canonical 3-divisible class c1(TD) = 3h** — the anticanonical class. This is the first
named channel in the program whose discrete invariants are not 2-adic.

## 5. (d) The honest gap: does the 3 reach the generation index? — CONSISTENT_UNCOMPUTED

A condensate section over X^4 is a map f: X^4 → D ≃ CP^2. Available pullback data on a 4-manifold:
y = f*h ∈ H²(X;Z), y² = f*(h²) ∈ H⁴(X;Z), degree datum d = ⟨y², [X]⟩. Twist the generation operator
by L = f*O(m). The symbolic index (h2 canon formula + twist; Dynkin anchors T(1/2) = 1/2, T(1) = 2
reproduced):

```
ind(D_X ⊗ V_R ⊗ L) = 2 T(R) k + dim(R)·(m² d / 2) + dim(R)·Ahat[X]
full 16-dim multiplicity bundle:  ind_full = 12k + 8 m² d − 2σ
X spin ⇒ intersection form even ⇒ d = 2d' ⇒ ind_full = 12k + 16 m² d' − 2σ   — EVEN, always.
```

Three sharp facts, printed by the script:

1. **Which term of the h2 canon formula the twist enters:** only `rk(V)·c1(L)²/2`, because
   `ch1(V_R) = 0` for every GU-native (traceless su(2)) channel. The CP^2 channel enters through a
   term **identically absent** from the native 12k arithmetic — a genuinely new channel, not a
   re-dress.
2. **How the 12k/2-adic wall constrains it:** on spin X the twist term is even (even intersection
   form; Rokhlin handles the gravitational term independently). **The CP^2 twist cannot make the
   full-bundle index odd.** What it can inject is 3-divisibility: `16 m² d' ≡ m² d' (mod 3)` is
   3-divisible for all d' **iff 3 | m** — and m = ±3 is exactly the (anti)canonical class
   c1 = 3h measured in (c). The channel's payoff shape is "the count is a multiple of 3," not "the
   count is odd 3"; an odd net 3 still requires the h2 §4 truncation route on top.
3. **The sub-sector trap, named to avoid conflation:** the (3,2) generation sub-sector with su(2)−
   gauged gives `ind = 3(k₋ + m²d)` — 3-divisible for ANY m, but that 3 is the **native multiplicity
   riding along** (h2 canon §4: import k₋ + truncation), not a new coset-born 3.

**What would settle the index leg (stated, not done):**

- **(i) Equivariant m-selection** — decompose the condensate channel of the 1792-dim carrier under
  the stabilizer S(U(1) × U(2,2)) and read off which homogeneous line bundle O(m) on
  D = SU(3,2)/S(U(1)×U(2,2)) the breaking direction transforms in. m = ±3 (canonical class) makes the
  3-divisibility canonical; any other m makes it an import. Finite-dimensional, executable in
  principle — this is the natural next script.
- **(ii) A nonconstant section f** — needs the unbuilt condensate dynamics; its degree d is otherwise
  a free import, exactly like k in 12k.
- **(iii) The C-07 twisted check** — build the induced generation operator with the L-twist and
  measure its spectrum (see §6.3 below).

## 6. (e) Adverse-evidence confrontation (mandatory)

### 6.1 Why the CP^2 channel is not the RP^3 / Z_2 channel

The RP^3 whose H²(RP^3;Z) = Z_2 is the **metric fiber** of Y14 itself (GL(4,R)/O(3,1) ≃ RP^3): the
families-index home GU's signature points at, 2-torsion, 3-free. D is a **different object at a
different layer**: not the fiber of the metric bundle, but the vacuum manifold of a symmetry-breaking
choice — a positive complex line in the J-complexified fiber form space, entering through the
breaking coset. Its H²(D;Z) ≅ H²(CP^2;Z) = **Z, free**, with the canonical 3-divisible c1 = 3h. The
profiles are measurably different, not rhetorically different.

**What evasion (rather than mere difference) still requires:** showing GU's actual breaking — the
[00:46:40] decreased-VEV datum — has D as its vacuum manifold. Two unproven premises: (α) a compatible
complex structure J is canonically present (the Hermitian signature (3,2) is J-INDEPENDENT, measured
over 21 J's, so the coset's homotopy type is robust to *which* J; but *whether any* J is canonical is
exactly T1'/R4-gated territory — a separate workflow is running those routes; gates only, no outcomes
cited here); (β) the condensate is valued in the line space of C^(3,2) rather than in the metric
fiber. "Positive lines" as the vacuum manifold is itself a modeling choice ("a positive-norm
condensate direction") — flagged, not derived.

### 6.2 Why it is not the native 12k channel

The 12k arithmetic lives in ch2 of traceless su(2) bundles (ch1 = 0). The CP^2 twist enters only
through `rk·c1(L)²/2` — absent from every native channel. But the confrontation cuts both ways, and
the script prints it: the new term is **even on spin X**, so the channel *respects* the 2-adic wall
rather than climbing it. It cannot deliver an odd count; it can deliver 3-divisibility, and only if
m ≡ 0 (mod 3), i.e. only through the anticanonical class. To evade rather than differ: derive m = ±3
equivariantly (§5 i) and a nonzero d (§5 ii). Both unconstructed.

### 6.3 Why it is not the mod-2 inflow / C-07 channel — and what escape-of-hypothesis does NOT prove

The Witten mod-2 index registers parity for **pseudoreal** reps; the Kramers/quaternionic evenness
argument (h2 canon §3c, the robust backbone of C-07-adjacent evenness) requires a **real** rep so that
J = j_S ⊗ j_R with J² = −1 exists. A line bundle L is complex — neither real nor pseudoreal — so both
hypotheses fail and neither wall *applies* to the twisted channel. That is an escape of hypothesis,
**not a counterexample**: nothing here shows the twisted operator actually has odd or 3-divisible
signature. To evade rather than differ, the induced generation operator twisted by f*O(m) must be
built on the carrier and its spectrum measured — the same discipline C-05/step9 applied to the native
connections (which all gave identically 0).

## 7. Verdict and standing

| leg | result | grade |
|---|---|---|
| (a) D ≃ CP^2, explicit retraction | constructed + verified (2000 lines, min rel. norm 0.001914; negative control 500/500 fails) | THEOREM |
| (b) chi = 3 with provenance | cellular (1,0,1,0,1) AND Gauss-Bonnet 3.000000 (S^4 control 2.000000) | THEOREM |
| (c) c1 = 3h, ⟨c2⟩ = 3, ⟨c1²⟩ = 9 | truncated Euler-sequence arithmetic, n measured | THEOREM |
| (d) the 3 reaching the index | twist term even (respects 2-adic wall), 3-divisible iff 3 \| m; m-selection + section + C-07 twisted check all unperformed | CONSISTENT_UNCOMPUTED |
| **route** | the coset carries a measured, provenance-clean 3-divisible invariant; the transfer to the count is the open invoice | **CONSISTENT_UNCOMPUTED** |

**Against the kill conditions (Section 6.2 of the persona doc):**

- **KC-2 (T2' typed failure: vacuum manifold connected in the relevant degree / only 2-torsion or
  even classes):** does **not fire** on this candidate — for the first time a named breaking channel
  has H² = Z free with a canonical 3-divisible class, measured not recalled. But KC-2 is not
  *survived* yet either: the clause "the integer never arrives" remains live until §5(i)–(iii) are
  done, and the whole thing is conditional on D being the actual breaking coset (6.1 α, β).
- **KC-3 (C-07 fork closure: every non-native candidate certified a foreign import):** informed — the
  CP^2 line-bundle twist is now a *specific, named* non-native candidate that escapes the
  Kramers/real-rep hypothesis; the m-selection computation (§5 i) is exactly the certification test
  that would stamp it "canonical" or "import."

**Honest gaps carried:** (1) D is a candidate coset — the identification of the [00:46:40] VEV's
vacuum manifold with D is unproven, and gated on the running R-routes (J-canonicity / conformal fiber);
(2) the index leg is fully uncomputed — no m, no section, no d; (3) the channel provably cannot
produce an *odd* count on spin X — the payoff shape is 3-divisibility, and odd-3 would still need the
truncation route on top; (4) "positive lines" as the vacuum manifold is a modeling choice; (5) the
Gauss-Bonnet normalization and the Dynkin/Hirzebruch formulas are standard math from memory, anchored
empirically (S^4 → 2; T(1/2) = 1/2; σ(CP^2) = 1) rather than re-derived.
