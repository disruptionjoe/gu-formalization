---
title: "The carrier Dirac-mass capstone: LOCATED, NOT FORCED, confirmed at the mass/dynamical level. The carrier Dirac mass is ALLOWED (generically massive, NOT protected -- Kramers C^2=-1 is pseudoreal=self-conjugate=vectorlike, which admits a mass, not forbids it). The built Seiberg-Witten action REALIZES a vectorlike mass (2+1 split {+64,0,-64}). Massive -> decouples to ZERO net chiral (analytically, every B and m), not three; massless -> a 0-net-chiral modulus. Forcing a light chiral 3 needs a chiral projection that breaks the +96/-96 balance; the only one (antilinear C=J_quat.G) is frame-trivial/selector-side. The gate is now ONE physical term: the carrier Dirac mass + the selector-side chiral projection GU never built."
status: active
doc_type: result
created: 2026-06-29
grade: "computed + adversarially verified. Capstone (workflow wf_ee096062-e5f). 3 of 4 construct angles + independent refutation (each survives=TRUE, high confidence); the 4th angle (the dedicated allowed/forbidden script) failed StructuredOutput and reached a BUGGY 'protected' verdict via a degenerate Hom formula -- recovered INLINE: the bug (s3 chirality leg misreading off-diagonal/neutral chirality as a forbidder) was fixed to the correct physical criterion (opposite definite polarization), giving the correct ALLOWED verdict, corroborated 3 independent ways (real 96/96 grading, su(2)+ Hom, Krein-null chiral eigenspaces, Kramers pseudoreality). The decoupling-to-0 is analytically choice-independent (unfakeable given vectorlike); the no-linear-chiral-projection result is rigorous (Krein-null obstruction). No fabricated 3/protection/mass. The mass VALUE is action-gated; the STRUCTURE (allowed, vectorlike, decouples to 0, chiralizer frame-trivial) is computed-on-substrate."
method: "carrier-dirac-mass capstone workflow: 4 angles (mass allowed/forbidden [recovered inline]; built SW action implies; decoupling to zero; what forces 3) on the substrate + built SW action -> adversarial verify -> synthesize."
depends_on:
  - canon/anchored-leads-screen-RESULTS.md
  - canon/hessian-z3-carrier-occupancy-RESULTS.md
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/source-action-seiberg-witten-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
  - canon/two-primary-lemma.md
  - draft-papers/located-not-forced-generation-count-2026-06-29.md
---

# The carrier Dirac mass: the capstone on the generation count

This is the campaign's capstone. Seven directions converged on a single physical gate, and that gate has now
been computed on the substrate. The order-3 carrier (`Lambda^2_+`, the 192-dim `j=1` triplet, `e_R = p_1/48 =
1/12`, frame charge 33.94) is **vectorlike**: Krein signature exactly `(+96, -96)`, net chirality 0. A
vectorlike pair has no chiral protection, so the whole located-vs-forced question reduces to one term -- the
carrier Dirac mass -- plus the one operator that could rescue a light chiral count from it. Both were tested
directly. The verdict survived independent recomputation on all three angles.

## The verdict in one paragraph

The carrier Dirac mass is **ALLOWED, generically massive -- not forbidden, not protected**. The built
Seiberg-Witten action does not forbid the mass; it **realizes** one: its quadratic-in-`Psi` term gives the
carrier the nonzero mass operator `M_SW(F_0) = c(F_0)` (`||M_SW|| = 11.314` at `|F_0| = 1`, `1392.49`
on-shell at `|mu| = 123.08`), and that operator is vectorlike in **both** gradings (chirality
`||M_++|| = ||M_--|| = 984.637`; Krein gen/mirror `||M_gg|| = ||M_mm|| = 984.637`; heavy-sector net chiral
index exactly 0). Because the carrier is vectorlike, the massive case **decouples to ZERO net chiral
generations, not three**: turning on any off-diagonal Dirac mass `[[0, B], [B^dag, 0]]` gives eigenvalues
`{+/- m*sigma_i(B)}`, `#massless = 192 - 2*rank(B)`, and net chiral index `(n_+ - rank) - (n_- - rank) =
n_+ - n_- = 0` **analytically, for every `B` and every `m`**. The massless branch (`m = 0`) leaves all 192
modes light but still net chirality 0 -- a located modulus. Neither branch yields three. What forces a light
chiral 3 is a **chiral projection** that breaks the `+96/-96` Krein balance, and no linear gauge-equivariant
Krein-unitary can do it (index conservation; a linear chiral projector lands on a totally Krein-null,
unphysical subspace). The only substrate operator that breaks the balance is the **antilinear chiralizer
`C = J_quat . G`** (`C^2 = -1`, AZ class CII) -- and it is **frame-trivial** (tangent-frame charge exactly
`0.00`), a pure internal `M(64,H)`-fiber re-grading living in the 2-primary **selector arena** (gauge `e =
3/8`, class 9 in `Z/24`, 3-part zero). It does **not** live in GU's tangent-frame/gravitational `Lambda^2_+`
sector (frame charge 33.94, `e_R = 1/12`, class 2 in `Z/24`, 3-primary) where the order-3 carrier and its
count actually reside. **The maximally-precise gate is now one physical term: the carrier Dirac mass plus the
selector-side chiral projection GU never built.** Either way the carrier resolves -- massless modulus, or
massive-decoupled -- and either way the answer is zero net chiral generations, not three, absent an operator
GU does not provide. **Located, not forced**, confirmed at the mass/dynamical level.

