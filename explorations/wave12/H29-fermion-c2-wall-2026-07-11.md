---
title: "H29 (Wave 12) -- The FERMION / C2 = 155.36 WALL: the source action's HARD residual. Even/odd + Krein attack on where the generation count lives."
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 12
depends_on:
  - "tests/wave12/H29_fermion_c2_wall.py"
  - "explorations/wave8/H23-source-action-construction-2026-07-11.md"
  - "absorbed/gu-source-action/SPEC.md"
  - "absorbed/gu-source-action/DEAD-ENDS.md"
  - "canon/no-go-quaternionic-parity-generation-sector.md"
  - "canon/carrier-dirac-mass-capstone-RESULTS.md"
  - "canon/two-arena-rep-theory-core-RESULTS.md"
  - "canon/shiab-existence-cl95.md"
verdict: "NARROWED (high confidence, structural). C2 = ||Gamma M_D Pi_RS|| = 155.3625 is EXACTLY characterized as the gamma-trace of the Velo-Zwanziger constraint-leakage block Q M_D Pi_RS -- a degree-1 symbol-norm (= sqrt(7)*bare), NOT an index. The even/odd (H20/H23-D Clifford-parity) lens PLACES C2 in the Clifford-ODD sector as the parity-partner of the even-sector |II|^2 graviton action, and the even-sector Krein positivity (H23-C) TRANSFERS: the odd-sector leakage O is Krein-self-adjoint. But the transfer is EQUALLY SIGN-BLIND (chirality split exactly symmetric c+ = c-), so it fixes C2's magnitude and supplies no chiral index. The odd sector is STRICTLY HARDER because the SAME particle-hole grading that organizes the even/odd split (O is Kramers J^2=-1 AND {G,O}=0) THEOREM-FORCES eta = 0 -- so C2 cannot be an index by any grading-preserving (canonical) move, whereas gravity's residual was a grading-PRESERVING soldering onto the real geometric object II_s. NOT resolved; no fit to 3; C2 not driven down (acausal trap avoided)."
---

# H29 -- The FERMION / C2 = 155.36 WALL

**Discipline.** This is the swing most at risk of motivated success (the buildbench has been
stuck on this wall for weeks; `DEAD-ENDS.md` records repeated beautiful-but-wrong burns). Every
positive claim below is an **exact matrix identity** on the verified `Cl(9,5) = M(64,H)`
representation (residuals `0.0e+00` or `~1e-14`), or an explicit ratio. **Nothing imported**
(no `24/8`, no `chi(K3) = 24`, no assumed K3, no fitting to 3). **C2 is NOT driven down** -- that
is the acausal Velo-Zwanziger trap in `DEAD-ENDS.md`; it is *characterized* and its obstruction
*named*. Reproducible: `python tests/wave12/H29_fermion_c2_wall.py` (exit 0, 12/12 PASS).

---

## 1. What the wall IS (characterized precisely)

`C2 = ||Gamma . M_D . Pi_RS|| = 155.3625` (Hilbert-Schmidt), at the repo covector `xi`, on the
verified rep. Anchor reproduced live; bare `||[Pi_RS, M_D]|| = 58.7215` reproduced.

**The exact identity (new, and it is the whole characterization).** Because `Pi_RS` projects onto
`ker Gamma`, we have `Gamma . Pi_RS = 0` (residual `1.1e-14`). Therefore

```
C2 = ||Gamma . M_D . Pi_RS|| = ||Gamma . [M_D, Pi_RS]|| = ||Gamma . (Q . M_D . Pi_RS)||
```

(all three `= 155.3625` to 4 dp; `Q = I - Pi_RS`). So **C2 is the gamma-trace of the
constraint-LEAKAGE block** `Q M_D Pi_RS`: the piece of the Dirac symbol `M_D` that pushes a
physical (gamma-traceless, `Pi_RS`) Rarita-Schwinger field OFF the constraint surface. This is
exactly the **Velo-Zwanziger consistency object** -- the Hessian/symbol-norm measuring how badly
the Dirac symbol fails to preserve the RS gamma-trace constraint. It is a **Hessian of an operator**,
not an index.

**Why it is NOT an index (re-derived numerically).**
- `C2 = sqrt(7) . bare` **exactly** (`2.6457513111`; `sqrt(7) = 2.6457513111`). This locks C2 into
  the rep's native prime spectrum `{2, 7, 13}` (canon C-04) -- an irrational surd, not an integer.
- `C2` is **degree-1 homogeneous**: `C2(2xi)/C2(xi) = 2.0`, `= 3.0` at `3xi`, `= 0.5` at `0.5xi`
  (all exact). A topological index is scale-INVARIANT; C2 is scale-DEPENDENT. **Different KIND of
  object** (SPEC.md, DEAD-ENDS.md -- confirmed, not re-litigated).

A valid `S_IG` would have to connect this scale-dependent symbol-norm to a genuine scale-invariant
index (SPEC.md object 5(iii)). H29's job was to test whether the 10-wave even/odd + Krein leverage
does that. It does not -- and it names precisely why.

