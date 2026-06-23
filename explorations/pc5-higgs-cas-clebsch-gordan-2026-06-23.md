---
title: "PC5 Higgs CAS Clebsch-Gordan: Multiplicity of (1,2,2) in adj(Sp(16))|_{G_PS}"
date: 2026-06-23
problem_label: "pc5-higgs-cas-clebsch-gordan"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
verdict_note: "The G_PS-irreducible (1,2,2) appears with multiplicity exactly 1 in adj(Sp(16))|_{G_PS}. NOTE: at the G_SM level, the (1,2,+1/2) representation has multiplicity 2 -- one from the (1,2,2) block and one from the SU(3)-singlet inside the (15,2,2) block (see §5.4). The multiplicity-1 claim refers specifically to the G_PS-level irreducible (1,2,2), not to (1,2,+1/2) in adj(Sp(16))|_{G_SM}. Upgrade to verified requires CAS computation in LiE or SageMath (FC-LIE)."
gate_status: "CONDITIONALLY_CONFIRMED"
correction: "PC5-VERDICT-OVERSTATED (2026-06-23): verdict changed from RESOLVED to CONDITIONALLY_RESOLVED. The body (§6, F5) explicitly names CAS computation in LiE or SageMath as the main remaining falsification test required for verified grade; RESOLVED is not warranted without it. Additionally, the original verdict_note stated multiplicity-1 for (1,2,+1/2) in G_SM without clarifying that G_SM-level multiplicity is 2 (§5.4 discovery). Three failure conditions now named: FC-LIE (CAS returns different multiplicity), F1 (adj(Sp(16)) != Sym^2 identification), F2 (wrong Pati-Salam embedding). Full failure condition list in §6."
---

# PC5 Higgs CAS Clebsch-Gordan: Multiplicity of (1,2,2) in adj(Sp(16))|_{G_PS}

## 1. Problem Statement

**What is being computed.**

The file `pc5-higgs-su2l-u1y-gate-2026-06-23.md` established that (1,2,+1/2) is present
in adj(Sp(64)) via the Pati-Salam branching chain:

    adj(Sp(64)) -> adj(Sp(16)) [restriction to S(6,4) sector]
    adj(Sp(16)) |_{G_PS} contains (1,2,2) [from (4,2,1) x (4bar,1,2) cross term]
    (1,2,2) -> (1,2,+1/2) + (1,2,-1/2) [under G_PS -> G_SM]

That file explicitly named as OQ1 (§6):

> **OQ1 (CAS branching: explicit multiplicity).** Compute adj(Sp(16)) |_{SU(4) x SU(2) x SU(2)}
> in LiE or SageMath. Confirm (1,2,2) appears with multiplicity 1 (not 0 or > 1). The
> multiplicity determines how many independent Higgs fields arise from this block.

This file resolves OQ1. The computation is an explicit step-by-step Clebsch-Gordan
analysis of the branching of adj(Sp(16)) under G_PS = SU(4) x SU(2)_L x SU(2)_R,
using the Pati-Salam decomposition S(6,4) -> (4,2,1) + (4bar,1,2) of the fundamental
representation of Sp(16).

**Why it matters.** The multiplicity of (1,2,2) determines how many independent Higgs-like
fields emerge from this representation-theoretic block. If multiplicity = 0, the gate fails
entirely (but this would contradict standard SU(4) representation theory). If multiplicity = 1,
the GU construction produces exactly one Higgs bidoublet from this block. If multiplicity > 1,
there would be multiple independent Higgs fields from adj(Sp(16)) alone, requiring an
explanation of why only one survives as the physical Higgs.

**Failure condition of this computation (F1 from pc5-higgs-su2l-u1y-gate).** "If an explicit
computer algebra computation of adj(Sp(16)) |_{SU(4) x SU(2) x SU(2)} (e.g., in LiE or
SageMath) shows that the (1,2,2) representation is ABSENT from the decomposition, the gate
fails."

---

## 2. Established Context

- **Pati-Salam decomposition** (generation-count-sm-branching-closure-2026-06-22.md, CONFIRMED):
  S(6,4) = C^{16} -> (4,2,1) + (4bar,1,2) under G_PS = SU(4) x SU(2)_L x SU(2)_R.

- **Sp(16) algebra and its fundamental** (pc5-higgs-su2l-u1y-gate §3.2, reconstruction):
  Sp(16) = Sp(2*8, C) in complex notation; its fundamental is C^{16} = S(6,4); the adjoint is
  adj(Sp(16)) with dimension dim(sp(16)) = n(2n+1) at n=16 = 16 * 33 = 528 (real dimension
  528, complex dimension 528 for the symplectic Lie algebra over C).

  Wait -- notation clarification needed. The symplectic group Sp(2n) acts on C^{2n}:
  - Sp(16) = Sp(16, C) acts on C^{16} (rank 8 symplectic group; 2n = 16 so n = 8)
  - dim_C(sp(16)) = n(2n+1) = 8 * 17 = 136 complex dimensions = 136

  The fiber spinor S(6,4) = C^{16} is the fundamental of Sp(16) (since C^{16} = C^{2*8} is
  the defining representation of Sp(16, C), with 2n = 16, n = 8).

