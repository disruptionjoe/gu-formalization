---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "R1 big swing (the ACTUAL Cl(9,5) carrier): push 'external by structure' toward unconditional and try to KILL it. TWO legs, both RUN (exit 0). Leg A UPGRADES the residual-closure items (2: APS/end eta; 3: family Chern) from the 2x2 QWZ / 1D-chain stand-ins to the actual 1792-dim gamma-traceless Rarita-Schwinger operator D_RS = E + E^dag built from the repo's verified Cl(9,5) = M(64,H) rep: over a closed loop of RS source parameters, {D_RS, Gamma_15} = 0 EXACTLY (7e-15) => spectrum symmetric about 0 => eta_0 = 0, and the negative-bundle Wilson-loop holonomy = 0 => c1(E_-) = 0. Leg B is the KILL attempt: build (or prove impossible) a covariant operator INTERIOR to class C that FORCES an ODD net chiral count -- which would break Theorem 1 / the 2-primary law. Reduced to a table-free parity criterion: an odd covariant count is possible IFF the carrier contains an odd-DIMENSIONAL so(4)+so(10) irrep. It does not -- only even-dim irreps appear -- so every interior covariant count is even. NO KILL: the no-go is HARDENED from the census's enumerated generator list to a parity theorem on the actual carrier. No target imported."
grade: "exploration / strong. Both legs computed on the ACTUAL Cl(9,5) carrier, not stand-ins. Leg A's structural premise {D_RS, Gamma_15} = 0 is exact (7e-15) and its two consequences (symmetric spectrum => eta_0 = 0; Gamma-conjugation of E_- <-> E_+ => c1(E_-) = 0) are re-derived on the true 1792-dim gamma-traceless RS bundle, upgrading canon/function-space-index-conservation-residual-closure items 2 and 3 from the 2x2 QWZ / 1D-chain stand-ins the doc itself flagged as 'asserted-by-machinery, not re-derived on the true RS bundle'. Leg B's reduction is rigorous (Schur: Gamma_15 central in the even algebra => each so(4)+so(10) irrep sits wholly in W+ or W-; achievable net counts = { sum_R d_R (k_R - l_R) }; parity is odd for some choice IFF some appearing irrep has odd d_R) and non-vacuous (the same machine reports odd-dim irreps as the trigger it looks for). HONEST WALL (Leg A): the only route to a nonzero count leaves the chirality-odd cross-chirality class -- a same-chirality DEFINITE (Riemannian) term that breaks {D, Gamma} = 0 and gives eta != 0; on the true Y14 that definite term is the internal-fiber (K3 / GL(4,R)/O(3,1)) Dirac operator whose family pushforward is the UNBUILT GU source action. The generation-count verdict stays OPEN; nothing here derives three -- it closes the odd-interior route by which three could have been forced from inside the delimited class."
depends_on:
  - canon/function-space-index-conservation-residual-closure-RESULTS.md
  - canon/core-theorems-symbolic-proof-RESULTS.md
  - canon/enum-completeness-class-c-RESULTS.md
  - tests/generation-sector/gen_sector_bridge.py
scripts:
  - tests/big-swing/R1_actual_rs_operator_residual.py
  - tests/big-swing/R1_kill_odd_index_isotypic.py
---

# R1 big swing: harden "external by structure" on the actual carrier, and try to kill it

**The swing.** The program's standing structural claim is that the generation count is **external by
structure** -- no finite endomorphism interior to the delimited class C can produce it. Two things had
been proved only on *stand-ins*: the residual-closure doc
(`canon/function-space-index-conservation-residual-closure-RESULTS.md`) established item 2 (APS/end
`eta_0 = 0`) and item 3 (family index `c1(E_-) = 0`) on a 2x2 QWZ Chern family and a 1D open chain, and
honestly flagged the gap: *"asserted-by-machinery, not re-derived on the true RS bundle."* R1 does two
things, both RUN (exit 0): **Leg A** re-derives those items on the **actual** operator; **Leg B** attempts
the offensive KILL -- construct an interior covariant operator that *forces* an odd count, which would
break Theorem 1.

**Honest outcome.** Leg A: **items 2 and 3 discharged on the actual carrier**, premise exact to `7e-15`.
Leg B: **NO KILL -- the no-go is hardened** from an enumerated-generator census to a table-free parity
theorem. The odd-interior route to "three" is closed; the count remains external and OPEN.

---

## Leg A -- residual-closure items 2 & 3 on the actual RS operator (`R1_actual_rs_operator_residual.py`)

Built the actual `1792`-dim gamma-traceless Rarita-Schwinger operator `D_RS = E + E^dag`
(`E = (1 - Pi) M_D Pi`) from the repo's verified `Cl(9,5) = M(64,H)` rep (via
`tests/generation-sector/gen_sector_bridge.py`), and swept a **closed loop** `xi(theta)` of RS source
parameters. Verified:

- **(P1) Chirality-odd premise, exact.** `{D_RS(theta), Gamma_15} = 0` to `7e-15`, `Gamma_15^2 = I`,
  `D_RS` Hermitian, `Gamma_15` K-anti-self-adjoint, **for every `theta`**. `Gamma_15` is the full
  14-chirality (product of the spinor gammas), central in the even Clifford algebra.
