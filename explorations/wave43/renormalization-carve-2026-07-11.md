---
artifact_type: exploration
status: exploration
created: 2026-07-11
title: "Renormalization carve (Wave 43): is GU's 4th-order RS + Krein structure UV-complete? Power counting PASSES on the consistency-forced ker-Gamma subspace for BOTH sectors (spin-2 Stelle D=4, spin-3/2 RS D=4 with numerator degree 0); loop POSITIVITY is the H26 open problem extended to both sectors. Verdict RENORMALIZABLE-BUT-POSITIVITY-OPEN; the binding obstruction is loop positivity = the source action, not power counting; the RS spin-3/2 does NOT spoil renormalizability because the matter is 4th-order."
grade: "exploration / COMPUTED power-counting (exact integer graph topology reproducing Stelle D=4; exact sympy homogeneity of the spin-3/2 projector; RS commutation residual 0; RS positivity residual 2 delta^2 / 4 delta^2) + ARGUED branch-identification and loop-positivity statements (primary-source-fenced to H26/H40). Verdict vocabulary: RENORMALIZABLE-BUT-POSITIVITY-OPEN. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3} assumed, inserted, hardcoded, or divided by; no count is touched."
depends_on:
  - tests/wave43/renormalization_carve.py
  - tests/wave23/H26_loop_ghost_unitarity.py
  - explorations/wave23/H26-loop-ghost-unitarity-2026-07-11.md
  - tests/wave28/H49_bach_weyl_sector.py
  - tests/wave17/H40_terminal_sourceaction.py
  - tests/wave16/H39_sourceaction_kclass.py
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/wave43/renormalization_carve.py
external_refs:
  - "Stelle, Renormalization of higher-derivative quantum gravity, Phys. Rev. D 16, 953 (1977)"
  - "Velo & Zwanziger, Propagation and quantization of Rarita-Schwinger waves in an external EM potential, Phys. Rev. 186, 1337 (1969)"
  - "Porrati & Rahman, Causal propagation of a charged spin 3/2 field in an external EM background, Phys. Rev. D 80, 025009 (2009)"
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 (2026)"
---

# Wave 43: is GU renormalizable AND ghost-rescued -- i.e. UV-complete?

**The setup.** The guardian wave ruled out SUSY: GU is a one-scale finite-cutoff EFT whose
only route to UV-completeness is RENORMALIZATION plus the Krein ghost rescue. GU's field
content is 4th-order in both sectors: spin-2 gravity is `box(box+m^2)` on TT (Stelle, H49);
matter is a 4th-order Rarita-Schwinger carrier B (index `-38`, gamma-trace-constrained
`ker Gamma`, on the `Cl(9,5)=M(64,H)` Krein space, H39/H40). The ghost is cleared at tree by
`[P,S]=0` (`P` = Cartan involution of `so(9,5)`, Bateman-Turok). H26 left the gravity ghost's
loop status OPEN: `[P,S]=0`'s commutation leg is radiatively stable, but loop POSITIVITY (weak
ghost symmetry `tr(C^dag C)=0`) is IR-broken and needs the unbuilt source-action S-matrix.

**The question.** Is GU RENORMALIZABLE-AND-UNITARY (power-counting renormalizable AND Krein
positivity holds at loop) / RENORMALIZABLE-BUT-POSITIVITY-OPEN (power counting passes but loop
positivity is the H26 open problem, now both sectors) / NON-RENORMALIZABLE (the RS spin-3/2
spoils power counting)?

**One-line answer.** **RENORMALIZABLE-BUT-POSITIVITY-OPEN.** Power counting PASSES for both
sectors on the `ker Gamma` physical subspace (COMPUTED: Stelle `D=4` for spin-2; RS `D=4` with
propagator-numerator degree `n=0` for the constrained spin-3/2). The RS spin-3/2 does **not**
spoil renormalizability -- because the matter is **4th-order**, the propagator is `1/p^4` and
the constrained projector is momentum-degree 0, exactly matching gravity. The single remaining
obstruction to UV-completeness is **loop positivity** -- the H26 weak-ghost-symmetry problem,
now extended to the matter sector -- which is undecidable without a built source action.

---

## The four verdicts

### Q1 -- POWER COUNTING: renormalizable, and the RS spin-3/2 does NOT break it

**COMPUTED.** The superficial degree of divergence in `d=4` for a graph with `L` loops,
internal lines with propagator `~ p^{-a_i}`, and vertices with `d_v` derivatives is
`D = 4L - sum_i a_i + sum_v d_v`.

- **Gravity (spin-2, 4th-order).** Propagator `~ 1/p^4` (`a=4`, the `box(box+m^2)` TT operator
  of H49), vertices `d_v <= 4`. With the graph identity `L = I - V + 1`, `D` collapses to
  `D = -4V + 4 + 4V = 4`, **independent of loop order** (verified on a swept table of graphs,
  `V=1..6`, `L=1..3`, all `D=4`). This is Stelle 1977: power-counting renormalizable.

