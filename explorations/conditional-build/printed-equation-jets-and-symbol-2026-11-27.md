---
title: Printed-equation finite jets and the actual nonnull symbol
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T2
expected_delta: Decide the finite-jet matching ceiling and identify the actual printed principal descriptor for the curved-lift question
actual_delta: Every fixed finite jet is matchable at sufficiently large coupling; selected printed P has an explicit nonnull exterior decomposition and nilpotent descriptor of length two
class_covered: Finite-rank unrestricted translation bundles with first-order P, algebraic quadratic Q and invertible normalized mass; symbol subresult fixes the low-Phi comm/symi/symi dictionary on full complexified adjoint one-forms in dimension14, odd-index signature and nonnull covector
premises:
- source-prescription-current-2026-11-13.md sections1-2 binds independent g and T and full fixed-g translations to draft sections5-7 and p45eq9.7
- printed-endpoint-analytic-branch-2026-11-27.md owns the printed P,Q dictionary and flat homogeneous closure only
- ricci-flat-ambient-source-jets-2026-11-27.md owns the curved forcing comparison but not complete endpoint residuals
source_bridge:
  status: conditional
  reason: The endpoint template and independent primitives are source-bound; the selected product dictionary and geometric completion are not source-unique, and neither exact I1B stationarity nor a physical solution domain follows
kill_condition: A failed finite-jet Jacobian or Clifford identity invalidates the corresponding statement; neither successful matching nor symbol degeneracy decides GU or a matrix cell
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Printed-equation finite jets and the actual nonnull symbol

program_target: X-P1-P2
tier: T2
expected_delta: Determine finite-jet matching and the actual printed descriptor.
actual_delta: Fixed finite jets match at sufficiently large coupling; selected nonnull P is decomposed exactly.

**ESTABLISHED:** an unrestricted completion can absorb every finite order of
the printed curvature forcing, with the quantifiers below. This does **not**
give a solution at fixed coupling. The selected printed operator has a large
kernel, but its frozen zero sector is only length-two nilpotent and admits a
finite differential inverse after adding the nonzero mass term. Actual mixed,
variable-coefficient constraint compatibility is still undetermined.

```gu-typed-objects
result: Printed endpoint jets and nonnull symbol
carrier: T in T*Y tensor End_C(S128), complexification of full adjoint translations LAYER=ambient BRIDGE=held-printed-product-dictionary-conditional CHIRALITY=N/A
pairing: source indefinite spin pairing H; algebraic complexification only ON=End_C(S128)
real_structure: K95 and flipped K77 held separately; q=5 and q=7 nested-Hodge ports; physical sharp phases require the stated real-form adapter
grading: exterior Clifford degree and longitudinal/transverse covector blocks, not physical chirality
action_owner: source-print -- no new action; I1B and residual-square I2B distinguished
target: P(tau)=Phi(tau wedge T) and finite holonomic residual jets MAP-TYPE=intertwiner
```

## 1. Source custody and the question that remains live

[Source prescription](source-prescription-current-2026-11-13.md) §§1–2
binds draft §§3.6,5–7, eqs6.18–6.22,7.3 and p45eq9.7. At fixed metric
section g and epsilon, A=A0[g]+varpi and T=varpi-c(epsilon,g), so
delta_varpi T=alpha and delta_varpi g=0. There is no supplied requirement
T=0 or restriction to the transported flat homogeneous216 space. Fixing a
Schwarzschild metric on an admitted patch and asking for a local printed
endpoint lift is therefore meaningful before a physical matter readout is
chosen. It is not yet a physical black-hole solution claim.

After the held invertible Hodge normalization, the equation is

    R_kappa(T)=kappa T+S_g+P_g T+Q(T,T)=0,
    F_h(T)=T+h[S_g+P_g T+Q(T,T)]=0,  h=1/kappa.

