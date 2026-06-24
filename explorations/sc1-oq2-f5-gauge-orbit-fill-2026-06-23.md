---
title: "SC1-OQ2 F5: Explicit CAS/Structural Check of Whether the Sp(64) Gauge Orbit Fills the Null-Mode Space NM(xi) at Null Characteristics"
date: 2026-06-23
problem_label: "sc1-oq2-f5-gauge-orbit-fill"
status: reconstruction
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: 2026-06-23
verdict_change_reason: "CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION (critical): this file explicitly NAMES an internal contradiction in the sibling lemma (§4: 'parts (ii) and (iii) are mutually inconsistent') and RESOLVES it in the SAME session (2026-06-23). Per the loop's RESOLVED-blocking rule (process/loop-adversarial-log.md: 'an explicit internal contradiction in the body of a file is an open problem; block CLOSED or RESOLVED verdicts until the contradiction is resolved IN A SUBSEQUENT SESSION' — same-session self-resolution does not count), a same-session-named-and-resolved contradiction caps the verdict at OPEN. The gauge-orbit-fill ('opposite to the prior split-signature ellipticity lemma's part (iii)') is a same-session CAS result that overturns a same-session lemma; it is a strong WORKING HYPOTHESIS but is not settled. Independently, the file's own item-3 conclusion is admittedly conditional on FF3 and FF4, both OPEN at reconstruction grade. The whole NM(xi) gauge-orbit question (does the orbit fill? what is the gauge-mechanism basis of the symmetric-hyperbolic switch?) is flagged for INTER-SESSION re-derivation. The verdict is therefore OPEN, not CONDITIONALLY_RESOLVED. The kernel-trichotomy / null-projection facts this file relies on (from sc1-oq2c) are unaffected; only the gauge-orbit-fill conclusion and its symmetric-hyperbolic corollary are downgraded."
---

# SC1-OQ2 F5: Does the Sp(64) Gauge Orbit Fill NM(xi)?

> [!VERDICT OPEN — downgraded from CONDITIONALLY_RESOLVED, 2026-06-23] CORRECTION
> SC1-LEMMA-CONTRADICTION-SAME-SESSION. This file NAMES an internal contradiction in the sibling
> lemma (§4: parts (ii) and (iii) mutually inconsistent) and resolves it in the SAME session. Per the
> loop's RESOLVED-blocking rule, a same-session-named-and-resolved internal contradiction is an open
> problem until re-derived in a SUBSEQUENT session; same-session self-resolution does not count. The
> gauge-orbit-fill result (the orbit fills NM(xi), opposite to the lemma's part (iii)) is a strong
> WORKING HYPOTHESIS but is NOT settled, and the file's own conclusion is admittedly conditional on
> FF3 and FF4, both OPEN. The whole NM(xi) gauge-orbit question is flagged for inter-session
> re-derivation. The kernel-trichotomy / null-projection inputs (from sc1-oq2c) are unaffected.

## 1. Problem Statement

**What is being computed.** At a null covector xi (g_Y(xi,xi) = 0, xi != 0) the principal
symbol c(xi) of D_GU is a nilpotent of order 2 (c(xi)^2 = 0, c(xi) != 0). Its kernel is the
null-mode space

  NM(xi) = ker c(xi),    dim_R NM(xi) = dim_R E / 2.

The prior split-signature ellipticity lemma (`sc1-oq2-split-signature-ellipticity-lemma`,
part (iii)) asserted that the **Sp(64) gauge orbit is a PROPER subspace of NM(xi)** — i.e.,
that a non-trivial physical (non-gauge) quotient NM(xi)/(gauge orbit) survives at each null
covector — and flagged the remaining gate for RESOLVED as:

> "CAS verification that the Sp(64) gauge orbit does NOT fill NM(xi) (F5)."

This file is that explicit check. It is a **negative-check by discipline**: if the orbit DOES
fill NM(xi), the gauge-orbit-proper-subspace claim fails and the conclusion of the analytic
framing must be re-examined.

**Why it matters.** The claim "null modes are not all pure gauge" was the stated load-bearing
step distinguishing the **symmetric-hyperbolic / real-principal-type** framing of D_GU from an
**elliptic-modulo-gauge** framing. The lemma's logic was: gate condition fires (physical null
modes exist) => switch to symmetric-hyperbolic. The present check tests whether the premise
("gauge orbit is a proper subspace") is actually true as an algebraic fact about Cl(9,5) and
Sp(64), or whether it was asserted by an under-justified H-linearity dimension count.

