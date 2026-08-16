---
artifact_type: exploration
status: exploration
doc_type: conditional-build-exact-intertwiner-gate
created: 2026-08-16
work_item: CB-1-H210
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-1 H210: the PS-singlet 210 has an exact current-K77 gamma-traceless vector-spinor port, but owner-grade admission does not settle the fixed-Hq real connection port"
grade: "EXACT signed-permutation Cl(7,7) arithmetic plus exact rational coefficients. The internal (6,4) split, PS invariance, gamma trace, D parity, Clifford support, fixed trace-Hq phase fingerprint, injectivity, and conditional family kernel are checked without floats. H210 is assumed, not derived. Equation-9.16 placement, source action/background selection, reality choice, quotient, domain, scale, threshold, and observable remain missing."
disposition: REAL_K77_210_RS_INTERTWINER_EXACT_AND_INJECTIVE__COMPLEX_PS_IDENTIFICATION__D_ODD_OPPOSITE_CLEBSCH__OWNER_GRADE6_ADMITTED__FIXED_TRACE_HQ_SIMULTANEOUS_PS_PORT_TYPE_MISSING
canon_verdict_change: none
steering_effect: "Use the exact RS tensor, not a fixed one-form times a grade-six blade, in CB-2. Keep an explicit reality horn: the real current-Cl(7,7) port exists (with conventional PS names after complexification), while simultaneous full-PS and fixed trace-Hq unitary placement is TYPE_MISSING. Do not derive an action or import a selector."
canonical_effect: pending_integration
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-two-ps-channels-have-distinct-upstairs-owners-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-source-owner-intersection-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md
  - explorations/conditional-build/selected-k77-grade5-unitary-parent-euler-closure-2026-08-10.md
  - explorations/conditional-build/selected-k77-trace-hq-connection-compatibility-2026-08-13.md
scripts:
  - tests/channel-swings/joe_directed_cb1_h210_k77_rs_intertwiner_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> source-native composition using complex `Spin(10)`/Pati--Salam labels as a
> comparator. Ordinary family indices, net chirality, scalar-Higgs VEVs, and
> conventional SO(10) mass mechanisms do not adjudicate Weinstein's proposal
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> before reuse. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-1 H210 — exact K77 210-to-RS intertwiner

## Outcome first

Under the declared `H210` horn, the unique Pati--Salam-singlet line in

```text
210 = Lambda^4(V_10) ~= Lambda^6(V_10)
```

does have an exact vector-spinor port on the current `Cl(7,7)` carrier.  With
the source-aligned internal split

```text
N^(6,4) = A_6(positive) + B_4(negative),
phi_4 = vol(B_4),       phi_6 = vol(A_6),
```

and covariant coframe components `theta^a`, the canonical
Rarita--Schwinger projection is

```text
T_a(psi) = c(i_{(theta^a)^sharp} phi_4) psi
           - (4/10) Gamma_a c(phi_4) psi.
```

Here `sharp` is the internal `(6,4)` metric raise; this convention is
load-bearing on the four negative directions. The probe constructs each
raised contraction word explicitly. Its coefficient relative to
`Gamma_a phi_4` is `0` on `A_6` and `1` on `B_4`; subtracting the derived
projector coefficient `p/n=4/10` therefore gives

```text
a in A_6:  T_a = -(2/5) Gamma_a phi_4,
a in B_4:  T_a = +(3/5) Gamma_a phi_4.
```

The signature-aware gamma trace is therefore

```text
Gamma^a T_a = 6(-2/5) phi_4 + 4(+3/5) phi_4 = 0.
```

identity. Every component is a nonzero scalar times an invertible real
signed-permutation Clifford word, so the map exists over the real
`Cl(7,7)` carrier independently of `H_q` and has rank `64` from either real
ambient Weyl half to the opposite half. After the complex PS factorization,
this is rank `16` on each internal Weyl copy; complexification is needed for
the conventional `(4,2,1)` / `(4bar,1,2)` names, not for existence of the
K77 representation map.
For a declared nonzero family covector `r:F=C^3 -> C`, the conditional map
`r tensor T` has rank `16` and kernel

```text
ker(r tensor T) = ker(r) tensor 16,
dim_C kernel = 2*16 = 32.
```

This is the algebraic shape needed by the `2+1` hypothesis. It neither derives
`r` nor names one of the three family directions.

## Source contract carried into the calculation

The mandatory packet rows `SC-GEN-57/51/53/59/02/04/56/50/52` and
`SC-CHI-50/54/51/53/03` control the interpretation:

- the target is two representation-theoretically ordinary family-shaped
  outputs plus one imposter-shaped output that can look the same at low energy;
- the parent carrier stays non-chiral and four-cornered even when luminous and
  dark halves decouple effectively;
- no ordinary three-family index, scalar Higgs mechanism, net-chirality no-go,
  named “third” family, or mass-only explanation substitutes for that claim;
- `H210` is assumed compatible and nonzero, with no `54`; deriving an action,
  vacuum, background, external selector, or fitted family row is off limits.

## Eight-lens exact audit

### 1. Clifford-algebra lens

The probe uses the repository's exact signed-permutation `Cl(7,7)` matrices.
The ambient axes split as external `(1,3)` plus internal `(6,4)`. Both
`phi_4` and `phi_6` are nonzero orientation blades and differ by the internal
volume word. The Hodge-dual presentations therefore encode the same complex
`210` owner line.

