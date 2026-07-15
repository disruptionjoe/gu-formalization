---
title: "W240 DESI intake adjudication and hourly Track B prediction queue"
status: exploration
doc_type: research_register
created_at: "2026-07-15"
updated_at: "2026-07-15"
claim_status: OPEN
scope: "GU-only Track B prediction search and dark-energy evidence hygiene"
inputs:
  - explorations/W239-track-b-distinctive-prediction-scan-2026-07-15.md
  - explorations/wave45/H46B-referee-grade-desi-verification-2026-07-13.md
  - lab/deep-research/desi-late-time-dark-energy-cpl-external-report-2026-07-15.md
machine_receipt:
  - tests/W240_desi_intake_and_hourly_prediction_queue.py
external_refs:
  - "DESI Collaboration, DESI DR2 Results II, arXiv:2503.14738"
  - "T. J. Hoyt et al., Union3.1, arXiv:2601.19424"
  - "DESI full five-year survey milestone, 2026-04-15"
  - "Euclid Consortium Q2 release and DR1 timing, 2026-06-24"
governance: "Exploration-tier only. No canon, verdict, claim-status, publication, or external-action change. bar(b) and H59 remain OPEN."
---

# W240: DESI intake adjudication and hourly Track B prediction queue

## Result

The external DESI report is useful as a literature and decision map, but it is not a safe numerical
source. Its central qualitative lesson survives: raw BAO distances, CPL posterior compressions, CMB
anchors, and supernova calibration choices answer different questions and must not be collapsed into
one headline. Its claimed DR2 distance table does not survive primary-source comparison.

The 30 W239 prediction targets are now converted into a dependency-aware hourly queue. The queue takes
cheap, high-information branch killers first, then commits to the two hard objects that can actually
produce a distinctive physical prediction. Future data releases are passive monitors. They do not
replace a GU derivation.

No current GU prediction has been found. This register organizes the search; it does not close
`bar(b)` or `H59`.

## 1. Provenance and numerical adjudication

The moved file is preserved byte-for-byte at
`lab/deep-research/desi-late-time-dark-energy-cpl-external-report-2026-07-15.md` with SHA-256
`CA125E1F16EE439CDADF3E20AB0198F6FE04BAF63858844556743310B022D49A`. It is external evidence. Its
embedded internal search tokens are not usable citations.

### The material numerical failure

The report says its first table is DESI DR2 Table IV. Several entries do not match the official DR2
paper or the released likelihood means already verified in H46B. Examples are:

| Quantity | External report | Official DR2 Table 4 | Difference in official printed sigma |
|---|---:|---:|---:|
| LRG1 `D_H/r_d` | 20.97 | 21.863 +/- 0.425 | 2.10 |
| LRG2 `D_M/r_d` | 16.84 | 17.351 +/- 0.177 | 2.89 |
| LRG2 `D_H/r_d` | 20.08 | 19.455 +/- 0.330 | 1.89 |
| ELG2 `D_H/r_d` | 13.83 | 14.176 +/- 0.221 | 1.57 |

The mismatch is not harmless rounding. The report also supplies an isotropic QSO `D_V/r_d`, while the
DR2 cosmology likelihood uses anisotropic QSO `D_M/r_d` and `D_H/r_d`. The numbers look like a mixed or
DR1-like table with tightened errors, not the cited DR2 likelihood. They do not match the arXiv v1 DR2
Table IV either. Therefore:

1. none of the report's raw-distance values may enter GU calculations;
2. H46B's official 13-element mean and 13 by 13 covariance remain authoritative;
3. the report may guide source discovery only, with each claim rechecked against a primary source.

### What did verify

The report's four main DR2 CPL posterior summaries agree with the DESI paper and H46B:

| Combination | `w_0` | `w_a` | DESI preference over flat Lambda-CDM |
|---|---:|---:|---:|
| DESI + CMB | -0.42 +/- 0.21 | -1.75 +/- 0.58 | 3.1 sigma |
| + Pantheon+ | -0.838 +/- 0.055 | -0.62 +0.22/-0.19 | 2.8 sigma |
| + Union3 | -0.667 +/- 0.088 | -1.09 +0.31/-0.27 | 3.8 sigma |
| + DES-SN5YR | -0.752 +/- 0.057 | -0.86 +0.23/-0.20 | 4.2 sigma |

The report also correctly emphasizes the following points, now independently checked:

- DESI reports 3.1 sigma for DESI plus full CMB, but 2.4 sigma when the full CMB likelihood is replaced
  by minimal early-universe priors. The CMB anchor is not a neutral formatting choice.
- The supernova dependence is scientifically material. DESI itself highlights the special leverage and
  calibration delicacy of low-redshift supernovae.
- Union3.1 finds that a self-consistent host-mass treatment reduces the old low-redshift cross-sample
  discrepancy and brings the recalibrated DESI-combined significances closer together, at about 3.2 to
  3.4 sigma. The exact sigma count remains calibration-sensitive.