- **(P2 = item 2) `eta_0 = 0` on the actual operator.** `{D_RS, Gamma_15} = 0` forces the block form
  `D = [[0, B],[B^dag, 0]]`, so `spec(D) = +/- sing(B)` is **symmetric about 0** exactly -> the APS/end
  reduced eta vanishes. Verified `eta = 0` at every loop point (max spectral asymmetry at machine zero).
- **(P3 = item 3) `c1(E_-) = 0` on the actual operator.** `Gamma_15` conjugates `E_-(theta) <-> E_+(theta)`
  along the loop, so `c1(E_-) = c1(E_+)`, while `c1(E_-) + c1(E_+) = c1(total) = 0` (the full space is
  trivial) -> `c1(E_-) = 0`. Confirmed both structurally and **numerically**: the discrete Berry /
  Wilson-loop holonomy of the actual negative bundle around the `theta`-loop is trivial, and
  `holonomy(E_-) + holonomy(E_+) = 0` (net chiral family holonomy zero).

**The wall (why this is not yet unconditional).** The *only* way to a nonzero count is to **leave** the
chirality-odd cross-chirality class -- i.e. add a same-chirality **DEFINITE** (Riemannian) term. The script
exhibits the control: adding a Dirac mass `t*Gamma` breaks `{D, Gamma} = 0` and yields `eta != 0`, and it
computes an external definite fiber index that **is odd for odd flux**. On the true `Y14` that definite
term is the internal-fiber (`K3` / `GL(4,R)/O(3,1)`) Riemannian Dirac operator, whose family pushforward is
the **unbuilt GU source action**. That single pushforward is the one open residual; everything else in
items 2 and 3 is now closed on the actual operator.

---

## Leg B -- the KILL attempt: is an odd interior covariant count possible? (`R1_kill_odd_index_isotypic.py`)

**Target.** Construct, or prove impossible, a covariant operator **interior to class C** -- real `Cl(p,q)`,
`p + q = 14`, gamma-traceless rank-3/2 field, the `j = 1` self-dual triplet carrying the cross-chirality
`(+96, -96)` Krein form, equivariant under the sector's split symmetry `so(4) (+) so(10)` -- that **forces
an ODD net chiral count**. Such an operator would break Theorem 1 / the 2-primary structural law.

**Reduction (rigorous, checked in code).** The full chirality `Gamma_15` is central in the even Clifford
algebra, hence commutes with `so(4) (+) so(10)`. By Schur, each irreducible subrep of the `192`-dim carrier
`W` lies **entirely** in `W+` or in `W-` (`Gamma_15` is a scalar on it). Writing
`W = (+)_R [a_R copies of R in W+] (+) [b_R copies of R in W-]`, any equivariant projector `P` has net
chiral count `chi(P) = tr(Gamma_15 P) = sum_R d_R (k_R - l_R)`, `0 <= k_R <= a_R`, `0 <= l_R <= b_R`, with
`d_R = dim R`. So the achievable net counts form the lattice `{ sum_R d_R (k_R - l_R) }`, and:

> an **odd** covariant net chiral count is possible **IFF** the carrier contains an **odd-dimensional**
> `so(4)+so(10)` irrep that actually appears.

**Result (computed).** For `so(4)+so(10)`: **odd-dim irreps present = NONE**; odd count possible =
**False**. Every irrep appearing in the carrier is even-dimensional, so **every** covariant net chiral
count is **even**. The odd count is arithmetically unreachable interior to class C.

**Non-vacuity.** The criterion is a real measurement: the machine is explicitly looking for an
odd-dimensional irrep as the trigger that *would* have permitted an odd count. It found none here; on a
carrier that contained one, it would report `odd count possible = True`.

**What this hardens.** Theorem 1 previously rested on the census's **enumerated generator list**. Leg B
replaces that with a **table-free parity theorem** on the actual carrier: no enumeration, just centrality +
Schur + an even-dimensionality check. The no-go is now structural, not list-dependent.

---

## What this settles, and what it does not

**Settles (this swing).** On the **actual** `Cl(9,5)` carrier (not stand-ins): the residual-closure
items 2 (`eta_0 = 0`) and 3 (`c1(E_-) = 0`) hold over a full source-parameter loop, from an exact
chirality-odd premise; and no interior covariant operator can force an odd chiral count. Both the
"is the residual really external?" and the "can an interior term sneak in an odd count?" questions get
clean answers on the true operator. This **hardens "located, not forced"** by removing the odd-interior
route.

**Does NOT settle (and no target imported).** This does not derive three and does not forbid three. Leg A
leaves exactly one open residual -- the definite internal-fiber (`K3` / `GL(4,R)/O(3,1)`) Dirac index whose
family pushforward is the unbuilt GU source action. Leg B closes only the *interior* route; the count can
still be fixed *externally* by that definite datum. No `chi(K3) = 24`, no `/8`, no `Ahat = 3` entered. The
generation-count verdict stays **OPEN**.

**Where the wall now is.** Build the GU source action (the definite `Y14` internal-fiber Dirac operator and
its family pushforward). That is the single object standing between "external by structure, odd-interior
route closed" and an actual count. It is the same wall named across the program's convergence reads.

**Governance.** Exploration-grade; staged under `explorations/big-swing-2026-07-03/` and `tests/big-swing/`.
This is a GU-carrier-specific hardening certificate, not a standalone theorem, so **no canon promotion is
proposed** (unlike R3 / R4, which are GU-independent and are candidates under the 2026-07-03 Promotion
Rule). The generation-count verdict remains OPEN.
