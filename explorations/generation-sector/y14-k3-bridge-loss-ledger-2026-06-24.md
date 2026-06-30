---
title: "Y14/K3 Bridge-Loss Ledger"
date: "2026-06-24"
status: exploration
doc_type: bridge_loss_ledger
verdict: "K3_CONTROL_ONLY_NOT_CURRENT_PHYSICAL_GU_GENERATION_EVIDENCE"
owned_path: "explorations/generation-sector/y14-k3-bridge-loss-ledger-2026-06-24.md"
depends_on:
  - "explorations/persona-and-dialectic/all-persona-wall-break-steelman-hegelian-2026-06-24.md"
  - "explorations/generation-sector/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/goal-draft-physical-rs-index-problem-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/analytic-index-fredholm/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md"
  - "explorations/analytic-index-fredholm/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md"
  - "explorations/analytic-index-fredholm/oc2-sobolev-a1-bounded-transform-2026-06-23.md"
  - "tests/y14_k3_bridge_gate.py"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
optional_executable:
  - "tests/y14_k3_bridge_loss_audit.py"
---

# Y14/K3 Bridge-Loss Ledger

This note treats the `Y^14 -> K3` story as a transport/loss problem. The
question is not whether K3 has useful index formulas. It does. The question is
whether the physical noncompact projected `Y^14` index data can be transported
to compact K3 or APS data without losing the information that makes it a GU
generation-count index.

Classification vocabulary:

| class | meaning in this ledger |
|---|---|
| preserved | the datum is carried by a proved map/equivalence with the same mathematical role |
| lost | the datum is discarded or forgotten and cannot be recovered unless a correction is added |
| corrected | the datum changes by an explicitly computed correction term, such as APS eta or spectral flow |
| imported | the datum is supplied by the compact model, a convention, or an external assumption rather than transported from `Y^14` |
| underdefined | the datum is named but the current files do not yet specify or prove it |

## 1. Verdict

**Current verdict: K3 is a compact control surface, not current physical GU
generation-count evidence.**

The compact K3 raw RS calculation is valuable because it makes the nearby
symbol classes and index arithmetic explicit:

```text
E_raw = (V + 1) tensor F
ind_C(E_raw) = -38 n + 5 k
```

and the BRST-style comparison branch is also explicit:

```text
E_BRST_style = (V - 1) tensor F
ind_C(E_BRST_style) = -42 n + 3 k
```

But those are compact control classes. They are not yet the physical
noncompact GU index because the transport channel from projected weighted
`Y^14` to compact K3 or APS data is still missing several load-bearing objects:
the physical gauge-fixed/BRST RS complex, the nonempty bounded tau-discrete
sector, the compact-remainder Fredholm theorem, the unitary or APS bridge map,
the right-`H` family certificate, the physical `ch_2(F)` background, and the
eta/spectral-flow/end corrections if a boundary route is used.

Decision-grade form:

```text
K3 raw RS index != physical noncompact GU index
```

until a same-operator, same-symbol, same-`H`, same-background bridge theorem is
proved.

Permitted current citation:

```text
K3 supplies compact control index formulas for candidate RS symbol classes.
Those formulas currently leave the physical GU RS symbol and the Y^14 -> K3
bridge open.
```

Forbidden current citation:

```text
K3 gives physical GU evidence for three generations.
```

Machine-readable certificate for the audit:

```json
{
  "artifact": "Y14_K3_BRIDGE_LOSS_LEDGER",
  "version": "2026-06-24",
  "verdict": "K3_CONTROL_ONLY_NOT_PHYSICAL_GU_GENERATION_EVIDENCE",
  "promotion_allowed_now": false,
  "current_decision": "DO_NOT_CITE_K3_AS_PHYSICAL_GU_GENERATION_COUNT_EVIDENCE",
  "classification_vocabulary": ["preserved", "lost", "corrected", "imported", "underdefined"],
  "allowed_current_citation": "K3 supplies compact control index formulas for candidate RS symbol classes; it is not current physical GU generation-count evidence.",
  "promotion_rule": {
    "all_required_closed": false,
    "required_fields": {
      "physical_rs_complex": "underdefined",
      "tau_discrete_projection": "underdefined",
      "weighted_fredholm_parametrix": "underdefined",
      "bounded_transform_family": "underdefined",
      "k3_reduction_or_aps_map": "underdefined",
      "right_h_structure": "underdefined",
      "background_ch2_f": "underdefined",
      "eta_spectral_flow": "underdefined",
      "noncircular_generation_readout": "underdefined"
    },
    "forbidden_inputs": [
      "ind_H(D_RS)=8",
      "ind_H(D_GU)=24",
      "rank_eff=4",
      "rank_eff=8",
      "three_generations",
      "physical_DOF_count_as_index"
    ]
  },
  "stages": [
    {
      "id": "physical_rs_complex",
      "dominant_class": "underdefined",
      "decision": "OPEN_MISSING_SYMBOL_DATA",
      "must_transport": ["physical RS symbol", "gauge/ghost complex", "kernel and cokernel units"]
    },
    {
      "id": "tau_discrete_projection",
      "dominant_class": "underdefined",
      "decision": "OPEN_OR_NO_GO_EMPTY_DISCRETE_SECTOR",
      "must_transport": ["nonempty H-linear finite sector", "projection boundedness", "operator invariance"]
    },
    {
      "id": "weighted_sobolev_closure",
      "dominant_class": "underdefined",
      "decision": "OPEN_WEIGHTED_FREDHOLM_PARAMETRIX",
      "must_transport": ["closed domain", "finite H-kernel", "finite H-cokernel", "compact remainders"]
    },
    {
      "id": "bounded_transform_family",
      "dominant_class": "underdefined",
      "decision": "OPEN_FAMILY_KSP_CLASS",
      "must_transport": ["norm-continuous bounded transform", "common H-Hilbert model", "spectral flow accounting"]
    },
    {
      "id": "compactification_or_k3_reduction",
      "dominant_class": "underdefined",
      "decision": "UNDERDEFINED_BRIDGE_MAP",
      "must_transport": ["same physical symbol", "unitary reduction or APS boundary operator", "compact homotopy class"]
    },
    {
      "id": "h_linear_structure",
      "dominant_class": "underdefined",
      "decision": "COMPLEX_ONLY_IF_NOT_CERTIFIED",
      "must_transport": ["right-H action", "H-linear connection", "H-linear projection", "H-linear boundary/reduction maps"]
    },
    {
      "id": "background_ch2",
      "dominant_class": "underdefined",
      "decision": "OPEN_BACKGROUND_DEPENDENT",
      "must_transport": ["F=s^*S(6,4)", "rank_C(F)=16", "ch_2(F)[K3]"]
    },
    {
      "id": "eta_spectral_flow",
      "dominant_class": "corrected",
      "decision": "APS_CORRECTION_UNCOMPUTED",
      "must_transport": ["eta(A_RS^phys)", "h(A_RS^phys)", "SF_bridge", "end correction"]
    },
    {
      "id": "generation_readout",
      "dominant_class": "underdefined",
      "decision": "GEN_COUNT_NOT_FINAL",
      "must_transport": ["physical H-index", "spin-1/2 additivity", "noncircular normalization"]
    }
  ],
  "claims": [
    {
      "id": "RS-SYMBOL",
      "status": "specified_open",
      "proof_grade": "contract_only",
      "finality": "not_final",
      "current_citation": "symbol-index gate specified; physical RS symbol still open"
    },
    {
      "id": "GEN-COUNT",
      "status": "open",
      "proof_grade": "open_none",
      "finality": "not_final",
      "current_citation": "generation count remains open"
    },
    {
      "id": "K3-CONTROL",
      "status": "control_only",
      "proof_grade": "compact_characteristic_class_control",
      "finality": "conditional_finality_as_control",
      "current_citation": "compact K3 formulas are controls, not physical GU evidence"
    }
  ],
  "branches": [
    {
      "id": "unprojected_y14",
      "decision": "NO_GO",
      "citation": "not citable as Fredholm physical index"
    },
    {
      "id": "projected_weighted_y14",
      "decision": "CONDITIONAL_OPEN",
      "citation": "citable only as a conditional analytic route"
    },
    {
      "id": "unitary_discrete_bridge",
      "decision": "UNDERDEFINED",
      "citation": "not citable until U and compact homotopy are supplied"
    },
    {
      "id": "aps_bridge",
      "decision": "UNDERDEFINED",
      "citation": "not citable until physical boundary operator and corrections are supplied"
    },
    {
      "id": "raw_compact_k3",
      "decision": "CONTROL_ONLY",
      "citation": "citable as compact control arithmetic only"
    }
  ]
}
```

