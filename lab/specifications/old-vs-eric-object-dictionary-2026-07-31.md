---
title: "Old construction / Eric-guided source-action object dictionary"
status: active_research
doc_type: specification
created: 2026-07-31
run: lab/process/runs/GUH-20260731T132849Z-old-eric-ten-lens-council/run-plan.md
---

# Old/Eric object dictionary

This dictionary prevents future construction agents from reusing one word for
different mathematical objects. It is branch-local working discipline, not a
canon or claim-status update.

## Geometry and symmetry

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| `X^4` | physical base manifold | not the full field arena |
| `Y^14` | `Met(X^4)`, with vertical fibre `Sym^2 T*X` | not an exterior `Lambda^2 direct-sum Lambda^3` fibre |
| `G_DW` | trace-reversed DeWitt/Frobenius form, fibre signature `(6,4)` | not raw Frobenius `(7,3)` |
| `g_Y` | gimmel metric on `TY`, total signature `(9,5)` | not the base spacetime metric |
| `H` | native structure group, normally `Sp(32,32;H)` or a declared stabilizer | not the infinite-dimensional gauge group |
| `calG` | gauge group `Gamma(Ad P)` | acts on connections affinely |
| `V` | `Omega^1(Y,ad P)` | vector space of connection differences, not `Conn(P)` itself |
| `Conn(P)` | affine torsor modeled on `V` | requires an origin before being written as a vector space |
| `IG` | `calG semidirect V` with a frozen convention | must include acting group, module, action, and group law |
| `epsilon` | moving group/reduction/Stueckelberg field, once globally typed | not automatically the physical observer or full Cartan flag |
| `A_LC(epsilon)` | proposed connection on `P` induced from the moving Spin/stabilizer reduction and native Levi--Civita data | construction required; the LC connection on `FY` cannot be silently reused as an `H`-connection |

## Cocycle, tilted action, and distortion

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| `c0(g)` | E0 zero-jet coboundary `A0-Ad_g A0` | omits the derivative gauge term; finite shadow only |
| `q_A(g)` | full connection gauge cocycle `g dot A-A`, in `Omega^1(ad P)` | contains `dg`; linearizes to a covariant derivative |
| `tau_q(g)` | tilted embedding `(g,q(g))` | subgroup graph; it does not declare the action variation domain |
| `Theta_q` | left-tilted-invariant, right-adjoint difference field | general algebra works for any genuine cocycle; quotient level must be declared |
| double coset | set, differentiable stack, or action groupoid `[tau_L(calG)\IG/tau_R(calG)]` | not automatically `Conn(P)/calG`; stabilizers matter |
| standard contorsion | difference of two connections on the same geometric carrier, transformed together | already tensorial; not the same as ordinary torsion |
| torsion | soldering-dependent two-form `de+omega wedge e` | not an arbitrary adjoint-valued one-form |
| `T_omega` / distortion | primal adjoint-valued one-form, schematically `varpi-epsilon^-1 d0 epsilon` | not its Euler covector, VEV, stress tensor, or Higgs without further maps |

## Variation, current, and symplectic objects

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| `E_B`, `E_T` | Euler density-duals in `Omega^13(Y,ad*P)` | not primal one-forms |
| `E_epsilon` | group-trivialized Euler density-dual in `Omega^14(Y,ad*P)` | must be included in Noether identities |
| `J_D` | density-dual connection current from the connection-linear Dirac/operator term | not a Clifford-vector current and not yet a primal bridge field |
| `Q_F` | curvature-vertex response paired with `D_A delta A` | `J_F=D_A^!Q_F` after integration by parts plus boundary flux |
| `J_F` | curvature Euler current | must remain separate from `J_D` until the bridge is derived |
| `R_KG` | DeWitt/Hodge/Krein/adjoint pseudo-musical from connection covectors to primal one-forms | sign, domain, covariance, and boundary conventions are part of the construction |
| `Theta_L` | variational boundary potential of the complete 14-form Lagrangian | not the distortion `T_omega` |
| `omega_L` | covariant presymplectic current in horizontal degree 13 and field-space degree 2 | not a symplectic form until integrated over a declared 13-chain with flux control |
| BV form | canonical odd/`(-1)`-shifted cotangent form on `T*[-1]F` | not the Krein form or `omega_L` |
| moment map | Hamiltonian map for a specified symplectic action | finite spinor `mu`, generalized Atiyah--Bott `F wedge eta12`, and source distortion are different objects |

