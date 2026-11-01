---
title: "K2466 Exact verifier design with unequal errors and costs"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional complete-carrier continuous and finite-count optimum with calibrated effect-cost dual; no measured or universal local optimum"
---

# K2466 Exact verifier design with unequal errors and costs

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2466
carrier: both original 108-dimensional positive Hilbert programs and complete Q/T effects LAYER=toy CHIRALITY=N/A
pairing: original positive-Hilbert effect order and complete target-orthogonal spectral pairing ON=declared_carrier
real_structure: complex positive states with exact real algebraic coefficients
grading: original tensor slots and finite character sectors
action_owner: repository-construction -- supplied conditional mathematical models
target: Exact verifier design with unequal errors and costs MAP-TYPE=evaluation
```

## Result and premises

K2463's equal-cost/common-error optimum does not decide designs whose two
local tests have different errors or charges. Here the exact complete-carrier
optimization reduces to finitely many algebraic candidates, including the
nonzero-character bottleneck that an isolated two-by-two optimization can
miss. A calibrated cost dual then decides whether additional effects can
improve the baseline. This is a prospective mathematical design rule for
supplied programs, not apparatus calibration or native GU physical recovery.
SC-META-53 remains UNCERTAIN; LT-SM8, ledger0.263 and canon are unchanged.

Use original target P=|Psi><Psi|, Q and phase-averaged T from K2457 on all108
coordinates. Labels must be fresh and independent of the current resource
conditional on history, with whole-instrument and setting-law calibration as
in K2463. Fixed pi gives per-actual-use branch charge
k_j=cU+pi*c_j/(1-pi)>0. Let e>0 be the unchanged original output allowance,
and beta_j>=0 a justified one-sided additive effect error. They are fixed
when optimizing; changing an instrument requires re-establishing its budget.
No optimization over unknown measurements or unrestricted branch leakage is
licensed by substituting hypothetical charges.

## 1. Complete original spectrum and its crossover

Write q for the T weight, a=27/100 or15/52 and h=1/[2(1+a)]. K2457's
original full-carrier blocks yield

    D(q)=1-6hq+h(h+4)q^2,
    g(q)=[1-hq+sqrt D(q)]/2,
    ell=max_(30 nonzero characters)[t+sqrt(t^2-4d)]/2,
    nu(q)=min(1-g(q),1-q ell).                         (1)

Other zero-character eigenvalues are at most1-q<=g(q). The probe
re-authenticates the original block reports and checks every nonzero block.
The maximizing character is(0,0,0,-1), with trace/determinant
3927/3302,569/1651 for the first law and761/670,213/670 for the second.
For both,1-h<ell<1. The unique crossover is

    qx=(ell-h)/(ell^2+h ell-h).                         (2)

To prove uniqueness, g(q)/q is the top eigenvalue of
T0+diag(1/q-1,0), strictly decreasing since its positive offdiagonal gives
the top eigenvector a nonzero first coordinate. It starts above ell and
ends below. Substitution into the characteristic polynomial gives(2), with
the larger-root check retained. The zero block controls q<=qx; a nonzero
block controls q>=qx. Omitting the second regime can choose a false optimum.

## 2. Exact finite algebraic optimization

Let beta(q)=b0+b1 q, k(q)=k0+k1 q, with beta endpoint values nonnegative
and both cost endpoints positive. Maximize the calibrated efficiency

    R(q)=[e^2 nu(q)-beta(q)]/k(q), 0<=q<=1.             (3)

A nonpositive maximum gives no finite certificate from this sufficient
bound. On[qx,1], R is linear fractional and endpoints suffice, unless it
is constant (then both endpoints and the entire segment tie). On[0,qx],
write the numerator as N=u+v q-w sqrt D, where

    u=e^2/2-b0, v=e^2 h/2-b1, w=e^2/2,
    A=h(h+4), L=v k0-k1 u,
    r=-3h k1-A k0, s=k1+3h k0.

The derivative sign is that of

    H=L+w(r q+s)/sqrt D.                              (4)

D is positive. Since the square-root second derivative is positive
(4A-36h^2=16h(1-2h)>0), N''<0. The numerator of R' is N'k-Nk',
whose derivative N''k<0, so at most one stationary point occurs on this
interval. Candidate roots solve

    L^2 D-w^2(r q+s)^2=0,
    L sqrt D+w(r q+s)=0.                              (5)

The first is a quadratic; the second rejects roots introduced by squaring.
Compare all admissible roots with0,qx,1. This is an exact finite procedure,
not a grid optimizer. Degenerate linear/constant quadratic cases are resolved
by the unsquared equation; an interval of ties on the second regime stays a
tie. The probe verifies original-law examples with common errors, unequal
errors, crossover maxima, unequal costs, endpoint maxima and no positive
margin. Interval enclosures check the algebraic candidates and strict
comparisons; equations(1)-(5) are their exact descriptions.

## 3. Released calibrated cost dual and added tests

On the entire target-orthogonal space let

    A_j=e^2(I-E_j)-beta_j I, k_j>0.

For finitely many complete target-preserving effects, cost reweighting
x_j=p_j k_j/(sum p_i k_i) maps the probability simplex bijectively to itself.
Thus the global continuous optimum is

    max_p lambda_min(sum p_j A_j)/(sum p_j k_j)
       = min_(X>=0,TrX=1) max_j Tr(X A_j)/k_j.          (6)

Indeed lambda_min is the minimum of the density-matrix expectation;
finite-dimensional compact convex minimax interchanges the two players.
No invertibility or full-rank density is required.

A baseline of value theta>0 remains globally optimal after adding effects
iff SOME density X supported on its active minimum-eigenvalue space obeys

    Tr(X A_j)<=theta k_j for every old and new j.       (7)

Sufficiency is the dual upper bound. For necessity, a dual minimizer at the
unchanged optimum must attain equality on the baseline mixture, so its
support lies in that minimum eigenspace. At a strict single zero-block
bottleneck this X is the unique eigenprojector. A new effect with strictly
larger normalized calibrated rejection then improves the optimum by a small
mixture (first eigenvalue derivative). At a block crossover use convex
combinations or general densities on the active space: one failed chosen
witness does not prove improvement.

Since Tr X(I-E)<=1, the universal sufficient charge threshold is

    k_E >= (e^2-beta_E)/theta.                         (8)

Negative right sides simply make every positive charge satisfy the bound.
When e^2-beta_E>0 this threshold is sharp over unrestricted complete
physical effects: E=P makes A_E=(e^2-beta_E)I on the complement. Mixing
it with the baseline gives a ratio strictly between the two individual
ratios when they differ; equal ratios tie. Thus below/at/above(8) it improves/ties/worsens. P is not asserted local
or available. A full-local optimum remains unproved; a new cheap local
effect could outperform the Q/T family.

## 4. Useful consumers and limits

For fixed routing and budget numerator Bconf, continuous prospective cost
is Bconf/[(-log(1-pi)) R]. Thus maximizing(3) minimizes this sufficient
continuous cost. K2465 supplies the sharper half/half numerator under its
stated pathwise or expected budget. The probe composes both original-law
unequal-error optima with e=.004998, fixed pathwise original budget10^-6,
confidence.05, explicit scaled branch errors and positive actual mean
success; it reports rounded actual-use counts and expected schedule costs.
These charges are examples, not measured durations. Integer ceilings can change the winner; Section5 resolves the finite expected-cost
objective for fixed setup. Calibration acquisition and confidence-qualified
cost tails still require their own complete formulas. No postselected-cost
optimum is asserted.

Controls reject the zero-block-only design when a different original
character controls it, omission of branch calibration, treating mean cost as
deterministic, and the assumption that unrestricted projectors must be local, using an
explicit two-qubit Bell projector as a separate control. That control is
not a locality test of the original108-dimensional P.
The full-carrier input is reused by authenticated evidence; universal
optimization/duality proofs are separate from the finite examples. Internal
review is not external-expert, proof-assistant, novelty or experimental
certification.

## 5. Released finite-count optimum, including rounding

The continuous optimum need not minimize the actual prospective expected
cost. Write Aconf>0 for the fixed confidence numerator divided by
-log(1-pi); put D(q)=e^2 nu(q)-beta(q) and retain positive affine k(q).
For fixed setup S the finite objective is

    S+ceil(Aconf/D(q))*k(q), D(q)>0.                   (9)

D is concave: nu is one minus the largest eigenvalue of an affine effect.
For each integer N, the feasible set F_N={q in[0,1]:D(q)>=Aconf/N} is a
closed interval or empty. Increasing k selects its left endpoint; decreasing
k selects its right endpoint; constant k admits any feasible point.
An incumbent C0 excluding setup bounds all improving counts by

    ceil(Aconf/max D)<=N<=floor(C0/min k).             (10)

A conservative enumeration from1 to the upper bound is also exhaustive.
For each N compute the interval endpoints by the zero-block quadratic
or the nonzero-block linear equation. Put z=Aconf/N. On the zero branch,

    (u-z+v q)^2=w^2 D(q)_discriminant,
    u-z+v q>0,                                    (11)

where D(q)_discriminant is the polynomial in(1), not the calibrated margin.
Retain the correct interval and unsquared sign. On the nonzero branch the
equality is e^2(1-q ell)-b0-b1 q=z. Add feasible0,1 and crossover values.
Degenerate/constant cases use the original equation. These exact algebraic
conditions on the fixed supplied constants define the endpoint candidates.

Minimizing N*k over these feasible pairs is EXACTLY minimizing(9): any
q has its minimal feasible N=ceil(Aconf/D(q)), and any larger feasible N
costs at least that minimal count because k>0. An endpoint with a smaller
minimal count is therefore harmless; that count is also enumerated. Fixed
setup adds a constant and does not change the winner. Setting-dependent
setup requires separate optimization and is not included here.

For both original laws, take normalized e^2=1, betaQ=1/50,betaT=2/25,
kQ=2,kT=3 and Aconf=100. These are supplied mathematical example values.
For a27/100 the continuous weight q approximately.68538665 has rounded
count283 and expected cost759.96442. Exhausting counts1--379 gives the
finite optimum at count283, q approximately.68197267, cost758.99827.
For a15/52, exhausting1--388 gives count289, q approximately.68567956,
cost776.16139, versus the continuous-weight cost776.37757. Both winners
are positive-sign zero-block equality roots with D=100/N. The probe
certifies all discriminant decisions, each feasible-count comparison and
the tail exclusion(Nmax+1)*min k>C0 using rigorous intervals. The published
roots are defined by(11), not by their displayed decimal approximations.

This completes finite rounding for the stated expected-cost objective.
It does not optimize tail-risk budgets, measured calibration acquisition,
routing-dependent information budgets or unsupplied hardware. Those require
their own declared inputs; a universal local-effect optimum remains separate.

[Probe](../../tests/channel-swings/k2466_calibrated_verifier_design_probe.py) and [report](../../lab/process/k2466-calibrated-verifier-design.json).
