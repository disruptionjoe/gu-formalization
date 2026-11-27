---
title: Complete spin-five constraint block at the held stationary backgrounds
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Decide the complete even highest-spin5 native M restriction at both held root boxes and consume any consequences for actual constraint consistency
actual_delta: The complete native spin5 time-kernel is invertible throughout both held root boxes:240 even highest directions plus240 odd directions exhausted by owned receivers. All remaining mixed and spin5 normal-normal sources are absorbed. Equivariant jet theory removes independent lower-order first-consistency tests, leaving two spin3 and four spin4 pure-normal channel types. No propagation or GU verdict.
class_covered: The complete even and odd highest-spin5 time-kernel in the autonomous imaginary-U W2/K95 quadratic block at the two fixed real zero-matter kappa1 root boxes, with first-consistency consequences on Q=2V7.
premises:
- 'source-action-mixed-consistency-2026-11-26.md: actual corrected mixed sources, coefficient parity and exhaustive full-M reduction'
- 'source-action-kappa1-constraints-2026-11-25.md: native time-kernel projector and complete spin6/spin7 inverses'
- 'source-action-constraint-source-repair-2026-11-26.md: prior odd spin5 receivers and horizontal first-consistency result'
source_bridge:
  status: conditional
  reason: W2 and freely specified Q jets are candidate constructions, not source-required physical states; propagation, physical quotient and source necessity remain unproved.
kill_condition: A singular restricted matrix, failed numerical search or failed sufficient error bound is not inconsistency. Any negative consistency claim must annihilate full M and every permitted normal and zero-order kernel-multiplier repair; a physical or GU claim needs its separate source bridge.
---

# Complete spin-five constraint block

program_target: LB-CLASS
tier: T2
expected_delta: Decide the complete even highest-spin5 native M restriction at both held root boxes and consume any consequences for actual constraint consistency
actual_delta: The complete native spin5 time-kernel is invertible throughout both held root boxes:240 even highest directions plus240 odd directions exhausted by owned receivers. All remaining mixed and spin5 normal-normal sources are absorbed. Equivariant jet theory removes independent lower-order first-consistency tests, leaving two spin3 and four spin4 pure-normal channel types. No propagation or GU verdict.

Basis: freshly fetched `8dc0d2475a7bdcd03dc9e3e2edd6cfc8bfcf9e35`.

## Result in plain terms

**The entire spin-five constraint block passes at both held backgrounds.** Exact root-box certificates cover all240 even highest-weight directions. An exact companion count proves the old two120-dimensional receivers exhaust the240 odd directions; their owned inverse certificates finish the block.

This removes all remaining mixed consistency tests and every normal-normal spin5 test. Together with the existing complete spin6/7 inverses, it also proves that lower-order terms cannot supply a separate first-consistency obstruction. The next potentially decisive calculation has only **six pure-normal channel types: two spin3 and four spin4**. A candidate inconsistency would still need to survive all allowed kernel-multiplier repairs. This result supplies neither propagation nor a physical state-space or GU verdict.

```gu-typed-objects
result: complete native spin5 auxiliary range at held roots
carrier: imaginary-U connection one-forms of W2 K95; N=ker K_dt; Q=two real geometric SO3 spin7 modules LAYER=ambient BRIDGE=physical_admission_unproved CHIRALITY=N/A
pairing: actual signed native trace/form pairing ON=declared_carrier
real_structure: full U64_64 native real carrier with highest-weight complexification for exact arithmetic
grading: spatial SO3 spin and coefficient involution chi; neither is physical chirality or family number
action_owner: repository W2 candidate, actual coupled quadratic Hessian at two held backgrounds
target: entire native M restriction and actual first-consistency source range MAP-TYPE=homomorphism
```

SC-ACT-01 ASSERTS action grammar, not uniquely selected W2. SC-ACT-06 ASSERTS a Euclidean Upsilon deformation-complex claim, not the present Lorentzian propagation. SC-GEO-51 names full U(64,64), and SC-GEO-55 names gauge-rotated Levi-Civita displacement. SC-META-53 is UNCERTAIN about treating indefinite spectra. Native minus adjoint, K95/K77, independent fields, observation contraction, source2+1 and total/observed/physical gradings remain distinct. LT-GR1, LT-GR6b and LT-SM8 keep their verdicts.

