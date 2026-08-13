---
status: completed
repository: gu-formalization
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-RB6
---

# RB6 target-blind source-concomitant grammar

## Target

Continue the source-action/external-datum construction without reopening the
already-settled statement that a complete complex--Cartan flag is missing.
RB6 asks whether existing source-owned geometry can generate the operators
needed by RB5's conditional calculus:

\[
H\longmapsto P_-=\mathbf 1_{(-\infty,0)}(H),
\qquad
Q\longmapsto J=Q(-Q^2)^{-1/2}.
\]

The grammar, contractions, and rejection rules are frozen before any
candidate spectrum is read.

## Prior-work and non-duplication and non-duplication

The completed July 29 packet
`source-owned-reduction-transport-packet-2026-07-29.md` already computed the
W177 Yang--Mills residual:

\[
\|D_{A_0}^*F_{A_0}\|\simeq3.19904
\]

with relative scale spread \(3.11\times10^{-6}\) and signal/control-floor
separation \(858.6\). Therefore the W177 background is already
`W177-AMBIENT-YM-NONSTATIONARY`, and its quadratic form is already killed as
a physical fluctuation Hessian. RB6 will re-run that control but will not
claim it as a new result or duplicate its implementation.

The unrelated untracked native-packet source audit remains outside this run's
write boundary.

## Construction fork

Load-bearing objects use the program-native construction:

- \(Y^{14}=\operatorname{Met}(X^4)\) with canonical
  \(TY=TX\oplus\operatorname{Sym}^2T^*X\), not the exterior numerical ten;
- the vertical trace-reversed DeWitt metric of signature \((6,4)\), not raw
  Frobenius \((7,3)\);
- indefinite/Krein adjoints, not positive-Hilbert adjoints; and
- the W131/W177 gimmel Levi--Civita curvature only on its already-declared
  conditional ambient branch.

Standard differential geometry supplies control identities and natural
concomitants; it does not silently replace these native objects.

## Layer 0

| phrase | RB6 object | not identified with it |
| --- | --- | --- |
| vertical endomorphism | a map of the canonical rank-ten \(\operatorname{Sym}^2T^*X\) fibre | an endomorphism of an exterior \(6+4\) ten |
| \(H\) | a DeWitt-self-adjoint source concomitant on that fibre | the RB5 planted flag selector or a physical Hessian |
| \(Q\) | a DeWitt-skew source concomitant on that fibre | charge conjugation, a Dirac operator, or a supplied complex structure |
| negative spectral sector | the result of a predeclared sign rule | a post-selected rank-four physical sector |
| curvature | W177 gimmel Riemann curvature on the conditional ambient branch | the independent \(X^4\) IG gauge curvature |
| stationarity | \(D_{A_0}^*F_{A_0}=0\) for the declared ambient Yang--Mills sector | stationarity of the full coupled GU source action |
| spectral multiplicity | an eigenvalue degeneracy or projector rank | a particle family, generation, index, or count |
| trace reversal | the DeWitt fibre pairing and its trace/traceless involution | the full Standard Model flag |

## Ratified L1--L7 packet

| axis | RB6 class |
| --- | --- |
| L1 | smooth associated bundles over the specific smooth \(Y^{14}\) |
| L2 | no computational observer; the canonical base/vertical bundle split only |
| L3 | smooth tensor contractions with gimmel/DeWitt invariant pairings |
| L4 | ambient pseudo-Riemannian \((9,5)\); no global causal-order claim |
| L5 | specific-object concomitants, not an RG/universality class |
| L6 | no coordination loop |
| L7 | indefinite DeWitt/Krein signature; no probability rule inferred |

This is not a claimed no-go escape and carries no chirality/count bridge.

## Frozen admissible grammar

Inputs may include only already source-owned tensors on the conditional W177
ambient branch:

- the gimmel metric \(G\), its inverse, and canonical base/vertical bundle
  projections;
- the trace-reversal tensor on
  \(\operatorname{Sym}^2T^*X\);
