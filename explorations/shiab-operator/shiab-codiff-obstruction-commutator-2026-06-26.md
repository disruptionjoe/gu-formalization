---
title: "Is the obstruction the commutator [Pi_RS, c.d*] = 343.73? (Computation B)"
date: "2026-06-26"
problem_label: "FC4-WORLDMODEL-COMMUTATOR-B"
status: RESOLVED
verdict: PARTIAL — obstruction is genuinely commutator-shaped (nonzero), but 343.73 is NOT that commutator, and the "d^2=0 iff [Pi_RS,codiff]=0" equivalence is a loose analogy (machine-refuted)
---

# Is the obstruction the commutator [Pi_RS, c.d*] = 343.73?

Code: `tests/shiab_codiff_obstruction_commutator.py` (runnable; builds everything
from the verified `oq_rk1_cl95_explicit_rep` Cl(9,5)=M(64,H)~M(128,C) rep).

## The world-model claim under test (persona 39, MMO / world-model)

> "Take `Phi := P o c o d*` with `P = Pi_RS` (the constraint projector). Then
> `d^2 = 0` iff `[Pi_RS, c o d*] = 0`, and the repo's already-measured `343.73`
> IS the magnitude of exactly this finite, computable commutator on `H^64`."

Three sub-claims, tested separately:
- (a) the commutator is nonzero (a genuine obstruction);
- (b) its magnitude equals/relates to the measured `343.73`;
- (c) "`d^2=0` iff `[Pi_RS, codiff]=0`" is a real equivalence.

## What was built (first principles, no tuning)

On the FULL vector-spinor space `VS = R^14 (x) S = C^1792` (`S = C^128`):

- `Gamma` = 14D gamma-trace, `Gamma(psi) = sum_a c(e_a) psi_a` (the spin-3/2
  irreducibility constraint `gamma^a psi_a = 0`). Surjective onto `S` (rank 128).
- `Pi_RS` = orthogonal projector onto `ker(Gamma)`, **rank 1664** (=1792-128).
  Verified: idempotent err `1.7e-14`, Hermitian err `0`, `||Gamma . Pi_RS|| = 1.1e-14`.
- `M_D = id_14 (x) c(xi)` = twisted Dirac principal symbol — **the operator the
  repo's 343.73 code actually contracts with**.
- `c.d*` (literal Clifford-o-codifferential endo): `(c.d* psi)_b = c(e_b)(sum_a xi_a psi_a)`.
- `grad.div` (pure form-sector codiff, no Clifford): `psi_b -> xi_b (sum_a xi_a psi_a)` — contrast.
- `shiab` = canon Clifford contraction `Omega^2 (x) S -> Omega^1 (x) S`,
  `shiab(e^i^e^j (x) s) = e^i (x) c(e^j)s - e^j (x) c(e^i)s` (kept distinct from `d*`, canon SC1).

`xi` = the repo's fixed sample covector. Norms are Frobenius (matching the repo's `np.linalg.norm`).

## Actual computed outputs

Reproduced the repo anchor exactly: **343.730237**.

