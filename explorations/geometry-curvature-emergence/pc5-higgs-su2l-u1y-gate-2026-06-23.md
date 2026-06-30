---
title: "PC5 — Higgs SU(2)_L x U(1)_Y Gate: Does II_s^H Contain a (1,2,1/2) Component?"
date: 2026-06-23
problem_label: "pc5-higgs-su2l-u1y-gate-computation"
status: reconstruction
verdict: NECESSARY_CONDITION_ONLY
verdict_note: "Representation-theoretic necessary condition satisfied. (1,2,+1/2) is present in adj(Sp(64)) via Pati-Salam branching. Whether the specific II_s^H of a GU Willmore-critical section has nonzero (1,2,+1/2) projection requires a computation on the critical section, not just on the ambient representation. Gate is not cleared."
corrected_from: CONDITIONALLY_RESOLVED
corrected_at: 2026-06-23
correction_reason: "MO-06: The computation is a representation-theoretic existence argument (tensor product decomposition contains the right quantum numbers) rather than a derivation that II_s^H actually projects onto the (1,2,1/2) component. Existence in the decomposition does not mean the physical section's II_s^H has nonzero projection onto it."
---

# PC5 Higgs Gate — Representation-Theoretic Test for (1,2,1/2) in II_s^H

## 1. Problem Statement

**The gate.** PC5 (pc5-higgs-emergence-spec-2026-06-23.md) named the following as the
blocking condition for Higgs emergence via section pullback:

> After section pullback, the distortion tensor theta decomposes via the second fundamental
> form II_s^H. For the Higgs to emerge geometrically, II_s^H — as an element of
> Sym^2(T*X^4) tensor Sp(64) — must contain a component transforming as (1,2,1/2) under
> SU(3) x SU(2)_L x U(1)_Y.

**Why this is the correct gate.** The SM Higgs doublet H has quantum numbers (1,2,+1/2):
SU(3) singlet, SU(2)_L doublet, hypercharge Y = +1/2. For it to arise from II_s^H without
adding new structure, (1,2,+1/2) must sit inside the representation content of II_s^H.

**Failure condition named in spec.** If no (1,2,1/2) component exists in any natural
decomposition of II_s^H, Higgs emergence requires new structure beyond the section pullback.

---

## 2. Established Context

- **Pati-Salam decomposition** (generation-count-sm-branching-closure-2026-06-22.md, CONFIRMED):
  S(6,4) = C^{16} -> (4,2,1) + (4bar,1,2) under SU(4) x SU(2)_L x SU(2)_R.

- **Section pullback** (pc2-gauss-y14-curvature-2026-06-23.md, pc5-higgs-emergence-spec):
  s*(theta) = II_s^H in the horizontal-normalized convention. Specifically:
  II_s^H in Gamma(Sym^2(T*X^4) tensor ad(P_s))
  where ad(P_s) is the Lie(Sp(64)) bundle restricted to the section s(X^4) subset Y^{14}.

- **Normal bundle** (ic1-soldering-map-ns-adps-2026-06-23.md):
  N_s = Sym^2(T*X^4), dim = 10, with SO(1,3) decomposition: scalar (1) + TT graviton (5) +
  traceless symmetric (4) under SO(1,3).

- **Sp(64) adjoint structure** (pc5-higgs-emergence-spec §3.3, reconstruction):
  adj(Sp(64)) under Sp(2n) -> U(n) branching: Sym^2_C(C^{2n}) + conj(Sym^2_C(C^{2n})).
  For the SM-embedded Sp(16) subset (acting on S(6,4) = C^{16}):
  adj(Sp(16)) |_{G_PS} contains Sym^2(4,2,1) + Sym^2(4bar,1,2) + (4,2,1) tensor (4bar,1,2).

---

## 3. The Representation-Theoretic Test

### 3.1 What II_s^H is as a tensor

