---
title: "H23 (Wave 8) -- The source-action construction: A = spin-lift(grad^gimmel). Attempt to make gravity's clear UNCONDITIONAL."
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 8
depends_on:
  - "tests/wave8/H23_source_action_construction.py"
  - "explorations/wave5/H21-theta-equals-II-2026-07-11.md"
  - "explorations/wave4/H18-forcing-computation-2026-07-11.md"
  - "explorations/wave7/H25-II-first-variation-2026-07-11.md"
  - "canon/shiab-existence-cl95.md"
  - "canon/ghost-parity-krein-synthesis.md"
  - "absorbed/gu-source-action/SPEC.md"
  - "absorbed/gu-source-action/DEAD-ENDS.md"
  - "absorbed/gu-source-action/SOURCE-ACTION-BUILDBENCH-PACKET-2026-07-10.md"
verdict: "PARTIAL. The spin-lift so(9,5)->End_H(S) is CANONICAL/forced (exact homomorphism); the gauge group it lands in is the NON-COMPACT real form Sp(32,32;H) (sharpens canon's 'Sp(64)'); the ghost parity P=K implements the Cartan involution and [P,S]=0 HOLDS for the natural covariant dynamics (Krein-self-adjoint) -- but SIGN-BLIND. The IDENTIFICATION A = spin-lift(grad^gimmel) is NOT kinematically forced: it is a codimension-8165 SOLDERING postulate GU's dynamics does not supply. mu_DW is NOT fixed (dimensionless ratio already fixed by H25; dimensionful scale free). Gravity does NOT go unconditional; it is clear-MODULO-soldering. The residual is the SAME CLASS as the buildbench's standing block but NARROWED to a single sharply-named bosonic object -- distinct from the fermion-sector C2 wall."
---

# H23 -- The source-action construction: `A = spin-lift(grad^gimmel)`

**Discipline.** Exploration-grade; compute -> adversarially verify -> HONEST grade. This is the
swing most at risk of motivated success, so every positive claim below is an **exact matrix
identity** on the verified Cl(9,5)=M(64,H) representation (all residuals `0.0e+00`) or an explicit
dimension count. Nothing imported (no 24/8, no assumed K3, no fitting). Reproducible check:
`tests/wave8/H23_source_action_construction.py` (exit 0, 10/10 PASS). "It fits beautifully" was
treated as a warning sign throughout (per `DEAD-ENDS.md`).

---

## The target

Seven waves cleared everything else on the gravity leg: H21 proved `s*(theta)=II_s` off-shell,
full-tensor, in the canonical gauge; H18 forced the II-class; H15/H25 gave Stelle `R^X + Weyl^2`
with the massive-ghost sign **CLEAR** at tree level (`C_RY>0`, `m^2_eff>0`). H21 isolated the
**single** remaining object as the canonical-connection identification

```
A  =  spin-lift( grad^gimmel )
```

-- GU's Sp(64)-bundle gauge connection `A` (the `pi` piece of `theta = pi - Ad(eps^-1)B`) equals
the spin-lift of the gimmel/DeWitt Levi-Civita connection on the SO(9,5) frame bundle of
`Y^14 = Met(X^4)` -- with action `S = |theta|^2 = |II|^2`. H21 flagged this as "the same class as
canon Assumption 3 = GU's unbuilt source action." H23's job: **establish it, or name the exact
obstruction.**

## What H23 computed (all exact, residual 0)

The construction splits into a part that **is** canonical and a part that is **not forced**. The
honesty of the verdict rests entirely on keeping these separate.

### (A) The spin-lift MAP is canonical and forced -- CONSTRUCTED

The lift `so(9,5) -> End_H(S)`, `sigma_ab = 1/4[e_a, e_b]`, is an **exact Lie-algebra
homomorphism**: the test verifies

```
[sigma_ab, sigma_cd] = eta_bc sigma_ad - eta_ac sigma_bd - eta_bd sigma_ac + eta_ad sigma_bc
```

