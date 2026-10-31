---
title: "K2338 Actual contact resonance and finite resource limits"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, survey or hardware acceptance
scripts:
  - tests/channel-swings/k2338_resonant_contact_resource_boundary_probe.py
---

# K2338 Actual contact resonance and finite resource limits

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
result: K2338
carrier: K2336 full Fock cavity plus mediator and neutral qubits with a protected reference spectator LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and restricted-input half-diamond channel distance ON=declared_carrier
real_structure: real coefficients and complex adjoint where required
grading: conserved local excitation; enlarged contact sectors
action_owner: repository-construction -- unchanged exchange plus matched longitudinal Hamiltonian, explicit control caps and optional loss model
target: fixed-angle contact failure, resonance containment and certificate optimization MAP-TYPE=evaluation
```

## Outcome and fixed microscopic object

[K2336](k2336-dispersive-contact-realization-2026-10-30.md) correctly charges its exchange remainder times the actual contact time. Here a small h/D is shown insufficient even at the PREDECLARED pi/2 echo angle, on an allowed input of the contact-channel specification. This strengthens its arbitrary-long-time example. Finite simultaneous resource caps reduce the complete sufficient certificate to one scalar minimization; a separate exact loss bound identifies a genuine channel limitation. None is a hardware measurement or a failure of every implementation.

Retain Hmic=D Pf+Delta Pe+g(a e+ +a† e-)+h(a f+ +a† f-)+chi(Pe Zf+Pf), chi=-h²/D, Zf=1-2Pf. The ideal contact is H0+chi(n+Pe)Zf after the physical neutral phase correction. Reference photons are spectators. Source ACT01/GEO55 ASSERTS and META53 UNCERTAIN, ledger0.263 and GU verdicts remain unchanged. This is a supplied positive-Hilbert device model, not GU quantization.

## Resonant failure at the actual echo time

Set g=h>0, Delta=D>0, x=D/h>=2, E=D-h²/D, Omega=sqrt(E²+8h²). Choose initial |nP=0,nR=N,e=0,f=1>, allowed by the lower optical-mediator vacuum label and arbitrary neutral state in the declared contact-channel domain. This does not assert that the correlated echo flag in the compiled K2334 circuit actually reaches this input. Its invariant local one-excitation basis (one cavity photon, mediator excited, neutral excited) has

    H=[[0,h,h],[h,E,0],[h,0,E]].                      (1)

The target corrected contact keeps the initial state unchanged. With delta=(Omega-E)/2 and w=(1-E/Omega)/2, the exact mediator-transition amplitude is

    A(t)=1/2[(1-w)e^[-i(E+delta)t]+w e^(i delta t)
                                      -e^(-iEt)].   (2)

This follows by separating the dark state (e-f)/sqrt2 and the bright state (e+f)/sqrt2. A subsequent phase on f cannot erase mediator population. Hence the actual pure-state trace distance from the ideal target, and therefore restricted-input half-diamond distance, is at least |A(t)|.

Take t=pi D/(2h²), exactly |chi|t=pi/2, the prescribed echo angle. This tests the specified contact channel at that angle, not the error of the entire compiled instrument. Rationalizing delta and using x>=2 gives

    pi/(1+x^-2)<=delta t<=pi,
    w<=2/(x-1/x)²,
    |A(t)|>=sin(delta t/2)-w
           >=1-pi²/(8x^4)-2/(x-1/x)².              (3)

For the lower phase inequality use Omega/h<=x+3/x; the upper uses Omega/h>=x+1/x. The sine estimate is cos u>=1-u²/2. At finite rates h=g=1,Delta=D=10,chi=-1/10,t=5pi, (3)>0.9794. The phase correction exp(iDt Pf) is exactly identity at this fixture. As x grows the error lower bound tends to1 while h/D tends to0. No arbitrary extra wait was introduced. K2336's valid sufficient bound becomes large here; its theorem is not contradicted. Adding noise/control perturbation of channel distance <=eta reduces this lower bound by at most eta.

## A scoped nonresonant repair

For arbitrary Delta, the same sector has cavity/mediator block A0=[[0,g],[g,Delta+chi]], neutral level E_f=D+chi and coupling h into the cavity. Define d=dist(E_f,spec A0). If d>2|h|, Weyl bounds isolate one eigenvalue lambda within |h| of E_f. Its normalized eigenvector v satisfies ||v_ce||<=r |v_f|, r=|h|/(d-|h|), by the resolvent equation. Decomposing f along v and its orthogonal complement gives

    ||(1-Pf)e^(-itH)f||<=2r/sqrt(1+r²)<=2|h|/(d-|h|) (4)

for ALL t. This suppresses the actual exchange failure, but does not certify the matched phase, multi-excitation gate or whole instrument. Near resonance d is small even if |D| is large. Timing, ramps and physical phase resources still have to be charged.

## Exact finite-cap reduction of the sufficient instrument budget

Now fix N, mediator g, noise rates, input/control errors and K2334 constants A=A'_N>0,B=B_N>0,G. Declare JOINTLY ATTAINABLE independent caps |h|<=H, |D|<=Dmax, |chi|<=X, g1<=G1, |Jzz|<=Z1, J<=Jmax, all positive. Amplitude-dependent noise or coupled engineering constraints require a different feasible set; marginal maxima from unrelated devices cannot be combined.

Put rho=|h/D|, beta=sqrt(N+1), q=ceil(log2(N+2)), dreg=2^q, C=q+2N, K=pi(N+1-1/dreg), a0=2beta(N+2). Since |chi|=h rho, the contact contribution of K2336 is exactly

    F(rho,h)=2C beta rho
       +K exp(2beta rho)[|g|/h+a0 rho]
       +lambda_c K/(h rho).                        (5)

At fixed rho it decreases in h, so the optimal h is

    h*(rho)=min(H,Dmax rho,X/rho).                  (6)

The full bound minimizes neutral time at G1,Z1. Hopping minimizes A J+lambda0 B/J at J*=min(Jmax,sqrt(lambda0 B/A)) when lambda0>0. When lambda0=0 the infimum is approached as J downarrow0; it is not attained at a forbidden zero-rate pulse. Neutral overhead is lambda0[G(3pi/(4Z1)+12pi/G1)+C pi/G1]. Input/control errors add unchanged. Thus one remaining scalar minimization of F(rho,h*(rho)) gives the global optimum of THIS certificate under these assumptions. Candidate piece boundaries are H/Dmax,sqrt(X/Dmax),X/H; retain only boundaries actually on the minimum envelope.

If g!=0 and caps are finite, F tends to infinity at both ends: as rho downarrow0, h*<=Dmax rho; as rho grows, exponential and endpoint terms diverge. Continuity ensures an attained global minimum. These are useful lower bounds on the certificate:

    F>=K|g|/H,
    F>=K|g|/H+2sqrt(2C beta lambda_c K/H) if lambda_c>0. (7)

They are NOT lower bounds on physical error. A minimum above tolerance means this conservative K2336 certificate cannot approve the capped family. It does not prove the apparatus fails. Explicit physical error(3) and the next bound have a different logical status.

## Executed optimization: unique minimum and a finite capped witness

The scalar problem is stronger than an unspecified numerical search. Write F as max(F_D,F_H,F_X), substituting h=Dmax rho,H,X/rho respectively. Each is strictly convex for rho>0: exp(b rho)/rho has second derivative exp(b rho)[(b rho-1)²+1]/rho³>0; exp(b rho)rho, exp(b rho),1/rho and1/rho² have the needed convexity, and the common positive exp(b rho)rho term is strictly convex. A finite maximum of strictly convex functions is strictly convex. With the endpoint coercivity already proved, there is exactly one minimizer, either a branch's derivative zero or a cap-switch kink. This gives a certified bracketing method rather than multiple local optima.

For a fully finite mathematical fixture use N=2,g=7/10,H=100,Dmax=10^6,X=1,lambda_c=10^-6. Then beta=sqrt3,C=6,K=11pi/4; h*=Dmax rho up to rho0=10^-4, h*=H until rho=1/100, then h*=X/rho. At rho0 the left derivative is negative and the right positive. Rational bounds beta in(3/2,7/4), K in(8,121/14) prove this directly: the left exponential bracket is at most (7/10)/(10^6 rho0²)(2beta rho0-1)+2beta*4*(1+2beta rho0)<-55, while the endpoint term is below21 and loss derivative is negative. The right derivative exceeds18+8*12-9>0. Thus the UNIQUE global contact-certificate minimizer is exactly rho0, h=100,D=10^6,|chi|=1/100.

Using exp(2beta rho0)<1001/1000 from exp(y)<=1/(1-y), its contact certificate is bounded above by the exact rational

    21/10000 + (121/14)(1001/1000)(7/1000+14/10000)
                   + (121/14)/10000 < 2/25.        (9)

This certifies only the contact contribution below0.08. Hopping, neutral overhead, input/control errors and fresh-register/reset assumptions still add through the full formula. It does not certify a whole instrument or any measured device. The example shows how jointly bounded rates can be evaluated without invoking an unbounded dispersive limit.

## Released physical loss floor, separate from certificate failure

During the contact additionally stipulate equal independent amplitude damping sqrt(gamma)a, sqrt(gamma)e-, sqrt(gamma)f-, with reference inert and no excitation-adding control. The initial state above has local excitation Kloc=n+Pe+Pf=1. Hmic preserves it; sum L†L=gamma I on that sector. Any jump lands in absorbing local vacuum. Thus survival is exactly exp(-gamma t), independent of detuning or coupling. Ideal matched contact preserves the excitation; measuring local vacuum gives the genuine channel lower bound

    distance>=1-exp(-gamma t).

For a target accumulated contact angle theta with |chi(t)|<=X, t>=theta/X, so

    distance>=1-exp(-gamma theta/X).                (8)

Time-dependent excitation-preserving controls obey the same survival law. This exact contact-class bound is not a claim about error-correcting encodings, excitation-adding replacements, heralded acceptance or a different full readout. Fresh pure registers and reset remain priced resources. The neutral damping hypothesis is additional to K2336's example dephasing model.

## Evidence and next decision

The probe checks exact dark/bright reduction, actual finite propagators at the prescribed time, the finite-cap algebra, cap feasibility and certificate lower floors, resolvent repair controls and exact one-excitation Lindblad loss. Mutations change detuning, target time, contact coefficients, caps or jump operators; a baseline failure/crash is never counted as a detected fault. Numerical propagators are finite controls; the general bounds use the written proofs. [Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675) provides established effective-Hamiltonian context, not a certification of this device.

Next obtain one device's joint feasible set, including signed detuning, longitudinal matching, spectator isolation, clocks/ramps and loss/reset costs. Then evaluate(5)-(6), and if conservative failure occurs test the actual channel with resonances retained. The exact counterexample rules out ratio-only certification, not all dispersive contacts. No physical feasibility follows from arbitrarily increasing h and D.
