---
title: "K1859: Optimizer tails close the fourth-order Gaussian Fisher law"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: uniform Gaussian envelope and polynomial first response for exact optimizers; sharp fourth-order Fisher value and inverse-budget asymptotics; second score-defect profile; no effective quartic error, second density profile or GU physics
---

# Optimizer tails close the fourth-order Gaussian Fisher law

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
result: optimizer Gaussian tail envelope, polynomial moment response, quartic Fisher value, second score defect and inverse-budget coefficient
carrier: real probability densities on R with raw second moment1 and fourth moment3-q LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial/Hermite degree only
action_owner: repository-construction -- scalar moment-constrained Fisher functional
target: unrestricted density variational problem MAP-TYPE=evaluation
```

## Result and preflight distinction

Use [K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md)'s
positive minimizer p_q (unique over all densities by
[K1851](k1851-fisher-parity-stability-2026-10-20.md)) with raw second moment1 and fourth moment3-q.
The unrestricted value satisfies

```
F(3-q)-1 = q²/6 + q³/4 + (11/108)q⁴ + o(q⁴),   q down to0.       (1)
```

For the **exact minimizers**, every fixed polynomial f also satisfies

```
E_(p_q) f = E_phi f - (q/24) E_phi[f H4] + o(q).                 (2)
```

Here phi is the standard Gaussian density and Hn are probabilists' Hermite
polynomials. K1857 proved the analogous bounded-observable response for all
leading-optimal competitors and exhibited competitors with diverging sixth
moment. We retain that counterexample. The new ingredient is a uniform
Gaussian envelope derived from the *actual optimizer's Euler equation*.
It is not transferred to generic near optimizers. There is no GU-physics,
novelty, external-expert or proof-assistant claim.

Preflight searched existing K1843, K1855 and K1857 by quartic value, polynomial
response and optimizer tail objects; those results explicitly leave this
transfer open. The variational lens proposes the actual quartic oscillator
rather than fitting a reference density. The functional-analysis lens demands
a uniform exterior comparison before expanding an unbounded residual. The
adversarial lens retains K1857's rare-tail contamination as a contrary control.
The cheapest successful route is multiplier secants, a maximum principle and
a two-dimensional score projection; it removes the need to prove a complete
second-order density expansion or run another numerical spectral solve.

## 1. Explicit uniform Gaussian envelope

K1843 supplies, with psi_q=sqrt(p_q)>0,

```
-4 psi_q'' +(a_q x²+b_q x⁴)psi_q = E_q psi_q,
b_q>0,   a_q=F(3-q)-2b_q(3-q),   E_q=2F(3-q)-b_q(3-q).     (3)
```

Put G(q)=F(3-q)-1. The exact dual gives, for every q' in(0,2),
`G(q')>=G(q)+b_q(q'-q)`. No differentiability of G is assumed.
For 0<q<=1/100 take q'=2q and use K1855's effective upper bound:

```
0<b_q <= [G(2q)-G(q)]/q
       <= (2q/3)(1+4q) < q.
```

The same bound gives F(3-q)<2. Hence `a_q>=1-6q>=1/2` and
`E_q<=2F(3-q)<=3` (the last inequality follows already from
G(q)<=q²(1+2q)/6). Let w(x)=exp(-x²/8). Direct differentiation gives

```
[-4 d²/dx²+a_q x²+b_q x⁴-E_q]w
 =[(a_q-1/4)x²+b_q x⁴+1-E_q]w >=0   for |x|>=3.          (4)
```

The exterior zeroth-order coefficient itself is positive:
`a_q x²+b_q x⁴-E_q >=x²/2-3>=3/2` there. Also
`||psi_q||_infinity² <=||psi_q||_2 ||psi_q'||_2=sqrt(F)/2<1`.
The Sobolev bound follows by integrating `(psi²)'` from both ends and applying
Cauchy-Schwarz; no pointwise differentiability estimate is imported.
Compare psi_q with `exp(9/8)w` on each exterior half-line. Their difference
has nonpositive boundary value at3 or-3. Its positive part belongs to H1
with zero boundary trace. Testing the distributional comparison against that
positive part, using compact cutoffs and then the form limit, yields
`4 integral |v'|² + integral(V-E)v²<=0`. Both terms are nonnegative, so v=0.
The form passage is valid since both psi_q and w are in the quartic form
domain for each q; positivity at infinity eliminates a boundary assumption
on their ratio. On |x|<=3 the same envelope follows from psi_q²<1.
Thus, uniformly for 0<q<=1/100,

```
p_q(x) <= exp(9/4) exp(-x²/4),       x in R.              (5)
```

All polynomial moments are uniformly bounded, and their tails vanish
uniformly. This is an exact-optimizer theorem; the multiplier equation is the
hypothesis absent from K1857's tail-contaminated near minimizers.

