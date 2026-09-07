---
title: "K126 K125 Wilson Klein BV-BFV defect completion wave"
status: active_research
doc_type: reverse_scaffold_fixed_width_gauge_parity_bv_bfv_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K125_WILSON_PARITY_BV_BFV_POINT_DEFECT_COMPLETION
claim_ceiling: exact repository-owned Wilson covariance and Clifford-Klein parity completion, explicit formal fixed-width classical action/minimal BV-BFV data, and exact finite K124-regulator bounded-even Gauss-preserving quantum control, plus a free charge-block one-particle self-adjoint-extension theorem that does not realize the K115 Fock interaction; no continuum gauge Hilbert/domain theorem, renormalized point defect, complete interacting Haag-Kastler net, interacting NESS, source/GU ownership, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k126-k125-wilson-klein-bv-bfv-defect-completion-wave.json
probe: tests/channel-swings/k126_k125_wilson_klein_bv_bfv_defect_completion_probe.py
---

# K126 K125 Wilson/Klein/BV-BFV defect completion wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: fixed-width Wilson-dressed and Clifford-Klein parity-complete defect with formal classical BV-BFV data and finite-regulator quantum control
carrier: nine charged impurity states tensor one irreducible Cl_18(C) module tensor eighteen full Dirac CAR species tensor the K124 U(1)^8 link-electric regulator LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: Hilbert adjoint and CAR L2 pairing on the regulator; classical Dirac, impurity and Majorana first-order pairings plus Maxwell electric boundary pairing ON=repository_owned_fixed_width_control
real_structure: real u(1)^8 connection-electric variables, Hermitian adjoint, complex Dirac conjugation and neutral real Clifford-Klein generators
grading: total fermion parity, BRST ghost number and BV antifield degree
action_owner: repository-construction
target: local gauge covariance, total parity, explicit classical master/boundary identities, finite-regulator Gauss preservation and the remaining point-Fock/NESS release boundary MAP-TYPE=not-a-map
```

Scope: this packet binds one repository-selected fixed-width completion of
K125 and one free point-extension discriminator. It does not bind Weinstein's
action, a GU-native gauge group, a selected Wilson path or Clifford carrier, a
continuum quantum gauge representation, a renormalized point interaction,
nature's state/effect rule or an empirical observable.

## Inline preflight bookend

The maximum-depth frontier rebuild admitted six arcs. Wilson dressing and the
edge-Clifford parity carrier are independent route-changing constructions.
Their joint positive result releases the classical action/BV-BFV and finite-
regulator quantum packets. A charge-block one-particle extension is an
independent discriminator: it tests whether ordinary self-adjoint boundary
data already owns the point defect. The interacting NESS packet is conditional
on an interacting Fock-domain and scattering/correlation theorem. A
source-owned action remains dependency-blocked because the current
qualification registry has no complete candidate.

Mechanism retrieval separated this packet from K89's cylindrical BFV model,
K104's unrelated action/BV/Green control, K118's free nongauge continuum host,
K122's free CAR net, K123's undressed odd compact-smearing interaction, K124's
finite gauge regulator and K125's exact obstruction. No correction newer than
those inputs changes the charge, parity, gauge or point-domain typing used
here.

The route-changing lens census covered Abelian gauge theory, Wilson-line
geometry, graded CAR algebras, complex Clifford modules, constrained impurity
representations, classical variation, BRST/BV-BFV, self-adjoint extension
theory, defect AQFT, constructive QFT, open-system scattering, NESS, source
fidelity, representation typing and hostile philosophy of science. It selected
the Wilson-plus-edge-Clifford route because it repairs K125's two independent
failures without requiring a bipartite grading. A bare one-particle boundary
unitary was retained only as a discriminator, not promoted to the interacting
Fock theory. Computation exhausts the finite Clifford, charge and boundary-form
identities; it does not replace the continuum analytic theorem.

## 1. Wilson dressing repairs local gauge covariance at fixed width

Let the K115 edge `e=(u,v)` have the K124 vertex-difference charge

```text
b_e = q_v-q_u in Z^8.
```

Choose a cut on the spatial circle and, inside one fixed defect interval `I`,
a path from the defect point `0` to every `x` in the support of `f_e`. Define

```text
W_e(0,x;A) = exp(i integral_[0,x] b_e dot A),
Psi_e^W(f_e) = integral_I f_e(x) W_e(0,x;A) psi_e(x) dx.
```

With `A -> A+d alpha` and the annihilation-field convention
`psi_e(x)->exp(-i b_e dot alpha(x))psi_e(x)`, the transporter contributes the
endpoint phase

```text
W_e(0,x)->exp(i b_e dot(alpha(x)-alpha(0)))W_e(0,x),
```

and therefore

```text
Psi_e^W(f_e)->exp(-i b_e dot alpha(0))Psi_e^W(f_e).
```

The impurity transition `X_vu=|v><u|` transforms with the inverse phase at the
origin, so `X_vu Psi_e^W` is locally gauge invariant. This directly repairs
K125's local-phase mismatch. It does not select the path: different circle
arcs can differ by a Wilson holonomy, and the eight holonomy sectors remain
supplied data.

On K124's finite lattice the transporter is a product of unitary links. It
therefore preserves the CAR smearing norm bound. At fixed nonzero width this
is a bounded dressing; it does not alter K125's `epsilon^-1/2` point-limit
scaling or construct a point interaction.

## 2. An edge-Clifford carrier repairs total fermion parity

The K115 rook graph has triangles, so its nine vertices admit no parity
assignment making all 18 transition matrices odd. Introduce instead one
neutral odd self-adjoint Clifford-Klein generator `kappa_e` for each undirected
edge:

```text
kappa_e kappa_f + kappa_f kappa_e = 2 delta_ef,
P kappa_e P = -kappa_e.
```

The complex Clifford algebra `Cl_18(C)` has an irreducible 512-dimensional
module. The certificate constructs all 18 Jordan--Wigner gamma matrices on
nine qubits, checks every square, all 153 distinct anticommutators and their
anticommutation with total parity.

Now `X_vu` is even, `kappa_e` is odd and the CAR field is odd. Hence

```text
degree(X_vu kappa_e Psi_e^W) = 0+1+1 = 0 mod 2.
```

Every dressed defect monomial is both gauge neutral and fermion even. No
bipartite vertex grading is required. The 512-dimensional choice is a concrete
irreducible complex realization; this packet does not prove that this is the
minimal physically admissible completion or that any such auxiliary carrier
is source-selected.

## 3. Explicit fixed-width classical action and minimal BV-BFV data

A classical realization uses eight real Abelian connections `A^a`, eighteen
full Dirac fields `psi_e`, nine charged complex Grassmann impurity variables
`chi_v` with a one-occupancy multiplier, and eighteen neutral real odd
variables `kappa_e`. With `X_vu=bar(chi_u)chi_v`, the repository-selected
action is

```text
S = S_Maxwell[A] + sum_e S_Dirac[psi_e,A]
    + integral dt (i bar(chi) D_t chi
                   +(i/2) sum_e kappa_e dot(kappa_e)
                   -lambda(sum_v bar(chi_v)chi_v-1))
    + integral dt sum_e g_e
        (X_vu kappa_e Psi_e^W(f_e) + Hermitian conjugate).
