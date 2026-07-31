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
