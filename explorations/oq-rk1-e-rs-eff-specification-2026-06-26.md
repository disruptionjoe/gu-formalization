---
title: "OQ-RK1: E_RS^eff Assembly and the Decisive rank_H(Pi_RS . E_+ . Pi_RS)"
date: "2026-06-26"
problem_label: "OQ-RK1"
status: exploration
doc_type: frontier_run_artifact
verdict: "BLOCKED_NEEDS_SPEC"
integrator_notes_2026_06_26:
  - "Scope of the '4 reachable ONLY via 8/Ahat(K3)' line: this is verified as 'no honest surrogate computed here equals 4 or 8', NOT an exhaustive proof that no other combination could reach 4/8. The forbidden division is refused; the negative claim is bounded to the surrogates actually computed."
  - "The factor-2 in rank_H = rank_C/2 (and ind_H = ind_C/2) is the quaternionic dimension halving from the fiber identity M(64,H) ox_R C = M(128,C). It is NOT Ahat(K3)=2 and is NOT a target-division: it divides independently-computed quantities (832, 96, -640...) and yields large negatives, never the target 8 or 4. The shared numeric divisor 2 is a coincidence, not the forbidden step."
blocking_component: "Gauge/BRST quotient of the RS field (RS_GU^phys / d_RS,-1)"
owned_path: "explorations/oq-rk1-e-rs-eff-specification-2026-06-26.md"
code:
  - "tests/oq_rk1_e_rs_eff_assembly.py"
reuses:
  - "tests/oq_rk1_cl95_explicit_rep.py"
  - "tests/rs_clifford_projector_model.py"
depends_on:
  - "explorations/cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md"
  - "explorations/hourly-20260626-0402-cycle1-physical-rs-ktheory-class-gate.md"
  - "explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
  - "explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
  - "explorations/af4-tau-rs-gauge-fixing-2026-06-23.md"
---

# OQ-RK1: E_RS^eff Assembly and the Decisive rank_H(Pi_RS . E_+ . Pi_RS)

## 0. Question and one-line answer

OQ-RK1 asks for the target-independent quaternionic rank

```text
rank_H( Pi_RS . E_+ . Pi_RS )   in M(64,H)
```

which would return `4` (=> 3 generations) or `8` (=> 4 generations).

**Answer: E_RS^eff is NOT specifiable from current repo data; the decisive rank is
NOT computable. Verdict = BLOCKED_NEEDS_SPEC.** The single load-bearing blocking
component is the **Gauge/BRST quotient of the RS field** — concretely the missing
physical gauge-fixed/BRST RS elliptic complex `RS_GU^phys` (its source-defined
gauge/BRST differential `d_RS,-1`, gauge-fixing condition, ghost complex, and the
resulting K-theory symbol class) on a common source-selected right-H module
`M_RS,H^src`. Every honestly computable surrogate is reported below; **none equals
4 or 8**, and `4` is reachable only through the forbidden `8/Ahat(K3)=8/2`
division.

## 1. Component status at assembly time

| # | Component | Status | What it actually pins |
|---|---|---|---|
| C1 | Gauge/BRST quotient of the RS field | partially -> **BLOCKS** | raw principal gauge symbol only; no `d_RS,-1`, no gauge-fixing/ghost data, no quotient idempotent on a common module |
| C2 | Chiral `E_+` projector | **fully pinned** | `E_+=(I+omega)/2`, rank_H = 32 on `S=H^64`; supplies only a factor-2 chiral halving |
| C3 | Honest K3 index reduction | form pinned, **number open** | `ind_C=(-40+2q)n+(4+q)k`; `q` (ghost count) and `k=ch_2(F)` unfixed |
| C4 | `ch_2(F)` / H-trace curvature | form pinned, **number open** | `c_1(F)=0`, odd Chern chars vanish; numeric `k`, the connection, the coefficient `(4+q)`, and global `Tr_H` all unfixed |

Only C2 is fully determined. C3 and C4 are blocked *downstream* of C1: the ghost
count `q=1-a`, the common module, and the chirality-compatibility of `E_+` with the
physical projector are all set by the same missing object, `RS_GU^phys`. Hence the
**single** load-bearing blocker is C1.

## 2. Assumptions (every one the verdict depends on)

These are stated so the conditional result is auditable. None is asserted as
proven; each is a modeling assumption or a verified fact.

1. **[verified]** `Cl(9,5) = M(64,H) ~ M(128,C)`; `omega^2 = +I`; `E_+` idempotent,
   rank_C = 64 -> rank_H = 32. (Explicit matrix rep, errors 0.0.)
