---
title: "K2386 Finite timing records, optimal bins and priced decoder rotations"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2386_finite_timing_recovery_probe.py
---

# K2386 Finite timing records, optimal bins and priced decoder rotations

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
result: K2386
carrier: K2383 four dual-rail code plus classical final flag and supplied finite time label LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and reference-aware half-diamond distance ON=declared_carrier
real_structure: complex qubit amplitudes and real loss-time densities
grading: occupied and erased pair flags with classical time labels
action_owner: repository-construction -- transparent X/Z drive and stipulated timing and decoded-output controls
target: complete channel recovery with finite timing information MAP-TYPE=evaluation
```

## Exact information gain and its scope

[K2383](k2383-driven-erasure-recovery-2026-10-31.md) supplies the complete driven channel with final flags but no loss-time record. Here supply an additional classical record of the second-loss time bin, without rail/bit labels or coherent environment access. The timing instrument is assumed to report that label without changing the specified loss dynamics. Its physical realization and error are independent costs. This is conditional quantum-information mathematics; SC-META-53 remains UNCERTAIN and LT-GR6b stays open.

For each two-erasure flag S and label b put

    p_Sb = integral_Bb omega_S(t) dt,
    m_Sb = integral_Bb omega_S(t) n_S(t) dt.

Empty labels contribute zero. Repeating the inherited binary-channel Bell bound for each retained classical flag gives the exact optimum over ALL final CPTP decoders,

    e_B = e_idle + (1/4) sum_S,b [p_Sb-||m_Sb||].       (1)

The error is reference-aware half-diamond distance from intended U(T). The maximum Bell overlap of an unnormalized branch is (p+||m||)/4. Preparing/rotating to the optimal axis attains the bound, and the resulting mixture of identity, traceless unitary conjugations and depolarization has the matching upper bound. No restricted decoder is used for the lower bound. Refinement cannot worsen (1), by triangle inequality. This reuses K2383's channel theorem and adds finite-record quantitative consequences.

## Sharp path-length bound, not an angular-diameter assertion

For a contiguous time bin let ell_Sb=integral_Bb ||n'_S(t)||dt. When ell<=pi, choose the axis at the midpoint of accumulated arc length. Every bin axis lies in its spherical cap of radius ell/2. Projection onto that midpoint gives ||m||>=p cos(ell/2). In general,

    0 <= p-||m|| <= p[1-cos(min(ell,pi)/2)]
                   <= p min(1,ell^2/8).              (2)

Thus its contribution to excess error is at most p ell²/32. Equal endpoint masses on a shortest arc attain the cosine bound for ell<=pi; antipodal masses attain the trivial bound for ell>=pi. Bounded ordinary densities can approach these limiting measures. A pairwise angular diameter is insufficient: equally weighted x,y,z axes have diameter pi/2 but mean norm1/sqrt3<cos(pi/4).

For the stipulated drive, ||n'_X||=2|g| and ||n'_Z||=2|h|. Partition equal increments of A(t)=integral_0^t 2 max(|h|,|g|). Each of B bins has path length at most A(T)/B, hence

    e_B-e_idle <= P2 min(1,A(T)^2/(8B^2))/4.          (3)

Equal A increments minimize the largest certified bin length, not necessarily the actual weighted loss. With B<=2^b a fixed-length b-bit register supplies that many labels conditional on the existing erasure flag. This is not an entropy constraint and does not price acquisition/storage/readout.

## Exact physical full-circle fixture and global B-label optimum

Only pairs0,1 are lossy. On an early interval[0,a], pair0 has constant rate -log(1-p)/a, 0<p<1, and all other rates vanish. Thereafter its rate vanishes. On[a,a+tau], pair1 has

    k1(t)=q/[tau(1-q(t-a)/tau)], 0<q<1,

and all other rates are zero. This bounded rate yields survival eta1=1-q(t-a)/tau. The only two-loss flag S={0,1} has probability pq and UNNORMALIZED second-loss density pq/tau. No third/fourth loss occurs. Drive h=0,g=pi/tau in the late interval, zero before. Then U(T)=-I and n_X traverses a great circle once. Switching is piecewise constant here; no finite-slew claim applies to this experimental drive fixture.

Equal-duration B bins give

    e_B=pq[3-sinc(pi/B)]/4,   e_idle=pq/2,             (4)
    sinc(x)=sin(x)/x.

They are globally optimal even among arbitrary measurable deterministic B-label records of this time. For a label set of angular measure l, center an arc of length l on the direction of its resultant. Integrating cos shows

    |integral_A exp(i theta) dtheta/(2pi)|<=sin(l/2)/pi.

An arc maximizes that projection. Concavity of sin on[0,pi] and sum l=2pi then give sum_b ||m_b||/(pq)<=B sin(pi/B)/pi, achieved by equal arcs. This proof covers disconnected label sets, not merely contiguous partitions; it assumes deterministic label encoding with B possible outputs. The finite-record penalty therefore decays as pq*pi²/(24*4^b) at B=2^b. Finite B never removes it in this fixture.

At p=q=1/2, B1 gives3/16; B2 gives(3-2/pi)/16; B4 gives(3-2sqrt2/pi)/16; ideal exact time gives1/8. These are exact formulas. The probe independently integrates the vector moments and the physically supplied survival law.

Equal probability or duration is not generally optimal. With two loss-supported constant-axis plateaus x and y, masses1/5 and4/5, separated by a zero-loss-density finite rotation, splitting between plateaus yields total normalized moment norm1. Equal-probability bins give (sqrt13+5)/10<1. Moving the transition away from the temporal midpoint similarly defeats equal duration. These supplied density/axis examples concern optimization, not the full-circle physical fixture.

For general supplied integrable omega and continuous axes, maximizing sum norms over the compact contiguous-partition simplex has a solution. At an interior boundary where each density is continuous and adjacent moments are nonzero, a necessary condition is

    sum_S omega_S(t_b)n_S(t_b).(mhat_Sb-mhat_S,b+1)=0.

It is not sufficient for global optimality. A grid dynamic program is only grid-optimal without a discretization remainder; theorem(4) already removes the need for numerical optimization in the uniform-circle fixture.

## Construct the axis decoder and price the added control assumption

After the inherited extraction, P=paxis.sigma is the classical output axis. Let n=m/||m||. For n!=-paxis,

    R=[I+(n.sigma)P]/sqrt[2(1+n.paxis)],
    R P R^dagger=n.sigma.                            (5)

At the antipode choose R=-i r.sigma with r perpendicular to paxis. If m=0 the extracted state is already I/2; any R works. Applying U(T)R restores the intended frame. The rotor identity is checked on generic rational unit vectors and antipodes, with an order-reversal countercontrol.

Now explicitly stipulate controllable X/Z Hamiltonians on the decoded output qubit; transparent physical code controls do not automatically supply them. Ignoring global phase, a ZXZ decomposition uses three principal Bloch angles of magnitude at most pi. With amplitude cap G and slew cap V, each pulse starts/ends at zero. Signed area A=|theta|/2 is realized by a triangle or trapezoid in

    t(A)=2sqrt(A/V)              if A<=G²/V,
         A/G+G/V                if A>=G²/V.           (6)

Areas follow directly from triangle/trapezoid geometry. Thus three serial output pulses require at most3t(pi/2), provided the stipulated axes and limits are available. At G=V=1 this is3(1+pi/2). This prices only output rotation duration, not timing apparatus or all extraction/preparation gates. The old21-gate budget does not transfer.

If the synthesized axis differs by angle alpha_Sb, its branch deviation is exactly ||m_Sb||sin(alpha_Sb/2): the binary channel's output change is (v.r)(n-n')/2 and its reference-aware norm equals the product of the functional norm ||v|| and output trace distance. Summing gives a weighted synthesis-error upper bound. Unrecorded environment access cannot be supplied by this rotation.

## Complete-instrument cost threshold

The ideal information gain is

    G_B=(1/4)sum_S[sum_b||m_Sb||-||sum_b m_Sb||].     (7)

Let delta0,deltaB bound the distance of the complete implemented instruments from their respective ideal channels. Triangle inequalities give e_actual,B<=e_B+deltaB and e_actual,0>=e_0-delta0. Actual improvement is therefore certified when delta0+deltaB<G_B. The weaker deltaB-delta0<G_B only improves an upper certificate; it does not compare actual devices.

For p=q1/2 and B2 in(4), G_B=1/(8pi). With delta0=deltaB=1/100, the sum1/50 is smaller (pi<4 suffices), so these supplied error budgets certify improvement. Both budgets still require evidence for the SAME complete instrument. A false-positive cost control sets delta0=deltaB=1/10: the upper-certificate difference condition passes while the actual-improvement condition fails.

Include timing acquisition and disturbance, register storage/readout, feedback, extraction/rotations, preparation and the appropriate noise/rate mismatch. Avoid double-counting intervals. K2377 bounds the stipulated instrument it proves; an endpoint channel bound cannot silently be promoted to a bound on a newly recorded timing instrument. The next physical test is a measured or rigorously specified record-resolved detector with these costs. The present result supplies an exact finite-bit target and achievable conditional decoder, not that device.

Independent internal review challenged the density law, cap assumption, rotor order and cost comparison. Exact finite probes support the written universal bounds and optimum proof; they are not external-expert, proof-assistant, measured hardware or GU certification.
