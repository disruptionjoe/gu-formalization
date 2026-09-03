---
title: "K114 K113 hybrid detector, finite-energy record and backreaction boundary"
status: active_research
doc_type: conditional_hybrid_diffusion_jump_detector_and_backreaction_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact finite-dimensional reversible diffusion-jump, finite-energy detector-record, readout/retention and informative-detector backreaction theorem on the K113/K111 carrier; the detector coordinate survives continuous tie-wall crossings but changes at finite jump rate, has nonzero finite-parameter error, and either backreacts record-conditionally or leaves the reversible informative class; no source/GU physical environment, spacetime causal BV-BFV descent, Born derivation, prediction or confirmation follows
manifest: lab/process/k114-k113-hybrid-detector-finite-energy-record-wave.json
probe: tests/channel-swings/k114_k113_hybrid_detector_finite_energy_record_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K114 K113 hybrid detector, finite-energy record and backreaction boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet enlarges K113's finite-dimensional classical reflected
diffusion by one finite detector coordinate and constructs an exact reversible
diffusion-jump process. It proves a finite-energy record, persistence across
continuous tie-wall crossings, finite readout error and a backreaction
boundary. It does not authenticate a physical bath, clock, detector or source
action and does not construct a spacetime stochastic field theory.

```gu-typed-objects
result: one S_256-equivariant reversible hybrid diffusion-jump law places a discrete branch label in the joint finite-energy Dirichlet domain and lets it persist across continuous tie-wall crossings, but every finite score contrast has nonzero readout error and an informative reversible detector either backreacts on the record-conditioned base dynamics or leaves this class
carrier: K111 closed normalized nonnegative weight simplex Delta_255 times a finite 256-state detector coordinate LAYER=observed CHIRALITY=N/A
pairing: joint classical Gibbs density exp(-beta V(w)) a_r(w) against relative simplex Lebesgue measure and counting measure, with the inherited K105 lowerer used only after detector-center evaluation ON=repository_hybrid_detector_control
real_structure: real simplex coordinates, real reflected diffusion, positive real detector scores and a real classical jump process
grading: degree-zero classical diffusion-jump process and detector center, with inherited minimal K91 BRST grading only after conditional branch transport
action_owner: repository-construction -- K113's quartic plus a conditional logarithmic detector score, reflected gradient dynamics and detailed-balanced jumps; not authenticated as Weinstein's source action or a physical GU environment
target: finite-energy record, tie-wall persistence, readout-retention accuracy and reversible measurement-backreaction boundary MAP-TYPE=evaluation
```

## Inline preflight bookend

K113 owns an exact reflected Gibbs diffusion on the full K111 simplex, but its
natural sharp record `argmax(w)` is outside the weighted `H1` Dirichlet domain.
The reverse edge is therefore not another discontinuous function of `w`. It is
whether a record becomes regular when the state space itself contains a
detector coordinate, and what price that enlargement pays.

The route census compared five constructions. Absorbing basin walls make the
record permanent by importing an irreversible branch law. A slave detector
`R=argmax(w)` repeats K113's wall singularity. A one-way finite detector driven
by the unchanged K113 process is admissible as a nonequilibrium escape but has
no immediate exact joint equilibrium law. A reversible hybrid process makes
the joint measure, boundary, jump rates and energy form exact. An actual
spacetime stochastic field theory has no authenticated source action, causal
covariance or BV-BFV domain to act on. The reversible hybrid route is selected
because it decides finite record energy and exposes backreaction without
pretending to close the physical owner.

## 1. Positive detector scores and the joint law

Let `n=256`, let `Delta` and `V` be K113's simplex and quartic, and choose

```text
epsilon>0,  m in {1,2,...},  beta>0,  c>0,
a_r(w)=(epsilon+w_r)^m,
A_m(w)=sum_s a_s(w).                                      (1)
```

The enlarged carrier is

```text
Omega=Delta times {0,...,255}.                             (2)
```

On `Omega`, define the joint probability density

