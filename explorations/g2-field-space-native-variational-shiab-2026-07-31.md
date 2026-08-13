---
title: "G2 field space and native variational Shiab: the action survives its compressed Euler formula"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: archived private execution record
specification: lab/specifications/g2-source-field-and-variational-shiab-packet-2026-07-31.md
certificate: lab/process/g2-native-variational-shiab-certificate.json
probe: tests/channel-swings/g2_native_variational_shiab_probe.py
grade: "G2 CONDITIONAL PASS WITH SOURCE-FORMULA CORRECTION. The selected native field graph and trace-adapted density-dual contraction are installed in a fourteen-form first-order action. The draft-style fixed-linear Upsilon simplification fails the native cyclic/Helmholtz gate, but the written action emits an exact slot-symmetrized Euler covector with a necessary two-input cubic map. No complete G3 variation, domain, vacuum, SM spectrum, index, count, or cosmological output is claimed."
canon_verdict_change: none
---

# G2 field space and native variational Shiab

## Result first

G2 produces a real construction rather than another missing-map diagnosis.

The field space is now frozen:

\[
B=A_{\rm LC}(\epsilon_{\rm red},g_{\rm DW}),
\qquad
T=A-B,
\]

where `A` is the free endpoint connection, `epsilon_red` is the varied moving
reduction, and `B` is a graph composite rather than a second independent
connection.

The native trace-adapted bosonic Shiab from RB1c is installed as

\[
\mathscr S_\epsilon^{\rm tr}:
\Omega^2(Y,\operatorname{ad}P)
\longrightarrow
\Omega^{13}(Y,\operatorname{ad}^*P).
\]

It has the correct exterior degree, native real form, right-quaternionic
structure, Krein reality, moving covariance, and a nonzero response on both
generic full-adjoint and scalar-curvature inputs.

The action

\[
I_1^{\rm var}
=\int_YT\wedge\mathscr S_\epsilon^{\rm tr}
\left(F_B+\frac12D_BT+\frac13q(T,T)\right)
+\frac{\kappa_1}{2}\int_YT\wedge\flat T
\]

is differentiable at the algebraic/bulk grade tested here. But its exact
Euler covector is not the draft's compressed expression

\[
\mathscr S_\epsilon^{\rm tr}(F_{B+T})+\kappa_1\flat T.
\]

The native contraction fails the cyclic identities needed for that shortcut.
What the action actually emits is

