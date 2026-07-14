---
artifact_type: exploration
label: W192
status: "exploration (W191 next-object big swing; explicit Cl(9,5) observer-section proxy plus carrier-type obstruction; no canon, claim-status, H-number, bar, verdict, or posture movement)"
created: 2026-07-14
title: "W192 -- Explicit carrier, torsion kernel, and spectral gate: the record state can select a shared carrier, but the current is not yet an Sp connection current"
verdict: "TYPED-OBSTRUCTION / STATE-SELECTED SAME-CARRIER / BARE KREIN RESIDUE DERIVED / RETARDED SPECTRAL SIGN OPEN. On the frozen (3,1) observer section H=(0,1,2,9), the repository's written Clifford-contraction shiab Phi_H: Lambda^2 H tensor S -> H tensor S is explicitly surjective, rank_C 512, with a 256-complex-dimensional preimage ambiguity. A frozen K-positive record spinor psi supplies the state-dependent vertex carrier v_mu=e_mu psi, and v lies in im(Phi_H), so the W191 same-carrier block exists on this branch. It is not bulk-law-forced: the central element -1 in Spin acts trivially on V and negatively on V tensor S, proving there is no nonzero state-independent Spin-equivariant lift V -> V tensor S. The stronger type gate is adverse: W180's real e_a vertex is K-self-adjoint and Clifford-odd, whereas a K-unitary connection generator must be K-anti-self-adjoint; the standard Spin(9,5) connection bivectors Sigma_ab satisfy the latter condition and are exactly orthogonal to span{e_a}. Thus W180's implemented J^a is a vector/soldering-current matrix element, not yet the Euler-Lagrange current of an Sp-valued connection unless an additional inhomogeneous/soldering-field identification is constructed. In the written spinor proxy, C_T(k)=I+sym_sharp(Phi_H d) has a source-visible rank-128 critical shell at |p|=2/sqrt(3), and bare K-residues (+,+,+,-) on the observer section. But the actual I1B ad(P)-valued shiab/star lift, record Hamiltonian, propagator, state, and C-metric are absent, so no on-shell retarded rho_J or physical pole verdict is derived."
grade: "EXACT / MACHINE-VERIFIED for 38/38 checks in the frozen complex 128-dimensional Cl(9,5) representation: Clifford/Krein relations; (3,1)+(6,4) section; odd self-adjoint gamma versus even anti-self-adjoint bivector type; central-parity lift obstruction; horizontal shiab rank, singular values, and nullity; state-dependent vertex inclusion; Krein-self-adjoint C_T spectra; rank-128 critical shell and source response; channel residue types; and zero-width static control. REPRESENTATION-THEORETIC for the central parity and Clifford-grade obstructions. STRUCTURAL / PROXY for identifying the written spinor shiab with the I1B law's ad(P)-valued operator. OPEN for the ad(P) shiab/star, gauge-reduced physical spectrum, current-current dynamics, retarded spectral density, interacting C-metric, and observed consequences."
depends_on:
  - explorations/W191-projected-i1b-source-block-2026-07-14.md
  - explorations/W190-constraint-reduction-selection-synthesis-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - explorations/W167-reduction-direct-sign-alpha-beta-2026-07-14.md
  - explorations/W161-lens-foundational-action-2026-07-14.md
  - canon/shiab-existence-cl95.md
  - explorations/shiab-operator/shiab-selector-search-2026-06-26.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/shiab_family_basis.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - RESEARCH-POSTURE.md
scripts:
  - tests/W192_explicit_carrier_kernel_spectral_gate.py
---

# W192 -- Explicit carrier, torsion kernel, and spectral gate

## 0. Result first

W191 reduced the second and third whole-picture stories to one exact question:

```text
Does the law's shadow channel and the record current use the same actual carrier?
```

W192 makes the strongest explicit construction the repository currently permits. It produces a clean split.

```text
                         BULK LAW
          written spinor shiab Phi: Lambda^2 V x S -> V x S
                              |
                    broad, surjective image
                              |
          no state-independent Spin lift from current V
                              |
                              v
                         RECORD STATE psi
                 supplies the missing spinor spurion
                              |
                  v_mu(psi) = e_mu psi in im Phi
                              |
                              v
                    STATE-SELECTED SHARED CARRIER
```

This is a better version of the joint story than either extreme:

- the law does not uniquely force the realized carrier;
- history does not freely invent a carrier outside the law;
- the law supplies an admissible carrier arena, while a record state supplies the missing intertwiner and
  selects one member.

