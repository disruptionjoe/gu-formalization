---
title: "PIN14 anomaly NUMBER: a genuine reconstruction attempt at the exact order of Omega^{Pin+}_14 (T1 from the operator-grade anomaly banking swing -- the 'one reconstruction number' that would exclude ANOMALY-TRIVIAL and make sigma's reflection-anomaly protection rigorous). VERDICT: |Omega^{Pin+}_14| = BLOCKED (exact order NOT certified), residual SHARPENED from 'the Adams chart' to THREE precise sub-steps. What IS genuinely reconstructed (not recited): the ABP reduction MTPin+ = MSpin ^ (RP^inf)^{3L-3} with the LEADING ko-Adams E_2 = Ext_{A(1)}(N,F_2), N = ~H^*(MTPin+) built with a DERIVED Steenrod action Sq^j x_i = C(i+3,j) x_{i+j} (from Thom iso + w(3L)=(1+a)^3) and machine-verified to satisfy the A(1) relations; both Margolis homologies H(N;Q_0)=0 (Q_0-acyclic) and H(N;Q_1)=F_2 concentrated in degree 1 (=> exactly ONE v_1-tower, the single source of the Z/2^k orders); and the indecomposable generators of N at degrees 0,4,8,12 (d=4 = the ABK/Z16 base) with NONE at stem 14. The exact order still needs: (1) the h_0-tower TRUNCATION LENGTHS at stem 14 (Bruner-Greenlees ko^(RP-Thom) / a verified minimal A(1)-resolution -- reciting them would be the forbidden over-claim), (2) the MSpin ABP correction summands Sigma^8 ko<2>, Sigma^10 ko, Sigma^12 ko<2> smashed with T at total degree 14, (3) the Adams d_2/d_3 differentials + hidden 2-extensions. sigma's SPECIFIC 14-class is T2-GATED (the group has room -- nonzero -- but WHICH class sigma is = [bulk, Pin+, deck], and the deck structure is the T2 object); ANOMALY-TRIVIAL is DISFAVORED (group nonzero, sigma survives the Kramers kill) but NOT rigorously excluded. Grade: RECONSTRUCTION-PARTIAL (framework + module + Margolis + generators, upgrading the prior probes' asserted table to a computed structure) with the NUMBER BLOCKED at the three named steps. Does NOT close the OPERATOR-END-PENCIL 'exact Pin+_14/eta reconstruction' residual; it sharpens it and upgrades the instrument."
status: active_research
doc_type: exploration
created: 2026-07-21
outcome: "BLOCKED on |Omega^{Pin+}_14| (exact order not certified); RECONSTRUCTION-PARTIAL of the ABP/A(1) structure; residual sharpened to three named steps; sigma's 14-class T2-gated"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
directed_by: "Joe direct chat, 2026-07-21 (T1 operator-grade anomaly banking; genuine shot at Omega^{Pin+}_14; one synchronous pass, foreground probe)"
inputs:
  - explorations/operator-grade-anomaly-banking-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - tests/channel-swings/operator_grade_anomaly_banking_probe.py
  - tests/channel-swings/pin_bordism_cardinality_probe.py
probe: tests/channel-swings/pin14_anomaly_number_probe.py (foreground, seed 20260721, numpy + exact F_2 linear algebra, EXIT 0, double-run byte-identical, 30/30 PASS)
---

# PIN14 anomaly NUMBER -- a genuine reconstruction attempt at |Omega^{Pin+}_14|

