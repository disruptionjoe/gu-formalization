---
artifact_type: exploration_result
doc_type: exact_topology_control
created: 2026-08-26
status: exploration
claim_verdict: FRAMING_RELATIVE_NOT_LENS_SPACE_INVARIANT
title: "Kirby--Melvin all-lens control: signature defect and 3-primary framing class are different typed objects"
grade: "EXACT arithmetic and standard-result-applied topology at the stated scope. The Kirby--Melvin/Rademacher defect formula, Dedekind reciprocity, honest-framing affine action and stabilization shift are exact. The repository's chosen RP3 tangential framing remains standard-result-applied; its identification with GU's self-dual twist remains reconstruction-dependent."
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
row_change: M-M27_EXECUTED_AT_FRAMING_TYPING_CEILING
scripts:
  - tests/channel-swings/kirby_melvin_lens_framing_three_primary_control.py
---

# Kirby--Melvin all-lens control

## Result

The M-M27 adversarial question, “is the nonzero 3-primary part special to
`p=2`?”, is not a question about the unframed lens space `L(p;q)`. It is a
question about a **chosen stable framing**. Kirby--Melvin and Rademacher give
an all-lens formula for the universal-cover signature defect,

`defect(L(p;q)) = 4 p s(q,p)`,

but that manifold/cover quantity is not the Adams `e`-invariant of an
unspecified framing. On a fixed spin 3-manifold, honest framings form an affine
`Z`-space. Adding the honest generator `rho` stabilizes to `2 sigma`, shifting
the stable class by `2 in Z/24`; modulo `3`, three successive shifts visit all
three residues. Therefore the same lens space and spin structure admits
framings with both zero and nonzero 3-primary projection.

This does not retract the filed result for the particular self-dual tangential
framing on `RP3=L(2;1)`: that chosen framing still has `p1=4`,
`e_R=1/12`, and stable class `2 mod 24`. It does reject any inference that its
nonzero 3-primary part is a property of `L(2;1)` alone, or that a table of
signature defects for `L(p;q)` can answer the framing-class question without a
framing column.

Scope: stable-framing arithmetic and lens-space signature defects only. No GU
class map, family-count bridge, source action, operator, index, anomaly phase,
prediction, canon verdict or public posture is changed.

```gu-typed-objects
result: the all-lens signature defect is separated from the chosen framing class, and the framing orbit reaches every Z/3 residue on each fixed spin lens space
carrier: spin three-manifold L(p;q) together with an explicitly chosen stable framing LAYER=toy CHIRALITY=N/A
pairing: NONE
real_structure: spin structure fixed while the honest framing varies in its affine integer orbit
grading: stable class in pi_3^S=Z/24 with separately computed Z/3 projection
action_owner: repository-construction
target: distinguish universal-cover signature defect from framing-relative stable class MAP-TYPE=not-a-map
```

## Preflight bookend

### Object and claim typing

- `L(p;q)`: oriented lens space, `p>0`, `gcd(p,q)=1`.
- `s(q,p)`: rational Dedekind sum.
- `4 p s(q,p)`: signature defect of the universal cover in the
  Kirby--Melvin/Hirzebruch normalization.
- `phi`: a chosen framing compatible with a fixed spin structure.
- `[phi] in pi_3^S=Z/24`: stabilized framed-bordism class.
- `e_R(phi) in Q/Z`: Adams real `e`-invariant of the chosen framing.
- Claim ceiling: type and compute these objects separately; do not infer an
  integer family count or GU class realization.

### Retrieval and correction history

The object search found the existing filed chain in
`canon/final-verdict-generation-count-and-the-open-bridge.md`: for the chosen
right-handed/self-dual tangential framing on `RP3`, `p1=4`, hence
`e_R=p1/48=1/12` and class `2 mod 24`. Existing big-swing artifacts repeatedly
mark the Kirby--Melvin normalization as formerly from-memory and preserve the
open bridge to a GU operator/index.

Primary custody was checked against:

- Rob Kirby and Paul Melvin, “Dedekind sums, mu-invariants and the signature
  cocycle,” *Math. Ann.* 299 (1994), 231--267,
  DOI `10.1007/BF01459782`, especially the Rademacher cotangent formula and
  `4 p s(q,p)` signature-defect identification.
- Rob Kirby and Paul Melvin, “Canonical framings for 3-manifolds,” *Turkish
  J. Math.* 23 (1999), 89--115, arXiv `math/9903056`, especially the affine
  framing action, stabilization `rho -> 2 sigma`, and the `L(p;1)` examples.

The first source-supported distinction is decisive: the papers compute both
framing-dependent and manifold-dependent quantities, but never license their
identification without a named framing.

### Routes considered

1. **Raw finite table.** Rejected as primary: it can illustrate the formula but
   cannot decide a universal typing question.
2. **Dedekind reciprocity plus affine framing action.** Selected: it yields an
   all-`p,q` formula and a general proof of framing dependence.
3. **Compute only `L(p;1)`.** Retained as a positive control because the closed
   form `(p-1)(p-2)/3` is primary-source explicit, but dominated as the final
   route.
4. **Treat `e_R` as a lens-space invariant.** Rejected as a category error: an
   `e`-invariant requires the framed class.

## Exact computation

The certificate evaluates the sawtooth definition

`s(q,p)=sum_{k=1}^{p-1} ((k/p))((qk/p))`

with `Fraction` arithmetic. It establishes:

1. `4 p s(1,p)=(p-1)(p-2)/3` for every tested `p=2..24`;
2. orientation reversal `q -> -q` reverses the defect;
3. Dedekind reciprocity holds exactly for every coprime pair through `p=17`;
4. `L(2;1)` has signature defect zero, while its **chosen framing** has
   `e_R=1/12`--a direct nonidentity witness;
5. the framing orbit `c -> c+2k mod 24` reaches residues `0,1,2 mod 3` for
   every base class `c`; and
6. the same `RP3` framing orbit contains class `2` (nonzero 3-primary) and
   class `6` (zero 3-primary).

The exact control table contains all 45 coprime `L(p;q)` labels for
`2<=p<=12`; the table is a reproduction control, not the proof of the general
statement.

## Postflight hostile review

### Strongest overclaim

“Every lens space has arbitrary 3-primary topology” is too broad. The result
is that every **framing orbit on a fixed spin lens space** reaches every
`Z/3` residue after stabilization. It says nothing about an unframed
manifold's intrinsic torsion or a GU-selected framing.

### Strongest contrary construction

A source/action-owned rule could select one distinguished framing on every
`L(p;q)`. That would make a table meaningful for that rule. No such family of
selected framings is supplied here; the existing `RP3` reconstruction names
one particular framing only.

### Weakest reproducibility seam

The load-bearing normalizations are the source formulas `defect=4ps(q,p)` and
`rho -> 2 sigma`. The self-test corrupts the factor four, the stabilization
shift, and the primary projection separately. All four planted corruptions
reach genuine failing assertions rather than crashes.

### Final disposition

M-M27 is executed at the exact typing ceiling:

- the all-lens signature-defect formula is reproduced;
- 3-primary support is proved framing-relative, not `p=2`-specific or even
  lens-space-determined; and
- the filed `RP3` chosen-framing result survives unchanged.

Reopen only with a source/action-owned rule selecting a specific framing
family on general `L(p;q)` and a typed map from that family to the GU carrier.

## Reproduction

```text
_local/cas-venv/bin/python \
  tests/channel-swings/kirby_melvin_lens_framing_three_primary_control.py \
  --selftest
```

Result: `13/13` exact checks and `4/4` planted mutations caught; exit `0`.
