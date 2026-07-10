---
title: "Exhaustiveness-by-type: PARTIALLY CLOSED -- three odd-primary escape routes shut, one open. tmf/String structurally shut (K3 is Spin-not-String, (1/2)p1=-24 infinite order); internal triality/SU(3)/qutrit Z/3 PROVABLY stranded (a family symmetry that commutes with the Dirac operator can only LABEL generations, never move the net count); every odd-primary stable-homotopy object is a DETECTOR collapsing onto the already-located pi_3^s. The SOLE surviving odd-primary object that both lives on the actual geometry and is not provably decoupled is the geometric equivariant Nikulin carrier-B rho (class (0,2,1)/3) -- which is EXACTLY the program's already-named single decider (SG4 + order-3-class->integer-3). Net: the investigation did not find a new escape; it PROVED THE DECIDER IS UNIQUE -- nothing routes around SG4."
status: staged
doc_type: results
created: 2026-07-10
grade: "COMPUTED / exact (2 build legs + 2 hostile referees, all exit 0 in-repo; 0 refuted, escape_missed=false both). All load-bearing group/structure facts fetched from primary sources this run (K3 sigma=-16 -> (1/2)p1=-24 Wikipedia/Hirzebruch; string obstruction=(1/2)p1 nLab; MString->tmf Ando-Hopkins-Rezk nLab; pi_*(tmf) nLab; Spin(8) triality fixed=G2 Wikipedia/arXiv:2502.14016; e_KO(8nu)=1/3). Internal Z/3 stranding closure re-derived two ways (exact frame-charge factorization + the load-bearing rep-theoretic argument: a Z/3 commuting with D gives a g-independent net index). Internal tier for the GU-facing corollary; the tmf-inapplicability (Spin-not-String) and the commuting-symmetry-labels-not-counts arguments are structural. No claim-ledger row moves; the generation count stays OPEN."
depends_on:
  - canon/ko-degree-obstruction-ladder-RESULTS.md
  - canon/two-primary-lemma.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - canon/w2-y14-spin-structure.md
scripts:
  - tests/exhaustiveness/leg_tmf_string.py
  - tests/exhaustiveness/leg_triality_equivariant.py
  - tests/exhaustiveness/verify_tmf_string.py
  - tests/exhaustiveness/verify_triality_equivariant.py
---

# Exhaustiveness-by-type: is there a non-KO/Spin/Pin odd-primary obstruction?