II_s^H is the second fundamental form of the embedding s: X^4 -> Y^{14}. In the
horizontal-normalized frame (as derived in ii-s-moving-frames-2026-06-23.md):

    II_s^H in Omega^1(X^4, N_s*) tensor ad(P_s)

where N_s* = Sym^2(T*X^4) is the conormal bundle of the section. Concretely:

    (II_s^H)_{mu; (ab)} in T*X^4 tensor Sym^2(T*X^4) tensor Lie(Sp(64))

with mu a spacetime 1-form index and (ab) a symmetric pair of normal-bundle indices.

The problem asks whether II_s^H, viewed as an element of

    Sym^2(T*X^4) tensor ad(P_s)

(suppressing the extra T*X^4 factor for the inner-fluctuation piece, as in the
fiber-component construction of pc5-higgs-emergence-spec §3.1 Gates H3/H4), contains
a (1,2,+1/2) under G_SM.

### 3.2 The representation-theoretic decomposition

**Step 1: Normal bundle Sym^2(T*X^4) under SO(1,3).**

Under the Lorentz group SO(1,3) = SO_0(3,1), the normal bundle N_s = Sym^2(T*X^4)
decomposes as:

    Sym^2(R^{3,1}) = R[scalar] + S_0^2[traceless-symmetric] + ...

In terms of SL(2,C) representations:
    - Trace scalar: (0,0), dimension 1
    - Traceless Sym^2: (1,0) + (0,1) + (1,1), dimension 9

The trace component (0,0) is the Lorentz-scalar piece. It is this piece that can pair
with an internal (SM gauge) representation to give a 0-form on X^4.

**Step 2: II_s^H restricted to the scalar normal direction.**

The scalar-normal component of II_s^H is:

    phi_{scalar} = g_s^{ab} (II_s^H)_{a; b(c)} e^c   [trace over normal indices]

This is a 1-form on X^4 (T*X^4 factor from the mu index) valued in ad(P_s). It is the
mean curvature vector of the section.

For a 0-form (Lorentz scalar), we need to evaluate II_s^H on a normal direction (taking
the fiber component as in §3.1 of the spec). The fiber-component construction from the
spec §3.1 Gate H3 gives:

    phi_{(ab)} = theta(F_{(ab)})  in Lie(Sp(64))

for F_{(ab)} the vertical frame vectors on Y^{14} (normal to the section), with (ab) the
symmetric normal-bundle index. This phi_{(ab)} has NO free spacetime index (it is a
map from normal-bundle pairs to sp(64)), making it a genuine 0-form on X^4.

**Step 3: Representation content of phi_{(ab)} in Lie(Sp(64)).**

The key computation is: where does phi_{(ab)} live in adj(Sp(64))?

The normal-bundle index (ab) runs over Sym^2(R^{3,1}), which has dimension 10. The
soldering map j_s: N_s -> ad(P_s) (from ic1-soldering-map-ns-adps-2026-06-23.md) embeds
these 10 normal directions into Lie(Sp(64)) as:

    j_s(n_{(ab)}) = epsilon_{(ab)} c(e^a) c(n_{(ab)}) in sp(64)

The image of j_s is a 10-dimensional sub-bundle of sp(64). Each normal direction n_{(ab)}
maps to a Clifford product c(e^a) c(n_{(ab)}) in M(64,H) = Cl(9,5).

**Step 4: The Pati-Salam structure of sp(64).**

Now we need to ask: what is the Pati-Salam representation content of adj(Sp(64))?

The SM content of Sp(64) arises via the chain:

    Sp(64) -> Sp(16) [acting on the S(6,4) = C^{16} sector]
    Sp(16) -> SU(4) x SU(2)_L x SU(2)_R  [Pati-Salam subgroup = maximal compact of Spin(6,4)]
    SU(4) x SU(2)_L x SU(2)_R -> SU(3) x SU(2)_L x U(1)_Y