## 1. A complete finite carrier

Write A=K_dt, N=ker A, P for the owned native orthogonal time-kernel projector, and

    C(T)=I+2N_cubic(T,.),    M(T)=P C(T) P.

The cubic polarization N_cubic and the kernel N are different objects. Every one of the 59 allowed background basis fields is spatially invariant. The diagonal coefficient involution

    chi(e,c)=(-1)^popcount((e XOR c) & 13319)

also preserves all of them and the time covector. It commutes with spatial rotations and M. It is an orientation-preserving metric involution on the native coefficients, not a physical chirality or a selected positive norm.

The complete even weight5 space has 664 dimensions. Its raising map has rank152, giving 512 highest-spin5 directions. Exact native K_dt on this complete highest space has rank272, leaving **240** highest-spin5 time-kernel directions. These are exact ranks, not dimensions inferred from a numerical solution's support.

The construction enumerates exterior wedges of all 14 native complex weight atoms, with the actual imaginary-U Clifford degree condition. Exterior multiplication is essential: substituting Clifford products when positive and negative weight atoms coexist would introduce contractions and mix degrees. An exact inverse coordinate transformation verifies independence and completeness of all 664 starting vectors. The raising and time-kernel calculations retain every native output row. Native weight, raising, Casimir and time-kernel equations verify the final basis.

Let Z denote that basis as ambient columns. Full M invariance follows from its definition and the proved SO3/chi symmetries. It does not require repeating a 59-by-240 guessed-space closure census. For an even highest5 source, projecting any full-N preimage by the commuting parity, spin5 Casimir and weight5 projectors gives a preimage in this complete space. The restricted range test is therefore exhaustive for those sources.

## 2. Use the native paired matrix

Let J be the actual signed diagonal native pairing. Define

    Q_pair = Z^dagger J,
    G = Z^dagger J Z,
    H(T) = Q_pair C(T) Z.

The dagger is conjugate transpose. A bilinear self-pairing of highest-weight vectors would vanish and is not this construction. The signed J belongs in H; positive absolute values enter only error estimates.

Because P is J-orthogonal and PZ=Z, Q_pair P=Q_pair. Complete-space invariance supplies a square coordinate matrix F with MZ=ZF, so

    H = Q_pair P C Z = G F.

Thus an invertible H proves both G and the native restriction F invertible. No new nondegenerate-Gram assumption is inserted. Conversely, singular H would require separating G from F before claiming M singularity.

This removes repeated applications of P from matrix assembly. Two exact rational center matrices, together with the next uniform perturbation bound, are enough; 59 separate full coefficient matrices are unnecessary if that bound passes.

## 3. A rigorous bound for every background uncertainty

Use positive computational weights

    g=(1,1,1,1,4,3,5,7,3,3,3,3,3,3),
    w_c=product(g_i for bits i in c),
    ||V||_w=sum_(e,c) w_c (|Re V_(e,c)|+|Im V_(e,c)|).

There is no extra form-mask weight. These weights do not replace the native physical pairing. Since g_i squared is at least |d_i| for the actual diagonal metric, weighted Clifford multiplication is submultiplicative. Commutators and anticommutators have bound2.

The actual native Phi, Phi-adjoint and wedge-adjoint formulas give

    ||Phi|| <= 86,
    ||Phi_adj|| <= 1604,
    ||wedge_comm(U,V)||_w <= 2 ||U||_w ||V||_w,
    ||wadj(U,V)||_w <= 2 ||U||_w ||V||_w.

For clarity, sum_i g_i=41 and sum_(i<j) g_i g_j=762. The first two bounds are respectively max_(i<j)[2g_i/|d_i|+2g_j/|d_j|+2(41)g_i g_j/|d_i d_j|] and max_i[2(41-g_i)+2(762)g_i/|d_i|]. The native cubic term is

    N_cubic(U,V) = (Phi(wedge_comm(U,V))
                   +wadj(U,Phi_adj V)+wadj(V,Phi_adj U))/6,

hence

    ||N_cubic(U,V)||_w <= 1098 ||U||_w ||V||_w.

An exact scan of every coefficient of every background field gives

    sum_alpha ||T_alpha||_w = 128637452/3.

