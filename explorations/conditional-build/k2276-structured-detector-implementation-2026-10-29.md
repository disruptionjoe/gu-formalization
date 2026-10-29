---
title: "K2276 A direct quantized-pump squeezed-number detector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied apparatus only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2276_structured_detector_implementation_probe.py
---

# K2276 A direct quantized-pump squeezed-number detector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2276 A direct quantized-pump squeezed-number detector
carrier: two-mode bosonic field and pump of weighted charge two plus neutral qubits LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: declared oscillator charge only; not native Clifford or chirality grading
action_owner: repository-construction -- supplied conditional apparatus
target: structured complete instrument and quantified pump backaction MAP-TYPE=intertwiner
```

Source SC-META-53 remains UNCERTAIN. LT-SM8/LT-GR6b and ledger0.263 are unchanged. No native interacting positive quotient, source-selected action, family or chirality count follows.

## Result

For the actual K2253 target b=(5/3)a1+(4/3)a2†, the enormous universal shell
compiler can be replaced by two supplied trilinear pump pulses and a finite
neutral circuit using dispersive number/bit interactions. The complete
recorded field channel, arbitrary external history, AND retained original
pump admit an explicit joint bound. The sharper bound uses a SECOND number moment; a later proof-only cutoff restores K2253's original first-moment input class. The conserved charge is now

    Q=N+2 n_c, N=n1+n2,

not ordinary three-mode particle count. This corresponds, for example, to
two equally energetic field quanta and a pump quantum of twice that energy;
the frequency/energy identification is a separate supplied resonance model.

Set A=a1 a2, G=N+1, r=log 3, and

    Hs=i(A†-A), S_s=exp(-i s Hs).

Then S_r† a1 S_r=b, so E=S_r† P0(n1) S_r. A coherent record flip C0
controlled by n1=0, with the record initialized in |1>, gives the exact Lüders isometry
V=S_r† C0 S_r. Dephasing gives E rho E with record0 and (I-E)rho(I-E) with record1, preserving the fixed instrument labels. Initializing the record in |0> without a compensating flip would implement the oppositely labeled instrument.

Prepare the pump in |alpha>, alpha=sqrt(mu)>0 calibrated to the squeeze
phase, and use the supplied conserving generator

    Halpha=(i/alpha)(A† c-A c†), U_s=exp(-i s Halpha).

Both signs of pulse area are initially allowed. Each Q=t shell has finite
dimension, and Halpha is the selfadjoint direct sum of its finite Hermitian
blocks, exactly as in K2270's domain construction. The finite-particle sum
is a core. The pump is untruncated with finite mean occupation mu; no finite
maximum capacity is claimed. Its preparation imports phase asymmetry.

## A rigorous joint pump approximation

For every psi in D(G), including an arbitrary spectator/history tensor,

    ||G S_s psi|| <= f(|s|)||G psi||,
    f(s)=cosh(2s)+sqrt(2)sinh(2s).

Proof: S_s†G S_s=cosh(2s)G+sinh(2s)(A†+A). Also

    ||(A†+A)psi||²
      <=2(||A†psi||²+||Apsi||²)
      <= <psi,(G²+1)psi> <=2||Gpsi||².

These identities hold first on finite-particle vectors, whose squeezed images have the required analytic number tails. The displayed norm estimate then extends by D(G)-graph closure; the corresponding strong continuity supplies the comparison-curve domain continuity used below. It is not inferred from an unspecified finite-moment assertion alone.

On an ideal PRODUCT comparison orbit the defect is particularly simple:

    (Halpha-Hs tensor I)(S_s psi tensor |alpha>)
      =(-i/alpha) A S_s psi tensor (c†-alpha)|alpha>.

The creation-side term vanishes because (c-alpha)|alpha>=0, and the surviving
pump vector has norm one. Since ||A phi||<=||N phi||/2<=||G phi||/2,
Duhamel gives, for either sign and 0<=s<=r,

    ||U_(±s)(psi tensor alpha)-S_(±s)psi tensor alpha||
      <= ||Gpsi|| I(s)/(2sqrt(mu)),
    I(s)=integral_0^s f(t)dt
        =sinh(2s)/2+sqrt(2)(cosh(2s)-1)/2.

This compares vectors with the ORIGINAL pump retained; it is not a
replacement of c by a scalar in the actual dynamics. Duhamel is justified
on these comparison curves: they are strongly differentiable, lie in the
direct-sum domain of Halpha, and Halpha acting on them is continuous, because
psi has finite G² moment and the coherent pump has all moments. Approximate
general states by domain vectors and purify to include external histories.

At r=log3,

    f(r)=(41+40sqrt(2))/9 <11,
    I(r)=(20+16sqrt(2))/9 <5.

## Finite neutral circuit instead of an exact vacuum predicate

Take q>=1 qubits and D=2^q. Standard exact finite phase estimation of
exp(2pi i n1/D) computes n1 mod D in a neutral register: q Hadamards,
q controlled number rotations, then the inverse q-bit Fourier transform.
Each controlled phase is a dispersive n1 P_bit pulse, already a familiar
primitive from the old alphabet. Flip the output record iff that q-bit
register is all zero, then uncompute the register. Denote this unitary C_D.
It returns all work bits to zero for EVERY n1, including n1>=D.

C_D differs from C0 only when n1 is a positive multiple of D. It is NOT an
exact vacuum measurement globally. With G² moment M2 of its input,

    ||(C_D-C0)phi|| <=2 sqrt(M2)/(D+1).

Here a vector-valued purification is allowed; n1>=D implies G>=D+1.
Both C0 and C_D commute with N and preserve every field number moment.
Compute/uncompute uses 2q dispersive pulses plus O(q²) neutral gates. One
conservative explicit budget is 10(q+1)² neutral Hadamard/controlled-phase/
SWAP/Toffoli gates, with at most 2q+2 neutral qubits including clean work,
record and ancillas. Standard clean-ancilla decomposition of the q-fold
controlled NOT supplies O(q) Toffolis. This gate model is declared; neutral
two-qubit gates have not been synthesized from the old single huge-register
nearest-coordinate-flip control budget. No precision cost is hidden: those
phase angles and pulse areas are supplied calibrated controls, and their
actual implementation errors must be budgeted separately.

## Complete instrument and adaptive bound

Use U_-r C_D U_r with one pump, fresh neutral record/work bits each call,
and dephase the record at the end. A three-term telescoping expansion around
S_-r C0 S_r has first-pump error sqrt(M2)I/(2sqrt(mu)), alias error
2f sqrt(M2)/(D+1), and reverse-pump error f sqrt(M2)I/(2sqrt(mu)). Thus

    e_call <= sqrt(M2)[(1+f)I/(2sqrt(mu))+2f/(D+1)]
           < sqrt(M2)[30/sqrt(mu)+22/(D+1)].

The reverse-pump term is applied to the ideal C0 S_r state, whose G² moment
is <=f²M2; the ACTUAL pump need not remain independent or coherent there.
Vector-norm error bounds half trace distance after dephasing/discarding
neutral workspace. The pump and arbitrary external histories remain retained.

For J calls with controllers that do not access the pump and whose IDEAL
unconditional detector inputs satisfy Tr(G²rho_j)<=M2_j,

    delta_J <= min(1, sum_j sqrt(M2_j)
                       [30/sqrt(mu)+22/(D+1)]
                       + epsilon_prep + sum_j epsilon_impl,j).

Use the K2253 ideal-prefix/actual-suffix hybrid, retaining the ORIGINAL pump
in the ideal target. Actual correlated histories do not need a separate
second-moment assumption for THIS trace-distance conclusion. Implementation
errors here must be valid full joint-channel bounds on the compared inputs,
or a domain-qualified Duhamel bound; mere scalar coefficient accuracy is
insufficient. Rare normalized postselection is not uniformly covered.

A concrete calibrated ideal-control consumer is

    J=10, all M2_j<=4, mu=10^10, q=17, D=131072.

Its error is <20[30/100000+22/131073]<0.009357.
There are twenty pump pulses, 340 dispersive pulses, and at most
10*10*18²=32400 neutral gates over ten calls, with 36 neutral qubits
sufficient per call (many can be reused). An additional total preparation
and implementation allowance 0.0006 keeps the joint error below0.009957.
These are operation counts in the DECLARED new model, not a wall-clock,
fidelity, hardware or affordability certificate. The stock is still large.
The M2<=4 controller condition must actually be proved in a chosen consumer;
it does NOT follow from the old B<=1 condition.

## Mean-only successor without a physical cutoff

The second-moment theorem also yields a full-channel guarantee on the original mean-input class. For input mean Tr(N rho)<=B and integer K>=0, project only in the ANALYSIS onto P_K. Its purification psi_K is subnormalized and

    ||G psi_K||²<= (K+1)(B+1).

The pump/squeeze/circuit proof is homogeneous in this vector; it never divides by the retained probability. Both actual and ideal input truncations cost at most sqrt(B/(K+1)) each. Consequently the SAME physical detector satisfies

    e_call <= 2sqrt(B/(K+1))
         +sqrt((K+1)(B+1)) a,
    a=30/sqrt(mu)+22/(2^q+1).                         (11)

There is no actual input cutoff, finite-shell compiler or boundary operation. For B>0, treating x=K+1 continuously, the unconstrained optimum is x*=2sqrt(B)/(a sqrt(B+1)); clipping to x>=1 and rounding to a positive integer gives a usable explicit bound. Its unconstrained minimum is 2sqrt(2a sqrt(B(B+1))). This is a bound optimization, not a claim of apparatus optimality. At B=0 use the vacuum second-moment theorem directly.

Take B=1,J=10,mu=10^18,q=30 and K+1=2^25. Then sqrt((K+1)(B+1))=8192 and the truncation term is sqrt(2)/4096. Using sqrt(2)<10/7 and2^30+1>2^30 gives

    10 e_call <10[10/(7*4096)
                    +8192(3/10^8+22/2^30)]<0.007624.

An additional total preparation/implementation error0.0006 keeps the full averaged field/record/history/original-pump error below0.008224. The core counts are20 pump pulses,600 dispersive pulses, at most96100 neutral gates and62 neutral qubits per call. Routing costs remain separate. This restores the original mean-only input class under the NEW trilinear control alphabet, with10^18 pump occupation. It does not provide finite actual or ideal second moments for arbitrary mean-bounded inputs. Energetic conclusions below apply only when their stronger moment hypotheses hold.

A concrete state in the newly covered class has p_0=1/2 and p_n=2/[n(n+1)(n+2)] for n>=1 on |n,0>. Telescoping gives total probability1 and mean N=1, but its second moment diverges. Equation(11) applies while the preceding second-moment theorem does not. No final energetic moment is inferred for this state.

## A nonempty ten-call consumer with all outputs retained

Supply ten two-mode field registers, each supported initially on total number N_j<=1, possibly jointly entangled with arbitrary external memory. Supply one independent coherent pump. Route one previously unused register per call using charge-preserving address controls; keep earlier field/record outputs isolated. Every ideal input has M2<=4, without assuming that the energetic output of one detector can be fed back under the same bound. This consumes20 field modes. Routing gates, duration and errors are additional supplied resources; the quoted operation counts cover detector cores only.

The actual global Q=N_all+2n_c is conserved for these ideal apparatus primitives and charge-preserving routing. Initially N_all<=10, so

    E(Q+1)² <= (11+2mu)²+4mu.                         (10)

Every actual field-subset G² moment inherits this bound. For the ideal final fields, Minkowski gives ||(N_all+1)Psi||<=sum_j||(N_j+1)Psi||<=20 f², hence E(N_all+1)²<=400 f⁴<5856400. Including the original independent pump in the ideal comparison gives E(Q+1)²<=(20f²+2mu)²+4mu. These are explicit moments of BOTH final compared systems. Arbitrary implementation errors require their own moment-preservation estimates; a small trace error alone does not preserve (10).

## Moment and energy ceilings

The ideal one-call field output has G² moment <=f(r)^4 M2<11^4 M2, since
the middle controlled record operation preserves G. For a single actual
call starting with an independent coherent pump, exact weighted-Q
conservation yields the finite but loose output bound

    Tr(G_out² rho_actual) <= E[(Q+1)²]
       =M2+4mu E(G_in)+4(mu²+mu)
       <=(sqrt(M2)+2mu)²+4mu.

Actual pump second moment is bounded by E(Q²)/4. The same conservation
propagates all existing total-charge moments within a detector call.
Arbitrary adaptive controllers require their OWN actual moment/energy
injection control to iterate these energetic estimates; the ideal-input
moment bound alone only licenses the channel hybrid above.

K2273 then bounds a one-call field mean-number error by sqrt(Mout2*delta),
where Mout2 is the larger of the two proven N² bounds (using the G² bounds
above is conservative). This bound is huge at large mu and does NOT establish
small energy error, nor a uniform energetic limit as delta tends to zero.
The construction closes the giant-compiler gap under a new trilinear control
model, while leaving economical energetic backaction and source preparation
as distinct burdens. Do not silently call channel accuracy an energy theorem.

Optional positive-pulse completion: on weighted shell t, every off-diagonal
trilinear matrix element is at most (t+2)^(3/2); each row has at most two,
so ||Halpha,t||<=2(t+2)^(3/2)/alpha. Hence

    B_±=2(Q+2)²/alpha ± Halpha >=0.

The shift commutes with Halpha. Its extra exp[-i 2r(Q+2)²/alpha] phase can be
repaired by a positive area pulse of (Q+2)², choosing area congruent to
-2r/alpha modulo2pi (integer spectral periodicity). This requires the stated
weighted quadratic compensator, another explicit control assumption, and
adds time/calibration costs. Q² expands into onsite and cross-Kerr terms.
Mean positive control energy requires finite Q² and RMS requires Q^4.
Do not import the old two-subsystem positive-pulse resource count unchanged.

## Verification and remaining requirements

The companion exact probe checks actual finite weighted-charge matrices, squeeze/moment coefficients, number-register computation and alias controls, moment polynomials, positivity and the displayed operation/error budget. Written direct-sum domain, Duhamel and adaptive proofs are distinct from finite controls. Independent internal review does not establish external-expert, hardware, novelty, Lean or remote-CI certification.

The trilinear coupling, calibrated coherent pump, neutral gates and dispersion controls are explicit new supplied primitives. Their physical implementation, clock/preparation, error calibration and useful uniform energetic accuracy remain independent tasks. The result gives a finite operation count under that specified model, not a proof that the old pairwise alphabet economically synthesizes it.

## Dependency evidence

- [K2253](k2253-full-instrument-reference-reuse-2026-10-29.md).
- [K2270](k2270-untruncated-detector-control-2026-10-29.md).
- [K2273](k2273-positive-control-energy-2026-10-29.md).

Eigenvalue readout and finite Fourier transforms are established background; see [Kitaev](https://arxiv.org/abs/quant-ph/9511026). The supplied trilinear-pump construction and resource bounds here are independently derived within the stated model, with no novelty claim.
