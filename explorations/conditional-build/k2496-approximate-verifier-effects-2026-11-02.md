---
title: "K2496 Approximate verifier-effect calibration controls full records"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional finite-dimensional full-memory process mathematics; no measured calibration or native GU quotient"
---

# K2496 Approximate verifier-effect calibration controls full records

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
result: K2496
carrier: original rank10/rank12 projectors on C108 with arbitrary finite retained storage memory and untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and operator norm ON=declared_carrier
real_structure: complex adjoint
grading: original P/plane/A/B/N reducing sectors and classical measurement records
action_owner: repository-construction -- supplied positive quantum instruments and exogenous flags
target: approximate effect preservation to finite-record/reference error and postselection/cost bounds MAP-TYPE=evaluation
```

## Result and boundary

Uniformly small dual errors on only the original two test effects imply a
linear error bound on the complete finite verification record and final target
bit, even with arbitrary retained storage memory and an untouched entangled
reference. This replaces the *assumed* full-channel proximity premise in
K2494's consumer with an explicit two-effect sufficient condition. It neither
constructs a calibrated apparatus nor says that reset-memory tomography is
enough to establish that uniform joint condition.

At gap j, history h, require a CPTP map Phi_j,h on H tensor E and

    ||Phi_j,h^*(Q tensor I_E)-Q tensor I_E|| <= epsilon_j,
    ||Phi_j,h^*(T tensor I_E)-T tensor I_E|| <= epsilon_j.       (1)

This is an operator-norm statement over the complete retained carrier, for
all reached histories; E may be arbitrarily large but finite. The actual
initial H/E/reference state may be entangled. Baseline Q/T tests, their
complements, adaptive record-based choices/stopping and the exogenous flag law
are unchanged. Flags may correlate across time but are independent of the
initial H/E/reference and are not altered by storage. No memory observation
or external feedback outside this stated interface is silently included.

For both original plane parameters r=27/127 and r=15/67, the output consisting
of the record, a final P/complement bit and the untouched reference differs
from the corresponding no-storage output by at most

    E_n = min(1,512 sum_{j=1}^{n-1} epsilon_j)                  (2)

in half trace norm. This is a bound on the reduced recorded output, after
tracing H and E, not on the full stored state. The constant is deliberately
coarse and is not claimed optimal. A sharper word-dependent bound and exact
zero-error theorem coexist with it.

Positive Hilbert space, projectors and process structure are supplied.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain the native physical
state/quotient/domain debts. Ledger0.263, source polarities, canon and physical
credit do not change. No hardware, external-expert, proof-assistant or novelty
claim is made.

## 1. Projection defect and a linear word bound

Suppress tensor identities. Choose a Stinespring isometry V for Phi and put
D_A=(A tensor I)V-VA and Delta_A=Phi^*(A)-A. For R=Q or T,

    D_R^*D_R = Delta_R-Delta_R R-R Delta_R.

In the R/(I-R) splitting this is block diagonal, with blocks
-R Delta_R R and (I-R)Delta_R(I-R). Positivity and (1) imply
||D_R||<=sqrt(epsilon), where epsilon=max of the two errors.
The apparent square root does not force a square-root observable error:

    Delta_AB = Delta_A B+A Delta_B+D_{A^*}^*D_B.              (3)

For a word W of length L in Q,T, contraction and a telescoping product give
||D_W||<=L sqrt(epsilon), and likewise for W^*. Induction in (3) then gives

    ||Delta_W|| <= L(L+1) epsilon/2.                         (4)

At epsilon=0 this recovers exact preservation of the generated algebra.
Equation (3) is an algebraic identity, not an invocation of an approximate
multiplicative-domain theorem with unstated constants.

The original target projector is

    P=(QTQTQ-r QTQ)/(1-r).

On P it equals one; on the principal plane QTQ=r Z, QTQTQ=r^2 Z;
on A/B/N both products vanish. Thus

    ||Delta_P|| <= (15+6r) epsilon/(1-r) <=22 epsilon.        (5)

The bound concerns target mass, not coherent output-state preservation.

## 2. From words to every effect in the original test algebra

K2494's exact algebra is C_P direct-sum M2 direct-sum C_A direct-sum C_B
 direct-sum C_N. Put d=1-r, c=sqrt(rd); on its plane use Z=|z><z|,
Y=|y><y| and U=|z><y|. Explicit polynomials are

    Z=(QTQ-QTQTQ)/(rd),
    Y=(TQT-QTQT-TQTQ+QTQTQ)/(rd),
    U=(QT-QTQ)/c.

From (4), the respective defect constants are

    C_P=(15+6r)/d, C_Z=21/(rd), C_Y=41/(rd), C_U=9/c.

For any effect X in the algebra, let p,a,b,n in [0,1] be its values on the
four scalar sectors, and [[x,z],[conjugate(z),y]] its plane block. Then

    X=nI+(a-n)Q+(b-n)T+(p-a-b+n)P
      +[x-a-r(b-n)]Z+[y-n-d(b-n)]Y
      +[z-c(b-n)]U+[conjugate(z)-c(b-n)]U^*.

The absolute coefficients are bounded, in order after I, by
1,1,2,1+r,1,1/2+c,1/2+c. The off-diagonal bound |z|<=1/2 follows from
0<=X<=I. Hence

    ||Phi^*(X)-X|| <= C(r) epsilon,
    C(r)=2+2C_P+(1+r)C_Z+C_Y+(1+2c)C_U.

For both original r, 1/5<=r<=1/4, rd>=4/25, 2/5<=c<=1/2, so

    C(r)<=2+44+(5/4)(525/4)+1025/4+45
          =8181/16 <512.                                  (6)

The same expansion works with operator-valued coefficients on an arbitrary
untouched reference. Scalar diagonal entries become positive contractions;
the off-diagonal reference block still has norm<=1/2. Indeed, for a positive
contraction F, its off-diagonal part is (F-JFJ)/2, with J=diag(I,-I), whose
norm is <=1/2 because F and JFJ are effects. All coefficient norm estimates
above survive. Since Phi does not act on the reference, (6) therefore bounds
the amplified restriction to the test algebra, independently of reference
and memory dimension. No assumption on their initial correlations is used.

## 3. Full records: no exponential history factor

Replace storage gaps by identities from last to first. At the gap being
replaced, all later gaps have already been removed. For any effect on the
final classical record/target bit/reference, backward evolution through the
remaining ideal Q/T instruments gives, on each current history, an effect in
the test algebra tensored with the reference algebra and I_E. This remains
true for adaptive choices and stopping, with stopped histories padded by
identities. The dual difference at the current gap is bounded by (6).
Past histories may have arbitrary actual joint states; their weights sum to
one, so the bound is epsilon_j C(r) with no factor for the number of words.
Sum the hybrids. Taking the supremum over final effects gives (2).

For correlated exogenous flags first fix the whole flag sequence, apply the
same bound, then average its unchanged law. Their temporal correlation does
not break the proof. Storage-controlled flags or flags initially correlated
with the stored state do not meet the stated model. Reference effects in this
argument are a tool for bounding the recorded output; the protocol itself
does not perform adaptive operations on that reference.

## 4. Contrary constructions and scaling

- Zero effect error does not preserve the full state: a unitary that swaps two
  A-sector basis states commutes with Q,T, but maps a stored basis state to an
  orthogonal state. Its half-diamond distance from identity is one. This does
  not disprove closeness to *some* transparent map: it is itself transparent.
- Testing only the target state is insufficient. A unitary fixing P and swapping
  a Q-only A vector with a T-only B vector gives zero Q/T expectation error on
  P, while it changes the Q acceptance of A from one to zero. Operator norm
  over H/E is an essential hypothesis, not a restatement of that calibration.
- Let Phi_eta=(1-eta)id+eta Ad_swap for that A/B swap. Both dual effect errors
  equal eta, and Q-record probability on A changes by exactly eta. Thus no
  universal o(epsilon) replacement of the linear order is possible.
- K2494's retained clock counterexample still invalidates isolated reset-memory
  tomography; (1) is imposed on the joint map with the clock retained. Its
  flag-flip counterexample also survives. These are reused, not new claims.
- Approximate preservation is not exact non-pumping: a P/A swap with probability
  epsilon has zero Q defect, T defect epsilon, and pumps epsilon target mass
  from A. The exact non-pumping conclusion has no zero-error-free extension.
- Rare postselection amplifies unnormalized errors. A uniform error bound that
  exceeds the ideal acceptance supplies no conditional certificate.

## 5. Postselection and paid restart consumer

If ideal all-pass acceptance is s0 and ideal accepted bad mass is b0, (2)
gives |s-s0|<=E_n and |b-b0|<=E_n. When s0>E_n,

    actual conditional error <= min(1,(b0+E_n)/(s0-E_n)).    (7)

For a desired tolerance tau, it suffices that

    E_n <= (tau*s0-b0)/(1+tau),

with positive right side and E_n<s0. For n-1 gaps of common error epsilon,
a sufficient calibration target is epsilon<= (tau*s0-b0)/[512(n-1)(1+tau)].
This translates an accepted-error goal into joint-effect tolerances; it does
not claim those tolerances have been measured or can be realized cheaply.
For s0=1/1000,b0=1/1000000,tau=1/50,n=3, the bound is
 epsilon<=19/1044480000. At epsilon=1/100000000, E_n=8/781250 and the
conditional bound is below1/50. The probe checks these rational quantities.

Let ideal one-attempt cost A0 include nonnegative preparation, test, storage
and reset charges; let c_j be a charge at a prefix whose distribution error is
E_j. The same event bound gives |A-A0|<=D=sum c_j E_j. Under independently
fresh restarts only, expected renewal cost A/s is bounded by

    (A0+D)/(s0-E_n).

Within-attempt success and cost need not be independent. Reusing correlated
memory across attempts does not establish the renewal law. For uniform (1)
with fixed positive epsilon, 512(n-1)epsilon grows while ideal acceptance may
decay; no asymptotic purification or infinite-cap validity is inferred.
A calibrated flag/restart interface and physical resource law remain separate.

## Evidence and next work

The paired probe checks the exact projection/word identity, all original-r
algebra polynomials, explicit retained-memory/reference channel fixtures,
linear-order and wrong-state-calibration controls, and rational postselection
and cost arithmetic. Finite tests support the written arbitrary-dimension
proof; their count is not a theorem count. Independent internal quantum review
and separate final-artifact review challenge the hypothesis and transfer.
No external-expert or proof-assistant certification is claimed.

Next: an actual full-memory calibration protocol or physical storage process
meeting (1), unchanged flags and independent restart with measured costs.
Improving 512 alone is less consequential unless it changes a specified
experimental tolerance. The original GU physical quotient remains unbuilt.

[Probe](../../tests/channel-swings/k2496_approximate_verifier_effects_probe.py),
[report](../../lab/process/k2496-approximate-verifier-effects.json),
[exact transparency and memory controls](k2494-memory-transparent-storage-2026-11-02.md).
Stinespring representation is standard; see
[Watrous, Theory of Quantum Information, lecture 5](https://cs.uwaterloo.ca/~watrous/TQI-notes/TQI-notes.05.pdf).
The proof here supplies the explicit finite-algebra constants; no novelty claim.
