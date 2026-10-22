---
title: "K1932: Nondegenerate thermal baths can escape the half-return floor"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit finite channel constructions, not a global optimum or native GU result
scripts:
  - tests/channel-swings/k1932_four_level_bath_catalyst_return.py
  - tests/channel-swings/k1932_four_level_bath_catalyst_return_probe.py
---

# K1932: Nondegenerate thermal baths can escape the half-return floor

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact finite thermal-channel construction and uniform marginal-return formula
carrier: four-state system and two finite nondegenerate equally spaced registers LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and half trace distance ON=product_input
real_structure: complex adjoint, diagonal initial bath and catalyst
grading: additive energy shells, not chirality
action_owner: repository-construction -- controlled energy-conserving unitaries
target: supplied extreme Schur channel MAP-TYPE=intertwiner
```

## 1. Question and result

[K1930](k1930-energy-shell-catalyst-disturbance-2026-10-22.md) proves a sharp
worst-case marginal catalyst disturbance of at least1/2 for an exact supplied
extreme rank-two channel when the thermal bath has two or three levels and the
catalyst spectrum is nondegenerate. Does occupying rank-two energy shells
actually escape that obstruction?

**Yes.** Four thermal levels suffice for an exact counterarchitecture.
Moreover, a sequence of finite baths and catalysts, both nondegenerate and
with the SAME fixed positive spacing Delta, realizes the full channel exactly
while the catalyst's worst-case marginal return distance tends to zero.
The bath and catalyst dimensions, bandwidths and preparation resources grow;
this is neither a fixed-bath vanishing-return theorem nor free repeatability.
Section5 further proves the exact four-level optimum for the fixed uniform
preparation, improving the first finite example to7/20.

Take v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2 and
C_jk=<v_k,v_j>. The four projectors span Hermitian(2). The target is
Phi_C(|j><k|)=C_jk |j><k|. H_S is any diagonal Hamiltonian.
For integers l>=1 and N>=l, put m=4l and d=2N+2m-3. Let

    H_B=Delta diag(0,...,m-1), tau_B(b)=t^b/Z_B,
    H_A=Delta diag(0,...,d-1), t=exp(-beta Delta) in(0,1),
    S={m-1,m+1,...,m+2N-3}, sigma_A=P_S/N.

Both spectra are nondegenerate. Initial S,B,A are independent. No pure flag,
extra register, reset, battery or measurement is available implicitly.
There are exact conserving unitaries with

    r = sup_rhoS (1/2)||sigma'_A(rhoS)-sigma_A||_1
      = t^(2l)/(1+t^(2l))
        + (1/N) sum_(a=0)^(l-1) [(t^(2a)+t^(2a+1))/Z_B](a+1/2).       (1)

For m=4 this is r=t^2/(1+t^2)+1/[2N(1+t^2)]. For t=1/2,N=2,d=9,
r=2/5. This is a strict escape from1/2 with a faithful thermal bath and exact
conservation. Equation(1) is the return of this protocol, not an optimum over
all possible protocols or preparations.

## 2. Explicit shell unitaries

Use units Delta=1 for indices. Every occupied environment input (b,n), n in S,
has energy E=b+n in[m-1,d-1]. Its energy shell therefore contains ALL m
vectors |b,E-b>, b=0,...,m-1. The margins are part of the construction.
Let e=(E-1) mod2. Odd catalyst input levels correspond to b=e+2a,
a=0,...,2l-1. Some are outside S and unoccupied; define their maps too.

Put W=2^(-1/2)[[1,1],[1,-1]]. For each j, assign the input column b=e+2a
to Wv_j in the following ordered output pair:

    a<l:    (e+4a, e+4a+2),
    a=l+k:  (1-e+4k, 1-e+4k+2), k=0,...,l-1.                       (2)

All indices lie between0 and m-1. Pairs are disjoint and cover the shell.
The first group has odd A output levels, the second even levels. Each unused
input column 1-e+2a is mapped to the orthogonal complement
(-conjugate(x_1),conjugate(x_0)) in its assigned pair, where x=Wv_j.
Thus all m columns form an orthonormal basis. This is a full unitary U_j,E,
including unoccupied input directions. Set U_j to the direct sum of these
unitaries on full shells and identity on partial shells (which have no input
weight), and U=sum_j |j><j| tensor U_j.

Each output stays at energy E, so [U,H_S+H_B+H_A]=0. For EVERY occupied
input column alpha, the vectors U_j alpha share the Gram matrix
<v_k,v_j>. Consequently

    Tr(U_j (tau_B tensor sigma_A) U_k*)=C_jk.

Every matrix unit is correct; linearity gives the full channel and its action
on entangled inputs. There is no inference from only populations or one prior.
Virtual odd columns outside S only complete the unitary; they are not an
extra prepared resource.

## 3. Exact marginal return

The squared coefficients of Wv_j are (c_j,1-c_j), with
c=(1/2,1/2,1,1/2). Different output bath labels eliminate cross terms on
tracing B, so the catalyst outputs are diagonal. For low bath index
b=e+2a<2l, the catalyst shifts n to n-2a or n-2a-2. For a uniform block of
N odd sites, these lose fractions a/N and(a+1)/N from S. The condition
N>=l ensures neither exceeds1. The weight of this pair of bath indices is
w_a=(t^(2a)+t^(2a+1))/Z_B.

Every high bath index b>=2l maps to an EVEN A level, outside S. Their total
probability is p_H=t^(2l)/(1+t^(2l)). Every final probability inside S is at
most its original1/N: each low-bath branch is a shifted uniform block with
nonnegative weights whose total is at most1. Therefore half trace distance
is exactly the mass outside S, not merely lower-bounded by it:

    r_j=p_H+(1/N) sum_a w_a(a+1-c_j).

Tracing S removes control cross terms for arbitrary rho_S. Convexity bounds
the distance by max_j r_j, and a basis input attains that maximum. It is
attained by j1,j2,j4, proving(1). A reference does not change this marginal
statement. Final correlations with S or B ARE allowed; no product catalyst
return is asserted. Initial preparation is diagonal; no coherent-state
optimizer is asserted.

## 4. Growing bath, resource cost and limits

Writing u=t^2 and bounding the finite weighted sum by the full geometric mean
shows

    r <= t^(2l) + [t^2/(1-t^2)+1/2]/N.                              (3)

For ANY fixed beta Delta>0, choose l and N>=l tending to infinity; both
terms vanish. For desired error rho>0, sufficient choices are
l>=log(2/rho)/(2 beta Delta) and
N>=max(l,2[t^2/(1-t^2)+1/2]/rho), rounded upward.
This is an explicit finite-dimensional existence/resource bound, not a
minimal cost or optimal rate. m=4l grows logarithmically and d=2N+8l-3 grows
as the specified1/rho upper construction. The full channel error is ZERO.

The catalyst's mean energy and preparation relative entropy are exactly

    E_A=Delta(m+N-2),
    D(sigma_A||tau_A)=beta Delta(m+N-2)-log N+log Z_A,
    Z_A=sum_(n=0)^(d-1) t^n.                                      (4)

Its excess free energy is D/beta. Thus the displayed small-return limit
uses unbounded energy and preparation cost; the trace-distance accuracy
alone does not price this protocol. Bath bandwidth is(m-1)Delta and catalyst
bandwidth is(d-1)Delta. This is not a thermodynamic preparation algorithm,
total work accounting, local-control synthesis or runtime bound.

The finite matrix check includes m=8: t=1/2,N=4 gives19/85, and N=10 gives
53/425. At fixed l the protocol approaches the strictly positive p_H;
letting N grow alone does NOT prove vanishing return at fixed bath. Section5 gives a matching four-level lower bound for the FIXED uniform
preparation; no lower bound optimized over all preparations is asserted. Zero temperature, exact zero gap,
and t=1 are different limiting models and are not silently included.
At t=1 fixed l this family approaches1/2, consistent with loss of thermal
bias. For m=2 or3 the occupied-shell rank-one theorem still applies.

## 5. Follow-through: sharp four-level return for this preparation

The unrefined4l protocol deliberately treats all full shells alike. At m=4,
its virtual unoccupied columns leave an avoidable boundary loss. At shells
with exactly one ACTUAL occupied input column b, replace the generic map by
Wv_j on the pair(b,b xor1), with b first, and its orthogonal complement;
leave the other two columns fixed. This is still a full conserving unitary.
It retains catalyst support probability c_j on both the lower and upper
boundary shells. Keep the earlier construction on rank-two occupied shells.

For the SAME uniform sigma on S and the SAME nondegenerate Hamiltonians,

    r_min(sigma) = p_H + (1/2-p_H)/N,   p_H=t^2/(1+t^2).             (5)

Here the minimum is over ALL exactly conserving joint unitaries realizing
the target, including those not globally controlled on unoccupied inputs.
It is NOT a minimization over preparations, Hamiltonians or bath sizes.
In particular t=1/2,N=2 improves2/5 to7/20; N=1 gives1/2 and N=6 gives1/4.
For every finite positive temperature and N>1, this is strictly below1/2.

**Achievability.** Interior shells lose all of their high-bath input weight,
a total p_H(N-1)/N. The boundary shells together have input weight1/N and
lose fraction1-c_j. Thus
r_j=p_H(N-1)/N+(1-c_j)/N. Direct transport shows no A probability in S
exceeds its original1/N. At the top site the formerly missing high-bath
contribution adds c_j p_H/N to c_j p_L/N, at most1/N; other sites retain
this property. The support measurement is again exactly the trace distance.
Maximizing over j gives(5), with all input coherences removed by tracing S.

**Matching lower bound.** K1923's extreme-Gram dilation argument implies
that on each occupied shell, the environment output for the equal j1/j2
prior has eigenvalues lambda_a/2, each repeated twice, where lambda_a are
that shell's initial positive eigenvalues. Indeed exact population
preservation restricts populated inputs to their original system labels;
extremality gives a common isometry from v_j tensor the input-support label.
The two orthogonal v1,v2 then give those repeated eigenvalues. This statement
does not presume our selected unitary or an equal-weight shell.

On a boundary shell P=I_B tensor P_S has rank1, so the Ky Fan eigenvalue
bound retains at most lambda/2. On each interior shell P has rank2 and its
two input eigenvalues are lambda_low=p_b/N and lambda_high=p_(b+2)/N,
with b=0 or1; lambda_low>lambda_high. The largest two output eigenvalues
sum to lambda_low, so escaped probability is at least lambda_high.
Summing gives at least1/(2N)+p_H(N-1)/N, exactly(5). This physical catalyst
support measurement lower-bounds return already at the fixed rho12 input.
No unsupported componentwise approximation or optimizer over coherences is
used: initial sigma is explicitly fixed. Unequal/coherent preparations,
other support patterns and approximate channels remain separate questions.

## 6. Scope and adversarial checks

This construction tests an actual escape, not only the necessary shell-rank
condition from K1930. Occupied rank-two shells appear for m=4,N>=2; edge
occupation is handled by full-shell margins, rather than omitted. A wrong
complex target phase changes the channel, pairing both inputs into the same
output pair destroys unitarity, and altered thermal weights change the
normalization/resource formula. Those actual input faults are rejected.
The matching1/2 construction and obstruction at bath size2/3 are retained.

[K1928](k1928-uniform-catalytic-channel-embezzling-2026-10-22.md) already
constructs small return with zero-energy degenerate registers. The present
construction fixes a positive spacing and prices both finite spectra. Known
prior work includes [Ng et al., Limits to catalysis](https://arxiv.org/abs/1405.3039)
and [vom Ende, Which Bath-Hamiltonians Matter for Thermal Operations?](https://arxiv.org/abs/2207.11189).
These concern catalytic resource and bath constraints; no novelty or complete
literature survey is claimed. The proof here is explicit and independently
reconstructed internally, not expert acceptance or formal verification.

SC-META-53 remains UNCERTAIN and supplies none of the positive Hilbert,
Hamiltonian or observable inputs. LT-SM8,LT-GR6b,AC-F1, source claims and canon
remain unchanged. Native full20/K-C/domain/accessibility and finite-duration
scalar dual construction remain independent open alternatives.

## Reproduction

Run both frontmatter scripts with Python3 and SymPy1.14.0. The producer's
--write option refreshes its JSON. It passes1284 exact finite matrix/rational
controls; the independently written transport probe passes104 controls and
rejects4 mathematical input faults plus1 report and1 pin fault after a green
baseline. Universal l,N,t claims rely on sections2–4, not on enumeration.
An initially selected temporary interpreter lacked SymPy; the confirmed
existing interpreter was used before any mathematical baseline was claimed.