P is first order, Q is algebraic bilinear, and the background is held.
The [printed branch result](printed-endpoint-analytic-branch-2026-11-27.md)
owns P,Q. The reconstructed W2 Euler equation uses different K,N: its
constraint inverses and symbol counts cannot be substituted here.

Draft p44eq9.4/SC-ACT01 (I1B), p45eqs9.7–9.10/SC-ACT02 (printed
endpoint), and p45eqs9.11–9.15/SC-ACT04 (I2B) are separate objects. Exact
Upsilon=0 implies first-order stationarity of the smooth residual square
I2B under all primitive variations, by the already-owned
[residual-square argument](k2348-even-distortion-stationarity-boundary-2026-10-30.md)
§5. It does not repair the
[I1B exact-Euler mismatch](printed-shiab-endpoint-audit-2026-11-27.md).
SC-ACT06's Euclidean reduced-ellipticity assertion does not supply the
Lorentzian domain or constraint reduction needed below.

## 2. Two different finite matching statements

### Formal inverse-coupling expansion

For arbitrary fixed smooth coefficients, there is a unique formal series
T=sum_(n>=1) h^n t_n of smooth differential expressions:

    t_1=-S_g,
    t_n=-P_g t_(n-1)-sum_(a+b=n-1, a,b>=1) Q(t_a,t_b), n>=2.

Coefficient comparison proves this recursively: the only occurrence of t_n
at order h^n is its identity term. No inverse of a principal symbol is used.
Every finite truncation has the stated higher-order residual; no convergence
or common function-space bound follows. This reuses the generic algebra of
the flat branch calculation with the actual printed coefficients.

### Exact finite spacetime jets

Fix a point x, an integer m>=0, and a linear splitting l_m of the genuine
holonomic jet truncation J_x^(m+1)E -> J_x^m E. Define

    f_m(h,u)=j_x^m F_h(l_m u).

The finitely many background coefficient jets are fixed numbers. Thus f_m
is polynomial in (h,u), even for a smooth background, and
f_m(0,0)=0, D_u f_m(0,0)=Id. The finite-dimensional analytic implicit
function theorem gives:

    for each x,m,l_m there is epsilon_(x,m,l_m)>0 such that
    for every |h|<epsilon there is u_m(h) with f_m(h,u_m(h))=0.

Each lifted finite jet has a smooth polynomial representative in a chosen
coordinate chart and trivialization. For h nonzero its R_kappa residual
vanishes through order m at x. This is an exact finite-jet conclusion, not
a neighborhood solution. The radii may shrink with m. The branches need not
be compatible across m or coincide with the highest jet components of the
formal full-field h-series. No fixed nonzero h, coherent infinite jet,
Fréchet implicit-function theorem, or kappa=1 solution follows.

