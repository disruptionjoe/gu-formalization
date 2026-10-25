---
title: "K2048: A characteristic phase current and its exact scattering constraints"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complex local PDE identities and conditional scattering constraints; no unrestricted global existence
scripts:
  - tests/channel-swings/k2048_characteristic_phase_current.py
  - tests/channel-swings/k2048_characteristic_phase_current_probe.py
---

# K2048: A characteristic phase current and its exact scattering constraints

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: a characteristic first integral, complete polynomial coupling criterion and phase-flat scattering gain law
carrier: two complex eigenlines of the real commuting K2038 graph in null coordinates LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Euclidean graph norm and local complex phase current ON=declared_graph
real_structure: real commuting fields represented by complex coordinates
grading: even polynomial interactions, not Grassmann parity
action_owner: repository-construction -- K2040 sextic on the K2038 action
target: local current and scattering constraints MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The actual complex sextic equations have
an exact phase current on each right characteristic. It constrains every
smooth scattering solution, including arbitrary phases. The identity extends
to a completely classified polynomial coupling family. It does not supply the
missing unrestricted large-data amplitude bound.

## 1. Exact current, including overlapping initial data

Use [K2046](k2046-large-data-characteristic-reduction-2026-10-25.md)'s fixed
classical system with u=x-t, v=x+t:

    z_v = i conjugate(z) w^4,
    w_u = -i z^2 conjugate(w)^3.

For C2 local solutions define J=Im(conjugate(z) z_u). No division by z is
involved, so the following identity includes zeros:

    J_v = 0.                                                (1)

Differentiate the first equation once in u and use the second:

    z_uv = i conjugate(z_u) w^4 + 4 |z|^2 z |w|^6.

In conjugate(z_v) z_u + conjugate(z) z_uv, the first two summands are
complex conjugates with the signs making their sum real; the last is
4 |z|^4 |w|^6, also real. This proves (1) exactly, without a phase-locked
assumption or numerical integration.

On the initial diagonal u=v=x, z0prime=z_u+z_v. Hence

    J(u) = Im(conjugate(z0) z0prime)
           - Re(z0^2 conjugate(w0)^4).                       (2)

The interaction term cannot be dropped. For locally constant z0=w0=1,
the first term is zero but J=-1. A flat Cauchy phase with overlapping fields
is not the same datum as a flat incoming free profile. The original full
Dirac carrier, physical source parity, independent-dual choice and observation
remain separate; none is selected by this two-eigenline identity.

## 2. Released classification of polynomial couplings

Consider the explicitly changed class

    z_v=i conjugate(z) F(w),
    w_u=-i z^2 G(conjugate(w)),                              (3)

where F and G are polynomials with constant complex coefficients. Direct
product differentiation, with no reality assumption on F or G, gives

    J_v=|z|^4 Im(Fprime(w) G(conjugate(w))).                 (4)

If F is constant, (1) holds for every G. If F is nonconstant, (1) holds for
all local solutions if and only if

    G(conjugate(w)) = lambda conjugate(Fprime(w)),
    lambda real.                                           (5)

Proof of necessity: arbitrary local field values are available to the
semilinear characteristic initial-value problem. Thus the polynomial in (4)
must be real for every complex w. Write Fprime=sum a_j w^j and
G=sum b_k conjugate(w)^k. Independence of the real-polynomial basis
w^j conjugate(w)^k implies

    a_j b_k = conjugate(a_k b_j) for every j,k.

Choose a_j nonzero. These equalities give b_k=lambda conjugate(a_k), with
lambda=conjugate(b_j)/a_j. The diagonal equality makes lambda real.
This also covers G=0. Conversely (5) makes the product lambda|Fprime|^2
real. This is a complete classification for this declared polynomial class,
not a classification of all PDEs or all norm-preserving interactions.
The actual sextic is F=w^4, G=conjugate(w)^3 and lambda=1/4.
An unmatched imaginary perturbation of G produces a nonzero current defect.

## 3. Exact scattering memory and phase restrictions

Condition now on a globally smooth solution with compact initial support.
[K2044](k2044-arbitrary-phase-characteristic-control-2026-10-25.md) and K2046
supply proven existence classes; global existence is not inferred from (1).
Each field's zero set propagates along its own characteristic, by uniqueness
of its locally Lipschitz real two-component ODE. Nonzero z cannot reach zero
in finite regular time, since backward uniqueness would then make the whole
ray zero. After the two transported supports separate, both forces vanish.
There are incoming and outgoing free right profiles Zin(u), Zout(u), and

    Im(conjugate(Zout) Zoutprime)
      = Im(conjugate(Zin) Zinprime) = J(u).                  (6)