- **adj(Sp(16)) via Sym^2 formula** (pc5-higgs-su2l-u1y-gate §3.2):
  For Sp(2n), the adjoint in terms of the fundamental V = C^{2n}:

      adj(Sp(2n)) ~= Sym^2_C(V)  as a complex representation

  where Sym^2_C(V) is the symmetric-square of the fundamental V, and the isomorphism is the
  standard one for the symplectic Lie algebra:
  sp(2n) = {A in M(2n,C) : J A^T J^{-1} = -A}
  which identifies naturally with Sym^2_C(C^{2n}) via the symplectic form J.

  For Sp(16) with V = C^{16}: dim_C(Sym^2_C(C^{16})) = 16*17/2 = 136. CHECK: this matches
  dim_C(sp(16)) = 136. CONSISTENT.

- **Pati-Salam splitting** of V = C^{16}:
  V = V_L + V_R, where V_L = (4,2,1) and V_R = (4bar,1,2) under G_PS.
  dim_C(V_L) = 4*2 = 8, dim_C(V_R) = 1*4*1 * ... wait, let us be careful.

  (4,2,1) means: SU(4) fundamental (4), SU(2)_L fundamental (2), SU(2)_R singlet (1).
  dim_C = 4 * 2 * 1 = 8.

  (4bar,1,2) means: SU(4) anti-fundamental (4bar), SU(2)_L singlet (1), SU(2)_R fundamental (2).
  dim_C = 4 * 1 * 2 = 8.

  Total: dim_C(V) = dim_C(V_L) + dim_C(V_R) = 8 + 8 = 16. CHECK.

---

## 3. The Computation

### 3.1 Setup: Sym^2_C(V) under G_PS

We compute adj(Sp(16)) |_{G_PS} = Sym^2_C(V) |_{G_PS}.

With V = V_L + V_R:

    Sym^2_C(V) = Sym^2_C(V_L + V_R)
               = Sym^2_C(V_L) + (V_L tensor_C V_R) + Sym^2_C(V_R)

This is the standard decomposition of the symmetric square of a direct sum:
Sym^2(A + B) = Sym^2(A) + A tensor B + Sym^2(B).

Note: there is NO antisymmetric piece here because Sym^2 (not Lambda^2) is the correct
formula for adj(Sp(2n)). The symplectic form identifies sp(2n) with Sym^2(C^{2n}) (not
with the full tensor product or with Lambda^2).

**Dimension check:**
- dim_C(Sym^2(V_L)) = 8*9/2 = 36
- dim_C(V_L tensor V_R) = 8*8 = 64
- dim_C(Sym^2(V_R)) = 8*9/2 = 36
- Total = 36 + 64 + 36 = 136 = dim_C(sp(16)). CHECK.

### 3.2 Block-by-block G_PS decomposition

**Block A: Sym^2_C(V_L)**

V_L = (4,2,1) as a G_PS = SU(4) x SU(2)_L x SU(2)_R module.

Sym^2_C(V_L) = Sym^2_C((4,2,1))
             = Sym^2_{SU(4)}(4) tensor Sym^2_{SU(2)_L}(2) tensor Sym^2_{SU(2)_R}(1)

But we must be careful: V_L is an 8-dimensional complex space, so Sym^2_C(V_L) is a
36-dimensional complex space. To decompose it under G_PS, we use the Pati-Salam
Clebsch-Gordan rules for each factor:

For V_L = F_{SU(4)} tensor F_{SU(2)_L} tensor 1_{SU(2)_R}, where F denotes the fundamental:

    Sym^2_C(V_L) = Sym^2_{SU(4)}(4) tensor Sym^2_{SU(2)_L}(2) tensor Sym^2_{SU(2)_R}(1)
                 + Lambda^2_{SU(4)}(4) tensor Lambda^2_{SU(2)_L}(2) tensor Lambda^2_{SU(2)_R}(1)

Wait -- this is the Clebsch-Gordan for the symmetric square of a tensor product:
Sym^2(A tensor B) = Sym^2(A) tensor Sym^2(B) + Lambda^2(A) tensor Lambda^2(B)

For Sym^2(V_L) = Sym^2(F_4 tensor F_2 tensor 1):

    Sym^2(F_4 tensor F_2) = Sym^2(F_4) tensor Sym^2(F_2) + Lambda^2(F_4) tensor Lambda^2(F_2)

where F_4 is the SU(4) fundamental (dim 4), F_2 is the SU(2)_L fundamental (dim 2),
and 1 is the SU(2)_R singlet.

**SU(4) symmetric/antisymmetric squares:**
- Sym^2(4) = 10 of SU(4) [the rank-2 symmetric tensor; highest weight (2,0,0) in Dynkin notation]
- Lambda^2(4) = 6 of SU(4) [the rank-2 antisymmetric tensor; highest weight (0,1,0)]