For the owned root coordinate box of radius r, this bounds the full 59-coordinate uncertainty by ||delta T||_w <= r(128637452/3). No affine direction is omitted.

Let D_j=||Z_j||_w, W=diag(w_c), and R be a frozen Gaussian-rational approximate inverse of the exact H at the rational center. Use maximum-column-sum matrix norms with Gaussian coefficient absolute value |Re|+|Im|. Since ||W Z D^-1||_1=1,

    eta0 = ||D(I-R H_center)D^-1||_1,
    Cstar = ||D R Q_pair W^-1||_1,
    eta = eta0 + 2196 r (128637452/3) Cstar.

If eta<1, Neumann's lemma certifies H, and therefore the native M restriction, throughout the entire root box. A convenient safe bound avoids explicitly forming R Q_pair:

    t_j = sum_i D_i |R_ij|_1,
    Cstar <= max_k (|J_k|/w_k) sum_j t_j |Z_kj|_1.

Every factor is rational and independently checkable. A failed bound only calls for sharper arithmetic or analysis; it proves no singularity.

## 4. Actual roots and consistency consequences

Both exact rational certificates pass:

| Held root | Center defect, weighted column1 | Full root-box Neumann bound | Conclusion |
|---|---:|---:|---|
| 0 | 3.50e-14 | 0.0007412202258171841 | Complete even N5 invertible |
| 1 | 7.49e-14 | 0.001371598753812693 | Complete even N5 invertible |

The bounds are exact rationals in the certificate; displayed decimals are summaries. Each bound is strictly below1 and covers all59 uncertain background coordinates. Center matrices are Hermitian and use the actual signed native pairing. Rationalized numerical inverses are only preconditioners; exact defect and perturbation bounds supply the proof.

The corrected mixed sources A_mix=d9−2 Pi5 P N_cubic(U9 T,y0) and nonzero B_mix=d25, with derivative channels4(A_mix−B_mix) and2(2A_mix+B_mix), are now absorbed throughout both boxes. This follows from complete block invertibility and exact symmetry membership, without treating an approximate primary response as exact.

The companion calculation starts with all684 odd weight5 vectors. Raising rank148 leaves536 highest5 directions; native K_dt rank296 leaves exactly240 time-kernel directions. Every column of the two owned120-dimensional receivers passes native time-kernel, weight, raising and odd-parity checks. Their concatenated exact rank is240, so they exhaust the complete odd block. Their already-owned invariant root-box inverses combine with the new even inverse to prove **full N5 regularity**. No new odd inverse is needed. These are coefficient representation multiplicities, not physical particle counts.

### Structural consequence: no independent lower-order discriminator

The new full M5 inverse and the owned full M6/M7 inverses establish the needed premise. The native cokernel then contains only spins at most4. Spatial cotangent in the time-adapted frame is

    W*=2V0 + 2V1 + V2,

so the value/first-jet module J1(Q) contains only spins at least5. The actual first-consistency operator is equivariant, with its already-owned equivariant primary lift. Therefore

    Hom_SO3(J1(Q), coker M)=0.

Apply this to the equivariant second-jet exact sequence

    0 -> Sym2(W*) tensor Q -> J2(Q) -> J1(Q) -> 0.

Compact SO3 admits an equivariant splitting. Restriction to the principal-symbol subspace identifies the equivariant maps from J2(Q) to coker M uniquely with their principal symbol: any two such maps having the same principal symbol differ by a map from J1(Q), which is zero. This is not a claim that every non-equivariant coordinate coefficient vanishes. It absorbs the lower-order terms without dropping moving-frame or transverse derivatives. Different equivariant jet splittings give the same cokernel result.

The previously repaired horizontal and mixed principal maps are consumed. For pure normal Hessians,

    Sym2(2V0+V1+V2)=5V0+3V1+5V2+V3+V4.

Full N5/6/7 inverses absorb every target of spin at least5. Across the two Q copies, only **two spin3 and four spin4 channel types** remain. These counts do not assert six independent native vectors. No normal-first lower-coefficient calculation is needed for this first-consistency question at these held backgrounds.

