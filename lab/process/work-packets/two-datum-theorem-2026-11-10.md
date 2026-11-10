---
title: "Work packet: the two-datum theorem (weld lift to class C + 3-local floor)"
status: ready_for_hourly
doc_type: work_packet
created: "2026-11-10"
authorized_by: "Joe direct chat, 2026-11-10 ('prep it for the hourly')"
program_target: [X-P1-P2, X-D1-P3]
tier: T1
claim_effect: none until the Tier-1 gate passes
---

# Work packet: the two-datum theorem

**Goal.** Prove, at structure level and for every action in class C
(`lab/process/action-class.json`), that the external data GU on the observerse
needs are **exactly two**: one orientation bit `D1` (P1 and P2 welded) and one
count datum `D2 = P3`. No fewer, no more, for additive invariants.

The work splits into two independent parts. Do them as separate runs. Part B is
smaller and goes first.

Before starting either part, read this whole packet, then
`program_focus` in `CURRENT-STATE.yaml`. The rules there (structure, not
specifics; no gate-object building; preflight and postflight) apply.

---

## What is already established (do not redo)

| Fact | Grade | Where |
| --- | --- | --- |
| P1/P2 weld: the DeWitt metric-fibre loop returns the coflip `C_perp = K J_obs` with uniform endpoint mismatch `-1` on all 20 normalized slots; one global orientation phase remains | exact finite associated-bundle grade, **for the written reconstructed first-order coefficient differential only** | `explorations/full20-dewitt-loop-transport-wave-2026-07-30.md`; `tests/channel-swings/full20_dewitt_loop_transport_probe.py` (green, re-run 2026-11-10) |
| `D1` is a Z/2 local system on the metric fibre `F` (holonomy of `pi_1(F) = Z/2`, the orthochronous character), not a number handed in | exact | `explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md` |
| `D1`'s home is time-orientation of `X^4`; all GU objects presuppose it | exact | `explorations/time-orientation-home-for-the-orientation-datum-2026-08-04.md` |
| Every entry of the observer-equivariant first-order symbol matrix `m_ij = dim Hom_H(V_14 (x) W_i, W_j)` is 0 or 1 (Schur multiplicity one); mirror exchange preserves it | exact | `tests/shiab_b5_observer_symbol_multiplicity_matrix.py` |
| Ghost-parity / positive-sector choice cannot select chirality (cross-chirality Krein form; every maximal positive subspace is half left, half right) | exact | `canon/swing-ghost-parity-no-chiral-selection.md` |
| `C_perp` character does not flip between the (3,1) and (1,3) horns | exact | `explorations/mh9-tier1-mechanism-falsified-2026-08-08.md` |
| Curved B5 Green trace symbol is Krein self-adjoint and coflip covariant; the absolute coflip phase cancels | local formal | `explorations/b5-curved-coflip-green-transport-2026-08-20.md` |

**Layer-0 warnings.**

- `Lean/GUFormalization/CoflipCore.lean` names its theorems "P1" and "P2". Those are the CH-REC co-flip statements, **not** ledger rows P1/P2. Do not cite them as the weld.
- `D1` is a Z/2 orientation and `P3` is a count. "Three multiplicity blocks != three generations" and "symbol support != chiral index" stay in force.
- The weld's `-1` is a returned coflip mismatch, not a frame return.

---

## Part B: the 3-local floor (target `X-D1-P3`, run first)

**Statement to prove.** Let `F = GL(4,R)/O(3,1)` be the metric fibre and `D1` the
time-orientation Z/2 local system on it. Every additive invariant of `F` (cohomology, K-theory or
compactly supported K-theory, and so any families-pushforward index built from them) with values in a
`Z_(3)`-module factors through the time-oriented double cover `F~`, on which `D1` is trivial. Hence no
additive invariant carries `D1` into the mod-3 count `P3`: **`D1` and `P3` are independent, and the
ledger cannot drop below two.**

**Accepted tools.** Mostow/Cartan retraction (`F ~ O(4)/(O(3) x O(1)) = RP^3`); transfer for a double
cover (`p_* p^* = 2`, invertible mod 3); cellular homology of `RP^3`; 3-local Thom isomorphism for an
orientable bundle; `Hom(Z/2, Z/3) = Ext(Z/2, Z/3) = 0`.

**Inputs already certified (2026-11-10).** `tests/program-focus/x_d1_p3_three_local_floor_probe.py`
(12 exact checks, 2 negative controls firing):

1. every Lorentzian metric has exactly one negative direction (the `RP^3` retraction);
2. `H_*(RP^3; F_3) = H_*(S^3; F_3)`, and the orientation-twisted `F_3` homology vanishes;
3. the antipodal map of `S^3` has degree `+1`, so the deck Z/2 acts trivially mod 3;
4. the normal bundle `Sym^2(R^3) + R` is orientable (`det Sym^2 g = det(g)^4 = 1`, and `O(1)` acts
   trivially on the time-time line);
5. `Hom(Z/2, Z/3) = 0`, with `Z/4` as the firing control.

**Steps.**

1. Write the lemma and proof (about a page) in
   `explorations/conditional-build/x-d1-p3-three-local-floor-2026-MM-DD.md` with the required
   frontmatter (`program_target: X-D1-P3`, `tier: T1`, `expected_delta`, `actual_delta`).
2. State the scope exactly: **additive** invariants only. A non-additive dependence of the count on the
   orientation (for example a sign-dependent choice of boundary condition) is **not** excluded. Name it as
   the residual.
3. Check the one non-trivial seam: the families pushforward over `F` uses compactly supported K-theory of
   a rank-7 bundle over `RP^3`. Confirm that its 3-localization is `K^{*-7}(RP^3) (x) Z_(3)` (Thom) and
   equals the `S^3` value (transfer).
