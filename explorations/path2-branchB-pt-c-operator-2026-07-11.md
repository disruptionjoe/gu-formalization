# Path 2, Branch B -- the PT / C-operator (Bender-Mannheim) construction, tested order by order

**Wave:** Path-2 loop-positivity blockbuster (H59 / keep-and-grade at loop level), blind multi-branch.
**Branch B mandate:** the PT-symmetric realization of keep-and-grade. Physical inner product is the
C-operator grading `<a|CPT|b>`; equivalently a similarity transform to a Dirac-Hermitian, isospectral
Hamiltonian. Test whether the C-operator / similarity transform exists and stays consistent for the
*interacting* theory ORDER BY ORDER, and whether the equivalent Hermitian theory stays local + relativistic.
**GU-independent** by construction: worked on the Pais-Uhlenbeck oscillator and generic 4th-order/Stelle
structure; no GU-specific input.

**Artifacts:** this file + deterministic test `tests/W49_path2_B_c_operator.py` (20/20 checks, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks used (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Two load-bearing forks, stated explicitly so the orchestrator can cross-test:

1. **Physical inner product.** We use the **C-operator grading** `<a|CPT|b>`, with the metric
   `eta = e^{-Q}` and charge `C = eta^{-1} P` built from the theory's own eigenstates -- NOT a
   positive-Hilbert-subspace projection (that is a *different* object and the wrong one for this branch;
   projecting would remove the ghost, not grade it). Positivity is `C^2 = 1` with the right signature.

2. **"The Hamiltonian."** We distinguish the **PT-Hermitian** `H` (`H != H^dag`, but `PT`-symmetric,
   real spectrum) from its **Dirac-Hermitian similarity image** `h = eta^{1/2} H eta^{-1/2} = e^{-Q/2} H e^{Q/2}`.
   The whole Q-caus question *is* the fork: is `h` a *local, Lorentz-invariant* operator, or does the
   similarity map `e^{-Q/2}` turn a local `H` into a non-local `h`? This is exactly the Mannheim-vs-critics
   axis.

The keep-and-grade construction (KEEP the ghost, GRADE the state space via an indefinite/Krein/PT metric)
is the correct object per the repo's settled ghost-clearance fork. Branch B does not re-litigate that; it
tests whether the PT realization of it survives interactions.

---

## 1. Five-persona team (run inline, sequential, single context)

### Persona 1 -- PT-QFT / C-operator specialist (the computation)

**Setup.** For a `PT`-symmetric `H = H0 + eps H1` with `H0` Dirac-Hermitian and `P`-even and `H1`
anti-Hermitian and `P`-odd (`H1 = i x^3` is the canonical case; the ghost's cubic self-coupling has this
structure), the metric `eta = e^{-Q}` obeys the pseudo-Hermiticity condition `eta H eta^{-1} = H^dag`.
Writing `Q = eps Q1 + eps^2 Q2 + ...` and expanding to first order gives the **defining C-operator equation**

>  **`[H0, Q1] = -2 H1`.**

In the `H0` eigenbasis (`E_n`) this is solved elementwise: `Q1_{mn} = -2 H1_{mn} / (E_m - E_n)`.

**Results (computed in `tests/W49_path2_B_c_operator.py`, Model B, truncated Fock space):**
- `Q1` from that formula is **Hermitian** (forced by `H1` anti-Hermitian) and **parity-odd**
  (`P Q1 P = -Q1`, forced by `H1` parity-odd). Verified to machine precision.
- Parity-oddness makes `C = e^{eps Q1} P` satisfy **`C^2 = 1` identically** (not just to first order):
  `C^2 = e^{eps Q1} P e^{eps Q1} P = e^{eps Q1} e^{eps P Q1 P} = e^{eps Q1} e^{-eps Q1} = 1`. Verified `||C^2-1|| ~ 1e-14`.
- `Q1` **solves** `[H0,Q1] = -2 H1` to `~1e-13`.
- The equivalent Hermitian `h = e^{-eps Q1/2} H e^{eps Q1/2}` has its **O(eps) non-Hermiticity exactly
  removed**: `||h-h^dag||/||H-H^dag||` is small and `-> 0` linearly in `eps` (0.046 at eps=0.005 -> 0.011 at
  eps=0.0025). The leading anti-Hermitian piece cancels because `H1 + (1/2)[H0,Q1] = H1 - H1 = 0`.
- The perturbative metric `eta = e^{-eps Q1}` is **positive-definite** (min eigenvalue > 0).

**Conclusion (P1):** the first interacting correction to the C-operator EXISTS, is uniquely fixed by
`[H0,Q1]=-2H1`, and does its job (keeps `C^2=1`, keeps `eta>0`, Hermitizes `H` to O(eps)). The PT
perturbation series is well-posed at first order. This is the standard Bender-Brody-Jones result reproduced
by independent numerics, not assumed.

### Persona 2 -- Math-physics referee (grades every step)

| Claim | Setting | Grade |
|---|---|---|
| Free-level C-operator/metric exists, `eta>0`, `h` Hermitian, spectrum real | QM, quadratic (Model A Swanson; exact) | **PROVEN** (closed form + numerics agree to 1e-13) |
| First interacting `Q1` exists, unique, `C^2=1`, `eta>0`, O(eps) Hermitization | QM, cubic (Model B) | **PROVEN at O(eps)** in QM (self-validating numerics) |
| C-operator exists non-perturbatively | QM, 2x2 interacting (Model C, BBJ exact) | **PROVEN** (exact) |
| Perturbation series converges / all-orders C exists | QM | **ARGUED, not proven** (only O(eps) shown; higher orders known to exist for `ix^3` in the literature but convergence is asymptotic, not established here) |
| Any of the above in QFT (field theory, continuum) | QFT | **NOT SHOWN** -- everything above is quantum-mechanical (finite dof) |
| Equivalent Hermitian `h` is LOCAL | QFT | **REFUTED** at the structural level (Persona 3 / Model D) |

**Referee's headline:** Q-pos is in good shape *in QM* order by order. The gap the referee will not let the
branch paper over is **QM vs QFT**: the C-operator is a similarity transform on the full Hilbert space, and
in QFT that transform's *locality* is not automatic -- it is the whole game. Grade the QFT statements
separately and honestly.

### Persona 3 -- Adversary (attacks Branch B's own claim)

**Attack: "Your equivalent Hermitian theory is secretly non-local, so you have not saved a *relativistic*
theory -- you have traded the ghost for non-locality."**

The generator is `Q1_{mn} = -2 H1_{mn}/(E_m - E_n)`. In QFT the energy labels become continuum dispersion
`E ~ omega(k) = sqrt(k^2 + m^2)`, so `Q1` carries **energy denominators** `~ 1/(omega(k_1) + omega(k_2) + ...)`.
A **local** operator (a finite polynomial in the fields and *finitely many* derivatives) has a momentum-space
symbol that is a **polynomial** -- an *entire* function of `k`. But `1/sqrt(k^2+m^2)`:
- is **not entire**: it has branch points at finite complex momentum `k = +- i m`, so its power series has
  **finite radius of convergence = m** (verified numerically in Model D: estimated radius 1.005 vs exact 1);
- its Taylor series **diverges for real `|k| > m`** (partial sums at `k=2m` blow up `5.5e1 -> 1.9e37`);
- **decays** on the momentum line while every nonzero polynomial diverges, so no *fixed* finite-order local
  operator approximates it uniformly on `R` (fixed degree-8 residual GROWS `1.7e-3` on `[0,4m]` `-> 6.2e-2`
  on `[0,40m]`).

Therefore `Q`, and hence `h = e^{-Q/2} H e^{Q/2}` (an infinite series in `Q`), is a **non-local** operator in
the relativistic field theory. **The adversary wins on Q-caus.** This is precisely the Mannheim-vs-critics
dispute (Mannheim: the PT/pseudo-Hermitian theory is unitary; critics -- e.g. the standard objection to
PT-QFT -- the isospectral Hermitian partner is non-local / the map does not preserve microcausality).

Note this does NOT break Q-pos: a non-local `h` can still be Hermitian with a positive metric. The cost is
paid in the *causality/locality* column, not the *positivity* column. That separation is the branch's key
finding.

### Persona 4 -- Cross-checker (independent second derivation)

Two independent checks, both in the test:
1. **Free PU analog, exact (Model A, Swanson `H = w(a^dag a+1/2) + alpha a^2 + beta a^dag^2`).** A genuinely
   non-Hermitian *quadratic* Hamiltonian -- the clean stand-in for the free Pais-Uhlenbeck C-operator (a
   quadratic non-Hermitian `H` with a known Hermitian similarity image). Built the positive metric
   `eta = (V V^dag)^{-1}` by an independent route (eigen-decomposition, not perturbation theory), verified
   `eta H = H^dag eta` (1e-13), `eta > 0`, and that `h` has spectrum exactly `Omega(n+1/2)` with the
   closed-form `Omega = w sqrt(1 - 4 alpha beta / w^2)` (agreement 1e-14). This confirms the free-level
   metric non-perturbatively and against a formula.
2. **2x2 Bender-Brody-Jones (Model C).** Exact closed-form `C = (1/cos a)[[i sin a, 1],[1, -i sin a]]`,
   `sin a = (r sin th)/s`. Verified `C^2=1`, `[C,H]=0`, real spectrum, and an *independently constructed*
   positive metric `eta=(VV^dag)^{-1}` intertwines `H, H^dag`. Confirms the C-operator exists
   non-perturbatively in a controlled interacting setting -- the perturbative Model-B result is not a
   truncation artifact.

Both cross-checks agree with Persona 1: existence and positivity of the grading are solid in QM.

### Persona 5 -- Synthesizer (branch verdict)

See Section 2.

---

## 2. Branch-B verdict on {Q-cut, Q-pos, Q-caus}

- **Q-pos (PRIMARY): PASS in QM, order-by-order INDICATION.** The C-operator / positive metric exists at
  free level (proven, exact), admits a unique first interacting correction `Q1` solving `[H0,Q1]=-2H1`
  (proven at O(eps)), keeps `C^2=1` exactly and `eta>0`, and Hermitizes `H` at leading order. Grade:
  **interacting-order indication (QM)**. NOT an all-orders proof, and NOT shown in QFT.

- **Q-cut: UNDETERMINED by this branch.** C-operator existence is *consistent with* ghost decoupling from
  the cuts but does not by itself establish it; the optical-theorem / Cutkosky computation is a different
  branch's object. Branch B contributes no independent Q-cut evidence. Grade: **not addressed.**

- **Q-caus (CRUX): FAIL (structural, QM->QFT).** The similarity generator `Q` carries energy denominators
  `1/sqrt(k^2+m^2)`, whose symbol is **not entire** (branch points at `k=+-im`, finite radius of convergence
  `m`). No finite-order local operator reproduces it; therefore the equivalent Dirac-Hermitian `h` is
  **non-local** in the relativistic theory. Unitarity/positivity is bought at the price of **locality /
  micro-causality**. Grade: **structural obstruction, high confidence at the symbol level.**

**Physical inner product used:** C-operator grading `<a|CPT|b>`, `eta=e^{-Q}`, `C=eta^{-1}P` -- keep-and-grade,
not positive-Hilbert projection.

**The ONE killing obstruction:** **non-locality of the equivalent Hermitian Hamiltonian.** The map that makes
the PT theory manifestly unitary (`e^{-Q/2}`) is generated by a non-local `Q` in QFT, so the "healthy"
Hermitian partner theory is non-local. Either you keep manifest locality (work with the PT-Hermitian `H`,
whose observable structure -- S-matrix causality -- is then what critics say is not established at loops), or
you keep manifest positivity (work with `h`, which is non-local). Branch B cannot have both simultaneously in
manifest form. That is the load-bearing finding.

**Confidence grade:** Q-pos = *interacting-order indication (QM only)*; Q-caus = *QM->QFT structural
argument (symbol-level, high confidence)*. Nothing here is an all-orders QFT proof, and nothing changes GU
claim status.

**Load-bearing assumption:** that the QFT metric/similarity generator inherits the QM energy-denominator
structure (i.e. `Q ~ H1/(E-E')` lifts to `Q ~ integral H1(k)/(omega+omega')`). If some cancellation or a
*local* choice of metric existed in QFT (a positive `eta` with a *polynomial* / local generator), Q-caus
could be rescued -- this is the single computation that would overturn the branch verdict. The known
no-go-flavored results (non-locality of the Hermitian partner) and the divergence structure make this
unlikely, but Branch B did not prove it impossible.

**What one computation would firm it:** exhibit, or prove non-existent, a **local** positive metric for the
interacting 4th-order/PU field theory at one loop -- i.e. decide whether *any* choice of `Q` (not just the
canonical energy-denominator one) can be local while keeping `eta>0` and `C^2=1`. A proof of "no local
positive metric exists" would upgrade Q-caus FAIL from structural-argument to theorem.

---

## 3. Honest limitations

- Everything computed is **quantum-mechanical** (finite degrees of freedom). The Q-caus obstruction is a
  *structural lift* of the QM generator to QFT via the dispersion `omega(k)`, argued at the level of the
  operator symbol -- not a full one-loop QFT amplitude computation.
- Only the **first** interacting order of `Q` was computed. Higher-order existence is known in the
  `ix^3` literature but convergence/all-orders is not established here.
- The truncated-Fock numerics are internally self-validating (residuals to machine precision, `O(eps)`
  scaling confirmed) but are illustrations of the algebraic identities, not a substitute for a QFT proof.
- Model D's non-locality criterion is deliberately the *correct* one (non-entire symbol / finite radius of
  convergence), not the naive "not polynomial on a compact interval," which Weierstrass would defeat.