## 2. Released successor: polynomial linear response

Let h_q=sqrt(p_q/phi), r_q=(h_q-1)/q and u=-H4/48.
K1857 gives `r_q->u` strongly in H1(phi), in particular bounded in L2(phi).
For a polynomial f of degree m,

```
[E_(p_q)f-E_phi f]/q = 2 E_phi[f r_q]+q E_phi[f r_q²].    (6)
```

The first term tends to2 E_phi[f u] by L2 convergence, since f is in
L2(phi). The second vanishes, as follows. On |x|<=R it is bounded by
`C q(1+R^m)||r_q||²`. Outside that interval,
`r_q² phi <=2(p_q+phi)/q²`; (5) bounds its contribution by
`(C/q) integral_(|x|>R)(1+|x|^m)exp(-x²/4) dx`.
Choose `R²=16 log(1/q)` for q small. The latter is a polynomial in R times
O(q³), while the former is O(q[1+log(1/q)^(m/2)]). Both vanish. This proves
(2) without falsely inferring polynomial response from L1 alone.
Examples are `E X6=15-15q+o(q)`, `E X8=105-210q+o(q)` and
`E X10=945-3150q+o(q)`. Odd moments are zero by exact-optimizer uniqueness
and reflection; no such exact symmetry is assigned to generic near optimizers.

## 3. The fourth-order residual and the score-square that cannot be dropped

Retain K1855's exact certificate at t=q/6:

```
d=1+t x²/2,   g=x+t H3/d,
I=E_p(rho+g)² +1+q²/6+q³/18 +E_p R_t,
R_t=t³[r0+t x8/2]/d²,
r0=(x8-2x6+3x4)/2,
r1=(-x10+3x8-3x6)/2.                                    (7)
```

Uniformly for t>=0 small, `R_t=t³r0+t⁴r1` plus a remainder bounded
in absolute value by `C t⁵(1+|x|12)`. For example Taylor's theorem for
(1+z)^(-2) on z>=0 gives `|(1+z)^(-2)-1+2z|<=3z²` and
`|(1+z)^(-2)-1|<=2z`; use z=t x²/2. Equation(5) makes the integrated
remainder O(t⁵). Gaussian moments and(2) give

```
E_phi r0=42,  -(1/24)E_phi[r0 H4]=-183/2,  E_phi r1=-675/2,
E_(p_q) R_(q/6) =7q³/36 -197q⁴/288 +o(q⁴).              (8)
```

The negative fourth-order residual does not establish a negative coefficient
for F: the nonnegative score square contributes at this same order. Set
s_q=rho_q+g_(q/6). Weak integration by parts is valid against x and H3
because (5) gives their square integrability and finite Fisher bounds the
score. Cutoffs recover `E rho f=-E f'`. Expanding only the rational
coefficients with uniform polynomial remainder bounds yields

```
E_(p_q)[s_q x]/q² -> -1/4,
E_(p_q)[s_q H3]/q² -> -25/12.                            (9)
```

For the first identity use E xH3=-q and E x³H3->6:
`t(-q)-(t²/2)6=-q²/4`. For the second use
`E H3²=6-9q+o(q)`, `E x²H3²->42`, `E rho H3=0`, and
`E xH3=-q`; thus `-q+t(6-9q)-(t²/2)42=-25q²/12+o(q²)`.
The Gram matrix of (x,H3) in L2(p_q) tends to diag(1,6), by(2).
The elementary Hilbert-space projection inequality therefore gives

```
liminf E_(p_q) s_q²/q⁴
 >= (-1/4)²+(-25/12)²/6 =679/864.                       (10)
```

Combine(7)-(10):

```
liminf [F(3-q)-1-q²/6-q³/4]/q⁴
 >=679/864-197/288=11/108.                              (11)
```

This lower bound uses actual optimizer tails, not a formal interchange of
Taylor expansion and an uncontrolled integral, and does not assume that the
second density response exists.

## 4. Exact feasible upper trial matches the bound

Define polynomials

```
u=-H4/48,
v=-1/192-H2/48-H4/64+H6/216+H8/4608,
h_s=1+s u+s²v.
```

Normalize `phi h_s²` by N=E_phi h_s² and dilate to raw second moment1.
As in K1855, zeros of h_s do not obstruct H1 admissibility: the weak derivative
energy of |h_s|sqrt(phi) agrees with the signed square root. Set
`B=E_phi x²h_s²`, `C=E_phi x4h_s²`, `D=E_phi(h_s')²`.
These are exact degree-four polynomials:

```
N=1+s³/64+7991s⁴/331776,
B=1+13s³/576+93863s⁴/331776,
C=3-s-173s³/144+604679s⁴/110592,
D=s²/24+s³/16+919s⁴/6912.
```

