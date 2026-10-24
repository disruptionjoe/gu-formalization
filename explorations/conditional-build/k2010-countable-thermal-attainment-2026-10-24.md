---
title: "K2010: Countable thermal attainment and a dimension-independent spacing penalty"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2010_countable_thermal_attainment.py
  - tests/channel-swings/k2010_countable_thermal_attainment_probe.py
---

# K2010: Countable thermal attainment and a dimension-independent spacing penalty

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
result: actual finite-or-countable optimizer, unrestricted parameter regularity and strict fixed-spacing exposed-line gap
carrier: fixed extreme four-state channel, four-level Gibbs bath and positive-gap nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and upper initial mean energy ON=independent_initial_registers
real_structure: complex shell unitaries and real diagonal populations
grading: discrete energy resonance shells, not source chirality
action_owner: repository-construction -- unchanged K2008 finite-or-countable model
target: existence and spacing sensitivity of the unrestricted dimensional optimum MAP-TYPE=intertwiner
```

## 1. Results and the gap in the prior argument

Keep exactly [K2008](k2008-effective-thermal-dimension-approximation-2026-10-24.md)'s
finite-or-countable model: nonnegative nondegenerate pure-point energies with
ground zero, minimum gap delta>0, a normal trace-class preparation of mean at
most finite E, independent registers, and exact spectral-projection conservation.
The bath energies are 0,1,2,3 and weights t^b/Z for 0<t<1. Denote the common
finite/countable infimum by F_infty(delta,E,t).

**Attainment.** On the feasible domain stated in K1987, F_infty is attained
by an actual finite or countably infinite catalyst of this same class. One
can choose an optimizer with at most two populated resonance components.
This does NOT prove a finite optimizer or a necessary dimension/error rate.
K2008's equality of infima alone did not establish this assertion.

**Parameter limits.** The unrestricted value is jointly lower semicontinuous
in (delta,E,t) for delta>0 and 0<t<1, treating infeasibility as +infinity.
It is left-continuous in spacing and right-continuous in budget at feasible
points. At fixed E,t it is continuous in delta inside (0,1/2) and (1/2,1).
Possible jumps at the thresholds are not evaluated here.

**Strict penalty uniform in dimension.** At t=1/2, every fixed delta>0 and
6/5<E<11/5 in the feasible domain satisfy

    F_infty(delta,E,1/2) > 63/100 - 3E/20.                 (1)

On every compact subinterval of that energy interval, with delta bounded
below by a positive constant, the gap is bounded below by a positive
constant, uniformly over all feasible dimensions and spacings. This
strengthens K1978's fixed-dimension strict gap. Increasing dimension alone
cannot erase a fixed positive spacing penalty. The result supplies no sharp
linear-in-delta lower rate.

Layer0: these are the same independent thermal objects as the cited results,
not an identified GU state space or physical quotient. SC-META-53 remains
UNCERTAIN; LT-SM8 and LT-GR6b remain NEEDS.

## 2. Compactify the spectra and populations, not all infinite unitaries

Take a sequence of finite near-minimizers, pinch and use the inherited sharp
shell construction. Sort energies a_0=0<a_1<..., and pad a missing index with
+infinity and population zero. Positive spacing gives a_i>=i delta. For
any integer m>=1,

    sum_(i>=m) p_i <= E/(m delta).                        (2)

This bound is uniform even though the Hamiltonian and dimension vary.
Diagonal extraction gives a_i^(n)->a_i in [0,+infinity] and p_i^(n)->p_i.
Finite limiting energies retain their gap and order. If a_i=+infinity,
then p_i=0 by the mean bound. Equation (2) proves total limiting mass one
and convergence of the padded populations in l1. Fatou on finite energy
prefixes gives sum a_i p_i<=E. Discard infinite limiting energies. The
remaining spectrum is finite or countable and has no finite accumulation.
Its diagonal state is normal, trace class and has finite mean.

No compactness of the infinite-dimensional unitary group is assumed.
Fixed-Hamiltonian energy compactness is familiar background (for example,
[Weis and Shirokov, Theorem 2](https://arxiv.org/abs/2002.03969)); it does not
by itself handle varying spectra, new resonances or exact-channel feasibility.
The elementary bound above and the shell argument below supply those steps.

## 3. Exact channel feasibility survives resonance mergers

The inherited necessary and sufficient shell condition is

    2 number{occupied a: e-a in {0,1,2,3}}
      <= number{physical a: e-a in {0,1,2,3}}.            (3)

Every occupied level counts, regardless of the size of its positive mass.
A limit can GAIN resonances, so checking each old shell separately without
accounting for simultaneous occupied inputs would be insufficient.

Fix a limiting shell e with an occupied input. All its catalyst indices,
and all indices of possible prelimit partners, have energies bounded by
e+1 for sufficiently large n. Their number is uniformly finite by spacing.
Pass to a subsequence where their finite exact resonance patterns stabilize.
Partition the occupied bath/catalyst pairs in this limiting shell according
to which PRELIMIT total energies are equal. For each group, every limiting
positive population is positive eventually. Its prelimit shell therefore
has at least twice as many physical positions as these occupied inputs.
Physical positions of distinct prelimit shells are disjoint: one fixed
(catalyst index,bath label) cannot have two energies. Their union lies in
the limiting shell. Adding the inequalities proves (3), including newly
merged shells. A countable diagonal subsequence handles all shells.

The shell construction used by K1943 and extended in K2008 now supplies
finite unitaries in each limiting shell. Each shell has at most four
bath/catalyst positions; the system factor is fixed and finite. Their direct
sum, with unitary completion on unused columns, is a bounded unitary that
commutes with all total-energy spectral projections and implements the exact
full channel. This is a construction from limiting shell data, not an
unjustified limit of unitaries or an approximate channel assertion.

## 4. Lower semicontinuity of the sharp return

Use the inherited diagonal sharp formula

    R(p)=1/2 sum_i (p_i-I_i(p))_+,
    I_i= sum_(a_j-a_i=g) L_g (p_j-t^g p_i)_+
          +sum_(a_i-a_j=g) L_g (t^g p_j-p_i)_+,
    g in {1,2,3}, L_g=(1+t+...+t^(3-g))/Z.               (4)

For each finite limiting energy, possible neighbors lie in a bounded window
and have bounded indices. Stabilize their exact prelimit resonance pattern.
Every old edge survives; the limit may add edges, whose incoming terms are
nonnegative. Populations and L_g(t) converge. Hence the limiting deficit at
each such index is no greater than the limit of its prelimit deficits.
Fatou applied to these nonnegative contributions yields

    R(p_limit) <= liminf_n R(p_n).                       (5)

The sharp construction realizes this value. K2008 says every admissible
countable value is at least the finite infimum, so a minimizing sequence
and (5) prove attainment with equality.

To obtain two populated components, apply K1972/K2006 to each finite
near-minimizer BEFORE extracting. Choose a subsequence with stable component
labels for each finite index. Two bounded levels in the same prelimit
connected component have a connecting chain of gaps at most three entirely
between their energies: sort the component's levels and use adjacent gaps.
All intermediate indices are uniformly bounded. That finite chain survives
a further subsequence, so a component cannot split among finite limiting
levels. New edges may merge the two labels. Thus there are at most two
populated components in the limit. This is not an invocation of an
infinite-dimensional extreme-point theorem.

For varying parameters converging to delta>0, finite E and 0<t<1, use a
uniform lower gap delta/2 and bounded energy in (2). The same proof yields
joint lower semicontinuity. Monotonicity supplies left spacing and right
budget continuity. Infeasible limiting parameters cannot be limits of
feasible protocols with bounded return, since the construction would give
a feasible limiting protocol.

## 5. Uniform approximation releases unrestricted spacing continuity

For E>1, K2008 gives, uniformly in feasible delta and 0<t<1,

    0 <= F_(2N+7)(delta,E,t)-F_infty(delta,E,t)
       <= (E-1)/(N-E), integer N>E.                     (6)

K2006 proves each finite F_d continuous in spacing within (0,1/2) and
(1/2,1). Uniform convergence in (6), followed by the elementary three-term
triangle inequality, transfers this continuity to F_infty. At E=1 the
value is constantly 1/2 on its feasible spacing interval. Above one the
inherited feasible value is 1/2. No infimum-of-continuous-functions shortcut,
threshold continuity, semialgebraicity of the unrestricted value, or explicit
uniform continuity modulus is claimed.

## 6. A fixed spacing leaves a positive gap even at infinite dimension

K1950's lambda=3/20 certificate, a=63/100 and cutoff K=8 proves

    R(p)+(3/20) mean(p)
      >=63/100 + sum_(s>8) ((3/20)s-63/100-1/2)p_s.     (7)

The tail coefficient is strictly positive for every s>8 (already at8 its
margin is7/100). Its proof uses the one-sided tail estimate and a finite
canonical census. For the present countable class the proof still applies:
positive spacing makes the low physical window finite; nonnegative flow
sums pass by Tonelli and the first moment is finite. This transfer also
follows by applying the same unnormalized tail argument directly, without
renormalizing or losing the strict tail term.

If an admissible countable protocol attained equality in (1), (7) would
force mean exactly E and zero population above8. Retain all its physical
levels through11: spacing makes that set finite and every occupied shell
is preserved. This would produce a FINITE protocol attaining the exposed
line at an interior energy, contradicting K1950's certified equality-face
classification. That classification permits only the two canonical endpoint
preparations, both supported at energies1,3; distinct nondegenerate components
cannot simultaneously occupy those same two energies. The current argument
reuses this classification and does not claim to recompute its census.

Section4 provides an attained countable optimum. Since none can equal the
line, its gap is strictly positive. This reasoning would fail if only an
infimum, without attainment, were available. For the uniform compact-energy
statement, the gap is lower semicontinuous, all feasible spacings are at
most2, and the feasible parameter set with delta>=delta_min and E in a
compact interior interval is closed and compact. Its positive gap therefore
has a positive minimum. Empty feasible parameter sets are excluded.

There is an effective fixed-parameter consequence at rational delta,E and
t=1/2. Evaluate the complete finite program at d=2N+7 and call its exact
value u_N. Increase integer N>E until

    u_N-(E-1)/(N-E) >63/100-3E/20.                       (8)

Strictness and (6) guarantee that this search terminates and returns a
rational positive lower-gap certificate. It may be computationally very
expensive; no large finite program or numerical gap is claimed executed here.
There is no derived complexity bound or matching small-delta lower rate.

## 7. Released positive-price consumer: an explicit finite optimizer

Fix delta in (0,1], 0<t<1 and ANY lambda>0. Minimize
J=R+lambda mean over the same finite-or-countable physical class, without
a fixed upper mean budget. Choose an integer N>1+1/lambda. Then the
penalized minimum is attained with at most **2N+7 physical levels**.
This is a fixed-spacing version of the finite positive-price endpoint;
K1950 already proves finite positive-price reduction in the unspaced model.

The pure mean1 protocol gives B=1/2+lambda. A competitor with J>B can
be replaced by that baseline. Otherwise its mean is at most B/lambda<N.
Remove occupied population above N, of mass q<1, but keep physical
completion levels through N+3. With H the discarded first energy moment,
the one-sided tail estimate and homogeneity give

    J(normalized low)-J(original)
      <= [q(J(original)+1/2)-lambda H]/(1-q)
      <= q(B+1/2-lambda N)/(1-q) <=0.                   (9)

The final coefficient is strictly negative, so every optimizer has zero
occupied mass above N. Normalization does not increase mean because every
discarded energy exceeds the original mean. This preserves actual spacing
and the exact full channel. Apply the existing finite two-component
reduction and K2008's count of retained physical levels: at most2N+7.
No arbitrarily distant unoccupied level is needed. The resulting bounded
finite-dimensional feasible family is compact and the penalty is
continuous in actual protocol data, proving attainment. Equivalently, the
complete finite shape program minimizes return plus the energy price.
At rational delta,t,lambda it is a finite exact rational calculation; no
large such minimization is claimed executed here.

For 1<delta<=2 the inherited return is always1/2 and minimum mean is2,
so the three-level mean2 witness minimizes every positive-price objective.
For delta>2 no protocol exists. At lambda=0 the cutoff argument fails and
no finite attainment is asserted.

This does NOT prove finite attainment at every hard budget. Supporting
lines determine a convex relaxation when the fixed-spacing budget frontier
is not convex, and no converse Lagrange-multiplier assertion is supplied.
The endpoint preparations at mean6/5 and11/5 already share the unspaced
supporting line even though fixed positive spacing forbids its strict
interior values. This is a concrete reason to retain the distinction.

Three exact physical consumers use the mean11/5, return3/10 preparation
on levels0,...,4 and a small remote singleton. At prices1/100,1/20,3/20,
they obey J<=B and contain actual mass beyond N; the normalization,
completion, energy and strict penalized improvement in (9) are checked.
The finite dimension bound is sufficient and may be very loose.

## 8. Checks, contrary cases and remaining questions

The accompanying standard-library scripts separately implement incoming-flow
and direct bath-label return calculations. Controls exercise rank-safe merging
of physical shells, disappearing tails, finite versus escaped levels, exact
geometric tails, threshold lower semicontinuity, and the strict tail margin.
The probe starts with a green baseline and then corrupts actual spectrum,
normalization, completion or return data. Counts in the report are finite
arithmetic controls, not proofs of the compactness or universal statements.

A mean bound WITHOUT a positive spacing bound does not provide the index
estimate (2): put n levels in [0,1] with equal populations. Their energy is
bounded while their index tails are not tight. This is a counterexample to
the compactness argument without spacing, not an exact-channel thermal protocol. This is an explicit reason
not to extend the theorem to vanishing gaps, degeneracies or continuous
spectra. A limit can strictly improve return when resonances appear;
ordinary return continuity, rather than lower semicontinuity, is false.

The producer and full replay pass27 merger protocols,4 escaping sequences,27
geometric prefixes and4 strict tail coefficients, plus3 physical positive-price transfers. The separate probe passes66
arithmetic groups plus3 positive-price transfers, rejects4 actual mathematical faults after a green baseline,
and checks4 provenance hashes separately. Its initial baseline was red because
the bath-label implementation omitted the common factor one half on incoming
maxima. The inherited shell formula exposed the error; the factor was repaired
and the full probe replayed. This harness error earns no mathematical-fault
credit. No universal proof or large program is counted as an executed finite test.

The proof and independently coded probes are same-author internal checks,
not independent specialist acceptance or proof-assistant verification.
Strongest overclaim: finite attainment or a sharp spacing penalty. Strongest
contrary mechanism: gained resonances with several occupied branches, handled
by the disjoint prelimit shell partition. Weakest remaining constructive seam:
the existence proof supplies no explicit optimizing countable preparation or
practical convergence rate. Full positive-spacing formulas, finite attainment
and necessary resource rates remain open. Source, ledger and canon unchanged.

Reproduce with `python tests/channel-swings/k2010_countable_thermal_attainment.py --write`,
the same command without `--write`, and
`python tests/channel-swings/k2010_countable_thermal_attainment_probe.py`.