```

The bilinear `X_vu` has origin charge `+b_e`; the dressed annihilator has
charge `-b_e`. The impurity bilinear is even and the remaining two factors are
odd, so the action is gauge invariant and Grassmann even term by term.

For odd Abelian ghosts `c^a`, set

```text
s A_mu^a = partial_mu c^a,       s c^a = 0,
s chi_v = i(q_v dot c)chi_v,     s bar(chi_v) = -i(q_v dot c)bar(chi_v),
s psi_e = -i(b_e dot c)psi_e,    s kappa_e = 0.
```

Wilson covariance gives `s Psi_e^W=-i(b_e dot c(0))Psi_e^W`. Commuting Abelian
charges and anticommuting ghosts give `s^2=0`, while edgewise charge and parity
cancellation give `sS=0`. The minimal functional

```text
S_BV = S + integral Phi^* sPhi
```

over the displayed fields therefore satisfies the classical master equation
`(S_BV,S_BV)=0`. This is an explicit formal classical statement. No nonminimal
gauge-fixing sector, regularized BV Laplacian, quantum master equation or
renormalized continuum measure is owned.

On a time slab the variation has the displayed bulk equations plus endpoint
potential

```text
Theta_Sigma = integral_Sigma dx
  (sum_a E^a delta A_x^a + i sum_e psi_e^dagger delta psi_e)
  + i sum_v bar(chi_v) delta chi_v
  + (i/2) sum_e kappa_e delta kappa_e,
