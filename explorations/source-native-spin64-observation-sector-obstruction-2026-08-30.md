---
artifact_type: exploration
status: exploration
doc_type: representation_obstruction_result
created: 2026-08-30
title: "Source-native Spin(6,4) real sectors do not descend through observation as a gamma-trace splitting"
target_claim: "INTERNAL — the naive bridge claim that observation pullback transports the ambient Omega0 / gamma-trace / gamma-kernel direct sum to three canonical observed sectors; verdict: OBSTRUCTED unless a new Clifford-trace intertwiner, quotient or dynamics is supplied"
source_claims: [SC-FER-04, SC-FER-05, SC-FER-07, SC-GEN-51, SC-GEN-52]
canon_verdict_change: none
probe: tests/channel-swings/source_native_spin64_observation_sector_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: representation-grade real-sector theorem plus obstruction to transporting the ambient gamma-trace splitting through observation
carrier: source-print Omega^0(Y,S-FULL-DIRAC) plus Omega^1(Y,S-FULL-DIRAC), and its observed pullback BRIDGE=section-pullback LAYER=source-print+observed CHIRALITY=S-FULL-DIRAC
pairing: Clifford contraction on vector-cospinor tensor products ON=the full Dirac spinor and its paired complex half-spin sectors
real_structure: real Cl(6,4) conjugation on the 32-real-dimensional Dirac module; it exchanges the complex 16+ and 16- half-spin sectors and likewise the 144+ and 144- gamma kernels
grading: normalized complex chirality chi=i*omega_6,4 together with form degree zero versus one; no observed physical chirality is assigned
action_owner: source-print field declaration and observation prescription; repository-construction owns only the representation theorem and non-intertwining witness
target: actual section pullback from ambient one-form spinors to observed one-form spinors, tested against the ambient and observed Clifford contractions MAP-TYPE=pullback
```

# Source-native Spin(6,4) sectors and the observation map

## Result in one sentence

The source-aligned `Spin(6,4)` real structure does preserve the **paired total**
gamma-trace exact sequence, exchanging its complex `16+ / 16-` and
`144+ / 144-` halves, but the actual observation pullback does **not** preserve
the ambient gamma kernel—even for a constant section—so the source's
`Omega^0 / gamma-trace / gamma-kernel` labels do not yet define three canonical
observed sectors.

This is a representation-grade obstruction to a naive bridge. It is **not** a
generation-count obstruction, a chirality verdict, a mass statement, an action
result, or a falsification of Weinstein's broader `2+1` proposal.

## 1. Preflight and retrieval

The source objects were frozen before calculation:

- draft equation (9.16) declares full-Dirac, unsubscripted
  `nu in Omega^0(Y,S)` and `zeta in Omega^1(Y,S)` with barred fields independent;
- the p.65 synopsis maps `nu` to the first true-family label, gamma multiplication
  on `zeta` to the second, and the RS remainder after pullback to an effective
  imposter label (`SC-FER-07`);
- the live exchange explicitly fumbles gamma-trace versus gamma-traceless
  language (`SC-GEN-52`), so this file may not choose one as the physical second
  family;
- observation is section pullback/contraction, not projection
  (`VZ4`, `MD-1`, `WG-B06`);
- HE-1's complex `16/144` calculation explicitly left the `Spin(6,4)` real form
  and physical-carrier bridge open.

Mechanism searches for gamma trace/kernel together with pullback/observation
found no prior artifact proving the commuting square tested below. Older
generation-count computations used section pullback and gamma-kernel ranks, but
did not test whether pullback preserves that kernel; their count conclusions are
not reused here.

## 2. Route selection

The real-Clifford route dominates a new complex branching census because the
complex dimensions `16` and `144` are already owned. The missing question is
how the real structure and observation map act on those spaces.

The bundle-geometric route dominates an index calculation because the source's
claimed observed sectors are obtained by pullback, and an index cannot repair a
noncommuting carrier map. The exact certificate is a control, not the proof:
the proof is the general Clifford-algebra witness in section 4.

Cheapest switch condition, fixed before execution: if section pullback
intertwines ambient and observed Clifford contractions, the gamma kernel
descends and the route switches to classifying the resulting observed
representations. If it does not, stop at the bridge obstruction and name the
additional datum required. The second branch fires.

## 3. The Spin(6,4) real-sector theorem

Let `V_R` be the real ten-dimensional quadratic module of signature `(6,4)`.
The exact real matrix construction in the probe gives

```text
Cl(6,4) on R^32,
omega_6,4^2 = -1,
chi = i omega_6,4,
chi^2 = 1.
```

All ten Clifford generators are real. Therefore ordinary real conjugation
commutes with Clifford multiplication but sends `chi` to `-chi`. It exchanges
the two complex half-spin eigenspaces:

```text
K : S+  <->  S-,       dim_C S+ = dim_C S- = 16.
```

Equivalently, the even real algebra carries the complex type convention used
by the source-facing representation calculations; neither complex `16` half is
a real sector by itself. The real object is their paired Dirac carrier.

Clifford contraction is surjective and has the explicit right inverse

```text
j(psi) = (1/10) sum_a epsilon_a e^a tensor gamma_a psi,
Gamma j = id.
```

Since every vector Clifford generator flips `chi`, this restricts to exact
sequences

```text
0 -> R+_144 -> V_C tensor S+_16 -> S-_16 -> 0,
0 -> R-_144 -> V_C tensor S-_16 -> S+_16 -> 0.
```

Real conjugation exchanges the two sequences and hence exchanges `R+_144` with
`R-_144`. It preserves their **paired total**, not either complex `144` alone.
This supplies the real-form result HE-1 lacked without turning a multiplicity
into a generation count.

At the ambient `Y^14` level the same dimension law gives `14*64-64=832` for
each complex half-spin gamma kernel and `1664` for the full-Dirac pair. These
are representation dimensions only. They are not observed particle counts.

## 4. Observation does not preserve the ambient gamma kernel

Along a section `s : X^4 -> Y^14`, write the cotangent split at one point as

```text
T*_s(x)Y = H* direct-sum N*,       dim H*=4, dim N*=10.
```

The actual observation map on one-form spinors is

```text
P_s = ds^* tensor 1 : T*Y tensor S -> T*X tensor s^*S.
```

For a constant section at the point, `P_s` is identity on `H*` and zero on
`N*`. Choose non-null covectors `h in H*`, `n in N*` and nonzero spinor `psi`.
Clifford multiplication by either non-null covector is invertible. Define

```text
t = h tensor psi - n tensor c(n)^(-1)c(h)psi.
```

Then the ambient gamma trace vanishes exactly:

```text
Gamma_Y(t)
  = c(h)psi - c(n)c(n)^(-1)c(h)psi
  = 0.
