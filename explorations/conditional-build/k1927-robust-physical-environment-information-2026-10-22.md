---
title: "K1927: Robust physical information without a bath spectral gap"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite positive Hilbert models; no native GU, novelty or formal proof
scripts:
  - tests/channel-swings/k1927_robust_physical_environment_information.py
  - tests/channel-swings/k1927_robust_physical_environment_information_probe.py
---

# K1927: Robust physical information without a bath spectral gap

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
result: quantified physical information and finite catalytic resource construction
carrier: finite four-level system, physical environment and optional purifying reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, diamond norm and entropy in nats ON=independent_product_input
real_structure: complex adjoint; no native reality identification
grading: system population labels; not physical chirality
action_owner: repository-construction -- joint unitary; additive conservation explicitly imposed for thermal consumers
target: supplied extreme Schur channel and approximate return MAP-TYPE=intertwiner
```

## 1. Statement and conventions

Reuse the four-level target of [K1925](k1925-extreme-channel-information-consumption-2026-10-22.md):
v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,-i)/sqrt2,
Cij=<vj,vi>, Phi_C(|i><j|)=Cij|i><j|. Let U on S tensor E,
with arbitrary finite initial Omega_E independent of S, induce Phi.
No faithfulness, energy conservation, controlled-unitary form, or bound on
bath size is assumed here. Put epsilon=||Phi-Phi_C||diamond/2 and

    delta=sqrt(2 epsilon), eta=min(2,10 delta),
    b=delta+sqrt(eta), e=min(1/2,b),
    L(epsilon)=log2-h2(e), t=min(1,2sqrt(epsilon)),
    g(t)=2t log4+(1+t)h2(t/(1+t)).                       (1)

Here log2 and log4 mean ln(2), ln(4), and h2 is binary entropy in nats.
Let rho_j be the PHYSICAL E output for input |j><j|. Then

    D(rho_1,rho_2)>=max(0,1-2b),
    chi({rho_1,rho_2}/2)>=L(epsilon).                   (2)

For the average input (|1><1|+|2><2|)/2, with final environment rho_bar,

    S(rho_bar)-S(Omega)>=L(epsilon)-g(t).               (3)

The right side tends to ln2 as epsilon tends to0 uniformly over finite
bath dimension and spectrum, including rank-deficient states. Constants
are conservative; no optimal finite-error modulus is claimed. In contrast
to K1926, there is no state spectral-separation denominator.

## 2. Physical environment recovery: the missing transfer

Purify Omega in E tensor R, and let V:S -> S tensor E tensor R be the
actual Stinespring isometry. The R marginal is Omega_R for every input:
U acts only on S,E. The finite-dimensional Stinespring continuity theorem
[Kretschmann--Schlingemann--Werner, Theorem1](https://arxiv.org/pdf/quant-ph/0605009)
gives an isometry T:C2 -> E tensor R such that

    ||V-(I_S tensor T)V_C||op<=delta,
    V_C|j>=|j> tensor vj.                               (4)

If necessary enlarge E by a fixed pure spectator for the common-dilation
comparison. This is an analytical embedding, not an implementation resource;
any recovery on the embedding composes with adjoining that fixed spectator.
It leaves all physical trace distances and entropies unchanged. In particular,
we do NOT require the dilation-alignment unitary to preserve R.

Set N_R(X)=Tr_E(T X T*) and N_E(X)=Tr_R(T X T*).
Pure-state trace distance is at most vector norm distance, so for the four
projectors Pj=vj vj*,

    D(N_R(Pj),Omega_R)<=delta,
    D(N_E(Pj),rho_j)<=delta.                            (5)

The FIRST relation is essential: closeness of a purified complement alone
would not establish physical-environment information for a mixed bath.
Let Delta=N_R-[X -> Tr(X)Omega_R]. The four Pj span Hermitian(2).
Writing Eab=|a><b|, X=E01+E10 and Y=-iE01+iE10, we have

    X=2P3-P1-P2, Y=P1+P2-2P4,
    ||Delta(E00)||1,||Delta(E11)||1<=2delta,
    ||Delta(X)||1,||Delta(Y)||1<=8delta,
    ||Delta(E01)||1,||Delta(E10)||1<=8delta.             (6)

For ANY state on a qubit and an arbitrary ancilla, its two diagonal block
trace norms sum to1, and its offdiagonal block trace norms sum to at most1
(positivity factorization and Cauchy--Schwarz). Applying (6) to its block
expansion yields ||(Delta tensor id)(rho)||1<=10delta. The diamond norm
of a difference of channels is optimized on such states, hence

    ||N_R-replace_Omega_R||diamond<=eta.                (7)

Now apply the information-disturbance theorem (KSW Theorem3) to the
complementary pair N_E,N_R. There is a CPTP decoder D:E -> C2 with

    ||D N_E-id_2||diamond<=2sqrt(eta).                  (8)

Combining (5),(8), each decoded rho_j is within b of Pj. Thus the single
computational-basis measurement of the decoder distinguishes labels1,2
with average error at most b; random guessing improves this to e<=1/2.
The trace-distance and binary Fano/Holevo inequalities give (2). This is
an existential physical decoder; no claim that it is local, inexpensive,
energy conserving or experimentally available is made.

## 3. Entropy increase uses only the four-dimensional system

Let xi_j=U(|j><j| tensor Omega)U*, and xi=(xi_1+xi_2)/2.
Since Phi is epsilon-close to Phi_C, the probability that a system-basis
measurement on xi_j fails to return j is at most epsilon. Projection and
purification give a normalized postselected state |j><j| tensor zeta_j
within sqrt(epsilon) of xi_j. Its E marginal is within sqrt(epsilon) of
rho_j. Therefore

    D(xi,omega)<=t,
    omega=(|1><1| tensor rho_1+|2><2| tensor rho_2)/2.

Both states have the same E marginal rho_bar. Entropy invariance gives
S(xi)=ln2+S(Omega), whereas S(S|E)_omega=ln2-chi. Apply
[Winter, Lemma2](https://arxiv.org/pdf/1507.07775) to S|E with dim S=4:
|S(S|E)_xi-S(S|E)_omega|<=g(t). Rearranging gives (3).
Using entropy continuity on E instead would introduce an unnecessary bath
dimension. This proof allows arbitrary system population leakage and
coherences in Omega. All quantities are finite.

## 4. Released thermal, return and dimension consumers

Let E=B tensor A, Omega=tau_B tensor sigma_A, with tau_B a finite Gibbs
state at beta>0. Require [U,H_S+H_B+H_A]=0 and H_S diagonal in the target
basis. Let W_S and W_A be the energy bandwidths. For the same binary input,
exact energy and entropy accounting gives

    beta(F_A(initial)-F_A(final))
      = Delta S_E+I(B:A)_final+D(rho_B||tau_B)+beta Delta E_S.

Since |Delta E_S|<=W_S epsilon, (3) proves

    beta Delta F_consumed >= L(epsilon)-g(t)-beta W_S epsilon.  (9)

Coherent or nonfaithful catalysts and final correlations are allowed.
If r=D(sigma_A_final,sigma_A), entropy continuity and the centered energy
bound give

    beta r W_A+f_d(r) >= L(epsilon)-g(t)-beta W_S epsilon,       (10)

where f_d(r)=h2(r)+r ln(d-1) up to r=1-1/d and ln d above it.
For d=1 the left side is0. Return on ALL inputs implies this particular
average-input condition; the lower bound itself needs only that average.
With W_A=0 and epsilon,r tending to0, every family obeys

    liminf r ln d >= ln2.                               (11)

More generally (11) holds if beta r W_A and beta W_S epsilon tend to0.
This rules out bounded catalyst dimension in that limit. It does not rule
out growing catalysts: K1928 supplies constructions attaining the leading
coefficient, including exact channel implementations.

## 5. Other useful consequences and hostile boundaries

If the WHOLE physical environment, rather than just A, must return within
r on every basis input, (2) and the triangle inequality force
r>=max(0,1/2-b). A separate discarded thermal bath evades this environmental
return requirement; it need not return. This is consistent with K1928.

The four-projector tomography is necessary. A nonextreme dephasing channel
C=I4 can be realized with a maximally mixed Pauli bath whose conditional
states are all unchanged. A purified complement can carry the labels while
the physical bath does not. The complex fourth projector is needed to fix
the Y direction; three real projectors cannot supply (7). These are explicit
controls against the strongest false transfers. Independent finite controls
test the projector reconstruction, block inequalities, leakage conditioning
and entropy signs; they do not prove the KSW/Winter theorems or replace the
analytic uniform argument. No optimal epsilon exponent is asserted.

## Reproduction

Run with Python and SymPy installed, from the repository root:

```sh
python tests/channel-swings/k1927_robust_physical_environment_information.py
python tests/channel-swings/k1927_robust_physical_environment_information_probe.py
```

The producer recomputes and compares its committed JSON report; use `--write`
only when deliberately regenerating that report. 20 producer and16 separately reconstructed exact controls;2 mathematical faults
are detected after a green baseline, with1report and1dependency-pin fault
checked separately. Assertion failures are distinguished from crashes.
No unchanged predecessor certificate bank is replayed.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the southeast rival; SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass toy;
SC-META-53 remains UNCERTAIN about indefinite spectra. None selects these
positive Hilbert channels, bath, apparatus, energies or units. LT-SM8,
LT-GR6b and AC-F1 remain unchanged. K1828 raw-column completion and K1892
imported CAR do not supply the paired full20/K/C/domain/accessibility bridge.
No source-register, physics-ledger or canon verdict changes. Universal scope
rests on the analytic arguments; finite exact controls and numerical entropy
illustrations are supplementary. No novelty, independent expert, formal-proof,
physical GU, infinite-reservoir or total-work claim.