```

up to the declared first-order convention. The corresponding Abelian BFV
charge is

```text
Omega_BFV = integral_Sigma dx sum_a c^a G_a,
G_a = partial_x E_a-rho_a^bulk-delta_0 rho_a^impurity.
```

The 18 dressed interactions commute with every `G_a`; the constraints commute,
so `{Omega_BFV,Omega_BFV}=0`. This boundary identity is classical and formal
at fixed width. It is not a constructed continuum physical Hilbert quotient.

## 4. Exact quantum consequence on the K124 finite regulator

On K124's finite lattice, replace the undressed compact CAR smearing by the
finite link-string dressing and tensor each transition with its bounded
`kappa_e`. For finitely many edges,

```text
||V|| <= 2 sum_e |g_e| ||f_e||_2.
```

Adjoint pairing makes `V` self-adjoint. The separate charge and grading checks
give `[G_a(j),V]=0` and `[P_total,V]=0`. Thus Kato--Rellich leaves K124's
electric domain unchanged for `H_0+V`; the Gauss kernel and even observable
algebra are invariant. Since `kappa_e^2=1`, each orthogonal reservoir channel
has the same `L_e^*L_e` coefficient as before the auxiliary completion, so the
K115 diagonal Davies rates are preserved edgewise; no coherent cross-channel
equivalence is claimed. This is an exact finite-regulator quantum theorem.

The same norm estimate is conditional in a continuum representation that
already owns unitary Wilson strings, CAR fields and a common free Gauss domain.
K125 supplied no such gauge Hilbert representation, so K126 does not claim it.
The Wilson paths live in the selected interval `I`; interval string support is
not point support, path independence or a complete causal Haag--Kastler net.

## 5. The ordinary one-particle point extension is insufficient

For the free first-order operator `D=-i d/dx` on the circle cut at the defect,

```text
Dom(D_U) = {f in H^1([0,L],C^m): f(L)=U f(0)}
```

is self-adjoint exactly when `U` is unitary. The boundary form cancels because
`U^*U=1`. If `[U,Q_a]=0` for all eight diagonal charge matrices, the extension
is gauge covariant and decomposes by total-charge block. The certificate checks
an explicit unitary block family and its boundary form.

This control does not realize K115. A one-particle boundary unitary preserves
one-particle number, whereas each K115 tunnelling term changes reservoir
occupation while changing the impurity/Klein state. A genuine point successor
must construct a common self-adjoint domain on the interacting Fock/Gauss
carrier, for example through an interior-boundary condition, counterterm,
quadratic form or resolvent limit. The free extension neither proves nor
excludes those routes.

## 6. The interacting NESS gate remains unreleased

Gauge covariance, evenness and finite-regulator self-adjointness do not supply
continuum reservoir correlation decay, a Moller or Ruelle morphism, convergence
or uniqueness of a stationary state, or physical-current identification. The
K115 ratio `6561/256` remains exact reduced-model truth and is not promoted to
an interacting field current.

## Inline postflight bookend

All six admitted arcs were attempted. Wilson transport repaired local gauge
covariance at fixed width, and the edge-Clifford module repaired total parity
without contradicting the triangular graph. Together they released the
explicit formal classical action, minimal BV functional, time-slab boundary
potential, Abelian BFV charge and exact finite-K124-regulator bounded-even
Gauss-preserving Hamiltonian. The point discriminator returned only the free
charge-block extension theorem: it does not reach the number-changing Fock
interaction. The NESS arc reached but did not pass its scattering/correlation
release condition.

- **Strongest overclaim caught:** a formal classical master equation plus a
  bounded finite-regulator Hamiltonian was initially close to being summarized
  as a continuum interacting gauge theory; the missing representation, common
  Fock/Gauss domain and causal-net theorem now remain explicit.
- **Strongest contrary route:** a genuine Fock-space interior-boundary
  condition or renormalized resolvent construction can evade the one-particle
  limitation and may make the fixed-width auxiliary Clifford carrier
  unnecessary.
- **Weakest reproducibility seam repaired:** the certificate constructs the
  full `Cl_18(C)` gamma family and checks all pairwise relations rather than
  encoding parity as a declared boolean; hostile review also caught a
  tautological first version of the charge-cancellation check and separated
  the frozen lead charges before mutation.

The eight gauge charges, eighteen auxiliary Clifford generators, eight spatial
holonomies, ten graph-cycle directions and real modular affinity remain
distinct. No source action, physical state, detector effect, Born rule,
held-out result, prediction, confirmation, canon, paper, release or public-
posture status changes.

## Next condition

Construct a continuum representation carrying the `U(1)^8` connection,
Wilson strings, CAR fields, Clifford-Klein impurity and one common self-adjoint
Gauss domain, then prove causal-hull locality or an honestly typed string-local
replacement. For a true point defect, construct the number-changing Fock-space
extension/IBC/counterterm/form/resolvent limit rather than substituting the
free one-particle extension. Only then prove reservoir correlation/scattering
control and an interacting NESS/current. Separately require an actual
source/GU action to select the charges, paths, carrier, coefficients and
boundary sector.

## Reproduction

```bash
python3 tests/channel-swings/k126_k125_wilson_klein_bv_bfv_defect_completion_probe.py
python3 tests/channel-swings/k126_k125_wilson_klein_bv_bfv_defect_completion_probe.py --selftest
```
