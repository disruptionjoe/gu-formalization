---
title: "Two-sided real I1B energy on a metric-decoupled compact phase core"
status: active_research
claim_verdict: exact_real_compact_core_two_sided_energy_with_all_order_formal_boundary_compatibility
doc_type: native_action_real_energy_result
created: 2026-10-09
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-real-energy.json
probe: tests/channel-swings/native_zorro_real_energy_probe.py
---

# The real restriction also has a two-sided compact-core energy obstruction

**Setting the imaginary packet to zero does not make the selected quadratic
energy semibounded on its natural compact phase core.** There are real
constraint-reduced fields with energy tending to either infinity, on both
stationary coupling branches. They satisfy the complete linearized metric
equation with zero metric perturbation and every finite-order formal
compatibility condition of the declared odd-Dirichlet boundary completion.
The proof uses a reflection character absent from the homogeneous metric
carrier, not freely variable metric momenta.

This is a theorem about a quadratic Hamiltonian and formal solution jets.
It does not construct a global evolution, select a physical domain, or
prove that a nonlocal admissibility condition must retain the core. Every
Hamiltonian completion that does retain it and agrees with this quadratic
form is unbounded above and below. The result binds the same selected
curved comm/symi/symi bosonic I1B reconstruction; it is not a universal GU
no-go or a test of the source's actual Spin(6,4) shielding proposal.

The [real primary reduction](native-zorro-real-packet-and-selection-2026-10-08.md)
and [imaginary compact-core theorem](native-zorro-constrained-energy-2026-10-08.md)
supply the algebraic inverse and local energy construction. The
[boundary constraints](native-zorro-boundary-constraints-2026-10-08.md)
remain correct: holding distortion jets fixed constrains five metric
momenta. The fields here vary in a different, metric-decoupled symmetry
sector. Classification: `SOURCE_NATIVE_ROUTE` within the stated
reconstruction.

```gu-typed-objects
result: real quadratic energy unbounded in both directions on a constraint-reduced compact core with zero metric forcing and all-order formal boundary compatibility
carrier: real Clifford one-form perturbations of the selected curved I1B background, homogeneous on the base spatial torus, in a specified finite reflection character LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: actual quadratic Noether Hamiltonian and reduced time symplectic form ON=compact_fibre_phase_core_with_declared_odd_Dirichlet_boundary_polarization
real_structure: source anti-involution fixed real grades 1,2,5,6,9,10,13,14; initial free field has grade 14 and no factor of i
grading: Clifford grade, primary kernel, finite reflection character and derivative order; no raw dimension read as a particle count
action_owner: source-action -- selected comm/symi/symi bosonic I1B reconstruction and explicitly declared boundary completion
target: failure of semibounded quadratic energy on this real compact core and on any energy-preserving completion containing it MAP-TYPE=restriction
```

## 1. Domain, symmetry and the complete metric equation

Keep `g*=diag(1,-1,-1,-1)`, time `x^0`, and the exact curved stationary
background of the predecessor. Use a flat spatial three-torus so that
base-homogeneous fields have finite spatial volume. Let `V` be a sufficiently
small fibre neighbourhood of `h0=diag(4,-1,-1,-1)`, invariant under the
three independent base spatial sign reflections. Every fibre metric is
Lorentzian there and `dt` has positive ambient square. Work at the
classical quadratic level. Compact support below means support strictly
inside `V`; the spatial torus has no boundary.

For signs `epsilon_i` let

```text
R_epsilon = diag(1,epsilon_1,epsilon_2,epsilon_3),
h -> R_epsilon^T h R_epsilon,
chi(epsilon) = epsilon_1 epsilon_2 epsilon_3.           (1)
```

The group is `G=(Z/2)^3`. It acts on the base coordinates and the induced
metric fibre, and by the induced Clifford-bundle action on distortion.
These are actual symmetries of the selected background, splitting and
action. Indeed the DeWitt metric is congruence invariant, the radial
vector and horizontal/vertical projectors are natural, and the connection
and trace constructions commute with this action. The combined ambient
Jacobian has determinant

```text
det(R_epsilon) det(Sym^2 R_epsilon)
  = det(R_epsilon)^6 = 1.                              (2)
```

Thus the ambient orientation and Hodge star are preserved even when the
base reflection reverses base orientation. The source real structure,
Clifford grading and time covector are preserved as well. No identification
with an unproved compact gauge shielding mechanism is involved.

The ten homogeneous base-metric components transform by the characters

```text
u_00, u_ii: 1;       u_0i: epsilon_i;
u_ij (i!=j): epsilon_i epsilon_j.                     (3)
```

None has character `chi`. The probe checks the complete ten-dimensional
character projector and, as a control, that a two-sign projector does
retain the expected off-diagonal metric component.

Let `P_chi=(1/8) sum_g chi(g) U_g` on distortion fields. The **full** mixed
operator `A=A3+A2`, its formal adjoint into the fibre-integrated metric
equation, and the action-derived primary recovery intertwine `G`. Therefore

```text
A^dagger t = 0 whenever P_chi t=t,                     (4)
```

