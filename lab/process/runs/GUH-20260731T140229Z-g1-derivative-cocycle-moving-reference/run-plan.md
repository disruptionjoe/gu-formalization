---
run_id: GUH-20260731T140229Z-g1-derivative-cocycle-moving-reference
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: G1-DERIVATIVE-COCYCLE-MOVING-REFERENCE
starting_revision: 8ba7f98b2d6601443e1ee51536dfd731c200cc7c
opened_at: 2026-07-31T14:02:29Z
closed_at: 2026-07-31T14:12:52Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
---

# G1 derivative cocycle and moving reference

## Objective

Construct the first swing in the ten-lens guided scaffold. Replace E0's
finite zero-jet coboundary by the derivative-bearing connection cocycle;
construct the moving gauge-rotated Levi--Civita/reductive reference as an
actual connection; prove patch, lift, tilted-action, and stabilizer laws; and
state exactly what quotient is obtained. This is construction work on the
source action and its datum, not another search for whether those objects are
needed.

## Layer-0 precondition

| shared term | Eric-guided object | existing construction object | mark |
| --- | --- | --- | --- |
| `epsilon` | gauge transformation in the inhomogeneous gauge group | `epsilon_IG`, a moving Clifford-plane/reduction/soldering field | `HOMONYM`; relate by the gauge action on reductions, never identify |
| Levi--Civita connection | connection induced from the trace-reversed `(9,5)` metric and Spin reduction | RB3 `Gamma_epsilon^A0`, a reductive projection of a supplied `G`-connection | `UNCERTAIN`; equality requires an explicit compatibility equation |
| cocycle | derivative connection cocycle in `Omega^1(ad P)` | E0 pointwise coboundary `A0-Ad_g A0` | `HOMONYM`; E0 is the zero-jet summand |
| double coset | action groupoid/stack with stabilizers | set-level quotient rhetoric and a finite orbit fixture | `UNCERTAIN`; determine the exact quotient and comparison map |
| contorsion/distortion | difference from the moving gauge-rotated reference | N1 `theta=A-Gamma(epsilon_IG)-U` | `UNCERTAIN`; the extra independent `U` prevents identification |

## Native/comparator fork

- Native geometry: `Y^14=Met(X^4)` with trace-reversed
  `Sym^2 T*X` fibre signature `(6,4)` and total `(9,5)`.
- Native gauge group: `Sp(32,32;H)` with right-`H`-linear connection
  coefficients and Krein structure retained.
- Standard comparator: an arbitrary smooth principal `G`-bundle with a
  reductive `H`-reduction. Any obstruction found there must be checked on the
  induced native Spin bundle before being called a GU obstruction.

## Fields and declared choices

1. `P -> Y`: native principal `G=Sp(32,32;H)` bundle.
2. `epsilon_red`: section of `P/H`, locally lifted by `u_i`; this is the
   moving reduction, not a gauge transformation.
3. `g in Gau(P)`: gauge transformation.
4. `A_LC(epsilon_red)`: induced `G`-connection from the native
   Levi--Civita Spin connection when `P=Q_Spin(Y) x_H G`.
5. `Gamma_epsilon^A0`: explicit reductive-reference rival for a supplied
   transforming connection `A0`.
6. `q_A(g)=A-g dot A`: fixed-reference derivative cocycle under the declared
   left gauge convention.
7. `tau_A(g)=(g,q_A(g))` and `Theta_A`, together with their moving-reference
   conjugation and patch laws.

No coefficient, basis, regulator, boundary condition, Cartan flag, VEV,
mass, generation count, or cosmological amplitude may be added during G1.

## Pre-registered expected verdict

The derivative cocycle should remain a genuine 1-cocycle and preserve the
tilted displacement algebra. A moving reference should exist without new
local data on the induced native Spin bundle, but an arbitrary `G`-bundle
should retain the topological existence of an `H`-reduction and its sector as
a global condition. The moving family of tilted subgroups is expected to be
a subgroupoid/group-bundle, not one fixed subgroup. Its double quotient is
expected to reduce to an adjoint quotient of distortion fields with matching
stabilizers, not automatically to `Conn(P)/G` after the reduction field is
kept.

## Kill conditions

1. **Jet plant:** choose `g(y0)=1` and `dg(y0)!=0`. If the proposed cocycle
   vanishes, it is still the zero-jet shadow and G1 fails.
2. **Cocycle:** failure of `q_A(gh)=q_A(g)+Ad_g q_A(h)` kills the convention.
3. **Lift plant:** dependence of `A_LC(epsilon_red)` on `u_i -> u_i h_i`
   kills the reference construction.
4. **Patch plant:** failure to transform as a connection on overlaps kills
   global descent.
5. **Moving covariance:** failure of
   `A_ref(k epsilon)=k dot A_ref(epsilon)` or of the conjugated cocycle law
   kills the moving packet.
6. **Right-H/native fork:** a construction requiring complex-linear
   coefficients that do not commute with right quaternionic multiplication
   kills native transfer.
7. **Fixed-plane plant:** a bare `-du u^-1` reference must fail lift descent;
   if it passes, the matcher is vacuous.