On any interval where these profiles are nonzero, write Z=amplitude*exp(i theta).
Then |Zout|^2 theta_outprime = |Zin|^2 theta_inprime. In particular a
phase-flat incoming profile cannot acquire a spatially varying outgoing
phase on that interval, even though its amplitude and its overall phase may
change. The sign of a nonzero phase gradient is preserved at the same
characteristic label. This rejects arbitrary proposed scattering maps that
preserve only total norm; it does not assert identity scattering, a quantum
S-matrix, or complete integrability.

## 4. Released amplitude equation and monotone gain

Set a=|z|^2, b=|w|^2 and C=z^2 conjugate(w)^4. The same actual equations give

    a*a_uv-a_u*a_v = 4 J Re(C) + 8 a^3 b^3.                (7)

This polynomial identity holds even at zeros. Where a>0 it becomes

    (log a)_uv = 4 J Re(C)/a^2 + 8 a b^3.                 (8)

For zero-current incoming profiles, J=0 and the right side is nonnegative.
Choose fixed v_minus and v_plus outside the compact left-field characteristic
support. Integrating (8) across this finite rectangle gives the exact gain law

    d_u log(|Zout(u)|^2/|Zin(u)|^2)
       = 8 integral_[v_minus,v_plus] a(u,v) b(u,v)^3 dv >=0. (9)

Thus the outgoing-to-incoming density ratio is nondecreasing along each
nonzero incoming interval. It is strictly increasing at labels whose
interaction integral is positive. Equation (9), not sample profiles, is the
whole-domain argument. It permits arbitrarily large data whenever their
global solution is otherwise established. It is distinct from conserved norm
and from the constant-phase real-plane theorem.

For nonzero J, the extra term in (8) has no fixed sign. Even J=0 provides a
mixed-derivative sign, not an upper bound on amplitude. Therefore neither
(8) nor (9) closes the arbitrary-complex large-data continuation problem.
The next concrete analytic question is to combine this fixed characteristic
current with a coercive bound or another independent integral. Repeating the
phase-locked reciprocal barrier does not answer it.

## 5. Further consequence for the classified coupling family

For (3) with the matched polynomial (5), the same calculation yields

    a*a_uv-a_u*a_v = 4 J Re(z^2 conjugate(F(w)))
                    + 2 lambda a^3 |Fprime(w)|^2.          (10)

Assume F(0)=Fprime(0)=0, so each zero field stays zero on its own
characteristic and compact supports separate as before. For an otherwise
established global smooth compact solution with zero incoming current,

    d_u log(aout/ain)=2 lambda integral a|Fprime(w)|^2 dv.   (11)

The gain ratio is nondecreasing for lambda>=0 and nonincreasing for lambda<=0.
The zero multiplier makes it constant. This extends the scattering constraint
to the entire matched polynomial class under the stated support conditions.
It does not transfer K2046's norm conservation or existence theorem to that
class. Without F(0)=Fprime(0)=0 even the finite-interaction support argument
can fail. These are necessary hypotheses, not an omitted technicality.

## 6. Verification and limits

A symbolic producer proves (4), (1) for the actual quartic coupling, and (7).
A separate Gaussian-rational implementation differentiates eight admissible
complex jets, checks eight general first-jet defects eight full matched-polynomial amplitude jets and nine matched/unmatched
polynomial coefficient pairs; five actual coefficient faults fail after the
clean baseline. The general classification and scattering/gain conclusions
use the written algebra and conditional smooth-domain proofs, not those finite
fixtures. The imported arithmetic helpers do not execute predecessor tests.

Hostile review checked the missing Cauchy interaction term, nonzero-ray
uniqueness, zero sets, fixed characteristic labels and the failure of a mixed
sign to prove an amplitude bound. No earlier source or ledger verdict moves.
A literature search on characteristic integrals and nonlinear Dirac systems
did not establish a novelty verdict; a characteristic integral alone is not a
complete Darboux-integrability or global-solution theorem. This is same-author
internal verification, not external or proof-assistant acceptance.
