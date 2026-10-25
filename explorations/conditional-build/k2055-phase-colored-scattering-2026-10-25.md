---
title: "K2055: Arbitrarily large phase-colored collision trains"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite incoming phase-lattice packet trains and open scattering neighborhoods; unrestricted complex large data open
scripts:
  - tests/channel-swings/k2055_phase_colored_scattering.py
  - tests/channel-swings/k2055_phase_colored_scattering_probe.py
---

# K2055: Arbitrarily large phase-colored collision trains

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
result: arbitrary-size finite phase-colored collision trains and open complex scattering neighborhoods
carrier: two classical commuting complex fields on the real line LAYER=toy CHIRALITY=N/A
pairing: positive weighted classical charge ON=declared_two_field_system
real_structure: complex conjugation and packetwise fixed real lines
grading: opposite characteristic directions, not fermionic parity
action_owner: repository-construction -- K2050 positive even-power equations
target: global classical continuation and strong L2 scattering MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The same positive-coupling system

    z_v=i conjugate(z) w^(2m),
    w_u=-i gamma z^2 conjugate(w)^(2m-1),
    u=x-t, v=x+t, integer m>=2, gamma>0,

has arbitrary-size complete scattering solutions outside one global phase
plane and outside every direct K2052 ordered-overlap smallness test. The
construction uses a finite grid of differently phased incoming packets.
K2052 then supplies open neighborhoods allowing complex noncompact tails.
No unrestricted large-data theorem or physical fermionic claim follows.

Inherited results: [K2050](k2050-local-conservation-classification-2026-10-25.md)
proves single-plane continuation; [K2052](k2052-ordered-collision-scattering-basin-2026-10-25.md)
proves ordered-overlap bounds and openness around complete compact references.
The new input is the finite mixed-sign collision-tile construction below.

## Theorem: finite phase-colored incoming trains

Let the initial data be finitely many smooth compact packets with bounded derivatives. Within each field the enclosing packet intervals are pairwise disjoint with positive gaps. All enclosing z intervals lie strictly to the left of all enclosing w intervals. Each packet has the form

    z0_i(u)=exp(i theta_i) X_i(u),
    w0_j(v)=exp(i phi_j) Y_j(v),

where X_i,Y_j are REAL smooth compact functions; they need not be nonnegative and may have internal or accumulating zeros. Assume integers n_i,k_j and fixed phases theta0,phi0 satisfy

    theta_i=theta0+n_i*pi/2,
    phi_j=phi0+k_j*pi/(2m),
    2theta0-2m phi0=pi/2 modulo 2pi.

Then the solution exists smoothly for all real times, and has exact free incoming and outgoing profiles outside a finite collision interval. There is no amplitude/charge smallness condition. Its data admit an open L2 intersect Linfinity neighborhood, relative to smooth data with bounded derivatives, of global two-sided strong-L2 scattering solutions; those perturbations can have arbitrary varying phase and noncompact tails, by K2052.

This is not unrestricted complex completeness, an infinite-packet theorem, or a general Goursat theorem.

## 1. Tangency and support, using real amplitudes

On collision tile (i,j), set z=exp(i theta_i)X and w=exp(i phi_j)Y. Let sigma=sin(2theta_i-2m phi_j)=(-1)^(n_i-k_j). Direct substitution, using cos(2theta_i-2m phi_j)=0, gives

    X_v=sigma X Y^(2m),
    Y_u=gamma sigma X^2 Y^(2m-1).

These are real equations with locally Lipschitz polynomial forces. Thus the complex force is tangent to the specified fixed real lines; uniqueness preserves these lines. This statement includes zeros and negative X,Y. On a zero z ray, z stays zero by local real-two-component ODE uniqueness, and similarly for w rays. A nonzero ray cannot hit zero in a bounded regular interval by backward uniqueness.

Consequently each z support stays on its original u labels and each w support stays on its original v labels. The interaction support is a finite grid of rectangles, all within u<v because the trains are initially fully incoming. In the complement at least one field vanishes and its opposite force also vanishes. Backward evolution is free.