2. **[verified]** Raw 14D gamma-trace map `Gamma^14|_+` is surjective onto `S^-`;
   chiral-positive kernel rank_C = 832 -> rank_H = 416.
3. **[verified]** Cl(4,0) toy with `F=C^16`: `Pi_raw . E_+ . Pi_raw` has rank_C = 96
   (= 48_H naive), and the RS symbol on the projected pure-gauge image has
   norm 73.48 != 0 — i.e. the pure-gauge image is NOT annihilated inside the
   gamma-trace kernel, so the physical space is NOT a subspace subtraction.
4. **[verified]** Atiyah-Singer on closed K3: `Ahat(K3)=2`, `p_1(K3)[K3]=-48`,
   `ch_2(T_C^*K3)[K3]=-48`, virtual class `E(q)=(V+q) tensor F`, so
   `ind_C=(-40+2q)n+(4+q)k`, `n=16`.
5. **[assumption, uncertified]** `rank_H = rank_C/2` and `ind_H = ind_C/2` (needs a
   global right-H trace `Tr_H` certificate; only the fiber dictionary
   `M(64,H) tensor C = M(128,C)` is established).
6. **[assumption, uncertified]** flat background `k = ch_2(F)[K3] = 0` (control only;
   NOT proven for the physical Sp(64)/section-pullback bundle).
7. **[assumption, uncertified]** a ghost-subtraction count `a` (=> `q=1-a`) selecting
   one branch `q in {0,+1,-1}` (the physical value is not source-derived).
8. **[assumption, uncertified]** a same-operator `Y^14 <-> K3` bridge (or APS
   `eta/h/SF/end` data) transporting the physical noncompact index to the compact
   K3 integrand.

## 3. What was computed (target-free)

Code: `tests/oq_rk1_e_rs_eff_assembly.py` (reuses the verified
`oq_rk1_cl95_explicit_rep.py` and `rs_clifford_projector_model.py`). Actual output:

```text
OQ-RK1  E_RS^eff ASSEMBLY ATTEMPT  (four justified components)
==============================================================================
C1 Cl(9,5) anchor : E_+ rank_H = 32.0, raw 14D kernel = 416.0_H
C2 Cl(4,0) toy    : Pi_raw.E_+.Pi_raw = 96_C = 48.0_H ; gauge image NOT annihilated (symbol norm 73.48 != 0)
C3/C4 K3 index    : ind_C=(-40+2q)*16+(4+q)*k ; flat-control k=0 -> q0=-640, q+1=-608, q-1=-672  (ind_H = /2 -> -320.0, -304.0, -336.0)
------------------------------------------------------------------------------
Any computable number equal to 4 or 8?  False
ASSEMBLY STATUS  : BLOCKED_NEEDS_SPEC
decisive rank_H(Pi_RS.E_+.Pi_RS) : NOT_COMPUTABLE
first missing slot : common_right_H_module
  -> M_RS,H^src: the source-selected common right-H module on which Pi_RS^phys, E_+, E_RS^eff all act
all missing slots  : ['common_right_H_module', 'gauge_brst_differential_d_RS_minus_1', 'ghost_subtraction_count_a', 'ch2_F_K3_value_k', 'H_linear_trace_certificate', 'Y14_K3_same_operator_bridge']
4 reachable ONLY via forbidden 8/Ahat(K3)=8/2 (INVALID_TARGET_DIVISION) -> REFUSED
==============================================================================
```

### Computable surrogate table (none is 4 or 8)

| quantity | value | traces to |
|---|---|---|
| `rank_H(E_+)` on `S=H^64` | 32 | C2 [verified] |
| raw 14D gamma-trace kernel | 416_H | C1/C2 [verified] |
| Cl(4,0) `Pi_raw.E_+.Pi_raw` | 96_C = 48_H | C1 [verified] |
| K3 `ind_C`, flat `k=0`, `q=0/+1/-1` | -640 / -608 / -672 | C3/C4 [control] |
| K3 `ind_H` (if `Tr_H`), flat | -320 / -304 / -336 | C3/C4 [conditional] |

The honest integrand yields large **negatives**, not a small effective rank. The
fiber surrogates (32, 416, 48) are the gamma-trace-free / chiral counts, not the
post-gauge-quotient physical rank.

## 4. Why the assembly BLOCKS (the type failure)