```text
pi(dw,r)=Z_hyb^-1 exp(-beta V(w)) a_r(w)
          dlambda_Delta(w),                               (3)
pi(r|w)=a_r(w)/A_m(w).                                    (4)
```

Strict positivity of `epsilon` makes every detector sector and every jump
available even on a boundary face. A simultaneous permutation of the simplex
coordinates and detector labels preserves (1)--(4), so the construction is
`S_256`-equivariant. In particular, the unconditional detector marginal is
uniform:

```text
pi(R=r)=1/256.                                             (5)
```

Equation (5) does not select a preferred branch. Information appears only in
the correlation between `W` and `R`.

## 2. Reversible diffusion-jump generator

For a function `f=(f_r)` on the hybrid carrier, let the continuous part in
sector `r` be the normally reflected gradient diffusion for

```text
U_r(w)=V(w)-(1/beta)log a_r(w).                            (6)
```

Its tangent drift is

```text
-grad_T U_r
  =-grad_T V+(m/beta) Pi e_r/(epsilon+w_r),                (7)
```

with covariance `(2/beta)Pi` and the same normal zero-flux boundary form as
K113. Couple the detector sectors by

```text
q_(r->s)(w)=c a_s(w),       s != r.                        (8)
```

The complete generator is

```text
Gf(w,r)=< -grad_T U_r, grad_T f_r >
        +(1/beta)Delta_T f_r
        +sum_(s!=r) q_(r->s)(w)(f_s-f_r).                 (9)
```

The continuous part is reversible against its sector density from (3). The
jump part obeys the pointwise identity

```text
pi_r(w) q_(r->s)(w)
 =Z_hyb^-1 exp(-beta V(w)) c a_r(w)a_s(w)
 =pi_s(w) q_(s->r)(w).                                   (10)
```

Thus (9) is reversible and stationary for (3). The construction owns its
finite-dimensional energy, covariance, reflection and jump rates. The
constant `c` is only an imported clock/barrier factor. Nothing here derives a
physical temperature, detector medium or fluctuation-dissipation relation
from GU.

## 3. The detector record has finite joint energy

The symmetric Dirichlet form is

```text
E(f,f)= (1/beta) sum_r integral pi_r |grad_T f_r|^2
       +(1/2) sum_(r!=s) integral pi_r c a_s (f_s-f_r)^2. (11)
```

For a fixed label `j`, define the sharp detector observable

```text
g_j(w,r)=1 if r=j, and 0 otherwise.                        (12)
```

Unlike K113's `1_{argmax(w)=j}`, equation (12) has zero continuous gradient.
Its jump contribution in (11) is finite because `Delta` is compact and every
score is bounded:

```text
epsilon^m <= a_s(w) <= (epsilon+1)^m.                      (13)
```

Therefore `g_j` belongs to the hybrid finite-energy domain. A continuous path
of `W_t` may cross any wall `w_i=w_j` without changing `R_t`; the detector
label changes only at a jump time of the finite-rate chain. The state-space
enlargement closes K113's analytic record-domain obstruction.

It does not make one branch permanent. The holding rate in detector sector
`r` is

```text
lambda_r(w)=c sum_(s!=r) a_s(w),                           (14)
c*255*epsilon^m <= lambda_r(w)
                 <= c*255*(epsilon+1)^m.                  (15)
```

Conditional on a base path, the no-jump probability over `[0,t]` is
`exp(-integral_0^t lambda_r(W_u)du)`. It is strictly between the bounds from
(15) for finite positive parameters. The record persists through base-wall
crossings, but it is not an absorbing superselection label.

## 4. Exact readout and retention frontier

At the K111 vacuum `w^(j)`, with `epsilon=1/257`, one coordinate is `2/257`
and the other 255 are `1/257`. Equation (4) gives

```text
Pr(R=j|w^(j)) = 3^m/(3^m+255*2^m),                        (16)
Pr(R=s|w^(j)) = 2^m/(3^m+255*2^m), s!=j.                 (17)
```

For every finite `m`, the error

```text
P_err=255*2^m/(3^m+255*2^m)                               (18)
```

