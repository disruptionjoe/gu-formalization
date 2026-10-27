---
title: "K2126: All-grade raw obstruction to moving the positive sector at P0"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact first-jet obstruction at P0 in fixed common-H raw upper class; no all-angle, changed-contraction or GU-wide conclusion
scripts:
  - tests/channel-swings/k2126_positive_sector_raw_coefficients_probe.py
---

# K2126: All-grade raw obstruction to moving the positive sector at P0

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact all-grade selected-sector first-jet obstruction at a fixed projector
carrier: K2120 complex32 at P0 inside original Jc complex128 and raw complex1920 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: SAME inherited current S=i Jc transpose H D0 Jc, P0 S P0=(9/280)P0 ON=declared_carrier
real_structure: arbitrary complex raw coefficients with fixed Hermitian H-adjoint condition
grading: Clifford grades, current sign and source ambient halves remain distinct
action_owner: repository-construction -- original K2028 upper contraction, now only selected32 preservation
target: conservative evolution of moving Ptheta without requiring complement invariance MAP-TYPE=intertwiner
```

## 1. Result, scope and predecessor distinction

At P0=(I+iT)(I+R)/4 of [K2120](k2120-inherited-core-current-2026-10-27.md),
NO arbitrary complex raw connection coefficients in the fixed common-H upper
class can support a nonzero first derivative of the SAME positive family
Ptheta, while preserving its32-dimensional evolution and inherited current.
The selected tangent operator is arbitrary, and no invariance or conservative
condition is imposed on the complementary96 dimensions.

The exact real-linear systems force all four real components

    theta_t=theta_1=theta_2=theta_3=0, at points where Ptheta=P0. (1)

The obstruction survives DELETING the entire lower-return equation. Consequently
an arbitrary southeast-block completion, or even an independently supplied
lower return, cannot repair this upper-class obstruction. Altering the upper
contraction or its common-H requirement is a different branch.

This is a pointwise first-jet theorem at P0, NOT a theorem for every theta and
NOT a proof that every smooth globally moving selector is constant. A path
can have zero derivative at P0. Raw-class equivariance under exp(i theta Z/2)
is not established and is not assumed. Source selection, observed physics and
GU recovery remain open.

[K2123](k2123-same-current-potential-dynamics-2026-10-27.md) used K2028's
all128-invariant thirteen-dimensional potential class. [K2124](k2124-moving-positive-polarization-2026-10-27.md)
left exactly the32-only relaxation open. This calculation removes that extra
all128 restriction; it does not infer a larger exclusion from the old class.

## 2. Eliminate the induced unknown without losing tangent freedom

Use the original15 blocks J_a of Jc, J_z=J_14, raw D0, and K(Omega). The top
block of D0 Jc equals J_z, which is invertible. Define

    A=J_z^-1 (KJc)_0,
    Bgrad=theta_t I + Cj theta_j,
    L=(i/2) Z Bgrad P0.                                      (2)

The fixed mass preserves P0 and can be added independently. For arbitrary
sections in the moving selected sector, the necessary pointwise equations are

    (KJc-D0 Jc A)P0=0,        all15 output rows,
    (I-P0) A P0=-L,
    P0(A+A*)P0=0.                                             (3)

They are also sufficient for the pointwise coefficient/invariance/conservation
identities, not by themselves a global domain theorem. The first equation
keeps every full-carrier output. The second cancels the actual derivative
leakage of Ptheta, since partial_mu P=(i/2)[Z,P]theta_mu and PZP=0.
The third makes the remaining tangent evolution skew in the positive norm.
Because Ptheta S Ptheta=cPtheta with constant c, conservation of that norm is
conservation of the inherited selected current. No commuting-P-with-S claim
is needed. Eliminating A through the top row does not set its tangent block
to zero: all conservative tangent corrections remain variables implicitly.

## 3. Exact all-grade common-form reduction

Freeze the original gamma_k, eta_k, volume v, W=(3I-v)/2 and B=gamma_7...gamma_13.
For a!=c the upper raw block is

    K_ac=eta_a gamma_a sum_(k!=a,c) gamma_k gamma_c W Omega_k,
    K_aa=0,   K_a,z=Omega_a.

The forced lower row in the baseline is sum eta_k B Omega_k* B J_k; the
second certificate discards it altogether. Expand arbitrary complex128x128
Omega_k in the complete real Clifford basis through

    Omega_k=(3I+v) eta_k gamma_k Y_k/4.

For one Clifford mask I of degree r, let sigma=(-1)^(r(r+1)/2) and
chi(a,c)=(-1)^(1_{a in I}+1_{c in I}). Common-H upper Hermiticity imposes
sum_(k!=a,c)y_k=0 when sigma chi=-1 for real coefficients, and when
sigma chi=+1 for imaginary coefficients. These are14-variable real systems;
there is no ansatz restricting Clifford grade. K2028's complete small kernels
and labels are reused and hash-pinned, not its all128-preserving solution.

Normalize input coordinates by J_z. Direct original-coordinate reconstruction
finds J_z X J_z^-1 has XOR shifts T:63, R:1, TR:62, Z:15, C1:0, C2:96, C3:80.
An XOR shift f means entries occur only at (i,i XOR f). Thus right multiplication
by P0 mixes exactly Hshift={0,1,62,63}. The normalized positive norm metric is
J_z^-* J_z^-1=(1225/121)I, checked directly rather than presumed unitary.
Transposition retains XOR support. Every raw return row has a fixed translate
of its top-row shift, so no other coset can cancel an equation in these cosets.

| Derivative components | Relevant top-row coset | Real+imaginary columns |
|---|---|---:|
| t and1 together | 14,15,48,49 | 256+256=512 |
| 2 | 80,81,110,111 | 264+260=524 |
| 3 | 94,95,96,97 | 264+260=524 |

There is an additional independent completeness check for the512-column
coset. Its512 masks have grades3 through11. The nonzero branch forces y
constant a inside the mask and b outside, with
(r-1)a+(13-r)b=0, giving y_in=13-r, y_out=-(r-1) up to normalization.
It is real for sigma=+1 and imaginary for sigma=-1. The opposite branch
has remaining determinant-24 and no kernel. Enumerating all16384 masks and
comparing these analytic vectors reproduces every stored column in this coset.
The two spatial cosets reuse the independently established K2028 complete
per-grade kernels; no fresh full229376-variable exhaustion is claimed.

## 4. Reproducible exact certificates

The probe reconstructs each raw column and all rows of(3), retaining real and
imaginary equations separately. Integer numerator scales are176 for raw
outputs and7744 for return equations; the projected leakage uses176 times
the square of the projector denominator. Primitive rows are normalized by
their integer gcd and only exactly duplicated equations are removed.
Explicit input bounds |y|<=16, |44J|,|44DJ|<=44 and unit gamma entries
bound elementary raw numerators by588544 and return numerators below2^27;
projector/metric scaling remains below2^42. Every dense product additionally
has a conservative Python-integer overflow bound before int64 execution. Independent sparse rational evaluation of the original
unreduced raw contraction checks representative real/imaginary columns on four
complete output blocks per coset.

Exact rational row reduction and independently computed finite-field lower
ranks give:

| Components | Coefficient rank | Augmented rank | Kernel dimension | Nonzero augmented minor mod101 |
|---|---:|---:|---:|---:|
| t,1 jointly |512|514|0|9|
| 2 |523|524|1|92|
| 3 |523|524|1|77|

The SAME ranks and minor residues hold after deleting the lower-return rows.
For the spatial systems the report includes explicit rational right-kernel
vectors and checks every original equation against them, proving the rank
upper bound. Nonzero modular minors prove the corresponding lower bounds
over the rationals AND reals. The number of independent appended derivative
columns is exactly2,1,1 respectively; therefore no nonzero linear combination
of gradient components belongs to the raw image. Separate pure-direction
failures alone would not prove this, which is why t and1 are appended jointly.
All other XOR cosets are homogeneous and cannot change that quotient rank.

The report records normalized equation hashes, pivot rows/columns, nullspace
vectors and determinant residues. These are exact finite algebra certificates,
not floating rank estimates or proof-assistant certification. Three coordinate/generator comparisons are negative normalization controls;
two raw-coefficient/Hermitian-reality mutations are rejected by the actual
common-form predicate. None is counted as a new all-grade proof.

Reproduce with Python3.12, NumPy2.5.4, SymPy1.14.0 and python-flint0.9.0:

    python tests/channel-swings/k2126_positive_sector_raw_coefficients_probe.py

No Sage or new search cache is required. Inputs and probe are public and
relative-path based. Existing K2028 classification is cited for the common-form
basis only; its old preservation/conservation restrictions are not reused.

## 5. Consequences and live alternatives

This rules out the proposed local repair at P0 even when one preserves only
selected32 and leaves its complement arbitrary. It also eliminates a lower-
only/southeast repair for this jet, saving that separate coefficient search.
The supplied Z connection in K2124 remains a valid changed-class construction;
it simply cannot come from the frozen common-H upper raw class at this jet.
Constant P0 with K2123 scalar/vector potentials remains a positive control.

The next discriminators are whether the obstruction persists at generic
Ptheta (without assuming equivariance), which exact upper common-form condition
must change, and whether a different positive family or derivative-dependent
observation can meet the same source/current demands. A free restriction is
not a physical quotient. These are distinct candidate constructions, not
permission to alter the source. SC-OP-04 ASSERTS candidate operator grammar;
SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action
prerequisite. LT-SM8/LT-GR6b, ledger0.263, source polarity and canon unchanged.
