---
title: "K2142: Finite-time real control: density, cost and causal complement"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar mathematics; no causal parity apparatus or GU recovery
scripts:
  - tests/channel-swings/k2142_finite_time_real_control_probe.py
---

# K2142: Finite-time real control: density, cost and causal complement

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
result: Finite-time real control: density, cost and causal complement
carrier: massive scalar one-particle L2 shell and full real Cauchy phase space LAYER=toy CHIRALITY=N/A
pairing: real Hilbert control norm, complex one-particle norm and CCR symplectic form ON=declared_carrier
real_structure: complex conjugation and real spacetime switching
grading: boson occupation; not GU grading
action_owner: repository-construction -- K2136 two-site scalar source pulses
target: finite-time real reachable closure and switching cost MAP-TYPE=intertwiner
```

## 1. The question that all-time complex density left open

[K2140](k2140-point-sites-blind-sectors-2026-10-27.md) proved all-time
COMPLEX cyclic density for two distinct sites. That is not a statement about
real switching in a fixed time interval. Here m>0, T>0, x1!=x2, and
B={k:k0<=|k|<=k1}, 0<k0<k1<infinity. Write omega=sqrt(k²+m²),
w=lambda/sqrt(4 pi omega), with real lambda!=0. Real controls are in
L2((0,T);R)^2 and the complex target space L2(B;C) is regarded as REAL.
The restricted displacement operator is

    (L chi)(k)=-i w(k) sum_j exp(-ik xj) int_0^T chi_j(t) exp(i omega t)dt. (1)

This is the projection of a full-field source displacement, not a replacement
of the local field by a sharp-cutoff field. The cost below is the L2 switching
norm, not total controller energy or work.

## 2. Real density at every positive finite time

Let u be real-orthogonal to the range. Set

    g_j(t)=int_B conjugate(u(k))[-i w(k)]exp(-ik xj)exp(i omega t)dk.

Real orthogonality says Re g_j(t)=0 almost everywhere on (0,T). The finite
shell and Cauchy--Schwarz make g_j entire, so Re g_j is real analytic and
vanishes on the entire real line. The Fourier measure of g_j is supported
in the compact positive-frequency interval [omega0,omega1]. The conjugate
has support in its negative, disjoint interval. Uniqueness of finite-measure
Fourier transforms applied to g_j+conjugate(g_j)=0 implies both measures zero.
Thus, for almost every k>0 in the shell,

    conjugate(u(k)) exp(-ik xj)+conjugate(u(-k)) exp(ik xj)=0, j=1,2.

The common nonzero radial factor cancels. The determinant is
2i sin(k(x2-x1)), nonzero almost everywhere. Hence u=0. The REAL closure of
ran L is all L2(B;C). Smooth real compact-time controls have the same dense
range because they are dense in the control space and L is bounded.
The argument is qualitative; it supplies neither a bounded inverse nor a
uniform pulse-cost bound. Coincident sites fail: their two equations coincide.
A single site has a whole angular blind space even on the shell.

## 3. Compactness and an explicit factorial cost obstruction

Let H=int_B w² dk and Omega=omega1. The two kernels have total squared
complex kernel norm 2TH, so L is Hilbert--Schmidt as a real map and compact.
The target is infinite dimensional. A compact map onto it cannot have a
bounded right inverse (otherwise the identity would be compact).
Here a sharper constructive family of bad directions is available.

For every integer N>=1 choose a unit u_N orthogonal in the COMPLEX inner
product to the 2N vectors

    a_j,l(k)=-i w(k) exp(-ik xj) omega(k)^l,  j=1,2, 0<=l<N.

Such vectors exist because only finitely many constraints are imposed on an
infinite-dimensional space. Taylor's integral remainder on REAL omega t gives

    |exp(i omega t)-sum_(l<N)(i omega t)^l/l!| <=(Omega t)^N/N!.

No exp(Omega T) factor is needed: the derivative has unit modulus on the real
segment. It follows that |g_j(t)|<=sqrt(H)(Omega T)^N/N!, and therefore

    ||L*_R u_N|| <= sqrt(2TH)(Omega T)^N/N!.

If ||L chi-u_N||<=epsilon<1, real inner products and Cauchy--Schwarz yield

    ||chi|| >= (1-epsilon) N! / [sqrt(2TH)(Omega T)^N].                 (2)

At fixed nonzero T this grows without bound with N. The target changes with
N; (2) is a worst-direction family, not a divergence claim for every fixed
wavepacket. The exact normalization is

    H=lambda²/(2 pi) [asinh(k1/m)-asinh(k0/m)].

The finite band bounds one-particle energy above by Omega and below by omega0.
Consequently finite input energy alone does not give uniform switching cost
on even this bounded-energy unit sphere. No finite discretization proves this
universal result; the proof is the finite-moment annihilation argument above.
The spectral-moment construction can be chosen smooth inside B by solving its
finite linear constraints in any sufficiently large smooth test space.

## 4. Why whole-field real density fails

For the full massive field, take nonzero smooth compact real Cauchy data
outside the union of intervals [xj-T,xj+T] at time0. Finite propagation implies
the associated real Klein--Gordon solution vanishes at each source site for
0<=t<=T. With unitary Fourier transform the one-particle vector is
h=(sqrt(omega) qhat+i phat/sqrt(omega))/sqrt2, and the direct normalization
identity is

    Im<h,L_full chi>=-lambda/2 sum_j int_0^T chi_j(t) q_free(t,xj)dt.

Thus the corresponding finite-energy one-particle displacement h is
symplectically orthogonal to every source displacement in that interval.
The real functional z -> Im<h,z> is continuous and nonzero. Thus the full-field
real reachable closure is proper and in fact has infinite codimension, using
arbitrarily many linearly independent exterior Cauchy data. This is compatible
with complex density: a symplectic/real annihilator need not be a complex one.
Projecting onto B destroys the exact Cauchy localization; it is precisely why
the band theorem cannot be promoted to a causal whole-field controllability
statement. Large uncontrolled out-of-band tails are not bounded by (2).

## 5. A full-record operational consequence

The remote Weyl unitary W(a h) commutes with every localized pulse during the
stated interval. Memory-only operations commute too. With independent initial
apparatus, every record effect of such a protocol commutes with W(a h), even
with feedback, provided the causal support and common output time stay fixed.
The same conclusion holds for limits whose record effects converge weakly.
Hence the record distribution on vacuum and W(a h) vacuum is identical.
This applies more generally to any instrument with effects in that causal
region; no finite-Weyl premise is needed for this probability statement.

Normalize ||h||=1 and let e_h=<h,omega h>. First, coherent inputs W(a h)
vacuum have mean energy n e_h, n=a², and ideal odd-record probability
(1-exp(-2n))/2. Identical actual record laws therefore imply worst-case
full recorded parity error at least (1-exp(-2n))/4. This is a simple control,
not the strongest finite-energy witness.

For the stronger finite-energy input witness, let
X=-i(a†(h)-a(h)), so W(t h)=exp(itX) and the vacuum law of X is standard
normal. Every bounded function of X commutes with all the record effects.
Choose the odd clipped-linear function f_delta equal to pi x/(2 delta) for
|x|<=delta, and equal to +/-pi/2 outside, and set

    psi_delta=exp(i f_delta(X)) vacuum.

The ENTIRE actual record distribution still equals the vacuum's. Global
particle parity sends X to -X, whereas the ideal odd-record probability is

    p_delta=1-(1/2) int_(-delta)^delta [1+cos(pi x/delta)] phi_G(x)dx
           >=1-sqrt(2/pi) delta.                                  (3)

Here phi_G is the standard normal density. The crude bound uses
1+cos<=2 and Pr(|X|<delta)<=sqrt(2/pi)delta. Expanding F(X)vacuum in the
normalized one-mode Hermite basis gives the exact quadratic-form identity

    <F(X)vacuum,H_F F(X)vacuum>=e_h int |F'(x)|² phi_G(x)dx.

Indeed the n-particle coefficient contributes n e_h, while the Gaussian
Dirichlet form has the same Hermite eigenvalue n. The clipped phase is
Lipschitz and the identity extends by quadratic-form closure. Therefore

    E_delta=pi² e_h Pr(|X|<delta)/(4delta²)
           <=pi² sqrt(2/pi)e_h/(4delta).                           (4)

This is finite mean free-field energy, with no second-moment or preparation
work claim. If both specified inputs have binary record error at most epsilon,
the SAME actual odd-record probability approximates both0 and p_delta, giving
epsilon>=p_delta/2. A complete field-plus-record channel error is at least its
record error. For a mean field-energy test budget E>0 choose

delta=pi² sqrt(2/pi)e_h/(4E). Then

    epsilon_E >= max(0,1/2-pi e_h/(4E)).                           (5)

This is a lower bound, not the sharp optimal full-instrument distance. It uses
two specified test inputs. A parity-invariant finite code may contain vacuum,
psi_delta and parity psi_delta, but (4) must not automatically be assigned to
every normalized code superposition. K2140's sharper1/sqrt2 uses a DIFFERENT
single-site blind vacuum–one-photon code. Neither result may replace the other.
Changing detector coverage or duration changes the causal complement; (5)
is not an all-times or all-apparatus impossibility theorem. Smooth exterior
Cauchy data give infinitely many finite-energy h; no hard frequency cutoff is
used in this part.

## 6. Acceptance, reuse and next construction

The finite probe checks angular equations, the real-adjoint distinction,
Taylor/moment identities, and the minimax record witness with actual modified
inputs. These are finite diagnostic controls. Real density, compactness,
factorial cost and causal-complement transfer are independently reviewed
written arguments. Prior-art ingredients are elementary Fourier uniqueness,
finite propagation and compact-operator theory, not claimed novel theorems.
K2136/37 supply the actual source displacement conventions; K2140 supplies
only the reused spectral fiber idea. No causal cutoff or parity control is
inferred from a finite matrix.

Next construct an actual specified wavepacket's real controls with both
in-band accuracy and out-of-band field energy, or change the detector
interaction while retaining its causal support and complete recorded output.
The local canonical-mode construction in
[K2143](k2143-local-canonical-parity-2026-10-27.md) tests a different observable;
it is not an escape from (3) for global particle parity.
SC-OP-04 ASSERTS candidate grammar; SC-OP-05/SC-META-53 UNCERTAIN and
SC-META-56 DISAVOWS the odd-action prerequisite remain unchanged. Ledger0.263,
LT-SM8/LT-GR6b, canon and all GU physical recovery claims are unchanged.