- \(R_{IJKL}\), \(\operatorname{Ric}_{IJ}\), scalar curvature, and covariant
  derivatives already needed for the W177 residual;
- canonical tensor product, contraction, raising/lowering, restriction to
  the vertical fibre, polynomial composition, commutator, and real scalar
  normalization.

Initial \(G_{\rm DW}\)-self-adjoint words are:

\[
I,\quad T_{\rm tr},\quad
H_{\rm Ric}=G_V^{-1}\operatorname{Ric}_{VV},\quad
H_{\rm Ein}=H_{\rm Ric}-\tfrac12R I,\quad
H_{\rm tf}=H_{\rm Ric}-\tfrac1{14}R I,
\]

and the vertical curvature-square endomorphism obtained from
\[
B_{IJ}=R_{IABC}R_J{}^{ABC}.
\]

Initial \(G_{\rm DW}\)-skew words are commutators of independently constructed
self-adjoint words, especially
\[
[H_{\rm Ric},T_{\rm tr}],\qquad
[H_{\rm Ric},H_{R^2}],\qquad
[T_{\rm tr},H_{R^2}].
\]

Scalar shifts and normalizations may be evaluated only as ambiguity controls;
they may not be tuned to obtain rank four, a gap, or polar admissibility.

## Forbidden symbols

No candidate expression may contain or use:

```text
u, P_W, J, Omega_C, epsilon_flag, chosen 6+4 block,
rank four, selected eigenvectors, target-labelled gamma matrices,
Standard Model labels, hypercharge, or P3/count data.
```

Candidates are generated and named before their spectra are computed.

## Pre-registered expected verdict

```text
H GRAMMAR:
  EXPECT AT LEAST ONE TYPE-CORRECT SOURCE-OWNED DEWITT-SELF-ADJOINT
  ENDOMORPHISM, BUT DO NOT EXPECT A UNIQUE RANK-FOUR NEGATIVE FLAG.

Q GRAMMAR:
  EXPECT NATURAL COMMUTATORS TO BE DEWITT-SKEW, BUT EXPECT SINGULARITY
  OR FAILURE OF THE POSITIVE-REAL POLAR BRANCH.

W177 PHYSICAL HESSIAN:
  ALREADY KILLED AT THIS BACKGROUND BY THE PRIOR NONSTATIONARITY RESULT.

OWNERSHIP:
  EXPECT EITHER SOURCE-OWNED-BUT-NONSELECTING OR
  SPECTRAL-OWNERSHIP-BLOCKED-BY-AMBIGUITY, NOT A FORCED SM FLAG.
```

## Kill conditions

1. Reject any word containing a forbidden symbol before evaluating it.
2. Reject an \(H\) unless \(H^{\dagger_{G_V}}=H\).
3. Reject a \(Q\) unless \(Q^{\dagger_{G_V}}=-Q\).
4. Reject any adapter that does not terminate in
   \(\operatorname{End}(\operatorname{Sym}^2T^*X)\).
5. Reject post-selection: rank and signature are read only after the word and
   zero-threshold rule are frozen.
6. Reject projector ownership at gap closure, signature mismatch, or failure
   of smooth/covariant transport.
7. Reject polar ownership if \(Q\) is singular, non-diagonalizable on the
   required real branch, or if \(-Q^2\) lacks positive real spectrum.
8. Reject uniqueness if equally natural contractions or canonical scalar
   shifts yield incompatible spectral flags.
9. Do not read the W177 quadratic form as a physical Hessian; its stationarity
   precondition is already false.
10. Do not infer a Standard Model group, compactification, VEV, mass,
    cosmological value, anomaly, index, generation, or count from any finite
    spectrum.

## Five-leg boundary

| leg | permitted RB6 conclusion |
| --- | --- |
| SM/Yukawa | source ownership or failure of a vertical flag selector only; no SM identification or Yukawa placement |
| quantum/Krein/BV | exact DeWitt adjoints and polar eligibility; no CME, state space, or physical quotient |
| gravity/cosmology | trace reversal and W177 stationarity boundary retained; no vacuum or cosmological prediction |
| UV/causality | pointwise natural concomitants only; no common-cone or curved subprincipal upgrade |
| P3/index/count | P3 remains separate; spectral ranks and degeneracies are not counts |