But the attempted construction also finds a genuine type obstruction. The implemented W180 current uses real
odd gamma matrices `e_a`. Those are Krein-self-adjoint observables. A `K`-unitary `Sp` connection generator must
instead be Krein-anti-self-adjoint; the standard `Spin(9,5)` connection subalgebra is supplied by the even
bivectors `Sigma_ab`. Therefore W180's displayed vector current is not yet the current obtained by varying an
`Sp` connection. An extra soldering/translation-field construction could repair the identification, but it is
not present in the repository.

**Verdict:** the same-carrier architecture survives as **state-selected**, not law-forced. The actual
`I1B`/current identity remains typed-obstructed. The spinor proxy additionally exposes a source-visible critical
shell and channel-dependent bare Krein signs, but it does not provide a physical retarded spectral density.

## 1. Frozen construction and fork ledger

| Object | Frozen construction | Status |
|---|---|---|
| real form | repository's `(9,5)` branch, `Cl(9,5)=M(64,H)` represented on `C^128` | explicit; signature-choice caveat retained |
| observer section | horizontal indices `H=(0,1,2,9)` with signature `(3,1)` | source-first choice |
| normal complement | indices `(3,4,5,6,7,8,10,11,12,13)` with signature `(6,4)` | exact complement |
| shiab | written canon Clifford contraction `Phi`, with the unresolved outer `star` treated as the identity on the selected proxy component; not the full four-real-dimensional selector family | explicit proxy branch |
| law carrier | horizontal spinor-valued one-forms `H tensor S`, complex dimension 512 | explicit proxy |
| actual GU torsion | `Omega^1(Y,ad P)` in the displayed law | type target; lift unbuilt |
| record state | deterministic `K`-positive spinor `psi=(u+Ku)/||u+Ku||` | frozen before responses |
| current vertex | `v_mu(psi)=e_mu psi`; `J_mu=<psi,K e_mu psi>` is its matrix element | state-dependent lift |
| field metric | `H_field=diag(+,+,+,-) tensor K` | Krein, not positive-Hilbert removal |
| differential convention | compact-support Fourier mode, `d -> i k wedge` | explicit |
| spectral object | bare `K` residue and finite static response | not an interacting `C`-metric spectral density |

The gimmel/DeWitt metric is not identified with the base momentum metric. The dynamic law is `I1B`, not
geometric `|II|^2`. The native keep-and-grade branch is retained. The generation `Z/3` versus `Z` fork does not
enter this calculation.

## 2. The decisive type audit

### 2.1 What a connection generator must satisfy

Let

```text
K = e_0 e_1 ... e_8,
```

the spinor Krein form used in W180. A generator `X` of the `K`-unitary connection algebra must satisfy

```text
X^dag K + K X = 0.
```

The explicit representation gives, for every one of the fourteen gammas,

```text
e_a^dag K - K e_a = 0,
e_a^dag K + K e_a != 0.
```

Thus `e_a` is `K`-self-adjoint. That is why the W180 bilinear

```text
J^a = Re <psi, K e_a psi>
```

is a real observable. It is also why `e_a` is not an infinitesimal connection generator.

By contrast, the bivectors

```text
Sigma_ab = (1/4)[e_a,e_b]
```

satisfy

```text
Sigma_ab^dag K + K Sigma_ab = 0
```

for all 91 pairs. They commute with chirality and are Clifford-even. The gammas anticommute with chirality and
are Clifford-odd. Their Frobenius overlaps vanish exactly:

```text
<e_a,Sigma_bc>_F = 0.
```

Therefore `span{e_a}` and the displayed connection-bivector sector are not two bases for the same carrier.
They are different Clifford grades with different Krein adjointness.

### 2.2 Consequence for W180

W180 implements

```text
c(A)=sum_a A_a e_a,
S_D=Re<psi,K c(A) psi>,
delta S_D/delta A_a=J^a.
```

The derivative identity is algebraically correct for those fourteen coefficients. The new result is that this
`A` is not an `Sp` connection as labelled: `c(A)` lies in the odd self-adjoint vector sector, not the even
anti-self-adjoint connection algebra. The construction may be read as coupling to a soldering, translation, or
inhomogeneous-IG field, but that reinterpretation requires an explicit map into the actual `Omega^1(ad P)`
connection variables.

The typed connection current for a spin connection would instead carry both a base and an algebra index,
schematically

```text
J^{mu,ab} = delta S_D/delta A_{mu,ab}
          ~ Re<psi,K e^mu Sigma^{ab} psi>,
```

with conventions and the full kinetic action declared. That object is not what W180 computes.

This is recorded as an exploration-grade correction boundary. No standing W180 status or repository verdict is
changed here.