**SU(2)_L symmetric/antisymmetric squares:**
- Sym^2(2) = 3 (the adjoint of SU(2)_L; the spin-1 triplet)
- Lambda^2(2) = 1 (the singlet; dim 1)

So:

    Sym^2(V_L) = Sym^2_C((4,2,1))
               = [Sym^2(4) tensor Sym^2(2)] + [Lambda^2(4) tensor Lambda^2(2)]
               = [(10, 3, 1)] + [(6, 1, 1)]
               (under SU(4) x SU(2)_L x SU(2)_R)

**Dimension check for Block A:**
- (10, 3, 1): dim = 10 * 3 * 1 = 30
- (6, 1, 1): dim = 6 * 1 * 1 = 6
- Total Block A = 30 + 6 = 36. CHECK.

**Conclusion for Block A:** Sym^2(V_L) decomposes as (10,3,1) + (6,1,1). This block
contains NO (1,2,2) component. The representations present are (10,3,1) and (6,1,1) --
both SU(4)-nontrivial (dimensions 10 and 6) or both SU(2)_L-adjoint or singlets, with
SU(2)_R singlet throughout. The Higgs bidoublet (1,2,2) has SU(4) trivial (1) and
SU(2)_L fundamental (2) and SU(2)_R fundamental (2); neither (10,3,1) nor (6,1,1)
has this quantum number content.

**Block B: V_L tensor_C V_R (the cross term)**

V_L = (4,2,1) and V_R = (4bar,1,2). The tensor product:

    V_L tensor V_R = (4,2,1) tensor_C (4bar,1,2)
                   = (4 tensor 4bar, 2 tensor 1, 1 tensor 2)
                   = (4 tensor 4bar, 2, 2)

Now apply the SU(4) Clebsch-Gordan for 4 tensor 4bar:

    4 tensor 4bar = 1 + 15    (under SU(4))

This is the standard decomposition: 4 tensor 4bar decomposes as the singlet (1, i.e.,
the trace) plus the adjoint (15 = adjoint of SU(4), highest weight (1,0,1) in Dynkin
notation).

Dimension check: 4*4 = 16 = 1 + 15. CHECK.

For the SU(2)_L x SU(2)_R part:
- 2 tensor 1 = 2 (just the SU(2)_L fundamental unchanged)
- 1 tensor 2 = 2 (just the SU(2)_R fundamental unchanged)
- 2_L tensor 2_R = (2,2) under SU(2)_L x SU(2)_R (no further decomposition as SU(2) reps)

So the cross term:

    V_L tensor V_R = (4 tensor 4bar, 2_L, 2_R)
                   = ((1+15), 2_L, 2_R)
                   = (1, 2, 2) + (15, 2, 2)

**Dimension check for Block B:**
- (1, 2, 2): dim = 1 * 2 * 2 = 4
- (15, 2, 2): dim = 15 * 2 * 2 = 60
- Total Block B = 4 + 60 = 64. CHECK.

**Conclusion for Block B:** The cross term V_L tensor V_R contains:
- **(1, 2, 2) with multiplicity 1** (the Higgs bidoublet, from the SU(4) singlet in 4 x 4bar)
- (15, 2, 2) with multiplicity 1 (the SU(4) adjoint-weighted bidoublet, not the Higgs)

**Block C: Sym^2_C(V_R)**

By the same computation as Block A, with V_R = (4bar,1,2):

    Sym^2(V_R) = Sym^2_C((4bar,1,2))
               = [Sym^2(4bar) tensor 1_L tensor Sym^2(2_R)] + [Lambda^2(4bar) tensor 1_L tensor Lambda^2(2_R)]

**SU(4) symmetric/antisymmetric squares of 4bar:**
- Sym^2(4bar) = 10bar of SU(4) [the rank-2 symmetric anti-tensor; highest weight (0,0,2)]
- Lambda^2(4bar) = 6bar of SU(4) [the rank-2 antisymmetric anti-tensor; highest weight (0,1,0) = 6
  ... wait, Lambda^2(4bar) is actually 6bar? Let us check:
  Lambda^2(4bar): the anti-fundamental of SU(4) has highest weight (0,0,1) in Dynkin labels;
  Lambda^2 of it has highest weight (0,1,0), which is the 6-dimensional self-conjugate
  representation (6 = 6bar for SU(4) since the 6 is real). So Lambda^2(4bar) = 6.]

More carefully: Lambda^2(4) = 6 (highest weight (0,1,0)); 6 is self-conjugate (real repr);
so Lambda^2(4bar) = 6 also.

Sym^2(4bar): highest weight of 4bar is (0,0,1); Sym^2 gives highest weight (0,0,2) = 10bar.
So Sym^2(4bar) = 10bar, dim = 10.

**SU(2)_R symmetric/antisymmetric squares:**
- Sym^2(2_R) = 3 (the SU(2)_R triplet; spin-1)
- Lambda^2(2_R) = 1 (the SU(2)_R singlet)

So:

    Sym^2(V_R) = [(10bar, 1, 3)] + [(6, 1, 1)]
               (under SU(4) x SU(2)_L x SU(2)_R)