8. **Stabilizer:** mismatch between double-action stabilizers and adjoint
   stabilizers kills the quotient claim.
9. **Quotient overclaim:** identifying the result with `Conn(P)/G` while an
   independent reduction/reference field remains kills the claimed
   equivalence.
10. **Count leak:** no cocycle, orbit, stabilizer, or quotient component may
    be read as chirality, index, or observed generation count.

## Constraint-surplus policy

The coefficient-one derivative term is fixed by the declared connection
transformation law, not counted as a discovery. Cocycle, tilted homomorphism,
and left/right covariance are algebraically dependent and will not be counted
as three independent constraints. Global surplus remains uncomputable until
the existence/selection freedom of the reduction and the LC-versus-`A0`
compatibility are priced.

## Planned outputs

- a typed global packet specification;
- a construction/adjudication dossier;
- a machine-readable certificate;
- an exact derivative-jet, lift, patch, and stabilizer probe with planted
  failures;
- roadmap/navigation updates; and
- validation, commit, push, and a closing receipt.

## Boundary

No global source action, native bosonic Shiab, complete Noether identity,
ambient domain, stationary orbit, Higgs, mass, index, count, cosmological
amplitude, or PP3 result is claimed by this swing.

## Completed result

G1 passed conditionally.

1. The full first-jet connection cocycle
   `q_A(g)=A-Ad_g(A)+(dg)g^-1` obeys the exact cocycle law and retains the
   tilted homomorphism and left-invariant/right-adjoint displacement.
2. The source gauge transformation and the moving reduction/soldering field
   are confirmed Layer-0 homonyms. Their constructed relation is the gauge
   action on the reduction, not field identity.
3. The native Levi--Civita Spin connection extends through an LC-equipped
   moving reduction with exact lift independence and gauge/patch covariance.
   The RB3 `A0`-induced reductive rival agrees only under the explicit
   equation `pr_h(u^-1 A0 u+u^-1 du)=omega_LC`.
4. The reference family conjugates the tilted subgroups and distortion maps
   across patches. It is a subgroupoid/group-bundle over the reduction field,
   not one frozen subgroup.
5. At fixed reference the two-sided tilted action groupoid is the adjoint
   quotient `[Omega^1(ad P)/G]`, with exactly matching stabilizers. It is not
   automatically `[Conn(P)/G]`. With a moving reference, the reduction field
   remains in `[E_ref x Omega^1(ad P)/G]` until a further equivalence removes
   it.
6. Native right-`H` and trace-reversed `(6,4)`/Spin compatibility passed. No
   hidden complex polarization or raw `(7,3)` substitution entered.

The exact plants rejected the zero-jet cocycle, frozen patch reference, bare
Maurer--Cartan lift, inert `A0`, arbitrary LC identification, generic
stabilizer, false connection-quotient equivalence, and fake quaternionic
commutativity.

## Constraint and datum disposition

The connection transformation law owns the coefficient of `dg`; it is not
counted as a fitted or derived constraint. The cocycle, tilted homomorphism,
and covariance laws are algebraically dependent. No positive global surplus
is claimed.

The native induced bundle needs no additional local reference coefficient.
The global reduction component, its boundary/variation owner, and the choice
between native LC and `A0`-induced graphs remain explicit G2 debits. None is
identified with P1, P2, or P3.

## Durable outputs

- `explorations/g1-derivative-cocycle-moving-reference-2026-07-31.md`
- `lab/specifications/g1-global-tilted-moving-reference-packet-2026-07-31.md`
- `lab/process/g1-derivative-cocycle-certificate.json`
- `tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py`
- branch-local roadmap and navigation updates

## Validation

| command | result |
| --- | --- |
| `python3 tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py` | `19 exact + 10 planted = 29 PASS` |
| `python3 tests/channel-swings/weinstein_guided_source_action_probe.py` | `14 exact + 4 planted = 18 PASS` |
| `python3 tests/channel-swings/old_vs_eric_ten_lens_contract_probe.py` | `19 exact + 10 planted = 29 PASS` |
| `python3 tests/channel-swings/rb3_moving_soldering_spinzero_probe.py` | all controls pass |
| `python3 tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py` | all controls pass |
| `python3 tests/channel-swings/rb4_observer_cartan_moving_family_probe.py` | all controls pass |
| `python3 -m json.tool lab/process/g1-derivative-cocycle-certificate.json` | valid JSON |
| `python3 process_gates/tests_root_readme_inventory_audit.py` | `4/4 OK` |
| `find tests/channel-swings -maxdepth 1 -type f -name '*.py' \| wc -l` | `154`, matching `tests/README.md` |
| `git diff --check` | exit `0` |

## Next swing

G2 must declare the full action field space before varying it. The recommended
default is `A_ref=A_LC(epsilon_red,g_DW)` as a graph-constrained composite,
with `epsilon_red` varied and the `A0` reductive graph kept as a hostile
comparator. G2 must also construct the native bosonic Shiab density-dual map
and carry the first-derivative `epsilon_red` boundary obligation forward.
