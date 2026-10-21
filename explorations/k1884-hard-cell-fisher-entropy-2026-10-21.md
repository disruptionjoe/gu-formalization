---
title: "K1884: Effective entropy of the actual three Fisher well profiles"
status: active_research
doc_type: exploration
scripts:
  - tests/channel-swings/k1884_hard_cell_fisher_entropy.py
  - tests/channel-swings/k1884_hard_cell_fisher_entropy_probe.py
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: forward hard-cell and mixture entropy with explicit finite budgets; no reverse entropy, sharp rate, sextic gap or native GU identification
---

# K1884: Effective entropy of the actual three Fisher well profiles

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
result: effective forward entropy of hard conditional profiles and full Gaussian mixtures
carrier: real densities with raw moments2=1,4=k>3,6<=k²+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy and forward relative entropy ON=real_H1_square_roots
real_structure: nonnegative real probability densities
grading: nearest-root labels and positive small-slack scale
action_owner: repository-construction -- constrained Fisher functional
target: actual conditional profiles and differential entropy MAP-TYPE=evaluation
```

## 1. The theorem and its place among the earlier results

Use [K1882](k1882-effective-fisher-rescaled-transport-2026-10-21.md)'s
hypotheses and notation: k>3, A=k+1, delta>0, raw E X²=1, E X4=k,
E X6<=k²+delta, finite Fisher I=4 integral |(sqrt(p))'|², and a **proved**
upper bound delta I<=U. Put roots r=(0,+sqrt(k),-sqrt(k)),
a=(k,2k,2k), b_j=a_j A. Let C_j be their nearest-root cells, p_j=P(C_j),
and Q_j the law of (X-r_j)/sqrt(delta) conditional on C_j.
All logarithms are natural; relative entropy is KL(P||Q)=integral p log(p/q).

For clarity the reused constants are
```
e_loc=4sqrt(delta)/(3k), 0<h<=sqrt(k)/4,
epsilon=13h/(4sqrt(k)), tau=4e_loc²/h²,
E=U-A²+A²[(1-epsilon)^(-2)-1]
  +2A e_loc(1+sqrt(k))+4A k tau+40delta/h²,