for base-homogeneous fields of arbitrary time dependence. This annihilates
every metric receiver, including lapse and shift; it is not a calculation
with a frozen metric equation discarded. Translation invariance makes the
metric Euler expression homogeneous, so checking the homogeneous receivers
also checks the expression against arbitrary base test variations.
The boundary contribution to that metric equation is zero for our compact
interior fields and all their formal time derivatives.

The stationary real distortion operator preserves this character. Hence
`u=0`, with all its time jets zero, is consistent with the **complete
linearized coupled equations** on this character. The character sector
is not asserted to be a nonlinear truncation: two `chi` fields can source
the trivial character at higher order. This does not affect the quadratic
energy claim. The separate nonlinear bosonic restriction `J=0` remains
as proved in the predecessor.

## 2. Real energy after every distortion primary constraint

Use a smooth `G`-equivariant complement to the time kernel; a finite-group
average supplies an invariant auxiliary positive form for this choice.
Its use chooses coordinates only, not a replacement physical pairing.
Write the representative as `s`, the kernel frame as `N`, and

```text
C_R=E^0 partial_t+C_sp,
W=N^T V N,       f=N^T C_sp s,
t=s-N W^-1 f.                                         (5)
```

The geometric kernel lemma makes `W` algebraic, and all forty real
primary classes are invertible on either branch. The recovery is local,
uses finitely many fibre derivatives, is `G`-equivariant, and preserves
compact support. Choosing a different complement only changes the
representative of the same recovered phase data.

Unlike the imaginary coordinates, these fields have no common factor
of `i`. Their action and Noether Hamiltonian have signs

```text
L_R^(2)=+1/2 t^T E^0 dot t+1/2 t^T C_sp t,
H_R,red^(2)[s]=-1/2 integral (s^T C_sp s-f^T W^-1 f).   (6)
```

The plus sign of the second term in (6) is essential. Importing the
imaginary-packet Hamiltonian sign would reverse the labelled witnesses.
The density is the same positive coordinate density as in the predecessor.
On the character sector the metric and boundary energy terms vanish.
The reduced time form is nondegenerate, and its restriction to this real
one-dimensional group character remains nondegenerate: distinct real
characters are symplectically orthogonal, and their sum is the full space.
This is a classical symplectic statement, not a positive state norm.

## 3. Exact grade-14 coefficient witnesses

In an adapted orthonormal frame write
`Gamma=gamma_0 gamma_1 ... gamma_13` and take the free direction

```text
s0=e^0 Gamma.                                         (7)
```

This is in the real packet. It is a dynamical quotient direction: on its
complete 18-coordinate time block,
`N^T s0=0` and `s0^T E^0 E^0 s0=-13`. A smooth complement containing its
covariant extension can be used in (5). The grade-14 Clifford volume and
the time direction are preserved by the ambient orientation-preserving
symmetries above.

Consider a fibre derivative along either `e^4` or `e^11`, with ambient
squares `eta_4=+1`, `eta_11=-1`. Both belong to the vertical traceless
space, so no base spatial dependence is introduced. The complete
primary source is one on the kernel direction

```text
r_b=e^0 gamma_(all indices except b),    b=4 or 11.     (8)
```

The full target kernel has dimension twelve. The potential component
connected to this source has dimension eleven; the remaining direction
has no coupling to it. Let `G_b` be the ten-by-ten mass matrix on the
other directions and `h_b` the corresponding `H_v` column. Exact entries
give

```text
W_connected = [ lambda G_b       (v+8w) h_b ]
              [ (v+8w) h_b^T     -eta_b kappa ],
lambda = kappa-(116a+4c)/3,
h_b^T G_b^-1 h_b = -eta_b (2/33).                    (9)
```

Both sparse Clifford and independent 128-state matrix calculations
rebuild the entire source/target derivative blocks and all five target
primary potentials, not just the displayed corner. A symbolic vector
solves every row of `Wz=f`. Thus the principal coefficient in the real
Hamiltonian (6) is exactly

```text
tau = 116a+4c-3kappa,
Q_b = (1/2) f^T W^-1 f
    = -eta_b 11 tau / [2(11 kappa tau+2(v+8w)^2)].     (10)
```

On the isolated stationary branch write `a=kappa alpha(w)` and
`c=kappa beta(w)`. Define

```text
C = 11 kappa^2(116alpha+4beta-3)
    / {2[11 kappa^2(116alpha+4beta-3)+2(v+8w)^2]}.
0.388 < C < 0.389,        Q_b=-eta_b C/kappa.           (11)
```

The bounds follow from rational interval arithmetic on the exact
stationary root. They certify a nonzero numerator and denominator;
no numerical inertia inference is used. Reversing `a,c,kappa` reverses
each coefficient and preserves their opposition. An overall sign change
of the action also exchanges the two signs.

| Fibre derivative | Real energy principal coefficient, `kappa>0` |
| --- | --- |
| `e^4`, positive ambient square | `-C/kappa < 0` |
| `e^11`, negative ambient square | `+C/kappa > 0` |

These coefficients are background dependent, through (10). The earlier
imaginary witness's vanishing cubic columns is not being generalized.