- BAO measures distances relative to the sound horizon. A GU distance prediction must state how `r_d`
  and the CMB acoustic scale are fixed.

### Timing corrections

The report's late-2026 or early-2027 DESI five-year language is now superseded by a more precise official
statement: the original five-year observations completed in April 2026, and DESI expects the first full
five-year dark-energy results in 2027. The report's 23 percent error shrink is only a square-root exposure
scaling. It is not an official DESI forecast.

Euclid's current official wording is DR1 in late 2026, with dark-energy discoveries expected in 2027.
The report's exact "DR1 Foundation in November 2026" label and date are not stable enough to use as a GU
gate. The queue records DESI five-year and Euclid DR1 as release monitors without inventing a fixed day.

## 2. Hourly scheduling rule

Each hourly run takes the highest-ranked `READY` item, attacks its first kill condition, and leaves one
bounded receipt. It does not perform another qualitative prediction brainstorm.

The ordering rule is:

```text
priority = dependency readiness, then expected branch information per bounded run,
           with the interacting physical-state gate protected as the hard North Star
```

Operational constraints:

1. one active technical packet at a time;
2. a failed prerequisite kills or downgrades every dependent prediction family immediately;
3. no target data may be used to fix a parameter and then confirm the same target;
4. a structural feature is not promoted to a prediction without a physical observable;
5. passive release monitoring consumes no hourly run unless new data have actually arrived;
6. every surviving numerical relation declares scale, running, quotient, comparison model, and first
   experimental confrontation before inspecting the target data.

## 3. Corrected decisive order

| Rank | Packet | Impact | First-run difficulty | State | First bounded deliverable and kill rule |
|---:|---|---:|---:|---|---|
| 1 | `DE-AMP`: GU CMB acoustic-scale amplitude re-solve | 4 | 2 | READY | Re-solve `theta_*` using GU's own `D_M(z_*)`, including the high-redshift tail, then rerun the official DR2 likelihood. If the canonical amplitude remains strongly disfavored, kill the positive raw-BAO leg. If it moves, report the predeclared shift and fit without calling it a novel prediction. |
| 2 | `FLAVOR-RANK`: coefficient-freedom no-go audit | 5 | 2 | READY | Count basis-invariant Yukawa degrees of freedom after every built symmetry, quotient, and source constraint. Any surviving independent coefficient kills zero-parameter mass and mixing claims at the current construction grade. |
| 3 | `NORM-RANK`: native normalization and rescaling audit | 5 | 3 | READY | Compute all field-rescaling invariants among `kappa`, `Z_U`, `mu_DW`, and physical pole parameters. If no absolute dimensionless relation survives, kill the fixed-range gravity route until new dynamics are built. |
| 4 | `FLAVOR-OBS`: existing-data invariant scan | 5 | 3 | GATED by `FLAVOR-RANK` | Search only the surviving invariant space for a rank, sign, zero, singular-value, mixing, or Dirac/Majorana relation. One adjustable GU-specific coefficient that absorbs the result kills the candidate. |
| 5 | `PHYSICAL-C`: interacting physical quotient, `C` metric, and pole gate | 5 | 5 | READY after ranks 1 to 3 | Build the constrained physical state space and one gauge-independent interacting observable. No positive interacting `C`, or no physical pole after the quotient, kills pole, interference, and mirror-observable families. This is the protected North Star and may span several bounded runs. |
| 6 | `POLE-PACKET`: native scale, residue, and line shape | 5 | 4 | GATED by `NORM-RANK` and `PHYSICAL-C` | Emit one predeclared pole mass or scale ratio, residue sign, line shape, and named confrontation. Any target-calibrated scale or standard EFT mimic with equal freedom kills distinctiveness. |
| 7 | `MIRROR-ESCAPE`: compactification-with-chirality census | 5 | 4 | READY | Exhaust native operators beyond W237's null-pair bilinear routes. If every compactifier kills chirality, close the current mirror-particle prediction route negatively. |
| 8 | `MIRROR-PACKET`: physical mirror spectrum and decays | 5 | 5 | GATED by `MIRROR-ESCAPE` and `PHYSICAL-C` | Prove cohomology survival, then derive charges, masses, splittings, branching ratios, and a production rate. Any independent mass or mixing parameter prevents a fixed-rate claim. |
| 9 | `COSMO-X`: model-native expansion and growth relation | 4 | 4 | GATED by `DE-AMP` and native source dynamics | Derive a parameter-free relation between non-CPL `w(z)` structure and a growth observable such as `f sigma_8`. Do not fit `f_0` to DESI and reuse it as a prediction. |
| 10 | `RECORD-X`: record-current response diagnostics | 3 | 4 | BACKLOG | Derive a retarded transfer function, memory observable, or source pulse only if it closes a prerequisite above. Equivalence to an ordinary fixed-source kernel kills novelty. |

