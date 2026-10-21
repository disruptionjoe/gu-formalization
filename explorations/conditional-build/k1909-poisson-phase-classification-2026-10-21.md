---
title: "K1909: The Poisson collision semigroup is nonclassical at early times"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; no native GU identification, novelty, or optimal temporal boundary
scripts:
  - tests/channel-swings/k1909_poisson_phase_classification.py
  - tests/channel-swings/k1909_poisson_phase_classification_probe.py
---

# K1909: The Poisson collision semigroup is nonclassical at early times

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
result: global rational phase witness and finite-time Poisson separation
carrier: four-dimensional logical density matrices and arbitrary classical phase laws LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: ordinary complex conjugation, no native K/C identification
grading: fixed population labels; not source graded-IG or physical chirality
action_owner: repository-construction -- supplied finite channels and controlled dilations
target: conditional noise discrimination and specified bath resources MAP-TYPE=intertwiner
```


## 1. Question resolved

Reuse [K1903](k1903-quantum-dephasing-witness-2026-10-21.md)'s
`V=[(1,0),(0,1),(1,1)/sqrt(2),(1,i)/sqrt(2)]` and `C=V* V`.
[K1906](k1906-dephasing-divisibility-boundary-2026-10-21.md)'s collision
semigroup is the Schur channel with coefficient matrix

    F_jk(t)=exp[t(C_jk-1)],  t>=0.                         (1)

It is CPTP and CP-divisible, by the Poisson series of compositions of the
C channel. The individual collision's nonclassicality did not decide the
mixture. K1908's witness had a positive initial derivative and was inconclusive.
A different, exactly certified witness now proves (1) is outside EVERY
classical random-phase law for **0<t<1/55**. At t=1/110 its witness value is
strictly below -1/11000. This settles a nonempty early-time interval and
excludes any classical phase process realizing the entire semigroup. It does
not locate the sharp transition or classify every intermediate time.

## 2. Global witness, not a phase-grid claim

Let W be the following rational Hermitian matrix, displayed as 1000W:

    [ 630       152-159i   -463-258i   -319+417i
      152+159i  133        -339-8i      54-151i
     -463+258i -339+8i     1015        -213-266i
     -319-417i   54+151i   -213+266i    478 ].             (2)

Every row sums to zero. For arbitrary |z_j|=1, the statement is

    z*Wz >=0.                                           (3)

Here is a finite rational certificate of the GLOBAL inequality. Divide by
the irrelevant common phase so z4=1. On the dense chart excluding z_j=-1,
write z_j=(1+i x_j)/(1-i x_j), with real x=(x1,x2,x3). Define

    m=(x1,x2,x3,x1*x2,x1*x3,x2*x3,x1*x2*x3),
    D=(1+x1^2)(1+x2^2)(1+x3^2).

Direct polynomial expansion gives D z*Wz=m^T G m, where 500G is

    [1260 304 -926 -318 -516 810 562
      304 266 -678 318 -275 -16 -121
     -926 -678 2030 -535 516 16 414
     -318 318 -535 2134 -1240 -805 -532
     -516 -275 516 -1240 1438 -110 -302
      810 -16 16 -805 -110 940 834
      562 -121 414 -532 -302 834 956].                  (4)

The exact LDL pivots of G, in this order, are

    63/25, 30343/78750, 8399911/15171500,
    9654885327/4199955500,
    3449792493541/9654885327000,
    143465073981273/862448123385250,
    8953914989286151/71732536990636500.

All are strictly positive, so G is positive definite and (3) holds on the
chart; continuity supplies every omitted phase point. Averaging establishes
Tr(W E[zz*])>=0 for arbitrary continuous, correlated or discrete phase laws.
This is not positivity of W on all complex vectors. W is a separating
observable for the classical phase set.

A deterministic phase-grid/linear-program scout suggested the coefficients.
A sampled affine-range phase-law search was infeasible, which by itself was
inconclusive. Numerical Gram optimization reported precision loss; only the
rounded rational polynomial identity and all-positive exact pivots in (4)
are banked. No optimizer success flag or numerical eigenvalue enters the proof.

## 3. Uniform finite-time bound and observable consumer

Put A=C-J, with J the all-ones matrix. Exact algebra yields

    Tr(WJ)=0,
    Tr(WA)=1777/1000-159sqrt(2)/125 = -d,
    d>1/50,
    ||W||_F^2=424611/125000 <4.                          (5)

All Re(A_jk)<=0. The integral exponential remainder gives
`|exp(tA_jk)-1-tA_jk|<=t^2 |A_jk|^2/2`. Bounding each |W_jk| by
|Re W_jk|+|Im W_jk| gives the exact conservative coefficient

    B=891/250-451sqrt(2)/250 <11/10.

Thus

    Tr(WF(t)) <= -d t+B t^2
               < -t/50+(11/10)t^2.                    (6)

The rational inequalities in (5)-(6) follow by squaring positive rational
bounds on sqrt(2), not floating-point rounding. Equation (6) proves the
stated interval and margin. On the normalized equal-superposition input,
the output is F(t)/4. At t=1/110 the output W expectation is below -1/44000,
where every classical output has nonnegative expectation. Since ||W||<2,
its trace distance (half the trace norm) from every classical-phase output
is greater than **1/176000**. No optimal full-channel or diamond distance is
claimed. This one input does provide the corresponding lower bound on
half-diamond distance, since the latter maximizes over inputs.

## 4. Follow-through and explicit opposite regimes

The all-time classical *process* hypothesis is now excluded by its early
single-time marginal. This implication needs no assumptions about independent
increments. Conversely, K1908's explicit 81-history Fourier law still proves
classical endpoint laws for all

    t >= log(12)/(1-1/sqrt(2)).                           (7)

That established late-time result is reused, not newly recomputed. There is
no inconsistency: sufficiently noisy endpoints can be classical although
an entire semigroup cannot have a classical phase dilation. The intervening
times and any sharp crossing remain open. Nonclassicality of a collision
alone was insufficient; (2)-(6) are the missing discriminator.

For a constructive repair, replace the collision by
`C_eta=(1-eta)C+eta I4`. Since its off-diagonal absolute sum is
`5(1-eta)/sqrt(2)`, K1908's same finite Fourier construction supplies an
actual phase-jump distribution whenever `eta>=1-1/(5sqrt(2))`. Independent
Poisson jumps drawn from that distribution realize
`exp[t(C_eta-J)]` at ALL times, not just separate endpoint laws.
This is a sufficient noise threshold, not its minimum. For example eta=9/10
satisfies it strictly. The same W still excludes early times when
`eta<d/(d+282/125)`, since Tr(W I4)=282/125. There is an unresolved gap
between these sufficient regimes; no threshold is inferred from a failed
witness. A rank-one unit-phase collision is an additional exact all-time
classical control. Both controls prevent equating a complex generator or
Poisson terminology with nonclassicality.

## Review and reproducibility

Strongest overclaim: extending the short interval to all times, contradicted
by (7). Strongest counterconstruction: the explicit noisy phase-jump repair.
Weakest seam: conjugation/half-angle normalization; the separate probe uses
fraction-pair complex arithmetic and independent polynomial multiplication,
not the producer's SymPy expression. It also reconstructs exact LDL signs.
Unresolved defects within the stated certificate: none after these checks.

Run the two listed scripts with Python and SymPy available. The report stores
W, G and the exact margins. The proof remains readable without trusting its
Boolean summary or a phase grid.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT the stylized curvature-mass toy. SC-META-53 remains
UNCERTAIN about the unbounded-spectrum problem. None identifies the positive
Hilbert system, bath, controls or accessible algebra used here. LT-SM8,
LT-GR6b and AC-F1, the source register, physics ledger and canon are unchanged.
The full20 injection, separate K/C forms, domain and accessibility remain
independent construction debts. No GU recovery, physical bath identification,
external expert review, novelty or formal proof is claimed.

The analytic arguments carry the universal statements. Exact probes check
polynomial identities, finite matrices and rational inequalities; mutations
of inputs test those checks, while report/pin mutations only test reporting
and provenance. Numerical scouts do not certify a phase law or universal sign.
