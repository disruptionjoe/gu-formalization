---
title: "Persona 36 — Zero-Knowledge / Pedersen-Commitment Cryptographer"
status: process
doc_type: persona_pass
updated_at: "2026-06-26"
---

# Persona 36 — Zero-Knowledge / Pedersen-Commitment Cryptographer

**Lens:** commitment schemes and Sigma-protocols — binding vs hiding, special-soundness witness extraction, Fiat-Shamir self-certification, trusted setup / CRS.

## One-sentence steelman

The shiab is the opening move of a commitment scheme: `d: Omega^1 -> Omega^2` commits the spinor field into a larger carrier, the observer's metric supplies the Fiat-Shamir challenge, and the "knock-back" `Omega^2 -> Omega^1` is the response; `d^2 = 0` is the binding/soundness condition.

## What this lens uniquely contributes

The binding/hiding split maps exactly onto the repo's gap structure: **hiding** (`Phi` non-injective, large kernel) is *settled* in canon; **binding** (does `d^2 = 0` survive the roll-up?) is the *open* gap — which predicts the obstruction lands on the soundness side, exactly where BRST / the no-go map already locate it. The "two-plus-one, third an imposter" reads as two witness-backed accepting transcripts (special soundness extracts a witness from two) plus one **ZK-simulator** transcript that passes the verifier with no extractable witness — a hiding-side artifact, not a real family.

## Concrete lead [concrete_lead]

Compute the binding subspace as a **linear** problem: `I_bind = Hom_{Spin(9,5)}(Lambda^2 V ⊗ S, V ⊗ S)` (Schur, finite, runnable with the existing `Cl(9,5)=M(64,H)` machinery), then impose closedness + no-obstruction as linear constraints. Three falsifiable outcomes: `dim I_bind = 1` (the selector is uniquely pinned — the OPEN "source-forced selector identity" closes), `= 0` (no sound commitment exists — "three-generations-as-a-proof" FAILS), `> 1` (residual blinding freedom = the observer's choice).

## Observer-creates-reality tie-in

The trusted-setup ceremony is GU "without making any choices" before a choice is made; the observer's metric is the toxic-waste/challenge that binds. Binding = finality (the commitment cannot be reopened = "the past is hard to undo"); hiding = the shadow (the witness is information-theoretically lost).