over all `91 x 91` generator pairs, `max err = 0.0e+00`. The 91 generators are independent
(`dim image = dim so(9,5) = 91`). This is the **unique** canonical lift (up to the chiral/scale
freedom already mapped in SHIAB-03/04) -- there is **no free choice in the lift itself**. So the
*object* "`spin-lift(grad^gimmel)`" is well-defined and forced. This removes one of H21's two
sub-gaps (the "does a canonical spin-lift exist" question): **yes, explicitly, and it is the
standard `1/4[gamma,gamma]` representation.**

### (B) The gauge group is the NON-COMPACT real form Sp(32,32;H) -- sharpens canon

The spinor Krein metric `beta_S = e_0...e_8` (product of the 9 spacelike gammas) is Hermitian,
`beta_S^2 = I`, **traceless**, with signature exactly **(+64, -64)** -- INDEFINITE. The spin-lift
image is `beta_S`-pseudo-anti-Hermitian: `beta_S sigma_ab + sigma_ab^dag beta_S = 0` for all 91
generators (`max err 0.0e+00`). Therefore the spin connection lands in the **pseudo-unitary
quaternionic** algebra `sp(32,32;H) = u(32,32;H)`, the **non-compact** real form -- **not** the
compact `Sp(64) = U(64;H)` that canon `shiab-existence-cl95.md` Step 4 names as "the gauge group."