## 2. Bridge Stages And Data Payload

The bridge has to move physical index data, not just names.

| stage | input payload | output payload | current transport status |
|---|---|---|---|
| Physical RS complex | GU-derived RS field bundle, gamma-trace maps, gauge maps, gauge fixing or BRST ghosts, `sigma_RS^phys` | physical symbol or elliptic-complex class to be indexed | underdefined: raw K3 class exists, physical GU class does not |
| Tau/discrete projection | full noncompact split-signature `Y^14` carrier with continuous spectrum | finite-multiplicity projected tau-discrete/residual sector | underdefined: scalar sector is empty; tau-twisted RS sector is unproved |
| Weighted Sobolev closure | formal projected operator | closed right-`H` operator on `W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}` | conditional: needs bounded `P_disc`, weight window, rank-3 end calculus, compact-remainder parametrix |
| Bounded transform | closed Fredholm family | `F_x = D_x(1+D_x^*D_x)^(-1/2) : X -> Fred_H(K_H)` | underdefined: pointwise Fredholmness does not imply norm-continuous family |
| Compactification/APS or unitary K3 reduction | projected weighted `Y^14` physical problem | compact K3 physical problem, or APS boundary problem with correction terms | underdefined: no `H`-unitary `U` or physical APS boundary operator is supplied |
| H-linear structure | ambient `Cl(9,5) ~= M(64,H)` and `Sp(64)` algebra | global H-linear Fredholm index and KSp family | partially preserved algebraically, underdefined globally for all maps and the pulled-back connection |
| Background/ch2 | internal `F = s^*S(6,4)` | `n = rank_C(F) = 16`, `k = ch_2(F)[K3]` | underdefined: `k` is not fixed by the physical background; `k=0` would be imported unless proved |
| Eta/spectral flow | boundary/end/family variation data | `-(eta+h)/2 + SF_bridge + C_end` correction package | corrected if computed; currently uncomputed and therefore lost if ignored |
| Generation readout | physical `ind_H(D_RS^phys)` plus spin-1/2 and additivity gates | Candidate A/B/other generation readout | underdefined: no readout is allowed until the physical H-index and bridge close |

Two global rules follow.

First, the compact K3 raw arithmetic can preserve characteristic-class
bookkeeping only after the physical symbol class is known. It does not by
itself preserve physical `Y^14` kernel/cokernel data.

Second, any route that removes the noncompact end must either prove lossless
unitary transport or pay the correction bill. Unpaid end data is lost data.

## 3. Loss Ledger Table