This order intentionally puts three cheap prerequisite audits before the full interacting construction.
It does not demote the hard `PHYSICAL-C` object. Once the fast gates have run, that object owns the long
chain because both a physical pole and a physical mirror packet depend on it.

## 4. Complete mapping of the 30 W239 targets

Every persona proposal remains in scope, but the hourly loop works dependency packets rather than 30
independent prose ideas.

| Packet | W239 targets absorbed |
|---|---|
| `FLAVOR-RANK` / `FLAVOR-OBS` | basis-invariant Yukawa singular-value ratio; `Z/3` texture-zero mixing sum rule; Dirac-only neutrino mass selection; zero-parameter relation among measured SM inputs; dimensionless overconstraint of existing data; sign prediction opposite a live competitor |
| `PHYSICAL-C` | physical extra-pole residue and line shape; renormalization-group fixed coupling ratio; threshold matching relation across GU sectors; physical mirror cohomology parity; positivity-fixed sign of a scattering interference term; channel-S allowed and channel-D forbidden chiral spectrum |
| `NORM-RANK` / `POLE-PACKET` | fixed-strength fixed-range short-distance force; massive-spin-2 gravitational-wave dispersion; parameter-free Kerr ringdown correction; dark-energy to spin-2 scale ratio; exact observable ratio of Einstein Weyl and vacuum terms; fixed tensor ratios in the source response function; torsion-balance force with predeclared alpha and lambda |
| `MIRROR-ESCAPE` / `MIRROR-PACKET` | complete vectorlike mirror multiplet spectrum; `SO(10)`-fixed mirror branching-fraction ratios; channel-S composite resonance pattern; topologically protected spectral multiplicity; fixed-rate mirror production and decay packet; complete correlated smoking-gun spectrum |
| `COSMO-X` | predeclared `w(z)` width and crossing shape; fixed sign relation between `w(z)` and `f-sigma8` |
| `RECORD-X` | retarded record-current transfer function; record-creation gravitational memory signal; capability-change correlated source pulse |

The machine receipt extracts W239's literal 30-row register and proves that this mapping covers every
target exactly once.

## 5. What the DESI report changes in GU

1. **It strengthens data hygiene, not GU's dark-energy claim.** The raw table failure is a concrete warning
   that secondary research reports must never seed likelihood arrays.
2. **It makes the amplitude re-solve the best cosmology quick win.** The CMB anchor and `r_d` handling are
   load-bearing, and H46B already named this exact unresolved calculation.
3. **It downgrades sigma-count chasing.** Union3.1 demonstrates that improved low-redshift calibration moves
   the catalogue-specific significances toward one another. GU should predict a cross-observable relation,
   not attach itself to whichever current catalogue gives the largest sigma.
4. **It reinforces the raw-likelihood versus CPL distinction.** GU's non-CPL shape must be confronted at the
   raw likelihood level while the CPL projection remains a separate, already unfavorable diagnostic.
5. **It turns future surveys into preregistered judges.** DESI five-year and Euclid DR1 matter only after GU
   freezes a model-native relation and comparison procedure before their results are used.

## 6. External release monitors

These are not hourly work:

- DESI full five-year dark-energy results: expected during 2027 according to the collaboration's April 2026
  survey-completion statement.
- Euclid DR1: scheduled for late 2026 according to the Euclid Consortium's June 2026 statement, with core
  cosmology results expected later.

On release, the first run verifies provenance and freezes a blind comparison packet. It does not retune GU.

## 7. Honest close

The quickest possible wins are negative but valuable: the amplitude re-solve can settle whether GU's
distance-level positive leg is fairly normalized; the flavor-rank audit can retire an entire family of
illusory mass predictions; and the normalization audit can determine whether a physical pole can ever be
made parameter-free with the built action. If those gates pass, the interacting physical quotient and `C`
metric become the decisive expensive object.

The DESI report did not supply a novel GU prediction. It supplied a better adversarial test plan and one
important source-quality failure. `bar(b)` and `H59` remain OPEN.

## Verified sources

- DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and
  Cosmological Constraints," [arXiv:2503.14738](https://arxiv.org/abs/2503.14738).
- DESI Collaboration, [DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/).
- T. J. Hoyt et al., "Union3.1: Self-consistent Measurements of Host Galaxy Properties for 2000 Type Ia
  Supernovae," [arXiv:2601.19424](https://arxiv.org/abs/2601.19424).
- DESI Collaboration, [five-year survey completion and 2027 result timing](https://www.desi.lbl.gov/2026/04/15/desi-reaches-mapping-milestone-surpassing-expectations/).
- Euclid Consortium, [Q2 release and late-2026 DR1 timing](https://www.euclid-ec.org/public/press-releases/euclid-quick-data-release-2/).

---

*Filed 2026-07-15. The external report was moved from the JB Workbench into GU and preserved
byte-for-byte. Read-only primary-source verification was performed. No publication, promotion, canon,
verdict, claim-status, or cross-repository action was taken.*
