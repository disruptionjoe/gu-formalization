---
artifact_type: exploration
status: exploration
doc_type: sg4-constraint-gate
created: 2026-08-14
work_item: SG4-1
channel: majorana_126_neutrino_mechanism
title: "SG4-1: exhaustive enumeration of every SO(10) irrep below dimension 2000 that can break B-L while preserving the Standard Model. The complete list is {16, 126, 144, 560, 672, 720, 1200}; the two smallest are exactly the 16 and the 126, and NOTHING below dimension 16 can do it. The 126 is the unique minimal RENORMALIZABLE option (|B-L| = 2); every other qualifying rep has |B-L| = 1 and reaches M_R only at dimension five. This converts 'SG4 is open' into a named finite constraint."
grade: "EXACT rational arithmetic: Weyl dimension formula, dominance-order closed form, root-lattice integrality. The enumeration is EXHAUSTIVE below the bound, not sampled, because for simply-laced D5 a dominant mu is a weight of V_lambda iff mu <= lambda and lambda - mu is in the root lattice. 26/26. NOT: a derivation of any field from GU, a claim that SG4 does or should declare these, or any claim-status movement."
disposition: MINIMAL_B_MINUS_L_CARRIER_IS_THE_16_OR_THE_126__NOTHING_BELOW_DIMENSION_SIXTEEN_QUALIFIES__126_UNIQUE_MINIMAL_RENORMALIZABLE__CONSTRAINT_ON_SG4_NOT_A_DERIVATION
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/bd2-126-channel-is-repulsive-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/baryon-number-and-proton-decay/
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/channel-swings/joe_directed_sg4_minimal_carrier_probe.py
---

# SG4-1 — what SG4 would have to declare

## Why this gate

Every result this session is about **GU-as-declared**, and canon makes SG4 —
the source action's field-space declaration — the open decider. BD-1 observed
that one object, the 126, would simultaneously supply a `B-L`-charged SM
singlet, give the nine surviving gauge bosons mass, and restore baryogenesis.
This gate turns that observation into an exhaustive, named constraint.

## The structural reduction

Derived and then verified by brute force rather than assumed:

> A weight `mu` is an SM singlet with `B-L != 0` **iff all five of its
> components are equal and nonzero**, `mu = (c,c,c,c,c)`, `c != 0`.

Colour-neutrality forces `mu1=mu2=mu3=a`; `T3L=0` forces `mu4=mu5=b`; then
`B-L=-2a` and `T3R=b`, so `Y=b-a`, and `Y=0` forces `b=a`. Equivalently, such
a weight is an **SU(5) singlet carrying nonzero `U(1)_X` charge** — orthogonal
to every SU(5) root `e_i - e_j`. A planted control confirms the nonzero
condition does real work: the all-zero weight is an SM singlet with `B-L = 0`.

This also explains MJ-5's profile `[0,0,0,0,0,2]` structurally rather than
numerically: a weight of `Lambda^k(10)` has at most `k` nonzero components, so
only `k=5` can have five.

## The enumeration

For simply-laced `D5`, a dominant `mu` is a weight of `V_lambda` **iff**
`mu <= lambda` in the dominance order and `lambda - mu` lies in the root
lattice. Both are exact tests with a closed form, so the sweep is
**exhaustive below the bound, not sampled**, and needs no Freudenthal
recursion.

Every SO(10) irrep with dimension `<= 2000` that can break `B-L` while
preserving the Standard Model:

| dim | highest weight | singlet at | `|B-L|` |
|---:|---|---|---:|
| **16** | `(1/2,1/2,1/2,1/2,1/2)` | `c=1/2` | **1** |
| **126** | `(1,1,1,1,1)` | `c=1` | **2** |
| 144 | `(3/2,1/2,1/2,1/2,-1/2)` | `c=1/2` | 1 |
| 560 | `(3/2,3/2,1/2,1/2,1/2)` | `c=1/2` | 1 |
| 672 | `(3/2,3/2,3/2,3/2,-3/2)` | `c=1/2` | 1 |
| 720 | `(5/2,1/2,1/2,1/2,1/2)` | `c=1/2` | 1 |
| 1200 | `(3/2,3/2,3/2,1/2,-1/2)` | `c=1/2` | 1 |

> **The two smallest are exactly the 16 and the 126, and nothing below
> dimension 16 qualifies at all.**

Agreement with MJ-5 is a live control: the singlet, 10, 45, 54, 120 and 210 all
fail, and the adjoint's failure is re-derived here from the dominance test
rather than inherited.

**The 126 is the unique minimal *renormalizable* option.** A renormalizable
Majorana mass is an operator with `|Delta(B-L)| = 2`, and only the 126 carries
`|B-L| = 2`. Every other qualifying representation is spinor-class with
`|B-L| = 1` and can reach `M_R` only through a dimension-five operator,
suppressed by an additional scale.

## What this constrains

GU's declared bosonic content is a `2 x 2` table with two ad-valued entries,
`eps` and `$` — and MJ-2 showed the 126 has multiplicity exactly zero in both,
tilted-group robustly. So **SG4 cannot close these gaps by choosing among the
fields the table already declares.** It must add content, and the cheapest
addition that closes all three at once is a 126; the cheapest that closes them
at all is a 16.

That is a real cost, and it should be stated as one. GU's characteristic
posture is that field content is *derived from geometry* rather than declared;
a 126 of internal scalars is a large, conventional GUT-style addition, and a 16
of scalars is unconventional in a different way (it breaks matter parity and
needs a second scale).

**BD-2 does not block this.** BD-2 showed the 126 *channel* is repulsive, which
closes the **condensate** route — a composite. An **elementary** 126 scalar
declared by SG4 is a different object and is untouched by that result. The two
must not be conflated.

## Claim ceiling

**This is a constraint, not a derivation.** It says what SG4 would have to
contain to close the three gaps. It does **not** derive any field from GU, does
not claim SG4 does or should declare these, and does not predict that GU is
completable. The underlying group theory — that `B-L` breaking in SO(10) needs
a 16 or a 126 — is standard GUT representation theory and is not claimed as
novel. What is GU-native is the exhaustive certified enumeration in GU's own
setting, the structural reduction above, and the composition with MJ-2, MJ-5,
PV-1, BD-1 and BD-2 into a single named constraint.

**Bound-limited:** exhaustive below dimension 2000. Larger representations
qualify (the pattern continues), but none is minimal.

## The composed position

Within GU-as-declared: neutrinos are Dirac (symmetry-protected by MJ-5,
dynamically preferred by BD-2, matching the source's own mass channel under
BD-2's corrected `$` reading); nine non-SM gauge bosons remain massless
(PV-1/PV-2); and the matter asymmetry cannot be generated (BD-1). All three
failures share **one** missing object, and that object is now named exactly: a
scalar in the 16 or the 126.

Falsifier unchanged and still live: observation of neutrinoless double beta
decay.

## Next gate

The honest next move is no longer inside this channel. Either SG4 gets built —
which is Lane 1's action work and not this channel's property — or the composed
negative gets an independent hostile review before it hardens. Selection stays
inside this channel; repository-wide GU priority is unchanged, the superposition
/ source-residual workstream is untouched, and no ledger, canon, or
current-state surface moves.
