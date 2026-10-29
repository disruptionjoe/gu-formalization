---
title: "K2220 Quantitative robust adapter exclusion"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit excluded factor neighborhood and transported neighborhoods; no universal nonlinear obstruction
scripts:
  - tests/channel-swings/k2220_robust_adapter_exclusion_probe.py
---

# K2220 Quantitative robust adapter exclusion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2220 Quantitative robust adapter exclusion
carrier: real normal Cl46 grade3/7 coefficients on complex32 spinor with both chiral16 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: alternating real-form reconstruction and coordinate matrix norms ON=declared_carrier
real_structure: inherited quaternionic bar and real grade coefficients
grading: fixed normal grade3 and grade7
action_owner: repository-construction -- fixed normalized coefficient descent
target: necessary ordered Euler and all-ten adapter system MAP-TYPE=intertwiner
```

## Result: an open exclusion beyond the Spin orbit

The [K2214](k2214-prescribed-adapter-fibers-2026-10-28.md) factor Y0 has an
explicit positive-radius neighborhood containing NO factor realized by real
nonsingular ports satisfying all ten original equations. The radius is
conservative, extremely small and claimed as a rigorous open-set certificate,
not an efficient search exclusion. It covers arbitrary nearby factors,
including factors outside the [K2217](k2217-spin-orbit-adapter-exclusion-2026-10-28.md)
Spin orbit. It does not exclude all different or isospectral factors.

Use the induced row-sum matrix norm with scalar norm |Re z|+|Im z|. Let
E(Y) be K2208's392-by120 real reconstruction matrix for the positive
chiral factor Y_plus. Let M0 be K2214's specified119-square minor, omitting
coordinate93, whose determinant modulo1000003 is992118. Define

    q=lcm denominators(M0), H=max(1,max |q M0_ij|),
    C=119! q H^118,
    g=||Ginv||, L=max(240,120g), Yb=||Y0_plus||+1,
    A0=33/7,
    Ka=2CL A0, A=2A0, B=120g A Yb,
    Kb=120g(Ka Yb+A0),
    r=(144/7)(A+B), k=(144/7)(Ka+Kb),
    Le=(1056Yb+11184)rk+528r²,
    e=15850252893220743860640/(27955676769824869*1225),
    rho=min(1,1/(2CL),e/(2Le)) >0.                  (1)

Every genuine full factor with ||Y_plus-Y0_plus||<=rho is excluded.
The exact q,H,g,Yb and resulting rational rho are computed from the actual
matrices in the [certificate](../../lab/process/k2220-robust-adapter-exclusion.json).
No floating singular-value estimate or large rational inverse is needed.

## 1. Reconstruction perturbation and normalization

The integer matrix qM0 has nonzero integer determinant. Its cofactors are
bounded by118! H^118. Hence the row-sum norm of M0^-1 is at most C.
Each Phi basis matrix is a signed complex permutation of norm1. Therefore

    ||E(Y)-E(Y0)|| <= L delta,
    delta=||Y_plus-Y0_plus||.                       (2)

The symmetric-part rows contribute at most240 delta; the imaginary
Ginv-reconstruction rows at most120g delta. Both real and imaginary
constraints remain active. If delta<=1/(2CL), the selected minor remains
invertible and its inverse norm is at most2C.

Every nonzero real kernel vector must have a93 nonzero: otherwise its
remaining119 coordinates vanish by that minor. Normalize a93=1. The known
reference is a0/35, with infinity norm33/7. Subtracting the old and new
selected equations, including the changing omitted column, yields

    ||a-a0/35||_inf <= 2CL A0 delta=Ka delta,
    ||a||_inf <= A.                                (3)

Nearby E(Y) may have rank120, in which case reconstruction is already
impossible. We do NOT assert persistence of a one-dimensional kernel.

For an actual real kernel vector set b=Ginv upper(Phi(a)Y); this is real
and obeys Phi(a)Y=Phi(b). For defining a real extension away from the kernel,
take the real part of that formula; no estimate is weakened. Then

    ||b||_inf<=B, ||b-b0/35||_inf<=Kb delta.         (4)

The reconstruction is w=(a+b)/14, u=epsilon(a-b)/30, v=I_N w, t=i u.
The bounds120 for the grade reconstruction imply that R=v+3t and barR=v-3t
have norms at most r and changes at most k delta. This is the SAME real
port reconstruction on both chiral halves, not a separately fitted inverse.

## 2. Ordered Euler obstruction persists

Preserve K2197's original order and define K(z)=sum eta_j gamma_j z gamma_j.
It has norm at most10. Put

    A_E=3K(barR²)+34barR²+36RbarR+8barR R-24R²,
    B_E=184R²+140RbarR+184barR R+194barR²
           +24K(barR R)+15K(barR²).

Every all-ten solution obeys the necessary contracted equation

    E_Euler=4 A_E Y-(5 B_E-A_E)=0.                  (5)

The monomial bounds give ||A_E||<=132r², ||B_E||<=1092r²,
||Delta A_E||<=264rk delta and ||Delta B_E||<=2184rk delta.
Thus ||Delta E_Euler||<=Le delta. The real00 coordinate of the ACTUAL
normalized reference residual equals the positive rational e in (1).
For delta<=rho it stays at least e/2>0, contradicting (5).
Nonsingularity ensures nonzero reconstruction; the selected minor ensures
normalization. A zero or singular candidate cannot evade the stated theorem.
No sufficiency of the Euler contraction is assumed: failure is enough.

## 3. Transported neighborhoods and exact limitations

For a genuine Spin rotor g, transport the neighborhood by Y -> gYg^-1.
Covariance transports the real grades, both halves and all ten rows. The
excluded set about Yg=gY0g^-1 contains the transported norm neighborhood

    ||g_plus^-1 (Y_plus-Yg_plus) g_plus|| <= rho.

An ordinary norm ball of radius rho/(||g_plus|| ||g_plus^-1||) is sufficient.
Spin(4,6) is noncompact; no uniform Euclidean thickness along the whole orbit
is asserted. Scaling ports does not change their factor and only multiplies
the ordered Euler residual quadratically. Arbitrary similarities remain
outside the geometric covariance claim.

## Verification and ceiling

The probe freshly constructs actual E(Y0), the119 minor, q/H, Ginv norm,
normalized Euler coordinate and explicit radius. It checks a genuine
imaginary factor perturbation in the real reconstruction equations and the
ordered polynomial, while making no assertion that perturbation solves the
system. Independent norm and cofactor controls catch lost imaginary parts
and the denominator factor; the minor and Euler faults change actual data
or equations. The continuum perturbation proof is written above; a finite
sample is not its substitute.

Source assertions, ledger0.263 and real-grade classification are unchanged.
No universal adapter exclusion, source GU falsification, efficient solver,
external-expert acceptance, proof-assistant certification or novelty follows.
Further candidates must leave these certified neighborhoods or change the
construction openly. The general nonlinear real nonsingular all-ten system
remains unresolved.
