# Agents Start Here

## What this repo is

The construction program for GU's missing **RS/IG source action**.
- Parent (finished audit): `../gu-formalization`.
- The target: `SPEC.md`.
- Current front-door candidate lens: `CRYPTOECONOMIC-SOURCE-ACTION.md`.
- Do-NOT-re-walk list: `DEAD-ENDS.md`.
- Running ledger: `DERIVATION-PROGRESS.md`.

## The discipline (non-negotiable — this is the whole value of the program)

1. **COMPUTE** on the explicit Cl(9,5) representation (via `lib/gu_bridge.py`), never just argue in words.
2. **ADVERSARIALLY ATTACK** every candidate — default to refuting it. This lineage has been burned repeatedly
   by seductive closures and forced analogies (`DEAD-ENDS.md`). **"It fits beautifully" is a warning, not
   evidence.**
3. **LAND ONLY WHAT SURVIVES.** Honest negatives are valuable and MUST be recorded. **Never import the
   target** (no `24/8 = 3`, no assumed-K3, no fitting to the answer).
4. **The four guards** (inherited from the parent's hardest results):
   - ANTI-TRAP: the bare constraint commutator `||[Pi_RS, M_D]||` must stay **58.72** — driving it to 0 is
     acausal decoupling (the Velo-Zwanziger trap), an automatic FAIL.
   - ANTI-FIXED-SOLVE: a carrier must be an **a-priori** geometric object, not solved from the target.
   - ANTI-VACUOUS: nilpotency / closure must be genuine, not trivially-zero on a degenerate complex.
   - ANTI-IMPORT: reaching a number must not smuggle in the matter-generation target.

## Current best candidate lens

Before inventing another local selector, read `CRYPTOECONOMIC-SOURCE-ACTION.md`.

The live steelman is that `S_IG` may be a **security-budget source action**:

```text
Score(phi)
  = GrowthValue(phi)
  - ValidationCost(phi)
  - FinalizationCost(phi)
  - WorstCaseAdversarialLoss(phi)
```

Here the adversary is not a person. It is the space of rival mathematical completions: alternate shiab
members, boundary sections, RS/BRST closures, theta couplings, index regularizations, target imports, and
acausal traps. This lens earns attention only if its loss channels are GU-native and computable.

## The target (SPEC.md, in one breath)

A BV source action `S_IG` with: the master equation `(S,S)=0`; a Noether identity that **forces** the
constraint (rather than imposing it by hand); a **non-equivariant** ghost (proven necessary); a **full BV
bicomplex** realizing the constraint cohomologically (NOT a clean decoupling, which is acausal); and the three
**global** objects the existing data lacks — a families pushforward, a boundary holonomy / spectral section,
and a BV-to-boundary-Dirac map. **Warning:** the natural characteristic-class number is **-5376, not 24**, so
even full success on the algebra does not guarantee "three generations." That is the real bar.

## How to use the verified foundation

```python
from lib import gu_bridge
e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()   # the verified setup
print(gu_bridge.C2())          # 155.3625  (the obstruction to reconcile)
print(gu_bridge.anchors())     # bare commutator 58.7215, C2 155.3625, gu path
```

Build ON these objects; do not re-derive them. They are already adversarially verified in the parent repo.

## Workflow pattern

Mirror the parent: **design candidates -> build + compute on the rep -> adversarial kill -> land survivors
with receipts.** Record every honest negative in `DERIVATION-PROGRESS.md`. A turn that proves a candidate
fails is a successful turn.
