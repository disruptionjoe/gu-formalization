---
title: 'Source low-VEV decoupling: primitive current and uniform readout requirement'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3; P1 fields/symmetry
tier: T2
expected_delta: Settle a source-to-test implication across the declared class and preserve source-compatible
  countercontrols
actual_delta: Small background does not force a small odd primitive vertex. The complete effective-NE-readout
  bound identifies the required asymptotic suppression; actual full-SM covariant one-form mixing survives.
  No physical rate or GU exclusion.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: SOURCE-RELEVANCE-APPLICABILITY
canon_verdict_change: none
class_covered: Source primitive u(64,64) connection variations on full K95 spinors; held source NE arrow
  and actual contraction; conditional physical readout maps with fixed auxiliary norms. No action, vacuum
  or fluctuation spectrum selected.
premises:
- 'SC-CHI-01/51/52 in lab/sources/source-claim-register.yaml: effective low-VEV/curvature split is source-constrained,
  not exact universal off-shell separation.'
- 'SC-GRP-02 and SC-GEO-55; source-prescription-current-2026-11-13.md: full-parent primitive variation,
  independent barred fields and nonzero NE arrow.'
- K95 pairing and ambient-correlated grade; physical fluctuation support, response maps and normalization
  remain repository premises.
source_bridge:
  status: conditional
  reason: The source requires effective decoupling; the primitive variation is source-authenticated. Its
    conversion to an observable response requires physical fluctuation support, inclusions, readouts and
    propagators, none supplied by a small VEV alone.