**Countercontrol:** u+h(u'-f)=0 with f(x)=1/(1-x) has formal coefficients
at x=0 of magnitude (n-1)!, hence zero h-radius. Each fixed nonzero h still
admits ordinary local ODE solutions. Setting the top jet to zero separately
at each m yields exact finite jets with different u(0) at h=1/2. Neither
formal divergence nor incompatible chosen splittings proves nonexistence.

### What the curvature calculation actually forces

If a family of actual solutions has a C^(m+1) expansion T=h t_1+O(h²),
then t_1=-S_g. A transported flat leading coefficient -h S_flat therefore
has R_kappa=Delta S+O(h) in C^m. Wherever Delta S is nonzero it cannot
remain an exact small-h solution with that unchanged leading coefficient.
The [Schwarzschild second normal source jet](ricci-flat-ambient-source-jets-2026-11-27.md)
therefore requires a curvature-dependent leading response. It does not
obstruct an arbitrary allowed response, and introduces no new free choice.

## 3. Actual printed nonnull symbol: full exterior decomposition

Fix a unit nonnull covector tau=theta^0, eta_0=epsilon=+1 or -1,
Gamma=gamma_0, Gamma²=epsilon, and W=tau-perp of dimension13. We work
on the complexification of the full adjoint carrier. Clifford coefficients
are Cl(W)=Lambda*W. A transverse one-form is beta or Gamma beta;
longitudinal inputs theta^0 A are killed by tau wedge.

For the selected low-Phi comm/symi/symi dictionary, with the owned odd-q
Hodge normalization, direct substitution gives

    B=sum_(b!=0) eta_0 eta_b {gamma_0 gamma_b,T_b},
    (P_0 T)_0=sum_(b!=0) eta_b [gamma_b,T_b]-{gamma_0,B}/2,
    (P_0 T)_a=-eta_0[gamma_0,T_a]-{gamma_a,B}/2, a!=0.

These are verified against the nested-star Engine.Phi, rather than a
symmetrized Euler surrogate. An even-q Hodge convention is not covered.

For beta in U_p=W* tensor Lambda^p W, put

    F beta=sum_a eta_a e_a wedge beta_a,
    C beta=sum_a eta_a i_(e_a) beta_a,
    (E omega)_a=i_(e_a) omega,   (J omega)_a=e_a wedge omega.

Contraction includes the metric; the eta factors raise the one-form index.
Then FE=(p+1)Id, CJ=(14-p)Id, FJ=CE=0, and

    U_p=A_p direct-sum B_p direct-sum H_p,
    A_p=im E, B_p=im J, H_p=ker F intersect ker C.

The dimensions are binom(13,p+1), binom(13,p-1), and
13binom(13,p)-binom(13,p+1)-binom(13,p-1); out-of-range binomials vanish.
These are algebraic identities in a nondegenerate indefinite space, not
orthogonal projections in a positive physical norm.

For **odd p**, longitudinal output is zero and

    P beta=2epsilon Gamma(EF-Id)beta,
    P(Gamma beta)=2(JC-Id)beta,
    P²=4epsilon(Id-EF-JC).

The squares on A_p,B_p,H_p are respectively -4epsilon p,
-4epsilon(13-p),4epsilon. At p=13 the13-dimensional B_p contributes
13 chains beta -> -2epsilon Gamma beta -> 0.

For **even p**, the output (longitudinal, transverse) is

    P beta=(2C beta, 2epsilon Gamma JF beta),
    P(Gamma beta)=(-2Gamma F beta, 2EC beta).

Hooks are killed. A_p in the beta copy pairs with B_(p+2) in the Gamma
copy for p=0,2,...,10, with square4epsilon(p+1)(12-p). A_12 in the beta
copy is killed (dimension1). The remaining B_p beta channels map into
longitudinal grade p-1 (4095 two-chains); the A_p Gamma channels map into
longitudinal Gamma grade p+1 (4096 two-chains). Their images are independent.

| Quantity | Complex dimension / block count |
|---|---:|
| Full carrier | 229376 = 14 times 2^14 |
| Nonzero generalized eigenspace | 114660 |
| Zero Jordan blocks of size2 | 8204 |
| Zero Jordan blocks of size1 | 98308 |
| Rank P | 122864 |
| Kernel P | 106512 |
| Kernel P² | 114716 |

There is no zero chain of length3. The odd nonzero part has dimension
106470, the even nonzero part8190. Even and odd hook sums are each45057.
P² is diagonalizable, with nonzero eigenvalues

    4epsilon times ({1,12,22,30,36,40,42} union {-1,...,-12}).

For general nonnull tau, replace epsilon in these squares by its norm.
The generalized-zero projector is the polynomial
prod_(lambda!=0)(Id-P²/lambda) over the distinct listed square eigenvalues.
The inverse of P on its complement is also polynomial in P. No large
matrix inverse is needed.

**Native seam:** for O=sum_(b!=0) theta^b gamma_b and
V=sum_(b!=0) theta^b Gamma gamma_b, PO=-2epsilon V, PV=24O, hence
P²O=-48epsilon O. This is the actual printed operator, not W2 K.

The numerical dimensions above are complex algebra dimensions. To use them
as real ranks on full u(H), the actual source sharp convention and phases
must preserve that real form: commutators and i-anticommutators of
sharp-skew inputs are sharp-skew, Hodge is real, and complexification is
End_C(S128). The real-coefficient Clifford fixture alone is not a proof of
this physical adapter. No physical particle, ghost, or chiral count is made.
K95(q=5) and flipped K77(q=7) are separate exact fixture ports, not an
unproved identification of their physical pairings.

## 4. Frozen descriptor and the remaining PDE burden

For fixed coefficients and dependence on the single tau-coordinate only,
the linear operator is kappa Id+P_0 partial_0, kappa!=0. On its zero
generalized sector N²=0,

    (kappa Id+N partial_0)^-1=kappa^-1 Id-kappa^-2 N partial_0.

It consumes one derivative of a smooth forcing and imposes no compatibility
condition by itself. The complementary part is an ordinary ODE with
invertible P_0. Thus symbol singularity alone is not an obstruction to this
frozen inhomogeneous problem.

The full problem contains tangential P_a partial_a, moving projectors,
connection terms and the nonlinear Jacobian. They can mix these blocks.
The next unresolved datum is the actual constrained reduction/prolongation
for those terms and a justified solution/domain estimate. A whole-carrier
noncharacteristic CK invocation is unavailable because P(tau)(tau A)=0.
This does not rule out a constrained CK formulation after its constraints
are proved compatible.

The GU* wedge companion has zero longitudinal symbol output by its outgoing
companion identity. The selected printed P has explicit nonzero even-p
longitudinal channels above. Sharing an LC Einstein restriction therefore
does not identify their differential symbols. The table must not be
transferred to wedge GU*.

## 5. Controls, literature and claim ceiling

The [probe](../../tests/program-focus/printed_equation_jets_symbol_probe.py)
passes363 exact checks: nested-star versus compact formula and exterior
blocks in both odd-index ports; trace/top-chain/longitudinal controls;
binomial partition arithmetic; variable-coefficient nonlinear recursion
through order6; exact finite jets with a divergence/non-gluing countercontrol;
and the length-two frozen inverse. Representative blade tests are controls,
not a dense census. The written exterior proof covers the full carrier.

Reproduce with SymPy1.14.0:

    UV_CACHE_DIR=/private/tmp/gu-current-uv-cache uv run --offline --with sympy==1.14.0 python tests/program-focus/printed_equation_jets_symbol_probe.py --verify

The finite-dimensional IFT and noncharacteristic CK distinction are standard,
not novelty claims. See Gantumur's [authored CK notes](https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf),
§§4–5, for the latter hypotheses. The root's bounded literature check located
an [IFT proof](https://arxiv.org/abs/1708.02065); the elementary finite-jet
application is proved above, not attributed as a new general theorem.
No Lean or external-expert certification is claimed.

- **ESTABLISHED:** formal recursion; exact separately quantified finite
  residual jets; necessary curved leading coefficient; selected nonnull
  printed-symbol decomposition and frozen descriptor inverse.
- **RULED OUT as inferences:** source-jet forcing alone proves every
  completion impossible; a singular principal symbol alone proves the
  mass-shifted frozen equation insoluble. No matrix-cell kill is claimed.
- **NOT MODELED / UNDETERMINED:** actual curved endpoint solution at fixed
  kappa, kappa=1 Schwarzschild/Kerr lift, null symbol, full constrained
  evolution, physical positivity/readout, or a stable full GU* completion.

The weakest link to a physical GU conclusion remains the actual source
operator/convention and admissible solution/observation domain. Mathematical
breadth does not establish class-C representativeness. SOURCE's existing
I1B mismatch and GU* repair costs remain visible. No choice is adopted:
budget10 families/4 obligations/net6/0 source-selected predictions.
