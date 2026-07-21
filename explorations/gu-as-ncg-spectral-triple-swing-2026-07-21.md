---
title: "Swing: recast GU as an NCG spectral triple — does a substructure generate the SM gauge group, and is it FORCED (SM output, matches Connes) or an external selector (GU hosts)?"
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (pre-registered NCG spectral-triple swing on GU's SM structure)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
inputs:
  - canon/shiab-existence-cl95.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/type-ii1-spectral-sm-checklist.md
  - explorations/type-ii1-spectral/type-ii1-oq1-j2-section-pullback-2026-06-23.md
  - explorations/type-ii1-spectral/type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md
  - explorations/type-ii1-spectral/type-ii1-ko-dimension-2026-06-23.md
  - explorations/channel-swing-CH-SM-2026-07-19.md
  - explorations/per-leg-recovery-state-2026-07-21.md
  - explorations/comparative-tensions-ledger-qg-toe-2026-07-21.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/generation-sector/gen_sector_bridge.py
probe: tests/channel-swings/gu_as_ncg_spectral_triple_probe.py (20 checks, ALL PASS, exit 0, deterministic)
---

# Recast GU as an NCG spectral triple: is the SM an OUTPUT or a hosted import?

**The decisive question (Joe's).** In Connes-Chamseddine (CC) noncommutative
geometry, the Standard Model gauge group is an **output**: you posit a finite
algebra `A_F = C (+) H (+) M3(C)`, and `U(A_F)` mod unimodularity/center *is*
`U(1) x SU(2) x SU(3)`; the Higgs is an inner fluctuation of the Dirac operator;
the fermion reps and hypercharges come from the representation of `A_F` on the
finite Hilbert space. If GU's SM structure could be made an output the same way —
if we found "the algebra of the bit" — GU would **match NCG's derivation status**
instead of merely **hosting** the SM with imported selectors. This swing tests
exactly that by trying to recast GU as a spectral triple `(A_GU, H_GU, D_GU, J,
gamma)` and asking whether a **forced substructure** delivers the SM gauge group.

**Headline (honest, NEGATIVE for "GU matches NCG"; CONFIRMS hosts-not-derives).**

1. **GU DOES recast as a bona fide real spectral triple** — but at **KO-dimension
   4 (mod 8)**, the quaternionic / `KSp` lane — **NOT** KO-dimension 6, the lane
   where the CC finite SM lives. Two of the three KO signs are verified directly
   on GU's `Cl(9,5)=M(64,H)` representation and *contradict* KO-6.
2. **The SM gauge group is NOT `U(A_GU)`.** `A_GU = M(64,H)` is a **simple**
   algebra; its unitaries are `Sp(64)` (dim 8256), a **simple** compact group with
   no `U(1) x SU(2) x SU(3)` product decomposition.
3. A subalgebra with SM-group unitaries **exists** (`C(+)H(+)M3(C)` embeds), **but
   it is NOT forced**: inside a *simple* algebra it is one member of a
   positive-dimensional conjugation orbit, singled out by nothing in GU's
   structure. **Selecting it IS the imported gauge selector.** This is the exact
   structural inverse of NCG, whose derivation *comes from* taking a small
   **block-sum** algebra as the primitive datum.
4. **Generations do NOT come out** — and GU is if anything *worse* than NCG here:
   NCG puts `N=3` in by hand; GU's quaternionic `J^2=-1` (Kramers) *forbids* an odd
   index from native carriers, so an odd count needs a non-quaternionic import. No
   bonus.

**Grade: RECASTS + SM NOT FORCED** (the pre-registered "likely" outcome), with the
sharper finding that GU recasts at the **wrong KO-dimension and wrong algebra
class** to *be* the CC SM geometry even in principle. This consumes and unifies the
banked Type II_1 `OQ1`/`OQ2`/KO-dim results into one direct statement and moves no
claim, verdict, or posture.

---

## 0. Setup: the two mechanisms are different objects

| | Connes-Chamseddine NCG | GU (Observerse) |
|---|---|---|
| Primitive algebra | `A_F = C (+) H (+) M3(C)` (**block sum**, dim_R 24) | `Cl(9,5) = M(64,H)` (**simple**, dim_R 16384) |
| KO-dimension of finite/internal part | **6 mod 8** (`J^2=+1`, `Jg=-gJ`) | **4 mod 8** (`J^2=-1`, `Jg=+gJ`) |
| Gauge group | `U(A_F)` mod unimodularity `= U(1)xSU(2)xSU(3)` (**output**) | `Sp(64)` structure group of `S=H^64`, then a **broken** subgroup selected by an imported Spin(10)->G_SM chain + VEV (**hosted**) |
| Higgs | inner fluctuation `D -> D + A + JAJ^-1` (**output**) | not from inner fluctuations; `D_GU` fluctuations preserve the input `Sp(64)` orbit (OQ2) |
| Generations | `N=3` put in by hand (multiplicity of `H_F`) | `3 = dim Lambda^2_+` located, **not forced**; native carriers forced **even** index |

The point of the table: NCG's derivation is *powered by the block-sum structure of
`A_F`*. A direct sum of blocks has a product unitary group; that product *is* the
gauge group. GU's primitive algebra is **simple**, so it has no blocks to read a
product group off of. Everything below is a consequence of that one difference.

---

## 1. Persona (i) — NCG spectral-triple theorist (the axioms and the gauge map)

**What a valid CC-style recasting requires** (Connes; Chamseddine-Connes-Marcolli):
a real, even spectral triple `(A, H, D, J, gamma)` with

- `A` an involutive algebra represented on `H`; `D` self-adjoint with compact
  resolvent and `[D,a]` bounded;
- grading `gamma`, `gamma^2=1`, `[gamma,a]=0`, `{gamma,D}=0`;
- real structure `J` antilinear isometry with the **KO-dimension sign triple**
  `(eps, eps', eps'') = (J^2, JD=eps' DJ, Jgamma=eps'' gammaJ)`;
- **order-zero** `[a, JbJ^-1]=0` and **order-one** `[[D,a], JbJ^-1]=0`.

The **gauge group** is `U(A)` acting by `a -> u a u*` and `D -> D + A + JAJ^-1`;
after removing the unimodularity/center it is the physical gauge group, and the
off-diagonal (Higgs) part of `D` transforms as the correct representation. For the
finite SM this works **because** `A_F = C(+)H(+)M3(C)`: the three summands give
`U(1)`, `SU(2)`, `SU(3)`; the hypercharges come from the *specific* bimodule
`H_F = C^96` (one generation, with `nu_R`) and the order-one condition; **KO-6 is
mandatory** — it is the sign package that produces the correct fermion doubling and
permits the Majorana/seesaw term.

**KO sign table (mod 8):**

| KO-dim | `eps=J^2` | `eps'` (JD/DJ) | `eps''` (Jg/gJ) |
|---|---|---|---|
| 0 | +1 | +1 | +1 |
| 2 | -1 | +1 | -1 |
| **4** | **-1** | **+1** | **+1** |
| **6 (CC SM)** | **+1** | **+1** | **-1** |

The theorist's demand on GU: exhibit `(A_GU, H_GU, D_GU, J, gamma)`, read its KO
signs, compute `U(A_GU)`, and check order-one. If `U(A_GU)` is not a product and no
sub-datum forces `A_F`, GU is **not** deriving the SM the CC way.

---

## 2. Persona (ii) — Clifford / GU-structure expert (the ingredients exist)

GU supplies every ingredient of a spectral triple, and they assemble:

- **Algebra.** `Y^14 = Met(X^4)` has signature `(9,5)` (Frobenius metric +
  trace-reversal; `canon/shiab-existence-cl95.md`). `Cl(9,5)` has index
  `(9-5) mod 8 = 4`, so `Cl(9,5) = M(64,H)` (Lawson-Michelsohn). Take
  `A_GU = M(64,H)` (or the GU-native operator subalgebra, contained in the
  `J_quat`-commutant `M(14,C) (x) M(64,H)`).
- **Hilbert space.** `H_GU = ` the spinor module `S = H^64` (dim_R 256), or the
  full Rarita-Schwinger / chimeric bundle `vector (x) spinor` (the `14 x 128`
  module carrying the RS index) on which `Pi_RS`, `M_D` act.
- **Dirac.** `D_GU = d_A + d_A^* + Phi` (the twisted RS operator with the shiab
  contraction `Phi`), or the finite symbol `M_D = sum xi_a e_a`.
- **Grading.** the chirality `omega = e_1...e_14`, `omega^2 = +1`, `{omega,e_a}=0`,
  splitting `S = S^+ (+) S^-`.
- **Real structure.** `J_quat = C . (complex conj)`, `C` the charge-conjugation
  word, `J_quat^2 = -1` (quaternionic; per-generator EXACT in
  `canon/no-go-quaternionic-parity-generation-sector.md`).

**Order-zero / order-one hold for the H-linear algebra.** `J_quat` is right-`H`
multiplication, i.e. the *commutant* of the left `M(64,H)` action; left and right
`H`-actions commute, so `[a, J_GU b J_GU^-1]=0` (order-zero). Every GU-native
primitive is `H`-linear (commutes with `J_quat`), so `[D_GU,a]` is again `H`-linear
and commutes with `J_GU b J_GU^-1` (order-one). **So GU is a legitimate real
spectral triple.** Its KO signs, read on the actual `M(64,H)` representation:
`eps = J^2 = -1`, `eps'' = +1` (`J omega J^-1 = +omega`), `eps' = +1` (classification
KO-4 row). That is **KO-dimension 4**, the quaternionic/`KSp` lane.

**The even part and subalgebras.** `Cl(9,5)` is simple; its even subalgebra
`Cl^0(9,5) = Cl(9,4) = M(32,H) (+) M(32,H)` (two quaternionic blocks — the chirality
split; type `H(+)H` since `(9-4) mod 8 = 5`), still far larger than `A_F`. `A_F` and
its complexification `C (+) M2(C) (+) M3(C)` embed
into `M(128,C) = M(64,H) (x) C`, but as tiny subalgebras chosen from an enormous
family (Section 4).

---

## 3. Persona (iii) — Representation theorist (which subalgebra, and does anything come out)

**Does `C(+)H(+)M3(C)` sit inside `M(64,H)`?** Yes. Its complexification
`C (+) M2(C) (+) M3(C)` (complex dim `1+4+9 = 14`) has a faithful representation on
`C^{1+2+3}=C^6 subset C^128 = H^64 (x)_R C`, compatible with the quaternionic
`*`-structure. Its unitary group is `U(1) x SU(2) x U(3)`, giving
`U(1) x SU(2) x SU(3)` after unimodularity — the SM gauge group. So **a subalgebra
whose unitaries are the SM group exists.** (Probe step C: the generated `*`-algebra
closes at `dim_C = 14`, exactly this complexification.)

**Does the fermion content / hypercharges come out?** Only if you *also* supply the
CC finite Dirac `D_F` (the Yukawa/off-diagonal operator) that satisfies **order-one
for `A_F`** and encodes the hypercharge assignment via its off-diagonal support.
GU's native `D_GU` does **not** supply this: `OQ2` shows `D_GU`'s inner
fluctuations preserve the input `Sp(64)` connection orbit — they do not produce the
CC one-form bimodule or select `SU(3)xSU(2)xU(1)/Z_6`. A generic self-adjoint `D`
*violates* order-one (probe step D, defect 15.5); only a specially adapted
`D = D_L (x) I + I (x) D_R`-type operator passes (defect 0). **The order-one finite
Dirac is a special import, not something GU's structure hands you.**

**The route GU actually uses is a different mechanism.** GU's hosted SM content
(CH-SM sweep) comes from a **Spin(10) grand-unified embedding** and a symmetry-
breaking chain `Spin(10) -> ... -> G_SM`, selected by a VEV — *not* from
`U(A_F)` of a finite algebra. The CH-SM sweep buys the gauge group, chirality of
one 16, anomaly cancellation, electric charges, and the **absolute hypercharge
normalization** `sin^2 theta_W = 3/8` — a genuinely strong hosting result — but the
selector (which chain, which VEV) is adapter-supplied and typed
(`RECOVERY-NOGO-SM-SELECTOR`: host is not a selector). So GU has *two* distinct
non-NCG routes to the SM content (GUT-breaking, and now this abortive NCG-subalgebra
route), and *neither* is the NCG unitaries-of-the-algebra derivation.

**Generation count.** NCG posits `N=3` as the multiplicity of `H_F` (Chamseddine-
Connes never derive it). GU has `3 = dim Lambda^2_+` as a *located native datum*,
but the quaternionic `J^2=-1` forces **even** index for every GU-native Hermitian
carrier (Kramers; `canon/no-go-quaternionic-parity-generation-sector.md`), so an
**odd** count such as 3 requires importing a non-quaternionic object. GU therefore
does **not** out-derive NCG on generations — it is a tie at best (both import the 3)
and arguably worse (GU's native parity actively resists odd). **The pre-registered
bonus does not materialize.**

---

## 4. Persona (iv) — Skeptic / anti-toy (is the SM subalgebra FORCED, or cherry-picked?)

The whole swing turns on one word: **forced.** The skeptic's hold-the-line test:
*matching-by-construction is the imported selector in disguise, not a derivation.*

**The subalgebra is NOT forced — three independent reasons, all rep-verified.**

1. **Simplicity kills the selector.** `A_GU = M(64,H)` is a **simple** algebra: no
   two-sided ideals, no canonical block decomposition. The copies of `C(+)H(+)M3(C)`
   inside it form a **positive-dimensional `Sp(64)`-conjugation orbit** — conjugating
   one copy by a unitary `g` that does not normalize it gives a *different, equally
   valid* copy (probe step C: off-subspace residual `0.924`, i.e. `g.A_F.g^-1 != A_F`,
   both `dim_C=14`). Nothing intrinsic to the simple algebra prefers one. In NCG the
   analogous choice is *not* free — `A_F` is the **primitive datum**, so its blocks
   are given, not carved. GU has to carve, and the carving is the import.
2. **Wrong KO-dimension.** Even granting a chosen `A_F`, GU's real structure is
   `J^2=-1` at KO-dim 4; the CC SM finite geometry is KO-dim 6 (`J^2=+1`,
   `Jgamma=-gammaJ`). `OQ1` proved ordinary section pullback cannot flip
   `(s^*J_GU)^2 = -1` to `+1`; the KO-dim note found *no* canonical bridge. So GU's
   own real structure cannot *be* the CC SM real structure — the KO-6 `J` has to be
   supplied separately (the Type II_1 route builds a *different* modular `J_tau` from
   a trace; that `J_tau` is an import, not GU's `J_quat`).
3. **The order-one Dirac is imported.** The hypercharge-bearing content lives in the
   off-diagonal `D_F`; GU's `D_GU` preserves the `Sp(64)` orbit and does not supply an
   order-one Dirac for `A_F` (OQ2 + probe step D).

**Verdict of the skeptic:** any "found" SM subalgebra here is **selected**, not
forced. It is the RECOVERY-NOGO-SM-SELECTOR in NCG clothing. The exercise does not
resurrect a derivation; it re-derives the host-not-derive conclusion from a third,
independent direction.

---

## 5. Synthesis — the honest outcome and what "the algebra of the bit" would have to be

**Answering Joe's three sub-questions directly:**

- **(1) Does GU recast as a spectral triple?** **YES** — a genuine *real* spectral
  triple `(M(64,H), H^64/RS-module, D_GU, J_quat, omega)` with order-zero and
  order-one satisfied for the `H`-linear algebra — but at **KO-dimension 4**, the
  quaternionic lane, **not** the KO-dimension 6 where the CC SM lives (two KO signs
  verified on the rep contradict KO-6).
- **(2) Is there a substructure whose unitaries are the SM gauge group?** A
  subalgebra `C(+)H(+)M3(C)` with SM-group unitaries **exists** and embeds, but the
  *whole-algebra* unitaries are `Sp(64)` (simple), not the SM group.
- **(3) DECISIVE — forced or external?** **EXTERNAL.** The subalgebra is one member
  of a positive-dimensional family inside a simple algebra; nothing in GU forces it.
  Plus KO-dim `4 != 6` and the order-one Dirac is an import. **GU HOSTS; it does not
  derive.** On the SM-structure axis NCG out-derives GU — consistent with the banked
  comparative-tensions ledger and per-leg leg-2 (`R1`, 6 typed imports).

**What "the algebra of the bit" would have to be (the exercise's real payoff).** For
GU's SM structure to become an *output* the CC way, GU's primitive internal datum
would have to be **a KO-dimension-6, block-sum algebra containing `C(+)H(+)M3(C)`
with `J^2=+1`**. That is flatly **incompatible** with GU's `(9,5)`/quaternionic
reconstruction, whose internal algebra is **simple**, KO-dim **4**, `J^2=-1`. So the
NCG route does not just fail to fire — it pins *exactly* why: matching NCG would
require replacing GU's signature/algebra class, not adding a lemma. The single most
consequential structural fact is the same one the whole program keeps hitting: GU's
internal algebra is **simple and quaternionic**, and simplicity is precisely what
denies it NCG's block-sum derivation of a product gauge group.

**Does this close the NCG route?** Not as an abstract impossibility — one could
still (a) work in the `KSp`/`KO^4` lane and look for a `KO-4`-native gauge story
(no CC template exists there), or (b) posit a *twisted* real structure
`J_new = K J_GU` with `K^2=-1` to reach `J^2=+1` (OQ1 F4) and then run the full
KO-6 sign + order-one battery — but that `K` is new input, i.e. another import. Both
are open construction problems, not derivations; the honest prior (three independent
obstructions) is against them.

**Generation count:** does **not** come out (located `3=dim Lambda^2_+`, not forced;
quaternionic even-index no-go). No bonus over NCG.

**Honest grade: RECASTS + SM NOT FORCED.** A clarifying negative: GU is a real
spectral triple, but a KO-4 quaternionic simple one that cannot host NCG's
derivation mechanism. This is **PROPOSAL-grade support for the existing "hosts, not
derives" canon**, reached by an independent NCG-language route; it self-banks
nothing and moves no verdict.

---

## 6. Probe receipts

`tests/channel-swings/gu_as_ncg_spectral_triple_probe.py` — **20 checks, ALL PASS,
exit 0**, deterministic (exact integer arithmetic + bit-reproducible linear algebra
on the repo's verified `Cl(9,5)=M(64,H)` rep; the single fixed-seed matrix in step D
witnesses a generic/dense property, seed immaterial):

- **[0] Classification.** `dim_R Cl(9,5) = dim_R M(64,H) = 16384`; KO-dim
  `(9-5) mod 8 = 4`; KO-4 triple `(-1,+1,+1)` vs KO-6 `(+1,+1,-1)` DIFFER.
- **[A] Recast on the 128-dim rep.** Clifford relations exact; `omega^2=+1`,
  `{omega,e_a}=0`; `C^2=-1`; `J_quat^2 = -1` (`eps=-1`); `J omega J^-1 = +omega`
  (`eps''=+1`) — two independent, rep-verified mismatches with KO-6.
- **[B] Unitary gap.** `dim Sp(64)=8256` vs `dim(u(1)+su(2)+su(3))=12`; `Sp(64)`
  simple, no product `U(1)xSU(2)xSU(3)`.
- **[C] Not forced.** `A_F` closes as a `*`-subalgebra (`dim_C=14`); a fixed
  non-normalizing conjugation `g.A_F.g^-1` is a *different* subalgebra (residual
  `0.924`), same dimension — a positive-dimensional family, none distinguished.
- **[D] Order-one is a selector.** generic self-adjoint `D` violates order-one
  (defect `15.5`); an adapted `D_L(x)I + I(x)D_R` satisfies it (defect `0`) — the
  finite Dirac is a special import.

Consistency with banked results (consumed, not re-run): `OQ1`
(`(s^*J_GU)^2=-1`, no section-pullback bridge to KO-6); `OQ2` (`D_GU` fluctuations
preserve the `Sp(64)` orbit, no CC bimodule); KO-dim note (GU `J^2=-1` is KO-4/`KSp`,
CC SM is KO-6); `canon/no-go-quaternionic-parity-generation-sector.md` (quaternionic
even-index wall); CH-SM (SM hosted via Spin(10) breaking, selector imported);
comparative-tensions ledger (NCG out-derives GU on SM structure).

---

## 7. Boundary

Exploration tier. **One new file** (this doc) + **one new probe**
(`tests/channel-swings/gu_as_ncg_spectral_triple_probe.py`). No other file touched —
no CANON, LANE-STATE, README, NEXT-STEPS, or any other agent's artifact. **No claim-
status, canon-verdict, paper-status, or public-posture change**: the outcome
(RECASTS + SM NOT FORCED) *confirms* the standing "GU hosts, does not derive" canon
via an independent NCG route; it does not move it. A positive would have been
PROPOSAL-grade pending hostile verification and never self-banked — but the outcome
is the negative/clarifying one, so there is no positive to guard. **No commit, no
push.** Research-only; Joe alone publishes.