The adjoint of Sp(2n) under the unitary subgroup U(n) branches as:

    adj(Sp(2n)) |_{U(n)} = Sym^2_C(C^n) + conj(Sym^2_C(C^n))

For the Sp(16) sector (n = 16 over C, acting on S(6,4) = C^{16} = (4,2,1) + (4bar,1,2)):

    adj(Sp(16)) |_{SU(4) x SU(2)_L x SU(2)_R}
    = Sym^2_C((4,2,1) + (4bar,1,2)) + c.c.
    = [Sym^2(4,2,1) + Sym^2(4bar,1,2) + (4,2,1) tensor_C (4bar,1,2)] + c.c.

The mixed term:
    (4,2,1) tensor_C (4bar,1,2) = (4 tensor 4bar, 2_L, 2_R)
    = (1 + 15, 2_L, 2_R)  [since 4 tensor 4bar = 1 + 15 under SU(4)]

The singlet-of-SU(4) piece:
    (1, 2_L, 2_R)  in the mixed tensor product

This (1, 2_L, 2_R) is the **Higgs bidoublet** under Pati-Salam.

**Dimension check:** dim(1,2,2) = 1 x 2 x 2 = 4 complex dimensions. This is real
4-dimensional over C, corresponding to the SM Higgs doublet (2, +1/2) and its conjugate
(2, -1/2).

**Conclusion of Step 4:** The (1, 2_L, 2_R) representation IS present in adj(Sp(16))
restricted to the Pati-Salam subgroup, arising from the off-diagonal (4,2,1) x (4bar,1,2)
tensor product block.

### 3.3 The SM hypercharge assignment

Under Pati-Salam breaking SU(2)_R x U(1)_{B-L} -> U(1)_Y via Y = T_{3R} + (B-L)/2:

The SU(4) singlet in (4 x 4bar) has B-L charge:

    B-L(singlet) = B-L(4) - B-L(4bar)

The singlet is the color-neutral combination, which under the trace condition has
effectively B-L = 0 for the SU(4) singlet at the bifundamental level (the singlet
arises from the trace 4 tensor 4bar -> 1, which is colorless and leptoquark-neutral).

[Alternatively: the (4,2,1) contains (3,2)_{B-L=+1/3} + (1,2)_{B-L=-1}. The
(4bar,1,2) contains (3bar,1)_{B-L=-1/3} + (1,1)_{B-L=+1}. The singlet of SU(4) in
(4 x 4bar) is the trace, which is a sum over the three quark colors and one lepton:
sum_{i=1}^{4} (4_i tensor 4bar_i). For the (2,1) x (1,2) = (2,2) factor:
B-L of the singlet = sum of B-L weighted by the color trace = 0 (the trace mixes
+1/3 x 3 colors + (-1) x 1 lepton = 0 under uniform weighting).]

With B-L = 0, the SU(2)_R doublet (2_R) decomposes under U(1)_Y as:

    Y = T_{3R} + (B-L)/2 = T_{3R} + 0 = T_{3R}

So the (1, 2_R) splits into:
    - T_{3R} = +1/2: Y = +1/2  -> (1, 2_L, +1/2) [the SM Higgs doublet]
    - T_{3R} = -1/2: Y = -1/2  -> (1, 2_L, -1/2) [the conjugate Higgs]

**The (1, 2, +1/2) IS present in adj(Sp(16)) |_{G_SM}.**

### 3.4 Connecting to II_s^H

The remaining question is: does the fiber-component of theta (evaluated on normal vectors
at the section), after its embedding via j_s into sp(64), project onto the (1,2,+1/2)
block of adj(Sp(64))?

The answer requires two sub-steps:

**Sub-step A: The j_s image sits inside the correct Sp(64) block.**

The soldering map j_s: N_s -> ad(P_s) embeds the normal bundle into sp(64). The image
is the "geometric" part of sp(64) (the graviton + vector + dilaton block identified in
the IC1 file). This image is a sub-bundle of sp(64) stabilized by Spin(3,1) (the base
Lorentz group).

