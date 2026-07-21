---
title: "Per-leg physics-recovery state: conditional-construction grading (given sigma, tau supplied)"
status: active_research
doc_type: exploration
created: 2026-07-21
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Per-leg physics-recovery state (honest, calibrated)

**Framing (conditional construction).** The question graded here is NOT "does GU
natively derive each sector?" It is: **provided the external orientation bit
`sigma` (the Z/2 that the operator analysis shows GU does not close from
structure) and the generation trit `tau` (Z/3) are supplied and read correctly,
how does each physics sector FIT / recover, and at what grade on the fit
ladder?**

**Fit ladder** (from the exploration contract, `lab/process/construction-space-map.json`):
- **Rung 2 (recovered-native):** structure forced by the construction with no
  sector-specific repair. North-Star bar; grades survivors only.
- **Rung 1 (hosted-with-typed-imports):** accommodates the sector's structures
  with typed AND counted imports.
- **Rung 0 (consistency-only):** not falsified by the sector's frozen sharp
  constraint list; imports permitted but typed. `R0_COND`/`R1_COND` = the same
  conditional on the frozen source-object interface as one typed import.
- **OPEN / BLOCKED / OUT-OF-SCOPE** as labelled.

**Live construction being graded.** `C10-DISTORTION-VACUUM-FIELD` (the (9,5)
distortion field carrying a VEV — Weinstein's vacuum object, transcript-anchored)
is the live candidate; `C11-SIGNATURE-77` is the (7,7) alternative. Round-11
evidence favors (9,5) + an explicit generation integer; the signature verdict
stays Joe-gated. The originally-tested bare `C1-W229` branch **fails** GR and
COSMO at consistency strength (`R0_FAIL`) — the conditional grades below come
from the C10 distortion construction, not the bare branch.

**One honest structural fact up front.** `sigma` is genuinely external:
`OPERATOR-END-PENCIL` resolved LC-SELECTOR — the section's +-i0 orientation does
NOT close from committed structure; "GU is oracle-relative at the operator level;
the oracle is `sigma`." So none of the YES/CONDITIONALLY grades below are
derivations of `sigma`; they are fits **given** it. What is genuinely strong is
that **one supplied bit `sigma` does quadruple duty** — it is simultaneously the
QM Krein sign, the GR vacuum-cancellation sign, the dark-energy sign, and the
record/time arrow (co-flip, audited to be ONE bit). That is the program's
sharpest unification signal, and it is a supplied bit, not a derived one.

---

## Per-leg table

| # | Leg | GRADE | Given sigma, tau supplied — does it fit? | One-line evidence | Honest gap to raise the grade |
|---|-----|-------|------------------------------------------|-------------------|-------------------------------|
| 1 | Quantum physical sector (Krein -> physical Hilbert / superselection) | **Rung 1 (hosted, conditional)** | **CONDITIONALLY YES** — on one typed boundary-adapter import; positive sector appears for the right orientation, wrong orientation fails cohomologically (a real kill test it survives) | CH-QM 9-dim toy passes all six certificates; H3 192-dim triplet lift passes both endings with exact zeros; `C10-QM = R1_COND` | Unconditional `QM-PHYSICAL-SECTOR = COMPLETE_CONDITIONAL_FAIL`: native (unimported) quotient/state/observable/probability/locality/dynamics certificates absent; the L7 Krein superselection + probability rule is source-gapped |
| 2 | Standard Model (gauge group + chiral matter) | **Rung 1 (hosted, 6 typed imports)** | **CONDITIONALLY YES at hosting only** — the SM content is hosted, the *selector* is imported, not derived | All 16 Spin(10)->G_SM chains R0-equivalent (exact SM content per 16, anomalies zero, chirality genuine); hypercharge normalization BOUGHT (sin^2=3/8); `C1-SM = R1`, R2 native selector = BOUNDED_NO_GO | A source-owned target-free selector (breaking chain + Higgs + spectrum + decoupling). `P-54-WELD`: the direct native `theta` (one vertical 10) -> conventional `Sym^2_0(10)=54` weld fails; only a conditional quadratic composite remains |
| 3 | Generations / flavor (three families; the trit `tau`) | **OPEN** (native value present, physicalization imported) | **CONDITIONALLY / NO** — `tau` *is* the supplied datum; the count `3 = dim Lambda^2_+` is native but **not forced**; the physicalization selector is a free import in BOTH (9,5) and (7,7) | `P-RANK-FOLD = DIRECT-FAIL` (Spin(10) chain acts as identity on flavor multiplicity; does not chiralize mirrors or collapse the extra SU(2)-); "located, not forced" (Door A ~3%); **B-FAILS**: no-fourth-generation is NOT a GU falsifier (it conflated an order Z/3-in-Z/24 with a dimension dim su(2)=3 — a quarantined pun) | A physical rank-three family object from the B5 source; what survives today is generation *universality* (identical (+32,-32,0) numbers), not a count-cap. Downstream of B5 (blocked) |
| 4 | General Relativity — vacuum cancellation | **Rung 0 (conditional; leaning theorem)** | **CONDITIONALLY YES for the O(M^2) vacuum cancellation** — on a source-owned VEV branch + one frozen coefficient (kappa^2=1, provenance pending) + a derivable de Donder presentation class | CH-GR exact identity `Q^TF = -[t2]^TF`, hard Z/2 sign gate (wrong sign has no real solution), Kerr-robust; `P-K2` PARTIAL-leaning-theorem; Theorem V master defect law, de Donder discharged to an equation of motion (BRST closure), two-center passes; `C10-GR = R0_COND` | **This is vacuum cancellation, NOT dynamical Einstein recovery** (standard Einstein stays comparator-only). Open: full covariant K2, action-level kappa^2 / de Donder provenance (source-gated), first nonlinear obstruction at O(M^3) |
| 5 | UV gravity / stationary-vacuum survivor | **Rung 0 (compatibility)** | **CONDITIONALLY YES as compatibility** — Schwarzschild/Kerr linear-in-M cheap-reads clear (part of the GR sharp list) | `PAPER-UV-GRAVITY`: W225/W236/W238 make the projected-shadow cheap read structurally clear for the stationary-vacuum Schwarzschild/Kerr class — "strengthens compatibility, not distinctiveness" | Compatibility is not recovery and not a distinctive prediction; no theorem-level novel assembly has cleared the overlap/novelty gate |
| 6a | Dark Energy — the SIGN (`sigma` readout) | **Rung 1-strength conditional prediction (strongest distinctive payoff)** | **CONDITIONALLY YES** — on `sigma` being a global relational orientation observable; co-variance derived at toy/symbol grade | **Prediction Packet 1 FROZEN** (internal): `sgn(w_0+1)>0`, `w(z) >= -1` pointwise; DE sign = readout of the transmitted Z/2; 60/40 exposed to the DESI crossing; `DE-F1-TRIPWIRE` two-sigma margin +1.11 | Operator-grade (not toy) co-variance; confirm global readability; needs official DESI/Euclid holdout (external) |
| 6b | Dark Energy — the AMPLITUDE | **OPEN / imported** | **NO** — no native absolute scale | `PRED-NORM-RANK = RESOLVED_NO_GO` (four invariant quotient families, no GU-native absolute scale); `rho_DE^(1/4) ~ 2.24 meV` (~1e-123 M_Pl^4) is an empirical point; `DE-AMP-DIAGNOSTIC` is data hygiene, not a prediction | A native absolute normalization datum — source-gated; currently freely specifiable |
| 7 | Dark Matter | **OUT-OF-SCOPE** | **UNKNOWN / not claimed** — GU tracks no dark-matter recovery leg | No recovery-leg entry; DM appears only in comparator/intake docs (Mannheim conformal, Verlinde/Bianconi entropic). Nearest candidate (PP2 matter-parity / mirror sector) is `BLOCKED_PRODUCIBILITY` | Not a tracked GU target; the native mirror route is `MIRROR-NATIVE-ROUTE = RESOLVED_NO_GO` for every native order-parameter class |
| 8 | Cosmological perturbations | **Rung 0 (conditional; was NO)** | **CONDITIONALLY** — on the C10 action supplying a closed SVT scalar truncation with dischargeable residues and Z_theta > 0 | CH-COSMO: GU-native projector (fiber Frobenius), automatically helicity-0, exactly one slicing residue, vector/tensor residues discharge by Schur; `C10-COSMO = R0_COND` (bare `C1-COSMO = R0_FAIL`) | Multi-scalar block diagonalization + positive kinetic term (Z_theta > 0) is C10-action-dependent (source-gated); observable transfer map still owed |
| 9 | Source Action / B5 middle-differential (the spine) | **BLOCKED_SOURCE_GAP** | **NO** — this is the object `sigma`, `tau`, and every conditional grade are supplied *into*; the skeleton exists but the native class is not delimited | CH-SRC skeleton exists at toy grade (B.1-B.4 exhibited; C2 law exact = 2.000000; 20 constraints frozen, no computed conflict) but closure needs the B.5 global data; `B5-MIDDLE-SOURCE-GAP` fired 2026-07-21; `OPERATOR-END-PENCIL` = complete-modulo-external-`sigma` | A stronger primary (Weinstein) packet delimiting the complete native first-order class: typed matrix/signs, middle contraction, filtration, domain/boundary, real/Krein closure, super-IG/BV identity. **Load-bearing; p2c/Joe-gated** |
| 10 | Records / arrow of time (CH-REC) — *added; where `sigma`'s co-flip lives* | **Rung 0 (conditional; zero extra payload)** | **CONDITIONALLY YES at zero import** — arrow + Krein sign + GR cancellation sign = ONE transmitted orientation | CH-REC co-flip holds at zero import in the finite inventory; H2 Lean `CoflipCore.lean` sorry-free/axiom-free; H4 BV-grade co-flip survives on descended observables | Decoupling the arrow costs exactly one extra Z/2 (accounting identity); the N->5 escalation route is closed conditional on the D1 canonical-reading condition |

---

## Overall honest summary

Given that the external orientation bit `sigma` and the generation trit `tau`
are supplied and read correctly, GU's live (9,5) distortion-vacuum construction
fits the physics **conditionally, at consistency-to-hosting grade** — QM sits at
hosted-with-one-import (`R1_COND`), the Standard Model at hosted-with-six-imports
(`R1`), and GR vacuum cancellation, cosmological perturbations, records/arrow,
and the SM chain all at consistency-conditional (`R0_COND`). **Nothing reaches
Rung 2 (native selection):** the SM group/Higgs/hypercharge and the generation
physicalization remain typed imports rather than derivations, and even the strong
GR result is a vacuum *cancellation*, not recovery of dynamical Einstein
equations. The one genuinely distinctive, falsifiable payoff of `sigma` is the
frozen dark-energy **sign** prediction (`w(z) >= -1` pointwise); the DE
amplitude, dark matter, and full dynamical GR/QFT recovery are **not** native
(amplitude and scale are imported, dark matter is out of scope).

**The single biggest open sector is the Source Action / B5 middle-differential
(leg 9).** It is genuinely `BLOCKED_SOURCE_GAP`, and it is load-bearing: the GR
kappa^2/de Donder provenance, the QM L7 superselection/probability rule, the SM
selector, the generation family object, and the cosmological closed-truncation
positivity all hang on it. Until an owner-grade primary packet delimits the
complete native first-order class, every conditional grade above stays
conditional and none can be validated to Rung 2. In one line: **most of physics
*fits* given the bit, but GU does not yet *force* any of it given the bit — and
the bit itself is supplied, not derived.**

*Read-only status report. No claim, canon verdict, or public posture moves.*
