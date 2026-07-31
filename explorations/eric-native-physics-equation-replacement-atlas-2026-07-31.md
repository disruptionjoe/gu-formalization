---
title: "Eric-native physics equation replacement atlas"
status: active_research
doc_type: exploration
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: lab/process/runs/GUH-20260731T153226Z-eric-native-equation-replacement-atlas/run-plan.md
registry: lab/process/eric-native-physics-equation-replacement-atlas.json
contract: lab/specifications/eric-native-equation-replacement-contract-2026-07-31.md
---

# Eric-native physics equation replacement atlas

## Result

Yes: the construction can now be organized as an equation-by-equation map
without returning to the empty statement that an external datum and source
action are needed.

The guided lane already has a bosonic source action and exact Euler packet.
The most coherent program is to treat that packet as one fourteen-dimensional
parent system. Maxwell, Yang--Mills, Einstein, Higgs/cosmology, and eventually
Dirac--Rarita--Schwinger are not separately inserted equations. They are
candidate low-energy blocks of one reduced Hessian and one odd extension.

This changes the central question from

> Which familiar physics equation should be added next?

to

> Which physical modes and equations does the frozen native action emit after
> one observation map, one stationary state, one quotient, and one Hessian?

That is both more GU-native and more informative. A single computation can
support or kill several legs at once.

The current boundary remains strict. The atlas records native parents,
candidate shadows, and downstream tests. It does not claim that the Standard
Model, Einstein gravity, quantum consistency, cosmology, chirality, or three
generations have already been recovered.

## What “replacement” means

Resemblance is not enough. Having a connection does not produce Yang--Mills;
having Clifford multiplication does not produce a physical Dirac equation;
having a vertical scalar does not produce the Higgs.

For a physical field \(\phi_i\), let \(\mathcal L_i\) lift it into the native
field space. The native action defines

\[
I_i^{\rm eff}[\phi_i]=I_Y[\mathcal L_i\phi_i],
\qquad
E_i^{\rm eff}=(D\mathcal L_i)^!E_Y.
\]

A familiar equation is earned only when the construction proves, on a closed
domain and after quotienting native gauge directions,

\[
E_i^{\rm std}
=Z_i\mathcal P_i(D\mathcal L_i)^!E_Y
+\mathcal O(M_i^{-1}).
\]

The lift, equation dual, projector, normalization, background, and error scale
must be frozen before the result is scored against familiar physics. Ordinary
pullback of differential forms is not enough because an Euler derivative is a
density-valued covector, not a field.

## The common native parent already built

The guided lane now has

\[
B=A_{\rm LC}(\epsilon_{\rm red},g_{\rm DW}),
\qquad T=A-B,
\]

and the action

\[
I_{G2}
=\int_Y T\wedge\mathscr S_\epsilon
\left(F_B+\frac12D_BT+\frac13q(T,T)\right)
+\frac{\kappa_1}{2}\int_YT\wedge\flat_1T.
\]

Its exact connection/distortion Euler equation is

\[
E_A=E_T
=\mathscr S_\epsilon(F_B)
+\frac12(L+L^!)T
+M_\epsilon(T,T)
+\kappa_1\flat_1T.
\]

The metric and reduction equations are the graph returns of this same action.
G3 also has the coupled gauge Ward identity, a preboundary potential
\(\Theta_{G3}\), the presymplectic current
\(\omega_{G3}=\delta\Theta_{G3}\), and the minimal ordinary-gauge BV packet
through antifield number one.

This matters because the program is not actionless. What is missing is a
target-blind completion of the odd terms and the maps that expose the
four-dimensional physical shadows.

## The science-council field/equation graph

```text
X^4 + declared finite datum d
        |
        v
Y=Met(X), reduction epsilon, metric g, connection A
        |
        v
B=A_LC(epsilon,g),  T=A-B
        |
        v
I_G2  --->  (E_A, E_epsilon, E_g, Ward, Theta, omega, partial BV)
        |
        +-- G3.5: enumerate/ablate target-blind native completions
        |
        +-- G4: L_d, R_d, equation dual, leakage, closed Krein domain,
        |       positive majorant, preboundary quotient
        |
        +-- solve one stationary native background
        |
        +-- compute one reduced bosonic Hessian
        |       |
        |       +-- massless connection modes -> photon/weak/strong candidates
        |       +-- spin-two quotient        -> Einstein candidate
        |       +-- heavy scalar mode        -> Higgs candidate
        |       +-- light scalar mode        -> cosmology candidate
        |
        +-- G5: freeze minimal odd action and compute its Euler/Hessian
                |
                +-- spinor zero-form block   -> Dirac candidate
                +-- spinor one-form complex  -> RS candidate
                +-- zero-order K pairing     -> Yukawa/mass candidate
                +-- action derivative        -> gauge/stress currents
                +-- physical index/readout   -> P3/generation test

Only after these arrows:
physical BV/anomaly test -> FLRW/PP3 test -> hostile Standard Model comparison
```