## 4. Compact oscillatory families with the required character

Choose a generic point of `V` near `h0` with each `h_0i` nonzero. Its eight
`G` translates are distinct. A sufficiently small ball `B` around it has
eight pairwise disjoint translated closures inside `V`. Such points lie
arbitrarily close to `h0`; the two strict coefficient signs persist by
smoothness. The probe checks an explicit rational eight-point orbit,
but existence and sign persistence use this open-neighbourhood argument,
not an uncertified numerical radius.

On `B` choose a smooth phase `rho` whose differential at the centre is
one of the two covectors above. Shrink `B` so it is nowhere zero and the
corresponding coefficient retains its strict sign. For a nonzero smooth
cutoff `b` supported inside `B`, set

```text
s_n=s0 b sin(n rho),       s_tilde_n=P_chi s_n,         (12)
```

and use the **full** curved recovery (5), including every lower-order
connection term. On the original ball the projected field is `s_n/8`,
so it is nonzero. Locality and the disjoint supports imply the exact identity

```text
H_R,red[s_tilde_n]=(1/8) H_R,red[s_n].                 (13)
```

There are no cross terms between distinct translates, and the action
symmetry makes all eight diagonal energies equal. The same projection
also transports the recovered auxiliaries, so (4) holds exactly.

The leading term before projection is
`n^2 integral Q(h,d rho) b^2 cos^2(n rho) dmu`.
All other terms are bounded in absolute value by `C1 n+C0` on the fixed
support. This follows from (6): `f` has one derivative of `s_n`, and
`s_n^T C_sp s_n` has at most one. Integration by parts with a vector field
`X(rho)=1` bounds the oscillatory integral by `O(1/n)`. Consequently the
two families, after projection and exact recovery, obey

```text
H_R,red[s_tilde_n^-]=-c_- n^2+O(n),
H_R,red[s_tilde_n^+]=+c_+ n^2+O(n),    c_-,c_+>0.      (14)
```

The signs interchange on the mirror branch. This proves two-sided
unboundedness on phase data without presupposing an evolution theorem.

## 5. Every formal boundary compatibility condition is satisfied

Use the predecessor's odd-Dirichlet polarization, with no perturbation of
the odd natural field at the fibre boundary. In the character sector the
metric source vanishes and the nondegenerate reduced distortion time
form gives a local differential generator

```text
dot s=Tcal s,       Bcal s=(P_odd R s)|_boundary=0.    (15)
```

Here `R` denotes the primary reconstruction in the boundary owner, not a
base reflection. Both `Tcal` and `R` are finite-order differential operators
with smooth coefficients on `V`; the algebraic `W^-1` introduces no
nonlocal inverse. They commute with `G`. Therefore for every integer
`j>=0`, `Tcal^j s_tilde_n` stays in the same character and has support in
the same compact union of balls. In particular,

```text
Bcal Tcal^j s_tilde_n=0 for all j>=0.                 (16)
```

The formal time jets `partial_t^j s=Tcal^j s_tilde_n`, together with
`partial_t^j u=0`, solve the differentiated coupled bulk equations and
all boundary compatibility conditions to every finite order. The metric
force vanishes at every step by (4). These are not merely primary data
that fail `C1` or `C2` as the earlier zero-distortion acceleration test did.

An invariant differential core and compatible formal jets do **not**
prove that its formal time series converges, that a Cauchy solution exists,
or that a closed generator has been selected. The ambient signature is
ultrahyperbolic; the repository's PD-ULTRAHYPERBOLIC-DOMAIN distinction
still applies. A nonlocal physical restriction could exclude these data.
What (14)--(16) exclude is semibounded energy for any completion that
contains this compact core and keeps its action-derived quadratic form.

## 6. What is closed, and what remains open

The real-only restriction is no longer an escape from the **compact-core
classical quadratic energy obstruction** in this reconstruction. Ordinary
local boundary compatibility in the declared completion does not eliminate
the new witnesses. The metric-momentum restriction previously derived is
preserved; the new route does not need independent metric momenta.

The completed physical domain, nonlocal admissibility, observed quotient,
fermionic closure, nonlinear dynamics, quantum spectrum and the source's
actual shielding proposal remain separate questions. This result neither
admits the reconstruction as a source-owned action-root candidate nor
proves positivity impossible under every further physical selection.
LT-SM8 and LT-GR6b acquire stronger selected-realization native evidence but
remain NEEDS. INHERITANCE_BRIDGE concerns a different, physical BV/BRST
pairing and remains undischarged. SC-META-53 remains UNCERTAIN;
SC-ACT-06's source polarity and Euclidean-moduli claim do not move.
No canon promotion, hypothesis vote or publication readiness follows.

## Reproduction

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_real_energy_probe.py
```

The probe certifies the finite Clifford coefficients twice, complete
symbolic primary recovery, rational branch bounds, ambient orientation,
metric-character absence and an eight-point orbit. Equations (4),
(13)--(16) are the analytic symmetry/locality argument above, not claims
that a finite matrix probe proves global evolution. Independent engines
are coefficient corroboration, not an outside review of this theorem.