Kcap=U+40delta/h²,
Splus=max(0,A-e_loc(1+sqrt(k))-2k tau),
D=1-(1-epsilon)² Splus²/Kcap,
B=E/(kA)²+16D/(9k²)+tau/(kA).
```
Their nonnegativity for valid U is proved in K1880/K1882, not imposed by
clipping an invalid energy estimate. Define
```
T=min(1,tau),
Cplus=max(exp(1),(3/2)sqrt(2pi U/(kA))),
Hstar=E/(2kA)+16A D/(9k)+T log(Cplus/T),                 (1)
```
with the last term zero at T=0. Then
```
sum_(j:p_j>0) p_j KL(Q_j || N(0,1/b_j)) <= Hstar.        (2)
```
Each positive-mass conditional cell has KL<=Hstar/p_j. Actual weights
are retained; neither mean zero nor equal outer masses is assumed.

K1882 bounds smooth localized entropy and hard-cell transport, while
explicitly leaving hard-cell entropy open. Its W2 theorem alone cannot
supply (2). K1867 proves entropy to a different, strongly log-concave quartic
optimizer near fourth moment3 from below. That theorem is not transferred
to the present three-well problem. The new step is a residual entropy bound
using Fisher control of the density height. This is independent probability
mathematics; no novelty, source-register, physics-ledger or canon claim.

## 2. Global Fisher controls the density height

For u=sqrt(p) in H1(R), u² is in W1,1 and tends to zero at both ends.
The identity
```
u(x)² = (1/2)[integral_(-infinity)^x (u²)'
             -integral_x^(infinity) (u²)']
       <= integral |u u'| <= ||u||_2 ||u'||_2
```
therefore gives ||p||_infinity<=sqrt(I)/2. Equivalently each globally
rescaled density f_j(y)=sqrt(delta)p(r_j+sqrt(delta)y) satisfies
```
f_j(y)<=M:=sqrt(U)/2.                                  (3)
```
The square root of the Laplace density is in H1 and saturates this
constant. No differentiability of a hard-cell truncation is used.

## 3. The remainder has finite, controlled forward entropy

Use the smooth cutoff subprobabilities u_j² from K1880, of masses m_j,
and their normalized rescaled laws nu_j. The actual cell splits as
```
p_j Q_j = m_j nu_j + r_j(y)dy,
t_j=integral r_j=p_j-m_j, 0<=r_j<=M, t=sum t_j<=T.
```
Here r_j denotes a residual density; r_j in root formulas elsewhere denotes
the root, distinguished by its argument. The residual can have jumps at
cell endpoints. Only its density height and moments are needed. K1882 proves
```
sum m_j KL(nu_j||gamma_j)<=E/(2kA),
sum integral y² r_j(y)dy <=16D/(9k²), gamma_j=N(0,1/b_j). (4)
```
The first uses Gaussian log-Sobolev only on the genuine global H1 cutoffs:
KL<=I_relative/(2b). A primary normalization is Bobkov--Gentil--Ledoux,
[equation1.1](https://www.math.univ-toulouse.fr/~ledoux/HamiltonJacobi.pdf),
whose standard Gaussian has rho=1; rescaling gives the displayed constant.
The theorem does not apply that form inequality to hard conditioning.

For t_j>0 the elementary Gaussian log-density formula and (3) give
```
t_j KL(r_j/t_j || gamma_j)
 <= t_j log[M sqrt(2pi/b_j)/t_j]
       +(b_j/2) integral y² r_j(y)dy.                    (5)
```
These integrals exist: the positive part of r log r is controlled by its
height, and comparison with a Gaussian using z log z-z+1>=0 bounds the
negative part by mass and second moment. Thus no unproved entropy
integrability is hidden in the split.

Use b_j<=2kA in the quadratic term of (5), obtaining 16AD/(9k).
Use b_j>=kA in its logarithmic normalization. The discrete entropy of the
three normalized residual masses t_j/t is at most log3, so the sum of
logarithmic terms is at most
```
t log[(3/2)sqrt(2pi U/(kA))/t].
```
Since Cplus>=exp(1), t log(Cplus/t) is increasing on 0<=t<=1.
It is therefore at most T log(Cplus/T). Convexity of relative entropy
gives
```
p_j KL(Q_j||gamma_j)
 <=m_j KL(nu_j||gamma_j)+t_j KL(r_j/t_j||gamma_j).
```
Zero masses contribute zero. Summing and using (4)-(5) proves (1)-(2).

## 4. An exact finite budget and rate

At k=4,delta=10^-12,U=25.002,h=10^-4, K1882's rational constants give
tau=1/22500. The bounds pi<22/7 and exp(1)<3 prove Cplus<5.
Moreover sum_(i=0)^25 12^i/i!>112500=5/tau, so log(5/tau)<12.
Consequently an entirely rational upper envelope is
```
Hstar <= E/40+(20/9)D+12tau <51/20000=0.00255.           (6)
```
For an even density, the known mass bounds p0>=2999999/4000000 and
p_+=p_->=999999/8000000 give central KL<0.0035 and each outer
KL<0.021. K1876's exact trial justifies the supplied U for the exact even
optimizer. Other densities must establish their own energy upper bound.

For fixed k, h=delta^(1/3) and U<=A²+eta with eta->0 yield
```
Hstar=O_k(eta+delta^(1/3)|log(delta)|).                   (7)
```
The same rate divided by a positive cell-mass lower bound controls that
conditional KL. This is a conservative upper rate, not claimed sharp.
It is not a fixed-delta modulus in I-I_star.

## 5. Mixtures, products and differential entropy

**Full actual-weight mixture.** Put G_p=sum p_j N(r_j,delta/b_j).
On label-coordinate space the reference chooses label j with mass p_j
and Gaussian coordinate gamma_j. The actual law has the same label mass
and coordinate Q_j. Its joint KL is exactly the left side of (2).
The map (j,y)->r_j+sqrt(delta)y and data processing therefore give
```
KL(p||G_p)<=Hstar.                                     (8)
```
No disjoint-support assumption is made for the reference Gaussians.

**Fixed weights for even densities.** Let G_even have weights
(1-1/k,1/(2k),1/(2k)). For even p the label divergence is the Bernoulli
KL of q=p_++p_- against 1/k. The elementary KL<=chi-squared inequality
and K1880's |q-1/k|<=e_loc(1+sqrt(k))/k prove
```
KL(p||G_even)<=Hstar+e_loc²(1+sqrt(k))²/(k-1).            (9)
```
The fixed-weight assertion is not extended to generic asymmetric
near-minimizers. For independent products, all these forward KL bounds
add. Independence is an input, not an inferred physical property.

**Differential entropy.** Write H_label=-sum p_j log p_j. Because the real
cells are disjoint, the change-of-variables identity is exact:
```
h(X)=H_label+(1/2)log(delta)+sum p_j h(Q_j).              (10)
```
All terms are finite by the height and second-moment argument above.
For any Q_j, Gaussian log density gives
```
h(Q_j)-h(gamma_j)
 =(b_j/2)[E_Qj Y²-1/b_j]-KL(Q_j||gamma_j).
```
If q_j=W2(Q_j,gamma_j), coupling and the L2 triangle inequality give
|E_Qj Y²-1/b_j|<=q_j(2/sqrt(b_j)+q_j).
K1882 proves sum p_j q_j²<=B. Cauchy-Schwarz and b_j<=2kA yield
```
|h(X)-[H_label+(1/2)log(delta)
                  +(1/2)sum p_j log(2pi exp(1)/b_j)]|
 <=Hstar+sqrt(2kA B)+kA B.                              (11)
```
The rational certificate bounds the right side of (11) by 0.077 for the
example in section4. This keeps actual cell weights, including vanishing cells. For the exact
even optimizer the known limiting weights give the explicit entropy law
```
h(p_delta)-(1/2)log(delta)
 -> (1/2)log[2pi exp(1) k/(k+1)]
       -((k-1)/k)log(k-1)+log(2)/(2k).                  (12)
```
This is differential entropy of the scalar distribution, not thermodynamic
or physical GU entropy.

## 6. Contrary controls, reproduction and limits

**Direction is essential.** Every hard cell is a proper interval or half
line, so gamma_j assigns positive mass outside it while Q_j is zero there.
Thus KL(gamma_j||Q_j)=infinity for every positive cell. This does not
assert that reverse KL to the full smooth mixture is always infinite.

**TV, W2 and second moments alone are insufficient.** For standard Gaussian
gamma set q_t=(1-t)gamma+t N(0,exp(-2/t²)). Then TV<=t, W2²<=t,
and second moments converge to1. The joint-label entropy identity gives
```
KL(q_t||gamma)>=t KL(N(0,exp(-2/t²))||gamma)-H_Bernoulli(t)
 >=1/t-t/2-H_Bernoulli(t) -> infinity.
```
This is a transfer countercontrol, not a moment-feasible competitor in the
three-well problem. It violates the uniform Fisher-derived height bound.

Run the producer and separate probe in tests/channel-swings. The producer
checks exact rational budgets and pins; the probe reconstructs the budget,
tests independent Laplace/Gaussian/finite-mixture controls, and distinguishes
actual mathematical coefficient faults from reporting and pin faults.
Finite checks supplement the continuum argument; they do not prove it.
The explicit argument makes the transfer available for separate mathematical
review; no external expert, proof assistant, independent acceptance or
novelty is claimed.

Hostile review targets entropy direction, hard-cell boundary jumps, rare
weights, residual concentration, assumed U, convex-mixture direction and
the difference between the Gaussian reference and the exact optimizer.
No sextic spectrum, optimizer-relative entropy, global multiwell
log-Sobolev constant or native GU identification follows. Those remain
separate questions with their own actual functional or spectral inputs.