The KO-degree ladder left one open gap: the universal reading of the two-primary lemma ("no
obstruction can carry odd torsion") rode an unproven completeness-by-type premise. This run attacks it
directly. Outcome: **PARTIALLY CLOSED -- three routes shut, one open, and the open one is the program's
already-named single decider.**

## Route-by-route

- **tmf / String-oriented -- CLOSED (structural).** A tmf/Witten obstruction is by construction a
  function of `(1/2)p1` that exists only on a String manifold (`sigma: MString -> tmf`, Ando-Hopkins-
  Rezk). The GU generation sector is **Spin-not-String**: `(1/2)p1[K3] = (1/2)(3 sigma) = -24`, of
  INFINITE order in `H^4(K3;Z) = Z` (not even rational-String) -- so `MString -> tmf` never acts on the
  geometric base. Total space `Y14 -> pi_14(tmf) = Z/2` (2-primary even in the String hypothetical);
  doubled `K3 x K3 -> pi_8(tmf) = Z (+) Z/2`; `RP^3` spine `-> pi_3(tmf) = pi_3^s = Z/24` (S->tmf iso
  through deg 6 -- the SAME already-located order-3 arena, no new object). One residual crack -- the
  13-dim boundary could a priori be String and hit `pi_13(tmf) = Z/3` -- is doubly gated (String-ness
  obstructed/unbuilt; NO theorem equating the Witten genus with the net-chiral count) and collapses
  into already-named bridges. Carries NO new odd obstruction.
- **Internal triality / Spin(8) / SU(3)-family / qutrit Z/3 -- CLOSED (provably stranded, upgraded from
  OBSERVED).** This IS genuine odd torsion. But it is a family SYMMETRY on the internal fiber, and the
  load-bearing closure is representation-theoretic: **a Z/3 that COMMUTES with the Dirac operator gives
  a `g`-independent net equivariant index (net count = the `g=1` index), so it can only LABEL
  generations by family charge, never move the total** -- and this disarms anomaly inflow (a symmetry
  cannot change a symmetry-invariant net index by any channel). Corroborated by the exact self-dual
  tangent-frame charge `= Tr(L^dag) Tr(Z) = 0` (every `so(4)` generator traceless; positive control
  fires nonzero). SCOPE CAVEAT: proven for a Z/3 placed internally (commuting with D); that GU so
  places the triality outer automorphism is reconstruction-tier.
- **Odd-primary stable homotopy (alpha-family at p=3, Adams-e odd part) -- CLOSED into the located
  arena.** `e_KO(8 nu) = 1/3` DETECTS the Z/3 -- but a detector is not an obstruction. The p=3
  alpha-stems coincide with the tmf 3-stems; the sector supplies frame pieces only in the old arena.

## The one open route -- and it is the existing decider

- **Geometric equivariant Nikulin carrier-B Z/3 -- OPEN (the sole residual).** An order-3 SYMPLECTIC
  automorphism acting on SPACETIME (K3, 6 fixed points), whose self-dual part scores NONZERO frame
  charge -- it lives in the gravitational/tangent-frame channel the count lives in. Its equivariant rho
  carries a nonzero order-3 class `(0,2,1)/3 = 2*(Dirac class)` (Homma-Semmelmann; Baer-Mazzeo). This
  is exactly the un-enumerated, 3-primary object the exhaustiveness gap warned about: **EQUIVARIANT
  Spin/KO_{Z/3} reaches odd torsion that ORDINARY (non-equivariant) KO cannot** -- so the KO-ladder's
  non-equivariant coverage does NOT extend to it. Honestly OPEN.

## The verdict: the decider is UNIQUE (the real result)

The investigation did NOT surface a fresh escape. It **proved the decider is unique**: tmf/String,
internal triality, and generic odd-primary stable homotopy are all closed off as independent
side-routes, so **nothing routes AROUND the SG4 / order-3-class->integer-3 channel.** The sole
surviving odd-primary object that lives on the actual geometry and is not provably decoupled is the
geometric equivariant Nikulin carrier-B rho -- which coincides EXACTLY with the program's already-named
"single decider" (the equivariant RS index on GU's actual 14-manifold, gated on SG4 + the order-3->3
bridge). It is a FORCING LEAD, not a forcing: `(0,2,1)/3 != 0` LOCATES an order-3 slot on the real
geometry the way `e_R` does; it does not by itself force the integer 3, and it tilts the same way the
rest of the program does ("2+1 effective, third is an imposter").

## Scope sharpening for the two-primary lemma / KO-ladder (honest correction)

The structural 2-primary blindness is proven for **NON-equivariant** KO/Spin/Pin invariants. It does
NOT extend to **equivariant** Spin/KO (G-index, rho), which genuinely reaches the odd torsion -- and the
ONE equivariant order-3 object that does so is precisely the LOCATED carrier (Nikulin rho / e_KO), the
detector that locates the count without forcing it. So "located, not forced" sharpens to: **the count
is LOCATED by an equivariant order-3 detector on the real geometry, and no NON-equivariant obstruction
can constrain it; forcing would require that equivariant object to COUPLE to the net count, which is
exactly the SG4 + order-3->integer-3 gate -- the program's single decider, now proven to have no
side-routes.**

## Grade

- tmf/String route: CLOSED (structural; Spin-not-String).
- Internal triality Z/3: CLOSED (provably stranded; commuting-symmetry argument).
- Odd-primary stable homotopy: CLOSED (detector, not obstruction; collapses to pi_3^s).
- Geometric equivariant Nikulin Z/3: OPEN = the existing single decider (SG4 + order-3->3), NOT a new
  escape.
- Net: located-not-forced is NOT a fully general closed theorem, but the odd-primary escape surface is
  reduced from "any un-enumerated obstruction" to ONE named channel that coincides with the decider.
  The count stays OPEN; the FORCE step is unchanged as the single open conjecture.