## 2. The even/odd lens (H20 square/square-root; H23-D Clifford parity): C2 IS the odd sector

The chirality involution `omega = e_0 ... e_13` satisfies `omega^2 = +I`, Hermitian (residual
`0.0`). Grading everything by `omega`:

| operator | parity under `omega` | residual |
|---|---|---|
| `M_D = id (x) c(xi)` | Clifford-**ODD** (`{omega, M_D} = 0`) | `0.0e+00` |
| `Gamma` (gamma-trace) | Clifford-**ODD** | `0.0e+00` |
| leakage `O = Q M_D Pi + Pi M_D Q` | Clifford-**ODD** | `0.0e+00` |
| `Pi_RS` | Clifford-**EVEN** | `0.0e+00` |

So **C2 lives entirely in the Clifford-ODD sector.** This confirms the task's central hypothesis:
C2 is the odd-sector object -- the fermionic parity-partner of the EVEN-sector graviton action
`|II|^2` (whose dynamics `M_D` sits inside, `sigma_ab` Clifford-even). The canon shiab is Clifford-odd
too (`shiab-existence-cl95.md` SHIAB-A: shiab is Clifford-odd, `d_A*` is Clifford-even), so the
fermion carrier and the C2 leakage share parity. The H20 "square and square-root" unification reads
concretely: **one `|II|^2`-on-`Y14` structure, even part = gravity, odd part = the C2 leakage.**

**But the split does NOT reduce C2.** Projecting the domain onto chirality `+/-`:
`c+ = ||Gamma M_D Pi P+|| = 109.8579`, `c- = 109.8579` -- **exactly equal** -- and
`sqrt(c+^2 + c-^2) = 155.3625 = C2` (Pythagorean). The even/odd split exposes C2 as **chiral-
SYMMETRIC**: zero net chiral asymmetry. This is the odd-sector analog of H23-C's sign-blindness.

## 3. Does the even-sector (H23) resolution transfer? YES -- and that is why it does not resolve

H23-C's gravity win: the Krein form `K = eta_V (x) beta_S` makes `M_D` Krein-self-adjoint
(`K M_D = M_D^dag K`, residual `0.0`), buying `[P,S] = 0` positivity -- but sign-blind.

**The transfer (H29-C2).** The SAME `K` makes the odd-sector leakage `O` **Krein-self-adjoint**:
`K O = O^dag K` (residual `7.8e-15`). The even-sector positivity machinery applies *verbatim* to
the fermion leakage. So the odd sector inherits the positivity/reality structure of the even sector.

**But it is EQUALLY sign-blind.** Combined with the exact chiral symmetry (`c+ = c-`), `K` fixes the
MAGNITUDE of C2 and supplies NO chiral index -- exactly as H23-C's `[P,S]=0` "pairs, does not select."
The transfer is real but count-blind. This is the honest core: the even-sector method **does**
transfer; it just does not buy what the count needs, in the odd sector any more than the even one.

## 4. Why the odd sector is STRICTLY HARDER (the eta=0 mechanism, canon C-01)

Here is the wall, named exactly. The leakage `O = Q M_D Pi + Pi M_D Q` is simultaneously:

1. **Kramers J-linear:** `O . C_RS = C_RS . conj(O)` with `C = e1 e3 e5 e7 e10 e12`, `C^2 = -I`
   (residual `0.0`). This is the no-go canon's `J^2 = -1` even-signature wall.
2. **particle-hole ODD:** with the boundary chiral grading `G = Pi_RS - Q` (`G^2 = I`),
   `{G, O} = 0` (residual `6.3e-14`). An anticommuting grading forces the spectrum `+/-lambda`
   symmetric, hence `eta(D_Sigma) = 0` (canon C-01; Altland-Zirnbauer class CII).
3. **Krein-self-adjoint** (Section 3): real magnitude.

**Consequence.** C2 is the **nonzero norm of a leakage whose spectral asymmetry (index / eta) is
THEOREM-FORCED to zero.** "C2 is not an index" now has its *mechanism through the even/odd lens*:
the very grading that organizes the even/odd split is the particle-hole symmetry that kills the index.

**Contrast with gravity -- this is what "strictly harder" means precisely.**
- **Even sector (H23-D):** the residual is a grading-PRESERVING **soldering** postulate
  `pi = spin-lift(grad^gimmel)`, landing the gravity field `theta` on the **real geometric object**
  `II_s` (the second fundamental form). Codim-8165 and underived, but natural and grading-preserving,
  onto an object that exists.
