---
artifact_type: exploration
label: W191
status: "exploration (pre-registered W190 projected-block execution; conditional same-carrier branch; no canon, claim-status, H-number, bar, verdict, or posture movement)"
created: 2026-07-14
title: "W191 -- The projected I1B plus native-current block: one exact cross-sector relation, with the pole and reservoir sign still open"
verdict: "PARTIAL-BUILD / ONE CROSS-SECTOR RELATION DERIVED / PHYSICAL SPECTRUM AND RESERVOIR SIGN OPEN. At a source-first flat section, the displayed I1B law and W180 native current reduce to the typed quadratic block eps[tau q h + (1/2)tau C_T tau - kappa tau j] if, and only if, the shadow and record source use the same projected displaced-torsion carrier. Exact elimination gives Delta K = -(eps/C_T)(q,-kappa)^T(q,-kappa), hence rank(Delta K)=1 and Delta_hj^2=Delta_hh Delta_jj. This is a real target-free relation and a local selector-rank reduction. It is conditional on the same-carrier identification, because the repository does not yet contain the explicit projected shiab map, full C_T(k), or native reservoir two-point function. The Gaussian law shadow is in the shiab/Ricci class, not automatically the geometric |II|^2 construction. The physical pole, the retarded spectral sign, the favorable total Krein branch, and predictive timing remain open."
grade: "EXACT for the 22/22 symbolic checks once the typed one-mode block is fixed: stationary elimination, Schur complement, rank-one kernel, determinant relation, shiab-family Ricci coefficient, auxiliary-invertibility and full-zero gates, retarded-sign formula, selector Jacobian ranks, separate-carrier negative control, and fade-timing control. DERIVED-ON-DISPLAYED-ACTION for the quadratic I1B form at flat B0 and T0=0. STRUCTURAL / CONDITIONAL for projecting the full Cl(9,5) and Sp(32,32;H) objects to q(k), C_T(k), and j(k). OPEN for the gauge-reduced physical spectrum, reservoir spectral density, total C-operator, source normalization, and observed predictions."
depends_on:
  - explorations/W190-constraint-reduction-selection-synthesis-2026-07-14.md
  - explorations/W187-law-shadow-reduction-audit-2026-07-14.md
  - explorations/W188-boundary-selection-nonvacuity-2026-07-14.md
  - explorations/W189-law-shadow-boundary-countermodels-2026-07-14.md
  - explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md
  - explorations/W161-lens-foundational-action-2026-07-14.md
  - explorations/W167-reduction-direct-sign-alpha-beta-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - RESEARCH-POSTURE.md
scripts:
  - tests/W191_projected_i1b_source_block.py
---

# W191 -- Projected `I1B` plus native-current block

## 0. Result first

W190 pre-registered one calculation that had to return the reduction, reservoir, and selector-rank outputs
together. The calculation has now been executed as far as the displayed GU objects permit.

The result is a genuine partial advance:

```text
actual displayed I1B law                         W180 native record current
             |                                               |
             +------ same projected carrier tau? ------------+
                                      |
                                      v
                         rank-one induced joint kernel
                                      |
                                      v
                    Delta_hj^2 = Delta_hh Delta_jj
```

If the two channels share the same projected displaced-torsion carrier, the relation is exact and does not
depend on a target observation. If they use distinct carriers, the relation generically disappears. The
repository does not yet contain the explicit projection needed to decide that fork, so the result is
**conditional but discriminating**, not a completion by notation.

The strongest plain-English update is:

> The same hidden channel that makes the observable gravitational shadow can also carry the record source.
> If it does, gravity-like response and record response cannot be tuned independently: they are two faces of
> one rank-one exchange and must satisfy an exact relation. Whether that channel is dynamically healthy is a
> separate spectral question that the present local action does not answer.

## 1. Frozen calculation ledger

The following choices were fixed before evaluating the block.

| Item | Frozen choice | Scope |
|---|---|---|
| background section | constant flat `X4` section, flat `B0`, and zero displaced torsion `T0=0` | local quadratic test, not a cosmological solution |
| retained field | one gauge-reduced scalar/trace shadow amplitude `h(k)` | tests the disputed shiab/Ricci shadow |
| eliminated field | one projected displaced-torsion / connection-distortion amplitude `tau(k)` | the candidate shared carrier |
| source | one projected W180 native record-current amplitude `j(k)` | no generic physicist cubic vertex inserted |
| boundary conditions | compact-support fluctuations, then Fourier decomposition | boundary terms are not silently used as dynamics |
| base metric | flat `X4` momentum invariant `s=k^2` | distinct from field-space pairing |
| field-space metric | explicit Krein type `eps=+/-1` | not replaced by a positive-Hilbert removal construction |
| domain | modes for which the projected symmetric torsion kernel `C_T(k)` is invertible | zeros of `C_T` are reported as gates |
| selectors allowed | projected law form factor `q(k)`, source magnitude `kappa`, and declared Krein/spectral type | no observed count, pole, or damping target is fitted |