4. Lean: add `Lean/GUFormalization/ThreeLocalFloor.lean` proving at least
   `theorem zmod2_to_zmod3_addHom_trivial (f : ZMod 2 →+ ZMod 3) : f = 0` and
   `theorem two_isUnit_zmod3 : IsUnit (2 : ZMod 3)`. Leave the topological transfer as a cited lemma.
5. Tier-1 review: two specialists (algebraic topology; index theory) and one hostile reviewer told to
   attack the additivity scope and the Thom/transfer seam.
6. Postflight: set `X-D1-P3` to `decided_for_C` (if Lean and review pass) or `constrained` (if not), and
   append to the shrinkage log.

**Preregistered outcomes.**

- **(a) Floor holds for additive invariants:** `X-D1-P3 -> decided_for_C`; ledger floor = 2.
- **(b) Seam fails:** the compactly supported pushforward picks up 3-torsion from somewhere the probe
  did not model. Record the counterexample; `X-D1-P3` stays open with the exact obstruction.
- **(c) Scope collapse:** the only additive invariants are trivially independent, so the statement has no
  content. Record as `constrained` with that note and move on.

**Kill condition.** A concrete additive `Z_(3)`-valued invariant of `F` that distinguishes the two
time-orientations.

**Budget.** 2 runs. If not closed in 2, reroute per `program_focus`.

---

## Part A: lift the weld to every action in class C (target `X-P1-P2`)

**Statement to prove.** For every action in class C whose first-order fermionic principal symbol is
observer-covariant (`H = Spin(4) x Spin(10)` equivariant, as class C requires), the P1/P2 weld holds:
P1 and P2 are one orientation datum. The only exception is a structurally described degenerate subfamily
whose nonzero-cell graph is disconnected.

**Why it should hold (structure, not specifics).**

1. Multiplicity one: each nonzero cell of the symbol matrix carries a one-dimensional space of
   equivariant maps (Schur). So any covariant principal symbol is one scalar per nonzero cell. There is
   nothing else to choose.
2. The coflip and the loop transport act cell by cell through representation data. The July result's
   `-1` is computed from the carrier and `C_perp`, not from the coefficient values.
3. Relative mirror-pair phases can survive only if the cell graph splits. Type-level check
   (2026-11-10): 12 types and 20 cells, **connected**, **no bridge cell** (no single vanishing coefficient
   disconnects it), cycle rank 9. The slot-level check (20 slots, 136 cells) is step 2 below.
4. Formal-adjoint sign: for a real action, the linearized Euler–Lagrange operator is formally self-adjoint
   with respect to the pairing that defines the action (the Helmholtz conditions). If that pairing is the
   Krein pairing `K` used by the weld, the "one global formal-adjoint sign" is fixed by reality of the
   action for all of class C.

**Steps.**

1. Read the probe `tests/channel-swings/full20_dewitt_loop_transport_probe.py` and mark exactly where the
   written coefficients enter. Confirm that the `-1` return does not depend on their values, only on which
   are nonzero.
2. Slot level: from `shiab_b5_observer_symbol_multiplicity_matrix.py`, build the 20-slot / 136-cell graph
   and compute connectivity, bridges and cycle rank. Derive the exact degenerate subfamily (the coefficient
   patterns that disconnect the mirror pairs).
3. Generalize the probe: replace the written coefficients with symbolic or random nonzero values on every
   cell (several seeds) and with planted degenerate patterns. Uniform `-1` must survive the generic cases,
   and the planted disconnections must leave the predicted number of free relative phases.
4. Helmholtz seam: show which pairing the weld's formal adjoint uses, and whether it is the action
   pairing. If it is not, the sign stays a named residual. Do not pick it by convenience.
5. Write up in `explorations/conditional-build/x-p1-p2-class-c-lift-2026-MM-DD.md` with the required
   frontmatter.
6. Lean: add a graph lemma, for example "a `ℤˣ`-valued function equal across every edge of a connected
   `SimpleGraph` is constant". It formalizes the propagation step; the representation theory stays cited.
7. Tier-1 review: two specialists (representation theory; Clifford/RS symbol calculus) and one hostile
   reviewer told to attack step 1 (hidden dependence on coefficient values) and step 4 (pairing identity).

**Preregistered outcomes.**

- **(a) Lift holds:** `X-P1-P2 -> decided_for_C` except the stated degenerate subfamily, which is recorded
  as a structural exclusion in the cell.
- **(b) Coefficient dependence:** the `-1` depends on coefficient values. Record the dependence; the weld
  stays at its July grade, and `X-P1-P2` stays `constrained`.
- **(c) Pairing mismatch:** the Helmholtz pairing differs from the weld's. The sign is a named residual,
  and the ledger reads "two data plus one sign convention".

**Kill condition.** A generic (all cells nonzero) covariant symbol for which the loop return is not uniform.

**Budget.** 3 runs. If not closed in 3, reroute.

---

## Forbidden in this packet

- writing down or fitting a specific action, Lagrangian or coefficient set as the answer (random or
  symbolic coefficients used to test genericity are allowed; they are not candidates);
- building the source action, a closed domain or a BV completion to "unblock" the lift;
- reading the CoflipCore "P1/P2" theorems as the ledger weld;
- calling the outcome "GU derives chirality" or "GU explains three". The result is about how many external
  data there are, not their values.

## What success means

"GU on the observerse needs exactly one orientation bit and one integer from outside, for every action in
class C (additive invariants)." It is scoped, structural and built from accepted tools, and it is the first
`decided_for_C` result the matrix can produce.