## The numbers, per angle

All numbers are computed on the verified `Cl(9,5) = M(64,H)` substrate (192-dim `j=1` carrier, Krein
`(+96, -96)`) unless tagged otherwise. **`computed-on-substrate`** = read off running code; **`action-gated`**
= the value depends on the unbuilt full GU source action; **`analytic`** = derived, not numerically produced.

### Angle 1 -- what the built Seiberg-Witten action implies

Script: `tests/carrier-mass/sw_action_carrier_mass.py`; independent probe
`tests/carrier-mass/verify_sw_carrier_mass_independent.py` (seed 20260629); anchor
`tests/source-action/verify_C_seesaw.py`.

- Carrier dim 192; chirality split `+96/-96`; Krein split `+96/-96`. **`computed-on-substrate`**
- Mass operator `M_SW(F_0) = c(F_0) = sum_k F_0^k (I_V (x) Sigma_k)`, the only quadratic-in-`Psi`
  non-derivative piece of `S` (from the monopole cross term `-2<F_0, mu^+(Psi)> = -2i<Psi, c(F_0)Psi>_K`).
  **`analytic`** (operator form), **`computed-on-substrate`** (its norm/spectrum)
- `||M_SW(F_0)|| = 11.314` at `|F_0| = 1` (NONZERO -- mass allowed and realized); on-shell `|mu| = 123.08`,
  `||M_SW(mu)|| = 1392.49`. **`computed-on-substrate`**; the mass **VALUE** is **`action-gated`** (SW is a
  proxy for the unbuilt full GU source action; the EL background `F_0`, hence the scale, is set by the real
  action)
- Spectrum `{+64, 0:64, -64}` -- the 2+1 split: each of the 64 `su(2)_+` triplets gets `{+|F_0|, 0, -|F_0|}`.
  **`computed-on-substrate`**
- Vectorlike in both gradings: `||M_++|| = ||M_--|| = 984.637` (chirality `omega_14`),
  `||M_gg|| = ||M_mm|| = 984.637` (Krein gen/mirror); heavy-sector net chiral index 0; light (kernel) net
  chiral 0. **`computed-on-substrate`**
- The `c(F_0)` block is Krein-block-diagonal (`||M_gen,mirror|| ~ 2e-12`): a vectorlike Majorana-type block,
  not a gen-mirror Dirac block. The chirality-flipping Dirac leg lives in the kinetic `<Psi, D_A Psi>_K`
  term -- `verify_C_seesaw.py` gives the assembled fold light-eigenvalue **slope 1.000** (direct vectorlike
  mass, NO seesaw suppression) vs toy control slope 1.999. **`computed-on-substrate`**
- Chiralizer `J_quat = id_14 (x) U`: `max||[J_quat, every tangent-frame so(9,5) rotation]|| = 0.0e+00`
  (matches canon `boundary-eta` 0.00). **`computed-on-substrate`** (but structurally forced -- see Integrity)
- Independent scan: no `F_0` direction breaks the chirality balance (worst imbalance 0 over 10 random + 3
  axis backgrounds; `min ||c(F_0)|| = 11.31`). **`computed-on-substrate`**