The generation `Z/3` versus `Z`-index fork is not used in this calculation. The gimmel/DeWitt metric and the
base `X4` metric remain distinct. The law being reduced is the displayed linear `I1B`; geometric `|II|^2` is
not inserted as a substitute.

## 2. The quadratic block from the displayed action

W161 displays the foundational action in the form

```text
I1B = <T, star_shiab(F_B + (1/2)d_B T + (1/3)[T,T]) + (1/2)T>_Y14.
```

Around `B0` flat and `T0=0`:

- `T star_shiab(delta F_B)` supplies the mixed quadratic term between the retained connection/metric
  fluctuation and displaced torsion;
- `T star_shiab(d_B T)/2 + <T,T>/2` supplies the projected symmetric torsion kernel;
- `T star_shiab([T,T])/3` begins at cubic order and does not enter this Hessian.

After the frozen one-mode projection, define

```text
q(k)   = projected shiab-curvature form factor,
C_T(k) = projected symmetric kernel from 1 + sym(star_shiab d_B),
eps    = the operative field-space Krein type.
```

W180's native current is `J^a = delta S_D / delta A_a`. Its bridge construction contains a linear coupling
between a connection-like mediator and `J`. On the **conditional same-carrier branch**, project that mediator
onto the same `tau` and write its unfixed normalization as `kappa`. The quadratic action is then

```text
S2(h,j,tau;k)
  = eps [tau q(k) h + (1/2) tau C_T(k) tau - kappa tau j].
```

This derivation does not discard `d_B T`. It packages its symmetric projection into `C_T(k)`. Therefore the
purely algebraic elimination used in W167 is valid only on modes where `C_T(k)` is invertible; if the derivative
piece makes `C_T(k)=0`, the reduced description fails at that mode and the full block must be retained.

## 3. Exact elimination and the cross-sector invariant

For one real projected mode, the `tau` equation is

```text
C_T tau + q h - kappa j = 0,
tau_* = (kappa j - q h)/C_T.
```

Substitution, equivalently the exact Schur complement, gives

```text
S_ind(h,j;k) = -eps/(2 C_T) (q h - kappa j)^2,

Delta K = -eps/C_T [[q^2,       -q kappa],
                    [-q kappa,  kappa^2 ]].
```

Thus

```text
rank(Delta K) = 1,
det(Delta K) = 0,
(Delta K_hj)^2 = Delta K_hh Delta K_jj.
```

The last equation is the decisive positive output. It is a target-free relation among a shadow coefficient,
a source-response coefficient, and their mixed response. It arises because all three are residues of one
carrier. Their magnitudes may change with `q`, `kappa`, and `C_T`, but they cannot vary independently.

This is not merely parameter counting. A matched separate-carrier control gives

```text
Delta K_separate = diag(-eps q^2/C_shadow, -eps kappa^2/C_source),
det(Delta K_separate) = eps^2 q^2 kappa^2/(C_shadow C_source) != 0
```

generically. So an explicit GU projection can falsify the same-carrier story.

## 4. Reduction / shadow output

### 4.1 What is fixed

W167's direct Gaussian reduction applies to the local invertible limit. For the shiab family

```text
J_ab = Ric_ab - t R g_ab,
c_R(t) = -2t^2 + t - 1/6.
```

Its discriminant is `-1/3`, so `c_R(t)<0` for every real `t` in the positive-pairing calculation. At the
Einstein value `t=1/2`,

```text
c_R = -1/6,
c_R,eff = -eps/(6 C_T(0))
```

under the present normalization. Therefore the Gaussian dynamic-law shadow is in the **shiab/Ricci class**.
It is not automatically the geometric bending functional `|II|^2`, which has a distinct Weyl-carrying origin.
A later commuting-reduction proof could relate the two, but this calculation does not assume that result.

### 4.2 What is not fixed

Let `A_h(k)` be the bare gauge-reduced retained block. The physical operator is

```text
K_eff(k) = A_h(k) - eps q(k)^2/C_T(k),
```

not the local coefficient by itself. Its physical poles require the explicit `q(k)`, `C_T(k)`, gauge projector,
source overlaps, sheet convention, and validity domain. Derivative mixing can introduce an additional full-block
zero; a dynamic `C_T(k)` can have its own zero and invalidate elimination. Consequently W191 does **not** decide
whether the apparent scalar is physical, gauge-null, a ghost, a tachyon, a resonance, or outside the effective
domain.

## 5. Reservoir / spectral output