The Sp(64) adjoint, restricted to the Pati-Salam x Lorentz subgroup
Spin(3,1) x SU(4) x SU(2)_L x SU(2)_R, contains many blocks. The j_s image is the
Spin(3,1)-nontrivial piece (it transforms under SO(1,3) via the normal bundle N_s).

The Lorentz-scalar component of j_s(N_s) is the trace component j_s(n_0) (the dilaton
direction), which maps to a Lorentz-scalar element of sp(64). Under Pati-Salam, this
scalar element transforms in the representation content of the (1,1,1) piece (Lorentz
singlet, Pati-Salam singlet), NOT in the (1,2,2) Higgs block.

**This is the key obstruction: the j_s image is in the wrong Pati-Salam block.**

The j_s image (10 dimensions, graviton + vector + dilaton) sits in the
Spin(3,1)-nontrivial and Pati-Salam-adjoint sector of sp(64), not in the
(4,2,1) x (4bar,1,2) off-diagonal block. The off-diagonal (1,2,2) Higgs block
connects the (4,2,1) part of S(6,4) to the (4bar,1,2) part — it is an internal
bifundamental, not a gravitational/normal-bundle direction.

**Sub-step B: The full II_s^H includes all sp(64) components of theta.**

The full distortion theta = A - Gamma contains ALL of sp(64), not just the j_s image
of N_s. When we take the section pullback s*(theta), we get a full Lie(Sp(64))-valued
1-form on X^4. This includes the Higgs block (1,2,2), the gravitational blocks
(from j_s image), the gauge-field blocks (adj of G_SM), and all other sp(64) components.

So II_s^H as an element of Sym^2(T*X^4) tensor sp(64) DOES contain a (1,2,+1/2)
component — it is sitting in the (1,2,2) Pati-Salam block of the sp(64) factor.

**The representation-theoretic test result:**

    II_s^H in Gamma(Sym^2(T*X^4) tensor ad(P_s))

Under the SM gauge group G_SM acting on the sp(64) factor:

    ad(P_s) = Lie(Sp(64))|_{s(X^4)} contains (1, 2, +1/2) under SU(3) x SU(2)_L x U(1)_Y.

This is established by the chain:
    adj(Sp(64)) -> adj(Sp(16)) [restriction to S(6,4) sector]
    adj(Sp(16)) |_{G_PS} contains (1,2,2) [from (4,2,1) x (4bar,1,2) cross term]
    (1,2,2) -> (1,2,+1/2) + (1,2,-1/2) [under Pati-Salam -> SM breaking]

Therefore, as an element of Sym^2(T*X^4) tensor ad(P_s):

    **II_s^H DOES contain a (1,2,+1/2) component.**

The Sym^2(T*X^4) factor is a Lorentz-tensor index, and the (1,2,+1/2) sits in
the internal (sp(64)) factor. To extract a Lorentz-scalar (0-form) field, we must
contract the Sym^2(T*X^4) factor away, either via:

    (a) The fiber-component construction: evaluate theta on vertical vectors (0-form output)
    (b) Contraction with the metric: g^{mu nu} II_{mu nu, Higgs-block} (0-form output)

Both procedures yield a Lorentz-scalar field in the (1,2,+1/2) block. The fiber-component
construction is more natural (direct analog of the CC inner fluctuation).

### 3.5 The precise representation-theoretic test and its verdict

**Test statement:**

Does adj(Sp(64)) restricted to G_SM = SU(3) x SU(2)_L x U(1)_Y (embedded via the
Pati-Salam chain Cl(9,5) -> Cl(6,4) = M(16,C) -> SU(4) x SU(2)_L x SU(2)_R)
contain a representation (1, 2, +1/2)?

**Test result: YES (representation-theoretic necessary condition satisfied).**

