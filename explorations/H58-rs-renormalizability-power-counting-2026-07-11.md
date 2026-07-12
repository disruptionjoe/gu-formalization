---
artifact_type: exploration
status: exploration
created: 2026-07-11
hypothesis: H58
title: "H58 -- FIRMing GU power-counting renormalizability from a structural argument into an EXPLICIT one-loop computation for the Rarita-Schwinger (spin-3/2) sector coupled to 4th-order (Stelle) gravity. VERDICT: CONFIRMED -- D <= 4 on the ker-Gamma subspace; the RS spin-3/2 does NOT spoil power-counting renormalizability. The ker-Gamma spin-3/2 projector is COMPUTED (explicit 4D Dirac matrices) to be momentum-degree 0 AND gamma-traceless, so it removes exactly the spin-1/2 / Velo-Zwanziger modes whose longitudinal insertion carries the dangerous degree +2. Two honest sharpenings: (S1) RS adds its OWN finite closed counterterm set beyond pure Stelle (not literally Stelle's set); (S2) the pass is CONDITIONAL on the exact background-independent degree-0 ker-Gamma projector (the GU program-native fork -- the standard massive-RS constraint-solve is NON-renormalizable). Loop positivity and asymptotic safety are OUT OF SCOPE (H57)."
grade: "exploration / COMPUTED (explicit 4x4 Dirac construction of the massless spin-3/2 projector: momentum-degree 0, gamma-traceless, transverse, residuals ~1e-16; exact integer graph-topology D(L) two ways; exact rational dimensional-identity cross-check; explicit counterterm enumeration) + ARGUED fork-identification (which construction the answer lives in). VERDICT vocabulary: CONFIRMED (power-counting only). No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3} assumed, inserted, hardcoded, or divided by; no generation count is touched (the integer 3 appears ONLY as the transverse-subspace dimension gamma^mu gamma_mu - 1 in the projector algebra)."
depends_on:
  - tests/W44_H58_rs_power_counting.py
  - explorations/wave43/renormalization-carve-2026-07-11.md
  - tests/wave43/renormalization_carve.py
  - explorations/wave42/renormalization-landscape-scan-2026-07-11.md
  - tests/wave42/W42_power_counting.py
scripts:
  - tests/W44_H58_rs_power_counting.py
external_refs:
  - "Stelle, Renormalization of higher-derivative quantum gravity, Phys. Rev. D 16, 953 (1977)"
  - "Velo & Zwanziger, Propagation and quantization of Rarita-Schwinger waves in an external EM potential, Phys. Rev. 186, 1337 (1969)"
  - "Behrends & Fronsdal / van Nieuwenhuizen, massless spin-3/2 projection operators (standard higher-spin propagator numerators)"
  - "Porrati & Rahman, Causal propagation of a charged spin 3/2 field, Phys. Rev. D 80, 025009 (2009)"
---

# H58 -- Is GU power-counting renormalizable? FIRMing the RS spin-3/2 + Stelle-gravity claim

## The claim under test (from Waves 42-43)

Wave 43 (verdict RENORMALIZABLE-BUT-POSITIVITY-OPEN) argued **structurally** that GU is
power-counting renormalizable and the RS spin-3/2 sector does not spoil it: the `ker Gamma` TT
projector is momentum-degree 0, so the superficial degree of divergence stays `D <= 4`, and the
`n=2` danger modes that normally wreck a coupled spin-3/2 theory (Velo-Zwanziger) are exactly the
modes `ker Gamma` removes. H58 FIRMs that structural argument into an **explicit one-loop
power-counting computation** with an explicit primitive-divergence / counterterm enumeration, and
asks whether it CONFIRMS, WEAKENS, or REFUTES.

**H58 is power-counting only.** Loop POSITIVITY of the Krein `[P,S]=0` rescue (the H57-adjacent
open frontier of PT/Krein QFT) and asymptotic safety are OUT OF SCOPE and are neither used nor
decided here.

## The three load-bearing forks (GEOMETER-VS-PHYSICS-OBJECTS.md) and which construction I used

Per the repo discipline, each object with both a standard-field default and a GU program-native
construction is named explicitly, with the construction used and why.

| Fork | Standard-field default | GU program-native | USED HERE + why |
|---|---|---|---|
| **RS propagator** | massive-RS with the 2nd-class constraint **SOLVED** -> `det(Gamma)^-1`, background-dependent vertices | `ker Gamma` **kinematic projector**, `Spin(9,5)`-equivariant, `g=1` full projection, background-INDEPENDENT | **GU program-native.** The answer lives here: the standard constraint-solve is exhibited (Part E) only as the CONTRAST carrying the classic disease. |
| **4th-order graviton propagator** | 2nd-order Einstein `1/p^2` (non-renormalizable) | Stelle 4th-order `1/p^4` (improved UV), the `box(box+m^2)` TT operator (H49) | **GU/Stelle `1/p^4`.** This IS GU's spin-2 sector; the `1/p^2` default would not be renormalizable at all. |
| **unitarity / positivity** | positive Hilbert space | Krein-graded `[P,S]=0` | **NEITHER -- out of scope.** H58 is the counterterm-structure question only; positivity is not touched. |