\[
\boxed{
E_T^{\rm var}
=\mathscr S_\epsilon^{\rm tr}(F_B)
+\frac12(L+L^!)T
+M_\epsilon(T,T)
+\kappa_1\flat T,
}

where `L=S_epsilon D_B` and `M_epsilon` is the two-input density-dual map
obtained by completely symmetrizing the cubic action over its three field
slots.

This is the important positive result: Eric's shortened field equation does
not work for the selected native map, but the geometry produced by the
written action does. We can continue with the exact Euler object rather than
abandoning the source-action route or pretending the failed identity passed.

## Plain English

The action contains a term with two copies of the field and another with
three copies. When the contraction has a special Chern--Simons cyclic
property, varying any copy gives the same answer. The two-copy term therefore
doubles and the three-copy term triples, which explains the factors `1/2`
and `1/3`. Everything collapses neatly into “apply Shiab to the full shifted
curvature.”

The native GU contraction is not that special. Moving the variation from one
slot to another changes the answer. That invalidates the neat collapse, but
not the action. The correct derivative is simply the average over all the
places the varied field can occur.

For the quadratic term this is the symmetric part of an operator. For the
cubic term it is a genuinely two-input source map. Both are canonical outputs
of the action; neither introduces a fitted coefficient.

## 1. Why this is not the old failed Shiab route

Three prior results matter:

1. The proved spinorial Shiab has the wrong input and output for the bosonic
   action slot.
2. A full-Spin map remaining in the same `Lambda2` adjoint sector is killed by
   exact central parity.
3. Moving into the full `Sp(32,32;H)` adjoint and multiplying by the native
   negative trace gamma creates a nonzero density-dual map, but its fixed-
   linear cyclic identity fails.

G2 uses result 3. It does not relabel result 1 and does not retry result 2.

The trace adapter is not an arbitrary observer vector. The DeWitt trace line
is canonical in the actual symmetric metric fibre and becomes negative only
after trace reversal:

```text
raw Frobenius fibre:   (7,3)
native DeWitt fibre:   (6,4)
native total space:    (9,5)
```

Under the full moving construction, the trace gamma, Hodge star, Clifford
soldering, Krein projection, and density move together.

## 2. Field-space decision

The selected branch treats the source-side `varpi` as the free endpoint
connection `A`. The “olive”/reference connection is

\[
B=A_{\rm LC}(\epsilon_{\rm red},g_{\rm DW}).
\]

Then `T=A-B` transforms homogeneously and

\[
F_A=F_B+D_BT+q(T,T)
\]

holds exactly.

This choice avoids two bad alternatives:

- varying `B` independently would add another connection equation that the
  source grammar does not own; and
- freezing `B` would violate the G1 patch and moving-reference laws.

The G2 exact fixture verifies the endpoint chain. At fixed `A`, moving `B`
forces `delta T=-delta B`; dropping that response changes the variation.
It also verifies that the independent-`B` derivative is generically nonzero,
so the policy is not harmless notation.

The `A0`-induced reductive connection remains a comparator. Adding it to the
selected action would introduce another continuous connection and destroy the
economy before the action had a chance to select it.

## 3. The native linear contraction

In compressed notation,

\[
\mathscr S_\epsilon^{\rm tr}(F)
=\kappa_{\mathfrak g}^{\flat}\pi_{\mathfrak{sp}}
\left[c(t_{\rm tr}(\epsilon))
\mathscr S_\epsilon^{\rm raw}(F)\right].
\]

The raw expression uses the moving one- and two-gamma soldering tensors and
the native `(9,5)` Hodge star. RB1c established that it is:

- nonzero on generic non-Riemannian full-adjoint curvature;
- nonzero on the scalar algebraic-Riemann plant after trace adaptation;
- degree-correct;
- Krein-real and right-`H`; and
- covariant when the full moving data move.

That is enough to install it in an action. It is not enough to assume its
Helmholtz identities.

## 4. The exact Euler geometry

Define the quadratic operator

\[
L=\mathscr S_\epsilon^{\rm tr}D_B.
\]

The term

\[
\frac12\int T\wedge L(T)
\]

varies to

\[
\frac12(L+L^!)T,
\]

including the Green flux defining `L^!`. It reduces to `L(T)` only if `L` is
formally self-adjoint on the declared domain.

For the cubic term define

\[
C(x,y,z)=\int x\wedge\mathscr S_\epsilon^{\rm tr}(q(y,z)).
\]

Let `C_sym` be its average over all six permutations and define
`M_epsilon` by

\[
\int x\wedge M_\epsilon(y,z)=C_{\rm sym}(x,y,z).
\]

Then

\[
\delta\left[\frac13C(T,T,T)\right]
=\int\delta T\wedge M_\epsilon(T,T).
\]

The coefficient `1/3` divides out the three field slots. It does not prove
that the slots were equal.

The G2 finite probe performs both calculations with exact rational matrices.
It uses Richardson elimination so the reported derivative is exact for the
cubic polynomial, not a numerical-tolerance coincidence.

## 5. Positive control and native-shaped failure

The probe includes two contraction classes.

### Chern--Simons control

With the invariant trace and identity contraction in a three-dimensional
transgression model, cyclicity holds. The exact derivative collapses to

\[
S(F_{B+T})+\kappa T.
\]

This proves the test can recognize the source's intended mechanism.

### Moving noncentral contraction

Insert a noncentral tensor that moves by conjugation with the reduction. The
action stays gauge covariant when that tensor moves, and its unsimplified
variation remains exact. But the compressed `S(F_{B+T})` derivative fails.
Freezing the insertion also breaks covariance.

This is the finite algebraic shape of the native trace/soldering contraction:
covariance does not imply cyclicity.

## 6. Why no repaired linear Shiab is reported

The complete cubic Euler response does not factor through a single polarized
curvature. The exact plant supplies `y,z` with

\[
q(y,z)=0
\]

but

\[
M_\epsilon(y,z)\ne0.
\]

A linear map of `q(y,z)` would have to vanish. Therefore the actual response
cannot be renamed `S(q(y,z))`. The two-input map is not optional bookkeeping;
it carries information erased by the curvature product.

This is also why tuning more left/right trace coefficients is the wrong next
move. RB1c's bounded four-order family already failed held out. The canonical
construction is the variational polarization, whose coefficients and slot
symmetry are fixed by the action.

## 7. Moving reduction and metric obligations

The selected contraction depends on

```text
epsilon_red -> B, T, t_trace, Phi1, Phi2, Clifford frame
g_DW        -> B, Hodge star, density, trace gamma, Krein dual
section     -> observation defect and pullback
```

Consequently G3 must include all these chain rules. In particular,

\[
\delta_\epsilon T=-\delta_\epsilon B
\]

and `delta_epsilon S_epsilon` is nonzero generically. The G2 plant explicitly
rejects omitting the moving-contraction response.

No claim of complete `E_epsilon` or metric stress is made here. The point of
G2 is that G3 now has a complete dependency graph and a correct `T`-Euler
seed rather than an ambiguous source slogan.

## 8. Datum and constraint surplus

G2 adds no new local direction: the trace line is native geometry and the
moving reduction was already a declared field.

It retains unresolved costs:

- the overall normalization relative to `kappa_1`;
- the global reduction component;
- boundary/domain data;
- the stationary orbit;
- the later Higgs/cosmological mode split; and
- P3 at its separate count/index equation.

The `1/2,1/3` coefficients are Eric-supplied guidance, not repo-derived
confirmation. Their new information here is that they normalize variational
slots even after the cyclic shortcut fails. Global constraint surplus remains
`UNCOMPUTABLE`.

## 9. G3 handoff

G3 must vary this corrected action, not the killed compressed equation. Its
minimum packet is:

1. all `A`, reduction, metric, section, spinor, and defect Euler forms;
2. the explicit two-input `M_epsilon` response;
3. the full Green/presymplectic potential and four-dimensional corner flux;
4. the coupled gauge and diffeomorphism Noether identities; and
5. the minimal BV master equation through antifield number one.

If G3 instead inserts `S(F_A)+kappa T` as the Euler covector, it silently
reintroduces the G2 failure.

## Validation and boundary

The new exact probe reports:

```text
G2-NATIVE-VARIATIONAL-SHIAB:
13 exact checks + 9 planted failures = 22 PASS
```

G1, RB1b, RB1c, RB2, and the guided council are regression dependencies.

G2 does not establish complete boundary differentiability, Noether/BV
closure, a selected domain or vacuum, N1/source equivalence, a Standard Model
Higgs, anomaly closure, index, observed generation count, cosmological
amplitude, or PP3.
