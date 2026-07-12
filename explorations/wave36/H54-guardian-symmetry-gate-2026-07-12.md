---
artifact_type: exploration
status: exploration
created: 2026-07-12
wave: 36
title: "H54 guardian-symmetry gate -- Sp(32,32;H)+[P,S]=0 is compatible with a guardian but is not itself one"
grade: "COMPUTED as a necessary-condition gate over the repo's current finite data; reconstruction-tier interpretation. No canon, claim-status, scientific-status, public-posture, or verdict movement."
depends_on:
  - tests/wave36/H54_guardian_symmetry_gate.py
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/misc/super-ig-algebra-construction-2026-06-23.md
---

# Wave 36 -- H54 guardian-symmetry gate

Test: `tests/wave36/H54_guardian_symmetry_gate.py` (deterministic, exit 0).

## Question

H54 asks whether the newly sharpened GU source-action data,

```text
Sp(32,32;H) + [P,S] = 0
```

already furnish the guardian symmetry needed for a UV-complete interacting massive Rarita-Schwinger sector:
local SUSY, super-IG, or an equivalent local odd gauge principle.  A yes would be huge because the
super-Higgs/gravitino template is the known way to avoid the Rahman finite-cutoff branch and might also pin
`mu_DW`.

This run does not try to build that action.  It only guards the definition of "guardian."

## Necessary conditions

A GU guardian must supply at least:

1. a local odd parameter;
2. a nonzero equivariant odd-square bracket, the analogue of `{Q,Q}`;
3. a transformation law on the RS/spin-1/2 Dirac-DeRham block system;
4. a Ward identity or first-class constraint preserving the gamma-trace domain;
5. a super-Higgs-like scale relation that could pin `mu_DW`;
6. compatibility with the existing Krein/Cartan square `[P,S]=0`.

The current structures supply item 6 and an even finite source-action arena.  They do not supply items 1-5.

The arithmetic anchor matches the Wave 34/35 bookkeeping:

```text
dim sp(32,32;H) = 8256
dim so(9,5) = 91
codim = 8165
```

So the current data are still the even source-action arena plus the soldering/Krein square.  That can be a
compatibility condition for a guardian.  It is not a local odd guardian.

## Controls

The test uses two controls.

- A formal super-IG algebra after supplying `Q` and `beta` passes the first two requirements, but still lacks
  the RS-block action, the gamma-trace Ward identity, the super-Higgs scale relation, and Krein compatibility.
  This restates the June super-IG note in the sharper H54 language: an algebra on connection space is not yet
  a VZ/super-Higgs guardian.
- The supergravity gravitino template is the positive control: it has the local odd gauge symmetry, closure,
  Ward identity, and super-Higgs relation.

## Result

```text
CURRENT_STRUCTURES_COMPATIBLE_BUT_NOT_GUARDIAN
```

This is a narrow negative result, not a no-go against H54.

It says:

- `Sp(32,32;H)` is an even gauge/source-action arena.
- `[P,S]=0` is an even Krein/Cartan compatibility square.
- Together they are compatible with a future guardian but do not furnish the guardian data.
- The H54 construction burden is now exact: supply `Q`, `beta`, the RS/spin-1/2 transformation law, the
  gamma-trace Ward identity, and a super-Higgs-like scale relation for `mu_DW`.

## Honest limits

This does not prove that GU lacks a guardian.  It proves only that the structures currently named by the
Wave 34/35 landscape assessment do not already contain one.  A future H54 construction can still succeed by
adding the missing odd data and showing that it acts on the full Dirac-DeRham system.

No claim status, canon verdict, generation-count status, public posture, or scientific verdict changes here.
