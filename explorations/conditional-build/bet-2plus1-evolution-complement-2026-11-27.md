---
title: Time normalization opens principal complements, but the native reference fails their first prolongation
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-2PLUS1
tier: T1
expected_delta: Classify normalized-time complements beyond the raw-operator result and test the actual lower equations
actual_delta: Six equivalent observed principal channels survive for every weight; an exact first-prolongation minor excludes arbitrary C1 local evolution complements of the held flat-section reference
class_covered: All constant nonzero real chiral weights in the existing completed wedge/SE reconstruction; lower exclusion on the native K95 flat horizontal section, F=U=0 split connection and b=H density jet, fixed contraction q and coherent normal jets
premises:
- Existing completed weighted fermion reconstruction, not a source-selected action or physical quotient
- Actual time normalization; independent input and output lifts are distinguished
- Full observed and hidden lower coefficients retained in the flat-section reference
- Arbitrary C1 pointwise graphs, with no covariance or orthogonality ansatz
source_bridge:
  status: conditional
  reason: Source effective low-gravity separation does not require an exactly invariant local complement, and does not select this reference connection or physical state/current
kill_condition: A failed native coefficient binding, time transport, all-weight cancellation or exact minor invalidates the affected class exclusion; principal compatibility alone is not an existence theorem
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Lane C only; no scientific matrix or ledger absorption
---

# Principal opening, differential obstruction

program_target: BET-2PLUS1
tier: T1
expected_delta: Decide the unconsumed normalized-time complement category.
actual_delta: Complete principal classification and an actual native first-prolongation obstruction.

**ESTABLISHED:** after time normalization, all six observed principal channels
are equivalent to the hidden spinor evolution channel. The space of complex
principal graph maps has dimension110592 for every allowed weight pair.
The earlier raw-operator exceptional-locus argument does not transfer.

**RULED OUT:** an arbitrary C1 pointwise invariant graph for the full evolution
of the existing flat-section, F=U=0, b=H reference. The pointwise necessary
system alone gave no modular obstruction; differentiating that constraint
once produces a certified contradiction. No derivative of the graph is
silently discarded.

**NOT MODELED / UNDETERMINED:** other F/U connections, individual curved
sections, nonlocal or approximate elimination, physical chirality/current,
family count and source GU. This is lane-C evidence, not a bet-wide kill.