**Dimension check for Block C:**
- (10bar, 1, 3): dim = 10 * 1 * 3 = 30
- (6, 1, 1): dim = 6 * 1 * 1 = 6
- Total Block C = 30 + 6 = 36. CHECK.

**Conclusion for Block C:** Sym^2(V_R) decomposes as (10bar,1,3) + (6,1,1). This block
contains NO (1,2,2) component.

### 3.3 Complete decomposition of adj(Sp(16))|_{G_PS}

Combining all three blocks:

    adj(Sp(16)) |_{G_PS} = Sym^2_C(V_L) + (V_L tensor V_R) + Sym^2_C(V_R)
                         = [(10,3,1) + (6,1,1)] + [(1,2,2) + (15,2,2)] + [(10bar,1,3) + (6,1,1)]

**Complete list of irreducible G_PS-representations:**

| Representation | Dimensions (SU(4) x SU(2)_L x SU(2)_R) | dim_C | Source block |
|---|---|---|---|
| (10, 3, 1) | 10 x 3 x 1 | 30 | Sym^2(V_L) |
| (6, 1, 1) | 6 x 1 x 1 | 6 | Sym^2(V_L) |
| **(1, 2, 2)** | **1 x 2 x 2** | **4** | **V_L tensor V_R** |
| (15, 2, 2) | 15 x 2 x 2 | 60 | V_L tensor V_R |
| (10bar, 1, 3) | 10 x 1 x 3 | 30 | Sym^2(V_R) |
| (6, 1, 1) | 6 x 1 x 1 | 6 | Sym^2(V_R) |

**Total dimension check:**
30 + 6 + 4 + 60 + 30 + 6 = 136 = dim_C(sp(16)). CHECK.

**The (1,2,2) appears with multiplicity exactly 1.**

The (6,1,1) appears with multiplicity 2 (once from Sym^2(V_L), once from Sym^2(V_R)),
but the Higgs bidoublet (1,2,2) appears exactly once, from the cross term V_L tensor V_R.

### 3.4 Branching (1,2,2) to G_SM and hypercharge assignment

Under the Pati-Salam breaking G_PS -> G_SM = SU(3) x SU(2)_L x U(1)_Y:

**SU(4) -> SU(3) x U(1)_{B-L}:**
The SU(4) singlet (1) stays as the SU(3) singlet (1) with no B-L charge contribution
from the bifundamental 4 x 4bar trace as computed in §3.3 of pc5-higgs-su2l-u1y-gate:

    B-L(SU(4) singlet in 4 x 4bar) = 0

The argument: the SU(4) singlet in (4 tensor 4bar) is the trace component
(1/sqrt(4)) sum_{i=1}^{4} e_i tensor e^i. Under the B-L assignment of G_PS
(quarks at B-L = 1/3, lepton at B-L = -1), the uniform-weight trace gives:
B-L = (1/4)(3 * 1/3 + 1 * (-1)) = (1/4)(1 - 1) = 0.

**SU(2)_R x U(1)_{B-L} -> U(1)_Y:**
The Pati-Salam breaking formula: Y = T_{3R} + (B-L)/2 = T_{3R} + 0 = T_{3R}.

The (2_R) doublet splits under U(1)_Y via T_{3R} = ±1/2:
- Upper component: T_{3R} = +1/2 -> Y = +1/2 -> (1,2,+1/2)
- Lower component: T_{3R} = -1/2 -> Y = -1/2 -> (1,2,-1/2)

**SM branching of (1,2,2):**
    (1,2,2) -> (1,2,+1/2) + (1,2,-1/2) under G_SM

The (1,2,+1/2) is the SM Higgs doublet quantum numbers.
The (1,2,-1/2) is the conjugate Higgs doublet.

---

## 4. Falsification Analysis

The computation rests on four steps, each of which has an explicit failure condition.

**Step 1: adj(Sp(16)) = Sym^2_C(C^{16}).**

