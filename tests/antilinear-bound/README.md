# WC-ANTILINEAR-BOUND verification scripts (2026-07-02)

Executable certificates for the antilinear-bound work card (NEXT-STEPS.md, 2026-07-02
publication-gating section, priority 2): convert the located-not-forced paper's antilinear
"finite adversarial hunt" (caveat (d)) into a delimited theorem/certificate.
RESULTS: `canon/antilinear-bound-RESULTS.md`.

## Verdict

**The hunt closes over a delimited class S, and the closure is a theorem, not a search.**
S = all antilinear operators `C = M . conj` on the 192-dim carrier with
`M^dag K M = lambda K-bar`, `lambda` real nonzero (Krein-compatibility = the antiunitary
condition = ghost-pairing compatibility) -- **no symmetry, frame, square, or continuity
assumption**.  The index-nullity theorem: every `C` in S maps the chirality pair to a
K-Lagrangian pair, so **every physical subspace keeps net chiral index exactly 0** under
every re-grading in S.  The hunted operator (frame-non-trivial antilinear CII swap)
**exists** in S -- constructed in closed form -- and still forces nothing.  Outside S,
admissibility itself fails (non-Krein antilinear operators do not act on physical states).
No CANON.md promotion (pauses for Joe).

| script | what it certifies | runtime | key numbers |
|---|---|---|---|
| `antilinear_ladder_census.py` | the declared symmetry-breaking ladder: full antilinear intertwiner space per rung, preserve/swap split, frame charges, strict-admissibility analysis with exact certificates | ~39 s (or `ANTI_STAGE=1`/`2` split) | swap dims 0/0/0/0/0 at L0/L2/L2b/L3/L4 (proof); 2 at L1/L1b (frame-trivial by equivariance, strict admissibility NON-EXISTENCE by exact C5 certificate); 4 at L5 (frame-active); 36 asserts |
| `antilinear_symmetry_free_bound.py` | the index-nullity theorem on S + closed-form strict witnesses (all four `(C^2, lambda) = (+-1, +-1)` sign patterns, incl. the AZ-CII shape), Krein-unitary dressings, sharpness of the S-boundary, D1-style continuity control | ~2 s | isotropy transport 3e-14; `chi_C(P) = 0` exact for 8 operators x 4 physical subspaces; outside-S control maps physical to indefinite Gram; 133 asserts |
| `verify/indep_check.py` | independent re-check: own gammas (recursive doubling), different (9,5) embedding, different seed, Gram-eigenvalue ranks, exact integer weight/Clebsch prediction of the full census table, Cl(7,7) cross-signature, Euclidean (14,0) premise-failure control | ~4 s | predicted table == census table (integers); L1 C5c non-existence reproduced; (7,7) theorem holds; (14,0) control fires `|chi| = 96`; 78 asserts |

## The ladder (declared rungs; subalgebras of the sector's g = so(4) (+) so(5,5))

| rung | algebra | anti dim | swap dim | frame charge of swaps | decision |
|---|---|---|---|---|---|
| L0 | so(4)+so(5,5) | 2 | 0 | -- | proof (re-verifies enum-completeness) |
| L2 | so(3)+so(5,5) | 4 | 0 | -- | proof |
| L2b | so(5,5) alone | 72 | 0 | -- | proof (+ monotonicity closes all rungs containing so(5,5)) |
| L3 | so(4)+t5(split Cartan) | 32 | 0 | -- | proof (split weights are conjugation-fixed) |
| L4 | t2+t5 (Cartan only) | 192 | 0 | -- | proof |
| L1 | so(4)+so(5,4) | 4 | 2 | 0 (forced by equivariance) | swaps exist, frame-trivial; strict (C^2=+-1 AND Krein) admissibility: NON-EXISTENCE (exact C5 certificate) |
| L1b | so(4)+so(4,5) | 4 | 2 | 0 (forced) | same as L1 |
| L5 | so(3)+so(5,4) | 8 | 4 | ~ 20 (frame-ACTIVE) | swaps exist and are frame-active; strict admissibility not found (search-grade); rung closed by the index-nullity theorem |
| L6 | symmetry-free | full space | -- | arbitrary | index-nullity THEOREM on S (companion script) |

## Running

Python 3.10+, numpy only (no scipy).  From the repo root:

```
python tests/antilinear-bound/antilinear_ladder_census.py
python tests/antilinear-bound/antilinear_symmetry_free_bound.py
python tests/antilinear-bound/verify/indep_check.py
```

On sandboxes that cap process lifetime, the census splits: `ANTI_STAGE=1` then
`ANTI_STAGE=2` (checkpoint in the system temp dir; results identical).

## Grades (honest)

- **Proof-grade (5-line linear algebra, premises machine-certified)**: the index-nullity
  theorem on S; the isotropy-transport lemma; the definiteness-transport corollary
  (class-S operators map physical subspaces to (+/-)-definite subspaces, never onto the
  K-null selections where the vectorlike +-96 lives).
- **Exact integer arithmetic**: the V1 weight/Clebsch prediction of the whole census table;
  the 16/16bar weight disjointness (split form) and B4-restriction identity.
- **Computed + independently re-verified** (machine-precision certificates, residuals
  1e-12..1e-15, spectral gaps O(1)+): the per-rung Hom censuses, swap splits, frame
  charges, the C5 closed-form admissibility certificates at L1/L1b.
- **Search-grade (flagged, not load-bearing)**: strict (A2 AND A3) admissibility at L5
  found nothing in 120 deterministic Gauss-Newton starts; the rung's closure does NOT
  depend on it (index nullity covers it).
- **None of this is a physics derivation of GU**; it bounds what the sector's antilinear
  operators can do to a chiral count.

## The one surprise (reported, not patched)

The paper's hunt looked for a frame-non-trivial antilinear chiralizer and found none.  The
bound shows WHY, and it is not scarcity: once all symmetry is dropped, admissible
frame-active CII swap operators exist **in abundance** (closed-form construction, all four
sign patterns).  What the hunt was really detecting is the theorem: **Krein compatibility
alone pins every physical subspace's net chiral index at 0**, so no admissible antilinear
operator -- found or unfound -- was ever going to force a count.  The correct formalization
of Krein-antiunitarity for antilinear operators (`M^dag K M = lambda K-bar`, not
`lambda K`; K is genuinely complex on this carrier) was caught and fixed during this pass.