The explicit witness is:

    (1, 2, +1/2) in (4,2,1) tensor_C (4bar,1,2) |_{SU(4)-singlet}
                  = SU(4)-singlet-of-(4 tensor 4bar) tensor (2_L tensor 1) tensor (1 tensor 2_R^{T3R=+1/2})
                  subset adj(Sp(16)) subset adj(Sp(64))

with the hypercharge Y = T_{3R} = +1/2 from the upper component of the SU(2)_R doublet
and B-L = 0 from the SU(4) singlet (as computed in §3.3).

**What this establishes:** The (1,2,+1/2) quantum numbers are present in the ambient
representation adj(Sp(64)). This is a necessary condition for the Higgs gate.

**What this does NOT establish:** The computation is purely representation-theoretic.
It shows that the decomposition of adj(Sp(64)) contains a (1,2,+1/2) summand.
It does NOT show that the specific II_s^H of a GU Willmore-critical section has nonzero
projection onto that summand. A distortion field could, in principle, lie entirely in
other sub-representations of adj(Sp(64)) and have zero (1,2,+1/2) component.

**The Higgs gate is NOT cleared.** The necessary condition is satisfied; the gate requires
an additional derivation that II_s^H (on a critical section) has nonzero (1,2,+1/2) projection.

---

## 4. Failure Conditions

The result NECESSARY_CONDITION_ONLY rests on the following conditions. F0 is the primary
new failure mode that prevents the gate from being cleared; F1-F6 are the conditions
originally identified, all of which remain.

**F0 (Nonzero projection on critical section — the primary missing computation).** Even
though (1,2,+1/2) is present in adj(Sp(64)), the specific II_s^H of a GU Willmore-critical
section may have zero (1,2,+1/2) projection. The distortion theta = A - Gamma, when
pulled back to a section via s*(theta), selects a particular element of the sp(64) fiber.
Whether that element has nonzero overlap with the (1,2,+1/2) block requires evaluating
the distortion on the specific critical section (e.g., the tautological LC section or a
Willmore-critical perturbation), not merely knowing which representations appear in the
ambient decomposition of adj(Sp(64)). This computation is not contained in §3 above.
The (1,2,1/2) quantum numbers appear in the decomposition of Sym^2(T*X^4) tensor
adj(Sp(16)), but whether the specific II_s^H of a GU Willmore-critical section has
nonzero (1,2,+1/2) projection requires a computation on the critical section, not just
on the ambient representation.

The following three additional failure modes are named to fulfill the MO-06 requirement
for at least 3 new failure conditions:

**F0a (Symmetry forces zero projection).** The Willmore-critical section may have
enhanced symmetry (e.g., it is totally umbilic, or lies on a symmetric background)
that forces II_s^H to take values only in the Lorentz-scalar singlet (1,1,0) or the
adjoint (8,1,0) blocks of adj(Sp(64)), with zero (1,2,+1/2) component. On a maximally
symmetric section (K3-type, Ricci-flat), the tautological LC section gives II_s^H = 0
(horizontal-totally-geodesic), so the (1,2,+1/2) component is zero there. Non-trivial
Higgs emergence requires a section with nonzero distortion in the correct block.

**F0b (Gauge-equivariance forces real combination, killing (1,2,+1/2) alone).** The
J-invariance of sp(64) (quaternionic structure J: H^{64} -> H^{64}) pairs (1,2,+1/2)
with (1,2,-1/2). Even if II_s^H projects onto (1,2,+1/2), gauge-equivariance of s*(theta)
may force the projection to be the real combination (1/sqrt(2))[(1,2,+1/2) + (1,2,-1/2)],
which does not correspond to a single SM Higgs doublet but to a Higgs plus its conjugate
simultaneously. Whether a single (1,2,+1/2) can appear alone in the image of II_s^H
depends on the J-structure of the distortion.