## Planned outputs

- `tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py`
- `explorations/rb6-target-blind-spectral-grammar-2026-07-30.md`
- scoped integration updates to the source/datum packet, N3 boundary,
  `NEXT-STEPS.md`, `explorations/README.md`, and `tests/README.md`

No canon, claim-status, or public-posture change is authorized.

## Pre-execution provenance correction

The first hostile/source-ownership audit fired before spectra were read and
narrows two phrases above.

First, \(VY\simeq\pi^*\operatorname{Sym}^2T^*X\) and its vertical inclusion
are canonical, but a global direct-sum projection
\(TY\to VY\) requires the declared W177 gimmel/Levi--Civita horizontal
branch. The curvature candidates below therefore restrict both covariant
slots through the canonical vertical inclusion and raise with \(G_V\);
they do not claim an unqualified global horizontal projector.

Second, W177 curvature tensors are geometry-owned and evaluable on a
conditional ambient background. They are not the whole source-owned field
register. The written action also admits target-blind *formula-level*
candidates that must be carried even though no source background currently
evaluates them:

\[
B^\theta_{ij}=\kappa_{\mathfrak g}(\theta_i,\theta_j),
\qquad
H_\theta=G_V^{-1}B^\theta,
\]

and similarly for the retained vertical coefficient
\(v=\operatorname{res}^V(A-A_0)\). After the separately declared
normal--vertical graph identification, a section second fundamental form can
also yield an adjoint square \(H_{II}=II_sII_s^\dagger\). These formulas are
action-owned at field/formula grade; the vertical evaluation, background,
normal identification, and stationary orbit remain open.

RB6 will therefore report two different outcomes:

1. the complete evaluable W177 invariant grammar and its measured spectra;
2. the typed but unevaluated action-field grammar for
   \(\theta,v,II_s\).

This correction prevents a negative result for the symmetric W177 geometry
from being misreported as a negative result for the full source action.

The hostile pre-spectrum review also adds one required rival and one ownership
refinement:

- the \(1/14\) Ricci shift removes the ambient fourteen-dimensional trace;
  it is not vertically tracefree. The grammar must also evaluate
  \(H_{\rm Ric}-\operatorname{tr}_V(H_{\rm Ric})I/10\);
- under the explicitly conditional
  \(A_0=\operatorname{spinlift}(\nabla^{\rm gimmel})\) ambient-Yang--Mills
  identification, the all-leg and vertical-only Riemann-square contractions
  are the corresponding tangent-representation curvature Gram words, up to
  invariant-pairing normalization. They are therefore both geometry-owned
  and conditionally action-owned evaluable candidates.

## Execution result

### Evaluable invariant/curvature grammar

The native vertical DeWitt fibre has inertia \((6,4)\); the raw Frobenius
control has \((7,3)\). The frozen words and their measured sign sectors are:

| word | negative rank | DeWitt inertia on negative image | gap |
| --- | ---: | ---: | ---: |
| \(I\) | 0 | \((0,0)\) | 1 |
| \(T_{\rm tr}\) | 1 | \((0,1)\) | 1 |
| \(H_{\rm Ric}\) | 9 | \((6,3)\) | 0.25000007 |
| \(H_{\rm Ein}\) | 0 | \((0,0)\) | 3.7499999 |
| restricted ambient-tracefree Ricci | 9 | \((6,3)\) | 0.53571411 |
| vertical-tracefree Ricci | 9 | \((6,3)\) | 0.14999981 |
| all-leg curvature square | 1 | \((0,1)\) | 0.25 |
| vertical-only curvature square | 0 | \((0,0)\) | closed |

No word produces a gapped negative-definite rank-four sector.

The source-shaped fits are:

```text
H_Ric:      -0.50000002 I - 0.75000005 T, residual 2.551e-7
H_R2:        0.87500001 I + 1.12500002 T, residual 8.123e-8
H_R2,V:      0.75000001 I + 0.75000002 T, residual 1.088e-7
```

The raw commutator norms are `3.679e-7` through `8.338e-7`, below the
declared `2e-5` concomitant resolution. No nonzero \(Q\) is resolved and
every word is polar-ineligible. The fitted identity/trace representatives
commute exactly; conditional point-stabilizer representation theory explains
the \(1\oplus9\) collapse without promoting raw finite-difference values to
exact zeros.

Under the conditional W177 ambient-Yang--Mills identification, the all-leg
and vertical-only curvature squares are the corresponding evaluable
action-owned curvature Gram words, up to invariant-pairing normalization.
They fail the same selection gate.

### Formula-level action-field grammar

The executable validates, as type controls only:

```text
H_theta = G_V^-1 kappa(theta_i,theta_j)
H_v     = G_V^-1 kappa(v_i,v_j)
H_F     = G_V^-1 G_V^kl kappa(F_ik,F_jl)
H_II    = II_s II_s^dagger
Q_ab    = [H_a,H_b]
```

The \(H\) words are DeWitt-self-adjoint and the commutators are
DeWitt-skew. Their source field values, common reduction, stationary orbit,
normal--vertical identification, spectra, and polar branches are absent, so
no spectrum is read from the planted type witnesses.

### Stationarity

The pre-existing W177 stationarity control was re-run:

```text
||D_A0^* F_A0||:               3.19904137
contracted-Bianchi floor:      0.00372577
signal/floor:                  858.6
verdict:                       W177-AMBIENT-YM-NONSTATIONARY
```

This kills a physical ambient-Yang--Mills Hessian or mass reading only at
that conditionally identified background. It does not kill the full coupled
source action, the independent \(X^4\) IG connection, or another stationary
orbit.

## Ownership disposition

```text
W177 invariant H grammar:         TYPED / EVALUATED / NONSELECTING
W177 nonzero Q:                   NOT RESOLVED ABOVE FD FLOOR
W177 curvature Gram action words: CONDITIONALLY ACTION-OWNED / NONSELECTING
theta/v/F/II H formulas:          ACTION-OWNED / TYPED / UNEVALUATED
action commutator Q formulas:     ACTION-OWNED / TYPED / POLAR OPEN
physical Hessian at W177:         KILLED
source-derived flag:              OPEN AT COUPLED STATIONARY-ORBIT GATE
P1/P2/P3 ledger:                  UNCHANGED
```

## Validation receipt

Passed:

```text
python3 -B tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py
python3 -B tests/channel-swings/rb5_epsilon_flag_ownership_spectral_hessian_probe.py
python3 -B tests/channel-swings/rb4_observer_cartan_moving_family_probe.py
python3 -B tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
python3 -B tests/channel-swings/unified_source_variation_probe.py
python3 -B tests/channel-swings/unified_source_datum_packet_v0_probe.py
python3 -B tests/channel-swings/vertical_source_action_reduction_probe.py
python3 -B tests/channel-swings/w177_ym_residual_and_mode_closure_probe.py
python3 -B tests/W246_cfs_self_adjointization_selector_ambiguity.py
uv run --with-requirements requirements.txt python -B tests/big-swing/vg_v3_j_commutant_conformal_native.py
uv run --with-requirements requirements.txt python -B tests/W240_z2even_compact_image_nogo.py
uv run --with-requirements requirements.txt python -B tests/W243_charged_corridor_closure.py
python3 -B process_gates/tests_root_readme_inventory_audit.py
PYTHONPYCACHEPREFIX=/tmp/gu-rb6-pycache python3 -m py_compile tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py
git diff --check
```

RB6 itself passes all 29 controls. The inherited no-goes retain their prior
scope. No compactification, Standard Model identification, VEV, physical
mass, cosmological value, anomaly/CME closure, common domain, index,
generation, or count is claimed.