The useful feature is fan-out. One background and one Hessian decide whether
the same construction can simultaneously carry gravity, gauge modes, a Higgs
mode, and a distinct cosmological mode. It prevents separate sector-by-sector
fitting.

## Equation atlas in plain English

| familiar component | what the familiar equation actually does | Eric-lane native replacement candidate | present status | exact next construction |
| --- | --- | --- | --- | --- |
| Maxwell | propagates one massless abelian connection and couples it to conserved electric current | abelian zero mode of the reduced \(E_A=0\) Hessian; Bianchi supplies only \(dF=0\) | candidate shadow | find a unique massless abelian line, physical Hodge map, zero leakage, and action-derived current |
| Yang--Mills | propagates self-interacting nonabelian connections and receives a covariantly conserved current | exact G2 distortion equation \(E_A=E_T=0\) reduced through the equation dual | native parent built | reduce and linearize it; test whether \(D{*}F\)-behavior survives removal of an explicit \(F^2\) control |
| photon/weak/strong | selects \(su(3)\oplus su(2)\oplus u(1)\), charges, kinetic signs, and mass pattern | massless gauge algebra of the stationary quotient Hessian | candidate parent | classify the kernel before applying Standard Model names |
| Dirac matter | propagates spin-1/2 matter, defines current, and admits a mass bilinear | odd Euler/Hessian on \(\Omega^0(Y,S)\), reduced on a closed right-\(\mathbb H\) Krein domain | carrier only | enumerate and freeze minimal native odd terms, then vary once for both propagation and current |
| Rarita--Schwinger/chimeric sector | propagates a constrained spinor-valued one-form | odd complex on \(\Omega^1(Y,S)\), with Clifford image/kernel as kinematics | carrier only | build the action, constraint propagation, domain, and physical cohomology |
| Higgs/EWSB | supplies a stable doublet, VEV, photon-preserving symmetry breaking, and weak masses | selected scalar block of the same reduced Hessian, provisionally in the vertical coefficient of \(T\) | candidate parent | obtain a stable heavy scalar and its gauge incidence without inserting doublet/hypercharge/potential |
| Yukawa/mass | couples left/right fermions through the Higgs and creates a constrained mass spectrum | zero-order block of the odd operator, using the admitted Krein-paired channel \(K e_{\rm vertical}\) | candidate parent | derive \(P_0,\rho(\Phi),Y_K,Y_C,C\)-reality and mirror gap from a written term |
| Einstein gravity | propagates two massless spin-two modes and couples universally to stress | equation-dual reduction of the exact \(E_g,E_\epsilon,E_A\) system | native parent built | isolate the spin-two quotient in the shared Hessian and test sign, mode count, symbol, and source universality |
| source conservation | makes gauge and gravitational sources compatible with symmetry | G3's coupled Ward identity across all field owners | identity built | extend it after matter is added and descend it with boundary flux included |
| cosmological sector | supplies a state-dependent vacuum source and its gravitational stress | stationary scalar/trace blocks of \(T,E_T,E_g,E_\epsilon\), matching Eric's distortion/olive grammar at proposal level | candidate shadow | derive the observation stress and split heavy Higgs-like from light cosmological modes |
| FLRW/PP3 | turns the source into \(H(z),\rho,p,w(z)\) and a falsifiable prediction | homogeneous restriction of the derived reduced metric/distortion equations | downstream test | run only after the state and amplitude owner are frozen; do not use PP3 to construct them |
| quantum/BV | removes gauge redundancy and defines the physical phase space and quantum obstruction problem | G3 preboundary/presymplectic and partial ordinary-gauge BV packet | partial BV | complete domain/BFV and the matter/diffeomorphism/RS owner complex |
| anomaly cancellation | checks quantum consistency of the emitted chiral spectrum | determinant/Pfaffian anomaly of the eventual physical odd complex | downstream test | compute after the group, representation, chirality, and domain are frozen |
| three generations | counts stable physical fermion modes or records a supplied count honestly | family index/readout of the eventual reduced odd complex; not the current three provenance blocks | downstream test | attach P3 only after a physical Fredholm domain/readout exists |
| external datum | carries finite orientation/channel/count choices without fitting the dynamics | conditional family \((I_d,E_d,L_d,R_d,D_d)\) | candidate parent | build G4 uniformly over P1/P2/P3 and record exactly where each datum is consumed |