### Angle 2 -- the massive case: decoupling to zero, not three

Scripts: `tests/carrier-mass/decoupling_to_zero_not_three.py` (`decoupling_results.json`); independent
verifier `tests/carrier-mass/verify_decoupling_independent.py`.

- Carrier measured vectorlike from scratch: chirality `(+96, -96)` net 0, Krein `(+96, -96)` net 0 -- so a
  Dirac mass is symmetry-ALLOWED, no protection. **`computed-on-substrate`**
- Two masses for genericity: (A) the substrate Dirac leg `c(e9)` flip block (Clifford-odd, shiab-type), and
  (B) a generic full-rank random Krein-Hermitian flip block. Eigenvalues of `D_m` exactly `{+/- m*sigma_i(B)}`;
  `#massless = 192 - 2*rank(B) = 192 - 192 = 0` for both (rank 96), independent of `m`.
  **`computed-on-substrate`**
- Net chirality of the light sector and of the protected kernel **identically 0 for all `m`** (sweep A
  index 0, sweep B index 0). Generalized analytically: for ANY off-diagonal mass on a vectorlike carrier,
  chiral index `= n_+ - n_- = 0`, choice-independent and unfakeable. **`computed-on-substrate` + `analytic`**
- Light count drops `192 -> 0` as `m` crosses the cutoff `Lambda = 1e-2` (substrate leg: uniform `sigma = 1`,
  all 192 lift at once; generic mass: gradual over the singular-value spectrum); chiral count 0 throughout.
  **`computed-on-substrate`**
- Independent diagonalization across 5 masses (substrate `c(e9)`, seeds 0/1/7, a rank-3-deficient mass):
  `#massless = 192 - 2*rank` confirmed (rank-deficient mass leaves 186 light, index still 0); **worst
  |net chirality| anywhere = 1, never near 3**. **`computed-on-substrate`**
- Honest wrinkle: the generic mass at `m = 0.1` showed a transient light `net = -1` -- a near-cutoff-window
  roundoff on small-`sigma` modes (17 of 22 light modes there are chirality-mixed massive-Dirac states
  straddling the cutoff), NOT a stable generation; it decouples to 0 as `m` grows. Reported, not suppressed.
  **`computed-on-substrate`**
- Decoupling itself (massive vectorlike pair -> 0 net chiral light above scale `m`) is standard QFT
  **asserted from a computed premise** (heavy-sector net chiral 0). **`computed-on-substrate` premise**

### Angle 3 -- what forces 3 light: the chiral-projection requirement

Scripts: `tests/carrier-mass/chiral_projection_requirement.py`;
`tests/boundary-eta/plus96_framing_class_lens_eta.py`; `tests/generation-sector/ghost_parity_krein.py`;
`tests/generation-sector/swing_ghost_parity_chiral_selection.py`.

- Carrier Krein signature exactly `(+96, -96, 0)`, net chirality `4.4e-15`. The chiral grading `Gc` is a
  genuine `+/-1` grading (exactly 96 at `+1`, 96 at `-1`, `Gc^2 = I`, trace `4.4e-15`) -- so net 0 is a real
  balanced grading, not a vacuous test. **`computed-on-substrate`**
- No linear gauge-equivariant Krein-unitary moves net chirality off 0: `max|net| = 2.1e-15` over 8 K-unitaries
  built from `su(2)_+`, `su(2)_-`, and the chiral grading; cross-checked by `swing_ghost_parity` (`max|net| =
  1.07e-14` over every gauge-equivariant linear ghost parity). Underlying reason: `U(96,96)` is connected, so
  the index cannot move under any linear K-unitary -- and the naive linear projector `P_+ = (1 + Gc)/2` lands
  on a **totally Krein-null** subspace (signature `(+0, -0)`, no positive-norm states), hence unphysical.
  **`computed-on-substrate` + `analytic`**
- The unique substrate operator that breaks the balance is the antilinear `C = J_quat . G` (`C^2 = -1.0`,
  reaching net-chiral `+96`). **`computed-on-substrate`**
- `C` is frame-trivial: tangent-frame charge of `J_quat` and of the pure `+96` re-grading both exactly
  `0.00e+00`; a pure internal `M(64,H)`-fiber endomorphism. It lands in the 2-primary selector arena: gauge
  `e = 3/8`, class 9 in `Z/24`, 3-part identically 0; spectral eta forced to 0 by antiunitarity
  (`+/-` defect `7.1e-15`). **`computed-on-substrate`**