```gu-typed-objects
result: normalized-time complement and first-prolongation test
carrier: full complex Dirac S128; hidden9S and observed6S of one-form plus independent scalar LAYER=ambient+observed BRIDGE=held-contraction-and-coherent-normal-jets CHIRALITY=S-FULL-DIRAC
pairing: arbitrary complex graph, no orthogonality or positive physical pairing ON=held_reconstruction
real_structure: complex K95 native geometry; K77 principal signs bound separately, no automatic lower real-form transfer
grading: central spatial Clifford chirality used for algebra, not physical weak chirality
action_owner: repository-construction -- existing weighted wedge/SE family, no new action
target: local graph invariant under time evolution MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The source total is
> nonchiral and its generation target is2+1. This operator complement is not
> a physical-family split or a count. Read
> [source-native routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Source custody and reuse

Basis: `784a27c9f5889dd2a229a0b42564bb0bb2f3978c`.
SC-OP-04 (draft p46eq9.16) supplies four independent classical fields and
candidate operator grammar; SC-OP-05 leaves southeast rivals open.
SC-CHI-04 (draft p64) and SC-CHI-52 (TOE2025 02:37:07) assert effective
low-gravity/low-mass separation, not exact local invariant graphs.

The [raw-complement result](bet-2plus1-local-complement-2026-11-27.md)
explicitly leaves normalized-time graphs open. It required the same lift r
on input and output, `D r=r D_O`. If time coefficients are invertible,
evolution intertwining instead corresponds to `D r=s D_O`, where
`s=A_0 r A_O0^-1`; generally s differs from r. We keep that distinction.

The lower reference, its density repair and complete opposite block are owned
in [unitary dual closure](bet-2plus1-unitary-dual-closure-2026-11-27.md) and
[shape coupling](local-dual-closure-second-fundamental-form-2026-11-24.md).
No new connection, action or density choice is introduced.

Graph invariance and its operator equations are established methods; see
[Makarov–Schmitz–Seelmann](https://arxiv.org/abs/1307.6439). Their operator-domain
hypotheses are not imported here. We derive the local necessary equations
directly. No novelty claim is made.

## 2. Complete principal classification

Reuse the authenticated raw coordinates of the previous theorem:
`R^-1 D_k R=M_k tensor Gamma_k`, `Gamma_k=gamma_k Wsharp`,
`p=w_+w_- !=0`, `r=sigma/p`, `s=c/p=-11r/12`.
Hidden coefficients are `-Gamma_k`. On observed coordinates
`(u0,u1,u2,u3,x,h)`, x is the common normal component and

```
(M_k u)_k=h,
(M_k u)_i=sum_(j not i,k)u_j+10x       (horizontal i!=k),
(M_k u)_x=sum_(j!=k)u_j+9x,
(M_k u)_h=r u_k+s h.
```

M0 is invertible for every r!=0: its spatial-difference subspace has
nonzero eigenvalue−1, its spatial-sum/normal block has determinant−12,
and its time/scalar block determinant−r. No old exceptional p remains.
Put `N_i=M0^-1 Mi` and `alpha_i=Gamma0^-1 Gamma_i`, i=1,2,3.
The weights cancel from alpha_i. The six following rows form an invertible
matrix V and simultaneously diagonalize every N_i:

| Character | Row |
|---|---|
| +++ | (1,1,1,1,20,0) |
| +++ | (0,0,0,0,12,1) |
| −++ | (1,−1,1,1,10,−1) |
| +−+ | (1,1,−1,1,10,−1) |
| ++− | (1,1,1,−1,10,−1) |
| −−− | (1,−1,−1,−1,−10,1) |

Direct substitution gives `V N_i=diag(epsilon_i)V`. Because V is invertible,
this proves completeness, simultaneous commuting involutions and independence
of r, not just sample-weight agreement. The probe checks the constant and
linear coefficients of `M0(r)N_i=Mi(r)` separately.

Conjugations by the three alpha_i commute. On full End_C(S128) their eight
characters each have dimension2048: in the full Cl14 blade basis their signs
are `(-1)^(b0+bi)`, three independent binary conditions. For a graph component
`l tensor Z`, `Z alpha_i=epsilon_i alpha_i Z` reduces the intertwiner condition
to `l N_i=epsilon_i l`. The row multiplicities are2,1,1,1,1 as above and zero
for the three two-minus characters. Including all nine hidden copies gives

`dim_C Hom_principal=9*(2+3+1)*2048=110592`.

This is not a physical parameter count. Invertible Clifford representatives
I, gamma1, gamma2, gamma3 and gamma0 remove the respective sign twists.
Thus the observed principal symbol is constructively six copies of the
hidden three-generator Clifford module. The two central Clifford chiralities
each have a two-dimensional irreducible spin factor and multiplicity32.
Any principal graph is therefore `I2 tensor T_+` and `I2 tensor T_-`, with
`T_sigma:C^192 -> C^288`. These maps allow arbitrary spinor/multiplicity
mixing; no equivariance or physical grading is imposed.

The principal conclusion covers both authenticated reciprocal sign ports.
The following lower result is specifically native K95.

## 3. Actual lower reference; not an arbitrary frozen curved operator

Take a flat horizontal metric `g=diag(-1,1,1,1)` and its same-metric section
in the owned native metric bundle. Retain the full nonzero second fundamental
form and the existing split correction F=U=0, b=H. The mixed ambient LC terms
are canceled by that specified connection; tangent and normal split connections
are zero in the translation-constant adapted frame along this section.
The ambient geometry is not flat. Shape, Clifford matrices, time covector,
density normal jet and channel transformation are constant **along the section**.
The density reference has zero tangential log-density gradient and normal
log-density gradient H along this section; b=H here means that full gradient.
Normal jets retain their inherited prescription.

The exact residual lower term is `Phi[z composed T_B]`, scalar row zero,
with `T_B(h,n)=S_n h`, `S_n=−g^-1 n/2`. It has only horizontal one-form
input columns and vanishes on the hidden kernel. Thus C_K=0 in this frame.
For horizontal b, define

```
A_n=sum_h gamma^h b(S_n e_h),
B_h=−sum_n gamma^n b(S_n e_h),
G=sum_n gamma^n A_n.
C_h=B_h−gamma_h G,   C_n=A_n−gamma_n G,   C_scalar=0.
```

The full output—not only its hidden projection—is used. In particular
`P_K C_N=P_K A`, agreeing with the already owned opposite block. As an
independent control, every input/output coefficient is checked against

`C_(a,j)=sum_(h,n:a!=h,n) (S_n)^j_h/(d_h d_n) gamma_a gamma_h gamma_n W`.

The native normal Gram is `(2,2,2,2,6,12,−2,−2,−2,−4)`.
No positive comparator or K77 relabeling enters.

### Weights do not repair this reference

In covariant coordinates `z_a=gamma_a u_a`, `nu=Wsharp h`, the time inverse
and lower row contain opposing W/Wsharp factors. Their intervening Clifford
product is even, so they cancel. The scalar preimage row is zero; the remaining
M0 inverse depends only on `c/sigma=−11/12`, not p. Thus the complete normalized
reference lower map, as well as its principal symbol, is independent of every
allowed nonzero constant chiral weight pair. This does not eliminate the
independently allowed F/U corrections.

### Clock sign custody

Raw covector and covariant coordinate components differ by eta. For the
physical covariant dx0 in K95, the observed time coefficient is
`−M0 tensor gamma0`, hidden `+gamma0`. In the probe the **evolution** coefficients
are `alpha_i=−gamma0 gamma_i`, `V=−M0^-1 gamma0 C_O`, `B=gamma0 B_raw`.
Thus the actual equations have the form

`partial_t h=alpha_i partial_i h+B o`,
`partial_t o=alpha_i partial_i o+V o`.

A consistent opposite time convention changes the signs of the necessary
first-derivative equation together; it does not change the prolongation test.
Do not identify these evolution coefficients with the unnormalized covector.

## 4. Keep the moving graph and test its first prolongation

Let `h=T(x)o` be any C1 local graph. Principal covariance gives the module
maps T_sigma above. In each central chirality, the four two-by-two blocks of
V that change chirality are multiplicity matrices X_j, and those of B are Y_j.
The derivative terms preserve central chirality. Consequently

`T_sigma X=Y`, where `X=[X_0 X_1 X_2 X_3]`, `Y=[Y_0 Y_1 Y_2 Y_3]`.

X has192 rows and Y has288. The pointwise reduced ranks happen to agree
modulo97. **That agreement is not a characteristic-zero existence result.**

Let V0 and B0 be the identity-spin coefficients of the same-chirality parts,
i.e. half their two-by-two spin trace. The time component of graph invariance is

`partial_t T_sigma=−T_sigma V0+B0`.

X and Y are constant along the flat section. Differentiating `T_sigma X=Y`
therefore forces `T_sigma V0 X=B0 X`. Combine the two equations:

`T_sigma [X | V0 X]=[Y | B0 X]`.

Every solution would put every row of the right side in the row space of a
matrix having only192 rows. The stacked matrix

```
[ X | V0 X ]
[ Y | B0 X ]
```

has a nonzero193-by193 minor in **each** central chirality. This is impossible
if T_sigma exists. Only one chirality and one time derivative are needed.
The result excludes arbitrary C1 moving graphs; a constant-graph test alone
would not have established it. No second derivative of T is required.

### Exact certificate and characteristic-zero transfer

The native matrix entries lie in Q(i,sqrt2,sqrt3). Reduce at97 with
`i=22`, `sqrt2=14`, `sqrt3=10`. Metric denominators and all basis inverses used
are units. Clifford and chirality bases are constructed from the same algebraic
expressions; their nonzero reduced determinants ensure their original
invertibility. The certificate lists the193 row and column indices and
matrix hashes. Its minor determinants are **87 and37 modulo97**.

A nonzero reduced minor proves the original minor nonzero. The argument
uses only the universal192-row upper bound; it does **not** infer an original
rank of160,288 or448 from a reduced rank. No floating-point rank is used.

## 5. Controls, surviving routes and effect

A basic countercontrol is
`D_K=a(partial_t+v partial_x)`, `D_O=c(partial_t+v partial_x)`, coupling b,
with a!=c and a,c nonzero. The normalized graph `T=−bt/a` works, while the
raw same-r time condition requires `(a−c)T=0`. Thus raw failure does not imply
normalized failure. The actual native result needed the new computation.
A second finite control distinguishes solvable pointwise algebra from
incompatible differentiated constraints. The actual principal survivor is
also retained, rather than rewritten as a universal obstruction.

The exclusion covers every allowed weight on this existing reference and
also defeats a proposed universal local-complement prescription required to
work on **every** admitted base including this flat one. It does not prove
that every F/U member or every individual curved background fails. Curved
coefficients would add derivatives of X,Y and connection terms. Nonlocal
lifts, independent barred maps, approximate decoupling and physical state
restrictions remain distinct categories. No automatic generation or dark-matter
claim follows from the 6/9 copy counts.

No new choice family, action or physical norm is adopted. Choice budget stays
10 families /4 grouped obligations /net6 /0 source-selected predictions.
No source, canon or physics-ledger verdict changes. Lane-C retention requires
separate lane-B re-derivation before any matrix or ledger absorption.

[Probe](../../tests/program-focus/evolution_complement_probe.py),
[exact certificates](../../lab/process/evolution-complement-certificates.json),
[evidence/reviews](../../lab/process/bet-2plus1-evolution-complement.json) and
[Lean finite cores](../../Lean/GUFormalization/EvolutionComplement.lean)
separate finite algebra from written geometry and differentiation. The Lean
core does not certify the native193-minors or full PDE theorem.
