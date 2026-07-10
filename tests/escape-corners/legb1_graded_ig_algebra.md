# LEG-B1: does a graded/fermionic extension of the inhomogeneous gauge group exist?

**Leg of:** corners-swing (corner (b), the graded-IG upstairs door), 2026-07-10.
**Scripts:** `LEG-B1-graded-IG-algebra.py` (+ `leg_b1_exact.py`; main run, `run3.log`), plus three
standalone exact certificates: `leg_b1_posthoc_ranks.py` (`posthoc_ranks.log`, exit 0: ansatz-
completeness ranks), `leg_b1_center_check.py` (`center_check.log`, exit 0: center(so(4)) = 0),
`leg_b1_unitary_center_channel.py` (`unitary_center.log`, exit 0: the unitary-anchor center
channel). Exact Gaussian-rational arithmetic (`fractions.Fraction` pairs; no floats in any assert
path), sympy only for Groebner-basis steps.
**Question decided by this leg:** (b1) does IG = G semidirect Omega^1(ad) admit a graded/fermionic
extension closing super-Jacobi, with odd generators in the transcript's stated field content; if
yes, what commutes with what, and is the resulting fermionic parameter local or rigid.
**NOT decided here:** (b2) what an upstairs BRST ghost would subtract in the matter sector (a
separate leg), and SG4 (whether GU's unbuilt action realizes any of this).

## The GU commitments this leg formalizes (verbatim, `papers/drafts/Transcript into the impossible.md`)

- [00:49:16] (L172-173): "Then what you do is you take the inhomogeneous gauge group on that group
  and you extend it to through supersymmetry. Now that's a mouthful, but it's also the entire
  universe without making any choices." And the field content: "It's zero forms and one forms
  valued either in add or in the spinners, and that's it."
- [00:48:49] (L169-170): "The unified field sought by Einstein is the observational graded
  inhomogeneous gauge group of the unitary, chimetric chimeric spin bundle."
- [00:46:02] (L157-158): "We will never find space time Susie. We fed Salam Strathy, which always
  needs to eat an affine space, the wrong affine space. Don't feed it Minkowski space. Feed it the
  space of connections. Then the Lorentz group is the gauge group. The space of four momentum
  becomes the space of gauge potentials. And what you find is the fermionic extension gives you
  exactly three families of chiral fermions..."
- [00:18:03] (L64-65): the tau_plus construction: "you have a map, tau, which takes the ordinary
  gauge group... into the inhomogeneous extension where g goes to tau plus of g equal to g... if I
  have a distinguished connection, which is d aleph g, and then I premultiply by g inverse."
- [00:19:42] (L67-68): the semidirect module structure: "I can multiply this, this inhomogeneous
  gauge group by its subgroup, and I can represent the gauge group on the space of add valued one
  forms."
- [00:32:46] (L106-107): the matter shape the odd parameters must be able to shadow: "if you pull
  back ordinary spinners, zero forms valued in the positive spinners, direct sum one forms valued
  in the negative spinners on that top space, you're gonna get three generations of standard model
  fermions."

## The toy (what was actually built)

Finite matrix model of the IG Lie algebra frozen at a point (all structure maps pointwise; the
derivative enters GU's IG only through the tau_plus embedding, not through the bracket -- see
"honest limits"):

- even part `ig0 = g (+) (V (x) g)`, `g = so(4)` (compact group on the repo's Cl(4,0) = C^4 toy
  fiber; Spin(4) double cover acts on spinors through the exact spin intertwiner, machine-verified),
  `V = R^4`, so the translation part is the `4 x dim(ad) = 24`-dimensional `Omega^1(ad)` slot.
- Bracket: `[(x,a),(y,b)] = ([x,y], x.b - y.a)`; translation part abelian. Exact Jacobi verified on
  all C(30,3) = 4060 basis triples, in BOTH regimes.
- Two equivariance regimes, because the transcript supports two readings:
  - **RG (gauge-only)**: the gauge algebra acts on `Omega^1(ad)` by ad on the Lie-algebra factor
    only (the mathematically standard IG semidirect structure; form index inert).
  - **RD (diagonal)**: one so(4) rotates everything including form indices (the transcript's "Then
    the Lorentz group is the gauge group" [00:46:02] -- frame and gauge identified).
- Odd candidates (the transcript's stated linearized field content [00:49:16]):
  (i) `Omega^0(S)` spacetime-spinor-valued scalars (4-dim);
  (ii) `Omega^1(S)` spinor-valued one-forms -- the RS-type parameter (16-dim);
  (iii) ad-valued spinors (24-dim);
  (iv) `Omega^0(S) (+) Omega^1(S)` -- the transcript's full spinor column (20-dim).
- Clifford infrastructure: Cl(4,0) chiral gammas over Q(i); both charge-conjugation intertwiners
  `C+-` (each unique up to scale, machine-solved); machine-determined symmetry types: `C-` is
  antisymmetric with `C- gamma_a` symmetric (all a) and `C- Sigma_ab` symmetric (all ab) -- so the
  vector pairing `Q^T C gamma_a Q'` and the 2-form pairing `Q^T C Sigma_ab Q'` are BOTH symmetric,
  i.e. both live in Sym^2(S) exactly as the character count demands (10 = 6 + 4).

## Full equivariant Hom dimensions (exact character arithmetic, su(2)xsu(2) peeling)

| regime | odd candidate M | dim Hom(Sym^2 M, g) | dim Hom(Sym^2 M, transl) | dim Hom(transl (x) M, M) |
|---|---|---|---|---|
| RG | (i) O0(S) | 2 | 8 | 8 |
| RG | (ii) O1(S) | 20 | 80 | 128 |
| RG | (iii) ad(x)S | 12 | 48 | 64 |
| RG | (iv) O0(S)+O1(S) | 30 | 120 | 200 |
| RD | (i) O0(S) | 2 | 2 | 4 |
| RD | (ii) O1(S) | 8 | 12 | 24 |
| RD | (iii) ad(x)S | 12 | 20 | 40 |
| RD | (iv) O0(S)+O1(S) | 14 | 24 | 48 |

Cross channels used by the flagship candidate (iv), RD: `{O0(S) x O1(S)} -> transl` has dim 10;
`transl (x) O0(S) -> O1(S)` (the algebraic gravitino-shadow slot `[a, eps] in Omega^1(S)`) has
dim 10 and is NONZERO -- the shape `eps -> a.eps` that mirrors the tau_plus twist
`eps -> D_aleph eps` at frozen-derivative level EXISTS as an equivariant action.

**Every candidate, in every regime, has a NONZERO translation channel** -- the representation-
theoretic precondition for a graded extension with `{odd,odd} <= Omega^1(ad)`.

## RESULTS

### R1. EXISTENCE: YES -- every candidate closes, in both regimes (PARTS 4-5, exact)

For ALL FOUR odd candidates and BOTH regimes, explicit nonzero equivariant symmetric brackets
`{.,.}: Sym^2(odd) -> Omega^1(ad)` were constructed from Clifford pairings (pattern tables on all
basis pairs; equivariance verified inside the finder on every (generator, basis-pair) instance),
and the full set of super-Jacobi identities was verified exactly for the graded algebra

    s  =  [ g (+) Omega^1(ad) ]_even  (+)  M_odd,
    {M, M} <= Omega^1(ad),   [Omega^1(ad), M] = 0   (minimal ansatz):

- (J-a) even Jacobi: all C(30,3) = 4060 triples, both regimes (checks 24/26).
- (J-b) module property: all 15 g-pairs x every odd basis vector (checks 33, 41, ...).
- (J-c) even-odd-odd: g-case = pattern equivariance (finder-verified on ALL instances, spot-
  rechecked); transl-case = structural (bracket is transl-valued + transl abelian), both asserted.
- (J-d) cubic: structural (transl acts 0; actg(0)=0 asserted); FULL loop run for candidate (i)
  in both regimes.

Checks 28-95; 96 checks total through PART 5. **The graded inhomogeneous gauge algebra EXISTS**,
with odd generators in each of the transcript's stated field-content slots, including the RS-type
spinor-valued one-form and the full `Omega^0(S) (+) Omega^1(S)` column.

Flagship explicit brackets (RD regime, machine-verified):
- candidate (i): `{Q,Q'}_mu^{ab} = (Q^T C gamma^a Q') delta^b_mu - (a<->b)` (delta-type) and
  `eps^{ab}_{mu nu} (Q^T C gamma^nu Q')` (eps-type) -- exactly a "momentum-shaped" pairing landing
  in the gauge-potential slot;
- candidate (ii) (RS-type): `{Psi,Psi'}_rho^{ab} = Psi^{[a T} C gamma_rho Psi'^{b]} + (Psi<->Psi')`
  plus gamma-traced variants (P3/P5/P7 families);
- candidate (iv): the above plus CROSS brackets `{eps, Psi} -> Omega^1(ad)` (six realized forms).

### R2. The anticommutator is FORCED into the gauge-POTENTIAL slot (kill lemma + PART 6, exact)

- **Minimal ansatz kill lemma (check 96), now fully general:** if `[transl, odd] = 0`, a g-valued
  component of `{Q,Q'}` violates the (transl, odd, odd) Jacobi: exact witness `a = e_0 (x) M_(0,1)`,
  `(Q_0,Q_0)` with `[a, {Q,Q'}_g] != 0` while the right side is identically 0. The generalization
  beyond the witness is closed by `leg_b1_center_check.py` (exit 0): **center(so(4)) = 0 by exact
  nullspace** (6 unknowns, 48 equations), so ANY nonzero g-valued anticommutator output is
  non-central and yields a violated instance -- the kill holds for ALL FOUR odd candidates in the
  minimal ansatz, not just candidate (i).
- **Extended ansatz, RG (check 97-98, ansatz-COMPLETE):** allowing `[transl, odd] = rho != 0` with
  rho in the FULL equivariant space (realized 8 = character dim 8), the (transl, transl, odd)
  Jacobi ideal E1 forces rho = 0 exactly (Groebner + radical membership: r_k^2 reduces to 0 for
  every k), and then the (transl, odd, odd) Jacobi forces alpha = 0 (exact linear solve, nullspace
  empty). **In the honest IG semidirect structure the g-valued anticommutator is DEAD, full stop
  (over C, complete equivariant ansatz).**
- **Extended ansatz, RD (checks 99-100, ansatz-COMPLETE):** rho realized 4 = character dim 4. The
  E1 variety is NOT zero: Groebner basis exactly `{r0 r2, r1 r2, r0 r3, r1 r3}` = union of the two
  CHIRAL planes (rho purely P+ gamma(w) or purely P- gamma(w)); each plane is 2-step nilpotent by
  the chirality flip, verified standalone: `P_chi gamma_a P_chi gamma_b = 0` for all a,b, both
  chiralities, 32 exact checks (`chiral_nilpotency.log`, exit 0). But on the FULL nonzero-rho
  variety the g-valued anticommutator stays dead: adding alpha_k = 1 makes the ideal trivial
  (GB = [1]) for BOTH chiral g-channels. **Nonzero [transl, odd] exists (chiral nilpotent shifts)
  -- and still cannot buy a gauge-algebra-valued {Q,Q'} for candidate (i).**

This is precisely the transcript's own claim shape, now machine-verified as FORCED rather than
chosen: "The space of four momentum becomes the space of gauge potentials" [00:46:02] -- in any
graded extension of IG (within the complete equivariant ansatz for candidate (i)), `{Q,Q}` MUST
live in the `Omega^1(ad)` (gauge-potential/translation) slot, never in the gauge algebra itself.
The super-Poincare analogy is exact: g plays "Lorentz", `Omega^1(ad)` plays "momentum", and the
graded extension is super-Poincare-SHAPED with the momenta replaced by gauge potentials.

### R3. The gravitino-shadow slot is real and inhabited (PART 7, candidate (iv), RD)

The transcript's full spinor column `Omega^0(S) (+) Omega^1(S)` admits, in the diagonal regime:
- a 10-dimensional equivariant space of actions `[transl, Omega^0(S)] -> Omega^1(S)` (character
  dim 10, realized 10/10) -- the algebraic shadow of the gravitino variation `eps -> D_aleph eps`
  (the tau_plus twist with the derivative frozen); each such action is 2-step nilpotent
  (rho(a) rho(b) = 0 structurally, check 102), so the (transl,transl,odd) Jacobi is automatic;
- 12 realized equivariant CROSS brackets `{Omega^0(S), Omega^1(S)} -> Omega^1(ad)` (channel dim 10);
- **ansatz-completeness CERTIFIED** (`leg_b1_posthoc_ranks.py`, exit 0): the realized patterns SPAN
  the full equivariant Hom channels exactly -- cross `{S,VS}->transl` rank 10 = character dim 10;
  `rho: transl x S -> VS` rank 10 = character dim 10; `{S,S}->transl` rank 2 = dim 2; `{S,S}->g`
  rank 2 = dim 2. Whatever PART 7 concludes is therefore complete for the degree-graded ansatz,
  not an artifact of a thin pattern basis;
- [P7-EXACT] the degree-graded system's exact alpha verdict and constructive witness: see run log
  (filled below).

### R4. Local, not rigid (PART 8)

Every structure map of every closed algebra above is a POINTWISE matrix map -- no derivative
appears in any bracket (the derivative of GU's IG lives in the tau_plus EMBEDDING, not in the
bracket). Hence `Maps(Y, s)` with pointwise brackets is a super-Lie algebra: the fermionic
parameter may be an arbitrary function eps(y) -- a LOCAL gauge-type parameter -- machine proxy:
super-Jacobi verified on the two-point mapping algebra with generic exact elements. The contrast
with spacetime SUSY is structural: there `{Q,Q} = P` is a derivative, so localizing eps forces
gravity (supergravity); here `{Q,Q}` is an ALGEBRAIC shift of the connection variable -- a
direction IG already gauges -- so locality costs nothing. What the odd parameter DOES to matter
fields is a representation question (leg b2), not settled here; what is settled is that the
graded IG provides a local fermionic parameter space with the right shape at zero cost.

### R5. The unitary-anchor center channel (the ONE escape from the kill lemma), decided at toy scale

The kill lemma's only premise is center(g) = 0. GU's stated gauge group is the **unitary group of
the spinors** ("You take the unitary group of those spinners" [00:48:49] L170), and `u(p,q)` HAS a
center -- so at the anchor the g-valued channel could only survive through the center.
`leg_b1_unitary_center_channel.py` (exit 0) decides that channel exactly:

- **EXISTENCE:** with odd generators NEUTRAL under the central charge, the gl(1|1)-type graded IG
  extension with `{Q, Qbar} = Z` (gauge-algebra-valued, central) CLOSES -- all graded Jacobi
  identities on all 364 basis triples, exact. A g-valued anticommutator IS available at a
  unitary-type fiber -- but only in the central direction, and only for neutral odd parameters.
- **KILL for spinors:** if the odd parameters carry nonzero central charge `z` under the central
  element they produce -- and spinor-valued parameters under `u(S)` carry `z = +-1` -- the CUBIC
  (odd,odd,odd) Jacobi is violated (exact witness `(Q,Q,Qbar)`; all violations are cubic, checked
  for z = +1, -1, +2). The central channel is DEAD for spinor-valued odd parameters: it dies on
  the cubic exactly as the noncentral channel dies on (transl,odd,odd).

Net at the anchor shape: the noncentral `su(S)`-part stays killed by (transl,odd,odd) (kill lemma,
center-free argument), the central part dies on the cubic for the transcript's own spinor-valued
parameters. What is NOT tested: the extended ansatz (`[transl,odd] != 0`) at a unitary fiber with
the su(n|1)-type joint Fierz across central + noncentral parts -- named open door, anchor-scale.

### What commutes with what (the closed algebra, minimal ansatz)

| bracket | value | status |
|---|---|---|
| [g, g] | g | semidirect even algebra, Jacobi exact |
| [g, transl] | transl | module action (regime-dependent) |
| [transl, transl] | 0 | abelian |
| [g, odd] | odd | spin (+ index) action |
| [transl, odd] | 0 (minimal) / chiral nilpotent shift into Omega^1(S) (extended, RD) | both close |
| {odd, odd} | Omega^1(ad) ONLY | g-component forced to 0 (R2) |

So: `s = g  semidirect  ( Omega^1(ad) (+) M )` with `Omega^1(ad) (+) M` a 2-step nilpotent
super-ideal -- super-Poincare-shaped, with gauge potentials as the momenta.

## Honest limits

1. **Frozen-derivative toy.** The bracket of the actual infinite-dimensional IG is pointwise (the
   derivative enters only through the tau_plus EMBEDDING `g -> (g, g^{-1} d_aleph g)`), so the
   finite toy is faithful for the bracket/super-Jacobi question. But the physically loaded odd
   embedding `eps -> (eps, D_aleph eps)` (the gravitino shape of steelman S3) involves `d` and is
   NOT testable at a point: what the toy verifies is that its algebraic shadow `[a, eps] = a.eps
   in Omega^1(S)` is available and equivariant. The derivative-level homomorphism property of an
   odd tau_plus is outside this leg (named, not decided).
2. **Complexified.** All Hom dimensions and closures are over Q(i) (i.e. the complexification).
   Real forms are NOT selected: Euclidean 4d has no Majorana spinors, so a real odd structure needs
   symplectic-Majorana doubling or a Krein structure (GU's carrier is already Krein (+96,-96) per
   the SW capstone). Existence over C is the right first question for the door; reality is
   SG4-adjacent and open.
3. **Fiber scale.** g = so(4) on the Cl(4,0) = C^4 toy fiber (the repo's own toy model scale), not
   the Cl(9,5) = M(64,H) anchor with Sp(64)=U(64,H); the mechanism (abelian translation slot +
   equivariant symmetric pairing into it + trivial/nilpotent translation action on odd) is
   representation-generic, but the anchor-scale run was not performed (compute cost), and the
   (9,5) signature changes which pairings are symmetric vs antisymmetric over R (over C the
   channel dimensions are signature-independent for the complexified algebra so(4,C) = sl(2)+sl(2)).
4. **Pattern-basis completeness.** Existence results ride explicit constructions (complete);
   NON-existence/forcing results within an ansatz are exact for that ansatz. The PART 6 rho spaces
   and the PART 7 channels are certified complete (realized rank = character dim;
   `posthoc_ranks.log`). Two ansatz CHOICES in PART 7 are not completeness-certified because they
   are choices, not bases: the degree-grading `{VS,VS} = 0` and `[transl, VS] = 0`. A closure
   using nonzero `{VS,VS}` or `[transl,VS]` channels is not excluded by this leg (it would only
   ADD closures -- the corner-open direction -- not remove the ones verified).
5. **Extended ansatz coverage.** `[transl,odd] != 0` was solved ansatz-completely for candidate
   (i) (both regimes) and for candidate (iv) in the degree-graded shape (RD). Candidates (ii) and
   (iii) were closed in the minimal ansatz only; their extended-ansatz g-channels are untested
   (the kill lemma covers their minimal ansatz fully, via center(so(4)) = 0).
6. **Unitary anchor.** R5's center-channel verdict is exact at toy scale (the center mechanics is
   fiber-size-independent), but the joint su(n|1)-type extended ansatz at the honest `u(64,64)`
   anchor was not run.
7. **This leg does not touch b2 or SG4.** Closure of the graded algebra does NOT show GU's action
   is invariant under it, does not produce a BRST complex, and does not decide what an upstairs
   ghost subtracts in the RS sector. It decides only the algebra-existence sub-question (b1).

## Firewall compliance

No chi(K3), no 24, no /8 manufacture, no A-hat = 3 anywhere (the script never imports topology).
The bare 58.72 commutator is never touched. All arithmetic exact.