`E_RS^eff` must be an H-linear idempotent on a common right-H module
`M_RS,H^src` satisfying `E_RS^eff Pi_RS^phys = Pi_RS^phys E_RS^eff = E_RS^eff`.
The repo supplies `E_+` (pinned) and a RAW gamma-trace projector `Pi_raw`, but
**not** `Pi_RS^phys`, because:

- The pure-gauge image is **not contained in / not annihilated within** the
  gamma-trace kernel (machine fact: RS symbol on it has norm 73.48). So the
  physical space is not `ker(Gamma)/im(gauge)` as a subspace difference; it
  requires a gauge-fixing condition + ghost/antighost complex with signs and
  degrees — all missing.
- With no gauge-fixing/BRST data there is no `d_RS,-1`, hence no `Pi_RS^phys`,
  hence no common module on which `E_+` and `E_RS^eff` co-act. The expression
  `rank_H(Pi_RS . E_+ . Pi_RS)` is therefore **not uniquely typed** (matching
  `cycle2-physical-rs-projector-effective-operator-certificate`,
  `UNDERDEFINED_CERTIFICATE_MISSING`, "first exact obstruction = missing common
  source-selected right-H module").

This is exactly the standing repo frontier object
`RS_GU^phys` flagged `OPEN_MISSING_SYMBOL_DATA`
(`hourly-20260626-0402-cycle1-physical-rs-ktheory-class-gate`).

## 5. Sharpest conditional result

Even granting the **maximally favorable** uncertified assumptions the repo data
permits without fabrication (assumptions 5-8: `Tr_H` valid, flat `k=0`, a fixed
branch `q`, and a same-operator bridge), the computable object is:

- index route: `ind_H in {-320, -304, -336}` for `q in {0,+1,-1}` — **not** 4 or 8;
- fiber route: `48_H` (Cl4 toy) / `416_H` (Cl(9,5) raw) / `32_H` (chiral half) —
  **not** 4 or 8.

The values `4` and `8` are reachable ONLY by either inserting the desired index
`ind_H(D_RS):=8` (target import) or dividing it by the genus,
`rank_eff := 8/Ahat(K3) = 8/2 = 4` (`INVALID_TARGET_DIVISION`). Both are refused.

> **Conditional statement.** Under assumptions {global `Tr_H`; flat `ch_2(F)=0`;
> ghost branch `q`; same-operator K3<->Y^14 bridge}, the honest K3 RS index is
> `ind_H = (-40+2q)*8 in {-320,-304,-336}`, and the fiber rank surrogate is
> `48_H`/`416_H`/`32_H`; **none is 4 or 8**. Without `RS_GU^phys` the decisive
> `rank_H(Pi_RS.E_+.Pi_RS)` is undetermined (the operator does not exist).

## 6. Fabrication self-check (FC4-HOLONOMY-01)

- No matrix was built to hit 4 or 8. Every matrix traces to a justified component
  (`E_+`, raw gamma-trace kernel, Cl(4,0) toy, K3 characteristic-class arithmetic).
- `INVALID_TARGET_DIVISION` (8/2=4) and target index insertion (8) are documented
  and **refused**, never executed.
- The free parameters `q` and `k` are left symbolic, NOT set to whatever recovers 8.
- `ind_H = ind_C/2` flagged conditional (no `Tr_H` certificate), not used to
  manufacture a small number.
- The assembly returns a typed `BLOCKED_NEEDS_SPEC` naming the first missing slot,
  rather than a fabricated quotient idempotent. Building that idempotent to reach a
  target would be the FC4-HOLONOMY-01 error and is refused.

## 7. The exact missing object (what would unblock)

```text
RS_GU^phys = (
  accepted source operator handle (actual D_GU, not screen-only D_roll),
  M_RS,H^src                              # common right-H module
  E_RS^+, E_RS^-, G_+, G_-, P_+, P_-,
  gauge_symbol, gauge_condition OR BRST ghost complex (signs, degrees),
  d_RS,-1                                 # source-defined gauge/BRST differential
  sigma_RS^phys(xi), ellipticity/exactness certificate,
  H_structure_certificate (Tr_H),        # global right-H preserved by connection+operator
  F = s^*S(6,4), ch_2(F)[K3] = k,         # background curvature, currently symbolic
  Y14<->K3 same-operator bridge OR APS eta/h/SF/end terms
)
```

The first field whose absence halts the computation is the **gauge/BRST
differential `d_RS,-1`** (component C1), which simultaneously fails to define the
common module `M_RS,H^src` and the ghost count `q` that C3/C4 need. Supplying
`RS_GU^phys` would make the gate computable; until then the decisive rank is
genuinely undetermined.