**Established context this builds on:**
- `sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md` (verdict OPEN as of 2026-06-23,
  downgraded from CONDITIONALLY_RESOLVED as a result of this file): kernel trichotomy; part (ii)
  states NM(xi) = Im c(xi), maximal-rank nilpotent; part (iii) ORIGINALLY asserted the gauge orbit
  is a proper subspace of NM(xi) — that claim is now RETRACTED/FALSE (part (iii')) following the
  stress-test in this file, which named the (ii)-vs-(iii) internal contradiction. **This file
  stress-tests the original part (iii) and triggered its retraction.**
- `sc1-oq2c-null-mode-interpretation-2026-06-23.md` (CONDITIONALLY_RESOLVED): Im c(xi) = ker c(xi)
  = NM(xi) (null-projection property); F4 ("gauge orbits fill NM(xi)") listed as
  CONDITIONALLY-ruled-out pending exactly this Sp(64) orbit computation.
- `sc1-oq3-gauge-equivariance-2026-06-23.md` (RESOLVED): the physical gauge action rho of
  g in Sp(64) on S = H^{64} is LEFT matrix multiplication in M(64,H); Clifford c(xi) is ALSO
  left matrix multiplication in M(64,H). Both act on the SAME H^{64}, from the SAME side.
  Sp(64) = U(64,H) is the FULL quaternionic-unitary group, strictly larger than rho_S(Spin(9,5)).
- `anomaly-audit-cl95-gauge-group-2026-06-22.md` (RESOLVED): Cl(9,5) ~= M(64,H); sp(64) =
  anti-H-Hermitian matrices, dim_R = 8256.

---

## 2. The Precise Algebraic Question

There are three distinct candidate notions of "the gauge orbit inside NM(xi)". Pinning down
which one the elliptic-modulo-gauge question requires is the entire subtlety, so we test all
three explicitly.

**(A) BRST-exact / dynamical-gauge orbit (the correct notion for elliptic-modulo-gauge).**
The dynamical gauge symmetry of the Dirac-DeRham complex is delta_eps Psi = d_A(eps) (an
exact-form/coboundary direction). Its PRINCIPAL SYMBOL is Clifford multiplication:

  sigma(d_A(eps))(xi) = c(xi) . (rho_*(eps) applied to a generating spinor) in Im c(xi).

So the pure-gauge (BRST-exact) null modes at degree p are exactly

  Gauge_BRST(xi) = Im c(xi).

The "elliptic modulo gauge" condition is precisely: ker c(xi) = Im c(xi), i.e. the symbol
complex is EXACT at xi modulo the coboundary. The physical quotient is the symbol cohomology
H(xi) = ker c(xi) / Im c(xi).

**(B) Inner / commutator orbit.** The operator-level inner-gauge tangent used in the prior
lemma's §5.3: span over eps in sp(64) of [c(xi), rho_*(eps)] applied to NM(xi), intersected
with NM(xi). This is the subprincipal-level gauge direction.

**(C) Direct group action.** rho(eps) . NM(xi) intersected with NM(xi): whether the group can
rotate within NM. (This is a red herring — Sp(64) being a large compact group acts transitively
on spheres, so it trivially "fills" any nonzero invariant region; it is not the relevant notion.)

The decisive algebraic input is the **null-projection property** established in two prior files:

  Im c(xi) = ker c(xi) = NM(xi)    [NULL-PROJ]

This holds because c(xi) is a MAXIMAL-rank nilpotent on the irreducible Clifford module:
rank c(xi) = dim_R E / 2, and a nil-2 operator with rank = (dim)/2 has Im = ker by rank-nullity
(Im subset ker always for nil-2; equal dimensions force equality).

[NULL-PROJ] is not optional: it is the same fact the lemma uses in part (ii) and that
sc1-oq2c §2.1 derives. It immediately settles notion (A):

  Gauge_BRST(xi) = Im c(xi) = NM(xi).

**The BRST-exact gauge orbit FILLS NM(xi) identically.** There is no further computation needed
for (A): the maximal-rank nilpotency that DEFINES the null cone is exactly the statement that
the pure-gauge directions exhaust the symbol kernel.

---

## 3. Explicit CAS Check

We confirm all three notions by direct linear algebra in a faithful quaternionic realization
of the GU structure. The model is structurally exact in the load-bearing respects:

- S = H^n realized as C^{2n} via the standard quaternion -> M(2,C) left embedding.
- c(xi) = g_s + g_t with two anticommuting Clifford generators inside M(n,H): g_s^2 = +Id,
  g_t^2 = -Id, {g_s, g_t} = 0, replicated diagonally across all n quaternionic lines so that
  c(xi) is MAXIMAL-rank nilpotent (rank = n = dim_C S / 2), giving [NULL-PROJ] exactly.
- Sp(n) = U(n,H) is the FULL anti-H-Hermitian gauge algebra (dim_R = n(2n+1)), acting on the
  SAME H^n by left multiplication, exactly as in `sc1-oq3` (rho = left matrix mult, full group).

This is the genuine GU configuration (Clifford and gauge on the same module, same side, full
quaternionic-unitary group), NOT a tensor-split toy where gauge and Clifford act on disjoint
factors. (We separately ran the tensor-split toy and a full-complex u(N) toy as controls; see
§4.)

Code: `explorations/_scratch_gauge_fill_maxrank.py`, `_scratch_gauge_fill_correct.py`.

**Verified algebraic facts (n = 8, dim_C S = 16; reproduced at n = 6 and with a generic null
direction xi = 0.7 g_s + 0.7 g_t):**

  c(xi)^2 = 0 exactly;  c(xi) != 0.
  rank c(xi) = 8 = dim_C S / 2.    [maximal rank]
  Im c(xi) = ker c(xi) = NM(xi);  dim NM(xi) = 8.    [NULL-PROJ verified]
  dim_R sp(n) generators = n(2n+1) = 136, full rank in End(S).

Results for the three notions (dim of the orbit's projection into NM, out of dim NM = 8):

| Notion | Construction | dim in NM | Fills NM? |
|--------|--------------|-----------|-----------|
| (A) BRST-exact | Im c(xi) | 8 / 8 | **YES** |
| (B) commutator | span_eps [c(xi), rho_*(eps)] . NM, cap NM | 8 / 8 | **YES** |
| (C) direct action | span_eps rho_*(eps) . NM, cap NM | 8 / 8 | **YES** |

**All three notions FILL NM(xi).** The result is robust to the choice of null direction and to
n. The commutator orbit (notion B) — the very object the prior lemma claimed gave a proper
subspace — fills NM completely once the FULL Sp(64) algebra (not just the Spin(9,5) image) is
used and c(xi) has its correct maximal rank.

---

## 4. Why the Prior "Proper Subspace" Claim Failed: Three Controls

The prior lemma's part (iii) reached the opposite conclusion. The control runs isolate exactly
where its argument broke:

**Control 1 — Full complex algebra u(N) on the rolled-up complex.** Taking the gauge algebra as
all of u(N) (the over-generated case) with maximal-rank c(xi): commutator orbit fills NM. (As
expected; u(N) ⊃ sp(n).)

**Control 2 — Tensor-split toy (gauge on a disjoint internal factor).** If — counterfactually —
the gauge group acted only on an internal multiplicity index disjoint from the Clifford H-line,
and c(xi) acted only on the H-line factor, then [c(xi), rho_*(eps)] is small and the commutator
orbit is a PROPER subspace (we measured dim 2 of 10 in a non-maximal-rank instance). This is the
regime in which the lemma's "H-linearity argument" implicitly lived: it treated the gauge action
as commuting-with-Clifford on a separate factor. **But that is not the GU structure.** Per
`sc1-oq3`, gauge and Clifford act on the SAME H^{64} from the SAME side; there is no disjoint
internal factor.

**Control 3 — Non-maximal-rank c(xi).** With c(xi) acting on only a 2-line block (rank 2 of 12),
Im c(xi) is a strict subspace of ker c(xi), and the commutator orbit covers only Im c(xi)
(physical "quotient" appeared non-trivial, dim 8). **But non-maximal rank contradicts the
established null-projection property [NULL-PROJ].** The lemma asserts maximal rank in part (ii)
and then implicitly uses non-maximal-rank intuition in part (iii). That is the internal
inconsistency.

**Named internal contradiction.** The prior lemma `sc1-oq2-split-signature-ellipticity-lemma`
simultaneously asserts (ii) NM(xi) = Im c(xi) (maximal-rank null projection) and (iii) the gauge
orbit Im c(xi)-class is a PROPER subspace of NM(xi) = ker c(xi). Under (ii), Im c(xi) = ker c(xi)
exactly, so the BRST-exact gauge orbit is NOT proper — it equals NM(xi). Parts (ii) and (iii) are
mutually inconsistent. The present computation resolves the inconsistency in favor of (ii): **the
gauge orbit fills NM(xi).**

---

## 5. The Correct Interpretation: This Does NOT Overturn Symmetric-Hyperbolic

A naive reading of "gauge orbit fills the symbol kernel" might suggest D_GU has NO physical
content at null xi. That reading is wrong, and the resolution is exactly what cements the
symmetric-hyperbolic (not elliptic) framing — but for a different reason than the lemma gave.

**The physical degrees of freedom are not the pointwise symbol kernel.** For ANY first-order
Dirac/de Rham-type operator on a Lorentzian manifold, at a null covector the principal-symbol
complex is a Koszul complex that is EXACT off the zero section: ker c(xi) = Im c(xi). The pointwise
"physical quotient" H(xi) = ker c(xi)/Im c(xi) is ZERO at every single null xi. This is not a
GU pathology — it is the universal structure of massless field equations.

**Maxwell control.** We verified the de Rham / Maxwell symbol on R^{3,1}: at null xi the symbol
(xi wedge + iota_xi) is maximal-rank nilpotent (rank 8 of 16), Im = ker, and the exact-form
(gauge) image fills the kernel; the symbol-complex Euler characteristic / cohomology is 0. The
two physical photon polarizations are NOT in the pointwise symbol kernel quotient — they are
recovered from the TRANSPORT (Bogoliubov / bicharacteristic) data, i.e. the cohomology of the
FULL complex along the null geodesic, after fixing initial data on a Cauchy surface.

**Consequence for the analytic framing.** The correct statement is:

  Elliptic case  (spacelike/timelike xi): ker c(xi) = {0}. No gauge, no kernel.
  Hyperbolic case (null xi): ker c(xi) = Im c(xi) = NM(xi). The symbol complex is EXACT;
    the gauge orbit fills the kernel; physical content lives in propagation, not in the
    pointwise kernel.

The switch from elliptic to symmetric-hyperbolic is correct, and it is forced precisely BY the
gauge-orbit-fill (Koszul-exactness at null xi), not by a (false) proper-subspace claim. The
well-posedness of the Cauchy problem (established independently in `sc1-oq2b-symmetric-hyperbolic`
via the Bar-Ginoux-Pfaffle theorem and the Friedrichs energy estimate) is what supplies the
physical content — the count of propagating modes equals the dimension of admissible Cauchy data
on a spacelike slice, NOT dim H(xi) at a single null covector.

**Net effect on the SC1-OQ2 conclusion.** The conclusion "D_GU is symmetric-hyperbolic / real
principal type, not elliptic" SURVIVES **conditionally on FF3 and FF4** (see §6). Its survival is
NOT unconditional: the corrected supporting argument runs through (A) the BRST-exact gauge orbit
equalling Im c(xi) — which presupposes FF3 (the dynamical gauge symmetry is generated by exact-form
coboundaries d_A(eps)), asserted here but not proved as a theorem — and (B) the pointwise physical
quotient H(xi) vanishing at every null xi — which presupposes FF4 (the FULL rolled-up symbol complex
on the 2^{14}-dim E is Koszul-acyclic off the zero section), verified only at reconstruction grade via
the irreducible-module argument, not by direct 4,194,304-dim computation. If FF3 fails, notion (A) no
longer coincides with Im c(xi) and the "gauge fills the kernel" leg does not run; if FF4 fails, a
genuine pointwise null-cohomology survives and the elliptic-vs-hyperbolic question reopens. The
supporting argument is CORRECTED in form (physical modes are carried by Cauchy-data transport, not by
a pointwise null-cone symbol-cohomology quotient) but its CONCLUSION inherits FF3/FF4 as open gates.
The generation count ind_H = 24 is computed by Atiyah-Schmid L2-theory on the fiber, which never used
a pointwise null-cohomology quotient, so it is untouched (and does not depend on FF3/FF4).

---

## 6. Result

**Verdict: OPEN** (downgraded from CONDITIONALLY_RESOLVED, 2026-06-23 — CORRECTION
SC1-LEMMA-CONTRADICTION-SAME-SESSION).

> [!WHY OPEN] This file NAMES an internal contradiction (§4: parts (ii) and (iii) of the sibling
> lemma are mutually inconsistent) and resolves it the SAME session. Per the loop's RESOLVED-blocking
> rule, that is an open problem until re-derived in a SUBSEQUENT session — same-session self-resolution
> does not count. The gauge-orbit-fill below is the CAS-supported WORKING HYPOTHESIS, not a settled
> result; it leans on FF3 and FF4, both OPEN. Re-derive inter-session before treating it as resolved.

**What is computed (reconstruction grade, with explicit CAS verification — working hypothesis):**

1. The Sp(64) gauge orbit **appears to fill** the null-mode space NM(xi) at every null covector
   (CAS result, working hypothesis). The BRST-exact (dynamical-gauge) orbit equals Im c(xi), which by
   the maximal-rank null-projection property equals ker c(xi) = NM(xi). The commutator orbit and
   direct-action orbit also fill NM when the full Sp(64) = U(64,H) algebra acts on the same H^{64} as
   c(xi) (verified explicitly in the model, n = 6, 8; generic null direction). Promotion to an
   established result requires inter-session re-derivation (the same-session contradiction-resolution
   gate) plus FF3/FF4.

2. This is the NEGATIVE-check outcome relative to the prior lemma's part (iii): the claim "gauge
   orbit is a proper subspace of NM(xi)" is FALSE. Parts (ii) and (iii) of
   `sc1-oq2-split-signature-ellipticity-lemma` are mutually inconsistent; the inconsistency
   resolves in favor of (ii) [the null-projection property].

3. The analytic-framework CONCLUSION is unchanged in DIRECTION (working hypothesis) **CONDITIONAL ON
   FF3, FF4, AND the inter-session re-derivation gate FF6** (all OPEN/fired): D_GU is
   symmetric-hyperbolic / real principal type, NOT elliptic-modulo-gauge. This unchanged-ness is NOT
   established and NOT unconditional. It rests on two of this file's own failure conditions (and is
   additionally capped OPEN by the same-session-resolution gate FF6):
   - **FF3 (OPEN)**: the BRST-exact/dynamical-gauge orbit equals Im c(xi), i.e. the gauge symmetry
     is generated by exact-form coboundaries d_A(eps). This is the entire basis for notion (A)'s
     "gauge fills NM(xi)"; it is asserted here, not independently proved as a theorem.
   - **FF4 (OPEN at full E)**: the symbol complex is Koszul-acyclic at null xi, dim H(xi) = 0. This
     is what rescues the conclusion from implying D_GU has no physical content; it is verified in the
     model and at reconstruction grade via the irreducible-module argument, NOT by direct
     4,194,304-dim computation on the full 2^{14}-dim rolled-up E.
   The gauge-orbit-fill is the Koszul-exactness of the massless-field symbol complex and is the SAME
   structure as Maxwell (verified control). Physical degrees of freedom are carried by Cauchy-data
   transport along null bicharacteristics, not by a pointwise null-cone symbol-cohomology quotient.
   If either FF3 or FF4 fires, the "unchanged" claim is not established and the elliptic-vs-hyperbolic
   framing must be re-examined (see FF3/FF4 rows below and §7 for the upgrade path).

**Failure conditions (explicit mathematical statements that would falsify this result):**

| Code | Condition | Impact if fired |
|------|-----------|-----------------|
| FF1 | rank c(xi) < dim_R E / 2 at some null xi (non-maximal nilpotent) | [NULL-PROJ] fails; Im c(xi) ⊊ ker c(xi); a genuine pointwise physical quotient would exist and the prior lemma's (iii) would be partially rehabilitated. RULED OUT by irreducibility of Cl(9,5) on S = H^{64} (sc1-oq2c §2, this file §3) but assumes the rolled-up complex inherits maximal rank from S; a degenerate form-degree pairing could in principle lower the rank. |
| FF2 | The physical gauge action rho is NOT left matrix multiplication on S (e.g. only the Spin(9,5) image, or a right action commuting with c(xi)) | If rho were the right-H action (commuting with c(xi)), the gauge orbit would map NM->NM trivially and the "fill" would be vacuous rather than load-bearing. RULED OUT by `sc1-oq3` (RESOLVED): rho = left mult, full Sp(64). |
| FF3 | The dynamical gauge symmetry of D_GU is NOT generated by exact-form coboundaries d_A(eps) (so Gauge_BRST != Im c(xi)) | If the true gauge group of the Dirac-DeRham complex had a symbol that is not c(xi)-coboundary, notion (A) would not coincide with Im c(xi) and the "fill" argument for (A) would not run. Requires the BRST/coboundary structure of the rolled-up complex; asserted here, not independently proved as a theorem. |
| FF4 | The symbol complex is NOT Koszul-exact at null xi (i.e. dim H(xi) = dim ker/Im != 0 at some null xi) | Would mean a genuine pointwise physical null-cohomology, contradicting the Maxwell-analogous Koszul-acyclicity and re-opening the elliptic-vs-hyperbolic question. RULED OUT in the model (Euler char 0; ker = Im verified) but the full 2^{14}-dim rolled-up E is checked only at reconstruction grade via the irreducible-module argument, not by direct 4,194,304-dim computation. |
| FF5 | Cauchy well-posedness fails (no symmetric-hyperbolic energy estimate) so that "physical content via transport" has no support | Then neither the pointwise-kernel nor the transport picture supplies physical modes and D_GU would be ill-posed. Independently CONDITIONALLY_RESOLVED against in `sc1-oq2b-symmetric-hyperbolic`. |

**Status of each:** FF1 ruled out at reconstruction grade (irreducibility); FF2 ruled out
(sc1-oq3 RESOLVED); FF3 OPEN (coboundary/BRST structure asserted, not proved); FF4 ruled out in
model, reconstruction grade for full E; FF5 CONDITIONALLY_RESOLVED elsewhere.

**FF3 and FF4 are LOAD-BEARING on item 3 (the "conclusion unchanged" claim), not merely
upgrade-to-RESOLVED niceties.** The symmetric-hyperbolic conclusion's robustness is exactly as strong
as FF3 (BRST-coboundary = gauge symmetry, so Gauge_BRST = Im c(xi)) and FF4 (full-E Koszul-acyclicity,
so dim H(xi) = 0) — both OPEN at reconstruction grade. The prose "analytic-framework conclusion is
UNCHANGED" must be read as conditioned on FF3/FF4; it is not an unconditional result. Combined with
the same-session-resolution cap (this file NAMED and RESOLVED the lemma's (ii)-vs-(iii) internal
contradiction in the SAME session — see §4 and the top-of-file banner), this is why the verdict is
**OPEN**, not CONDITIONALLY_RESOLVED: the FFs are legitimate and specific (3+ falsifiable math
statements), but the gauge-orbit-fill conclusion is a same-session overturn of a same-session lemma
whose unchanged-ness still depends on FF3/FF4, so it stands as a working hypothesis pending
inter-session re-derivation.

---

## 7. Open Questions and Cascade

**For re-upgrade above OPEN:**
- **Inter-session re-derivation** of the NM(xi) gauge-orbit question (primary gate, FF6 fired): the
  fill result and the (ii)-vs-(iii) contradiction-resolution were produced in the same session, so per
  the loop rule an intervening session must independently re-derive the result before the verdict can
  rise above OPEN.
- FF3: prove that the gauge symmetry of the rolled-up Dirac-DeRham complex is exactly the
  exact-form coboundary delta_eps Psi = d_A(eps), so Gauge_BRST(xi) = Im c(xi) as a theorem,
  not as a model-verified identity.
- FF4: direct verification (or a clean irreducibility theorem) that the rolled-up symbol complex
  on the full E = (Omega^{even} + Omega^{odd}) tensor S is Koszul-acyclic off the zero section,
  i.e. dim H(xi) = 0 at every null xi in the full 14D bundle, not just on the irreducible
  S-factor.

**Cascade — correction to the prior lemma (APPLIED 2026-06-23).** `sc1-oq2-split-signature-ellipticity-lemma`
part (iii) ("gauge orbit is a proper subspace of NM(xi)") has been corrected to: "the gauge orbit
FILLS NM(xi) (Koszul-exactness at null xi), which is the correct symmetric-hyperbolic signature;
physical modes are carried by Cauchy-data transport, not by a pointwise null-cohomology quotient."
This file NAMED an internal contradiction (lemma parts (ii) vs (iii)); per the loop's
RESOLVED-blocking rule (`process/loop-adversarial-log.md`: a same-session-named internal
contradiction cannot be self-resolved in the same session), the lemma's **file verdict was
downgraded from CONDITIONALLY_RESOLVED to OPEN**, and its corrected part (iii') stands as a working
hypothesis pending inter-session re-derivation. The *physics direction* of the analytic conclusion
(symmetric-hyperbolic, not elliptic) is unchanged; only the supporting mechanism is corrected and
the file verdict tracking is downgraded. THIS file (the F5 stress-test) is itself **OPEN** for the
same reason: it NAMED and RESOLVED the lemma's (ii)-vs-(iii) contradiction in the SAME session, which
the loop's RESOLVED-blocking rule treats as an open problem until re-derived in a subsequent session.
The gauge-orbit-fill result (the orbit fills NM(xi)) is a strong working hypothesis backed by the CAS
check and the [NULL-PROJ] algebraic fact, but it is a same-session overturn of a same-session lemma
and its symmetric-hyperbolic corollary still leans on FF3/FF4, so it is not yet settled. The DERIVATION-PROGRESS entry for the
lemma which stated the F5 gate as "CAS verification that the Sp(64) gauge orbit does NOT fill NM(xi)"
is resolved with the opposite sign: the orbit DOES fill, which is the expected and correct outcome.

**No change to downstream verdicts.** VZ evasion (off-null invertibility of c(xi)) is untouched —
it concerns spacelike/timelike xi where ker c(xi) = {0}, with or without gauge. Generation count
ind_H = 24 (Atiyah-Schmid L2-theory on the fiber) never used a pointwise null-cohomology quotient
and is untouched.
