---
title: "B3-DE likelihood-scope disposition: CPL is compression, not the pointwise target"
status: active_research
doc_type: primary_source_likelihood_scope_disposition
created: "2026-08-23"
registry: lab/process/b3-de-likelihood-scope-disposition.json
probe: tests/channel-swings/b3_de_likelihood_scope_disposition_probe.py
grade: "PRIMARY-SOURCE LIKELIHOOD-SCOPE DISPOSITION; CROSSING EVIDENCE PRESERVED; NO LEDGER MOVEMENT"
target_claim: NONE-NOT-A-KILL
target_claim_note: "types an external likelihood and an internal prediction target; does not kill a source claim or the GU family"
canon_verdict_change: none
---

# B3-DE likelihood-scope disposition

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> conventional cosmological comparators throughout. Every numerical result
> binds only the named model, data combination and nuisance treatment. Read
> `lab/methods/source-native-comparator-routing.md` before reusing it.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: B3-DE primary-source likelihood-scope disposition
carrier: DESI DR2 BAO ratios with named CMB and supernova likelihoods LAYER=observed CHIRALITY=N/A
pairing: likelihood and covariance evaluation ON=the exact declared observed carriers
real_structure: N/A
grading: N/A
action_owner: comparator
target: LT-GR2e dark-energy likelihood semantics MAP-TYPE=evaluation
```

## Disposition

`B3-DE-01` is disposed
`DISPOSED_NO_LEDGER_MOVEMENT__LIKELIHOOD_SCOPE_CORRECTION`.

The filing intuition was two-sided and therefore valuable, but its proposed
absolute withdrawal was too strong. The DESI CPL pair `(w_0,w_a)` is not a
literal pointwise measurement of `w(z)`, so it cannot by itself be either a
direct target for GU or credit for landing near a central pair. But the
likelihood information that prefers evolution and crossing does not vanish
when the CPL coordinates are demoted. DESI's extended analysis finds the same
qualitative preference through parametric and nonparametric routes while
explicitly saying that noncrossing alternatives are disfavored, not ruled out.

The correct relocation is therefore:

1. **Observed carrier:** DESI BAO distance ratios, combined only with the
   explicitly named CMB and supernova likelihoods.
2. **Compressed evidence:** the CPL posterior and model comparison. These are
   useful evidence coordinates, not literal samples of a true pointwise
   equation of state.
3. **Direct evidence:** nonparametric and class-constrained likelihood tests.
   These retain a lean toward phantom-divide crossing but do not exclude the
   entire noncrossing class.
4. **GU target:** evaluate one action-owned GU family, including its pointwise
   `w(z) >= -1` property where that property is actually derived, through the
   same observables and covariances. No such direct GU likelihood exists in
   this repository yet.

This corrects both tempting one-sided readings. “CPL is only a compression, so
the evidence against GU disappears” is false. “The CPL central pair directly
measures a crossing and therefore falsifies every noncrossing GU family” is
also false.

## Primary-source chain

### DESI DR2 baseline cosmology

DESI DR2 Results II reports that the `w_0 w_a` extension prefers the quadrant
`w_0 > -1`, `w_a < 0`, with preference over Lambda-CDM dependent on the named
dataset combination. The paper reports `3.1 sigma` for DESI+CMB and a range
`2.8--4.2 sigma` when different supernova samples are added. Those are
model-comparison statements within the CPL extension, not pointwise
measurements of `w(z)`.

Source: DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon
Acoustic Oscillations and Cosmological Constraints*, arXiv:2503.14738v3.

### Extended dark-energy analysis

DESI's extended analysis supplies the decisive scope check. It says the CPL
form can reproduce distances and expansion to high accuracy yet may fail to
represent the underlying `w(z)`, potentially producing an apparent crossing.
It then tests broader parametric and nonparametric reconstructions. Those
routes continue to indicate a possible crossing near `z ~ 0.5`; noncrossing
alternatives fit less well but cannot be ruled out. The evidence therefore
survives, but its ceiling is a likelihood preference rather than a direct
class-wide exclusion.

Source: DESI Collaboration, *DESI DR2 Results III: Extended Dark Energy
Analysis*, arXiv:2503.14743v2.

### 2026 Lyman-alpha AP update

The citation-time audit must include the newer DESI Results IV likelihood. Its
Lyman-alpha full-shape Alcock--Paczynski measurement is centered at `z=2.33`
and updates the combined `w_0 w_a` comparison to `2.7 sigma` for DESI+CMB and
`3.2 sigma` when supernovae are added. This is an important high-redshift
geometric anchor. It is not, by itself, a pointwise measurement of the
low-redshift crossing; future GU evaluation must consume it as part of the
full named likelihood chain.

Source: DESI Collaboration, *DESI DR2 Results IV: Cosmological Constraints
from the Lyman-alpha Forest Full-Shape and BAO Measurements*,
arXiv:2607.27410v3.

## DARK-ENERGY-07 correction chain preserved

The source reconstruction retains every standing correction:

- the approximately `3.2 sigma` displacement of the recorded CPL point is a
  two-degree-of-freedom Mahalanobis radius, while the one-dimensional reading
  is approximately `2.7 sigma`;
- fixed-`omega_m h^2` bounds on `f_0` are roughly three times tighter than the
  profiled bounds and cannot be substituted for them;
- the bare `+5.7 sigma_A` overshoot is not an honest mechanism statement,
  because Lambda-CDM itself gives `+4.0` on that amplitude coordinate. The
  recorded discriminator is shape: the amplitude-marginalized shape penalty
  is `Delta chi^2 = +19.3` at `M^2=8`, while the fitted CPL shape gains
  `Delta chi^2 = -22.8`;
- adding uncalibrated supernovae does not mechanically punish a low `H_0`:
  they constrain distance shape and `Omega_m`, and the calibrated GU value
  `Omega_m ~ 0.352` lies near the recorded DES-Y5 value;
- the one-parameter theta family is not class-wide excluded. It is driven to
  its Lambda-CDM limit, with best-`f_0` `Delta AIC` only `+1.9` to `+3.2`.
  The honest status remains “excluded as the DESI dark-energy signal;
  unconstrained-but-null as a family.”

## Ledger comparison

LT-GR2e v0.263 remains byte-identical at `NEEDS / MISSING_CONSTRUCTION`. Its
distance already asks for matter/radiation FLRW perturbations and a held-out
`w(z)` from the surviving horn. Its revival trigger already requires an
action-owned cosmological solution, fixed initial data and held-out
DESI/CMB/BAO predictions. That wording is stronger and more source-faithful
than either importing a CPL central pair or deleting the DESI likelihood
preference. No evidence delta is warranted.

The historical comparative-tensions ledger remains historical evidence. Its
sentence treating the CPL central pair as the literal pointwise target is not
licensed for current reuse. Its weaker content survives: crossing models fit
the named data combinations better, so a derived noncrossing GU family faces
a scoped likelihood lean until it is evaluated directly.

## Hostile review and exact ceiling

- **Overclaim attacked:** demoting CPL coordinates does not demote the data or
  erase the nonparametric crossing preference.
- **Contrary evidence retained:** DESI explicitly reports that noncrossing
  alternatives are disfavored but cannot be ruled out.
- **Unclosed seam:** no action-owned GU background/perturbation solution has
  been evaluated against the current DESI+CMB+supernova likelihood, including
  the 2026 Lyman-alpha AP update.
- **No laundering:** this disposition supplies no numerical fit, mechanism,
  prediction, confirmation, source ownership, ledger verdict, canon verdict
  or public-posture change.

Three B3 entries remain. They require their own citation-time source
reconstruction; this result grants no shortcut into B2/source-action work.