The ultralocal real W180 bridge kernel produces a real induced term. It has **no damping width** and cannot by
itself select the absorbing versus reinforcing reservoir.

For a retarded nonlocal continuation

```text
C_R(s) = a(s) + i rho(s),
Im[-eps/C_R] = eps rho/(a^2 + rho^2).
```

This cleanly exposes the sign object: once a retarded convention is fixed, the self-energy sign is the relative
Krein/spectral sign `eps rho`. But W180's current identity derives neither the reservoir spectral density
`rho(s)` nor which field-space type supports it. The latest dressed-selfenergy work can determine the internal
anti-damping channel and an order-one threshold in its modelled lift; it does not derive this external native
current two-point function. The favorable total branch therefore remains conditional on the reservoir sign.

Magnitude cannot repair the wrong sign: scaling `kappa` changes the size of the term but not the sign of
`eps rho`. This agrees with the prior open-system negative control without importing its toy self-energy as the
native answer.

## 6. Selector-rank / compression output

For fixed `C_T`, the three induced coefficients are proportional to

```text
O(q,kappa) = (q^2/C_T, q kappa/C_T, kappa^2/C_T).
```

Their Jacobian has generic rank two, while the output space is three-dimensional. The exact determinant relation
therefore leaves prediction codimension one. Once the reduction calculation derives `q` and `C_T` rather than
allowing them to vary as boundary choices, the remaining response to the source magnitude `kappa` has rank one.

This is a real local compression, but it is **not** a proof that W188's entire eight-coordinate boundary package
has become one datum. It establishes one relation in one bridge sector. To reduce the global rank, the same
carrier must be constructed natively and its consequences must tie to independent holdout observables.

The latest everpresent-accretion result also needs a narrower reading. If

```text
r(N) = kappa0 sqrt(N)/g_kin,
```

then every `kappa0>0` eventually crosses a favorable fixed threshold, but

```text
N_* = (r_* g_kin/kappa0)^2.
```

So growth removes the magnitude from the **eventual-basin bit** only. The crossing epoch and every timing-sensitive
prediction still depend on the unbuilt magnitude. Saturation below threshold would also defeat eventual crossing.

## 7. What moved, and what did not

### Moved

- The W190 shared hinge is no longer only a verbal architecture. A native displayed-law/current block has an
  exact conditional Schur complement.
- The same-carrier branch forces one cross-sector invariant and one unit of prediction codimension.
- The law shadow is narrowed to the shiab/Ricci Gaussian class in the local invertible limit; `|II|^2` is not
  silently substituted.
- The unbuilt spectral datum is isolated as the retarded projected current two-point function, rather than a
  generic statement that the system is open.

### Did not move

- The full `Cl(9,5)` / `Sp(32,32;H)` projected shiab form factor `q(k)` is not built.
- The full symmetric displaced-torsion kernel `C_T(k)` and its zeros are not built.
- The W180 current has not been proven to occupy the same projected carrier as the shadow.
- The reservoir spectral density and favorable Krein type are not derived.
- No full-Hessian pole, total QFT `C`-operator, observed count, or measured prediction is closed.
- No canon, claim-status, H-number, bar, verdict, or research-posture state changes.

## 8. Falsifiers and the next exact object

The conditional joint story fails in this sector if any of the following occurs:

1. the explicit native projection places the W180 current and shiab shadow in orthogonal or independent carriers;
2. the three measured/derived response residues violate
   `(Delta K_hj)^2 = Delta K_hh Delta K_jj` after common normalization;
3. `C_T(k)` is noninvertible throughout the claimed domain or its full-block zeros produce an uncontrolled
   physical instability;
4. the derived retarded density has the reinforcing sign on the physical sheet;
5. allowing the remaining selectors restores full output rank and eliminates holdout relations.

The next exact object is now smaller and better posed than “unify the whole theory”:

> Construct the projected symmetric torsion kernel `C_T(k)` and the W180 current two-point spectral density
> `rho_J(k)` in one explicit `Cl(9,5)` representation and one declared observer section, then test whether the
> current and shiab shadow share the same carrier.

That single construction decides three things at once: whether the rank-one relation is native, whether auxiliary
elimination is valid on the physical domain, and which reservoir sign the actual current supplies.

## 9. Verification

`tests/W191_projected_i1b_source_block.py` passes **22/22** lightweight exact symbolic checks:

- 7 same-carrier elimination and Schur-complement checks;
- 5 shiab-coefficient and physical-pole-gate checks;
- 3 reservoir spectral-sign checks;
- 4 selector-rank and separate-carrier checks;
- 3 everpresent-growth scope controls.

**Final verdict: PARTIAL-BUILD / ONE CROSS-SECTOR RELATION DERIVED / PHYSICAL SPECTRUM AND RESERVOIR SIGN OPEN.**