```

But observation kills the normal term:

```text
P_s(t) = h tensor psi,
Gamma_X(P_s(t)) = c(h)psi != 0.
```

Therefore

```text
P_s(ker Gamma_Y) is not contained in ker Gamma_X.
```

The failure already occurs at a constant section, so it cannot be repaired by
calling the general pullback a projection. For a nonconstant metric section,
`(s^*omega)_mu = omega_mu + omega_(ab) partial_mu g_ab` adds the known
contraction term and supplies no automatic Clifford-trace commuting law.

The probe verifies the witness in exact integer `Cl(1,1)` matrices and verifies
the full `Cl(6,4)` reality, chirality and gamma-splitting controls. The small
witness is a non-vacuity control; the displayed algebraic argument proves the
statement for the source dimensions.

## 5. Exact conclusion and surviving route

The naive commuting square

```text
T*Y tensor S  --Gamma_Y-->  S
     | P_s                    | R_s
     v                        v
T*X tensor s^*S --Gamma_X--> s^*S
```

is not supplied and is false for the literal constant-section pullback with
`R_s` equal to ordinary restriction. Consequently, the ambient direct sum

```text
Omega^0(Y,S) + im(j_Y) + ker(Gamma_Y)
```

does not descend as the corresponding observed direct sum merely by applying
`s^*`. In particular, the ambient RS remainder can leak into the observed
gamma-trace sector.

What survives is precise:

1. the paired `Spin(6,4)` real `16+/16-` and `144+/144-` sector theorem;
2. the source's kinematic ambient decomposition;
3. the possibility of an effective `2+1` mechanism after extra structure.

What is newly required is one of:

- a source-owned lift/retraction `(L_s,R_s)` making Clifford contraction a
  commuting square;
- a corrected observed kernel such as `ker(Gamma_X P_s)` together with a proof
  of its representation and quotient meaning;
- or action/BV/boundary/domain dynamics whose physical cohomology supplies the
  missing sector map.

Without one of these, no representation-grade observed `2+1` theorem exists.
With one, this obstruction becomes the exact acceptance test for the bridge.

## 6. Hostile review

**Strongest overclaim.** The witness obstructs only transport of the ambient
gamma splitting by literal observation pullback. Weinstein's proposal already
mentions effective behavior and leaves reduction/dynamics unresolved, so this
is not a source-claim kill.

**Strongest contrary construction.** A purpose-built retraction can project
away precisely the leakage witness, or physical cohomology can define sectors
after quotient rather than before it. Neither construction currently exists in
the admitted source-native packet, but either would answer this result.

**Weakest seam.** The `Spin(6,4)` real theorem concerns the internal ten-
dimensional factor, while the pullback obstruction is an abstract theorem on
the ambient `4+10` cotangent split. Their composition into one physical carrier
still needs the same source-owned observation/spinor intertwiner this result
identifies as missing.

**Controls.** Exact integer Clifford relations, signature, volume square,
chirality exchange, gamma right inverse, `144/832/1664` dimension laws, a
purely horizontal positive control and the kernel-preservation hostile control
all pass. No floats, fitted parameters, data or conventional family index enter.