### 2. D5 / Pati--Salam lens

`phi_4` commutes with all 15 `spin(6)` and all 6 `spin(4)` generators. The
same is true of `phi_6`. The RS tensor is then checked component by component,
including the covector action on its free internal one-form index. It is not a
multiplicity-only argument.

### 3. Rarita--Schwinger lens

The coefficient is `p/n=4/10`, not a fitted number. A planted `3/10` projector
has nonzero gamma trace. The exact cancellation also fixes the relative
`A_6:B_4` Clebsch ratio to `-2:3` up to one overall scale.

### 4. D-parity / family-block lens

An even normalizer element containing one `A_6` and one `B_4` reflection
preserves ambient chirality but reverses `vol(B_4)`. Thus the singlet line is
`D`-odd and exchanges the two `phi_4` eigenspaces. Those eigenspaces have equal
rank on either ambient Weyl half. In conventional complex PS language they are
the `(4,2,1)` and `(4bar,1,2)` family blocks, with opposite orientation
eigenvalues. Which block is called plus is an orientation convention; the
opposite relative sign is invariant.

### 5. Clifford-grade / novelty lens

This calculation forces a correction in terminology:

| object | `phi_4` presentation | Hodge-dual `phi_6` presentation |
|---|---:|---:|
| `210` owner tensor | grade 4 | grade 6 |
| gamma-traceless RS port | grades 3 and 5 | grades 5 and 7 |

A generic admitted grade-six endomorphism is therefore not the RS port. A
fixed one-form line times `phi_6`, like the useful generic port fixture in
earlier work, leaves an unpaired internal vector and is not PS invariant.
The invariant object is the full contraction tensor above.

HE-4B's “internal grade-six coefficient” is defensible only for the
Hodge-dual **owner tensor**. It becomes mistyped if reused as the complete
`Omega^0 -> Omega^1_RS` port.

### 6. Current-K77 real / trace-Hq lens

The fixed trace-owned form `H_q=iB Gamma(q)` exposes a new and exact fork. For
the same internal negative trace axis used by the current compatibility probe:

```text
phi_4 owner: Hq-skew with real phase
phi_6 owner: Hq-skew with real phase

A_6 grade-5 RS components: 6 real phases
B_4 grade-3 RS components: 1 real phase + 3 i phases
```

Thus the owner line itself is admitted, but no single overall phase places
the complete PS-equivariant RS tensor in the fixed-`H_q` unitary connection
real form. Componentwise phase completion is available in the full
`u(64,64)` basis, but the exact probe shows that it destroys gamma
tracelessness and full PS equivariance. This is expected structurally: choosing
`q` inside `B_4` already reduces `Spin(6,4)` to the stabilizer of `q`.

This does **not** kill the real current-`Cl(7,7)` H210 representation port (and
hence does not kill its complexification). The repository
itself classifies trace `H_q` as a construction while the source's defining
Hermitian form remains unspecified. The simultaneous

```text
full PS equivariance + gamma tracelessness + fixed trace-Hq unitarity
```

is therefore `TYPE_MISSING`, not a source-level no-go and not permission to
choose a new form in this lane.

### 7. Family-symmetry lens

The family result is basis-free. Any nonzero `r in F*` has a two-dimensional
kernel and stabilizer preserving the line `[r]`; no basis vector is selected
or called the third family. The conjugate half must carry the conjugate map.

### 8. Source-fidelity and falsifier lens

The complex representation gate survives: the exact port is nonzero,
injective, PS equivariant, D odd, and gamma traceless. The strongest remaining
falsifiers are now downstream and typed:

1. no source-faithful equation-9.16 barred/unbarred cell can carry this
   cross-half tensor;
2. a required real structure cannot reconcile the PS tensor with the operator
   pairing;
3. the map is removed by observation, quotient, or domain conditions; or
4. the declared family covector is zero.

If CB-2 cannot type a compatible cell, `H210` should fall below the alternative
path rather than trigger construction of a new action or external selector.

## Replacement text for HE-4B

If the older loose sentence is revised, the exact replacement is:

> The unique PS-singlet `210` owner can be represented by the admitted
> Hodge-dual grade-six blade `phi_6=vol(A_6)` (equivalently the grade-four
> blade `phi_4=vol(B_4)`). Its canonical gamma-traceless internal
> `Omega^0 -> Omega^1_RS` port is the full contraction tensor
> `T_a=c(i_{(theta^a)^sharp}phi_4)-(4/10)Gamma_a c(phi_4)`, with Clifford support in
> grades `3/5` (or `5/7` in the dual presentation), not one pure grade-six
> coefficient. Owner admission therefore does not by itself provide a
> source-selected, equation-9.16-placed, fixed-`H_q`-unitary connection port.

## Claim ceiling

This artifact proves an exact conditional intertwiner and exposes its real-form
fork. It does not derive the `H210` horn, a source action, nonzero stationary
background, equation-9.16 cell, family covector, effective-half selector,
physical quotient, closed domain, mass, named family, scale, threshold,
observable, or prediction. It does not change `SC-GEN-53`, canon, or public
posture.

## Reproduction

From the repository root:

```bash
python3 tests/channel-swings/joe_directed_cb1_h210_k77_rs_intertwiner_probe.py
python3 -m py_compile tests/channel-swings/joe_directed_cb1_h210_k77_rs_intertwiner_probe.py
```
