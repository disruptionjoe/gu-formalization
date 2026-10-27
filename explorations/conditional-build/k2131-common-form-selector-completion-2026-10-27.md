---
title: "K2131: Same-form completion of moving positive-sector dynamics"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied changed-contraction coefficient on the full carrier; selected-domain dynamics only, no full-carrier positivity or GU quotient
scripts:
  - tests/channel-swings/k2131_common_form_selector_completion_probe.py
---

# K2131: Same-form completion of moving positive-sector dynamics

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
result: explicit Hermitian interpolation and selected-domain extension
carrier: original Jc complex128 in raw complex1920 with moving positive32 Ptheta LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: original full H and SAME inherited current S=i Jc* H D0 Jc ON=declared_carrier
real_structure: complex adjoint; selector is not a source-selected real quotient
grading: Clifford and current sign distinct from ambient source halves
action_owner: repository-construction -- changed full coefficient, original principal injection and form
target: extend selected moving dynamics to an H-selfadjoint coefficient MAP-TYPE=intertwiner
```

## 1. What the raw obstruction does and does not exclude

K2126 excludes nonzero selected jets in the frozen raw upper contraction at P0;
K2129 proves smooth-selector rigidity for the entire fixed circle family. Neither says that the
same common H forbids every coefficient extension. Here an explicit extension
exists for EVERY angle and all real first derivatives, preserving Jc,D0,H
and the inherited selected current. It deliberately changes the upper raw
contraction. It is not source-selected and does not repair the full1920
principal dynamics, positivity or original mass coefficient.

## 2. Actual native Gram identity and global left inverse

Use J=Jc, F=J*HD0J=aT+bVZ with a=9/280,b=27/280,V=C1C2C3,
and P=Ptheta=exp(i theta Z/2) P0 exp(-i theta Z/2), as in K2120--K2124.
The actual Euclidean Gram G=J*J is diagonal, with eigenvalues121/980 and242/1225.
Exact original-coordinate calculation gives

    [G,T]=[G,Z]=0,    G+RGR=(1573/4900)I,
    PGP=dP,          d=1573/9800.                         (1)

For the all-angle deduction, Rtheta=Utheta R Utheta* anticommutes with G-dI
because G commutes with Utheta. Restricting to its +1 space makes G-dI compress
to zero. T commutes with both. No sampled-angle extrapolation enters (1).

Set X=JP, L=d^(-1)PJ*, so LX=P and XL is an orthogonal projection on im X.
This uses P directly and requires no choice of a32-column frame. In particular
it is smooth and periodic under theta->theta+2pi. Real source-selection and
observation constraints remain independent.

## 3. Compatibility and full Hermitian interpolation

For real mu,a_mu and theta_mu define

    Q_a=a0 I+sum Cj aj,     B_d=theta_t I+sum Cj theta_j,
    A=mu M+i Q_a-(i/2)Z B_d,
    Y=D0 J A P,            C=X*H Y=P F A P.                  (2)

The algebra from K2120 gives

    C=-i a mu P M P + a P Q_a P -(i b/2)P V B_d P=C*.       (3)

Indeed TP=-iP, PZP=0, [P,M]=[P,Cj]=0, M*=-M, V*=-V and
[V,B_d]=0. The mass's VZ term compresses to zero, while FZ's V term survives.
This is the original inherited form, not an independently chosen positive one.

Since H*=H and H^2=I, put

    Q=H Y L+L*Y*H-L*C L,        K=H Q.                    (4)

C=C* proves Q=Q*, hence HK=K*H. Also YP=Y, LX=P and Y*HX=C yield

    QX=HY+L*C-L*C=HY,        KX=Y.                      (5)

Thus KJP=D0JAP exactly. The range of Q lies in the sum of the two spaces
im(HY) and im(L*), each of dimension at most32, giving rank K<=64.
A necessary condition for ANY Hermitian extension is C=C*; (4) proves it is
sufficient here. This is standard finite-dimensional Hermitian interpolation
applied explicitly to the native matrices, with no novelty claim.

The subtraction in(4) is essential: dropping it preserves Hermiticity but
adds H L*C to KX. A real rather than imaginary coefficient on ZB_d generally
violates(3). These are actual algebraic failure controls.

## 4. Selected-domain and global consequences

Because the original principal intertwining is D_j J=D0 J Cj, a selected
section phi=Ptheta phi satisfies

    (D0 partial_t+D_j partial_j+K)J phi
      =D0 J(partial_t+Cj partial_j+A)phi.                  (6)

The sign of the gradient term in A is exactly the K2124 connection repair.
For smooth bounded potentials and bounded first theta derivatives, its selected
propagator and H1 domain are those of K2123/K2124, transported by Utheta.
This earns selected current conservation and finite speed under those same
assumptions. Equation(6) does not construct a well-posed full1920 Cauchy problem.
K depends algebraically on P and the first derivatives; no singular frame appears.
Circle winding leaves the same K2124 holonomy and transformed boundary condition.

If mu is included, this constructs a NEW full coefficient whose action on the
selected32 agrees with mu M. It can differ from K1967's supplied mass coefficient
on the complementary carrier. The original full mass adjoint defect remains a
true statement about that original coefficient. To keep that full coefficient
fixed would be an additional constraint not imposed here.

At a nonzero jet at P0, K cannot retain K2126's common-H raw upper contraction;
otherwise it would contradict that exact obstruction. Thus a southeast-only
change cannot implement(4). The existence result localizes the obstruction to
the contraction restriction rather than the common form, and eliminates an
unproductive search for a universal common-H no-go.

## Acceptance and next input

The probe reconstructs J,D0,H and all relevant128-matrix products from native
inputs. It checks the Gram identities, compatibility and factorized full-carrier
interpolation; the universal extension proof above establishes the unsampled
angles and derivative values. Finite controls do not certify a full PDE or
physical quotient. Independent internal review is required; no external or
proof-assistant certification or novelty is claimed.

Next ask whether any admissible changed upper contraction can be derived from
the source grammar or a specified observation/action, and whether a physically
selected positive family survives it. An arbitrary completed matrix alone is
not that derivation. SC-OP-04 ASSERTS candidate grammar; SC-OP-05 and SC-META-53
remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. Source register,
ledger0.263, LT-SM8/LT-GR6b and canon are unchanged.
