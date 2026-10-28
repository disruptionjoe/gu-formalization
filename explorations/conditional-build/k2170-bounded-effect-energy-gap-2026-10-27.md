---
title: "K2170 Quantitative bounded-effect energy gap"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed positive free-field model and binary diagonal effects with reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2170_bounded_effect_energy_gap_probe.py
---

# K2170 Quantitative bounded-effect energy gap

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2170 quantitative Cauchy deficit, capped overlap envelope and certified energy bounds
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

The constraint0<=e_n<=1 supplies an explicit positive correction to
[K2168](k2168-finite-budget-moment-envelope-2026-10-27.md)'s moment energy bound,
uniform over every infinite binary effect at any fixed positive feasible contrast.
A shift-operator estimate turns the mismatch with a geometric sequence into an
energy cost. A further capped-geometric overlap optimization and a rational covering
certificate make the bound executable without cutting off occupations.

In the same fixture as K2168, the new results include

    contrast Delta >= 1/2  implies E > 0.54234444248,
    contrast Delta  = 1/2  implies E > 0.54324604.           (0)

The second statement uses a64-bin PROBABILITY partition, not an occupation truncation
or a sampled minimum. It is deliberately stated at exact contrast; no monotonicity
of the true optimized energy is assumed. The first is a proven threshold-uniform
bound and yields a genuine finite-budget exclusion.

The model is the supplied positive scalar Fock vacuum and photon-added signal,
binary diagonal effects with positive-root Kraus and one real squeeze per reported
outcome. K2162's hidden-Kraus reduction is reused. E means VACUUM OUTPUT FIELD ENERGY.
Arbitrary channels, an autonomous controller, clock, switching, preparation, record
and reset costs are not accounted for. SC-META-53 remains UNCERTAIN. LT-SM8/LT-GR6b,
source, ledger and canon do not change; no GU-positive physical quotient or source
realization follows. Layer0 is the declared toy Fock model, not the source Cl77 carrier.

## 1. The exact residual and its spectral gap

Use K2168 notation N>0,z=N/(N+1),p_n=(1-z)z^n. For the positively informative
click branch define

    a_n=sqrt(p_n e_n), w=sum a_n², M=sum n a_n²,
    T=sum(n+1)a_n a_(n+1), r²=M/(M+w),
    eta=sqrt(M(M+w))-T, g_n=sqrt(1-r²)r^n.

Positive contrast means M=N(w+Delta)>Nw, hence0<z<r²<1. Bounded effects give M<=N,
so the following weighted sums converge. Direct expansion proves

    2r eta = sum(n+1)(a_(n+1)-r a_n)².                    (1)

Let S be the BACKWARD unilateral shift on ell², B=S-rI. Since SS*=I,

    BB*=(1+r²)I-r(S+S*) >= (1-r)² I,
    ker B = span{g}.

The lower bound makes B surjective with closed range of B* equal to(ker B)^perp;
there B*B >= (1-r)² I. Equivalently use the polar decomposition on this complement.
The weighted sum in(1) dominates ||Ba||², yielding

    eta >= (1-r)²/(2r) [w-|<a,g>|²].                     (2)

Using the opposite shift or interchanging BB* and B*B on all of ell² would lose the
kernel and is invalid. The probe checks a finite interior block identity only; the
operator proof establishes the infinite-dimensional result.

## 2. Bounded tails force a positive deficit

For integer L>=1, a/sqrt(w) has tail mass at most u=z^L/w, whereas g has tail mass
v=r^(2L). When u<v, head/tail Cauchy and monotonicity of the binary fidelity give

    |<a,g>|/sqrt(w) <= h(u,v)
       =sqrt((1-u)(1-v))+sqrt(uv),
    eta >= w(1-r)²/(2r) [1-h(u,v)²].                    (3)

One can always choose L with u<v because r²>z. This already quantifies the strictness
that K2168 proved qualitatively.

For a bound uniform over the unknown w at fixed Delta, choose integer J>N with
z^J<Delta. Bounded e implies the exact tail estimate

    M-Jw <= sum_(n>J)(n-J)p_n = N z^J.

Thus a<=w<=b, where

    a=N(Delta-z^J)/(J-N)>0, b=1-Delta.

If a>b, the moment constraints themselves prove infeasibility. Otherwise define

    R_-=N/(N+1-Delta),
    R_+=(Na+N Delta)/((N+1)a+N Delta).

These bound r² since r² decreases with w. Pick L with U=z^L/a<V=R_-^L. Since U<V<=1,
replacing the actual tail bounds by U,V in(3) is conservative. Also

    1-h(U,V)² >= (V-U)²/[2(V+U-2UV)],
    (1-r)²/(2r) >= (1-r²)²/8.

The first follows by rationalizing sqrt(V(1-U))-sqrt(U(1-V)) and bounding the squared
sum denominator by twice the sum of its two squared terms. Therefore

    eta >= epsilon_Delta
      := a(1-R_+)²(V-U)²/[16(V+U-2UV)] > 0.              (4)

For rational inputs this bound uses only rational arithmetic, although the stronger
radical version(3) is available. No compact-attainment theorem is needed for this
uniform inequality before taking the infimum.

## 3. Turn the deficit into field energy and a threshold bound

With K2168's G,f,C,alpha,beta and q=(beta/alpha)^(1/4), the actual branch energy is

    F(x)=wG(M/w,x)+Cx eta.

Its unique positive minimizing squeeze satisfies

    (M+w/2) A'(x)=CT >=0,