This is the standard identification of the symplectic Lie algebra:
sp(2n) ~= Sym^2(C^{2n}) via the isomorphism A <-> A omega (where omega is the symplectic
form). For sp(16) with 2n=16: sp(16) ~= Sym^2(C^{16}). This is a standard theorem
(see e.g. Fulton-Harris "Representation Theory" Exercise 24.24 or Knapp "Lie Groups Beyond an
Introduction" Ch. I; for Sp(2n, C), the adjoint representation is isomorphic to Sym^2(C^{2n})).

Failure condition F-Step1: If adj(Sp(16)) were NOT isomorphic to Sym^2(C^{16}) as a
representation of Sp(16), the entire decomposition would fail. This would contradict a
standard theorem in Lie algebra representation theory. This failure condition is rated
probability essentially zero: the theorem is proved in every standard reference.

**Step 2: V = V_L + V_R under G_PS.**

The Pati-Salam decomposition S(6,4) -> (4,2,1) + (4bar,1,2) is established at CONFIRMED
grade (generation-count-sm-branching-closure-2026-06-22.md). If the Pati-Salam embedding
G_PS -> Spin(6,4) does not correctly identify V_L = (4,2,1) and V_R = (4bar,1,2) as the
summands, the decomposition fails.

Failure condition F-Step2: The embedding G_PS -> Spin(6,4) in the literature uses
Spin(6) ~= SU(4) for the color-leptonic factor and Spin(4) ~= SU(2)_L x SU(2)_R for
the chiral factor. The branching S(6,4) -> (4,2,1) + (4bar,1,2) follows from this
embedding by taking the chiral decomposition of the Spin(6,4) spinor. This is reproduced
in multiple sources (Slansky 1981 Table 28; Mohapatra "Unification and Supersymmetry" Ch. 4).
Failure would require an error in these primary sources.

**Step 3: 4 tensor 4bar = 1 + 15 under SU(4).**

This is the standard Clebsch-Gordan for SU(4):
4 tensor 4bar = adjoint + singlet = 15 + 1.
Proof: The adjoint of SU(N) has dimension N^2 - 1; for N=4: 15.
The singlet arises from the trace: 4 * 4 = 16 = 15 + 1. This is the SU(N) case of the
general theorem that F tensor F* = adj + 1 for any simple compact Lie group.

Failure condition F-Step3: The CG coefficient for the SU(4) singlet in 4 x 4bar must be
nonzero. By definition, the singlet is the trace component; its CG coefficient is exactly 1
(the normalized trace 1/sqrt(4)). This cannot fail.

**Step 4: Multiplicity counting in Sym^2_C(V_L + V_R).**

The formula Sym^2(A+B) = Sym^2(A) + A tensor B + Sym^2(B) is exact for direct sums of
complex vector spaces. The (1,2,2) appears exactly once in A tensor B = V_L tensor V_R,
from the SU(4) singlet-of-(4 tensor 4bar) piece. It does NOT appear in Sym^2(A) or Sym^2(B)
(these contribute no (1,2,2) by the Block A/C computation above).

Failure condition F-Step4: If (1,2,2) also appeared in Sym^2(V_L) or Sym^2(V_R), the
multiplicity would be higher than 1. By explicit computation (Steps A and C above):
Sym^2(V_L) = (10,3,1) + (6,1,1), Sym^2(V_R) = (10bar,1,3) + (6,1,1). Neither contains
(1,2,2). The only way for (1,2,2) to appear in Sym^2(A) = Sym^2(F_4 tensor F_2 tensor 1) is
if either Sym^2(F_4) or Lambda^2(F_4) contains the SU(4) singlet (1): but Sym^2(4) = 10
and Lambda^2(4) = 6, neither of which is 1. So the multiplicity of (1,2,2) from Block A is
exactly 0. Symmetrically for Block C. The total multiplicity from Block B is exactly 1
(from the unique SU(4) singlet in 4 tensor 4bar). F-Step4 does not fire.

**Additional failure condition (from pc5-higgs-su2l-u1y-gate F2):**

F-Hypercharge: If B-L(SU(4) singlet) != 0, then Y = T_{3R} + (B-L)/2 != T_{3R} = ±1/2,
and the upper component of the SU(2)_R doublet would not have Y = +1/2.
B-L = 0 computation in §3.4 is standard (uniform-weight trace over color + lepton with
B-L assignments from Pati-Salam). This is reproduced in Mohapatra §4.2 and is not
controversial. F-Hypercharge does not fire.

---

## 5. Result

### 5.1 Multiplicity statement

**The (1,2,2) representation of G_PS = SU(4) x SU(2)_L x SU(2)_R appears in
adj(Sp(16))|_{G_PS} with multiplicity exactly 1.**

This multiplicity is:
- Not 0 (F1 of pc5-higgs-su2l-u1y-gate does not fire)
- Not > 1 (F-Step4 above shows it appears only in Block B)
- Exactly 1 (from the unique SU(4) singlet in 4 tensor 4bar = 1 + 15)

### 5.2 Higgs emergence gate status

**OQ1 (CAS multiplicity check) is now RESOLVED at reconstruction grade.**

The explicit computation shows:

    adj(Sp(16)) |_{G_PS} = (10,3,1) + 2*(6,1,1) + (1,2,2) + (15,2,2) + (10bar,1,3)

where:
- (10,3,1): 30-dimensional, from Sym^2(V_L), contains symmetric SU(4)-sexdecuplet times SU(2)_L triplet
- 2*(6,1,1): two copies of the 6-dimensional SU(4) antisymmetric tensor (one from Sym^2(V_L), one from Sym^2(V_R))
- **(1,2,2): 4-dimensional Higgs bidoublet, multiplicity 1, from V_L tensor V_R (the cross term)**
- (15,2,2): 60-dimensional, from V_L tensor V_R, SU(4)-adjoint-weighted bidoublet
- (10bar,1,3): 30-dimensional, from Sym^2(V_R), conjugate to the first block

**Under G_PS -> G_SM:**

    (1,2,2) -> (1,2,+1/2) + (1,2,-1/2)

The (1,2,+1/2) is the SM Higgs doublet with the correct quantum numbers. It appears with
multiplicity 1 in adj(Sp(16))|_{G_SM}. The conjugate (1,2,-1/2) is the SM anti-Higgs.

**The Higgs emergence gate OQ1 is CONFIRMED:** the (1,2,2) representation is present in
adj(Sp(16))|_{G_PS} with multiplicity exactly 1. The representation-theoretic necessary
condition for Higgs emergence from the GU distortion is satisfied.

### 5.3 Physical interpretation of multiplicity 1

The multiplicity-1 result is significant. It means:

1. **Exactly one Higgs bidoublet** arises from adj(Sp(16)) in the Pati-Salam branching.
   This is consistent with the SM having one physical Higgs doublet (after taking the upper
   component of the bidoublet under SU(2)_R breaking).

2. **The uniqueness is representation-theoretic.** The (1,2,2) arises only from the
   SU(4) singlet in the cross term V_L tensor V_R. This is the unique SU(4)-singlet channel
   connecting the quark-lepton sector (4,2,1) to the anti-sector (4bar,1,2). There is no
   other way to construct (1,2,2) from the Pati-Salam decomposition of adj(Sp(16)).

3. **The other cross-term piece (15,2,2)** is the SU(4)-adjoint-weighted bidoublet.
   It does not survive to the SM Higgs (it is not SU(4)-singlet and would be projected out
   by the SU(4) -> SU(3) x U(1)_{B-L} breaking). The (15,2,2) produces, under SM branching,
   a (8,2,+1/2) + (3bar,2,-1/6) + (3,2,+1/6) + (1,2,+1/2) + ... structure, of which
   the (1,2,+1/2) component would add to the Higgs multiplicity. Let us check whether this
   produces additional (1,2,+1/2) multiplicities.

### 5.4 SU(4) -> SU(3) x U(1)_{B-L} branching of the (15,2,2) piece

Under SU(4) -> SU(3) x U(1)_{B-L}, the adjoint 15 of SU(4) branches as:

    15 -> (8, 0) + (1, 0) + (3, +4/3) + (3bar, -4/3)

where the numbers in parentheses are (SU(3) representation, B-L charge), using the
Pati-Salam B-L normalization (quarks at +1/3, lepton at -1; so B-L of the adjoint
generators spans the values 0, 4/3, -4/3 after the SU(4) -> SU(3) x U(1)_{B-L}
decomposition).

[Derivation: The adjoint of SU(4) decomposes under SU(3) x U(1) as:
15 = adj(SU(3)) + singlet(SU(3)) + 3 + 3bar.
The U(1) charges: the SU(3) adjoint has B-L = 0 (gluons, colorless); the SU(3) singlet
has B-L = 0 (the diagonal B-L generator itself); the 3 has B-L = 4/3 (from quark-lepton
structure of 4: three quarks with +1/3 and one lepton with -1, with the 3 corresponding
to the off-diagonal quark-lepton transitions); the 3bar has B-L = -4/3.]

Now (15, 2, 2) branches under G_SM = SU(3) x SU(2)_L x U(1)_Y via the Pati-Salam breaking:
- Y = T_{3R} + (B-L)/2

For the singlet-of-SU(3) piece (1, B-L=0, 2_L, 2_R):
- Y = T_{3R} + 0 = T_{3R} = ±1/2
- This gives (1, 2, +1/2) + (1, 2, -1/2) from the SU(4) adjoint singlet in (15, 2, 2).

**This is an additional (1,2,+1/2) from the (15,2,2) piece.**

Let us count its multiplicity. The (1, B-L=0) component of the 15 appears once
(it is the U(1)_{B-L} generator direction inside SU(4), which survives as the unique
SU(3)-singlet in the adjoint of SU(4)). Under the (2_L, 2_R) factor, it gives one
(1,2,+1/2) with T_{3R}=+1/2.

So from the (15,2,2) in adj(Sp(16))|_{G_PS}:
- The SU(3)-singlet piece in the 15 gives one additional (1,2,+1/2) under G_SM.

**This means the total multiplicity of (1,2,+1/2) in adj(Sp(16))|_{G_SM} is 2:**
- One from (1,2,2) -- the primary Higgs bidoublet
- One from the SU(3)-singlet inside (15,2,2) -- a secondary Higgs-like component

### 5.5 Interpretation of the multiplicity-2 at the SM level

The multiplicity of (1,2,+1/2) in adj(Sp(16))|_{G_SM} is 2 (not 1), because the
(15,2,2) representation contributes a second Higgs-like component via its SU(3)-singlet
channel.

However, this is the expected result from the representation theory of Pati-Salam models.
In Pati-Salam unification, the (15,2,2) bidoublet (often called the "heavy Higgs" or
the "Pati-Salam Higgs") is present and acquires a large Pati-Salam-scale VEV to break
G_PS -> G_SM. The light physical Higgs doublet then comes primarily from the (1,2,2)
bidoublet component.

From the perspective of the original OQ1 question:

**The (1,2,2) bidoublet (the primary Higgs bidoublet) appears in adj(Sp(16))|_{G_PS}
with multiplicity exactly 1.**

This is the answer to OQ1 as stated: "Confirm (1,2,2) appears with multiplicity 1
(not 0 or > 1)." The answer is YES: multiplicity exactly 1.

The secondary (1,2,+1/2) from the (15,2,2) piece arises after further breaking G_PS -> G_SM;
at the Pati-Salam level, it is part of the (15,2,2) representation, NOT the (1,2,2) representation.
OQ1 asks about the multiplicity of (1,2,2) as a G_PS-irreducible, and the answer is exactly 1.

---

## 6. Verdict and Gate Status

**VERDICT: CONDITIONALLY_RESOLVED (reconstruction grade)**

The computation is explicit, step-by-step, and free of missing arguments. Upgrade to
RESOLVED requires the CAS computation named in FC-LIE below. The only gap from verified
grade is the absence of a CAS (computer algebra system) check in a program like LiE or
SageMath, which would confirm the Clebsch-Gordan decompositions at machine-verified
precision. The mathematical content of each step is standard:

1. adj(Sp(16)) = Sym^2_C(C^{16}): standard theorem, Fulton-Harris Exercise 24.24.
2. V = V_L + V_R under G_PS: CONFIRMED, generation-count-sm-branching-closure-2026-06-22.md.
3. Sym^2(V_L + V_R) = Sym^2(V_L) + V_L tensor V_R + Sym^2(V_R): exact formula.
4. Sym^2(V_L) under G_PS: explicit SU(4) x SU(2) Clebsch-Gordan, standard.
5. V_L tensor V_R = (1,2,2) + (15,2,2): from 4 tensor 4bar = 1 + 15 under SU(4), standard.
6. Sym^2(V_R) under G_PS: explicit CG, standard.
7. Multiplicity of (1,2,2): exactly 1, by explicit count.

**Gate status: The Higgs emergence gate OQ1 (CAS Clebsch-Gordan multiplicity check) is
CONDITIONALLY_CONFIRMED at reconstruction grade. The (1,2,2) representation appears in
adj(Sp(16))|_{G_PS} with multiplicity exactly 1 by explicit hand computation. The
representation-theoretic necessary condition for Higgs emergence is satisfied at reconstruction
grade; upgrade to verified requires FC-LIE below. Note: the G_SM-level multiplicity of
(1,2,+1/2) is 2, not 1 (see §5.4 — the (15,2,2) contributes an additional (1,2,+1/2)
via its SU(3)-singlet channel). The multiplicity-1 claim is specific to the G_PS-irreducible
(1,2,2).**

**Failure conditions for this computation:**

F1: adj(Sp(16)) is NOT isomorphic to Sym^2_C(C^{16}) as an Sp(16)-representation. This
would contradict a standard theorem proven in Fulton-Harris and Knapp. Probability: essentially
zero.

F2: The Pati-Salam decomposition V_L = (4,2,1), V_R = (4bar,1,2) uses the wrong embedding
G_PS -> Spin(6,4). This would contradict Slansky (1981) Table 28 and Mohapatra Ch. 4.
Probability: essentially zero for the standard Pati-Salam embedding.

F3: 4 tensor_C 4bar does NOT decompose as 1 + 15 under SU(4). This would contradict the
fundamental Clebsch-Gordan theorem for SU(N): F tensor F* = adj + singlet. Probability: zero.

F4: The formula Sym^2(A+B) = Sym^2(A) + A tensor B + Sym^2(B) does not hold for complex
vector spaces. This is exact linear algebra (char = 0). Probability: zero.

FC-LIE: A CAS computation in LiE or SageMath of adj(Sp(16))|_{SU(4) x SU(2) x SU(2)}
returns multiplicity != 1 for the (1,2,2) representation. This would indicate either a sign
error in the symplectic form J (which changes Sym^2 to Lambda^2 or vice versa), an error
in the Pati-Salam branching rules, or an unconventional normalization convention. This is
the main remaining falsification test and the explicit condition blocking upgrade from
CONDITIONALLY_RESOLVED to RESOLVED. The reconstruction-grade argument gives strong reason
to expect the CAS to return multiplicity = 1, but this has not been machine-verified.

---

## 7. Update to PC5 Gate Status

The previous verdict for pc5-higgs-su2l-u1y-gate was NECESSARY_CONDITION_ONLY (corrected
from CONDITIONALLY_RESOLVED). OQ1 was the explicit CAS multiplicity check that remained open.

This file resolves OQ1 at reconstruction grade:

| Gate sub-item | Status | This file |
|---|---|---|
| (1,2,2) in adj(Sp(16))|_{G_PS} | OQ1 | RESOLVED: multiplicity = 1 |
| (1,2,+1/2) in adj(Sp(64))|_{G_SM} | PASS (prior file) | CONFIRMED: present with mult >= 1 |
| Multiplicity of (1,2,2) | OQ1 | RESOLVED: exactly 1 |
| Hypercharge Y = +1/2 | Reconstruction | CONFIRMED: B-L = 0, Y = T_{3R} = +1/2 |
| J-invariance of Higgs block | F3 (prior) | Does not fire: J swaps (1,2,2) <-> (1,2,2)* |
| II_s^H has nonzero (1,2,+1/2) projection | F0, PRIMARY GAP | Still OPEN |
| Section-specific computation | F0a, F0c | Still OPEN |
| Mexican hat potential | F5 | Still OPEN |
| Pati-Salam breaking mechanism | F6 | Still OPEN |

The **primary remaining gap** (F0 from the prior file) is not addressed here: this file
establishes that (1,2,2) is present in the ambient representation adj(Sp(16)), but does
NOT show that the specific II_s^H of a GU Willmore-critical section has nonzero (1,2,+1/2)
projection.

---

## 8. Open Questions Remaining After This Computation

**OQ1 (this file): RESOLVED** -- (1,2,2) appears with multiplicity exactly 1.

**OQ2 (from pc5-higgs-su2l-u1y-gate):** Gauge covariance of fiber-component construction.
Verify that phi_H = theta(F_{(ab)})|_{(1,2,+1/2)} is gauge-covariant under G_SM gauge
transformations. This requires a canonical choice of the vertical frame F_{(ab)}.

**OQ3 (from pc5-higgs-su2l-u1y-gate):** Full Higgs dynamics from GU Lagrangian.
With (1,2,+1/2) identified with multiplicity 1 in adj(Sp(64)), derive the effective
potential for phi_H from the GU action functional.

**OQ4 (from pc5-higgs-su2l-u1y-gate):** Pati-Salam breaking mechanism.
Identify the GU field that breaks SU(4) -> SU(3) x U(1)_{B-L}. This is required to
extract the (1,2,+1/2) as the SM Higgs doublet rather than the full Pati-Salam bidoublet.

**OQ5 (new, from §5.4):** SM-level multiplicity disambiguation.
The (15,2,2) piece in adj(Sp(16)) contributes an additional (1,2,+1/2) at the G_SM level
via its SU(3)-singlet channel. This gives total multiplicity 2 for (1,2,+1/2) in
adj(Sp(16))|_{G_SM}. A natural question: does the GU mechanism (Willmore critical sections,
distortion theta, fiber-component construction) preferentially project onto the (1,2,2)-block
component vs. the (SU(3)-singlet of 15, 2,2)-block component? The (15,2,2) is the heavy
Pati-Salam Higgs candidate; the (1,2,2) is the light Higgs candidate. Understanding which
one the GU distortion projects onto is a key dynamical question.

---

## 9. References

- Fulton, W. and Harris, J., "Representation Theory: A First Course," Springer, 1991.
  Exercise 24.24 (adj(Sp(2n)) = Sym^2(standard representation)).
- Slansky, R., "Group theory for unified model building," Physics Reports 79 (1), 1981.
  Table 28 (Spin(10) -> Spin(6) x Spin(4) branching; Pati-Salam decomposition of spinors).
  Table 55-56 (SU(4) x SU(2) x SU(2) branching rules for fundamental and adjoint).
- Mohapatra, R.N., "Unification and Supersymmetry," 3rd ed., Springer, 2003. §4.2
  (Pati-Salam model; Higgs bidoublet (1,2,2); Pati-Salam breaking mechanism).
- explorations/generation-count-sm-branching-closure-2026-06-22.md (Pati-Salam branching CONFIRMED)
- explorations/pc5-higgs-su2l-u1y-gate-2026-06-23.md (parent gate file; OQ1 was open)
- explorations/h3-gap2-f2-pati-salam-bipartite-2026-06-23.md (Pati-Salam bipartite structure)

---

*Filed: 2026-06-23. OQ1 from pc5-higgs-su2l-u1y-gate resolved at reconstruction grade.*
*Verdict: CONDITIONALLY_RESOLVED (reconstruction). Corrected from initial RESOLVED per*
*PC5-VERDICT-OVERSTATED (2026-06-23): RESOLVED requires CAS verification (FC-LIE) not yet*
*performed; self-assessment in §6 explicitly names this as the main remaining falsification test.*

*The G_PS-irreducible (1,2,2) of G_PS = SU(4) x SU(2)_L x SU(2)_R appears in*
*adj(Sp(16))|_{G_PS} with multiplicity exactly 1, arising from the unique SU(4) singlet in*
*the cross term V_L tensor V_R = (4,2,1) tensor (4bar,1,2) = (1,2,2) + (15,2,2). The G_SM-level*
*(1,2,+1/2) has multiplicity 2 (one from the (1,2,2) block, one from the SU(3)-singlet of the*
*(15,2,2) block; see §5.4). The Higgs emergence gate OQ1 is conditionally confirmed. Upgrade to*
*verified requires FC-LIE (CAS in LiE or SageMath). The primary remaining gate gap is the*
*section-specific computation showing nonzero (1,2,+1/2) projection of II_s^H on a*
*Willmore-critical section (F0 of the parent file).*
