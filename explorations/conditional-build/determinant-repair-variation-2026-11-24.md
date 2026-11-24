---
title: Determinant repair — moving variation, dual descent and density freedom
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2
tier: T2
expected_delta: Sharpen the existing lower-gradient survivor by full variation and domain requirements without constructing an action
actual_delta: Moving-section jets, two-sided variational descent and global density countercontrols accepted at scoped T2
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Determinant repair: what local cancellation does and does not buy

> **GU-COMPARATOR-ROUTING — scope before inference.** Conventional chirality,
> family indices and exact autonomous-sector comparisons bind only their named
> constructions. They do not decide the source's non-chiral total/effective
> 2+1 mechanism without its physical observation bridge. Read
> `lab/methods/source-native-comparator-routing.md` and its source pointers.

program_target: X-P1-P2
tier: T2
expected_delta: Full variation and dual-field requirements for the existing structural survivor
actual_delta: Moving-section jets, two-sided descent and global density controls; native physical ownership open

```gu-typed-objects
result: Moving determinant-jet identities, variational quotient conditions and global weight controls
carrier: Y=Met(X4), actual symmetric-metric vertical tangent; full complex Dirac S128 with independent scalar/one-form bars and unbarred fields LAYER=ambient+observed BRIDGE=literal-contraction CHIRALITY=S-FULL-DIRAC
pairing: trace-reversed vertical K with lambda=1/2; separately fixed component dual and named measure; auxiliary positive L2 only for norm comparison ON=declared_carrier
real_structure: complex structural identities; K95 reconstructed geometry, no K77 or positive physical-state transfer
grading: existing ambient spin labels and observed quotient; no integer family grade supplied
action_owner: N/A -- necessary variation identities for supplied bilinear operators, not a new action or selected Lagrangian
target: full observed-sector compatibility of the recorded determinant-gradient survivor MAP-TYPE=intertwiner
```

Base: `bcaf26a2068bc3dad0cfcf19e14ea11eb5da4673`. Targets X-P1-P2,
X-P2-P3, secondary X-P1-P2-P3. No row, class, source or canon verdict moves.

## 1. Source and scope

