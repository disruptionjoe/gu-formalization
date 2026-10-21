---
title: "K1908: A finite-time witness for quantum Markov dephasing"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum dynamics; no GU identification or optimal full-channel distance claim
scripts:
  - tests/channel-swings/k1908_quantum_markov_phase_noise.py
  - tests/channel-swings/k1908_quantum_markov_phase_noise_probe.py
---

# K1908: A finite-time witness for quantum Markov dephasing

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
result: global phase witness, finite-time semigroup bound and finite Fourier phase law
carrier: four-dimensional positive logical density matrices and Schur channels LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and state expectation ON=conditional_target
real_structure: complex conjugation and CAR star; no native K/C identification
grading: finite occupation sectors and even fermion parity
action_owner: repository-construction -- supplied finite interactions or quantum channels
target: conditional coherence, causal implementation and memory demands MAP-TYPE=intertwiner
```

## Result and distinction

A time-homogeneous, population-fixing, CP-divisible semigroup need not be
a mixture of classical phase unitaries at each time. For the supplied
four-level system take

    L=diag(-1,1,0,-i), Hsystem=0,
    G_jk=l_j conjugate(l_k)-(|l_j|²+|l_k|²)/2,
    F_jk(t)=exp(t G_jk).                                    (1)

The phase witness below proves F(t) is outside every classical random-phase
mixture for every 0<t<1/12. At t=1/24 its expectation is at most-1/48,
where every classical phase law gives a nonnegative value. This supplies
a finite-time observable distinction, not merely an unavailable classical
Markov dilation. K1907 uses this coefficient geometry, rescaled and with a
diagonal Hamiltonian, as a CP-divisible approximation to K1903's endpoint;
nonclassical noise and divisibility are independent questions.

## A global inequality for arbitrary phase laws

For arbitrary complex unit phases z1,...,z4 define

    a=(z1+z2)/2, b=(z2-z1)/2,
    r=z3-a, s=z4-a+i b.

Then |a|²+|b|²=1 and Re(a conjugate(b))=0. The sharp inequality is

    |b|² <= 2(|r|²+|s|²).                                  (2)

Write c=|a|, d=|b|. A common phase makes a=c and b=+/-i d, so
|a-i b| is either c+d or |c-d|. Since c²+d²=1 and c,d>=0,
c+d>=1 and c+d-1<=1-|c-d|. Reverse triangle therefore gives

    |r|²+|s|² >= (1-c)²+(c+d-1)².

Set u=d/(1+c), in [0,1]; then c=(1-u²)/(1+u²), d=2u/(1+u²), and

    2[(1-c)²+(c+d-1)²]-d²
       =4u²(2u-1)²/(1+u²)² >=0.

The constant 2 is sharp: take z1=(3-4i)/5, z2=(3+4i)/5,
z3=z4=1. Then |b|²=16/25 and |r|²+|s|²=8/25. This includes the
zero and endpoint cases; no phase grid or distribution restriction is used.
The initially published conservative constant 6 remains valid, but is
superseded here by this exact extremal calculation. With row vectors

    bvec=(-1/2,1/2,0,0),
    R=[(-1/2,-1/2,1,0);
       (-(1+i)/2,(-1+i)/2,0,1)],
    W=2 R*R-bvec*bvec,                                    (3)

where stars mean conjugate transpose, (2) says z*Wz>=0. Consequently
Tr(W Cclass)>=0 for every classical phase correlation Cclass=E[zz*].
W is not claimed positive semidefinite on arbitrary quantum states.
It is a separating observable on the restricted classical phase set.

## Negative derivative upgraded to a certified finite interval

R annihilates both the all-ones vector and l=(-1,1,0,-i), whereas
bvec l=1. Thus

    Tr(W J)=0,             Tr(W G)=-1.                     (4)

The row/column norm terms in G vanish in this trace because W1=0.
For Re w<=0 the integral Taylor remainder obeys
|exp(tw)-1-tw|<=t²|w|²/2. Every G_jk has nonpositive real part, hence

    Tr(W F(t)) <= -t+B t²,
    B=(1/2) sum_jk |W_kj| |G_jk|²
     =11/2+4sqrt(2) <12.                          (5)

This proves the stated interval and the 1/24 margin. For a simple exact
upper bound use sqrt(2)<13/8, giving B<12.
The output of the normalized equal superposition is F(t)/4, so measuring
W gives expectation at most-1/192 at 1/24. The same input under classical
phase noise has nonnegative expectation. Since ||W||<=||W||F<6,
its trace distance (half trace norm) from every classical output is at least
1/2304. The bound is conservative, with no optimal robustness claim.
A depolarized classical phase mixture is still subject to (2); arbitrary
measurement noise needs a separate bound and is not silently covered.

## Known generator geometry, independently rederived in this case

For clarity about prior art, the line-or-circle criterion for one normal
Lindblad operator is an established result of Kümmerer and Maassen,
reviewed by Fagnola, Gough, Nurdin and Viola, *Mathematical Models of
Markovian Dephasing*,2019, section 5.1 and Theorem 29:
https://arxiv.org/abs/1811.11784v2 . The following argument specializes the
criterion; it is not a novelty claim or a claim about all quantum channels.

Project coefficients orthogonally off the all-ones vector using P.
For one Lindblad operator, PGP=(Pl)(Pl)* has rank1. A classical phase
Markov generator is a positive sum of jump terms Pz(Pz)* and diffusion
terms Pr(Pr)* with r real, plus a Hamiltonian term killed by P. Every
nonzero term must therefore lie on the same complex line. A diffusion
requires the spectral points l_j to be collinear in the complex plane.
A jump requires z_j=alpha+beta l_j with beta nonzero and |z_j|=1,
so the spectral points must lie on one circle. For(-1,1,0,-i), the first
three distinct points are collinear, excluding a circle, while the fourth
excludes a line. This matches the explicit finite-time obstruction above.
Positive controls: real l gives a Gaussian random phase; unit-modulus l
has generator G_jk=l_j conjugate(l_k)-1 and is exactly a Poisson random
unitary jump law. A complex coefficient or nonzero phase cycle alone
therefore does not exclude classical noise.

## The previous compound-Poisson channel is not adjudicated by its name

K1906 constructs exp[t(Phi_C-id)] for K1903's nonclassical collision
channel. That remains an exact CPTP semigroup. Nonclassicality of one
collision does not by itself establish nonclassicality of the Poisson
mixture. The present witness has initial derivative
Tr(W(C-J))=13/2-4sqrt(2)>0, so its small-time proof does not settle that
specific mixture. This is an explicitly inconclusive discriminator, not a
proof of classicality. The nonclassical endpoint established here uses(1).
The strongest useful resolved alternative is thus an explicit single-Lindblad
model with a rigorous observable interval, rather than an assertion about
the previously named Poisson model without a witness or representation.

## Released successor: an explicit late-time classical representation

For any four-mode correlation matrix D satisfying

    2 sum_{j<k}|D_jk| <=1,                                 (6)

let each z_j independently range over the three cube roots of unity and
assign the 81 vectors the probabilities

    p(z)=[1+2 Re sum_{j<k} D_jk conjugate(z_j) z_k]/81.        (7)

They are nonnegative by(6), sum to 1 and satisfy E[z_j conjugate(z_k)]=D_jk.
This follows from exact Fourier orthogonality on the finite phase group;
exponents in a product are at most 2 in magnitude, so a zero residue modulo 3
is a zero exponent. Diagonals follow from unit phases and normalization.
The 81-term construction can be collapsed by the redundant global phase,
but its size is no optimal history-count claim. It is an explicit random
unitary representation, not an inference from a failed witness.

For (1), the six off-diagonal magnitudes sum to

    exp(-2t)+2 exp(-t)+3 exp(-t/2).

At t=2log7 this is 1128/2401, so twice the sum is 2256/2401<1.
Every later time also satisfies(6). Thus the SAME semigroup has provably
nonclassical channels for 0<t<1/12 and explicit classical endpoint laws
for all t >=2log7. The intermediate interval is unclassified; no unique
transition, optimal threshold or classical process representation follows.
A family of endpoint phase laws need not assemble into one stationary-
independent-increment law or reproduce interventions across times.

For the earlier K1906 compound-Poisson model, each off-diagonal damping
rate is at least1-1/sqrt(2). Therefore(6) holds for

    t >= log12/(1-1/sqrt(2)).                               (8)

This resolves its late-time classicality constructively. Its shorter times
remain open; the positive derivative of the current witness supplies no
answer there. Conversely the explicit unitary-jump control is classical
at every time. These controls separate a nonclassical collision, a quantum
Markov generator, single-time nonclassicality, and a classical stochastic
process without conflating any pair.

## Review, reproducibility and ceiling

The strongest overclaim would be inferring a nonclassical endpoint solely
from a nonclassical dilation. Equation(2) and the finite-time remainder
remove that gap for the stated interval. The strongest contrary construction
is the unitary complex Poisson control, which is classical despite complex
coefficients. The weakest seam is a sign/conjugation error in the witness;
the independent probe computes the whole generator and trace directly, and
input mutations must fail real checks after a clean baseline. The analytic
proof carries arbitrary phase laws and all times in the interval. Numerical
values are illustrative; no external expert review or formal proof is claimed.

Carrier: supplied positive C4, ordinary complex conjugation, fixed population
basis and bounded logical observables; no microscopic local bath or energy
claim. SC-OP-04 ASSERTS candidate grammar, SC-MAS-01/SC-CHI-02 ASSERT the
stylized scalar toy, SC-META-53 remains UNCERTAIN. No full20/K/C/accessibility
bridge is inferred. LT-SM8, LT-GR6b, AC-F1 and all source, ledger and canon
verdicts stay unchanged. This is independent conditional quantum mathematics.