This is a genuine sharpening (and an adversarial catch): `Spin(9,5)` is non-compact simple, so it
**cannot** map non-trivially into the compact `Sp(64)`; the spin rep is not unitary but
`beta_S`-pseudo-unitary. Canon's "Sp(64)" is the automorphism group of the bare `H`-module
structure; the connection the geometry actually carries preserves the **indefinite** `beta_S` and
so lives in `Sp(32,32;H)`. This is fully consistent with the `ghost-parity-krein-synthesis.md` A0
correction ("the indefinite Krein form exists only because the internal gauge group is taken
NON-COMPACT") -- H23 makes that explicit at the connection level.

### (C) `[P,S]=0` HOLDS for positivity -- but is SIGN-BLIND

`beta_S` implements the **Cartan involution** of `so(9,5)`: `beta_S sigma_ab beta_S = +sigma_ab`
for rotations (both indices in `so(9)` or both in `so(5)`) and `= -sigma_ab` for boosts (mixed) --
`max err 0.0e+00`. So the Krein ghost parity `P = K = eta_V (x) beta_S` (canon V2: `K` implements
the Cartan involution, equals the ghost parity on the triplet) is exactly the Cartan `Z2`.

The natural covariant dynamical operator -- the twisted Dirac symbol `M_D = id_14 (x) c(xi)` -- is
**exactly Krein-self-adjoint**: `K M_D = M_D^dag K` (`err 0.0e+00`). This is precisely the
Bateman-Turok condition `[P_ghost, S] = 0` for **consistent ghost removal / positivity**. So on the
constructed dynamics the massive ghost **clears in the Krein sense**.

**The adversarial catch (C3).** This Krein-self-adjointness holds for **every** covector `xi`
(verified over 5 random `xi`, `err 0.0e+00`) -- it is a structural feature of *any* `so(9,5)`-
covariant operator, not a tuned coincidence. That is exactly why it is **sign-blind**: the parity
*pairs* generation with mirror (K-balanced eigenspaces), it does not *select*. `[P,S]=0` buys
gravity's positivity; it does **not** buy the generation count. This matches the canon fence
verbatim (`{K,chi}=0 forces Re tr(chi Pi_+)=0`; SHIAB-05: the same-chirality Majorana channel is
absent from the equivariant family). **Generation count stays OPEN** -- no chiral selection is
manufactured here, and any that appeared would be the p-hacking the program has avoided.

### (D) The IDENTIFICATION is NOT forced -- a codimension-8165 soldering

Here is the honest wall. `theta = pi - Ad(eps^-1)B` is `ad P`-valued, i.e. takes values in the
`~8256`-dimensional gauge algebra `sp(32,32;H)` (`dim = 64 * 129`; the complex Krein upper bound
`u(64,64)` is `16384`). The reference `spin-lift(grad^gimmel)` pins the connection to the
**91-dimensional** `so(9,5)` image. So `A = spin-lift(grad^gimmel)` is a **codimension-8165
constraint per point** -- massively non-automatic.

Nothing in GU's kinematics imposes it:
- The spin-lift being canonical (A) makes the *reference* canonical, not the *dynamical* `A`.
- H21's `s*(theta)=II_s` is a **gauge** statement (holds in the tautological gauge); it does not
  force GU's dynamical `pi` onto the reference.
- The source action `S = |theta|^2` does **not** force it either: `theta` is the **gravity field**,
  so its Euler-Lagrange equation is `d_A * theta = source`, **not** `theta = 0`. The vacuum is not
  the soldered configuration. (Driving `theta -> 0` would additionally re-hit the acausal-trap
  family in `DEAD-ENDS.md`.)

So the soldering `pi = spin-lift(grad^gimmel)` -- the step that makes `theta` *be* the geometric
second fundamental form -- is a **structural postulate GU's dynamics does not supply**. It is the
**same class** as canon Assumption 3 / the buildbench's standing block.

### mu_DW is NOT fixed

Even granting the soldering, the identification does not fix `mu_DW`. The **dimensionless** ratio
(horizontal:vertical) that sets `m^2_eff` was already computed by H25 (`m^2_eff = 5/6`..`5/4`,
`O(1)`, sign-positive) directly from the gimmel geometry -- soldering adds nothing there. The
**dimensionful** overall scale `mu_DW ~ M_Pl` is the coupling constant of `|theta|^2` (the analog
of `1/G` / the Stelle coefficients); soldering makes `A` a function of the gimmel metric but leaves
its overall normalization free. So `mu_DW` stays exactly where H24/H25 left it: **not derived**.

## VERDICT: PARTIAL

| Sub-claim | Result | Grade |
|---|---|---|
| spin-lift map `so(9,5) -> End_H(S)` | exact homomorphism, unique canonical lift | **CONSTRUCTED** (residual 0) |
| gauge group real form | non-compact `Sp(32,32;H)`, `beta_S` sig `(64,64)` | **CONSTRUCTED**; sharpens canon "Sp(64)" |
| `[P,S]=0` (positivity) | `M_D` Krein-self-adjoint, `K M_D = M_D^dag K` | **HOLDS** (residual 0), but **sign-blind** |
| chiral selection / generation count | absent from covariant family | **OPEN** (unchanged; canon fence) |
| `A = spin-lift(grad^gimmel)` identification | codim-8165 soldering, not forced by kinematics or by `S=|theta|^2` | **NOT FORCED** (structural postulate) |
| `mu_DW` scale | dimensionless ratio fixed (H25); dimensionful scale free | **NOT FIXED** |

**Gravity does NOT go unconditional.** It is **clear-MODULO-soldering**: given the one postulate
`pi = spin-lift(grad^gimmel)`, everything downstream is in hand (spin-lift canonical, sign clear,
ghost clears in the Krein sense). Without it, `theta` is not pinned to `II_s` and the whole H18/H21
chain is a gauge/reconstruction statement rather than a derivation.

**Confidence.** HIGH on (A)/(B)/(C) -- they are exact representation-theoretic identities,
independent of whether GU is correct. HIGH on (D) as a *negative* result (the dimension gap is
unambiguous; the EOM argument is standard). The one thing I did **not** find, after adversarially
looking for it, is any GU-internal principle (tautological section, shiab, `s*(theta)=II_s`) that
**forces** the soldering. The tautological structure on `Y=Met(X)` makes the *reference* canonical;
it does not collapse the dynamical connection onto it. Claiming otherwise would be choosing `A` to
get the answer.

### Honest caveats

1. **The soldering could still be true** -- as a *postulate* it is natural (the reference is the
   unique metric-compatible torsion-free lift). H23's claim is only that it is **not derivable**
   from the currently-built structure, which is exactly what "the unbuilt source action" has always
   meant. A future dynamics that forces `theta` onto the SFF locus would upgrade this to CONSTRUCTED.
2. **P2 (`S = |theta|^2` exactly) is not re-litigated** -- taken from H18 (transcript-grade). A
   Willmore-type variant would change the story; H23 assumes the II-class `|theta|^2`.
3. **Grade of the numerics.** Exact matrix identities on the 128-dim complex rep (all residuals
   `0.0e+00`), not a symbolic proof over the abstract algebra -- but for these finite-dimensional
   identities the explicit rep is decisive.
4. **`beta_S` convention.** Built as the product of the 9 spacelike gammas; the Cartan/Krein
   results are convention-robust (any spacelike-product choice gives the same `so(9)+so(5)` split).

## Match to / narrowing of the buildbench's standing obstruction

The buildbench's block (`SOURCE-ACTION-BUILDBENCH-PACKET`, `SPEC.md`) is the **fermion/generation**
residual: the 5-part `S_IG`, the `C2 = 155.3625` boundary symbol-norm that is **not an index**, the
missing families-pushforward / boundary-Dirac / BV-to-boundary-Dirac carriers. H23 does **not**
touch that wall.

What H23 does is **separate out the GRAVITY residual** and name it precisely:

- **Gravity residual (H23):** one bosonic **soldering** postulate `pi = spin-lift(grad^gimmel)`
  (+ the dimensionful `mu_DW` scale). Sign/structure done; `[P,S]=0` positivity done; the only gap
  is a single natural-but-underived constraint on the connection.
- **Fermion residual (buildbench):** the `C2`-to-index carrier, families pushforward, boundary
  Dirac -- untouched, still the real wall, and the place the generation count actually lives.

So the standing obstruction is **matched in class but narrowed and split**: the gravity leg's block
is a clean, single, nameable soldering -- **strictly softer** than the fermion sector's `C2` wall,
and provably distinct from it (the soldering is a statement about the `so(9,5)`->`sp(32,32;H)`
connection embedding; `C2` is a boundary symbol-norm on the RS constraint surface). H23 confirms
`DEAD-ENDS.md`'s discipline: the identification is *not* forced, and the honest outcome is to name
the obstruction rather than manufacture a closure.

## RE-RANK signal

- **Does gravity go UNCONDITIONAL?** **No.** It stays **clear-modulo-one-soldering-postulate +
  mu_DW scale** -- a strong PARTIAL, but not unconditional. The sign is decided (H25), the ghost
  clears in the Krein sense (H23 C), the spin-lift is canonical (H23 A) -- what remains is a single
  structural assumption GU's dynamics does not supply.
- **Does H22-ship become #1?** **Yes.** The gravity leg is now as complete as it can be **without**
  the soldering dynamics: the residual is one sharply-named, natural assumption. That is exactly the
  right shape to **ship as a conditional theorem** -- "GU gravity is tree-level Stelle-clear with a
  positive, decoupled massive ghost, **conditional on the single soldering postulate**
  `pi = spin-lift(grad^gimmel)` and the overall scale `mu_DW`." H22-ship should write that
  conditional, with the soldering as the one honest, isolated assumption (not a list of gaps).
- **Precise next object.** Two, in order:
  1. **The soldering carrier:** a GU-internal dynamics or constraint that forces `pi` onto
     `spin-lift(grad^gimmel)` (or falsifies it). Candidate surface: does the tautological
     soldering form on `Y = Met(X)` plus a first-order (Palatini-type) variation of `|theta|^2`
     drive `pi` to the metric-compatible lift on-shell? That is the one move that would turn this
     PARTIAL into CONSTRUCTED. (It must not reduce to `theta=0`, which is acausal-trapped.)
  2. **`mu_DW`:** the one dimensionful scale, still the source-action overall normalization.
- **Do H5/H19 (entropic) rise?** **No.** Gravity's sign and positivity survived and strengthened;
  the Stelle reading is reinforced, not weakened.
- **Fermion/generation frontier unchanged.** The `C2`-to-index carrier remains the separate, harder
  wall; H23 leaves it exactly where the buildbench had it.

---

*Filed 2026-07-11. Wave 8, THE source-action swing. Reproducible:
`python tests/wave8/H23_source_action_construction.py` (exit 0, 10/10 PASS). Exploration-grade;
not promoted to canon. Adversarially graded: no forcing was manufactured, no target imported; the
honest outcome is a narrowed, precisely-named obstruction.*