The machine registry contains the full equations, source anchors, observation
maps, construction obligations, kill conditions, and datum debits for all
fifteen rows.

## Primary-source callouts as native construction directives

These callouts are not passive citations. A direct Weinstein statement is
used to identify where the corresponding object should be sought in the
native parent geometry. If the source stops before a formula or proof, the
atlas continues with the source-shaped carrier, action, reduction, or spectral
test; “not supplied” is provenance, never the terminal result.

The source labels are deliberately disambiguated:

- **Oxford/Portal**: the 2013 Oxford address with the 2020 Portal preface and
  supplementary presentation, locally archived as
  [`portal-special-gu-first-look-2020-04-02.md`](../lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md);
- **TOE 2025**: Curt Jaimungal's *Geometric Unity: 40 Years in the Making*,
  locally archived as
  [`toe-weinstein-gu-40-years.md`](../lab/sources/transcripts/toe-weinstein-gu-40-years.md);
- **ITI/UCSD 2025**: the later Into the Impossible/UCSD seminar, locally
  archived as
  [`weinstein-ucsd-2025-04-transcript.md`](../lab/literature/weinstein-ucsd-2025-04-transcript.md);
- **ITI 2021**: Brian Keating's earlier *Geometric Unity Revealed* official
  editorial transcript; and
- **GU Draft 2021**: the author's working draft, used where a formula rather
  than a spoken description controls.

