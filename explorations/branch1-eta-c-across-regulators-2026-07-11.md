---
artifact_type: exploration
status: exploration (Branch 1 / Front B "the dissolver"; STAGE 2 of the full-FRG horn computation; 5-persona inline team; deterministic test)
created: 2026-07-13
hypothesis: "Compute eta_C -- the shared-Z_h off-diagonal Einstein-Hilbert x Weyl spin-2 TT trace in the FRG (the additive f_2^2 term of beta_{f_2^2}) -- across at least TWO regulator families and settle its SIGN. eta_C>0 robust -> f_2^2*>0 lifted -> HORN Q (ghost removable, quasi-Hermitian, the type-III Krein-TT frontier DISSOLVES); eta_C<=0 -> f_2^2*=0 -> HORN K (genuine non-definitizable ghost, frontier REAL). The sign is the whole result."
branch: "W89 -- Stage 2 decider handed off by W88. Reuses W88's truncation (polynomial f(R) to R^2 + Weyl^2 + ker-Gamma spin-3/2; sphere/dS; York/TT), the ker-Gamma spin-3/2 a_2 coefficients, and the beta_{f_2^2} = -kappa f_2^4 (b_2^grav+b_2^RS) + eta_C(g,lambda) f_2^2 structure (f_2^2*=0 a structural root at every regulator; lift iff eta_C>0). Computes eta_C at the W83/W88 Reuter FP (g*=0.674, lambda*=0.151) for regulator family 2 (exponential r=y/(e^y-1)) and family 3 (exponential shape sweep r_s=s*y/(e^y-1)) alongside family 1 (Litim), by direct off-diagonal FRG trace (D1) cross-checked against the graviton anomalous-dimension identity eta_C=-eta_h (D2). Reads off the sign and the horn."
title: "eta_C is Z_h-SCHEME-dependent, NOT regulator-family-dependent: within a scheme its sign is robust across Litim/exponential/shape (the off-diagonal C^2 threshold integral Phi^2_2(0) is positive-definite for every admissible regulator), but ACROSS the two physical schemes for the shared graviton wave-function renormalization Z_h it is + vs 0. EH-ADAPTED (Z_h=Z_N, eta_h=eta_N*=-2 at the Reuter FP): eta_C = -eta_N* c_reg = +2 c_reg > 0 for ALL three regulators -> a lifted root f_2^2* = eta_C/(kappa b_2) in [0.07, 0.16] > 0 -> HORN Q. WEYL-ADAPTED (Z_h=1/f_2^2, eta_h=eta_Weyl*=0 at the marginally-irrelevant Weyl direction): eta_C = 0 for ALL three regulators -> only the structural root f_2^2*=0 -> HORN K. The two derivations AGREE (direct off-diagonal trace = anomalous-dimension identity) in every regulator family. So the three-regulator test the brief requested demonstrates sign-robustness WITHIN a scheme but does NOT settle the horn -- the Z_h-SCHEME does. VERDICT: REGULATOR/SCHEME-DEPENDENT. Honest lean HORN K (frontier REAL), TRUNCATION-CONDITIONAL: the graviton is ONE field with ONE physical Z_h, its leading UV kinetic term is the 4th-order Weyl term, so the physical eta_h -> eta_Weyl -> 0 => eta_C=0; the EH-adapted eta_C>0 is plausibly a regulator artifact of mis-adapting a 2nd-order cutoff to a 4th-order propagator (double-counting the graviton normalization), consistent with robust one-loop AF (Fradkin-Tseytlin) and W88's leading-diagonal eta_C=0. The frontier is NOT dissolved. Deciding higher truncation named: the full off-diagonal EH x Weyl TT Hessian with a single self-consistent graviton Z_h whose anomalous dimension is computed from the LEADING (4th-order) kinetic term -- equivalently the BMS essential-scheme Weyl-coupling FP value for GU's exact ker-Gamma content."
grade: "COMPUTED / analysis, exploration-grade, STAGE 2 of 2. HIGH confidence on the STRUCTURAL readouts: (1) the off-diagonal C^2 threshold integral Phi^2_2(0) is positive-definite for all three regulator families (Litim closed-form 1/2; exponential 1.0; shape sweep 0.69-1.12, all by quadrature) -> the SIGN of eta_C is carried by -eta_h (the scheme), never by the regulator family; (2) WITHIN the EH-adapted scheme eta_C>0 robustly across all three families (sign regulator-family-invariant, magnitude moves O(1)); (3) WITHIN the Weyl-adapted scheme eta_C=0 across all three families; (4) the two derivations agree; (5) f_2^2*=0 remains a structural root in every scheme+regulator (W88 carried forward). MEDIUM on the SCHEME split being the true un-settled fork and on the HORN-K lean: eta_h=eta_N* (EH-adapted) vs eta_h=eta_Weyl* (Weyl-adapted) is a genuine truncation choice; the lean to Weyl-adapted (leading 4th-order kinetic term sets the physical graviton normalization) is a physical argument, not a theorem. The Reuter-FP eta_N*=-2 is exact/canonical (a scaling statement, regulator-independent). PORTED (cited): pure-gravity Weyl one-loop 133/10 (Fradkin-Tseytlin/Avramidi-Barvinsky); the Reuter-FP location + eta_N*=-2 (Reuter; Codello-Percacci-Rahmede); the two-sided literature on the Weyl FP value (one-loop/some-gauge AF f_2^2*=0 vs Newton-induced nontrivial four-derivative FPs -- Codello-Percacci; Benedetti-Machado-Saueressig; the O(1) c_reg normalization (schematic, sign load-bearing). Deterministic test tests/W89_eta_c_across_regulators.py, exit 0. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon/RESEARCH-STATUS/claim-status/verdict/posture changed. H59/H61a remain OPEN. NOT committed by this run."
depends_on:
  - explorations/full-frg-fr-weyl-rs-stage1-2026-07-11.md
  - explorations/second-regulator-reuter-fp-2026-07-11.md
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/horn-k-vs-q-gu-ghost-2026-07-11.md
  - tests/W88_full_frg_stage1.py
  - tests/W85_second_regulator_reuter.py
  - tests/W86_regulator_shape_sweep.py
  - tests/W83_frg_fr_weyl_af_as.py
  - tests/W87_horn_k_vs_q.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W89_eta_c_across_regulators.py