| operator `M` | `\|\|[Pi_RS, M]\|\|` (the claim's object) | `\|\|Pi_perp M Pi\|\|` (off-surface escape) | `\|\|Pi M Pi\|\|` (compression) | `\|\|(Pi M Pi)^2\|\|` |
|---|---|---|---|---|
| `M_D` (twisted Dirac symbol, repo's op) | **58.72** | 41.52 | 287.68 | 1213.29 |
| `c.d*` (literal Clifford o codiff) | **113.42** | 83.04 | 278.54 | 1656.65 |
| `grad.div` (no Clifford) | 203.93 | 144.20 | 534.39 | 25432.59 |

All commutators are **nonzero**. **None equals 343.73.**

### What 343.73 actually is (exact decomposition)

`343.73 = || (Pi_RS . M_D . Pi_RS)|_(S+ -> S-)  applied to the gauge image ||`.

- Full `S+ -> S-` compression block `||P_minus M_D P_plus|| = 203.42`.
- Restricted to the 64-column (un-normalized) pure-gauge image `xi (x) eps`: **343.73**.
- The ACTUAL commutator `||[Pi_RS, M_D]|| = 58.72`; restricted to the gauge image
  `||[Pi_RS, M_D] . gauge|| = 119.64`.

So `343.73` is the norm of the **constraint-COMPRESSED Dirac symbol applied to the
(un-normalized) pure-gauge modes** — a *diagonal* (surface-preserving) block hit on
gauge inputs. A commutator is the *off-diagonal* (surface-escaping) part. They are
different operators, and 343.73 even exceeds the full block norm because the gauge
embedding `vstack(xi_a I)` carries its own `|xi|*sqrt(64)` scale. **343.73 is not a
commutator of `Pi_RS` with anything.**

### shiab (canon Clifford contraction, distinct from d*)

- `||Gamma^(1) . shiab|| = 215.85 != 0` -> shiab does **not** map `ker(Gamma^(2))` into `ker(Gamma^(1))`.
- `||(I - Pi_RS) . shiab|| = 57.69 != 0`.

So the canonical shiab is *also* not a constraint-surface-preserving operator, and it
is a genuinely different object from `d*` (different escape/commutator footprints) —
confirming canon SC1's shiab != d* distinction is real and measurable, not cosmetic.

### The "d^2 = 0 iff [Pi_RS, codiff] = 0" equivalence — machine-refuted

Take `M = Pi_RS` itself. Then `[Pi_RS, M] = 0` exactly (it commutes), yet the natural
constrained operator `D = Pi_RS . M . Pi_RS = Pi_RS` has `D^2 = Pi_RS != 0`
(`||D^2|| = 40.79 = sqrt(1664)`). So **"[Pi,M]=0 => D^2=0" is FALSE**; the forward
direction of the stated "iff" does not hold. Analytically: `[Pi,M]=0 => D = Pi M Pi
= M Pi`, so `D^2 = Pi M^2 Pi`, which is zero only if `M^2` annihilates the surface —
not automatic. The true, correct statement is the weaker one:

> `[Pi_RS, M] = 0  <=>  M preserves the constraint surface ker(Gamma)`
> (i.e. `M` is block-diagonal w.r.t. `ker(Gamma) (+) ker(Gamma)^perp`).

The de Rham `d^2=0` framing and the "iff" are a **loose analogy**, not a theorem.

## Verdict on the three sub-claims

- **(a) Nonzero commutator / genuine obstruction? YES.** `[Pi_RS, c.d*] != 0`
  (= 113.42 for literal `c.d*`; = 58.72 for the Dirac symbol the repo uses). The
  codifferential/Dirac symbol genuinely fails to preserve the gamma-trace constraint
  surface. The qualitative world-model intuition — "an obstruction lives here, and it
  is commutator-shaped (`Pi_RS` does not commute with the relevant differential)" — is
  **correct and now quantified for the first time**.
- **(b) Magnitude = 343.73? NO.** The commutator is 58.72 / 113.42; `343.73` is a
  different object (compressed Dirac symbol on the un-normalized gauge image). The
  persona's literal identification "343.73 IS the commutator" is **FALSE**. They are
  *related* only in that both witness `im(d_A)`/the Dirac symbol escaping `ker(Gamma)`.
- **(c) "d^2=0 iff [Pi_RS,codiff]=0"? LOOSE ANALOGY (refuted as stated).** Forward
  direction fails by explicit machine counterexample (`M=Pi_RS`). The genuine content
  is the weaker equivalence `[Pi_RS,M]=0 <=> M preserves ker(Gamma)`.

## Choice-dependence (stated honestly)

- The exact commutator VALUE is choice-dependent: it depends on which "codifferential"
  is meant (twisted Dirac symbol 58.72 vs literal `c.d*` 113.42 vs `grad.div` 203.93 —
  the persona itself flagged this ambiguity via canon SC1) and scales with `|xi|`
  (the repo's fixed sample covector was used). Frobenius norm throughout.
- The QUALITATIVE results are choice-robust: for every natural operator choice the
  commutator is nonzero, none reproduces 343.73, and 343.73 is structurally a
  compression-on-gauge (not a commutator). The "iff" refutation (M=Pi) is choice-free.

## Net read for the lead

PARTIAL. The lead is **right that a real, commutator-shaped obstruction exists** (and
this computation pins it down: `Pi_RS` does not commute with the codifferential/Dirac
symbol, so a naive constraint-surface quotient fails and gauge-fixing/ghosts are
genuinely required — consistent with, and a cleaner statement of, the repo's existing
"`im(d_A)` escapes `ker(Gamma)`" finding). The lead is **wrong on the two sharp
quantitative claims**: 343.73 is not the commutator, and the "`d^2=0` iff" is not a
theorem. Advance the qualitative framing; kill the "343.73 = `[Pi_RS, c.d*]`" equality
and the "iff".
