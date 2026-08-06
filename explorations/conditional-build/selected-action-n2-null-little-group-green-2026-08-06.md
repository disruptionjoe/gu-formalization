---
artifact_type: exploration_result
created: 2026-08-06
status: EXACT_N2_HELICITY_ONE_NOT_SPIN_TWO__LOCAL_GREEN_FLUX_LIVE__SECOND_LAYER_OWNER_MAP_PRIMARY
ledger: lab/process/conditional-physics-ledger-v0.37.json
registry: lab/process/selected-action-n2-null-little-group-green.json
---

# N2 null little-group and principal Green-flux typing

## Outcome

The completed first-layer grade-one source action does not recover the
graviton at its only positive two-extra-mode coefficient locus.

The `N2` kernel is exactly six-dimensional: four diffeomorphism directions
plus two source modes. The transverse rotation that fixes the null covector
acts on those two quotient modes by

```text
J_phys = [ 0 -1]
         [ 1  0]
```

and therefore

```text
J_phys^2 = -I,
char(J_phys) = x^2+1.
```

That is the real helicity-`±1` module. A massless spin-two pair would have
`J_phys^2=-4I` and characteristic polynomial `x^2+4`. The earlier count of
two was real, but it was a multiplicity statement, not a spin statement.

The same two modes carry a nondegenerate, gauge-descending local principal
Green flux. Its finite matrix is a scalar multiple of the identity and is
definite at the positive `N2` embedding. This makes the failure cleaner: the
modes are not merely an isotropic numerical accident, but their representation
is wrong for the graviton. A live flux cannot repair wrong helicity.

The preregistered ending `N2_WRONG_HELICITY` fires. No value of `kappa_1` is
selected, and no residue or quotient is booked.

## Layer 0

Five objects remain separate:

1. a two-dimensional algebraic kernel after gauge;
2. its representation under the compact `SO(2)` part of the null stabilizer;
3. the principal Green flux obtained by differentiating the full filtered
   source symbol;
4. a covariant presymplectic or BFV quotient;
5. a global right-`H`/Krein physical domain.

Only items 1--3 are constructed here. In particular, “two modes” does not
mean “two graviton polarizations,” and a definite finite flux does not mean
positive energy or unitarity.

## Source return

`SOURCE-CONFIRMS_AND_SOURCE-SILENT`.

The public material confirms that a Shiab member belongs to the bosonic action
and that the construction aims at an upstairs replacement for Einstein's
equation. It does not publish the `N2` locus, the polarization action, the
Green flux or a common physical domain. The helicity and flux results are new
repo constructions, not source attributions.

## 1. Exact low-memory reconstruction

The probe rebuilds the complete null source symbol directly from the reviewed
`Cl(7,7)` Shiab evaluator, avoiding the predecessor's memory-heavy full-bank
replay. It reproduces

| block | exact rank |
|---|---:|
| raw forward cross | 12 |
| formal `d_B T` Euler cross | 11 |
| full source-variable cross | 15 |
| Schur correction | 14 |
| pre-Schur principal form | 28 |
| diffeomorphism image | 4 |

The same 24-dimensional connection Hessian and the invariant
`1+104+91` grade-one inverse are used. Both the principal and Schur forms have
the gauge image in their radical.

## 2. Compact null-stabilizer calculation

Fix `k=(1,0,0,1)`. The generator `J_12` of rotations in the transverse
`1--2` plane is Lorentz and fixes `k`. Its induced action includes all three
indices of the source variables:

- both symmetric metric indices;
- the one-form index of the connection;
- both Lorentz-bivector indices.

The complete principal and Schur forms satisfy exact infinitesimal covariance

```text
J_src^T P0 + P0 J_src = 0,
J_src^T Q  + Q  J_src = 0.
```

Over the quadratic number field defined by

```text
N2(z)=z^2+(1352/615)z-1178198372/69047075,
```

the kernel has dimension six. Extending the four gauge columns by two kernel
columns and descending `J_src` gives `J_phys` above. Its characteristic
polynomial is complement-independent, so changing representatives cannot
turn helicity one into helicity two.

Each positive `N1` root has only one additional real source mode and therefore
cannot individually supply a real helicity pair either. Thus none of the
positive exceptional factors already found in the completed first-layer bank
recovers the graviton.

## 3. Principal Green flux

The Schur symbol is filtered rather than uniformly second order: after the
source change of variables, its metric, mixed and connection blocks can have
orders four, three and two. The time-covector derivative therefore cannot be
replaced by a naive two-point second-order formula.

The probe evaluates the exact pencil at six time-covector values, verifies
that its fifth finite difference vanishes, and uses five-node Lagrange
differentiation at `k_0=1`. On the two-mode quotient the result is

```text
G_N2 = c(a) I_2,
c(a) = (600329995/1382653597)a
       - 111263815960284/35822959328735,
```

where `a` is the class of `z` modulo `N2`. It has rank two, pairs trivially
with every gauge direction and is invariant under changing physical lifts by
gauge. At the positive real embedding,

```text
c(a) = -1.72722841269413...
```

so the finite flux is definite up to the overall action-sign convention.
This is a principal-symbol result, not a construction of the covariant
phase-space form, boundary conditions, positive Hilbert norm or global
evolution domain.

## 4. Disposition

This is a scoped route kill:

- killed: the positive `N2` locus as the spin-two Einstein carrier of the
  completed first-layer grade-one bank;
- preserved: the graph-only Einstein theorem on its declared constant-`T`
  subspace;
- open: other source-owned action layers, especially the distinct second-layer
  residual norm `I2B` and its map to the observer `||II||^2` functional;
- not claimed: a falsification of every source-action completion or GU.

Ledger v0.37 keeps the headline counts and residue fixed, migrates six
distances and promotes the `I2B <-> ||II||^2` owner map to the rank-one gate.
The right next move is to test whether that distinct layer supplies a genuine
helicity-two carrier before spending on a global domain.

## Boundaries

No Einstein equation, graviton, positive energy, unitarity, cosmology,
particle spectrum, coefficient prediction, BV/BFV quotient or global domain
is claimed. P1/P2/P3 remain unused. Curt remains formally separate and no
third lane is promoted.