external_refs:
  - "Reuter, Nonperturbative evolution equation for quantum gravity, PRD57 (1998) 971, hep-th/9605030 -- the Reuter fixed point; eta_N=-2 at the FP"
  - "Codello, Percacci & Rahmede, Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- f(R) FRG, EH fixed point, robustness"
  - "Codello & Percacci, Fixed points of higher-derivative gravity, PRL97 (2006) 221301, hep-th/0607128 -- HD gravity FRG; Weyl coupling asymptotically free; nontrivial Newton coupling induces additional four-derivative fixed points"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- HD Reuter FP; and Four-derivative interactions in asymptotically safe gravity, arXiv:0909.3265; Taming perturbative divergences, NPB824 (2010)"
  - "Reuter & Saueressig, Quantum Einstein Gravity, New J. Phys. 14 (2012) 055022, arXiv:1202.2274 -- regulator robustness; threshold functions Phi^p_n"
  - "Fradkin & Tseytlin, Renormalizable asymptotically free quantum theory of gravity, NPB201 (1982) 469; Avramidi & Barvinsky, PLB159 (1985) 269 -- one-loop AF of the Weyl (C^2) coupling, 133/10"
  - "Salvio & Strumia, Agravity, arXiv:1403.4226 -- AF Weyl coupling f_2^2 -> 0; ghost mass m2^2 ~ f_2^2"
  - "Percacci, An Introduction to Covariant Quantum Gravity and Asymptotic Safety (2017) -- FRG threshold functions Phi^p_n(0)=1/n! (Litim), type-Ia/type-II regulator adaptation"
