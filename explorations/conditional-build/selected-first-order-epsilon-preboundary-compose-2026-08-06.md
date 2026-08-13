---
artifact_type: compose_result
created: 2026-08-06
status: SELECTED_FIXED_METRIC_EPSILON_PREBOUNDARY_COMPOSED__COMPACT_DIRICHLET_GREEN_EXACT__UNRESTRICTED_GLOBAL_BFV_OPEN
channels: [COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
canon_verdict_change: none
---

# Selected first-order epsilon / preboundary composition

## Result in plain English

The current first-order Build queue was asking for one piece that the
repository had already built but had never composed into the selected branch.

The exact earlier epsilon/Green result covered all eight displayed Shiab
product assignments. The later Bianchi gate selected
`comm/symi/symi` from those eight. Therefore the selected first-order action
already has:

- the primitive epsilon Euler row;
- exact off-shell homogeneous even owner cancellation at the finite selected
  grade;
- a compact-core closed Green graph with zero flux for Dirichlet epsilon data;
  and
- an explicit unrestricted boundary flux when that condition is removed.

This does not finish the physical quotient. It removes “construct primitive
epsilon” from the queue and replaces it with the honest remaining burden:
move the metric/Hodge/DeWitt/Krein/density and observation owners through the
action, then globalize the unrestricted preboundary/BFV class and add
diffeomorphism/odd closure.

## 1. Layer 0: three transformations and two boundary statements

| phrase | exact object | kept distinct |
| --- | --- | --- |
| principal gauge motion | shared affine derivative of the two connections, killed by `T=A-B` | homogeneous adjoint rotation |
| homogeneous gauge motion | `[T,chi]` with moving `Phi1/Phi2`/Shiab, pointwise scalar variation zero | primitive variation of epsilon as a field |
| primitive epsilon variation | `delta B=D_B eta`, `delta T=-D_B eta`, plus moving-Shiab chain | diffeomorphism or odd super-IG BV |
| Dirichlet Green closure | boundary trace of `eta` vanishes on a compact core | unrestricted preboundary charge |
| unrestricted flux | `int_boundary <eta,i_n(E_B-E_T)>` | nonzero reduced BFV class or physical transition |

The three transformations are compatible pieces of one source-shaped action,
but they are not synonyms. The two boundary alternatives are mutually
exclusive domain choices, not two verdicts about the same phase space.

## 2. Source and repository collision

The source confirms the moving Shiab family, the two-connection definitions,
and the primitive epsilon chain. It does not select `comm/symi/symi` or give a
physical BFV domain.

The repository supplies the missing specialization in two later exact steps:

1. the complete eight-row Bianchi calculation makes `comm/symi/symi` the
   unique Bianchi-compatible nonzero displayed row, explicitly **not
   attributed to Weinstein**;
2. the selected intrinsic action scan proves moving-Shiab homogeneous Ward
   closure on all 91 K77 bivector generators.

Because the primitive epsilon artifact enumerated all eight rows, the selected
row is a literal member of its tested domain. No new product selector, field,
coefficient or datum is inserted.

Scoped return:

```text
SOURCE-CONFIRMS: moving family, two-connection epsilon chain, equivariance
SOURCE-CORRECTS: Hodge/metric/density/section motion is not part of the fixed-
                 metric primitive epsilon chain
SOURCE-SILENT:   selected product attribution, global noncompact Y14 domain,
                 diffeomorphism/odd BV and physical BFV phase space
```

## 3. Composed first-order chain

For right logarithmic parameter `eta=epsilon^-1 delta epsilon`, the already
verified chain is

```text
delta B = D_B eta,
delta T = -D_B eta,
delta Phi_i = [Phi_i,eta].
```

Writing `K_S` for the action derivative with respect to the Shiab map gives

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S.          (1)
```

Equation (1), the two-connection principal radical, and the selected
homogeneous moving-Shiab cancellation are now one compatible fixed-metric
first-order owner package. The composition does not make equation (1) a new
fixed-epsilon translation equation and does not erase the moving-Shiab term.

## 4. Exact preboundary identity

The finite independent control uses an oriented interval with vertex field
`eta_0,...,eta_3` and edge Euler difference `e_0,e_1,e_2`. Exact summation by
parts gives

```text
sum_i (eta_(i+1)-eta_i)e_i
 = sum_(j=1,2) eta_j(e_(j-1)-e_j) + eta_3 e_2 - eta_0 e_0.  (2)
```

The last two terms are the boundary flux. They vanish for
`eta_0=eta_3=0`. With unrestricted exact rational data the planted flux is
`11`, so the test would fail if compact Dirichlet closure were silently
reported as vanishing unrestricted charge.

The continuum owner is the prior compact-core graph

```text
D_B : H10 intersect H1_0 -> H9,
```

with the unrestricted alternative
`int_boundary <eta,i_n(E_B-E_T)>`. This is a formal Green pair, not global
hyperbolicity, self-adjointness, positivity, maximal dissipativity or BFV.

## 5. What is genuinely still open

The first-order selected package still needs:

1. moving metric/Hodge/DeWitt/Krein/density contributions to the Euler and
   presymplectic owners;
2. composition of the already-exact observation first jet and equation dual
   with this selected action, including the nonlinear section response;
3. diffeomorphism and odd super-IG BV closure;
4. a global noncompact or otherwise physically justified Green domain; and
5. unrestricted preboundary/BFV reduction and common interacting positivity.

The separate second-layer/observer `I2B <-> ||II||^2` owner map remains rank
two and is not merged back into this first-order package.

## 6. Ledger v0.25

```text
Ledger v0.25 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances migrate: `LT-GR1`, `LT-GR2b`, `LT-GR5`, `LT-GR6`, and
`LT-SM8`. Verdicts, reason kinds, revival triggers, residue and quotient count
are frozen. Compact Dirichlet descent does not count a fifth quotient.

## 7. Seven-axis disposition

- **Layer 0:** principal, homogeneous, primitive epsilon, Dirichlet and
  unrestricted objects are separated.
- **L1 syntactic:** selected row and epsilon/Green formulas are located.
- **L2 type:** the selected product is inside the earlier eight-row domain.
- **L3 algebraic:** exact owner compatibility and summation-by-parts identity.
- **L4 geometric:** fixed metric/section compact core only; moving owners open.
- **L5 variational:** primitive epsilon Euler and compact Dirichlet Green row
  composed; unrestricted BFV and odd/diffeomorphism closure open.
- **L6 analytic:** formal `H10 cap H1_0 -> H9` graph only; global physical
  domain open.
- **L7 physical:** no Q1, transition, unitarity, particle or cosmology claim.

## 8. Constraint and lane fence

```text
new fields: 0
new coefficients: 0
new selectors: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## Evidence

- `tests/channel-swings/selected_first_order_epsilon_preboundary_compose_probe.py`
- `tests/channel-swings/conditional_physics_ledger_v025_probe.py`
- `lab/process/selected-first-order-epsilon-preboundary-compose.json`
- `lab/process/hostile-reviews/2026-08-06-selected-first-order-epsilon-preboundary-compose-review.md`
