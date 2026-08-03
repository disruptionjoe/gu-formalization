---
artifact_type: exploration
status: exploration
doc_type: lemma-note
created: 2026-08-03
work_item: M-M1
register: lab/process/improvement-register-2026-08-03.md
panel_refs:
  - "lab/process/eleven-lens-audit-2026-08-03.md (What held up: MOVE-4's dim Hom = 0; B1 for the (9,5)/(7,7) fork)"
  - "lab/process/improvement-register-2026-08-03.md (M-M1, rep-lens item R7/RT-O1)"
title: "M-M1 signature-independent scalar-vanishing lemma: for ALL signatures (p,q) with p+q = 2 mod 4, dim Hom(S+ (x) S+, Lambda^0) = 0 — two-line proof (omega^T = -C omega C^{-1} at n=14; equivalently -w_0 swaps the D_m spin nodes for m odd, so (S+)* = S-). Corollary: NO signature choice at n=14 supplies a same-chirality scalar (Majorana-mass) channel; MOVE-4's fact A is immune to the (9,5)/(7,7) fork."
grade: "EXACT / structural — complexified representation theory, no numerics load-bearing; generalizes (does not replace) the standing case-sweep certificates; Lean-able per the register row"
claim_status_change: none
canon_verdict_change: none
depends_on:
  - canon/two-arena-rep-theory-core-RESULTS.md
  - canon/shiab-existence-cl95.md
  - tests/big-swing/R4_spin95_hom_vanishing.py
  - tests/chase/MOVE-4/move4_spinor_square_forms.py
outcome: "Lemma proved (two independent one-line arguments); session numeric spot-check exact (0.0) at n=10,14 with n=8,12 positive controls; fact A promoted from case-swept to structurally signature-independent in scope of citation, with no claim-status change"
---

# M-M1 — the signature-independent scalar-vanishing lemma

**What this is.** The register's M-M1: the two-line structural proof that
replaces (by generalizing) the 4-case sweep behind fact A of
`canon/two-arena-rep-theory-core-RESULTS.md` — and immunizes the MOVE-4 fact
against the signature fork the audit re-opened (B1: (9,5) vs (7,7) is
UNDER-DETERMINED). Nothing here changes a claim; the vanishing was already
canon. What is new is that it holds for **every** signature at once, so the
fork cannot touch it.

## Lemma

Let n = p + q with n ≡ 2 (mod 4), and let S± be the complex chiral (half-)
spinor modules of Spin(p,q). Then

```text
dim_C Hom_{Spin(p,q)}(S+ (x) S+, Lambda^0) = 0     for EVERY signature (p,q),
```

and likewise for S- (x) S-. For n ≡ 0 (mod 4) the same space has dimension 1
(the same-chirality scalar EXISTS — this is the control direction).

## Proof (two lines, two independent forms)

**Clifford form.** Complexify: every so(p,q) with p + q = n has the same
complexification so(n,C), acting through the same complexified Clifford
algebra Cl(n,C), on the same S±; a nonzero real invariant would complexify to
a nonzero complex one, so it suffices to work over C, where the signature has
disappeared. Let C be a transpose intertwiner, gamma_a^T = eps C gamma_a
C^{-1}. Then for the volume element omega = z gamma_1 ... gamma_n (normalized
omega^2 = +1):

```text
omega^T = eps^n (-1)^{n(n-1)/2} C omega C^{-1} = (-1)^{n/2} C omega C^{-1}
        = -C omega C^{-1}   at n = 14  (n = 2 mod 4),
```