Single synchronous pass, foreground, maximum honesty about grade. This is **target T1**
from `operator-grade-anomaly-banking`: the exact order of `Omega^{Pin+}_14` (and the
Pin-`eta` / SW number of `sigma`'s degree-1-derived 14-class) -- the "one reconstruction
number" that would make `sigma`'s reflection-anomaly protection rigorous by **excluding
ANOMALY-TRIVIAL**. Everything is CONDITIONAL on the proposal-grade anomaly-inflow
identification (`sigma` = the `w1` reflection/`T` `Z/2`, receptacle `Omega^{Pin+}_14`).
Nothing here promotes that; it consumes it.

## 0. Verdict up front

> **`|Omega^{Pin+}_14|` = BLOCKED** (exact order NOT certified in this pass), but the
> residual is **materially sharpened** and the instrument is **upgraded from asserted to
> computed**. Grade: **RECONSTRUCTION-PARTIAL** (the ABP/A(1) framework, the module, its
> Margolis homologies, and its generators are genuinely computed) with the **NUMBER
> BLOCKED** at three precisely-named sub-steps.
>
> - **What is genuinely RECONSTRUCTED (machine-computed, firm):**
>   1. Controls `n = 0..7` + both anchors (`Omega^{Pin-}_2 = Z/8`, `Omega^{Pin+}_4 = Z/16`);
>      `n = 14 > 7` carries **no sporadic Pin+ zero**, so the group is a nonzero finite
>      2-group -- the receptacle has room.
>   2. The **ABP reduction made concrete**: `MTPin+ = MSpin ^ T`, `T = (RP^inf)^{3L-3}`,
>      leading ko-Adams `E_2 = Ext_{A(1)}(N, F_2)` with `N = ~H^*(T)`. The A(1)-module `N`
>      is built with a **DERIVED** Steenrod action `Sq^j x_i = C(i+3, j) x_{i+j}` (from the
>      Thom iso and `w(3L) = (1+a)^3`), and **machine-verified to satisfy the A(1)
>      relations** (`Sq^1 Sq^1 = 0`, `Sq^2 Sq^2 = Sq^1 Sq^2 Sq^1`) -- a genuine
>      "is-a-valid-A(1)-module" check, not an assertion.
>   3. **Both Margolis homologies** of `N` through degree 14: `H(N; Q_0) = 0` (`N` is
>      `Q_0`-acyclic -- no `HZ`/`Z`-carrying pieces) and `H(N; Q_1) = F_2` **concentrated in
>      degree 1** (=> **exactly ONE `v_1`-tower**, the single source of the `Z/2^k` orders).
>   4. **Indecomposable generators** of `N` at degrees **`0, 4, 8, 12`** (`d = 0 mod 4`;
>      `d = 4` is the ABK / `Z/16` base, `d = 0` the `Z/2`) -- and **NONE at stem 14**.
> - **What is still MISSING to bank the NUMBER (named, not papered) -- the three steps:**
>   1. The **h_0-tower TRUNCATION LENGTHS** in `Ext_{A(1)}(N, F_2)` at stem 14 (= the
>      Bruner-Greenlees `ko ^ (RP^inf Thom)` values / the `nu` truncation function): the
>      mechanism that turns the Bott `Z`-tower into `Z/16` at `n = 4` and into the stem-14
>      order. Needs a verified minimal A(1)-resolution or the BG tables -- **reciting them is
>      the forbidden over-claim.**
>   2. The **MSpin ABP correction summands** `Sigma^8 ko<2>`, `Sigma^10 ko`,
>      `Sigma^12 ko<2>` (from `MSpin_(2) = ko v Sigma^8 ko<2> v Sigma^10 ko v ...`) smashed
>      with `T` -- each hits total degree 14 and must be added before reading off the group.
>   3. The **Adams `d_2`/`d_3` differentials** and **hidden 2-extensions** that assemble the
>      `E_infinity` columns into the finite abelian group.
> - **`sigma`'s SPECIFIC 14-class: T2-GATED.** The group has room (nonzero), but WHICH
>   element `sigma` is `= [observerse bulk, Pin+, with the deck structure]`, and the deck
>   structure **is** the T2 object. So `sigma != 0 at 14` cannot be decided here.
>   **ANOMALY-TRIVIAL is DISFAVORED** (group nonzero; `sigma` survives the only known
>   trivializer, the Kramers 64-fold) **but NOT rigorously excluded** -- it needs both the
>   exact order (step 1-3) AND the T2 class-assignment.

Probe: `tests/channel-swings/pin14_anomaly_number_probe.py` -- foreground, numpy + exact
`F_2` linear algebra, seed `20260721`, **EXIT 0**, double-run **byte-identical**,
**30/30 PASS**.

## 1. Pre-declared kill-conditions (written BEFORE computation)

- **KILL-A (instrument):** if the controls `n = 0..7` (incl. anchors `Z/8`, `Z/16`) do NOT
  reproduce, the machine is broken -> discard.
- **KILL-B (module validity, anti-toy):** the reconstructed A(1)-module `N` must
  **satisfy the A(1) relations**. If `N` fails `Sq^1 Sq^1 = 0` or
  `Sq^2 Sq^2 = Sq^1 Sq^2 Sq^1`, the derivation is wrong -> discard, do not report structure.
- **KILL-C (Margolis engine):** the Margolis homology routine must reproduce the known
  controls (`H(F_2; Q_i) = F_2`; `H(A(0); Q_0) = 0`, `H(A(0); Q_1) = A(0)`). Else the
  `H(N; Q_i)` values are untrustworthy -> discard them.
- **DECISION (the number):** `|Omega^{Pin+}_14|` counts as **BANKED** ONLY if the exact
  order is produced from a CERTIFIED in-probe computation (tower truncation lengths from a
  verified resolution, MSpin corrections included, differentials + extensions resolved) --
  **not recited from a table**. If any of the three sub-steps is not certified, report
  **BLOCKED** and name exactly which.
- **DECISION (`sigma`'s class):** "is `sigma`'s specific 14-class nonzero" is BANKED only if
  evaluable WITHOUT the deck action. If the class-assignment needs the deck action, record
  **T2-GATED**.
- **Pre-declared expectation:** the framework/module/Margolis/generators are reconstructible
  in one pass; the exact order is NOT (it needs the BG `ko^RP` truncation data + MSpin
  corrections + differentials); `sigma`'s class stays T2-gated. **Anti-toy line held: the
  parent swing DECLINED "recite `|Omega^{Pin+}_14|` as computed"; this pass holds that line.**

<!-- RESULTS BELOW WERE WRITTEN AFTER RUNNING THE PROBE -->

## 2. The reconstruction (what the machine actually computed)

Probe run: **EXIT 0**, double-run **byte-identical**, **30/30 PASS**.

### 2a. Controls + the ABP reduction, made concrete (KILL-A, KILL-B cleared)

The tangential structure `Pin+(TM) <-> Spin(TM (+) 3 det TM)` gives the Madsen-Tillmann
spectrum `MTPin+ = MSpin ^ T` with `T = (RP^inf)^{3L-3}` (Thom spectrum of `3L` over
`RP^inf`, bottom cell normalised to degree 0). By the ABP splitting
`MSpin_(2) = ko v Sigma^8 ko<2> v Sigma^10 ko v ...`, the **leading** summand is `ko ^ T`,
whose ko-Adams `E_2` is (shearing iso + change of rings over `A(1) < A`)

    E_2(leading) = Ext_{A(1)}( N , F_2 ),      N = ~H^*(T)  as an A(1)-module.

`~H^*(T)` has basis `x_i` (degree `i`, `= a^i U` desuspended, `i >= 0`), and the Thom iso
gives the Steenrod action from `Sq(U) = w(3L) U = (1+a)^3 U`:

    Sq^j x_i = C(i+3, j) x_{i+j}   (mod 2).

For `A(1)` this is `Sq^1 x_i = (i+1 mod 2) x_{i+1}` (nonzero iff `i` even) and
`Sq^2 x_i = C(i+3,2) x_{i+2}` (nonzero iff `i = 0, 3 mod 4`). **This is derived, not
asserted**, and the probe **verifies `N` satisfies the A(1) relations** through degree 14
(`Sq^1 Sq^1 = 0`; `Sq^2 Sq^2 = Sq^1 Sq^2 Sq^1`, both identically `0` on `N`). The same
`3L` twist that builds `Sq(U) = (1+a)^3` **is** the Pin+ criterion (`Spin(TM+3det)`
preserves `w2`), and `RP^4` (Pin+, `w2 = 0`) is the `Z/16` generator at `n = 4` -- tying
`N`'s construction to the receptacle flavor.

### 2b. Margolis homology of N -- the genuine structural finding (KILL-C cleared)

The Milnor primitive `Q_1 = Sq^1 Sq^2 + Sq^2 Sq^1` is built as a composite AND checked
against the derived closed form `Q_1 x_i = (i+1 mod 2) x_{i+3}` (using
`(i+3)^2 = (i+1) mod 2`). The Margolis routine is validated on `F_2` and `A(0)` controls,
then applied to `N` (trusted through degree 14, buffered below the `x_23` truncation):

    H(N; Q_0) deg 0..14 : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   =>  N is Q_0-acyclic
    H(N; Q_1) deg 0..14 : [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]   =>  ONE v_1-tower, based deg 1

By the Adams-Margolis classification, `N` is, up to free A(1)-summands, a single
suspension of the "ko-type" (`v_1`-periodic) module: `H(N; Q_0) = 0` means **no `HZ` /
`Z`-carrying pieces** (consistent with `Omega^{Pin+}_*` being all-torsion), and
`H(N; Q_1) = F_2` (1-dimensional) means **exactly ONE `v_1`-tower** -- the single Bott
tower whose Adams-differential **truncation lengths** are the actual `Z/2^k` group orders.
This is the precise structural reason the number is not readable from `E_2` alone.

### 2c. Indecomposable generators -- a strong cross-validation

`dim( N_d / (Sq^1 N + Sq^2 N)_d )` (the `Ext^0` / bottom-of-tower count) is computed:

    indecomposables deg 0..14 : [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0]

i.e. generators exactly at `d = 0, 4, 8, 12` (`d = 0 mod 4`). This **matches where
`Omega^{Pin+}` is prominently nonzero** (`0 : Z/2`, `4 : Z/16`, `8 : ...`, `12 : ...`) and
cross-validates that `N` is the right module: `d = 4` is the **ABK / `Z/16` base**, `d = 0`
the `Z/2`. Crucially, **stem 14 (`= 2 mod 4`) carries NO fresh generator** in the leading
term -- its group rides the `v_1`-tower's reach plus the MSpin corrections, which is exactly
why `n = 14` is harder than the `0 mod 4` anchors and why the leading term alone does not
pin it.

## 3. Why the NUMBER is BLOCKED -- three precise missing steps

The reconstruction pins the `E_2` **structure** (one `v_1`-tower + generators at
`0,4,8,12` + `Q_0`-acyclicity) but NOT the exact order. Closing `|Omega^{Pin+}_14|` needs:

1. **Tower truncation lengths at stem 14.** The `h_0`-tower heights in
   `Ext_{A(1)}(N, F_2)` at stem 14 -- equivalently the Bruner-Greenlees `ko ^ (RP^inf
   Thom)` values / the `nu` truncation function. This is the mechanism that cuts the Bott
   `Z`-tower to `Z/16` at `n = 4`; at `n = 14` it needs a **verified minimal A(1)-resolution**
   (or the BG tables). Reproducing this from scratch is a known-hard input a foreground pass
   does not run, and **quoting the BG value would be the recitation the anti-toy discipline
   forbids.**
2. **MSpin ABP corrections at total degree 14.** The higher summands `Sigma^8 ko<2> ^ T`,
   `Sigma^10 ko ^ T`, `Sigma^12 ko<2> ^ T` contribute at total degree 14 (`14-8=6`,
   `14-10=4`, `14-12=2` in the smashed module). Through degree 7 `MSpin = ko` so the leading
   term is exact, but at `n >= 8` these corrections are real and **must be added** before
   reading off `Omega^{Pin+}_14`.
3. **Differentials + extensions.** The Adams `d_2`/`d_3` that truncate the towers, and the
   hidden 2-extensions assembling the `E_infinity` columns into the finite abelian group.

Reciting a published `|Omega^{Pin+}_14|` here would be exactly the planted-toy over-claim
this session guards against (and which the parent swing already declined). **The honest
output is BLOCKED on the number, with the residual sharpened from "the whole Adams chart"
to these three named sub-steps, and the leading `E_2` structure genuinely reconstructed.**

## 4. sigma's specific 14-class -- T2-GATED (unchanged, now grounded)

The **group** `Omega^{Pin+}_14` is pure topology (`sigma`-independent) and has room
(nonzero). But WHICH class `sigma` is `= [observerse bulk, Pin+, WITH the deck structure]`,
and the deck structure **is** the T2 object (`operator-grade-anomaly-banking` T2). So the
class-ASSIGNMENT needs the deck action -> **`sigma`'s class-nonvanishing is T2-GATED**,
consistent with the parent swing. The probe adds the honest degree-14 discrimination:
`w1(L)^14[RP^14] = 1` shows a degree-14 `w1` unoriented number **exists** (the target
degree is populated), but `RP^14` is **NOT Pin+** (`w2(TRP^14) = C(15,2) = 1 != 0`; it is
Pin-), so the object realising `sigma`'s **Pin+** 14-class is precisely the T2-gated
question -- not a manifold the SW machine hands us for free. Planted discrimination fires as
required: `0` on trivial/Spin inputs (`w1 = 0`), `1` on the `RP^2`/`RP^4` generators.

**Consequence:** `ANOMALY-TRIVIAL` (the class vanishes) is **DISFAVORED** -- the group is
nonzero, `sigma` survives the only known trivializer (the quaternionic Kramers 64-fold kills
the mod-2 index anomaly, not the geometric `w1` bit), and the Spin-side zeros are `w1`-blind
-- **but NOT rigorously excluded**, because excluding it needs BOTH the exact order (Section
3) AND the T2 class-assignment. This is the honest depth behind "PROTECTED (proposal grade)":
the protection's decisive input is entangled with the T2 deck action AND with an un-banked
order.

## 5. Does this close the OPERATOR-END-PENCIL "exact Pin+_14/eta reconstruction" residual?

**No -- but it sharpens it and upgrades the instrument.** Before this pass, the residual
read "needs the `ko ^ (RP^inf Thom)` Adams chart through degree 14 / the ABP `ko`-module
summand structure at `n = 14`" -- a single undifferentiated blocker, with the Pin table and
the `Z/16` anchor merely **asserted** in the prior probes. After this pass:

- the ABP reduction is **built explicitly** (`MTPin+ = MSpin ^ (RP^inf)^{3L-3}`, leading
  `E_2 = Ext_{A(1)}(N)`), the A(1)-module `N` is **constructed with a derived action and
  machine-verified valid** (upgrading "asserted table" to "computed structure"),
- the leading-term structure is **genuinely computed** (`Q_0`-acyclic; one `v_1`-tower;
  generators at `0,4,8,12`; `d=4` = the `Z/16` base cross-validated),
- and the remaining blocker is **resolved into three precise, independently-attackable
  sub-steps** (truncation lengths, MSpin corrections, differentials/extensions).

So the pencil residual moves from **"open, undifferentiated, table-asserted"** to
**"leading `E_2` reconstructed; number BLOCKED at three named steps."** The next pass that
would close it: a verified minimal A(1)-resolution of `N` (giving the `h_0`-tower heights =
the BG `ko^RP` truncation data) **plus** the three MSpin-correction modules **plus** the
`d_2`/`d_3` + extension analysis. That is a bounded, well-posed computation -- but it is a
dedicated resolution-engine build, not a foreground pass.

## 6. Typed claims and honest ledger

- **EXACT (machine-computed in the probe):** the controls `n = 0..7` incl. anchors
  `Z/8`, `Z/16`; the derived action `Sq^j x_i = C(i+3,j) x_{i+j}` and the verification that
  `N` satisfies the A(1) relations; `H(N; Q_0) = 0` and `H(N; Q_1) = F_2 @ deg 1` (Margolis
  routine validated on `F_2`, `A(0)`); indecomposable generators of `N` at `0,4,8,12` with
  none at stem 14; the flavor tie (`3L`-twist = Pin+ criterion; `RP^4 <-> Z/16`); the
  planted discrimination (trivial `-> 0`; `RP^2`/`RP^4 -> 1`).
- **DERIVED / STRUCTURAL (rides on the ABP reduction, itself standard):** the leading
  ko-Adams `E_2 = Ext_{A(1)}(N)`; `N` = free `(+)` one `v_1`-tower (based deg 1); the
  `Z/2^k` orders come from truncating that tower; stem 14 rides the tower + MSpin
  corrections (no fresh bottom).
- **RECONSTRUCTION-GRADE / OPEN (named, not papered):** the exact `|Omega^{Pin+}_14|` --
  BLOCKED on (1) the stem-14 `h_0`-tower truncation lengths (BG `ko^RP` / verified
  resolution), (2) the `Sigma^8 ko<2>`, `Sigma^10 ko`, `Sigma^12 ko<2>` MSpin corrections at
  total degree 14, (3) the `d_2`/`d_3` differentials + hidden 2-extensions.
- **T2-GATED (consumed from the parent swing, re-grounded):** `sigma`'s specific 14-class
  nonvanishing -- the group has room but the class-assignment needs the deck (T2) action;
  `ANOMALY-TRIVIAL` disfavored but not excluded.
- **Falls (do not ship):** "`|Omega^{Pin+}_14|` computed / recited as computed" (BLOCKED);
  "`sigma != 0` at 14, anomaly banked" (order BLOCKED + class T2-gated); "the leading `E_2`
  IS the answer" (MSpin corrections + differentials still required).

## 7. Boundary

Exploration tier. Only two NEW files written -- this document and the probe
`tests/channel-swings/pin14_anomaly_number_probe.py` (foreground, seed `20260721`, numpy +
exact `F_2` linear algebra, **EXIT 0** on both of two runs, double-run **byte-identical**,
**30/30 PASS**; kill-conditions declared in Section 1 BEFORE the probe was run). GU otherwise
read-only. **No commit, no push** (the coordinator commits with explicit paths). No edit to
LANE-STATE, research-portfolio, NEXT-STEPS, canon, PP1/PP2/PP3, the anomaly-inflow swing,
`pin-bordism-cardinality`, `operator-grade-anomaly-banking`, the LP-LC receipt, or any other
agent's artifact, or any claim/canon/verdict/ledger/portfolio file. No claim-status,
canon-verdict, paper-status, or public-posture change; the externality of `sigma`/`tau`, the
verdicts `LC-SELECTOR` and `CARDINALITY-1 + PROTECTED` (proposal), and the proposal-grade
anomaly-inflow identification are **consumed, not moved or promoted**. Nothing routes
externally (Joe alone publishes).

**Contribution.** A genuine reconstruction attempt at T1's "one number": the ABP reduction
`MTPin+ = MSpin ^ (RP^inf)^{3L-3}` is built explicitly and the leading ko-Adams module `N`
is **computed** (derived Steenrod action, verified A(1)-module, `Q_0`-acyclic, one
`v_1`-tower, generators at `0,4,8,12`), upgrading the prior probes' **asserted** Pin table to
a **computed** `E_2` structure and reproducing the `Z/16` base as an indecomposable bottom.
The exact `|Omega^{Pin+}_14|` stays **BLOCKED**, but the residual is sharpened from an
undifferentiated "Adams chart" to **three precise sub-steps**, and `sigma`'s decisive
14-class stays **T2-gated** (`ANOMALY-TRIVIAL` disfavored, not excluded). The
OPERATOR-END-PENCIL "exact Pin+_14/eta" residual is **not closed** -- it is sharpened,
instrument-upgraded, and made into a bounded, well-posed follow-on computation.