| stage | datum | class | ledger entry |
|---|---|---|---|
| Physical RS complex | Name "Rarita-Schwinger" | preserved | The name and broad field type survive across notes, but this is not enough for an index theorem. |
| Physical RS complex | Gauge-fixed/BRST physical symbol | underdefined | Current files do not derive the physical GU RS elliptic complex from the actual typed GU operator/action. |
| Physical RS complex | Raw K3 gamma-trace-free class `E_raw` | imported | It is a compact control class unless the physical GU complex is proved to reduce to it. |
| Physical RS complex | BRST-style class `E_BRST_style` | imported | It is a comparison class until the two spinor ghost/subtraction complexes are derived from GU. |
| Tau/discrete projection | Continuous noncompact sector | lost | Projection intentionally discards it; this is acceptable only if the physical problem is the projected sector. |
| Tau/discrete projection | Scalar discrete sector | lost | The scalar `SL(4,R)/SO_0(3,1)` route has no scalar discrete series in the current notes. |
| Tau/discrete projection | Tau-twisted RS discrete/residual sector | underdefined | The nonempty finite sector is the open representation-theoretic gate. |
| Tau/discrete projection | H-linearity of the projection | preserved | Algebraically plausible from `Cl(9,5)` and `Sp(64)`, but it still has to be part of the projection theorem. |
| Weighted Sobolev closure | Weight choice `delta` away from walls | corrected | The raw operator is replaced by a weighted conjugate to avoid indicial/Plancherel walls. |
| Weighted Sobolev closure | Full unprojected Fredholmness | lost | Split signature and continuous spectrum block ordinary full `Y^14` Fredholmness. |
| Weighted Sobolev closure | Compact-remainder parametrix | underdefined | Needs bounded `P_disc`, end calculus, normal/indicial invertibility, finite kernel/cokernel. |
| Weighted Sobolev closure | Rank-3 A3 corner control | underdefined | Single-face b-calculus is not enough for the full fiber end. |
| Bounded transform | Pointwise index | preserved | If the operator is Fredholm, the bounded transform has the same Fredholm index. |
| Bounded transform | Family KSp class | underdefined | Requires common domains, unitary trivialization, uniform gap/control, and norm continuity. |
| Bounded transform | Zero crossings | corrected | Crossings require spectral sections or spectral-flow terms; otherwise projection data can jump. |
| Compactification/APS or unitary K3 reduction | K3 topological invariants | imported | `Ahat(K3)=2`, `p1=-48`, `chi=24`, `sigma=-16` are compact model data. |
| Compactification/APS or unitary K3 reduction | Physical noncompact kernel/cokernel | underdefined | No proved `U` or APS theorem identifies it with compact data. |
| Compactification/APS or unitary K3 reduction | End geometry | lost | The closed K3 bulk forgets the noncompact end unless APS/end corrections are supplied. |
| H-linear structure | Ambient right-`H` module | preserved | The local algebra `Cl(9,5) ~= M(64,H)` preserves right-`H` structure. |
| H-linear structure | Global H-index conversion | underdefined | Halving a complex index requires the pulled-back connection, symbol, projection, and bridge maps to be H-linear. |
| Background/ch2 | Complex rank `n=16` | preserved | The expected rank of `F=s^*S(6,4)` is stable as a bookkeeping input. |
| Background/ch2 | `k = ch_2(F)[K3]` | underdefined | The physical `Sp(64)` background has not fixed it. |
| Background/ch2 | Flat branch `k=0` | imported | It is a special assumption unless the actual GU background proves flat/trivial `F`. |
| Eta/spectral flow | Closed K3 no-boundary term | preserved | Closed K3 has no APS term internally. |
| Eta/spectral flow | Noncompact boundary/end correction | corrected | APS routes require `-(eta+h)/2`, plus spectral-flow and end terms if present. |
| Eta/spectral flow | Imported old eta cancellations | lost | Eta values for other boundary operators do not compute the physical RS correction. |
| Generation readout | Candidate comparison values | preserved | `I=8` and `I=16` remain comparison labels after an independent physical H-index exists. |
| Generation readout | Target values as inputs | lost | They must be discarded as inputs; using them triggers `INVALID_CIRCULAR`. |
| Generation readout | Current generation-count evidence | underdefined | The physical index and bridge are still open, so no generation readout is allowed. |

## 4. Promotion Rule: When K3 May Be Cited As Physical GU Index Evidence

K3 may be cited as physical GU generation-count evidence only after all of the
following promotion fields are closed.