| component | primary-source callout | what it directs us to seek in the GU-native parent | source/Layer-0 guard |
| --- | --- | --- | --- |
| Maxwell | Oxford/Portal `02:40:24`; TOE 2025 `01:44:45--01:45:42` | Do not add Maxwell separately. Search for the unique closed massless abelian summand of the same reduced G2/G3 connection Hessian that carries the nonabelian sector; then construct its physical Hodge map and action-derived electric current. | The sources give a square/abelianization relation, not the photon quotient or Maxwell equation. |
| Yang--Mills | Oxford/Portal `00:43:47`, `01:59:12--02:03:07`; TOE 2025 `00:41:50--00:43:38`; ITI/UCSD 2025 `00:05:43--00:06:32`; GU Draft 2021 §9.1 | Treat the exact first-order G2 Euler packet as the square-root parent. Its reduced second variation must contain a nonabelian propagation/current block that intertwines with (D_A{*}F_A=J) after the explicit (F^2) control is removed. | Oxford first displays the conventional equation and then a proposed replacement. A connection or Bianchi identity alone is not Yang--Mills dynamics. |
| Einstein gravity | Oxford/Portal `00:42:16`, `01:43:32--01:46:17`, `02:35:10--02:40:19`; TOE 2025 `02:14:44--02:23:28`; ITI/UCSD 2025 `00:09:46--00:30:05`; GU Draft 2021 §9.1 | Layer-0 identify the corrected G2 Euler covector with the total-swervature/displasion role, apply the G4 equation-dual pullback to (X), and isolate the gauge-quotiented massless spin-two block of the shared Hessian. | The spoken replacement lives on (Y) and must be pulled back. It is not yet a two-mode physical graviton theorem. |
| Higgs | TOE 2025 `01:35:23--01:36:08`; ITI/UCSD 2025 `00:42:42--00:43:47`; Oxford/Portal `02:40:24--02:41:39`; GU Draft 2021 §12.9 | Search in the vertical ad-valued one-form coefficient of (T), not an added scalar bundle. Require one action-selected Hessian mode whose curvature expansion emits its kinetic, quadratic, and quartic terms and whose minimal coupling is the same incidence map used by the (K)-paired fermion zero-order block. | “Ad-valued one-form” and “scalar mode” are origin/carrier statements, not yet the observed doublet, VEV, or Yukawa map. |
| Dirac | Oxford/Portal `00:45:44`, `01:57:48--02:03:07`, `02:40:24--02:41:16`; TOE 2025 `02:35:07--02:42:55`; ITI/UCSD 2025 `00:34:27--00:36:13`, `00:46:02`; GU Draft 2021 equations (9.18)--(9.20), §12.9 | Build the odd action on (Omega^0(Y,S)oplusOmega^1(Y,S)) as the square-root partner of G2/G3. Its rolled Euler/Hessian complex must jointly emit Dirac/RS propagation, the (K)-paired VEV/mass channel, current, and constraints before reduction. | Oxford explicitly says the Dirac piece was unfinished at that release. The carrier nevertheless gives a concrete construction target. |
| Schrödinger evolution | No direct GU-native Schrödinger equation was located. Nearest directions: Oxford/Portal `00:47:35`; ITI 2021 `00:31:42`; TOE 2025 `00:14:17`. | Follow the source's broader instruction to geometrize the quantum: after G4 constructs the reduced BV/BFV phase space and positive Krein majorant, derive its Hamiltonian flow from the action and test whether the physical one-parameter evolution is unitary and admits (i\partial_t\Psi=H_{\rm phys}\Psi). | This route is a repo synthesis from the source's quantum-geometry direction, not an equation spoken by Weinstein. Generic wavefunction or Dirac-square language is not silently renamed Schrödinger. |
| weak force | Oxford/Portal `00:43:47`, `02:08:36`; ITI/UCSD 2025 `00:32:46`, `00:40:27--00:46:40`; TOE 2025 `02:50:38--02:53:14` | Compute the action-selected maximal compact stabilizer of the stationary quotient. Test whether its massless and odd modes jointly emit (SU(2)\times U(1)), chiral currents, the Higgs incidence, photon-preserving breaking, and a (W/Z) mass block. | The sources make group/representation and breaking claims, not a separately derived weak field equation. “Dark weak” at Oxford `02:08:36` is a distinct proposed sector. |
| strong force | Oxford/Portal `00:43:47`, `02:08:36`; ITI/UCSD 2025 `00:40:27--00:46:40`; TOE 2025 `02:50:38--02:53:14` | From the same stabilizer, test for an (SU(3)) massless connection factor with positive kinetic form and the correct odd-mode incidence. Derive its current and self-coupling from the reduced native action before asking about running or confinement. | The sources place color in a maximal-compact/Pati--Salam branching. They do not supply QCD dynamics, confinement, or a gluon quotient. |
| dark energy | ITI/UCSD 2025 `00:03:06`, `00:09:46--00:27:00`; TOE 2025 `02:14:44--02:23:28`; Oxford/Portal `01:44:16`, `02:09:22--02:10:44`; GU Draft 2021 §9.1 | Use (T=A-B) and the coupled (E_T,E_\epsilon,E_g) family. Solve a stationary scalar/trace branch, derive its observation stress and Ward identity, and isolate a light cosmological Hessian mode distinct from the heavy Higgs mode before FLRW/PP3. | The sources give the distortion/VEV direction. They do not give PP3's quantitative sign, amplitude, or (w(z)) locus. |
| dark matter | ITI/UCSD 2025 `00:38:09--00:41:24`; TOE 2025 `02:33:47`, `02:37:37`, `02:50:38--02:53:14`; Oxford/Portal `02:08:36--02:10:44` | Define the luminous observation image inside the physical odd complex and study its orthogonal/cohomological complement. Branch that complement under the stationary stabilizer, derive masses/charges from the common zero-order operator, and test high-curvature recoupling as mixing in the same family. | These are spectrum/representation claims, not a mass, abundance, stability, cross-section, or cosmological-fit calculation. Dark matter is not the TOE DESI/dark-energy claim. |

The machine-readable crosswalk records these ten routes under
`requested_source_crosswalk`, and each corresponding atlas component points
back to its callout id. The key use is prospective: the passages constrain
where and how to look inside the native construction while the hostile
intertwining and empirical gates still decide whether the proposed object is
actually present.

## What each specialist changed

The same ten specialist lenses were asked for a replacement map, not for a
fresh diagnosis that a datum/action was absent.

1. **Affine and differential geometry.** Distinguished field restriction
   from Euler-covector reduction. It requires a stabilizer reduction
   \(r_\epsilon\), lift \(L_s\), and formal transpose \((D L_s)^!\).
2. **Group cohomology and gauge groupoids.** Kept the inhomogeneous/tilted
   grammar but typed the fixed-reference quotient as an adjoint-distortion
   groupoid. It cannot be silently identified with \(\mathcal A/G\).
3. **Symplectic geometry and BV--BFV.** Made the G3 preboundary form the seed
   of the physical quotient, not proof that a boundary polarization already
   exists.