- **RS matter (spin-3/2, 4th-order) -- the crux.** Write the 4th-order RS propagator as
  `(numerator)/p^4`. The pivot is the **homogeneity degree `n` of the numerator** (the spin-3/2
  projector). Computed exactly (sympy scaling `p -> lambda p`):
  - the transverse projector `theta_{mu nu} = eta_{mu nu} - p_mu p_nu/p^2` is **degree 0**;
  - the massless TT spin-3/2 projector (built entirely from `theta` and constant `gamma`) is
    **degree 0** => `n=0`;
  - the longitudinal / constraint (spin-1/2) insertion `p_mu p_nu/m^2` is **degree +2** -- these
    are exactly the modes `ker Gamma` removes.
  The closed form (verified on swept graphs) is **`D = 4 + n*I_RS`**:
  - `ker Gamma`-constrained carrier B (`n=0`): `D = 4`, fixed -> **RENORMALIZABLE**;
  - unconstrained / VZ-leaked (`n=2`): `D = 4 + 2*I_RS`, grows with loops -> non-renormalizable.

**Verdict: POWER-COUNTING RENORMALIZABLE on the `ker Gamma` physical subspace.** The generic
higher-spin expectation (spin-3/2 spoils power counting) does **not** fire here, because GU's
matter is **4th-order, not 2nd-order**: the extra two derivatives soften the propagator to
`1/p^4`, and on the gamma-traceless subspace the numerator is degree 0, so the RS sector counts
exactly like Stelle gravity. The higher-spin danger `D = 4 + 2*I_RS` is carried by precisely the
longitudinal spin-1/2 modes that `ker Gamma` projects out -- the same modes whose propagation is
the Velo-Zwanziger acausality H40 already flags (`C2 = ||Gamma M_D Pi_RS|| = 155.36 != 0`).

### Q2 -- THE KREIN RESCUE EXTENDED TO MATTER: same status as gravity

**COMMUTATION leg -- COMPUTED, radiatively stable, SAME as gravity.** H26 Part B already lives
on the `Cl(9,5)=M(64,H)` matter Krein space: `P = beta_S` (Cartan involution) is a group element
and every covariant vertex commutes with `P` (residual 0). This carve re-exhibits the protected
leg on a compact RS model (spin-3/2 pair + spin-1/2 constraint pair, ghost parity `kappa`,
Krein-unitary `S`): `||[P,S]|| = 0`, `||S^dag eta S - eta|| = 0`. The matter ghost's commutation
stability is identical to gravity's -- as the canon synthesis records, the Krein form, the
gauge-sector rescue, and the ghost parity are **one `Z2`** at kinematic grade.

**POSITIVITY leg -- OPEN, SAME as gravity, one RS-specific tightening.** The weak-ghost-symmetry
residual `tr(C^dag C)` under an IR regulator `delta` (modelling BT's collinear-IR obstacle):
- `ker Gamma`-ENFORCED: only the physical spin-3/2 pair is active -> `tr(C^dag C) = 2 delta^2`,
  **exactly equal to gravity's residual**;
- LEAKED: both pairs active -> `tr(C^dag C) = 4 delta^2`, **double gravity's** (the constraint
  channel adds to `C`).
Either way `> 0` for `delta > 0` while `[P,S]=0` holds throughout -- the SAME analytic
nullness/IR obstruction as H26 Part C. **Matter's rescue is neither better nor categorically
worse than gravity's: SAME status.** The one RS-specific feature is a tighter gate -- the same
`ker Gamma` cure must simultaneously deliver causality, the `n=0` power-counting softening, AND
reduce the positivity residual to gravity's `2 delta^2` -- but it is the SAME unbuilt term, so a
consistency-forced causal cure plausibly delivers all three at once (Porrati-Rahman: the causal
window and the improved UV behaviour of charged higher-spin are the same non-minimal coupling).

### Q3 -- THE OVERALL VERDICT: RENORMALIZABLE-BUT-POSITIVITY-OPEN

Power counting PASSES for both sectors on the `ker Gamma` subspace (COMPUTED). Loop positivity is
the SAME H26 open problem, now for BOTH the spin-2 and spin-3/2 sectors (COMPUTED commutation
stability; positivity gated on the unbuilt S-matrix). GU is therefore:
- **NOT NON-RENORMALIZABLE** -- the RS spin-3/2 does not spoil power counting (the 4th-order
  structure is load-bearing and does the softening);
- **NOT yet RENORMALIZABLE-AND-UNITARY** -- loop positivity is unproven, exactly as it is unproven
  anywhere for 4-derivative gravity;
- **RENORMALIZABLE-BUT-POSITIVITY-OPEN, gated on the source action.**

### Q4 -- WHICH OBSTRUCTION BINDS: loop positivity, not power counting

**The binding obstruction is loop positivity (the H26 gated-on-source-action problem), NOT power
counting.** Power counting passes conditionally on `ker Gamma`, and `ker Gamma` is **forced by
consistency** (H40: the VZ leakage is a genuine acausality; the cure is demanded, not optional).
Once the consistency-forced causal cure is in, power counting is renormalizable AND causality
holds. The only remaining obstruction to UV-completeness is loop positivity. Stated cleanly:

> **GU's UV-completeness is EXACTLY the source-action loop-positivity question (H26 extended to
> both sectors).** Power counting is not a hard no; it is cleared to a conditional pass on the
> same object that gates positivity.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| gravity `D = 4` independent of `L` (Stelle) | **COMPUTED** | A1, exact integer topology over swept graphs |
| transverse / TT spin-3/2 projector is homogeneity degree 0 (`n=0`) | **COMPUTED** | B1/B2, exact sympy scaling |
| longitudinal `p_mu p_nu/m^2` insertion is degree `+2` | **COMPUTED** | B3, exact sympy scaling |
| `D = 4 + n*I_RS`; `n=0` renorm, `n=2` non-renorm | **COMPUTED** | B4, exact integer topology |
| GU branch = the `ker Gamma` constraint (`n=0` constrained / `n=2` leaked) | **COMPUTED `n`; ARGUED** | B5, identified with H40's VZ leakage `C2=155.36` |
| RS commutation `[P,S]=0` radiatively stable, SAME as gravity | **COMPUTED** | C1, residual 0; H26 Part B on the same `Cl(9,5)` |
| RS positivity residual `2 delta^2` (enforced) / `4 delta^2` (leaked) | **COMPUTED (model)** | C3, swept `delta` |
| loop positivity is the binding, undecidable-without-`S` obstruction | **ARGUED (source-fenced)** | inherits H26; needs built S-matrix |
| matter must be 4th-order for renormalizability (2nd-order = VZ disaster) | **ARGUED** | classic higher-spin power counting |

---

## Honest limits

- **The renormalizability is CONDITIONAL, not unconditional.** Power counting passes only on the
  `ker Gamma` subspace with `n=0`. The built minimal coupling leaks (`C2 != 0`, H40), which is the
  `n=2` non-renormalizable branch. The renormalizable branch requires the SAME unbuilt causal-cure
  term as H40's field-space declaration. The pass is real but gated.
- **`D = 4 + n*I_RS` uses the effective-falloff bookkeeping, not a full GU loop integral.** The
  numerator degree `n` is computed exactly for the projector building blocks; the graph-level `D`
  is the standard superficial-degree estimate. A genuine renormalizability proof (BRST-closed
  counterterm structure, gauge-ghost sector, no non-local divergences) is not attempted -- there is
  no built action to run it on. The claim is power-counting, at the same grade as Stelle's own
  superficial-degree argument, extended to the constrained RS sector.
- **Part C is a model, not GU's loop calculation** (inherited from H26). It demonstrates the
  logical structure (positivity residual `~ delta^2` while `[P,S]=0`, and the RS constraint channel
  doubling it) and the reduction to gravity under `ker Gamma`. It does not compute a GU loop
  integral -- there is none without a built `S`.
- **The 4th-order matter order is an ARGUED structural input.** H40's index symbol `M_D` is
  degree-1 (Dirac-type, appropriate for the index theorem). The renormalizability argument assumes
  the physical RS kinetic operator is genuinely 4th-order (matching Stelle gravity in one action),
  as the guardian-wave one-scale-4th-order framing states. If the matter dynamics were 2nd-order,
  the spin-3/2 would be the classic non-renormalizable VZ case -- so the 4th-order structure is
  load-bearing for the whole verdict.
- **No count, no chirality.** No generation number is asserted; the sign-blindness fence of H23(C)
  is respected. No forbidden target is touched.

---

## RE-RANK signal

**OPEN, UNIFIED (no new kill).**

This carve **removes a candidate hard-no**: power-counting non-renormalizability from the RS
spin-3/2 does **not** fire. The 4th-order kinetic term softens the propagator to `1/p^4`, and the
`ker Gamma`-constrained spin-3/2 projector is momentum-degree 0, so the RS sector counts exactly
like Stelle gravity (`D=4`). The generic higher-spin obstruction is carried entirely by the
longitudinal modes the constraint removes.

It **adds the power-counting leg** to the list of questions that ALL reduce to the one unbuilt
object -- the source-action `ker Gamma` / causal-cure term:
1. field-space declaration (H40),
2. loop positivity (H26),
3. causality / VZ (H40),
4. `mu_DW` / the observable scale (H49/H50),
5. **power-counting renormalizability (this carve)** -- newly cleared to conditional-pass.

**Single next object UNCHANGED:** the soldering-carrier source action `S` (`A = spin-lift(grad^
gimmel)`, `S = |theta|^2`), which now carries FIVE questions. The UV-completeness question is not a
missing calculation on existing machinery -- it is the SAME missing object. Until `S` is built,
GU is **RENORMALIZABLE-BUT-POSITIVITY-OPEN**: power counting passes on the consistency-forced
`ker Gamma` subspace (both sectors), the commutation legs are radiatively stable (both sectors,
residual 0), and the loop-positivity leg is provably undecidable from GU-internal data. The
binding obstruction is loop positivity, and it is exactly the source action.