## 2. Correct incoming Goursat problem on one tile

Let a tile be u in [u_left,u_right], v in [v_bottom,v_top]. Set

    s=u_right-u in [0,S], r=v-v_bottom in [0,R].

The incoming right-moving amplitude X is prescribed on r=0; the incoming left-moving amplitude Y is prescribed on s=0. Their characteristic integral equations are

    X(s,r)=X_in(s)+ integral_0^r sigma X(s,r') Y(s,r')^(2m) dr',
    Y(s,r)=Y_in(r)- integral_0^s gamma sigma X(s',r)^2 Y(s',r)^(2m-1) ds'.

Each incoming trace is smooth and finite by previously completed tiles. Both packets vanish to all orders at their enclosing endpoints. In particular Y_in(0)=0 and the unique bottom trace obeys Y(s,0)=0. Likewise X(0,r)=0 at the right packet endpoint. Incoming traces may have internal zeros. Local existence on this rectangle follows by the usual contraction of these explicit integral equations on sufficiently small subrectangles. Compatible corner jets are inherited from previously solved/free regions; at the outer zero boundaries they also follow directly from the flat packet endpoints.

Do NOT replace this by arbitrary Goursat data: if Y(s,0) is nonzero and sigma=-1, the bottom characteristic could obey a superlinear growing ODE with independently prescribed X_in(s) and blow up. The packet-zero boundary is essential below.

## 3. Quantitative finite-tile bounds

Put a=X^2, b=Y^2, A=sup_s X_in(s)^2, B=sup_r Y_in(r)^2, L=sup_r |(Y_in(r)^2)'|. The equations are

    a_r=2 sigma a b^m,
    b_s=-2 gamma sigma a b^m.

Case sigma=+1:

    b<=B,
    a<=A exp(2 B^m R).

Case sigma=-1: a<=A. If B=0 the tile is free. Otherwise on each component where b_in(r)>0 set q=b^(1-m), q_in=b_in^(1-m), C=2 gamma(m-1). Direct differentiation gives

    q_s=-C a,
    q>=q_in-CAS,
    q_sr=4 gamma(m-1)a b^m=2(m-1)b_s,
    q_r=2(m-1)b+f(r),
    f=q_in'-2(m-1)b_in.

Choose explicit finite constants

    h=B^(1-m)/2,
    K=(m-1)L(h+CAS)^(m/(m-1))+2(m-1)B,
    epsilon=min(h,[(m-1)/(K+1)]^(m-1)).

At a putative point q=epsilon, q_in<=epsilon+CAS<=h+CAS. Also

    |q_in'|=(m-1)|b_in'|q_in^(m/(m-1)).

Therefore f>=-K and

    q_r>=2(m-1)epsilon^(-1/(m-1))-K>=K+2>0.

For fixed s, no downward crossing can occur as r increases. A component's finite left endpoint r0 is a zero of b_in, so q_in tends to infinity as r decreases to r0; the inequality q>=q_in-CAS prevents an entry below epsilon there. In particular the bottom r=0 is safe because its w trace is zero. The same argument works for every internal component, even accumulating ones. A zero b_in ray remains zero by uniqueness. Thus

    a<=A, b<=epsilon^(-1/(m-1))

throughout every partial local solution and then throughout the tile.

## 4. Smooth extension, causal grid and finite scattering

The preceding bounds control the actual real amplitudes |X| and |Y|, hence the complex amplitudes. Differentiate their characteristic integral equations: the highest derivatives enter linearly with bounded polynomial coefficients on each finite tile. Induct on derivative order, using the already bounded lower derivatives and a Gronwall estimate in the physical time coordinate (s+r)/2. This gives bounded derivatives through every finite partial tile. The local polynomial semilinear problem therefore extends to the closed tile. No division by the amplitudes is used in this derivative continuation step.