is strictly positive. The certificate uses `m=16`, where the correct-record
probability is exactly

```text
3^16/(3^16+255*2^16).                                     (19)
```

The contrast can approach a perfect record only in the singular `m ->
infinity` limit. At finite parameters the detector alphabet has eight
available bits, but the joint law does not carry eight perfect bits about the
base branch.

The kinetic factor `c` cancels from (4), (16) and (17). Reducing `c` makes
records persist longer but does not improve their stationary accuracy.
Increasing `m` improves the vacuum score contrast, but it strengthens the
record-conditioned drift in (7) and generally changes the base equilibrium.
Retention and readout are therefore distinct imported controls.

## 5. Exact backreaction boundary

Summing (3) over detector labels gives

```text
pi_W(dw) proportional to exp(-beta V(w)) A_m(w)
                     dlambda_Delta(w).                     (20)
```

For `m=1`,

```text
A_1(w)=sum_r(epsilon+w_r)=256 epsilon+1,                   (21)
```

so the unconditional base marginal is exactly K113's Gibbs law even though
each record-conditioned drift contains the nonzero term in (7). For `m>1`,
`A_m` is nonconstant on the simplex and the base Gibbs marginal is reweighted.
The more accurate `m=16` certificate therefore does not preserve the K113 base
law.

There is also a direct no-go inside this reversible gradient class. Requiring
the continuous drift in every detector sector to remain exactly K113's drift
forces

```text
grad_T log a_r(w)=0 for every r and w.                     (22)
```

Connectedness of `Delta` makes each `a_r` constant. Equivariance makes the 256
constants equal, so (4) becomes state-independent and uniform. Hence an
informative reversible detector cannot be non-invasive record by record in
this class.

This is not a universal measurement no-go. A driven one-way detector, a
nonequilibrium environment, degenerate or state-dependent noise, an absorbing
memory, or a larger field-theoretic apparatus may evade (22). Each escape is a
new dynamical owner and must separately satisfy causal, domain and observable
descent.

## 6. Branch interface and exact ceiling

Detector-center evaluation `R=r` names the existing K110 projector `P_r` and
the corresponding K91 action/domain/Green retract. Because a base tie-wall
crossing does not change `R`, the named retract is stable through that
continuous crossing. A later finite-rate jump changes the named retract.
Thus the hybrid center supplies a regular finite-energy branch label, not an
invariant branch sector for all time.

The result is finite-dimensional and classical. Normal reflection is not a
BV-BFV boundary condition; the detector center is not a local spacetime
observable net; classical Gibbs conditioning is not a Born derivation; and
the conditional logarithmic score is not an authenticated source/GU action.
The delayed-choice holdout remains unscored.

## Inline postflight bookend

- **Strongest overclaim:** “K114 derives a physical measurement that solves
  K113.” Refused. It constructs a finite-energy detector coordinate only after
  importing a hybrid carrier, score, clock and reversible coupling.
- **Strongest contrary construction:** a one-way nonequilibrium detector may
  read the unchanged K113 process without record-conditioned backreaction.
  That route is not excluded; it must own its driven environment, stationary
  or operational law, dissipation and causal domain.
- **Strongest mistyping risk:** using the unchanged `m=1` base marginal to call
  the detector non-invasive. Refused. Record-conditioned drift still changes,
  and higher score contrast reweights even the marginal.
- **Weakest reproducibility seam:** simulation can mistake long holding times
  for permanent records and high `m` for zero error. The exact certificate
  checks positive holding-rate bounds and the strictly positive rational error
  before any numerical interpretation.

The certificate runs a clean exact baseline before every hostile mutation.
No source/GU stochastic action, physical environment, measurement or collapse,
spacetime causal BV-BFV quotient, Born derivation, held-out score, prediction,
confirmation, canon, paper or public posture moves.

## Reproduction

```bash
python3 tests/channel-swings/k114_k113_hybrid_detector_finite_energy_record_probe.py
python3 tests/channel-swings/k114_k113_hybrid_detector_finite_energy_record_probe.py --selftest
```