kill_condition: A source contradiction requires nondecoupling on required physical modes under independently
  established dynamics and domains. A nonzero primitive vertex alone closes only the proposed implication
  from small background to small normalized response.
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: Source applicability conditions with retained countercontrols
carrier: fullCl14 S128 and raw one-form/scalar carrier with actual observed contraction LAYER=ambient+observed BRIDGE=declared-source-variation-and-observation CHIRALITY=S-FULL-DIRAC
pairing: K95 nondegenerate indefinite Krein pairing; independent density-dual bars ON=declared_carrier
real_structure: K95 quaternionic reality; no transfer to source K77
grading: correlated ambient Omega and prescribed horizontal chi_H kept distinct
action_owner: repository-construction -- source primitive grammar retained; complete physical action and response unselected
target: actual q on one-form/scalar fields MAP-TYPE=contraction
```

program_target: X-P1-P2-P3
tier: T2
expected_delta: Settle source applicability across declared classes
actual_delta: Small background does not force a small odd primitive vertex. The complete effective-NE-readout bound identifies the required asymptotic suppression; actual full-SM covariant one-form mixing survives. No physical rate or GU exclusion.

# Primitive current at zero VEV: weak compatibility and the missing response suppression

Internal T2 result; evidence base `14778ad8a4308d2d88357bba8a81819cedbc3f40`. Root executed the accompanying probes; validation and independent reviews are recorded below.

## Result and source ceiling

The actual geometric weak current has compatible sector parity under the
surviving correlated ambient grading. It does **not** force plain horizontal
off-shell oddness or supply a complete physical V−A current by itself.
The source's full parent also admits ordinary bosonic connection variations
that exchange the correlated sectors. Their primitive current vertex is
nonzero at zero background VEV. Thus a small VEV controls the background
mixing coefficient, but does not by itself control the derivative of that
coefficient with respect to an independent fluctuation.

This is an explicit additional response burden for an interacting realization
of SC-CHI-01/04/51/52, not a source contradiction. Heavy or constrained modes,
small physical fluctuations, a physical current quotient or a small coupling
can suppress the response. None is proved or excluded here. The result does
not assert an observable cross section, a gauge-boson mass, or a new family.

## 1. Custody: what the source actually requires

- SC-CHI-01 conditions the proposed effective split on no VEV pulling the
  subfields of `varpi` significantly above zero. It supplies no numerical
  threshold and no assertion that all fluctuations vanish with the mean.
- SC-CHI-04 asserts effective low-gravity chirality after pullback/branching;
  SC-CHI-51 names a VEV in a Dirac/RS-like operator; SC-CHI-52 gives the
  curvature→mass→effective Weyl-decoupling chain. The stylized `R/4` coefficient
  is not a complete connection-current or gauge propagator.
- On the source primitive slice, `A=A0[g]+varpi`, `delta varpi=alpha`,
  `delta epsilon=delta g=0`. Source `varpi` spans `Omega¹(ad U(64,64))`.
  The authenticated NE response is

      delta_varpi(d_A)[xi tensor T] nu = xi tensor T nu.       (1)

  Four independent barred/unbarred fields let this NE bilinear be isolated
  by setting `zeta=bar-nu=0`. NW and SE currents cannot cancel it on that
  polarized test. Fixed invertible epsilon wrappers transport it.

These are reused November 13 facts, not new source discoveries. Metric/epsilon
chain rules cannot cancel an independently varied `varpi` coefficient.

The new comparison uses the reviewed metric-spin reconstruction and its
surviving `G=diag(Omega,-Omega)` on `(zeta,nu)`. `Omega²=1` and on its K95
pairing `Omega^sharp=-Omega`. Its actual quotient is
`G_o=diag(Omega,-Omega,-Omega)` on `(b,tau,nu)` or `(b,sigma,nu)`.
The unresolved eq9.16/§11.2 half-label collision means this is a typed
candidate grading, not an authenticated identification of all luminous slots.
K77 reality is not inferred from K95.

## 2. Exact current parity, with independent bars

Split a parent generator by the actual ambient involution:

    T_e=(T+Omega T Omega)/2,   T_o=(T-Omega T Omega)/2.

Thus `[T_e,Omega]=0` and `{T_o,Omega}=0`. Since `Omega^sharp=-Omega`,
conjugation by Omega preserves the parent Lie algebra `T^sharp=-T`; both
parts are genuine allowed parent directions, not merely complexified guesses.

For the exterior/codifferential reconstruction, Clifford contraction `Phi`
is Omega-odd and the form actions do not change spinor Omega. Its primitive
response consequently has the two parities

    {G,delta D[T_e]}=0,       [G,delta D[T_o]]=0.              (2)

This follows block by block: NW is `Phi(alpha wedge -)`, the cross arrows
carry `alpha` or its contracted/formal-dual response, and SE is zero.
If a rival adds SE, its actual parity must be tested; the isolated NE result
below needs no assumption about that extra block. Tangent metric-spin
variations can also change the form connection, whose spin parity is even.
No generic full-parent variation is asserted to preserve observation closure.

Let `B` be the specified nondegenerate density pairing, and represent an
independent barred row by `B(beta,-)`. This does **not** identify beta with
the unbarred field. The extended form/scalar pairing has `G^sharp=-G`.
For sector vectors `G beta=epsilon beta`, `G psi=delta psi`, and a response
`G V=p V G`, polarization gives

    (epsilon+p delta) B(beta,V psi)=0.                       (3)

Hence the Omega-even parent direction has same-sector current (`p=-1`);
the Omega-odd direction has opposite-sector current (`p=+1`). A field-space
odd operator and a same-sector bilinear are compatible because the density
pairing exchanges the two ambient halves. Independent bars do not justify
replacing this pairing by a positive same-half form.

### Geometric weak success

The actual normal geometric weak generator is a Spin bivector, so it commutes
with Omega. Its simultaneous form action also preserves spin Omega. The
already-owned Category-G observation intertwiner therefore carries its
same-sector current structure to the actual six-spinor carrier wherever the
corresponding barred observation is retained. At the isolated horizontal NE
vertex this statement needs only literal `b=P_H zeta`.

There is no implication to `pi_b G_o=chi_H pi_b`: the first receiver grade
is Omega. Thus the failed horizontal-grade demand is not a necessary
consequence of weak-current compatibility.

Here compatibility means this **sector parity of the actual current vertex**.
It does not prove that a fixed geometric weak transformation commutes with
the complete second-fundamental-form-dependent operator on a held background.
Geometric covariance and unbroken fixed-background symmetry remain different;
the parallel normal-center test can fail the latter without contradicting (2).

## 3. The full parent has an invertible mixing direction

Because Omega is a K95 skew-adjoint involution, its two eigenspaces are null
and pair nondegenerately. In an adapted complex basis, with `n=64`,

    Omega = [ I  0 ],      K = [ 0 I ],
            [ 0 -I ]          [ I 0 ]

and the full real Lie algebra is

    u(K) = { [ A  B ] : B†=-B, C†=-C },
             [ C -A†]

where A is arbitrary complex. The Omega-even part is `B=C=0`, real
dimension `2n²=8192`, isomorphic to `gl(n,C)` as a real Lie algebra. The
odd part is `A=0`, also real dimension8192. This is an algebraic parent
decomposition, not a count of physical gauge particles.

In particular

    T_o = i [0 I; I 0],
    T_o^sharp=-T_o,   {T_o,Omega}=0,   T_o²=-I.              (4)

This is an ordinary bosonic Lie-algebra-valued connection variation. “Odd”
means odd under the ambient spinor involution. It does not mean a Grassmann
odd field, a BRST ghost, or the odd generator of the proposed super-IG algebra.

Choose any nonzero horizontal covector xi. Equations (1) and (4) give a
primitive vertex with complex rank128 on the full scalar carrier, rank64
from either ambient half. The actual horizontal observation retains it:

    q_b delta D_NE[xi tensor T_o] nu = xi tensor T_o nu.     (5)

The right side is injective because xi is nonzero and `T_o^-1=-T_o`.
This is a written all-dimension rank proof, not a sampled rank assertion.
The one-form test row can detect it under the nondegenerate density pairing.
A further physical row/solution quotient may annihilate it; the theorem does
not assume that quotient is the full algebraic receiver.

At a metric-spin background with `varpi=0`, the operator may have the exact
ambient parity, while (5) is unchanged. More generally along backgrounds
`varpi_epsilon→0`, the primitive derivative is still (5). Therefore no estimate
`||delta_varpi D_NE[T_o]|| ≤ C ||varpi_epsilon||` with a fixed finite C can
hold in a fixed nondegenerate finite-dimensional norm on this vertex. This
norm statement is independent of any physical positive Hilbert structure.

In contrast, an actual fluctuation of amplitude `eta` contributes `eta`
times (5). A zero mean does not imply a large fluctuation, a small fluctuation,
or any particular propagator. No such conclusion is being drawn.

## 4. Charge-resolved chirality of the ambient half

Reuse the authenticated normal16 branching. In one sign convention the
correlated source spinor is

    R_+ = H_L tensor F  plus H_R tensor Fbar,
    R_- = H_L tensor Fbar plus H_R tensor F,

with `F=Q+d^c+u^c+L+e^c+n^c` and source `6Y` table

    (3,2,1), (3bar,1,2), (3bar,1,-4),
    (1,2,-3), (1,1,6), (1,1,0).

The representation-valued horizontal difference is `[F]-[Fbar]` on `R_+`,
its negative on `R_-`. Its dimension is zero, but the class is nonzero:
the only common SM irrep in F and Fbar is the sterile singlet. For example,
the right-handed charge-conjugate quark doublet is not a right-handed
same-charge quark doublet. Forgetting color and hypercharge loses this
distinction: both F and Fbar restrict to four weak doublets and eight weak
singlets. A weak-only dimension or horizontal trace test would miss it.

This is a kinematic success of the source's correlated representation and
the actual weak action. It supports neither a physical count nor the claim
that every six-spinor slot has already been assigned to a source family.
The K95 quaternionic conjugation preserving Omega is not a Majorana fixed
subspace; independent bars remain independent. Source 2+1/imposter provenance
is not replaced by repeated F copies.

## 5. The exact new response datum

For specified physical inclusion/solution and readout maps, the quantity to
control is schematically

    R_mix(epsilon) = L_dark(epsilon)
                    delta D[alpha_odd(epsilon)]
                    I_luminous(epsilon),                  (6)

with the actual density-dual row and any propagation factors included.
The small background VEV does not automatically bound (6), because it does
not bound the vertex derivative (5). A physical decoupling argument can
instead show small allowed alpha, a vanishing physical current image,
propagator suppression, or a small normalized coupling. Integrating out a
heavy sector changes the effective response and must be treated with that
actual inverse/domain; it is not excluded by (5).

This narrows the next source question: which physical response removes or
suppresses the Omega-odd parent directions in the low-gravity regime? The
existing scalar `R/4` mass toy controls a background coefficient and does
not answer that current question by itself. The required information is
smaller than an entire action, but it is still not source-selected here.

## 6. Novelty and refusal to over-credit

Reused: source primitive variation and independent-field polarization;
background-parallel does not mean derivative-parallel; normal charge tables;
Category-G weak transport; moving-projector bounds; the newly reviewed
metric-spin ambient-grade theorem.

New: the even/odd primitive-current split with the actual K95 sharp law and
independent density rows; an admitted invertible parent mixing direction
whose rank64-per-half vertex survives literal horizontal observation at zero
VEV; and the consequent explicit response-suppression datum. The classification
does not redo an odd-adapter search and does not impose exact parent-sector
invariance as a source requirement.

Sources/evidence: `lab/sources/source-claim-register.yaml` SC-CHI-01/03/04/51/52,
SC-FER-05/06/07, SC-OP-04/05, SC-GRP-02/03; section9 and section11–12 extraction;
November13 `source-prescription-current`, `source-joint-symmetry-current`,
`source-weak-action-transport`, `source-moving-repair`; current physics rows
RA-A2/A5/A6/A8 remain missing selection/physicality data. No ledger, source
adherence, class-C status or canon change is inferred.

## 7. Does block Lorentz plus SM neutrality remove the mixing directions?

**No, and two categories must be separated.** A Lorentz-scalar internal
generator has only a small sterile residual. A Lorentz-covariant connection
one-form can carry Omega-odd charged-support couplings as well.

### 7.1 Complete sharp-skew scalar-generator intersection

Reuse the November 13 full commutant theorem: every complex-linear
Lorentz-scalar, SM-neutral, Omega-odd endomorphism of S128 is supported on
the two normal sterile singlets. Its complex dimension is4 and maximum
rank8. This is already an exhaustive theorem, including higher Clifford
degrees, and is not newly counted here.

The additional source-parent test is `T^sharp=-T`. On the sterile carrier

    S_st = (H_L tensor C²) plus (H_R tensor C²),
    chi_N=diag(1,-1),

the actual K95 pairing has the type

    K_st = [ 0       I₂ tensor D ],
           [ I₂ tensor D       0 ],
    D=diag(d_+,d_-),  d_+,d_- nonzero real.                (7)

This is a neutral pairing, not a positive8 replacement. Its form follows
from `chi_H^sharp=-chi_H` and `chi_N^sharp=chi_N`: opposite horizontal
halves pair, while different normal chiralities do not. Compact SM
averaging makes its sterile-isotypic projector selfadjoint, so restriction
to that isotypic is nondegenerate. Horizontal Lorentz duality fixes the
two-component spin pairing; remaining normal-line phases may be normalized
to make the two coefficients real. Their actual signs need not be guessed:
the following theorem holds for either sign and any nonzero magnitudes.

Write the already-classified scalar endomorphism as

    T = diag(I₂ tensor A_L, I₂ tensor A_R),
    A_L=[0 b; c 0].

The parent sharp law is equivalent to

    A_R = -D^-1 A_L† D.                                  (8)

There are precisely **two complex parameters b,c, hence four real
parameters**. No further equation removes them in the source's full unitary
parent. The ranks are exactly0,4,8 according as zero, one or both of b,c
are nonzero. Each directed Omega-half map has rank0 or4; the corresponding
NE vertex and literal horizontal readout retain that rank for nonzero xi.
Thus even in this narrower scalar-generator category, SM neutrality and
the native sharp law do not force the entire connection into the Omega
centralizer.

This does not establish a physical sterile-neutrino or Majorana mass. It
classifies an allowed current generator on the source carrier. Requiring
compatibility with a separate selected quaternionic reality, a different
K77 branch, a preserved domain or an additional unbroken U1 changes the
intersection and must be stated. In particular the already-owned extra
`U1_X` condition removes even the sterile complex Hom; its presence is not
inferred from the name SM.

### 7.2 Covariance of the whole one-form is a larger category

Demanding that **each coefficient endomorphism** be a Lorentz scalar is
stronger than Lorentz covariance of the source field
`alpha in H* tensor u(64,64)`. On the actual K95 Clifford carrier, for real
X in H,

    alpha_lambda(X) = i lambda c_H(X),  lambda real,        (9)

is sharp-skew, Omega-odd, and commutes with the normal SM action. Under block
Lorentz it obeys the exact tensor equivariance

    alpha_lambda(LX) = rho(L) alpha_lambda(X) rho(L)^-1.

Thus (9) is a Lorentz-equivariant, SM-neutral one-form type. Individual
endomorphisms `i c_H(X)` transform as a horizontal vector; they are not
members of the scalar-generator commutant in §7.1. The source permits a
general parent-valued one-form, so excluding this tensor type would require
an additional restriction, not just Lorentz covariance.

The same witness is equivariant under endogenous graph Lorentz: the induced
normal spin action commutes with horizontal Clifford multiplication. This
particular tensor does not require an independently chosen compensation.

Its isolated NE response is `i lambda J_H nu`. The actual observation gives

    q delta D_NE[alpha_lambda] nu
       = (i lambda J_H nu, 4 i lambda nu, 0)

in `(b,tau,nu)` coordinates, or `(i lambda J_H nu,0,0)` in
`(b,sigma,nu)` coordinates. For nonzero lambda this has rank128, since
`Gamma_H J_H=4I`, and acts on charged as well as sterile normal spinors.
The barred density may detect it by the same independent-field argument.

Equation (9) is an admitted **field type**, not a chosen stationary VEV,
an added action, a derived mass or a fundamental Higgs scalar. A coefficient
may vanish in the physical regime, and its fluctuation/propagator/readout
still needs the test in (6). If an additional quaternionic-commuting
connection restriction is imposed, `i c_H(X)` requires a separate check:
the source's full U parent is not that smaller group.

**Consequence.** The proposed implication
“block Lorentz + SM symmetry forces all allowed parent directions into the Omega
centralizer” is false at the structural tensor level. Even the narrower
Lorentz-scalar generator reading retains a four-real-parameter sterile
current family. The actual source shrinkage is therefore a precise
conditional response burden, not an exclusion of low-VEV chiral sectors.

# Effective-port bound and complete observation channels for the primitive odd-parent vertex

Internal T2 follow-through; the effective-port and channel scope is retained.

## Exact hypotheses

1. In the declared K95 complex spinor carrier, use the neutral ambient splitting `S=S_+ plus S_-`, dim_C S_±=n=64. Choose paired bases so `Omega=diag(I,−I)` and `K=[0 I; I 0]`. Give both halves the same auxiliary standard Hermitian norm. This is a mathematical norm choice, not an assertion of positive physical states.
2. At each held background, I:L→S_+ and P:S_-→D are fixed complex-linear maps from/to finite-dimensional auxiliary Hermitian spaces. They may be arbitrary-rank and background-dependent, but are fixed before the primitive variation direction is chosen. Density-dual/readout/propagation maps, if supplied, must be included in P or I with their actual types. Opposite direction follows by swapping halves.
3. The variation support includes every `T_C=[0 C; C 0]` with `C†=−C` and `||C||≤1`. These are genuinely Omega-odd, Krein-skew directions of the source full parent. This is an admitted *primitive* variation family. It is not proved to be the set of unsuppressed physical excitations.
4. For the source application, P is the **effective row on the actual vertex image**, not an arbitrary full-receiver row. In `(b,tau,nu)` coordinates define `j_xi(u)=(P_H xi tensor u,c(xi)u,0)`. For a supplied complete receiver row L_rec set `P_eff=e L_rec j_xi|S_-`, with density-dual transport included. The exact bound uses `||P_eff||`; a bare factor `|e| ||xi||` is legitimate only for a separately specified product-norm port, not the full trace graph. No NW/SE polarization cancellation is allowed on this isolated current.

## Theorem

For every such pair of maps,

    max_{C†=−C, ||C||≤1} ||P C I|| = ||P|| ||I||.          (R1)

The same maximum is attained in the smaller set `C†=−C`, `C²=−I`, `||C||=1`. Thus the witnessing full parent generator may be taken invertible, with `T_C²=−I`, rather than singular or a disappearing direction.

**Proof.** The upper bound is submultiplicativity. If either map is zero equality is immediate. Otherwise finite dimension supplies unit x∈L and unit v∈S_- with `||I x||=||I||` and `||P v||=||P||`. Identify the paired halves as the same auxiliary C^n and put u=I x/||I||. Choose |lambda|=1 so `<u,lambda v>` is real. If u=lambda v, set H=I. Otherwise w=u−lambda v and

    H=I−2 w w†/(w†w).

Then H†=H, H²=I, and H u=lambda v, since `w†u=1−<u,lambda v>` and `w†w=2(1−<u,lambda v>)`. Put C=iH. It is anti-Hermitian, unitary, squares to−I, and

    ||P C I x||=||I|| ||P(i lambda v)||=||I|| ||P||.

In the neutral-pair basis, `T_C†K+K T_C=0` and `{T_C,Omega}=0`; with both off-diagonal blocks C its square is−I. Therefore the witness is in the admitted full parent. ∎

A single fixed generator can miss the response: for orthogonal u,v, the ports I=u and P=v† give `P(iI)I=0`. The maximizing direction depends on the two ports. This is why one full-rank vertex alone did not prove (R1).

## Exact consequences

**No common effective-port cancellation.** `P C I=0` for every admitted odd direction if and only if I=0 or P=0. This applies to effective linear ports of any rank, not only scalar adapters or orthogonal projectors. A nonzero complete receiver row may induce P_eff=0; that is a genuine channel-annihilating survivor, not excluded by (R1). The maps must be common to the variation family; tailoring a different readout to each tested generator changes the claim.

**Uniform asymptotic condition.** For backgrounds indexed by epsilon→0, define

    M(epsilon)=max_{C†=−C,||C||≤1} ||P_epsilon C I_epsilon||.

Then

    M(epsilon)→0 iff ||P_epsilon|| ||I_epsilon||→0.        (R2)

In particular if both norms remain bounded below by positive constants, low VEV alone cannot give uniform suppression over this full normalized variation family. If a physical coupling kappa_epsilon is included, the deciding product is `|kappa_epsilon| ||P_epsilon|| ||I_epsilon||`. If the physical allowed variation support is smaller, (R1)'s lower bound need not apply; the actual restricted-support supremum must be computed. These are genuine surviving suppression mechanisms, not exceptions hidden by the theorem.

**Coherent moving compensation cannot change the response.** For invertible coordinate/frame maps R_±, transport every leg:

    I'=R_+ I,    P'=P R_-^−1,    C'=R_- C R_+^−1.

Then `P'C'I'=PCI` exactly. K, adjoints, q, the variation support and its norm must be transported too. Using the transported auxiliary norms leaves (R1) unchanged. Comparing unrelated fixed-coordinate norms introduces their equivalence/conditioning constants; a singular coordinate rescaling does not demonstrate physical suppression. A physical background change or restriction of allowed variations is a different operation, which must be tested on its new response.