Index z intervals from right to left and w intervals from left to right. The tile (i,j) receives its z trace from (i,j-1) and its w trace from (i-1,j), with free initial traces on the first row/column. Order the tiles by i+j. There are finitely many; each inherits finite smooth input and the phase assigned to that packet. Across a zero gap the corresponding field is zero and the other is transported unchanged. Smoothness across endpoints follows from uniqueness and the transported flat endpoint jets, not from merely patching density solutions.

For t<0 the fields move apart and are free. For t greater than half the distance between the outermost initial supports all possible pairs have crossed and the supports are again disjoint, so the solution is exactly free. These facts prove two-sided classical completeness and exact compact scattering.

## 5. Explicit family beyond one plane and beyond every K2052 criterion

Choose one nonzero z bump f on [0,1] with theta=pi/4. Choose two nonzero w bumps g1 on [2,3], g2 on [4,5] with phases 0 and pi/(2m). Scale all three amplitudes by lambda>0. Then

    z0=lambda exp(i*pi/4)f,
    w0=lambda(g1+exp(i*pi/(2m))g2).

The z packet encounters sigma=+1 followed by sigma=-1. For m>=2 the two w phases are not equal modulo pi, so no single real phase line contains all w data. This does not belong to K2050's single fixed phase plane.

For the K2052 criterion, choose v in the first w bump with g1(v)!=0. Its A_k(u)>=a0(u) for every k>1. Thus

    eta_k >= 2 gamma(m-1) lambda^(2m)
             |g1(v)|^(2m-2) integral f(u)^2 du
           = c lambda^(2m), c>0,

uniformly for EVERY k>1. Choose lambda so c lambda^(2m)>=1. Since 1-k^(1-m)<1, no k satisfies K2052's direct ordered-overlap criterion. Nevertheless the finite-tile theorem proves this compact reference is complete. This is not a contradiction: K2052 explicitly treats its criterion as sufficient.

## 6. Open neighborhoods and topology

The completed reference has compact initial support in a common [l,r] and survives every finite interval. Choose T>(r-l)/2. The K2052 finite-time solution-map continuity in L2 intersect Linfinity sends sufficiently close smooth data to neighborhoods of outgoing separated data at +T and reflected outgoing separated data at -T. The ordered-overlap functional equals zero at both reference endpoint profiles and is continuous, so these neighborhoods satisfy its strict criterion. Gluing gives two-sided global smooth scattering for the perturbed data. The neighborhood is in the full intersection topology within the prescribed smooth class, not a restriction to the finite phase lattice or common support. K2052 also gives continuous asymptotic profiles. No quantitative universal perturbation radius or novelty certification is claimed.

## 7. Verification and adversarial limits

Exact Gaussian-rational controls substitute real signed amplitudes into the
actual complex force, including zero rays and mixed phases. Separate rational
jet checks verify coordinate signs, reciprocal derivatives, and safe barrier
constants; integer phase-lattice and topological-order checks test the finite
grid. Mathematical coefficient faults are rejected after a clean baseline.
These tests verify identities and fixtures. The written proof, not a time-step
simulation or a sampled trajectory, supplies smooth continuation, countable
zero handling inside each finite packet, all amplitudes, and openness.

Independent internal construction/review and the integrating proof review
checked the strongest contrary case: arbitrary Goursat input with a nonzero
bottom w trace can grow without this barrier. It is excluded explicitly, as
are infinite packet grids and nonlattice phases outside the perturbative open
neighborhood. The phase proof is on signed amplitudes, not densities alone.
The zero trace and finite tile ordering are indispensable. No source verdict,
canon promotion, external acceptance, proof-assistant or novelty claim.

Adjacent literature includes Pelinovsky's one-dimensional nonlinear Dirac
survey (arXiv:1011.5925) and Zhang's global Dirac-type result
(arXiv:1205.4568). Neither abstract licenses a theorem transfer to this specific
higher-power phase-sensitive system; the result here uses the explicit proof.

Next: test nonlattice collision phases or infinitely many packet interactions
with a uniform control, rather than redoing compact-support perturbation or
claiming failure of a sufficient bound implies blowup.
