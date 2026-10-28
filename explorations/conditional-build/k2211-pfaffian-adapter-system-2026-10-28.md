---
title: "K2211 Pfaffian degree17 system for every normalized adapter row"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact lower-degree polynomial criterion for all ten fixed-adapter rows; no general solution or exclusion
scripts:
  - tests/channel-swings/k2211_pfaffian_adapter_system_probe.py
---

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
result: complete chiral Pfaffian degree17 polynomial adapter criterion
carrier: full real Cl77 S128 with auxiliary normal complex S32 and both16-dimensional chiral halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: algebraic normal Chevalley bilinear form and alternating chiral pencil forms ON=declared_carrier
real_structure: real normal Cl46 ports and quaternionic bar transport; conjugate tangent-volume sector retained
grading: normal Clifford grades3/7 and chirality; no observed-family grading
action_owner: repository-construction -- fixed K2169 simple-contraction normalized adapter
target: all ten original coefficient-descent rows with exact nonsingular chart MAP-TYPE=intertwiner
```

# K2211 Chiral Pfaffian elimination of all ten adapter rows

## Result

For the fixed K2169 normalized adapter, the complete nonzero-port problem has
an exact real polynomial formulation of degree17 in the same240 real port
coordinates. This replaces the full32 determinant's degree65 equations. It
uses two nonvanishing degree16 real polynomials, one on each chiral half.
The alternative product inequation has degree32. No root search or emptiness
claim follows. This is a change in the exact equation representation, not a
new family exclusion or source/physical verdict.

The carrier is full real Cl77 S128 with W(3,1)+N(4,6), represented for algebra
by faithful complex normal S32. Sending the real tangent volume Omega to i
is an isomorphism of the real algebra Cl(N)+Omega Cl(N) with Cl(N)_C.
The full real carrier is retained: its opposite tangent-volume sector is
the complex conjugate. A zero in this faithful algebra is therefore zero
in the original full real representation; no physical chirality is discarded. The normal Chevalley bilinear B is symmetric,
pairs opposite chirality, and makes grades3/7 skew. It is not a positive
physical pairing. Real structure beta is quaternionic conjugation, not
entrywise conjugation or Clifford reversion. Action owner is the repository's
fixed simple-contraction coupled operator; target is all ten original lower
rows with the normalized adapters. Source grammar and torsion caveats of
K2169/K2208 remain; no ledger, canon, source or GU verdict follows.

## 1. Pfaffian adjugates and the two genuine denominators

Use the K2208 conventions, P=7I_N w-15iu, barP=beta(P), R=I_N w+3iu,
z=I_N w+iu, t=iu, real grade3 w,u. Select a half E=S_epsilon and write
F for its opposite. Let U=P:E→F, V=P:F→E, and barU=barP:E→F.
B_EF is the invertible block of B from F to E. Set

    Omega_E=B_EF barU,
    d_E=Pf(Omega_E),       rho_E=d_E conjugate(d_E).

Omega_E is alternating16. Its entries are linear in the240 real coordinates,
d_E has degree8, rho_E degree16. With b=7w-15epsilon u,
Omega_E=-epsilon i Phi(b); hence this is exactly K2208's real-grade map,
and Pf((-epsilon i)Phi(b))=Pf(Phi(b)). The opposite half similarly tests
a=7w+15epsilon u. The two real trivectors a,b are independent before a
prescribed invertible Y is supplied: neither half's invertibility may be
silently inferred from the other's.

For an alternating16 matrix Omega, define H=padj(Omega) by H_ii=0 and,
for i<j using zero-based indices,

    H_ij=(-1)^(i+j) Pf(Omega with rows/columns i,j deleted),
    H_ji=-H_ij.

Pfaffian expansion proves Omega H=H Omega=Pf(Omega)I as a polynomial
identity, including singular Omega. H has degree7. Thus

    L_E=H_E B_EF=d_E barU^-1

whenever d_E!=0. Lift L_E as the single odd block F→E and apply beta.
Its opposite block N_E:E→F satisfies

    N_E=conjugate(d_E) V^-1.

This follows because beta(barP)=P and beta exchanges halves. This transport
must include the quaternionic conjugating matrices; complex entrywise
conjugation alone is not beta. L_E,N_E are polynomial matrices of degree7,
with no inverse used in their definition.

## 2. All ten rows, with order retained

Write r_j=d_jR, s_j=d_jbarR, D_j=d_jz, where d_j is metric algebraic
contraction, not a spacetime derivative. Superscripts E,F on an even map
mean diagonal restriction. On an odd map a subscript E means E→F, and a
subscript F means F→E. Define polynomial degree8 matrices

    X_j=-eta_j N_E r_j^E,        Z_j=-eta_j L_E s_j^F.

Then on rho_E!=0 the actual unique adapters satisfy

    C_{j,E}=X_j/conjugate(d_E),
    barC_{j,F}=Z_j/d_E.

K2169's original residual restricted to E is exactly

    q_j^E=4t_F C_{j,E}-eta_j D_j^E+7barC_{j,F}z_E
      +2 sum_i barC_{i,F}s_i^F C_{j,E}
      +eta_j sum_i barC_{i,F}[D_i,gamma_j]_E.

Therefore the polynomial

    F_j^E=4d_E t_F X_j-eta_j rho_E D_j^E
      +7conjugate(d_E) Z_j z_E
      +2 sum_i Z_i s_i^F X_j
      +eta_j conjugate(d_E) sum_i Z_i[D_i,gamma_j]_E       (*)

obeys F_j^E=rho_E q_j^E. Each term has total homogeneous degree17.
No coefficient has been commuted except the scalar d_E. Repeat on F.
Original ten Clifford rows correspond to ten matrices on BOTH halves;
it would be false to describe one half's ten equations alone as complete.
K2169 already proves all remaining upper equations follow from these rows
and the unique necessary adapters.

## 3. Equivalent degree17 real algebraic system

For a nonzero candidate, K2169 proves P invertible is necessary. In the
present notation that is exactly rho_E!=0 and rho_F!=0. Conversely those
conditions make P invertible and (*) equivalent to every original row.
Thus the full nonzero-port criterion is

    Re F_j^E=Im F_j^E=Re F_j^F=Im F_j^F=0, all ten j;
    rho_E!=0, rho_F!=0.

Both rho are real nonnegative polynomials, independently of physical
positivity. This elementary nonnegativity is complex modulus square only.
One may introduce two real scalars h_E,h_F and equations

    h_E rho_E-1=0, h_F rho_F-1=0.

Every equation then has total degree at most17 in242 real variables. These
saturation variables merely encode the exact open chart; dropping them
admits singular artifacts. Zero port is the known separate positive control
with arbitrary normalized adapters, outside this nonzero-port criterion.
The240-coordinate projective scaling and smooth-adapter rigidity of K2169
are unchanged. The theorem does not assert algebraic independence or count
solutions from the number of matrix entries.

For any exact proposed Y, K2208 first yields a real linear reconstruction
space in a. Since b is then linear in a, w,u and all these polynomials pull
back to that kernel without raising degree: two degree16 inequations and
full degree17 residuals. This supplies an exact all-ten-row consumer of the
prescribed-factor reconstruction, rather than mistaking paired Jordan,
abstract norm-one completion, or grade realization for descent. It does
not make the nonlinear search efficient.

There is a further exact saving only for this prescribed invertible-Y
consumer. The reconstruction identity Phi(a)Y=Phi(b) gives

    det Phi(b)=det Phi(a) det Y.

Since det Y!=0, the two Pfaffian zero loci coincide on the real kernel.
One may therefore retain just ONE rho!=0 and one saturation variable after
pullback. With m real kernel coordinates, the complete nonzero-port problem
has m+1 real variables and equations of total degree at most17. Both
chiral sets of full rows still remain. This reduction is invalid before Y
is prescribed or if its invertibility is omitted; neither ranks of Euler
coefficients nor paired-Jordan spectra replace that hypothesis.

## 4. Preflight, controls, postflight and limits

Read K2169, K2171, K2197, K2202, K2205 and K2208, native AGENTS and typed
object routing. Repository search for Pfaffian adjugate/denominator and
degree17/degree65 mechanisms found K2169 degree65 and K2208 prescribed-factor
reconstruction, but no existing complete degree17 all-row criterion. This
is an internal duplicate check, not a literature novelty assertion.

The exact probe builds the normal Fock matrices and Pfaffian
minors directly, checks adjugate identities even on a singular alternating
matrix, transports the actual real structure, and compares all twenty
chiral residual blocks with independently evaluated original fullCl77
C/kernel/RR maps on a real noncommuting mixed fixture. It preserves failed
rows as nonsolution controls, includes the inherited zero-port positive
control, verifies both denominators and homogeneity, and tests corrupted
product order/sign/coefficients against the original rows. Finite controls
support the universal polynomial identities; they are not a parameter
search or proof-assistant/external-expert certification. The next task is
a new structural consequence or exact candidate of this lower-degree
system; no blanket no-go has been proved.

## Reproduction

Run `python tests/channel-swings/k2211_pfaffian_adapter_system_probe.py`;
`--write` regenerates `lab/process/k2211-pfaffian-adapter-system.json`.
The Pfaffian implementation is a shared-minor arithmetic circuit; it does
not expand a polynomial in240 variables. Exact finite checks and deliberate
fault rejection accompany the written universal derivation. No broad
parameter sweep, elimination, or proof-assistant certification is claimed.