---

# W89 -- Branch 1 / Front B (the dissolver): eta_C across regulators, and its SIGN

**Role in the flow.** This is **Stage 2** of the full-FRG horn computation W88 handed off. W88 reduced the
entire type-III Krein-TT horn question to a single number, `eta_C`, the additive `f_2^2` term of

```
beta_{f_2^2} = - kappa f_2^4 ( b_2^grav + b_2^RS )  +  eta_C(g, lambda) f_2^2 ,
```

with `f_2^2* = 0` a **structural root at every regulator** (both terms vanish there) and a **lifted
HORN-Q root** `f_2^2* = eta_C / (kappa b_2)` that exists iff `eta_C > 0`. So the whole fork reduces to
`sign(eta_C(g*, lambda*))` at the Reuter FP. W88 computed the **leading diagonal EH dressing** and got
`eta_C = 0`, and named the **only** remaining lifter -- a **shared graviton wave-function renormalization
`Z_h`** generating the **off-diagonal EH x Weyl TT trace** -- as the Stage-2 deliverable. **This file
computes that `eta_C`, for three regulator families, and reads the sign.**

**Deliverables:** this file + deterministic `tests/W89_eta_c_across_regulators.py` (17/17, numpy-only,
exit 0). **Not committed. Not a claim-status/verdict change.** Exploration-grade.

---

## 0. Construction fork (GEOMETER-VS-PHYSICS-OBJECTS discipline, stated up front)

The load-bearing fork here is **not** geometer-vs-physics; it is a **within-physics regulator/scheme
fork** that the geometer-discipline rule (identify, name, do not default silently) forces us to surface:

| Object | Construction A | Construction B | Determined side |
|---|---|---|---|
| **The shared graviton `Z_h` that dresses `C^2`** | **EH-adapted** (`Z_h = Z_N`, the 2nd-order Newton normalization; "type Ia" spectrally-adjusted regulator): `eta_h = eta_N* = -2` at the Reuter FP | **Weyl-adapted** (`Z_h = 1/f_2^2`, the LEADING 4th-order kinetic-term normalization; "type II"): `eta_h = eta_Weyl* -> 0` at `f_2^2* = 0` | **NOT settled by the regulator family.** Leaned Weyl-adapted (B is physical: the graviton's leading UV kinetic term is 4th-order) -> `eta_C = 0` -> HORN K, TRUNCATION-CONDITIONAL. |

The gravity functional and the RS carrier forks are inherited from W83/W88 (induced `|II|^2` -> `f(R)+Weyl^2`;
ker-Gamma transverse gamma-traceless spin-3/2), reused verbatim, not re-defaulted.

---

## 1. `eta_C` written explicitly as the FRG trace it is (specialist)

In the spin-2 TT block the graviton inverse propagator carries **both** kinetic terms:

```
Gamma^(2)_TT(z) = (1/f_2^2) P_4(z)  +  Z_N P_2(z)  + (mass/cc) ,     z = -Box ,
```

- `(1/f_2^2) P_4(z) ~ (1/f_2^2) z^2` -- the **Weyl** (4th-derivative) operator carrying the coupling
  `1/f_2^2` (hence the ghost). Its `z^2` coefficient **is** the `C^2` coupling.
- `Z_N P_2(z) ~ Z_N z` -- the **Einstein-Hilbert** (2nd-derivative) operator carrying the Newton
  normalization `Z_N = 1/(16 pi G) ~ k^2 g^{-1}`.

`eta_C` is the coefficient of the **additive `f_2^2` term** in `beta_{f_2^2}`. Equivalently, up to a
normalization, `eta_C = -eta_h^{(C)}`, the **anomalous dimension of the graviton wave-function
renormalization `Z_h` that dresses the `C^2` operator's coefficient `1/f_2^2`** through the **shared
regulator** `R_k = Z_h * (shape)`. It is the piece of the Wetterich trace

```
partial_t Gamma_k = (1/2) STr[ (Gamma_k^(2) + R_k)^{-1} partial_t R_k ]
```

in which `partial_t R_k` carries the anomalous dimension, `partial_t R_k ⊃ -eta_h Z_h (shape)`,
**projected onto the `z^2` (= `C^2`) heat-kernel coefficient**:

```
eta_C * f_2^2  =  [ z^2-projection of  (1/2) STr( (Gamma^(2)+R_k)^{-1} ( -eta_h Z_h * shape ) ) ] .
```

**Why the diagonal EH mixing does NOT give it (W88, recovered).** The EH term `Z_N P_2` is suppressed
relative to `(1/f_2^2) P_4` by the ratio `rho ~ Z_N f_2^2 / k^2`. A `partial_t R_k` insertion that hits
only the EH part contributes `~ eta_N rho / f_2^2 ~ eta_N Z_N f_2^2/k^2`, i.e. a term `∝ f_2^6` in
`beta_{f_2^2}` -- **not** the additive `f_2^2`. So the diagonal EH dressing gives `eta_C = 0`. This is
exactly W88's Part-C readout, reproduced.

**Why the SHARED `Z_h` is the only source of an independent `eta_C`.** If the **regulator prefactor**
`Z_h` carries the graviton anomalous dimension `eta_h`, then `-eta_h Z_h (shape)` dresses the **whole**
inverse propagator -- **including the leading `(1/f_2^2) P_4` Weyl term**. Its `z^2` projection is
`~ eta_h * (1/f_2^2)`, which converts (via `beta_{f_2^2} = -f_2^4 partial_t(1/f_2^2)`) into the additive
`-eta_h f_2^2`. **So `eta_C = -eta_h * c_reg`**, with `c_reg` the positive `z^2`-projected threshold
integral. Everything now rides on **`eta_h`** and on **`sign(c_reg)`**.

---

## 2. The three regulator families and `c_reg > 0` (D1, direct trace, by quadrature)

`c_reg` is the `z^2`-(`C^2`-)projected threshold integral of the off-diagonal EH x Weyl trace. In the
standard FRG threshold-function formalism the `C^2` coefficient is governed by `Phi^2_2(0)`
(Reuter-Saueressig; Percacci),

```
Phi^p_n(0) = 1/Gamma(n) INT_0^inf dy y^{n-1} [ r(y) - y r'(y) ] / [ y + r(y) ]^p ,
```

a **strictly positive** quantity for every admissible (positive, monotone) regulator. Computed
(`W89` Part A):

| Regulator family | `Phi^2_2(0)` | `c_reg = A_norm kappa Phi^2_2(0)` |
|---|---:|---:|
| 1. Litim/optimized `r=(1-y)th(1-y)` (closed form `1/n!`) | `0.5000` | `3.17e-3` |
| 2. Exponential `r=y/(e^y-1)` (quadrature) | `1.0000` | `6.33e-3` |
| 3. Exp shape sweep `r_s=s y/(e^y-1)`, `s in [0.5,1.25]` (quadrature) | `0.69 - 1.12` | `4.39e-3 - 7.07e-3` |

**`Phi^2_2(0) > 0` for all three families**, and it **moves by O(1)** between them. So `c_reg` (the
**magnitude** of `eta_C`) is regulator-family-dependent, but **its positivity -- hence the sign of
`eta_C` -- is not carried by the regulator family.** The sign is carried entirely by `-eta_h`.

---

## 3. `eta_C` per regulator, per scheme (D1 x D2), and the horn readout

`eta_C = -eta_h * c_reg`. There are **two physical schemes** for the shared `Z_h`, and they are the
un-settled fork:

**EH-adapted (`Z_h = Z_N`).** `eta_h = eta_N* = -2` at the Reuter FP (this value is **exact/canonical**:
for the dimensionless `g = G k^2` to sit at a non-Gaussian FP in `d=4`, `Z_N ~ k^2`, so the anomalous part
is fixed at `eta_N* = 2-d = -2` -- a scaling statement, **regulator-independent**). Then

```
eta_C^{EH} = -eta_N* c_reg = +2 c_reg > 0     for ALL THREE regulator families,
```

giving a **lifted root** `f_2^2* = eta_C/(kappa b_2)` (with `b_2 = 133/10 + 0.70 = 14.0`):

| Regulator | `eta_C^{EH}` | `f_2^2*` (lift) | Horn |
|---|---:|---:|:--:|
| Litim | `+6.33e-3` | `0.071` | **Q** |
| Exponential | `+1.27e-2` | `0.143` | **Q** |
| Shape sweep | `+8.8e-3 .. +1.4e-2` | `0.099 .. 0.159` | **Q** |

**Weyl-adapted (`Z_h = 1/f_2^2`).** `eta_h = eta_Weyl* = partial_t ln f_2^2 = beta_{f_2^2}/f_2^2 -> 0`
at the marginally-irrelevant Weyl direction (`f_2^2* = 0`, W83 eigenvalue `-0.0`). Then

```
eta_C^{Weyl} = 0     for ALL THREE regulator families   ->   only f_2^2* = 0   ->   HORN K.
```

**D2 (anomalous-dimension identity) agrees with D1.** `eta_C = -eta_h` up to the positive normalization
`c_reg`; the direct off-diagonal trace (D1) and the identity (D2) give the **same sign structure and the
same scheme-split in every regulator family** (`W89` B3).

**The readout.**
- **Within** the EH-adapted scheme: **HORN Q for every regulator family** (sign regulator-family-robust;
  only the magnitude moves).
- **Within** the Weyl-adapted scheme: **HORN K for every regulator family**.
- **Across** the two schemes: `sign(eta_C)` is `+` vs `0`. **The Z_h-SCHEME decides the horn, not the
  regulator family.**

**This is the honest core finding.** The three-regulator test the brief requested demonstrates
sign-robustness *within* a scheme, but it **does not settle the horn** -- the deciding datum is the
scheme choice of `Z_h`, a truncation-level question the regulator family cannot reach.

---

## 4. Adversary + referee (persona passes)

**Referee (computed vs ported).** COMPUTED here: the three `Phi^2_2(0)` (Litim closed form + exponential
+ shape sweep, by quadrature); `c_reg > 0` for all three; `eta_C = -eta_h c_reg` per scheme per
regulator; the horn readout; the D1=D2 agreement; the branched verdict. PORTED (cited): `133/10`;
`eta_N* = -2` (canonical Reuter-FP scaling); the two-sided Weyl-FP literature; the O(1) `c_reg`
normalization (schematic, sign load-bearing). **Grade: the load-bearing readout -- `sign(eta_C)` is
Z_h-scheme-set and regulator-family-robust-within-scheme -- is the one robust to the schematic
magnitudes.**

**Adversary press 1: "`eta_C` is scheme-dependent."** **Conceded -- and it is the finding, sharpened.**
It is **not** regulator-family-dependent: `c_reg > 0` for Litim, exponential, and the shape sweep, so
within any fixed `Z_h`-scheme the sign of `eta_C` is identical across all three families. What it depends
on is the **`Z_h`-scheme** (EH-adapted `eta_N* = -2` vs Weyl-adapted `eta_Weyl* = 0`) -- a truncation
choice, not a regulator convention. Naming the axis correctly is the deliverable.

**Adversary press 2: "you missed a graviton-tadpole contribution."** The one-graviton tadpole (from the
cubic vertex closing on the `C^2` insertion) is real, but on the maximally-symmetric background it feeds
the `a_0`/`a_1` heat-kernel coefficients -- the **cosmological and Einstein** terms -- not the `a_2`
(`C^2`) coefficient at the order that would change `eta_C`'s sign; and it is `∝ f_2^4` (a `b_2`-type
running), not the `eta_h * (1/f_2^2)` **dressing** structure that defines `eta_C`. So it does not alter
the scheme-split. (A full curved-background tadpole with the `C^2`-projection is part of the named
deciding truncation.)

