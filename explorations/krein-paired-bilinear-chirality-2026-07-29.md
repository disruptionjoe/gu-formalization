---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "KREIN-PAIRED BILINEAR CHIRALITY: verdict BRIDGE-SUCCEEDS, retracting the same-day BRIDGE-FAILS result. The earlier probe measured the OPERATOR e_vertical against omega_4 (0/10 cross-chirality); the physical object is the BILINEAR <Psi, M Psi>_K, and GU's Krein form is itself 4D-chirality-crossing -- K ANTICOMMUTES with omega_4. The composite K.e_vertical is therefore cross-chirality on 10/10 fibre directions and on every split tested. Control N1 is decisive against triviality: composing with K INVERTS the pattern, taking the base directions from 4/4 cross to 0/4, so K exchanges the two classes rather than flipping everything. N2 confirms an identity pairing does not restore the channel. Consequence: T10 is NOT established as required, and Weinstein's 'minimal coupling and Yukawa coupling are the same thing' survives this test."
grade: "EXACT on the verified in-repo Cl(9,5) representation, all controls passing including a pattern-inversion control and a planted identity-pairing control. SCOPE: establishes cross-chirality only, which is NECESSARY and NOT SUFFICIENT for a Dirac mass. Lorentz invariance in 4D, landing in the Lambda^0 channel SA-Y1 names, non-vanishing, and magnitude are all separately open."
probe: tests/channel-swings/krein_paired_bilinear_chirality_probe.py
retracts: explorations/vertical-vev-chirality-bridge-2026-07-29.md
construction: "program-native Cl(9,5) = M(64,H) with the in-repo Krein operator (product of the nine plus-gammas). No positive-Hilbert substitution."
origin: "Joe direct chat, 2026-07-29, reasoning from the Bateman-Turok / Mannheim ghost-parity position"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: "BRIDGE-SUCCEEDS"
---

# The Krein-paired bilinear, and why the earlier verdict was wrong

## The error, stated plainly

The same-day vertical-vev probe asked whether the **operator** `e_vertical`
flips `omega_4`. It does not — 0/10. That arithmetic was correct and its
controls all passed.

**The question was wrong.** A mass term is not an operator. It is a **bilinear**

```text
<Psi, M Psi>_K  =  Psi^dagger K M Psi
```

and in a Krein setting the pairing `K` carries chirality structure of its own.
The earlier probe never composed `K` with `M`. Correct arithmetic, wrong object.

## The origin of the correction

Joe, reasoning from the Bateman–Turok / Mannheim ghost-parity position: one works
**with** the indefinite structure rather than removing it, so the pairing is not
inert bookkeeping and has to be composed in. That is exactly what was missing.

## Result

| | cross-chirality under `omega_4` |
|---|---|
| bare `e_a`, fibre — *what the earlier probe measured* | **0/10** |
| `K . e_a`, fibre — *what a mass term actually is* | **10/10** |

`K` **anticommutes** with `omega_4`. GU's Krein form is documented as *"purely
cross-chirality"*; the explicit computation confirms it acts that way against
the 4D chirality operator too. So chirality-crossing composed with
chirality-preserving is chirality-crossing, and the bilinear supplies the mass
channel the bare operator could not.

## Why this is not trivial — the control that matters

If `K` simply flipped everything, the result would be vacuous. **It does not.**
Control `N1`:

| | bare | composed with `K` |
|---|---|---|
| **base** directions | 4/4 cross | **0/4 cross** |
| **fibre** directions | 0/10 cross | **10/10 cross** |

Composition with `K` **inverts** the pattern. It exchanges the two classes,
which is precisely what a cross-chirality pairing should do — and it is why the
base route (which looked like the mass route bare) is the one that closes once
the pairing is included. `N2` confirms an identity pairing leaves the fibre
directions chirality-preserving, so the effect is `K`'s, not an artifact. `N3`
holds it across alternative base/fibre assignments.

## Consequence for the build

- **`T10` is NOT established as required.** It returns to open rather than
  confirmed-necessary.
- **`SA-Y1`'s status returns to the Layer-0 `UNCERTAIN`** it had before the
  earlier probe over-resolved it.
- **Weinstein's claim survives this test.** *"Minimal coupling and Yukawa
  coupling are the same thing. The only thing that's really different is the
  spin."* On the chirality axis, in the Krein setting, that now checks out.

## What is still NOT shown — binding

**Cross-chirality is necessary, not sufficient.** This result does not show:

- that the resulting mass is **Lorentz-invariant** in 4D;
- that it lands in the **`Lambda^0` channel** `SA-Y1` names, rather than merely
  being cross-chirality;
- that it is **non-vanishing**;
- anything about its **magnitude**.

Each is separately open, and the `Lambda^0`-channel question is the one that
would actually close `SA-Y1`. The honest state is that the chirality obstruction
is removed and the channel-identification question is untouched.

## Method note worth keeping

Two probes, same day, opposite verdicts, both with passing controls. The
difference was **which object the question was about**. Controls verify that you
computed what you said; they do not verify that you asked the right thing. That
is what Layer-0 is for, and it should have been run on "what is a mass term" as
well as on "what is a Higgs."