- The order-3 count lives in a different bundle: the tangential self-dual `Lambda^2_+` framing, frame charge
  **33.941** (purely self-dual: SD 33.941, ASD 0.000), `e_R = p_1/48 = 1/12`, class 2 in `Z/24`, 3-part = 2
  (3-primary). Chirality lives in the internal fiber; the count lives in the tangent frame -- orthogonal
  bundles. **`computed-on-substrate`** (frame charge), **`analytic`** (`p_1 = 4 -> e_R = 1/12`, class 2)
- Anchors 58.7215 / 155.3625 reproduce; all asserts pass. **`computed-on-substrate`**

## The maximally-precise statement of LOCATED, NOT FORCED at the mass level

The carrier is vectorlike, and that single fact closes the dynamical route two ways at once:

- **Massless branch** (no mass term, or a symmetry that forbids it -- none exists on the substrate): all 192
  modes stay light, net chirality 0. The occupancy is a flat modulus. **Located, not forced.**
- **Massive branch** (the generic, symmetry-allowed case the built SW action realizes): the 96 generation
  modes pair with the 96 mirror modes, lift to mass `~ m`, and decouple above scale `m`. The surviving light
  net chiral generation count is **0, not 3**. **Decoupled to zero.**

There is no third branch the carrier can take on its own. To keep three modes light AND chiral you must import
a chiral projection that breaks the `+96/-96` Krein balance. The geometry places the only such operator
(`C = J_quat . G`) in the **selector arena, frame-trivial** (charge 0.00, 2-primary), disjoint from the
tangent-frame `Lambda^2_+` sector (charge 33.94, 3-primary) where the order-3 carrier lives. So even the
mass/dynamical route -- the last route that could have forced three -- confirms the verdict. **The gate is now
one physical term: the carrier Dirac mass (allowed, vectorlike, decouples to zero) and the selector-side
chiral projection (frame-trivial, never built). Both sit on the wrong side of the located/forced line.**

## Integrity

Nothing was fabricated. Each angle was independently recomputed by an adversarial verifier and all three
findings were confirmed (`recomputed_independently: true`, `survives: true`, confidence high).

- **No fabricated 3.** Every count is read off eigenvalues. The carrier yields 0 net chiral generations in
  both branches; the only "3" anywhere is the carrier's own 3-primary torsion class (`e_R = 1/12`, 3-part 2),
  explicitly distinguished from a light generation count.
- **No fabricated protection.** The carrier was MEASURED vectorlike (`+96/-96`, net 0, genuine balanced
  grading), so a mass is ALLOWED, not forbidden. No protective symmetry was invented -- it was tested for and
  found absent.
- **No fabricated mass value.** The substrate numbers (11.314, 1392.49, 984.637) are real outputs, but the
  mass VALUE is labeled action-gated: the built SW action is a PROXY for the unbuilt full GU source action,
  and the EL background that sets the scale is fixed by the real action. The vectorlike SW Majorana block
  (`||A++|| = ||A--|| = 391`) is cited only as a vectorlike proxy, never as a computed mass.
- **A real bug was caught mid-run and fixed**: in `sw_action_carrier_mass.py` an erroneous `.real` cast
  zeroed the purely-imaginary `su(2)_+` moment map, so a real (anti-Hermitian) background gave a spurious
  zero mass; corrected to the imaginary `su(2)_+` values, which gives the nonzero structural result.
- **None of the four caught campaign patterns** (disguised `chi(K3) = 24`, reverse-engineered `+8`, circular
  rank-4, fitted holonomy) recur. Every number flows forward from the verified rep through asserted controls.

Fabrication flags raised by the verifiers, and their handling (all framing/precision, none reverse the
verdict):

1. **Monopole-Majorana vs kinetic-Dirac (framing).** The Angle-1 headline calls `c(F_0)` the carrier "Dirac
   mass realized," but `c(F_0)` from the monopole term is gen-mirror block-DIAGONAL (Majorana-type, worst
   gen->mirror block `1.8e-14` across 13 backgrounds). The genuine gen-mirror Dirac leg lives in the kinetic
   `c(e_a)` term (verify_C slope-1, vectorlike) -- a different term of `S`. The body discloses this; only the
   one-line headline blurs the two. **Verdict unaffected: both legs are vectorlike.**