- **Odd sector (H29):** the natural target is a **generation index**, and it is OBSTRUCTED BY A
  THEOREM (`eta = 0`, CII), not merely unbuilt. To get a nonzero odd index you must either
  (a) **BREAK the grading** -- reviving a connection-DEPENDENT, non-canonical index (canon C-02/C-03),
  or (b) **IMPORT** the antilinear chiralizer `C = J_quat . G`, which the capstone shows is
  **frame-trivial / selector-side** (tangent-frame charge `0.00`, 2-primary arena). Both are exactly
  the forbidden moves. The even sector's escape has no odd analog: there is no geometric object the
  odd leakage canonically solders onto, because its canonical landing (an index) is theorem-blocked.

## 5. What it says about the count (located vs forced)

Attacking C2 clarifies located-vs-forced by proving C2 is **count-BLIND**: the generation number is
not in C2's magnitude (chiral-symmetric, index forced to zero). It lives in the selector-side chiral
projection C2 provably cannot supply. This **reinforces the capstone's "located, not forced"** from a
new direction: the `(9,5)`/H-class Kramers wall (even signature) and the `eta = 0` CII structure are
inherited by the C2 leakage itself. The `(7,7)` alternative (`J^2 = +1`) is exactly where this wall
would dissolve -- so the C2 wall is **signature-contingent** in the precise way the no-go canon flags,
and the odd-primary `Z/3` arena where the located 2-bit lives is orthogonal to (not produced by) the
C2 magnitude. **C2 does not force 3; it forbids the odd sector from producing ANY odd index
intrinsically.** No `24/8`, no `chi(K3)`, no fit -- the only integers anywhere are rep dimensions and
the exact homogeneity degree.

## 6. Verdict: NARROWED (not RESOLVED, not a bare WALL)

**NARROWED, high confidence** on the structural facts (all exact rep-theory identities, residual
`0.0`, independent of whether GU is correct). The 10-wave even/odd + Krein leverage genuinely
sharpens the obstruction:

- **Before:** C2 was a mysterious `155.36` non-index symbol-norm with named-but-opaque missing
  carriers (families pushforward / boundary Dirac / BV-to-boundary-Dirac).
- **After:** C2 is the **magnitude of a particle-hole-ODD, Kramers (`J^2 = -1`), Krein-self-adjoint
  constraint-leakage** `Q M_D Pi_RS`, chiral-symmetric, whose index is theorem-forced to zero. The
  even-sector Krein positivity transfers but is sign-blind. The residual is precisely one object.

**Not RESOLVED.** No closure was earned and none was manufactured. Earning it requires the missing
carrier below; the honest prior (no-go canon + capstone) is against its existence.

**The precise next object (the residual, named).** A **canonical, grading-BREAKING boundary-Dirac**
`D_Sigma` on the non-compact `Y14` end whose APS `eta != 0` **without** breaking the Koszul-Tate
positive-Hessian grading (which forces the CII particle-hole `C = J_quat . G` and hence `eta = 0`)
and **without** importing the frame-trivial antilinear chiralizer. On the current data these two
requirements are **mutually exclusive** (C-01 forces the grading from the positive KT Hessian; the
grading forces `eta = 0`; breaking it forfeits canonicity per C-02/C-03). That mutual exclusion --
not a missing computation -- is the wall. This is **strictly harder than gravity's soldering**: the
soldering is a grading-preserving postulate onto a real object; the fermion residual asks for an
object a theorem currently forbids.

### Honest caveats

1. **Grade of the numerics.** Exact matrix identities on the 128-dim complex rep (residuals `0.0`
   or `~1e-14`), not a symbolic proof over the abstract algebra. For these finite-dim identities the
   explicit rep is decisive.
2. **`eta = 0` is imported at theorem level** from canon C-01 (`step1..step5`); H29 verifies the
   grading INGREDIENTS on the C2 leakage directly (`{G,O}=0`, `G^2=I`, Kramers `J^2=-1`,
   Krein-self-adjoint) but does not rebuild `D_Sigma` itself. The inference "these ingredients =>
   `eta=0`" is C-01's, cited not re-proved.
3. **The mutual-exclusion claim (Section 6) is the strongest interpretive step.** It rests on
   C-01 (grading forced by positive KT Hessian) + C-02/C-03 (grading-break gives connection-dependent,
   non-canonical index) + capstone (the only balance-breaker is frame-trivial). Each leg is canon; the
   *conjunction* into "mutually exclusive on current data" is H29's synthesis, exploration-grade.
4. **No p-hacking.** No `3` appears (sector norms `109.858, 155.362, 58.722`, ratio `sqrt(7)` -- all
   irrational). C2 is unchanged at `155.3625` (explicitly not reduced -- the acausal-trap family is
   avoided). The "narrowing" is a structural re-characterization by exact identity, not a numeric
   reduction and not a fit to the target.

---

*Filed 2026-07-11. Wave 12, the FERMION/C2 push-further swing. Reproducible:
`python tests/wave12/H29_fermion_c2_wall.py` (exit 0, 12/12 PASS). Exploration-grade; not promoted
to canon. Adversarially graded: no forcing manufactured, no target imported, C2 not driven down; the
honest outcome is a sharply narrowed, precisely-named obstruction that is strictly harder than the
gravity soldering.*