The normalized variance is B/N. Gaussian integration by parts gives raw
Fisher `2-B/N+4D/N`; dilation multiplies this by B/N. Thus exactly

```
q(s)=3-CN/B²,
J_trial(s)=(B/N)(2-B/N+4D/N)-1.
```

Their rational expansions at0 are

```
q(s)=s+743s³/576-8921s⁴/2304+O(s⁵),
J_trial(s)=s²/6+s³/4+919s⁴/1728+O(s⁵).
```

Since q'(0)=1, the ordinary inverse-function theorem gives a positive s(q)
for every sufficiently small positive q, meeting both raw moments exactly.
Eliminating s gives
`J_trial(s(q))=q²/6+q³/4+(11/108)q⁴+O(q⁵)`.
This proves the matching limsup and hence(1). It asserts neither an effective
finite-q fourth-order error nor equality of the nodal trial and optimizer.

## 5. Released successor: the second score-defect profile

The matching bounds also determine the part of the score not already fixed
by K1855's rational score. Equations(1), (7) and (8) force
`E_(p_q) s_q²/q⁴ ->679/864`, so the projection inequality(10) saturates.
Let

```
L(x)=-x/4-25H3(x)/72.
```

Its coefficients are the limiting inverse Gram matrix applied to(9).
Expanding the square and using the two pairings, the Gram limit and the
matched norm yields

```
E_(p_q)[s_q/q²-L]² ->0.                                  (12)
```

This is a sharp second-order *score-defect* profile. It is not the complete
second-order density response. In fixed Gaussian measure it also says
`(s_q/q²)h_q ->L` strongly in L2(phi). Indeed the first error is exactly
(12), and `||L(h_q-1)||²=E_p L²+E_phi L²-2 E_phi[L²h_q]->0`:
the first term converges by(5), the cross term by h_q->1 in L2(phi) and
L² in L2(phi). This step needs no unproved weighted bound on
`(h_q-1)/q`. The polynomial norm `E_phi L²=679/864` is checked exactly.

## 6. Released budget successor and limits of the result

For the unique small positive q_B with F(3-q_B)-1=B, asymptotic inversion gives

```
q_B=sqrt(6B)-(9/2)B+(317sqrt(6)/48)B^(3/2)+o(B^(3/2)).    (13)
```

Substitute q=sqrt6 z-(9/2)z²+c z³, z=sqrt B, into(1): the z⁴
coefficient is `sqrt6 c/3-317/24`, giving the displayed c. Strict monotonicity
from K1843 and the positive leading coefficient justify inversion; no
differentiation of a little-o remainder is used. Earlier K1855 effective
budget brackets remain the finite-error statements.

Equation(2) unlocks exact-optimizer polynomial response, including the
sixth/eighth moments needed here. It does not give a second-order H1 density
profile or a second polynomial response. Nor does it impose a tail envelope
on arbitrary densities merely satisfying near-optimal leading energy. Those
are different questions. A fifth-order value coefficient requires another
response estimate or an independently controlled dual; serializing more
terms of the upper trial alone does not certify it.

## Verification and hostile postflight

Run `sage -python tests/channel-swings/k1859_fisher_optimizer_tail_response.py`
and `python3 tests/channel-swings/k1859_fisher_optimizer_tail_response_probe.py`.
The producer derives the Hermite moments, rational trial jets, residual and
projection constants, inverse coefficient and dependency hashes. The separate
Fraction implementation reconstructs Hermites, Gaussian moments and series
without importing the producer. Its clean baseline precedes input mutations;
reporting-flag mutations are separate. Finite algebra does not prove the
maximum principle, log-cutoff limit, weak score identities or variational
asymptotics: the written proof above owns those arguments.

Hostile review checked: exact versus near optimizers; multiplier sign and
secant direction; absence of assumed value differentiability; exterior
comparison boundary and form-domain passage; logarithmic cutoff rates;
whole-line rational remainders; score-square projection and Gram normalization;
raw moments; normalization/dilation direction; nodal Sobolev energy; exact
inverse moment matching; and the inverse-budget coefficient. The principal
contrary construction is retained K1857 tail contamination, whose failure to
satisfy(3) is why it does not refute(5). The strongest overclaim would be a
generic near-optimizer moment theorem or a proved second density profile;
neither is claimed. No unresolved proof defect was found in this scope.
Independent-agent review of the written argument and a separate integrating
review found no blocking defect. The producer passed27 exact identity/jet
groups, including the strengthened supersolution identity; the separate replay passed20 rational groups and detected12
mathematical-input/reference faults plus4 reporting faults, each after its
clean baseline and with the failed assertion printed. These finite checks
remain distinct from the written analytic argument, independent-agent review,
formal verification and external peer review. No formal or external acceptance
is claimed. Source, physics-ledger and canon verdicts are unchanged.