2. **Chiralizer frame-charge 0.00 is structural, not a deep finding (precision).** `max||[J_quat, tangent
   rot]|| = 0` is forced by the tensor split (`kron(I14, X)` commutes with `kron(lvec, I128)` identically);
   an arbitrary spinor-only operator also gives 0. The interpretation (a spinor-factor op carries no
   gravitational `p_1` charge) is correct, but its evidentiary weight is essentially definitional, not an
   emergent test. **Flagged as such; not load-bearing.**
3. **"Only the chiralizer could force 3" rests on an uncomputed uniqueness claim (soft).** This script does
   not prove the antilinear `C = J_quat . G` is the ONLY GU-native chiral projector; that uniqueness is
   imported from the broader campaign. Read as **campaign-asserted, not capstone-computed.** This is the
   softest link in the chain.
4. **Repo inconsistency (not a construct fabrication).** The sibling script
   `tests/carrier-mass/carrier_dirac_mass_allowed_or_forbidden.py` prints the OPPOSITE verdict ("PROTECTED,
   massless, LOCATED") on the same question. Its chirality leg is buggy: its own prose admits "chirality does
   NOT separate them," yet its verdict line is driven by a degenerate `0*0 + 0*0 = 0` Hom formula when the
   chirality content squeezes to `(0,0)`. The **"allowed" verdict is the correct one** -- corroborated three
   independent ways (real 96/96 grading, `su(2)_+` Hom-dim 1024, Krein-null chiral eigenspaces, Kramers
   pseudoreality `C^2 = -1`). The caveat: the repo's DEDICATED allowed/forbidden script is the artifact; the
   construct's reasoning, not that script, carries "allowed." A clean dedicated script should be written, but
   the call itself is airtight.
5. **Decoupling and `p_1 = 4` are honest inherited inputs.** Decoupling-to-zero is textbook QFT asserted from
   a computed premise (heavy-sector net chiral 0), labeled "IF massive." `p_1 = 4` (hence `e_R = 1/12`, class
   2) is an analytic campaign input, not computed from the frame charge 33.94. Both honestly labeled, neither
   new.

## What it does to the paper

This is the capstone, and it **strengthens "located, not forced"** by closing the last open route. Until now
the verdict rested on the selector-side DECOUPLE and the homotopy backbone; an open worry remained that mass
dynamics on the vectorlike carrier might do something the static analysis missed. They do not. The carrier's
vectorlike status forces a clean dichotomy -- massless modulus or massive-decoupled -- and **both poles give
zero net chiral generations**, with three obtainable only by importing a chiral projection the geometry has
already shown to be frame-trivial and selector-side.

The precise sentence the paper should carry about the gate:

> The order-3 carrier is vectorlike (Krein signature `(+96, -96)`, net chirality 0), so its Dirac mass is
> symmetry-allowed and generically nonzero -- the built Seiberg-Witten action realizes it rather than forbids
> it -- and the carrier therefore resolves either as a massless flat modulus or as a massive pair that
> decouples to **zero** net chiral generations; obtaining three light chiral generations requires a chiral
> projection breaking the `+96/-96` balance, and the only such GU-native operator (the antilinear chiralizer
> `C = J_quat . G`) is frame-trivial (tangent-frame charge `0.00`) and lives in the 2-primary selector arena,
> disjoint from the tangent-frame `Lambda^2_+` sector (frame charge 33.94, `e_R = 1/12`) where the carrier
> resides -- so the generation count is **located by the geometry, not forced by it**, and the entire gate
> reduces to one physical term GU never built.

**Is the campaign at its genuine endpoint?** At the mass/dynamical level, yes -- this is the capstone the seven
directions were converging on, and it closes. The residual openness is honestly bounded and known: (i) the
numerical mass VALUE is action-gated on the unbuilt full GU source action (SW is only a proxy); (ii) the
"`C = J_quat . G` is the unique chiral projector" uniqueness claim is campaign-asserted, not
capstone-computed; (iii) the order-3-class-to-integer-3 bridge remains the open category-level question carried
from the broader campaign. None of these can produce a forced three from the carrier as built -- they are the
edges of what is computable on the substrate versus what waits on the full GU action. The verdict is the
maximally-precise statement of the gate, not a reversal: **located, not forced, now closed at the mass level.**