**Adversary press 3 (for HORN Q, the dissolver's own steelman): "the EH-adapted `eta_C > 0` is real --
robust across all three regulators -- so the frontier dissolves."** **Answered but not dismissed.** The
positivity is genuine *within* the EH-adapted scheme. The reason it does not dissolve the frontier: the
graviton is **one** field with **one** physical wave-function renormalization, and in the UV its kinetic
term is **dominated by the leading 4th-order (Weyl) term**, so the physical `Z_h` is `1/f_2^2` and the
physical `eta_h -> eta_Weyl -> 0`. The EH-adapted `eta_C > 0` is plausibly a **regulator artifact** of
mis-adapting a 2nd-order cutoff to a propagator whose leading term is 4th-order -- **double-counting** the
graviton normalization. This is supported by the robust one-loop AF result (Fradkin-Tseytlin;
Avramidi-Barvinsky) and by W88's leading-diagonal `eta_C = 0`. The lean is physical, not a theorem, so it
is **truncation-conditional** -- HORN K stands as the honest reading, not an unconditional kill of HORN Q.

**Cross-checker (second derivation + literature).** D2 (the `eta_C = -eta_h` identity) is independent of
D1 (the direct trace) and gives the same scheme-split. Literature (read-only) is **genuinely two-sided**
and maps exactly onto the two schemes: one-loop / certain gauge+regulator choices give the Weyl coupling
**asymptotically free** (`f_2^2* = 0`, the Weyl-adapted side -- Fradkin-Tseytlin; agravity; the CPR/BMS
marginally-irrelevant `C^2` direction), while **"a nontrivial Newton coupling induces additional
nontrivial four-derivative fixed points"** (the EH-adapted side, a lift) is reported in the higher-
derivative FRG literature (Codello-Percacci; BMS). **The literature does not settle the sign either** --
it corroborates that the split is real, not an artifact of our modeling.

---

## 5. Synthesizer -- the verdict

**`eta_C` per regulator + its sign + regulator-dependence.**
- Regulator 1 (Litim): `c_reg = 3.17e-3`; `eta_C^{EH} = +6.33e-3` (HORN Q lift), `eta_C^{Weyl} = 0` (HORN K).
- Regulator 2 (exponential): `c_reg = 6.33e-3`; `eta_C^{EH} = +1.27e-2` (HORN Q lift), `eta_C^{Weyl} = 0` (HORN K).
- Regulator 3 (exp shape sweep): `c_reg in [4.39e-3, 7.07e-3]`; `eta_C^{EH} > 0` all shapes (HORN Q lift),
  `eta_C^{Weyl} = 0` (HORN K).
- **Regulator-dependence:** the **sign** of `eta_C` is **regulator-family-INVARIANT within a scheme**
  (`c_reg > 0` for all three families) and **SCHEME-dependent across the two `Z_h` schemes** (`+` vs `0`).

**VERDICT: REGULATOR/SCHEME-DEPENDENT.** `sign(eta_C)` is fixed by the `Z_h`-scheme (EH-adapted ->
`eta_C > 0` -> HORN Q lift; Weyl-adapted -> `eta_C = 0` -> HORN K), **NOT** by the regulator family. The
requested two-/three-regulator test shows sign-robustness *within* a scheme but does not settle the horn.

**Honest lean: HORN K (frontier REAL), TRUNCATION-CONDITIONAL.** The graviton's one physical `Z_h` is set
by its leading UV (4th-order Weyl) kinetic term, so the physical `eta_h -> 0` and `eta_C = 0`; the
EH-adapted `eta_C > 0` is plausibly a regulator artifact. Consistent with robust one-loop AF and W88's
leading-diagonal `eta_C = 0`. **The type-III Krein-TT frontier is NOT dissolved.** This inherits W87/W88's
consequence unchanged (HORN K keeps the observer firewall genuine and does not hand GU the cheap
ghost-free upgrade) -- stated as inherited context, not re-litigated, and **not** a verdict change.

**Deciding higher truncation (named).** The full **off-diagonal EH x Weyl TT Hessian with a SINGLE
self-consistent graviton wave-function renormalization `Z_h`**, whose anomalous dimension `eta_h` is
computed from the **leading (4th-order) kinetic term** rather than assumed EH- or Weyl-adapted;
equivalently, the **BMS essential-scheme Weyl-coupling FP value for GU's exact ker-Gamma
`(N_S, N_D, N_V, N_RS)` content**. That -- not another regulator family -- is what flips or confirms the
horn. A `C^2`-projected curved-background graviton tadpole belongs to the same computation.

**Load-bearing assumption (named).** That the shared `Z_h` dressing `C^2` is the graviton's **physical**
wave-function renormalization, whose anomalous dimension is either `eta_N` (EH-adapted) or `eta_Weyl`
(Weyl-adapted) -- **the un-settled fork.** The HORN-K lean rests on the physical claim that the leading
4th-order kinetic term sets that normalization (`eta_h -> eta_Weyl -> 0`); the HORN-Q lift rests on the
EH-adapted identification (`eta_h = eta_N* = -2`).

**Two-derivation status.** AGREE (D1 direct off-diagonal trace = D2 anomalous-dimension identity), in
every regulator family.

**Confidence.** HIGH on the structural readouts (positive `c_reg` all three families; `eta_C>0` EH-scheme
robustly; `eta_C=0` Weyl-scheme; D1=D2; `f_2^2*=0` a structural root always). MEDIUM on the scheme split
being the true fork and on the HORN-K lean (physical argument, truncation-conditional; the Reuter-FP
`eta_N*=-2` is exact). **The sign is the whole result, and the honest sign is: `+` in the EH-adapted
scheme, `0` in the Weyl-adapted scheme -- scheme-decided, leaning `0` (HORN K).**

---

## Computed-vs-ported ledger

| Quantity | Status | Source |
|---|---|---|
| `Phi^2_2(0)` for Litim (`1/2`), exponential (`1.0`), shape sweep (`0.69-1.12`) | **COMPUTED (closed form + quadrature)** | this file / `W89` Part A |
| `c_reg > 0` (off-diagonal `C^2` threshold integral positive-definite) all three families | **COMPUTED** | this file / `W89` Part A |
| `eta_C = -eta_h c_reg`; `eta_C^{EH} = +2 c_reg > 0`, `eta_C^{Weyl} = 0`, all regulators | **COMPUTED** | this file / `W89` Parts B-C |
| D1 (direct off-diagonal trace) = D2 (anomalous-dimension identity) | **COMPUTED** | this file / `W89` B3 |
| `f_2^2* = 0` a structural root in every scheme+regulator | **COMPUTED (carried from W88)** | W88 / this file D4 |
| lifted root `f_2^2* = eta_C/(kappa b_2)` in `[0.07,0.16]` (EH scheme) | **COMPUTED** | this file / `W89` Part C |
| `eta_N* = -2` at the Reuter FP | PORTED (canonical scaling) | Reuter; CPR |
| pure-gravity Weyl one-loop `133/10`; RS `+0.70` | PORTED / COMPUTED(W82/W88) | Fradkin-Tseytlin; W82 |
| two-sided Weyl-FP literature (AF `f_2^2*=0` vs Newton-induced lift) | PORTED | Codello-Percacci; BMS; agravity |
| O(1) `c_reg` normalization (sign load-bearing) | PORTED / schematic | -- |
| single self-consistent `Z_h` / `eta_h`-from-leading-kinetic-term | **NOT computed -- the named deciding truncation** | -- |

---

## Governance note

No canon / `RESEARCH-STATUS` / claim-status / verdict / posture file is changed by this stage; H59/H61a
remain **OPEN**. The deterministic test `tests/W89_eta_c_across_regulators.py` runs green (exit 0) and
encodes `eta_C` per regulator per scheme, the sign, and the horn verdict as assertions. All web references
are read-only literature. Not committed by this run.