With Z_j=ker M_j, full high-spin inversion also gives Z5=Z6=Z7=0. A negative spin4 test retains seven normal kernel-channel types (two scalar Z4, vector Z3/Z4, tensor Z2/Z3/Z4) plus its zero-order Z4 term. A negative spin3 test retains nine normal types (two scalar Z3, vector Z2/Z3/Z4, tensor Z1/Z2/Z3/Z4) plus zero-order Z3. Horizontal multiplier derivatives remain zero modulo im M by the owned boost identity. These are still required repairs, not new physical choices.

The conclusion concerns pointwise first consistency of candidate jets. It does not establish higher constraint closure, propagated solutions or physical admissibility.

## 5. Faster next calculation: eliminate the range inverse

The remaining six channels admit a checked algebraic shortcut. Let G=A_R^-1 R, R=1−P. For spatial covectors a,b, choose native metric generators U_a,U_b with [U_a,A]=K_a and [U_a,C]=2N_cubic(U_aT,.). All13 covectors orthogonal to the held time direction qualify, including the10 normals. Set j_a=P U_a P and take exact primary responses M y_a=P K_a V. The actual multiplier symbol is

    L_a=M j_a−j_a M+2P N_cubic(U_aT,.)P.

For the full cross principal coefficient,

    r_ab=P K_a G K_b V+P K_b G K_a V−L_a y_b−L_b y_a,
    q_ab=P(U_a K_b+U_b K_a)V
         −2P[N_cubic(U_aT,y_b)+N_cubic(U_bT,y_a)],
    r_ab=q_ab−M(j_a y_b+j_b y_a).

Indeed P K_a G=P U_a R and j_a M y_b=P U_a P K_b V. Their sum is P U_a K_b V. Thus q_ab computes the same cokernel class without applying G. The diagonal quadratic coefficient is one half of r_aa; off-diagonal full cross coefficients are not halved. Ambient U need not fix the background. For a true horizontal boost S with ST=0, this representative differs from the owned mixed representative by M y_(S eta), so the normalization agrees modulo M.

Approximate responses require explicit residuals e_a=M ytilde_a−P K_a V:

    rtilde_ab=qtilde_ab−M(j_a ytilde_b+j_b ytilde_a)+j_a e_b+j_b e_a.

This identity is a calculation scaffold, not a six-channel solvability result. Input spanning, both Q copies and every permitted multiplier repair still require the native test. No lower-order coordinate term is dropped by the identity.

## 6. Evidence, reproduction and scope

[Evidence](../../lab/process/source-action-even-spin5.json) · [data-only certificate bundle](../../lab/process/source-action-even-spin5-certificates.json) · [probe](../../tests/program-focus/source_action_even_spin5_probe.py) · [independent reviews](../../lab/process/hostile-reviews/2026-11-26-source-action-even-spin5-review.md).

### A reconstruction control caught and fixed

A first source-membership check failed despite valid basis equations. Sparse elimination had recorded pivots in column-discovery order; reducing in that order could reintroduce a previously eliminated coordinate. Reduction now uses ascending pivot order while retaining original basis-coordinate indices. An independent reconstruction reproduces the false residuals before the fix and zero residuals after it. No native field, complete basis, source or equation changed; no completeness condition was weakened. This is separate from the earlier corrected nonzero mixed constant B.

The full executed calculation includes exact exterior-coordinate roundtrips, raising/time ranks,960 native equations for the even basis, native reality closure, signed Gram checks, both rational center matrices, rational preconditioner defect bounds, and the complete odd-kernel/receiver rank comparison. The positive Clifford weights are computational estimates only.

The installed ten-record capsule passed an empty-cache bounded replay:

```sh
python3 tests/program-focus/source_action_even_spin5_probe.py --repo . --cache _local/even-spin5 --mode unpack
python3 tests/program-focus/source_action_even_spin5_probe.py --repo . --cache _local/even-spin5 --mode replay
python3 tests/program-focus/source_action_even_spin5_probe.py --repo . --cache _local/even-spin5 --mode status
```

This mode freshly reconstructs the complete even/odd carriers, ranks and source coordinates; recomputes original-engine controls and the first complete H column at each root; and repeats the full exact matrix-defect and root-box arithmetic with frozen rational preconditioners. The other478 H columns are authenticated stored records, **not** recomputed in this bounded replay. Their full native assembly executed once. The original Hodge-Euler engine agrees exactly with both first C-images and all240 pairings for each;161 generic fast-engine/projection controls also pass. Hashing alone is not called mathematical verification. All capsule inputs are data-only and native/procedure-bound.