## 3. Why a record state is necessary

The W180 current as implemented is a vector `J in V`. The written canon shiab lands in a vector-spinor
`V tensor S`. Comparing them requires a lift

```text
L: V -> V tensor S.
```

There is an exact representation-theoretic obstruction to a nonzero Spin-equivariant, state-independent `L`.
The central element `-1 in Spin(9,5)` acts trivially on the vector representation `V` but as `-1` on `S`, hence
as `-1` on `V tensor S`. Equivariance would require

```text
L(v) = L((-1).v) = (-1).L(v) = -L(v),
```

so `L=0`.

This is the sharp form of the missing-carrier problem: **the bulk symmetry alone cannot turn a vector record
current into the spinor-valued shiab carrier.**

A record state `psi` changes the situation. Once `psi` is frozen, it supplies the missing spinor spurion:

```text
L_psi(e_mu) = e_mu psi,
J_mu(psi) = <psi,K L_psi(e_mu)>.
```

This lift is state-dependent and breaks the full symmetry to the stabilizer of `psi`. That is not automatically a
defect; it is a concrete mathematical version of selection by record/history. But it means the shared carrier is
selected by the state, not forced by the unbroken bulk law.

## 4. The explicit horizontal shiab

On the frozen observer section, the written Clifford-contraction shiab is

```text
Phi_H: Lambda^2 H tensor S -> H tensor S,

Phi_H(e^a wedge e^b tensor s)
  = e^a tensor e_b s - e^b tensor e_a s.
```

Its matrix has shape

```text
512 x 768.
```

The explicit singular-value decomposition returns

```text
rank_C(Phi_H) = 512,
nullity_C(Phi_H) = 256,
singular values = sqrt(2) with multiplicity 384,
                  sqrt(6) with multiplicity 128.
```

Therefore `Phi_H` is surjective. For the frozen record spinor, the vertex carrier

```text
v(psi) = (e_0 psi,e_1 psi,e_2 psi,e_9 psi)
```

has a preimage to relative residual `7.85e-17`.

This gives a positive and a negative conclusion:

- **positive:** after the record state supplies the spinor lift, the current vertex can occupy a law-admissible
  shiab carrier;
- **negative:** image membership is not selective, because every horizontal vector-spinor is in the image and
  each has a 256-dimensional affine family of curvature preimages.

So “the current lies in the shiab image” cannot by itself explain which shadow occurs. The reduction or source
action must choose a preimage or quotient.

## 5. The explicit spinor-proxy torsion kernel

For a horizontal vector-spinor `T_a`, the Fourier principal symbol of the written canon map is

```text
(Phi_H d T)_a
  = i [k_a sum_c e_c T_c - slash(k) T_a].
```

Let `D(k)=Phi_H sigma(d)(k)` and let `sharp` be the adjoint defined by

```text
H_field = diag(+,+,+,-) tensor K.
```

The quadratic part of the displayed action's **spinor-valued proxy** is

```text
C_T^spin(k) = I + (1/2)[D(k)+D(k)^sharp].
```

It is exactly Krein-self-adjoint. The spectra at unit coordinate momenta are

```text
spacelike k=(1,0,0,0):
  1-sqrt(3)/2  multiplicity 128,
  1            multiplicity 256,
  1+sqrt(3)/2  multiplicity 128;

timelike k=(0,0,0,1):
  1-i sqrt(3)/2  multiplicity 128,
  1              multiplicity 256,
  1+i sqrt(3)/2  multiplicity 128.
```

At

```text
|p| = 2/sqrt(3),
```

the spacelike kernel rank drops from 512 to 384: a 128-dimensional critical shell. Dropping the `dT` term
restores the identity kernel and removes the shell. Thus W167's purely algebraic elimination is not globally
valid even in this simplest written-shiab proxy.

The record vertex sees the shell. Its exact projected inverse response is

```text
R_space(p) = (1-p^2/2)/(1-3p^2/4),
R_time(omega) = 1/(1+3 omega^2/4).
```

The first expression has the same `2/sqrt(3)` pole. This is a real warning against treating `T` as everywhere
auxiliary. It is **not yet a physical tachyon or particle result**: the full `star_shiab`, the `ad(P)` lift,
normalization, gauge quotient, boundary conditions, and validity scale are missing, and any can move or remove
the proxy shell.

## 6. What can be said about the reservoir sign

For the frozen `K`-positive record state, define the vertex-excited states

```text
|a> = e_a |psi>.
```

The explicit representation gives