This is the connection to the moving-Clifford Lorentz compensation: a faithful re-expression of observation/current cannot erase the primitive response. That does not forbid a changed physical quotient or dynamics from suppressing it.

## Complete observation-channel classification

This is an independent algebraic completion of the isolated-port result. It uses the full source primitive one-form range and the full independent fermion inputs; it does not assume those are all physical modes.

Write a general receiver row in `(b,tau,nu)` coordinates as `(L_b,L_tau,L_nu)`. A horizontal alpha=xi_H tensor T has

    q delta D_NE nu = e (xi_H tensor Tnu,c_H(xi_H)Tnu,0),

so the effective row is `e (L_b j_H,xi + L_tau c_H(xi_H))`. In `(b,sigma=tau−Gamma_H b,nu)` coordinates the image is `(e xi_H tensor Tnu,0,0)`. Therefore sigma-only and nu-only rows are nonzero examples blind to every **horizontal** NE vertex.

A normal primitive alpha=n tensor T is also source-admitted and gives

    q delta D_NE nu = e (0,c_N(n)Tnu,0).

It detects the sigma-only row. Since the odd parent family contains an invertible T and c_N(n) is invertible for nonnull n, a row annihilating every normal NE response for all independent nu must have L_tau=0. The horizontal responses then force L_b=0. Thus across all source primitive covectors:

    NE-blind receiver rows are exactly the nu-output-only rows.