## What was computed (the firming)

The deterministic test `tests/W44_H58_rs_power_counting.py` (17/17 checks, exit 0) firms the
structural argument in five parts.

### Part B -- the decisive object: the ker-Gamma spin-3/2 projector, from explicit Dirac matrices

The pivot of the whole claim is that the `ker Gamma` spin-3/2 projector is momentum-degree 0.
Wave 43 verified this on the scalar building block `theta.theta`. H58 builds the **full massless
spin-3/2 projector from explicit 4x4 Dirac matrices** (Weyl representation, `{gamma^mu,gamma^nu} =
2 eta^{mu nu}` verified, `gamma^mu gamma_mu = 4`):

```
P^{3/2}_{mu nu} = theta_{mu nu} - (1/3) gt_mu gt_nu,
  theta_{mu nu} = eta_{mu nu} - p_mu p_nu / p^2      (transverse projector),
  gt_mu = gamma_mu - p_mu p_slash / p^2              (transverse gamma).
```

Computed (residuals `~1e-16`):
- **momentum-degree 0**: `P(lambda p) = P(p)` exactly -> the numerator carries **no momentum
  growth** (the load-bearing fact);
- **gamma-traceless**: `gamma^mu P_{mu nu} = 0` -> the projector lands in `ker Gamma`, i.e. it
  **removes exactly the gamma-trace (spin-1/2) modes** -- and those spin-1/2 modes ARE the
  Velo-Zwanziger danger modes;
- **transverse**: `p^mu P_{mu nu} = 0`;
- the **longitudinal / constraint complement** `p_mu p_nu / m^2` (with `m` the fixed `mu_DW` scale)
  is **momentum-degree +2** -- the exact modes `ker Gamma` projects out, and the source of the
  danger.

So numerator degree: **constrained `n = 0`**, **leaked `n = +2`**. The coefficient `1/(D-1) = 1/3`
is the inverse transverse-subspace dimension (`gamma^mu gamma_mu - 1 = 3`), **not** a generation
count -- the sign-blindness / no-count fence is respected.

### Parts A, C -- the superficial degree D(L), two independent ways

Propagator falloffs (momentum degree of the denominator): graviton `1/p^4` (`a=4`), `ker Gamma`
carrier `p_slash * P^{3/2} / p^4 ~ 1/p^3` (`a=3`, numerator `= ` degree-1 `p_slash` x degree-0
`P^{3/2}`), leaked carrier `1/p^1` (`a=1`, numerator degree +2). Ghosts (`1/p^4` diffeo FP,
`1/p^3` gravitino) do not worsen the count.

`D = 4L - sum_i a_i + sum_v d_v` with the topological identity `L = I - V + 1`, and vertices tied
to the action by `d_v = 4 - sum_legs[field]` (`[h]=0`, `[B]=1/2`; the highest operators are the
marginal dim-4 `C^2`, `R^2`, `Bbar D^3 B`):

- **`ker Gamma`-constrained (`n=0`)**: `D <= 4` for **every** swept 1PI graph (1-3 loops, mixed
  `h`/`B` content) -- worst-case `D = 4`. **Power-counting RENORMALIZABLE.**
- **VZ-leaked (`n=+2`)**: `D = D_constrained + 2*I_B` -> grows with the number of internal RS
  lines. **NON-renormalizable.** The `+2` per line is exactly the degree-+2 longitudinal mode.

Independent cross-check via the dimensional identity `D = 4 - sum_ext[field] - sum_v[coupling]`:
all GU couplings have mass-dimension `>= 0` (`[alpha_Weyl]=0`, `[B]`-kinetic `= 0`, RS-graviton /
Yukawa vertices `= +3`), so `D <= 4` for every graph. The two computations agree.

### Part D -- the primitive-divergence / counterterm enumeration (the decisive H58 sub-question)

`D <= 4` means only local operators of dimension `<= 4` are generated. Enumerating them in the
`{h ([h]=0), B ([B]=1/2)}` content:

- **Pure-Stelle gravity set (5):** `Lambda`, `R`, `R^2`, `C^2`, `E_GB`.
- **RS-added set (7):** `Bbar B`, `Bbar D B`, `Bbar D^2 B`, `Bbar D^3 B` (the 4th-order kinetic),
  `(Bbar B)^2`, `Bbar B R`, `Bbar Sigma.R B`.