4. **Calculus of variations.** Required every current and physical equation
   to be an Euler derivative of the same frozen action. This rules out
   inserting a convenient current after the fact.
5. **Krein/quaternionic operator theory.** Required the physical positive
   structure, right-\(\mathbb H\) domain, and mass bilinear to be built
   together. In particular the pairing \(K\) remains part of the mass map.
6. **Hyperbolic and boundary PDE.** Required a closed admissible domain,
   normal operator, leakage test, and boundary quotient because signature
   \((9,5)\) has no ordinary thirteen-dimensional spacelike Cauchy surface.
7. **Clifford, index, and generation theory.** Kept the
   \(\Omega^0\oplus\Omega^1\) and Clifford image/kernel decomposition as a
   carrier while forbidding a block-to-count inference. P3 enters only at a
   physical Fredholm/readout map.
8. **Standard Model representation theory.** Required the physical gauge
   algebra and representations to be read from the stationary quotient
   Hessian before comparison with \(su(3)\oplus su(2)\oplus u(1)\).
9. **Higgs/Yukawa specialist.** Separated an admitted vertical scalar channel
   from an actual Higgs. The latter still needs a doublet representation,
   stable potential, VEV, gauge-boson mass map, Yukawa incidence, and mirror
   gap from one action.
10. **Gravity and cosmology.** Required the heavy Higgs-like and light
    cosmological modes to be two Hessian modes of one parent and required
    observation stress before any \(w(z)\) claim.

## Science-council synthesis

The council's strongest recommendation is not to construct the familiar
equations in the order textbooks present them. The efficient order follows
shared dependencies:

1. **G3.5: target-blind census and ablation.** Enumerate natural native action
   and odd terms from the declared geometry. Remove explicit Einstein,
   Yang--Mills, Dirac, Higgs/Yukawa, and cosmological controls one by one.
2. **G4: observation/domain packet.** Build \(L_d,R_d,(D L_d)^!\), differential
   intertwining, leakage zero, closed Krein domain, positive majorant, and
   preboundary quotient uniformly over the datum family.
3. **Stationary native backgrounds.** Solve the complete coupled G2/G3 Euler
   system before interpreting any mode.
4. **One reduced bosonic Hessian.** Compute its gauge, spin-two, and scalar
   blocks without Standard Model or cosmological labels. This is the next
   highest-information swing.
5. **G5 minimal odd extension.** Freeze one target-blind matter action and
   derive the Dirac/RS operators, zero-order mass block, currents, and extended
   Ward/BV identities together.
6. **Name low-energy physics last.** Only surviving native modes may be
   compared with the photon, weak/strong gauge fields, graviton, Higgs,
   cosmological mode, and observed fermions.
7. **Run downstream gates.** Anomalies, physical index/count, FLRW/PP3, and
   hostile Standard Model comparison occur after the relevant choices are
   frozen.

This order has a decisive control. If a familiar equation appears only when
its dedicated conventional term is restored, it is **supplied**, not
emergent. The conditional native family continues either way, so a negative
sector result is informative without stalling the whole construction.

## Datum policy: build through it, not around it

For declared finite datum \(d\), construct the entire family

\[
(I_d,E_d,L_d,R_d,\mathcal D_d).
\]

The action and native background are not selected by the desired Standard
Model output. The datum is consumed only at its typed arrow:

- P1: a possible orientation/sign/domain choice;
- P2: a channel datum whose type is still to be constructed;
- P3: the count datum, consumed only at a physical index/readout.

This gives the external datum a real mathematical job without allowing it to
become a bag containing the gauge group, charges, Yukawa matrices,
cosmological amplitude, or target projectors.

## Source provenance and boundaries

The transcript claim identifiers used here are owned by
`lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md`. In particular,
the atlas uses the action architecture (`WG-SA0`, `WG-B01`, `WG-B04`--`B06`,
`WG-SH1`), ad-valued-one-form Higgs (`WG-C02`), fermion carrier and generation
labels (`WG-F01`--`F04`), effective chirality/curvature-linked mass proposals
(`WG-F08`, `WG-F09`), rolled complex (`WG-X01`, `WG-X02`), and dynamic
dark-energy grammar (`WG-DE1`--`DE3`).

Those source claims generate candidate constructions; they do not override
the results of exact variation or the Layer-0 typing. The killed compressed
G2 Euler shortcut remains killed. The transcript's qualitative DESI/dynamic
dark-energy claim does not by itself contain the repo's quantitative PP3
prediction.