## Observation, domain, and datum

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| `s:X->Y` | observation section | not a 13D ambient Cauchy hypersurface |
| `L_s`, `R_s` | lift and restriction maps between reduced and admissible ambient fields | require retract and off-slice leakage equations |
| `Theta` | positive majorant/Cartan polarization for the Krein problem | not supplied by trace reversal alone |
| `D_partial` | closed Krein-self-adjoint boundary/normal domain | not an integer count or P2 |
| `Pi_adm` | admissible ultrahyperbolic mode/polarization constraint | may be nonlocal; covariance must be checked |
| `P1` | existing `Z/2` orientation datum | conditionally welded with P2 through `C_perp=K J_obs` |
| `P2` | orientation of the projected vertical RS symbol on the X-sector edges | already typed; boundary/polarization data are different unless an orientation-line map is built |
| `P3` | separate realized chiral-index/count datum in the right-`H`/relative-`KO` interface | not a decomposition, kernel dimension, `Z/3` class, or coefficient |

## Fermion, Higgs, and count objects

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| `Gamma` | Clifford contraction `V tensor S -> S` | its image, kernel, and product-rule blocks are representations, not observed generations |
| `S`, `im Gamma`, `ker Gamma` | three provenance sectors; `S` and `im Gamma` are spinor-type, `ker Gamma` is RS-type | Eric's first/second/third labels are not a count theorem |
| `384+1152+128` | exact even/even product-rule decomposition of `ker Gamma_14` | multiplicities, not chiral indices |
| `3E+ + 3E- + X_1536` | observer branching character before physicalization | a physical differential must remove mirrors and `X` |
| `0->1->13->14` | proposed shortened rolled sequence | not a complex until adjacent compositions vanish; length does not imply count |
| analytic index | Fredholm/domain-dependent difference of chiral kernels | not a block count; coefficient changes cannot move it without a domain/class transition |
| order-three class | torsion-valued invariant | cannot map additively to integer three without a separate bridge |
| vertical one-form channel | `(1,10)` under the observation split; a 4D Lorentz-scalar multiplet | not automatically the SM Higgs doublet |
| physical Yukawa bilinear | complete ordered `K`- or `C`-paired zero-order kernel | classify `K M`, not bare `M`; total projections precede factor interpretation |
| same-Weyl scalar | `S+ tensor S+ -> Lambda^0`, absent equivariantly | not the SW cross-chirality moment-map endomorphism |
| physical Higgs | moving `(1,2)_(1/2)` field with kinetic term, stable vacuum, potential, and Yukawa incidence | a vertical/ad-valued one-form is only its proposed parent |

## Cosmology

| symbol / phrase | type used here | relation and non-identifications |
| --- | --- | --- |
| VEV | expectation in a specified state or value at a selected classical stationary orbit | not any nonzero field configuration |
| `T_mn^obs` | observation-slice metric variation of the reduced action | not the distortion one-form |
| conservation | consequence of the complete Diff/gauge Noether identity on the required Euler shell with controlled flux | not isolated `D_A^*T=0` by slogan |
| heavy Higgs mode | gauge-doublet Hessian eigenmode of the shared parent | cannot also be the `H0`-scale cosmological eigenmode under an ordinary canonical two-derivative action |
| light cosmological mode | gauge-singlet radial/trace-relative eigenmode of the same parent, if constructed | separate mode does not require a separate parent field, but its splitting is a datum unless derived |
| `f0` | PP3 amplitude coordinate | must be emitted by the source action or named free before confrontation |
| PP3 | frozen conditional curve family and kill rules | stronger than Eric's qualitative dynamic-DE statement; existing DESI inputs have no confirmation weight |

## Standing semantic tests

Before using any shared word in a new claim, mark the pair
`SAME-OBJECT`, `HOMONYM`, or `UNCERTAIN` and name the relating map. In
particular:

- field versus Euler covector;
- connection current versus Clifford-vector current;
- bare operator versus K-paired bilinear;
- 14D scalar versus observation-slice scalar;
- sector label versus observed generation;
- domain/polarization versus P2;
- VEV versus stationary value versus stress tensor; and
- dynamic dark energy versus PP3's quantitative locus.
