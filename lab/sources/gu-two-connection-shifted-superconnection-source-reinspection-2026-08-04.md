# Source reinspection: two connections, shifted roll, and the actual action

Date: 2026-08-04
Gate: `K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER`

## Disposition

| question | disposition | evidence |
|---|---|---|
| Does Eric state a four-entry two-connection `D^2` mnemonic? | `SOURCE-CONFIRMS` | TOE 2025 `02:44:06–02:45:13` |
| Does he release the construction? | `SOURCE-UNRELEASED` | TOE: “created and have never released” |
| Does that passage identify its `A,B` with the IG bi-connection? | `SOURCE-SILENT` | no identification in the local passage |
| Does GU independently have a bi-connection from one IG element? | `SOURCE-CONFIRMS` | Portal `02:27:46–02:33:13`; Into the Impossible `00:17:01–00:22:26`; draft guide §7 |
| Is the difference of that pair augmented torsion? | `SOURCE-CONFIRMS` | Portal and draft guide |
| Is there a released first-order GU bosonic action? | `SOURCE-CONFIRMS_PREEXISTING` | draft eqs. 9.4/9.7/9.10; W161; W191 |
| Does the source identify that action as the action of the 2025 cyclic operator? | `SOURCE-SILENT` | the 2025 operator is unreleased and no action is attached to it |
| Are the `1/2,1/3` terms structurally Chern--Simons-like? | `SOURCE-CONFIRMS_ANALOGY` | rendered draft eq. 12.4 comparison |

## Primary-source extracts used as data

### TOE 2025

At `02:44:06–02:45:13`, after the `0 -> 1 -> 13 -> 14` fermion roll,
Weinstein recalls a cyclic construction with two connections and the four
tokens

```text
d_A, F_B
identity, d_B
```

with two minus signs in the second column. He says a complex is born “on
shell,” but also says the construction has never been released. The passage
does not say what bundle shift types the entries, what equations define the
shell, or whether `A,B` are the older inhomogeneous-gauge bi-connection.

### Portal 2020

At `02:27:46–02:28:42`, one element of the inhomogeneous gauge group maps to
two connections. Their difference is an honest adjoint-valued one-form. At
`02:32:38–02:33:13`, the same difference is explained as augmented torsion.
This is a bosonic geometric construction, independent of the later fermion
roll.

### Into the Impossible / UCSD

At `00:17:01–00:22:26`, Weinstein again explains two ways to move a
distinguished connection and subtracts them to recover an equivariant
contorsion/augmented-torsion object. This confirms the IG pair, but does not
link it to the 2025 cyclic operator.

### 2021 action surfaces already in the repository

`docs/paper-formalization-candidates.md` §4A, W161, W191 and the rendered draft
carry the first-order action in the normalized wedge convention

\[
 I^B_1 = \left\langle T,
 *\operatorname{Shiab}\!\left(
 F_B+\frac12 d_BT+\frac13 T\wedge T
 \right)+\frac12T\right\rangle .
\]

The Euler row is recorded as

\[
 \Upsilon=S-T=0,
\]

“swervature equals displasion.” The action was not missing from the repo. The
missing object is the map, if any, from this density-dual Euler row to the
connection difference in the 2025 square.

## Layer-0 correction to the predecessor

The predecessor correctly said that a cyclic action owner for the unreleased
2025 operator was source-silent. Its shorter wording could be misread as
saying GU had no bosonic action owner. The broad source/repo collision now
records the correct split:

- `I1B` is a pre-existing source-owned bosonic action;
- an action specifically owning the 2025 cyclic operator remains
  source-silent;
- identifying the operator's pair with the IG pair makes its connection
  difference augmented torsion `T`, not the Euler density `Upsilon`;
- identifying the pair with an action-derived pair would require a bosonic
  primalizer `R_B: Omega13(ad)^! -> Omega1(ad)`.

## What the source does not authorize

- no mixed Bianchi identity for distinct `A,B`;
- no equality between `T=0` and `Upsilon=0`;
- no identification of the shifted cyclic roll with D916;
- no actual K77 Shiab selection or global Euler primalizer;
- no physical Dirac Hamiltonian, mass, generation, particle or dark-sector
  conclusion;
- no use of P1, P2 or P3.