**Answer to "does RS add a counterterm beyond pure Stelle?": YES -- but benignly.** Relative to
pure Stelle gravity (which has no matter field), the RS sector DOES introduce new counterterms
(the RS-bilinear + curvature-RS operators). Crucially they form a **FINITE, CLOSED** set (every
dim-`<=4` RS/mixed operator; no infinite tower, no operator of loop-growing dimension), all of the
same form as the 4th-order RS action -- which IS the definition of renormalizability. The Wave-43
phrasing "controlled by the same finite set of counterterms [as Stelle]" is therefore **sharpened**:
it is a finite closed set that EXTENDS Stelle's, not Stelle's own set.

### Part E -- adversarial: cure or relocation?

The classic non-renormalizability of spin-3/2 + gravity comes from **solving** the 2nd-class
constraint: `det(Gamma)^-1` enters the vertices, `det(Gamma) -> 0` in a background (Velo-Zwanziger),
the inverse is a non-polynomial background-dependent momentum structure of unbounded degree, and
`D` grows with loops. Modelled two ways:
- **standard constraint-solve** (`n=+2`, `det(Gamma)^-1`): `D = 4 + 2*I_B` grows -> NON-renorm;
- **GU `ker Gamma`** (fixed, `Spin(9,5)`-equivariant, background-INDEPENDENT, degree 0): `D = 4`
  constant -> renorm.

The `ker Gamma` cure **avoids** the disease (does not relocate it) **precisely because** the
projector is the program-native object: exact, background-independent, degree 0, generating **no**
inverse-determinant vertex. This is the load-bearing fork, stated and used explicitly.

## Verdict

**CONFIRMED (power-counting renormalizability).** `D <= 4` for every L-loop 1PI graph on the
`ker Gamma` subspace, by two independent computations; the `ker Gamma` spin-3/2 projector is
COMPUTED (explicit Dirac) to be momentum-degree 0 and gamma-traceless, removing exactly the
spin-1/2 / Velo-Zwanziger modes. The RS spin-3/2 sector does **not** spoil power-counting
renormalizability. Two honest sharpenings:

- **S1 (precision).** RS adds its OWN finite, closed counterterm set beyond pure Stelle -- so the
  precise statement is "a finite closed counterterm set that extends Stelle's", not "the same
  counterterms as Stelle". The renormalizability claim survives; the phrasing is tightened.
- **S2 (conditional).** The pass is conditional on the GU program-native fork: the `ker Gamma`
  projector must be exact, background-INDEPENDENT, degree 0. The standard massive-RS
  constraint-solve is NON-renormalizable (Part E). The answer lives on the program-native side.

## What H58 leaves open (routes to H57 / asymptotic safety)

- **Loop POSITIVITY** of the Krein `[P,S]=0` rescue -- the H26/H57-adjacent open frontier of
  PT/Krein QFT. `D <= 4` says the divergences are absorbable by a finite counterterm basis; it says
  NOTHING about whether the theory is unitary with the ghost at loop level. That is the binding
  obstruction to UV-completeness (Wave 43, Q4), untouched here.
- **Asymptotic safety** as the alternative UV route (a functional-RG fixed point for GU's operator
  content) -- structurally plausible (Wave 42, Survey 4), not built, and independent of power
  counting.
- **Completeness of the GU action.** Renormalizability requires the finite dim-`<=4` RS/mixed
  counterterm basis (Part D) to be present in the action; whether the specific `|II|^2` + ker-Gamma
  RS carrier already contains all of them (or must be extended by finitely many) is a separate,
  benign "is the action complete" question -- it does not affect power-counting renormalizability.

## Honest limits

- The graph-level `D` is the standard superficial-degree estimate (Stelle's own grade), not a full
  BRST-closed all-orders renormalizability proof. The projector degree, the graph topology, the
  dimensional-identity cross-check, and the counterterm enumeration are exact; the "no non-local
  divergences / BRST-closed counterterm structure" leg is not attempted (there is no built source
  action to run it on -- the same gate as Waves 42-43).
- The `4th-order` matter order is a structural input (guardian-wave one-scale-4th-order framing): a
  `2nd-order` (Dirac) spin-3/2 coupled to gravity is the classic VZ / non-renormalizable disaster,
  so the 4th-order structure is load-bearing.
- Part E's two-construction contrast uses the verified closed form `D = 4 + n*I_B` (`n=0`/`+2`),
  corroborated by Part C's exact graph sweep; it is a model of the constraint-solve disease, not a
  computed `det(Gamma)^-1` loop integral.
- No count, no chirality, no forcing. No forbidden target is touched; the integer 3 appears only as
  the transverse-subspace dimension in the projector algebra.

---

*Reproducible: `python tests/W44_H58_rs_power_counting.py` (17/17 PASS, exit 0). Exploration-grade;
not promoted to canon. No git commit (the orchestrator verifies and commits). No canon/verdict file
touched.*