since eps^n = 1 for n even and (-1)^{n(n-1)/2} = (-1)^{n/2}. Hence
C P± C^{-1} = (P∓)^T for the chirality projectors P± = (1 ± omega)/2, and
every invariant scalar bilinear (they are exactly s,t -> s^T C' t with
C' in {C, C omega}) restricts to same-chirality blocks as

```text
P+^T C' P+ = C' P- P+ = 0.        QED
```

**Weyl-group form.** n = 2m with m odd (n ≡ 2 mod 4) is exactly the case
where the longest Weyl element of D_m satisfies w_0 ≠ -1: -w_0 is the diagram
automorphism swapping the two spin nodes. The dual of the irrep with highest
weight lambda is the irrep with highest weight -w_0(lambda), so
(S+)* ≅ S-. Therefore

```text
Hom(S+ (x) S+, Lambda^0) = Hom(S+, (S+)*) = Hom(S+, S-) = 0   (Schur). QED
```

For m even, w_0 = -1, (S±)* ≅ S±, and the dimension is 1 — which is why the
Cl(4,0)/Cl(8,0) controls in `tests/big-swing/R4_spin95_hom_vanishing.py`
correctly return 1.

**Real-form remark.** The vanishing bounds every real Hom space too:
Hom_R(A,B) (x) C = Hom_C(A_C, B_C), so the real chiral modules S±_R of
Cl(9,5) = M(64,H) (dim_R 128, quaternionic type, S±_R (x) C ≅ 2 S±_C) also
carry no invariant same-chirality scalar — the quaternionic structure cannot
resurrect a real invariant where the complex count is 0.

## Corollary (the fork immunity)

At n = 14, **no** signature choice — (9,5), (7,7), (13,1), (11,3), any (p,q)
with p + q = 14 — supplies a same-chirality scalar (Majorana-mass) channel
inside the Spin-equivariant family. The audit's re-opened signature
under-determination (B1; W202/H19: (9,5) vs (7,7) UNDER-DETERMINED) therefore
cannot touch MOVE-4's fact: the heavy-Majorana absence recorded at
`canon/shiab-existence-cl95.md` (CORRECTION SHIAB-05) and as fact A of
`canon/two-arena-rep-theory-core-RESULTS.md` is signature-independent, not a
(9,5) accident. Resolving the fork will change other things (the Kramers
wall, the real family dimensions); it cannot change this channel count.

Bookkeeping note, matching SHIAB-05's minor note: both invariant bilinears
C and C omega (the Lambda^0 and Lambda^14 channels) vanish on same-chirality
blocks — the "Lambda^0 dim = 2" intermediate is Lambda^0 + Lambda^14, and
both summands are off-diagonal.

## Relation to the standing evidence (what this does and does not replace)

The citable machine evidence is unchanged and stays where it is:

- `tests/big-swing/R4_spin95_hom_vanishing.py` (fact A certificate): explicit
  Cl(9,5) in two gamma bases, second signature Cl(7,7), controls
  Cl(4,0)/Cl(8,0) returning 1, exact-integer weight cross-check.
- `tests/chase/MOVE-4/move4_spinor_square_forms.py` (SHIAB-05 certificate):
  chirality-block support of the invariant bilinear space on the 128-dim rep,
  hard checksum 16384 = 128^2, errors 0.00e+00.

This note upgrades the *scope* of what those certificates witness: the sweep
sampled cases; the lemma covers every (p,q) with p + q = 14 (and every
n ≡ 2 mod 4) structurally. The sweep remains the executable regression; the
lemma is the reason it could never have come out otherwise. Register flag: the
Weyl-form argument is short enough to be Lean-able (optional, not done here).

## Session verification (spot-check, not a committed certificate)

Session script (scratchpad, `_local/cas-venv` python, exit 0): Jordan-Wigner
gammas, explicit transpose intertwiner C = product of the antisymmetric
gammas, no metric eta anywhere (purely complexified objects):

```text
n= 8: omega^T = +C omega C^{-1}; P+^T C P+ != 0   (control: scalar exists)
n=10: omega^T = -C omega C^{-1}; ||P+^T C P+|| = ||P-^T C P-|| = 0.0 exactly
n=12: omega^T = +C omega C^{-1}; P+^T C P+ != 0   (control: scalar exists)
n=14: omega^T = -C omega C^{-1}; ||P+^T C P+|| = ||P+^T C omega P+|| =
      ||P-^T C P-|| = 0.0 exactly; ||P+^T C P-|| = O(10) (off-diag channel live)
```

The zeros are exact floating-point zeros (the JW matrices have entries in
{0, ±1, ±i} and the products never mix into the same-chirality blocks). The
committed regressions above are the durable evidence; this run is a
consistency check of the lemma's signs.

## Layer-0 fence / scope

This note counts channels in an equivariant family. It derives no generation
count, selects no operator, and moves no verdict (`claim_status_change:
none`). It strengthens the *robustness* of an existing canon fact against the
open signature fork; the fork itself (register M-H4) remains open and is not
addressed here.