The [primary 2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf)
§9.3 treats the four fermionic variables as independent and displays a
candidate operator, with rivals left open. The repository's
[rendered extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
and SC-OP-04/05 retain that strength. SC-CHI-52 concerns effective low-mass
separation; it does not require exact off-shell autonomy. SC-GEO-55's
connection displacement is not automatically ordinary tangent torsion.
These source statements remain unchanged.

Reuse the [exterior/adjoint result](source-exterior-connection-2026-11-13.md)
and [full-parent compatibility](source-lower-term-compatibility-2026-11-13.md).
Their actual observation is q=(P_H,Gamma_Y,nu); its hidden one-form satisfies
Gamma_N z=0. Under their stated principal coefficients and normal-jet
prescription, the remaining SW leakage is -lambda z(H), H=t/2, where t_y=y
is the vertical Euler vector field. The supplied correction
V z=lambda i_(t/2) z cancels that leakage. Here lambda denotes the scalar
operator coefficient, not the vertical trace-reversal coefficient1/2.
This paper tests consequences of that existing structural rival. It does
not choose the source operator, its full density or its boundary condition.

## 2. Moving observation versus frozen ambient coordinates

Write b for the observing metric and y for the independent fiber metric.
On a fixed-signature component put

    f0(b,y)=1/2 log|det b| - 1/2 log|det y|,
    rho0=exp(f0),                    s_b(x)=(x,b_x).

In affine symmetric-matrix coordinates, with independent variations h,k of b
and v,w of y,

    D_b f0[h]= 1/2 tr(b^-1 h),
    D_y f0[v]=-1/2 tr(y^-1 v),
    D_bb² f0[h,k]=-1/2 tr(b^-1 h b^-1 k),
    D_yy² f0[v,w]= 1/2 tr(y^-1 v y^-1 w),
    D_by² f0=0.                                         (1)

Along y=b, f0=0 identically: D_diag f0=0 and D_diag² f0=0.
For rho0 the partial mixed Hessian is generally NONZERO,
D_by²rho0[h,v]=-rho0 tr(b^-1 h)tr(y^-1 v)/4, but the full
diagonal first and second derivatives still vanish. Freezing y and retaining
only D_b rho0 invents a spurious response for the moving-section weight.
More generally rho0(b,b)=1 to every order.

This implies equality of **a common integrand's** weighted/unweighted
section restriction and its derivatives, if all other ingredients are the
same. It does not equate two differently reconstructed operators or an
ambient fourteen-dimensional variational integral with an integral on X.
A density on Y is not automatically an integrable four-density after pullback;
a specified observation measure is required.

For the existing b-induced connection metric, the vertical pairing obeys

    K_y(t,v)=-tr(y^-1 v),    K_y(t,t)=-4,
    grad_(G_b) f0=t/2.                                  (2)

The horizontal derivative vanishes under the same b-induced lift. Thus the
ambient vector t/2 has zero primitive b derivative at FIXED y. Nevertheless,
its component along the moving section is b/2 and differentiates to h/2.
That is evaluation at a moving point, not a new epsilon or varpi response.

Let zeta= zeta_a dy^a + zeta_mu dx^mu in a fixed local spinor trivialization.
The correction evaluated on the section is

    (V zeta)|s_b = lambda/2 sum_a b^a zeta_a(x,b),
    delta_b(V zeta)|s_b[h]
      =lambda/2 [zeta_a h^a + b^a h^c partial_(y^c)zeta_a]|y=b.  (3)

Equation3 holds for a held ambient field; any moving field/frame has its
additional chain term. The symmetric-coordinate contraction counts off-diagonal
entries once in the chosen Sym² basis. It is neither gamma trace nor s* zeta.
There is no derivative of h here because V is zeroth-order and evaluated,
whereas varying the full s* zeta includes derivatives of the section.

For a supplied section density mu_b and held component pairing, the variation
of the already-existing scalar bilinear contribution
lambda/2 mu_b bar-nu b^a zeta_a(x,b) additionally contains

    (delta log mu_b) bar-nu b^a zeta_a
      + (h^c partial_c bar-nu) b^a zeta_a.                (4)

For mu_b=vol_b, delta log mu_b=tr(b^-1h)/2. If bars are density-valued,
that density belongs inside the barred variable instead; do not count it twice.
Spinor identifications, the rest of D, and the actual source measure have
separate derivatives. Equations3–4 compute a contribution, not GU's full
stress tensor. Nonzero contributions do not by themselves disprove equivalence.

## 3. Local cancellation fixes a jet, not a pairing or metric equation

For every smooth scalar profile F with F(0)=0 and F'(0)=1, the structural
weight f_F=F(f0), rho_F=exp(f_F) has

    f_F|s_b=0,       grad f_F|s_b=t/2,
    grad f_F=F'(f0)t/2.                                 (5)

All such weights preserve the SAME local SW cancellation and equal-one
section density. This classifies a profile subfamily, not all natural weights.
More generally f=f0+r with r and its full first jet zero on the graph has
that same local data. Higher normal jets are unconstrained by cancellation.
For profiles, at y=b and fixed y,

    D_b(grad f_F)[h]=F''(0) tr(b^-1h)t/4.                (6)

Along the moving diagonal, the F'' terms cancel between b and y variation;
the result remains h/2. Thus local closure plus equality on every section
cannot determine the ambient primitive metric response. They do not fix F''(0)
or a global adjoint/domain. Smooth profile comparisons are structural controls,
not proposed source actions; C membership (including its polynomial-jet clause)
is not inferred for any new profile.

**Variation of the full intertwining identity.** If a supplied compatible
family satisfies q_b D_b=d_b q_b for all b, then

    (delta q)D+q(delta D)=(delta d)q+d(delta q).           (7)

For a moving hidden field k_b with q_b k_b=0, differentiation also includes
q delta k=-(delta q)k. The derivative of q_bD_bk_b is consequently zero.
One must not use the nonzero V contribution in (3) with a frozen q or a
frozen hidden representative to declare the complete repaired family broken.
Equation7 is conditional on the SAME compatible normal-jet/domain family;
pointwise cancellation at just one b does not establish it.

## 4. Four independent fields: the stronger variational test

Let a supplied density-valued bilinear operator K act on a splitting
E=H⊕O, where q:E→O is the actual supplied quotient. After a supplied density/pairing identification of the independent barred
fields with dual rows, use the true dual splitting, and compact support or an explicit
boundary pairing. Write its blocks as K_HH,K_HO,K_OH,K_OO.
Source independence alone does not identify its barred observation with this
dual splitting; that bridge is a hypothesis. This is the operator INCLUDING
the density and pairing, not automatically
D, its time-normalized form, or a guessed Hermitian adjoint.

Variation with respect to the observed barred variable gives
K_OH h+K_OO o. Variation with respect to the observed unbarred variable gives
K_HO^! bar-h+K_OO^! bar-o, with formal differential dual !.
Hence exact autonomous observed equations for arbitrary independent hidden
and barred-hidden data require BOTH cross blocks to vanish:

    K_OH=0,                 K_HO=0.                     (8)

One-sided quotient closure alone tests only the first relevant block, and
only after the density-dual map identifies its output with O!. Under those
identifications K=[[A,B],[0,C]] supplies an immediate contrary control:
unbarred observation descends, but barred observation receives B! bar-h.
Setting bar-h=0 instead chooses an annihilator subspace; it is a different,
possibly consistent restriction and must be sourced/transported explicitly.
The transpose dual of a quotient is an injection, not another quotient.

This theorem does NOT conclude that the actual repaired GU operator has
B!=0. Its full density-dual K and barred observation have not been supplied.
It also does not require a total theory to have exact independent sectors:
SC-CHI-52's effective decoupling may retain controlled cross terms.

**Actual normal-kernel response of the added arrow.** On the stated metric
normal bundle N of dimension10, let J_N psi=(gamma_r psi)_r and
P_K=1-J_N Gamma_N/10 be the gamma-kernel projection. For H=t/2, H²=-1,

    Gamma_N P_K=0,
    i_H P_K(H^flat psi)=(1-1/10)H² psi=-9 psi/10.       (8a)

Thus the added lower arrow lambda i_H has rank128 on the hidden kernel.
Its metric-dual arrow on the independent barred equation has nonzero hidden
component lambda P_K(H^flat bar-nu), also rank128. This is an exact local
consequence of the supplied nondegenerate metric/spin pairing; it does not
identify the source's final density-dual or barred observation. In the repaired
unbarred equation the old leakage cancels this contribution. The old barred
operator must likewise be included before assessing its net cross block.
One cannot add the lower correction to one Euler equation while leaving its
dual variation unmodified in an independently varied bilinear.

As a positive control, if a supplied K is formally self-dual or anti-self-dual
on a common domain with the compatible orthogonal hidden/observed splitting,
vanishing of one cross block forces the other. That property has not been
established by the source's candidate matrix or by calling its stars adjoints.

A second mandatory chain is general: if barred density coordinates are
transported by bar-u'=rho_b bar-u, the change is invertible pointwise.
The two coordinate expressions agree only when their operator is the same
transported operator. Their primitive metric variations differ off shell by

    <E_bar-u', (delta_b rho_b) bar-u>,                    (9)

plus analogous terms for any other transported field. For rho_F(b,b)=1 the
diagonal derivative is zero: this scalar map adds no section-only metric
chain term. The generic nonzero term in (9) concerns ambient primitive b
variation at fixed y, or another nonconstant field map. This vanishes on the
appropriate matter shell, not generally for independent fields. It is a
field-coordinate identity, not a construction of an action. Multiplication
by rho does not supply the lower drift of a newly reconstructed adjoint.

For a first-order P with principal symbol defined by [P,a]=sigma_P(da),
its weighted formal dual is

    P^!_rho = rho^-1 P^! rho
             =P^!+sigma_(P^!)(df).                     (10)

It changes every relevant differentiated block, not only a displayed SW row.
The source four-field equations must therefore be tested together. Equations
8–10 give the next finite discriminator once K and the barred readout are
specified; they do not authorize building them.

## 5. The global weight test and its contrary control

The canonical determinant weight is not a bounded change of norm on the
entire metric bundle. Fix b and use y=e^s b. Then

    f0=-2s,        rho0=e^-2s.                           (11)

Scaling is an isometry of the vertical trace-reversed metric; its volume
element is scale invariant. The tautological horizontal density scales as
e^(2s), so the ambient metric density along this scale translation acquires
e^(2s), whereas rho0 times it is invariant. Localized bumps translated along
the scale coordinate give unbounded ratios of weighted to unweighted norms
in one direction and the inverse ratios in the other. This is a genuine
positive-measure L2 comparison, not positivity of the native Krein theory.

There IS always an isometry U:u→rho0^(1/2)u from L2(rho0 mu) to L2(mu).
What fails globally is treating the identity map as a bounded invertible
same-Hilbert-space equivalence. U transports graph domains and the operator;
for first-order P,

    U P U^-1=P-1/2 sigma_P(df0).                         (12)

Thus a pointwise density-coordinate substitution cannot preserve a fixed
closed domain or spectrum without checking the transformed operator/end data.
No Fredholm, physical spectrum or new index is inferred here.

**Do not overstate this as unavoidable.** F(s)=tanh(s) obeys the local
conditions in §3 and gives e^-1<rho_F<e globally. Hence weighted and
unweighted L2 norms ARE equivalent for this smooth profile control, while
the same section-local leakage cancellation survives. It is not source-selected
or certified as an action in C. For the SAME fixed differential expression P, bounded rho and inverse give
equivalent graph norms on a common domain (and the same maximal domain),
because both the u and Pu norms are equivalent. They do not by themselves
compare a CHANGED weighted-adjoint or conjugated expression: derivative
commutators and boundary prescriptions must then be checked. On any region with 0<c<=rho0<=C<infinity the original determinant
weight likewise gives equivalent L2 norms, without a conclusion about ends.

## 6. Material result and next discriminator

The local determinant-gradient survivor remains live in its declared category.
Its one-section closure neither fixes the global weight nor establishes full
four-field variational descent or a metric equation. The wave supplies:

1. Exact cancellation of the weight's moving-section derivatives, paired with
   the nonzero and separately typed operator/field variation.
2. A first-jet equivalence class with freely different ambient metric responses.
3. The two-cross-block test for independent barred/unbarred autonomy, with
   field-transport and formal-dual chain terms explicit.
4. A proved global norm change for the canonical determinant weight and a
   bounded-profile countercontrol preventing a false all-weight exclusion.

These are T2 compatibility requirements on structurally defined categories,
not a new theory or a class-C kill. The shortest additional discriminator is
the actual density-dual cross block K_HO and barred observation, before any
full Einstein variation or end-index calculation. If those are supplied and
nonzero, exact autonomous quotient interpretation fails in that category;
effective coupling or a sourced annihilator restriction remain separate.
If they vanish, metric response and graph/end-domain tests remain. Do not
build the missing action or choose a profile merely to make a test pass.

The Nov21 native-index packet and parked integer/mod3 bridge retain their
exact missing inputs; no integer is supplied by these local results.

## Reproduction

`tests/program-focus/determinant_repair_variation_probe.py` checks noncommuting
metric Hessians, moving-section cancellation, profile jet freedom, section
operator and measure chain rules, quotient/dual countercontrols, adjoint and
unitary-conjugation drift, and global norm controls. The proof above carries
the general statements; finite controls do not certify an unbuilt source
operator or analytic domain. Report and independent review live in
`lab/process/determinant-repair-variation.json` and
`lab/process/hostile-reviews/2026-11-24-determinant-repair-variation-review.md`.

Validation: 48 exact controls PASS. Independent T2 review accepted the stated
scope after three corrections; internal review is not external-expert
certification. No Lean result or class-C decision is asserted.
