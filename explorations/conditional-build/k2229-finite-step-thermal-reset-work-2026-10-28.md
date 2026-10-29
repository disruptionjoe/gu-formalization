---
title: "K2229 Finite-step thermal reset with explicit work"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied tunable record gap and fresh resonant Gibbs cells; no bath renewal, autonomous apparatus or GU realization
scripts:
  - tests/channel-swings/k2229_finite_step_thermal_reset_work_probe.py
---

# K2229 Finite-step thermal reset with explicit work

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
result: K2229 local sequential thermal reset and mean work identity
carrier: positive record qubit, fresh finite Gibbs qubits and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: binary occupation and additive energy
action_owner: repository-construction -- tunable gap and externally timed resonant exchange
target: replacement channel, net mean switching work and thermal-cell consumption MAP-TYPE=intertwiner
```

## Preflight selection and scope

Loaded AGENTS, geometer-versus-physics routing T15/T16/T17, source-native
comparator routing, six-axis Layer 0, research posture, current state,
verification, contribution and path-dependency surfaces. This is the same
positive, post-readout record as K2223; no indefinite GU form or native action
is identified with its Hamiltonian. None of the Higgs/chirality comparators
is used to adjudicate a source claim.

K2226 already solves unrestricted sorting of the fixed identical thermal
register, with exact uniform error and sharp exponent. Repeating that
optimization adds no resource construction. Its fresh-cell and global-control
limitations suggest a different substantive target: an explicit two-qubit
exchange implementation with finite switched-gap work and precision. This
changes the allowed bath gaps and record Hamiltonian during reset; it is
not an improvement to K2226's optimum in its unchanged model.

Retrieval of reset/erasure/gap/quasistatic/collision terms in conditional-build
K artifacts found K99/K100 finite Gibbs discrimination, K1910/K1911 dephasing
and K1916 preparation accounting, but no prior finite-step detector reset
consumer. Finite-step SWAP erasure itself is established: see Meier and
Yamasaki, [PRX Energy 4, 023008 (2025)](https://doi.org/10.1103/PRXEnergy.4.023008),
Appendix A1. The relative-entropy accounting follows the same finite-reservoir
principle as [Reeb and Wolf](https://arxiv.org/abs/1306.4352). No novelty is
claimed for these general thermodynamic mechanisms.

## 1. Why a fixed degenerate record cannot cool for free

Let H_R=0, tau_B=exp(-beta H_B)/Z on any finite bath, and
rho_R=diag(1-w,w), 0<=w<=1/2. If [U,I_R tensor H_B]=0, then

    rho_R tensor tau_B >= w I_R tensor tau_B,
    U (I_R tensor tau_B) U* = I_R tensor tau_B.

Taking the bath trace gives rho_R' >= w I_R. Every unwanted-record
population is at least w; its half trace distance from a prescribed pure
record is therefore at least w. Identity attains w. Equivalently the induced
record channel is unital, since I_R/2 tensor tau_B is invariant. No bath size
or degeneracy evades this exact bound. It concerns an initially independent
Gibbs bath, fixed degenerate record and energy-preserving unitary, without
work storage or additional nonequilibrium resource. It does not exclude
K2226's arbitrary driven unitaries, a nondegenerate record, nonthermal bath,
or an explicit battery. Correlations with an untouched field do not change
this local marginal argument.

## 2. Concrete reset protocol

Fix beta>0, coupling g>0, 0<v<=1/2 and r>1. Write

    x_j=log((1-v)/v)+j log r, E_j=x_j/beta,
    p_j=1/[1+((1-v)/v) r^j], j=0,...,m, q=p_m.

Supply m+1 initially independent qubits B_j at the common temperature beta,
each with Hamiltonian E_j n and Gibbs state diag(1-p_j,p_j). Their gaps
are different; this is not K2226's identical p=1/4 bath. The record has zero
Hamiltonian at input and output. It may have arbitrary reference correlations.

1. Raise the record gap from zero to E_0 while isolated.
2. Couple it to B_0, then decouple, by the exchange pulse below.
3. For j=1,...,m raise its gap from E_(j-1) to E_j, then exchange with B_j.
4. Lower its gap from E_m to zero while isolated.

For each collision use the TOTAL Hamiltonian

    H_j=E_j(n_R+n_Bj)+g(I-S), t_swap=pi/(2g),

where S is the two-qubit SWAP. Both summands are nonnegative and commute.
Exp[-igt(I-S)]=S at t=t_swap. Thus the exact propagator is free diagonal
rotations followed by SWAP. Those rotations leave the fresh diagonal Gibbs
state invariant. On R and any reference F, the collision channel is exactly

    X_RF -> diag(1-p_j,p_j) tensor Tr_R(X_RF).

The old state and its correlations transfer to the spent cell (with a local
phase rotation). No initially pure ancillary bit or global bath sorting is
required. After the last collision the complete reset is the replacement
channel with output diag(1-q,q). Its half-diamond distance from ideal pure
reset is exactly q: the difference is a replacement map, and the trace norm
of the difference of its two output states is 2q. This is uniform over all
inputs and references, even though the work below depends on the input.

The free gaps stay on during exchange. Coupling switch-on and switch-off
works cancel exactly: expectation of g(I-S) is conserved during the pulse.
Each has magnitude <=g because at pulse entry R and the fresh cell are
independent and <S>=Tr(rho_R tau_j) lies in [0,1]. Their absolute sum is
therefore <=2g per collision. A stronger universal operator-norm bound would
be 4g; the 2g bound uses this stated product-entry property, not arbitrary
entangled pulse inputs. All generators are finite-dimensional, positive and
bounded; this establishes supplied finite controls, not fabrication or a
clock realization.

## 3. Exact work, heat and excess dissipation

Let w be the initial excited population. In particular K2223's dephased
record has 0.3045489<w<0.3046040. No work is inferred from an entropy formula:
the actual gap switches give it directly,

    beta W = w x_0 + sum_(j=1)^m p_(j-1)(x_j-x_(j-1)) - q x_m.   (1)

The last term is recovered work in lowering the final gap. Omitting it
prices a different endpoint Hamiltonian. The bath energy increase is

    beta Q = x_0(w-v)+sum_(j=1)^m x_j(p_(j-1)-p_j) = beta W.     (2)

This equality follows by telescoping and zero record endpoint energies.
It includes only the supplied switches and cells; it excludes cell
preparation/renewal, clock, electronics, observer copying and detector work.

For the dephased input, let h be binary entropy in nats and D Bernoulli
relative entropy. A direct identity is

    beta W = h(w)-h(q)+D(w||v)+sum_(j=1)^m D(p_(j-1)||p_j).     (3)

Indeed for each exchange a->b at gap x_b=log((1-b)/b),
x_b(a-b)=h(a)-h(b)+D(a||b). Sum over a=w,b=v and the remaining pairs.
Each term is nonnegative. The first mismatch term retains the uncertainty
of the optimized w: the protocol uses a fixed v and is not secretly tuned
to an uncertified exact prior. Formula (1) remains valid for coherent inputs;
formula (3) uses the diagonal population entropy h(w), not an assertion that
this equals their von Neumann entropy. The uniform channel bound does not
imply a uniform input-independent work cost.

Set delta=log r. For successive Gibbs states, with A(x)=log(1+exp(-x)),

    D(p(x)||p(x+delta))=A(x+delta)-A(x)+delta p(x)
       = integral_0^delta [p(x)-p(x+t)] dt
       <=delta[p(x)-p(x+delta)].

Consequently

    0 <= beta W-h(w)+h(q)-D(w||v) <= delta(v-q).                (4)

There is also the standard curvature bound m delta^2/8 because A''<=1/4.
At a fixed final gap and v, m->infinity makes delta=(x_m-x_0)/m shrink,
so the excess above h(w)-h(q)+D(w||v) goes to zero. If v=w is supplied
exactly, the mismatch term vanishes. This limiting claim does not hold at
fixed r while q->0. The scalar h(w)-h(q) bound is a lower bound on this
specified marginal reset, not a claim about protocols exploiting accessible
quantum side information.

A conservative absolute-switch account is

    W_gap,abs = W+2qE_m,
    W_all,abs <= W+2qE_m+2g(m+1),                              (5)

when gaps increase and the final quench lowers them, as here. The net is W.
This distinguishes recovered energy, total exchanged energy and net work.

## 4. Exact detector consumer

Choose v=3/10, r=101/100, m=1700. Then

    q = 3*100^1700 / (3*100^1700+7*101^1700),
    0.00000001930579 < q < 0.00000001930581,
    17.762860 < beta E_m < 17.762861,
    0.616212 < beta W < 0.616260.

These work bounds hold for the entire certified K2223 w interval. They are
rational interval inequalities, not floating-point reported digits. The
probe uses the positive atanh series for log with explicit geometric tail,
and downward-rounded rational p_j sums with an exact 1700-unit last-place
error allowance. It never sums huge rational denominators or truncates a
thermodynamic tail.

For M=1000 resets with independent fresh banks, telescoping replacement
channels yields half-diamond error <=M q<0.00001930581 for arbitrary
intervening CPTP detector maps. Each reset consumes 1701 fresh, different-gap
thermal cells; the total is 1,701,000. Total contact time per reset is exactly
1701*pi/(2g), with ideal instantaneous gap switching as a declared control. No finite
switching-power or smooth-ramp implementation is claimed.
Total time at fixed g grows with the number of contacts. Holding total time
fixed while increasing m requires g to grow; (5) then makes the bound on
absolute control exchange grow accordingly. This is an explicit sufficient
control family, not a universal speed limit or optimal work/time tradeoff.

To take q->0 the final beta E_m=log((1-q)/q) diverges. At fixed maximum gap
this family has error floor 1/(1+exp(beta E_max)). This is a family-specific
bound; it is not a no-go for collective compression with bounded individual
gaps, which K2226 already constructs. Finite q keeps every Gibbs cell faithful,
so no finite-temperature exact erasure or rank violation occurs.

## 5. Composition with the retained-drift detector

The [K2228 continuum control theorem](k2228-continuum-energy-form-detector-control-2026-10-28.md)
gives half trace error delta on the complete detector output, including the
record and arbitrary reference, for its specified input-energy bound. Apply
the uniform reset above afterwards, retaining any separately copied reported
outcome. Contractivity and a hybrid comparison give complete error at most
min(1,delta+q). Erasing the working record does not erase an already copied
classical outcome or price the copying operation.

For the SAME fixed optimized instrument, let w be the ideal click probability
in the K2223 interval and w_actual the actual post-readout record population.
The record measurement gives |w_actual-w|<=delta. Formula (1) is affine in its
initial population, so the *actual* reset work satisfies exactly

    |beta W(w_actual)-beta W(w)| <= x_0 delta.

Thus the certified reset-work interval expands by x_0 delta at each end;
no unbounded-field-energy convergence is needed for this bounded record-work
statement. For delta<=1/10000, x_0=log(7/3)<1 yields

    complete error < 0.00010001930581,
    0.616112 < beta W_actual < 0.616360.

These are sufficient bounds with supplied speed chosen to meet the K2228
estimate and fresh reset cells; they are not an efficiency optimum. The
post-readout marginal assumption holds after record pinching, even when
correlated with field and reference. A general continuum smear has its own
prior; do not use the K2223 numbers for it. No numerical addition of reset
work to field E_star is licensed without a common energy ruler and beta.
The field control's *actual* output energy still has only K2228's upper
bound, not convergence to the ideal optimum.

## 6. Renewal boundary and hostile postflight

The apparatus's record returns to a degenerate Hamiltonian and a nearly pure
state. Its bath does not return to its initial product Gibbs state. Cell B_0
receives the old record and field correlations; later B_j receives the prior
Gibbs marginal p_(j-1) at the larger gap E_j. Equation (2) accounts for their
energy increase. Reusing them as fresh independent thermal cells invalidates
the channel proof. An external bath-renewal map must be constructed and
priced before cyclic thermal apparatus credit. The supplied initial Gibbs
bank is the resource; exact local swaps do not constitute a renewal mechanism.

Strongest overclaim: a low net erasure work proves a low-cost autonomous
repeatable detector. The total apparatus, thermal preparation/renewal,
external timing and gap control remain unconstructed. The true result is
finite-precision sequential reset with exact mean switch work in a stated
control/resource model. A second overclaim would append W to the detector's
dimensionless E_star without selecting a shared energy ruler and beta.

Strongest counterconstructions: fixed-degenerate energy-preserving control
cannot reset below w; K2226's driven collective compression beats the
family-specific maximum-gap floor without contradicting it; a pure SWAP
resource resets exactly without a faithful finite Gibbs bank. These separate
which supplied resources each theorem uses.

Weakest reproducibility seams are forgetting the final gap quench, ignoring
free rotations in the SWAP pulse, assuming resonance for unequal gaps,
confusing the reference-uniform replacement channel with input-independent
work, and silently renewing spent cells. The written proof resolves these;
small exact matrix-unit and shell-permutation checks exercise the channel and
obstruction. Large-consumer certification is rational arithmetic. Neither
finite controls nor agent review is proof-assistant/external certification.
No source claim, ledger, physical grade, GU hypothesis vote or canon changes.