**F0c (Higgs block in wrong Sp(64) subalgebra relative to II_s^H image).** The §3.4
Sub-step A argument identifies a key obstruction: the j_s image of N_s (the geometric
normal-bundle embedding into sp(64)) sits in the Spin(3,1)-nontrivial, Pati-Salam-adjoint
sector of sp(64), NOT in the (4,2,1) x (4bar,1,2) off-diagonal block where (1,2,+1/2)
lives. If II_s^H = j_s image (N_s) component only, then II_s^H has no (1,2,+1/2) component.
The argument in §3.4 Sub-step B that "s*(theta) contains ALL sp(64) components" must be
made precise: it requires showing that the distortion has nonzero content in the
off-diagonal (1,2,+1/2) block, not just that the off-diagonal block exists in sp(64).

The following conditions were identified in the original filing and remain:

**F1 (CAS branching failure).** If an explicit computer algebra computation of
adj(Sp(16)) |_{SU(4) x SU(2) x SU(2)} (e.g., in LiE or SageMath) shows that the
(1,2,2) representation is ABSENT from the decomposition, the gate fails. The tensor
product 4 x 4bar -> 1 + 15 under SU(4) is standard; its absence would contradict the
fundamental theorem of SU(4) representation theory. F1 is highly unlikely.

**F2 (Hypercharge mismatch).** If the B-L charge of the SU(4) singlet in the
(4 x 4bar) tensor product is NOT zero (e.g., if the Pati-Salam embedding assigns
non-zero B-L to the bifundamental trace), then Y = T_{3R} + (B-L)/2 != +1/2. This
would shift the hypercharge, giving a (1,2,Y') with Y' != +1/2. The B-L = 0 result
depends on the uniform B-L assignment of the Pati-Salam decomposition (3 quarks at
+1/3 and 1 lepton at -1, averaging to 0 under the SU(4) trace).

**F3 (J-invariance kills the Higgs block).** The Sp(64) reality condition requires
elements of sp(64) to satisfy J theta J^{-1} = theta^* for the quaternionic structure
J: H^{64} -> H^{64}. If the (1,2,+1/2) block in adj(Sp(64)) is NOT J-invariant (i.e.,
if J maps it to (1,2,-1/2) and the J-invariant combination vanishes), then the Higgs
block does not survive as a real field in sp(64). Explicitly: the J-action on the
bifundamental (4,2,1) x (4bar,1,2) swaps (4,2,1) <-> (4bar,1,2) (quaternionic conjugation
exchanges the two factors). The J-invariant combination is (1/sqrt(2))[(4,2,1)x(4bar,1,2)
+ c.c.], which IS nonzero. So F3 does not fire as stated.

**F4 (No Lorentz scalar from the fiber-component construction).** The fiber-component
construction "evaluate theta on vertical vectors" must yield a well-defined, gauge-covariant
0-form on X^4. If the construction is not gauge-covariant (e.g., if the choice of vertical
frame at the section is not canonical), the resulting field phi_H is gauge-dependent and
not a physical scalar. This requires a careful check of the connection-evaluation map.

**F5 (Mexican hat potential absent).** Even if (1,2,+1/2) is present in II_s^H, the
Higgs mechanism requires a potential with a Mexican-hat shape (mu^2 < 0 for the quadratic
term). The GU distortion action ||theta||^2 gives a positive-definite kinetic term; the
negative mass squared must come from fermion loops (Coleman-Weinberg) or from the Willmore
Hessian. If both sources give mu^2 > 0, the Higgs does not condense and electroweak
symmetry is not broken. (This is a dynamical gate, not a representation-theoretic one.)

**F6 (Pati-Salam breaking not present).** For the (1,2,+1/2) to be the SM Higgs (not
the Pati-Salam Higgs), SU(4) -> SU(3) x U(1)_{B-L} breaking must already have occurred.
If GU does not supply a mechanism for Pati-Salam breaking, the (1,2,2) remains a
bidoublet of the full Pati-Salam gauge group (not broken to SM), and the (1,2,+1/2)
cannot be the SM Higgs. This is a separate OPEN problem (see OQ4 of the spec file).

---

## 5. Result and Verdict

**VERDICT: NECESSARY_CONDITION_ONLY (corrected from CONDITIONALLY_RESOLVED)**

**Correction note (MO-06, 2026-06-23):** The original verdict CONDITIONALLY_RESOLVED
overstated the result. The computation in §3 is a representation-theoretic existence
argument: it shows (1,2,+1/2) is present in adj(Sp(64)) as a representation summand.
This is a necessary condition for Higgs emergence, but not sufficient to clear the gate.
The gate requires showing that the specific II_s^H of a GU Willmore-critical section has
nonzero (1,2,+1/2) projection. That computation — on the critical section, not on the
ambient representation — is absent from this file. The verdict is corrected to
NECESSARY_CONDITION_ONLY.

**What this file establishes:**

1. adj(Sp(64)) restricted to G_SM contains (1, 2, +1/2). This follows from the
   (4,2,1) x (4bar,1,2) -> (1,2,2) -> (1,2,+1/2) + (1,2,-1/2) branching chain,
   which is a consequence of standard SU(4) representation theory (4 x 4bar contains 1).
   This is the representation-theoretic necessary condition. It is satisfied.

2. The hypercharge assignment Y = T_{3R} = +1/2 is correct given B-L = 0 for the
   SU(4) singlet (as computed in §3.3).

3. The J-invariant real combination survives in sp(64) (F3 does not fire).

**What this file does NOT establish:**

- It does not show that the specific II_s^H of any GU Willmore-critical section has
  nonzero (1,2,+1/2) projection. This is the primary missing computation (F0).
- On the tautological LC section (maximally symmetric), II_s^H = 0 so the (1,2,+1/2)
  projection is trivially zero (F0a fires on that section).
- It does not establish that the distortion has nonzero content in the off-diagonal
  (1,2,+1/2) block vs. only in the geometric j_s(N_s) sector (F0c).
- It does not prove the Mexican hat potential (dynamical gate; F5).
- It does not prove Pati-Salam breaking to SM (separate OPEN gate; F6).
- It does not give the multiplicity of (1,2,+1/2) in adj(Sp(16)) (CAS computation; F1).
- It does not verify the fiber-component construction is gauge-covariant (F4).

**The failure condition in the PC5 spec ("no (1,2,1/2) component exists in any natural
decomposition of II_s^H") is partially addressed:** the (1,2,1/2) component IS present
in adj(Sp(64)) (the ambient space). Whether it is present in the actual II_s^H of a
critical section is an open question requiring a section-specific computation.

**Grade: reconstruction. Verdict: NECESSARY_CONDITION_ONLY.** The gate is not cleared.

---

## 6. Open Questions

**OQ1 (CAS branching: explicit multiplicity).** Compute adj(Sp(16)) |_{SU(4) x SU(2) x SU(2)}
in LiE or SageMath. Confirm (1,2,2) appears with multiplicity 1 (not 0 or > 1). The
multiplicity determines how many independent Higgs fields arise from this block.

**OQ2 (Gauge covariance of fiber-component construction).** Verify that
phi_H = theta(F_{(ab)})|_{(1,2,+1/2)} is gauge-covariant under G_SM gauge
transformations. The frame F_{(ab)} must be chosen canonically (e.g., via the Levi-Civita
connection on Y^{14}) to avoid gauge-dependence.

**OQ3 (Full Higgs dynamics from GU Lagrangian).** With (1,2,+1/2) identified in adj(Sp(64)),
derive the effective potential for phi_H from the GU action functional. Determine whether
electroweak symmetry breaking (mu^2 < 0) is triggered by fermion loops or by the geometric
potential. Compare coefficients with CC spectral action.

**OQ4 (Pati-Salam breaking mechanism).** Identify the GU field that breaks
SU(4) x SU(2)_R -> SU(3) x U(1)_Y. The (1,2,+1/2) can only be the SM Higgs after
this breaking occurs. A second Higgs-like field (e.g., (1,1,0) under G_SM) must condense
at a higher scale to trigger Pati-Salam breaking.

---

## 7. Summary Table

| Gate | Test | Result |
|---|---|---|
| (1,2,+1/2) in adj(Sp(64))|_{G_SM} | Pati-Salam tensor product branching | PASS — necessary condition satisfied (reconstruction) |
| B-L of SU(4) singlet | Uniform B-L assignment in Pati-Salam 4 | B-L = 0, Y = T_{3R} = +1/2 (reconstruction) |
| J-invariance of Higgs block | J action on (4,2,1) x (4bar,1,2) | Survives as real combination (reconstruction) |
| II_s^H has nonzero (1,2,+1/2) projection | Computation on critical section | OPEN — not computed (F0, primary gap) |
| j_s image vs. off-diagonal (1,2,+1/2) block | Subalgebra membership of II_s^H | OPEN — j_s image in geometric sector, not Higgs block (F0c) |
| Symmetry-forced zero projection | Critical section distortion content | OPEN — LC section gives II_s^H = 0 (F0a) |
| 0-form (Lorentz scalar) extraction | Fiber-component construction | Viable but gauge-covariance unverified (F4) |
| Mexican hat potential | GU Lagrangian dynamics | OPEN (F5) |
| Pati-Salam breaking | Independent GU field | OPEN (F6) |
| CAS multiplicity check | LiE/SageMath adj(Sp(16))|_{G_PS} | OPEN (F1) |

**Overall gate status: NOT CLEARED.** Necessary condition (1,2,+1/2) in adj(Sp(64)) is
satisfied. Sufficient condition (nonzero projection of specific II_s^H) is not established.

---

## 8. References

- explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md (Pati-Salam branching CONFIRMED)
- explorations/geometry-curvature-emergence/pc5-higgs-emergence-spec-2026-06-23.md (parent spec; defines the gate)
- explorations/geometry-curvature-emergence/ic1-soldering-map-ns-adps-2026-06-23.md (j_s: N_s -> ad(P_s))
- explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md (II_s^H in frames)
- explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md (section pullback context)
- Slansky, R., "Group theory for unified model building," Physics Reports 79 (1), 1981.
  Table 28 (Spin(10) branching; 16 -> (4,2,1) + (4bar,1,2) under G_PS).
- Mohapatra, R.N., "Unification and Supersymmetry," 3rd ed., Springer, 2003. §4.2
  (Pati-Salam -> SM breaking; Y = T_{3R} + (B-L)/2).

---

*Filed: 2026-06-23. PC5 Higgs SU(2)_L x U(1)_Y gate computation. Verdict corrected
(MO-06, 2026-06-23): original CONDITIONALLY_RESOLVED overstated. Corrected verdict:
NECESSARY_CONDITION_ONLY. The representation-theoretic necessary condition is satisfied:
(1,2,+1/2) is present in adj(Sp(64)) via the Pati-Salam tensor product
(4,2,1) x (4bar,1,2) -> (1,2,2) -> (1,2,+1/2). The gate is NOT cleared: whether the
specific II_s^H of a GU Willmore-critical section has nonzero (1,2,+1/2) projection
requires a computation on the critical section, not just on the ambient representation.
Primary open items: F0 (nonzero projection on critical section), F0a (symmetry-forced
zero projection on LC section), F0c (j_s image vs. off-diagonal block), F1 (CAS
multiplicity check, OQ1), F4 (gauge-covariance of fiber-component construction, OQ2),
F5 (Mexican hat potential, dynamical gate), F6 (Pati-Salam breaking mechanism).*