so x>=q. The positive coercive x² and x^-2 terms ensure a minimizer exists. Since
G(mu,x)>=f(mu), the click contribution is at least w f(M/w)+Cq eta. The other
branch contributes its ordinary relaxed lower bound. Thus

    E_min(Delta) >= R_bound(Delta)+Cq epsilon_Delta.       (5)

The normalization uses eta=sqrt(M(M+w))-T; it is not the difference of a branch mean
and T. For unoptimized squeezes, energy is no smaller than the optimized value, so
the same lower bound applies.

This also yields a threshold result without asserting true-optimum monotonicity.
Fix delta>0 and use its J,L. For Delta>=delta, a(Delta) increases and R_-(Delta)
increases, while

    mu_max(Delta)=N+(J-N)Delta/(Delta-z^J)

and hence R_+(Delta) decrease. Formula(3) then gives the same epsilon_delta for
all feasible larger contrasts. K2168 proves R_bound increasing. Consequently every
such detector obeys E>=R_bound(delta)+Cq epsilon_delta.

## 4. Exact capped-geometric overlap envelope

A stronger bound in(2) uses the maximum overlap under ||a||²=w and0<=a_n<=sqrt(p_n),
DROPPING the fixed-M constraint. The exact maximizer is

    a_n=min(t g_n,sqrt(p_n)).

Indeed each expression g_n a_n-lambda a_n² is maximized pointwise by this clipped
value when lambda=1/(2t). Sum the inequalities and add lambda w; all sequences are
square summable and the overlap converges by Cauchy. Strict concavity gives uniqueness.
The norm is continuous, strictly increasing while below1, and thereafter saturated
at1. Thus0<w<1 uniquely selects t.

Because r²>z, capped coordinates form a tail n>=K, K>=1. Its norm and crossing give

    t²=(w-z^K)/(1-r^(2K)),
    t²(1-r²)r^(2K-2) <= (1-z)z^(K-1),
    t²(1-r²)r^(2K)   >= (1-z)z^K.

At a boundary either adjacent K describes the same sequence. The exact maximum is

    H_cap=t(1-r^(2K))
       +sqrt((1-z)(1-r²)) (r sqrt(z))^K/(1-r sqrt(z)).

In(2), replace |<a,g>| by H_cap. This is an exact overlap RELAXATION, not the detector
optimizer: the clipped sequence generally has the wrong M. It still supplies a
lower bound because it optimizes over a larger set. The numerical certificate below
uses the simpler rational tail bound, not an unproved inversion of this cap formula.

## 5. Certified consumers with every probability covered

Use N=1/3,m1=5,m_-1=5/9,m2=41,nu=3,C=40/3,alpha=41/6,beta=3/2.
For delta=1/2, choose J=1,a=1/8,b=1/2,R_-=2/5,R_+=5/8,L=6. Then
U=1/512,V=64/15625 and q>2/3, proved by (2/3)^4<9/41. Exactly,

    C(2/3) epsilon_delta = 5997601/806912000000.

Adding K2168's certified R_bound(1/2)>0.5423370097 proves the first inequality(0),
uniform for Delta>=1/2. A budget B<=0.54234444248 therefore cannot reach contrast1/2
or greater in this instrument class.

The stronger exact-contrast bound partitions every feasible w in[1/8,1/2] into64
adjacent rational intervals. On each[a_j,b_j], use R_-=r²(b_j),R_+=r²(a_j),
U=z^L/a_j and V=R_-^L in(4), maximizing its valid bound over integer L=1..18.
Separately K2168 strict convexity supplies a global supporting tangent to L_d(w)
at the interval midpoint. Exact interval evaluation encloses both tangent value
and slope, so its minimum over the entire interval is a rigorous lower bound.
Add C(2/3) times the local deficit, then take the minimum across all64 covered bins.
The JSON report records every endpoint, L, deficit, tangent and rational lower bound.
The result exceeds0.54324604 (display approximately0.5432460419584665).

No uncovered probability, tail cutoff, floating minimization or assumed optimal
profile enters. The stronger bound excludes an exact contrast of1/2 below that
energy; a threshold-uniform upgrade of the partition itself is not claimed.

## Controls, independent review and continuation

Run `python tests/channel-swings/k2170_bounded_effect_energy_gap_probe.py` in the
repository SymPy environment; `--write` regenerates the report. Controls include
weighted residual expansion, correct shift order, geometric zero-defect sequence,
exact threshold T=7/24, uniform rational margin, squeeze-root bound and capped-tail
sum/norm. Changed shift orientation, tail index, adjoint order, geometric tail,
squeeze lower bound and cap denominator produce genuine failed checks after a green
baseline. The64-bin certificate is exact rational interval evidence. Universal
operator/cap/energy arguments receive independent mathematical review; neither finite
controls nor report hashes substitute for those proofs.

K2162 already supplies full conic/grid tail certification in principle; it is reused,
not presented as new. Next integrate the cap-fidelity inequality into a sharper
certified finite-budget solve, or construct an actual stable autonomous instrument
with preparation/reset accounting. The latter must handle the noninvariant physical
smear span, common domain, clock and information destination. An isolated oscillator
can be squeezed by two positive-frequency quarter-period evolutions plus a half-period,
but externally switched control is not an autonomous implementation here. Field energy
cannot be promoted to reset cost without specifying the bath and work model.

No novelty, proof-assistant, external-expert, arbitrary-channel optimum, native GU
positivity or total thermodynamic cost is claimed. The actual finite-budget optimum
remains open beyond its already solved saturation and weak-budget limits.