```text
[K,e_a]=0       for a=0,...,8,
{K,e_a}=0       for a=9,...,13.
```

Hence on the `(3,1)` observer section:

```text
channel          intermediate K type        signed bare residue
0,1,2 spatial    positive                    +1,+1,+1
9 timelike       negative                    -1
```

This is more precise than a single free “reservoir sign.” The bare sign is tied to the channel. A selected
current polarization can predominantly occupy positive or negative type, and a full interacting `C` metric can
regrade the physical states.

What is **not** derived is the on-shell retarded spectral density

```text
rho_J(omega,k) = spectral support x signed matrix elements.
```

The static Clifford representation determines the matrix elements and bare Krein types. It contains no record
Hamiltonian, vacuum/state distribution, excitation energies, propagator, continuum threshold, `i0` prescription,
or interacting `C` operator. Its real-frequency finite response has zero continuum width. Therefore W192 derives
the **bare residue type**, not the physical absorbing/reinforcing sign of `rho_J` on shell.

## 7. Effect on the W190-W191 joint story

### What strengthened

- The second and third stories now meet in an explicit mathematical mechanism: a record state supplies the
  spinor spurion that the bulk symmetry cannot supply and selects a carrier inside the law-admissible image.
- The need for selection is not only philosophical. It follows from the central action of Spin on `V` versus
  `V tensor S`.
- The written shiab derivative term can create a source-visible critical shell, so the reduction map genuinely
  carries dynamical information.
- The bare Krein sign is channel-typed rather than a freely floating scalar.

### What weakened

- The W180 vector current is not yet an `Sp` connection current. Its action is typed to an odd vector/soldering
  field unless an additional map is built.
- Same-carrier **existence** in the spinor proxy is cheap because `Phi_H` is surjective; it does not select one
  curvature preimage.
- The W191 determinant relation remains conditional on a one-carrier truncation after the state, quotient, and
  preimage are fixed. It is not a bulk-law identity across the full 512-dimensional block.
- The physical reservoir sign and total spectrum remain open because bare `K` type is not the interacting
  retarded spectral density.

## 8. The coherent plain-English story after the big swing

The strongest surviving universal story is now:

> A law supplies a structured space of possible response channels. It cannot by itself identify an observer's
> realized channel because the required map may be forbidden by the unbroken symmetry. A concrete record state
> breaks that symmetry and supplies the missing intertwiner, selecting a channel that the law already permits.
> The propagation kernel then decides whether that selected channel is stable and what correlations it forces.
> Explanation comes from the combination: lawful admissibility, state-dependent selection, and spectral
> survival. None of the three can substitute for the other two.

This is not “geometry explains everything,” nor “history chooses anything.” Geometry/law constrains the arena;
records provide a typed symmetry-breaking selection; dynamics tests whether the choice survives.

## 9. Falsifiers and next decisive object

The state-selected story would be weakened or killed if:

1. a native, state-independent `ad(P)` intertwiner is constructed, showing the central-parity obstruction was an
   artifact of comparing the wrong representations;
2. the correct `star_shiab`/`ad(P)` kernel is invertible and has no counterpart of the proxy critical shell;
3. the properly typed connection current has zero overlap with every physical shiab-shadow mode;
4. the retarded current spectral density has the reinforcing sign in every admissible physical channel;
5. choosing `psi` and its preimage consumes as many freedoms as the relations the construction produces.

The next exact object is no longer “compute some spectral density.” It is the typed replacement for W180's
fourteen-coefficient vertex:

```text
A_mu = sum_{a<b} A_mu^{ab} Sigma_ab,
J^{mu,ab} = delta S_record/delta A_mu^{ab},

and a declared map
Phi_ad: Lambda^2 H tensor spin(9,5) -> H tensor spin(9,5)
```

or the correct `sp(32,32;H)` analogue. Once `Phi_ad` and a record kinetic operator are present, the same test can
compute the actual carrier overlap, `C_T(k)`, and Lehmann/retarded `rho_J` without a type substitution.

## 10. Verification

`tests/W192_explicit_carrier_kernel_spectral_gate.py` passes **38/38** deterministic checks in 2.7 seconds:

- 5 representation and observer-section checks;
- 6 carrier-type and central-parity checks;
- 8 horizontal-shiab and state-lift checks;
- 10 torsion-kernel, spectrum, critical-shell, and response checks;
- 9 channel-residue and zero-width spectral controls.

**Final verdict: TYPED-OBSTRUCTION / STATE-SELECTED SAME-CARRIER / BARE KREIN RESIDUE DERIVED /
RETARDED SPECTRAL SIGN OPEN.**