Fresh replay SHA256: `6e35019d239f03cfbb5c32f5ecc651d73c13d3184cc2b857d16beba52031ce36`. Bundle SHA256: `aab4a323b2f00ff59ba17775f33e39c0b413d596a4ba366286c018a0477716fb`. Frozen probe: `05e450d25077c162f1345936ceaeb2315b691e9280e9ef1a11d045c13b2a6edd`.

- **ESTABLISHED:** complete even/odd dimensions240/240; full native M5 invertibility at both root boxes; removal of independent lower-order first-consistency discriminators; reduction to six pure-normal principal channel types; exact no-G computation identity.
- **RULED OUT:** a spin5 M-cokernel obstruction at these backgrounds, or a separate lower-order equivariant obstruction on Q at this first-consistency stage. No candidate completion, source theory or physical mode is excluded.
- **NOT MODELED / UNDETERMINED:** the six remaining augmented channels, higher constraint closure, propagated admissible solutions, physical quotient/energy and source necessity.

Choice budget remains10 families/4 obligation bundles/net6/zero source-selected predictions. No new action, state restriction, quotient, boundary datum or physical pairing is introduced. No source/physics/canon/class-C/paper/governance/schedule change. Joe's Nov26(g) counterfactual proposals remain unexecuted.

## Appendix: optional full matrix reproduction

Set GUEVEN_CACHE to the unpacked cache above, for example `GUEVEN_CACHE=_local/even-spin5`. Keep the unpacked originals intact and rebuild in a separate cache. Timestamps
change artifact bytes, so compare exact mathematical payloads before using the
original frozen records for certificate replay.

```sh
GUEVEN_REBUILD="$GUEVEN_CACHE/full-H-rebuild"
python3 tests/program-focus/source_action_even_spin5_probe.py --cache "$GUEVEN_REBUILD" --mode highest
python3 tests/program-focus/source_action_even_spin5_probe.py --cache "$GUEVEN_REBUILD" --mode kernel --method kernel --steps 0
python3 tests/program-focus/source_action_even_spin5_probe.py --cache "$GUEVEN_REBUILD" --mode validate
python3 tests/program-focus/source_action_even_spin5_probe.py --cache "$GUEVEN_REBUILD" --mode matrix --steps 0
python3 - "$GUEVEN_CACHE" "$GUEVEN_REBUILD" <<'PY'
import json,sys
from pathlib import Path
old,new=map(Path,sys.argv[1:])
def read(path,name):return json.loads((path/name).read_text())
a,b=read(old,'even-basis.json'),read(new,'even-basis.json')
for key in ('basis','basis_pivots','complete_N5_even_dimension','time_rank'):
    assert a[key]==b[key],key
a,b=read(old,'even-root-matrices.json'),read(new,'even-root-matrices.json')
assert a['complete'] and b['complete'] and a['dimension']==b['dimension']==240
for ar,br in zip(sorted(a['roots'],key=lambda r:r['root']),sorted(b['roots'],key=lambda r:r['root'])):
    for key in ('root','root_record_sha256','completed','columns','hermitian','complete'):
        assert ar[key]==br[key],(ar['root'],key)
    for ai,bi in zip(ar['image_controls'],br['image_controls']):
        assert {k:v for k,v in ai.items()if k!='seconds'}=={k:v for k,v in bi.items()if k!='seconds'}
print('All480 exact H columns and full-native-image hashes agree.')
PY
python3 tests/program-focus/source_action_even_spin5_probe.py --cache "$GUEVEN_CACHE" --mode certify
```

The final command deliberately uses the frozen original matrix record, whose
hash binds the frozen inverse candidates. Equality of every mathematical
column connects the fresh native reconstruction to that exact certificate.
Do not overwrite timestamp-bearing original matrix records and then bypass a
preconditioner binding mismatch.

`--steps N` on `kernel` or `matrix` processes at most N further columns per
selected stage/root. `--root-index 0` or1 limits matrix assembly to that root.
Checkpoints reject changed procedure/native-input bindings. `--output` applies
to bundle, replay and status only. `--generate-candidates` explicitly opts into
floating candidate discovery; exact certificate replay never requires it.