| field | required proof object | current state | failure decision |
|---|---|---|---|
| Physical RS complex | GU-derived gauge-fixed operator or elliptic BRST complex with all bundles, maps, and symbol conventions | underdefined | `OPEN_MISSING_SYMBOL_DATA` |
| Tau/discrete projection | nonempty finite tau-twisted RS sector, `P_disc` H-linear, bounded on weighted `L^2` and `W^{1,2}`, invariant modulo compact terms | underdefined | `NO_GO_EMPTY_OR_UNBOUNDED_SECTOR` |
| Weighted Fredholm parametrix | compact-remainder parametrix with finite right-`H` kernel/cokernel and weight away from walls | underdefined | `OPEN_WEIGHTED_FREDHOLM_PARAMETRIX` |
| Bounded transform family | norm-continuous `X -> Fred_H(K_H)` family with common domains or unitary trivialization | underdefined | `UNDERDEFINED_FAMILY_KSP_CLASS` |
| K3 reduction or APS map | either an H-unitary discrete-mode map `U` intertwining operators modulo compact homotopy, or an APS compactification for the same physical operator | underdefined | `UNDERDEFINED_BRIDGE_MAP` |
| Symbol-class match | proof that K3 class is the reduction of the physical `Y^14` class, not merely another RS class | underdefined | `OPEN_MISSING_SYMBOL_DATA` |
| Right-H certificate | global right-`H` structure preserved by connection, symbol, projectors, ghosts, and bridge/boundary maps | underdefined | `COMPLEX_ONLY_H_STRUCTURE_MISSING` |
| Background `ch_2(F)` | physical value of `k = ch_2(F)[K3]`, or proof that the result is independent of it | underdefined | `OPEN_BACKGROUND_DEPENDENT` |
| Eta/spectral flow/end terms | `eta(A_RS^phys)`, `h(A_RS^phys)`, `SF_bridge`, and `C_end` computed or proved zero for the same operator | underdefined | `APS_CORRECTION_UNCOMPUTED` |
| Noncircular readout | no use of `ind_H(D_RS)=8`, `ind_H(D_GU)=24`, `rank_eff=4/8`, three generations, or physical DOF count as inputs | guard active | `INVALID_CIRCULAR` if violated |

Only after these fields close may the K3 physical RS index be compared with
the generation-count convention:

```text
I = ind_H(D_RS^phys)
I = 8   -> Candidate A comparison
I = 16  -> Candidate B comparison
else    -> OTHER_INDEX comparison
```

If the result is background-dependent, complex-only, non-elliptic, missing a
bridge, or corrected by uncomputed APS/end data, K3 cannot be promoted.

## 5. Claim Certificate Table For RS-SYMBOL, GEN-COUNT, And K3-CONTROL

| claim | status | proof grade | finality | current certificate | closure condition | forbidden citation |
|---|---|---|---|---|---|---|
| `RS-SYMBOL` | `specified_open` | `contract_only` | `not_final` | The symbol-index gate is specified. The raw K3 and comparison formulas are controls. The physical GU RS symbol is still missing. | Derive physical gauge-fixed/BRST complex, prove ellipticity, identify K-theory class, compute index with H and background certificates. | "The RS index is 8" or "the K3 raw class is the physical GU class." |
| `GEN-COUNT` | `open` | `open_none` | `not_final` | No physical generation-count claim follows from current K3 data. | `RS-SYMBOL` returns an independent H-index, then spin-1/2 additivity and normalization are applied without target insertion. | "K3 proves three generations" or "total GU index is 24" as a settled result. |
| `K3-CONTROL` | `control_only` | `compact_characteristic_class_control` | `conditional_finality_as_control` | K3 computes compact raw/control formulas such as `-38 n + 5 k` and comparison formulas such as `-42 n + 3 k`. | Promote only if a bridge theorem proves the compact physical class equals the projected `Y^14` physical class with all corrections included. | "Compact K3 control arithmetic is physical GU evidence." |