This classification is on the complete spinor input, equivalently after checking both Omega halves. A restricted physical inclusion can leave additional blind rows.

Finally the held weighted SW arrow has primitive response, up to its fixed nonzero sign/coefficient,

    delta D_SW[xi tensor T] zeta = g T zeta(xi#).

This follows from the same formal-codifferential response used in the current result; scalar density does not change the independently varied connection term. Its q output is `(0,0,g T zeta(xi#))`. Choose nonnull xi and independent zeta with arbitrary contracted value; an invertible odd T then detects every nonzero remaining L_nu. Consequently **no nonzero complete receiver row annihilates both independent cross-current families on all unrestricted source inputs**. This is not asserted for a physical solution subspace or a restricted surviving variation set.

The classification makes the source test concrete. Keeping only horizontal one-form variations leaves a trace-channel escape; retaining normal primitive directions removes it; retaining the independent SW response removes the final scalar-output escape. Each premise is explicit and independently testable. The general norm theorem is applied separately to the effective port in each retained channel, not to L_rec merely because L_rec is nonzero.

## Source-facing meaning and limits

The current wave establishes a source-admitted nonzero odd primitive vertex at zero VEV. This theorem strengthens that witness to a complete statement about effective ports: retaining two uniformly nonvanishing ports on the tested vertex image and every normalized odd-parent direction prevents uniform mixing suppression. The channel classification separately identifies which full-receiver rows can make that effective port vanish when particular input/variation legs are omitted.

SC-CHI-01/04/51/52 asks for effective low-gravity decoupling, not small response to every arbitrarily normalized off-shell variation. Therefore this is **not** a source contradiction. A physical realization must identify which condition changes: the available odd fluctuation directions/amplitudes, a physical coupling or propagator, or a response port. The theorem concerns the isolated polarized primitive vertex with fixed ports, not automatically the derivative of a complete effective observable. If a field-dependent solution/quotient/readout map contributes its own derivative or correlated terms, assemble that full response first; it need not factor as one P_eff C I. Nothing here assumes that all source primitive directions survive constraints as light physical modes. Nothing supplies a physical Hilbert space, a quantum covariance, a positive measure, a stationary vacuum, a global domain or an observable transition rate.

The next physical datum is consequently narrower than an entire source action: an asymptotic bound for the **actual allowed odd-parent response** after the stated physical reduction. The theorem prevents claiming that a small mean VEV, a coherently transported epsilon frame, or nonzero ports on the retained current channel alone supplies that bound. It does not dismiss a source-derived channel-annihilating physical quotient.

## Validation

The companion `source_small_vev_current_probe.py` (integrated readout controls) provides exact Gaussian-rational finite witnesses: coincident/orthogonal/complex-overlap ports; scaled and zero ports; a restricted-support countercontrol; correct Krein and axial signs; and complete moving-frame transport versus an intentionally omitted leg. It does not numerically optimize or claim to verify the dimension-independent theorem by sampling. Root executed the integrated probe serially; see the verification record.

## Evidence and verification

- [GEOMETER-VS-PHYSICS-OBJECTS.md](../../GEOMETER-VS-PHYSICS-OBJECTS.md)
- [source-claim-register.yaml](../../lab/sources/source-claim-register.yaml)
- [conditional-physics-ledger-v0.263.json](../../lab/process/conditional-physics-ledger-v0.263.json)
- [source-relevance-wave.json](../../lab/process/source-relevance-wave.json)
- [2026-11-24-source-relevance-wave-review.md](../../lab/process/hostile-reviews/2026-11-24-source-relevance-wave-review.md)

Exact probes validate the finite identities and contrary controls; the written arguments supply the quantified statements. Internal agent review is not external scientific certification. These results do not select a physical spectrum, a family count or an empirical prediction.