## 6. Branch/Bridge Robustness Table

| branch or bridge | current decision | what survives | what fails or is lost | robustness | allowed citation |
|---|---|---|---|---|---|
| Unprojected `Y^14` | `NO_GO` as current Fredholm route | right-`H` algebraic carrier survives | full Fredholmness is lost to split-signature null cone and noncompact continuous spectrum | robust negative against compact elliptic import | not citable as a physical Fredholm index |
| Projected weighted `Y^14` | `CONDITIONAL_OPEN` | possible physical noncompact route if tau-discrete sector is real and bounded | scalar discrete route fails; tau RS sector, bounded `P_disc`, parametrix, and family continuity remain open | branch-local and promising but not closed | citable only as a conditional analytic route |
| Unitary discrete bridge | `UNDERDEFINED` | would preserve kernel/cokernel and H-index if `U` exists and intertwines modulo compact homotopy | no finite-rank normalized mode bundle or H-unitary operator has been supplied | high value, zero current proof grade | not citable until `U` and compact homotopy are explicit |
| APS bridge | `UNDERDEFINED` | can correct end loss by `bulk - (eta+h)/2 + SF + C_end` | physical RS boundary operator, eta, kernel, spectral flow, and end terms are not computed | viable but correction-heavy | not citable until corrections are for the same operator |
| Raw compact K3 | `CONTROL_ONLY` | compact characteristic-class arithmetic is robust; K3 invariants are fixed | noncompact end, physical symbol, projection, H certificate, and background `k` are not transported | robust as control, weak as physical evidence | citable as compact control arithmetic only |

## 7. First Exact Missing Proof Object

The first missing proof object is the typed physical GU RS complex.

It must be an object, not prose:

```text
RS_GU^phys =
  (E_RS^+, E_RS^-,
   G_+, G_-,
   P_+, P_-,
   gauge maps,
   gauge condition or BRST ghost complex,
   sigma_RS^phys(xi),
   H-structure certificate,
   GU source operator/action branch)
```

This object must say whether it comes from the actual `D_GU`, the current
`D_roll` proposal, or a deliberately branched comparison operator. Without it,
there is no way to know whether the compact K3 symbol should be `E_raw`,
`E_BRST_style`, or a third class. That means every later bridge step would be
transporting an unnamed payload.

The first bridge-specific proof object after that is:

```text
P_disc theorem for the same RS_GU^phys:
  nonempty finite tau-twisted sector,
  H-linear projection,
  weighted Sobolev boundedness,
  invariance modulo compact terms,
  compact-remainder parametrix,
  family stability or spectral-flow accounting.
```

If this object fails because the tau-twisted sector is empty, K3 remains a
separate compact control model. If it succeeds, the unitary or APS bridge can
be meaningfully attempted.

## 8. Next Meaningful Proof/Computation Step

The next useful step is a proof packet with one positive or negative decision:

1. Derive `RS_GU^phys` from the typed GU operator/action and identify its K3
   symbol class. Decide whether the class is `E_raw`, `E_BRST_style`, or a
   third virtual class.
2. Keep `k = ch_2(F)[K3]` symbolic unless the physical `Sp(64)` background
   fixes it, and certify the right-`H` conversion before reporting an H-index.
3. In parallel, prove or refute the tau-twisted `P_disc` theorem for that same
   physical complex. Do not use compact K3 kernel counts as proof of the
   noncompact discrete sector.
4. Choose exactly one bridge route: an H-unitary discrete-mode reduction `U`,
   or an APS compactification with the physical RS boundary operator and
   computed `eta`, `h`, spectral-flow, and end terms.
5. Only after those objects exist, run the generation readout as a comparison
   layer. If the independent result is neither 8 nor 16, report
   `OTHER_INDEX`; if it is background-dependent or complex-only, do not
   compare it as a physical generation count.

This is intentionally narrower than "do more K3 arithmetic." The arithmetic is
already a good control. The missing work is the transport certificate.
