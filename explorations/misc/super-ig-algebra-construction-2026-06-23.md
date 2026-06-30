---
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
title: "Super-IG Algebra Construction over the Space of Connections"
---

# Super-IG Algebra Construction over the Space of Connections

**Status.** Exploration-grade. This note defines the minimal algebraic object that
would deserve the name "super-IG" and tests whether the current GU data specify a
canonical one. No coordination or canon files are updated here.

**Verdict.** A formal family of Lie superalgebras extending
`IG = G rtimes Omega^1(ad P)` is easy to define once one supplies an odd module `Q`
and a `G`-equivariant symmetric bracket

```
beta: Sym^2 Q -> Omega^1(Y, ad P).
```

However, the existing IG/tau+ data do **not** canonically determine such a `beta`.
The natural "spinor square gives a gauge-potential translation" attempt either
requires extra Clifford/soldering structure not present in the IG algebra alone, or
it reduces equivariance from full `Sp(64)` to the Clifford-preserving subgroup. Thus
super-IG is **defined conditionally**, not constructed as a canonical GU symmetry.

After the VZ F6 non-decoupling result, this is not currently a blocking problem:
the RS sector does not become a standalone 4D Rarita-Schwinger EFT at the
principal-symbol/KK-truncation level, so a guardian symmetry is unnecessary there.
Super-IG would only become urgent if a later loop computation drove the RS/spin-1/2
mixing blocks `B/C` to zero in the IR.

---

## 1. Input Context

From the required source notes:

1. `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md` identifies the
   relevant claim: do not feed SUSY Minkowski space; feed it the affine space of
   connections. The Poincare translation sector is replaced by gauge-potential
   translations.

2. `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md` fixes the
   non-super algebraic substrate:

   ```
   G = Sp(64)
   Conn(P) is affine over V = Omega^1(Y, ad P)
   IG = G_P rtimes V
   ```

   with the tau+ construction working for `G = Sp(64)` and not requiring the old
   `2^14 = dim u(128)` matching.

3. `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` fixes the corrected
   gauge group and anomaly setting: `Cl(9,5) ~= M(64,H)`, `S = H^64`, and the natural
   gauge group is quaternionic unitary `Sp(64)`.

4. `explorations/vz-evasion/vz-f6-eft-decoupling-2026-06-23.md` conditionally resolves the
   EFT decoupling concern: the `B/C` blocks are kinematic, not KK-suppressed, and the
   4D EFT RS sector does not become standalone at the principal-symbol level.

5. `canon/no-go-class-relative-map.md` section 2.5 now treats guardian symmetry as
   contingent: useful only if the Dirac-DeRham non-decoupling mechanism fails.

---

## 2. The Base IG Lie Algebra

Let `P -> Y` be the `Sp(64)` principal bundle over `Y = Y^14`. Write:

```
gP = Omega^0(Y, ad P)
V  = Omega^1(Y, ad P)
A  = Conn(P)
```

`A` is an affine space modeled on `V`. The infinitesimal inhomogeneous gauge algebra is:

```
ig = gP rtimes V
```

with bracket

```
[(eps, a), (eta, b)]
  = ([eps, eta], ad_eps b - ad_eta a),
```

where `eps, eta in gP` and `a, b in V`. The translation part `V` is abelian. This is
the connection-space analogue of the Poincare algebra `so(1,3) rtimes R^{1,3}`:
`gP` plays the Lorentz-like role and `V` plays the translation/momentum role.

---

## 3. Minimal Definition of Super-IG

The minimal algebraic datum for a super-extension is:

```
(Q, rho, beta)
```

where:

- `Q` is a Z/2-odd vector space of local odd parameters or charges.
- `rho: gP -> End(Q)` is the infinitesimal gauge action.
- `V` acts trivially on `Q` in the minimal model.
- `beta: Sym^2 Q -> V` is a symmetric `gP`-equivariant bilinear map.

Then define the Lie superalgebra:

```
sig(Q, beta)_0 = ig
sig(Q, beta)_1 = Pi Q
```

with brackets:

```
[(eps, a), (eta, b)]
  = ([eps, eta], ad_eps b - ad_eta a)

[(eps, a), q]
  = rho(eps) q

{q, r}
  = (0, beta(q, r)) in gP rtimes V.
```

This is a valid Lie superalgebra if and only if `beta` is `gP`-equivariant:

```
ad_eps beta(q, r) = beta(rho(eps)q, r) + beta(q, rho(eps)r).
```

The super-Jacobi identities then hold:

- even-even-even is the ordinary semidirect-product Jacobi identity;
- even-even-odd is the representation condition for `rho`;
- even-odd-odd is exactly the equivariance condition above;
- odd-odd-odd is automatic because `beta(q,r)` lands in the abelian translation
  part `V`, and `V` acts trivially on `Q`.

**Conclusion.** A super-IG algebra exists formally for any choice of `(Q,beta)` meeting
this condition. The hard question is not existence; it is whether GU supplies a
canonical, nontrivial `(Q,beta)`.

---

## 4. Candidate Brackets and Failure Modes

### 4.1 Trivial Odd Extension

Take any `gP`-module `Q` and set:

```
beta = 0.
```

This always gives a Lie superalgebra:

```
sig_triv = (gP rtimes V) ltimes Pi Q.
```

This is mathematically valid but physically empty. The odd generators do not square
to gauge-potential translations, so this does not implement the transcript's
"space of gauge potentials replaces four-momentum" claim.

**Verdict:** defined, but not a SUSY-like structure.

### 4.2 Fundamental-Spinor Square Attempt

The tempting GU-motivated choice is:

```
Q = Omega^0(Y, S),       S = H^64
```

and a bracket schematically of the form:

```
beta(q, r)(X) = mu(q, c(X)r) + mu(r, c(X)q),
```

where:

- `X in TY`;
- `c(X)` is Clifford multiplication;
- `mu(-,-)` is the quaternionic moment-map type bilinear with values in `sp(64)`.

This has the right analogy with super-Poincare:

```
{Q, Q} ~ Gamma^mu P_mu
```

becomes

```
{Q, Q}(X) ~ moment_map(Q, c(X)Q) in ad P.
```

The problem is equivariance under the full gauge group. `c(X)` is Clifford-geometric
data. It is preserved by the Clifford/spin subgroup, but not by an arbitrary
`Sp(64)` gauge transformation. For `beta` to be `Sp(64)`-equivariant, one would need:

```
beta(gq, gr)(X) = Ad_g beta(q, r)(X)
```

for all `g in Sp(64)`. The inserted Clifford operator `c(X)` prevents this unless
`g` preserves the Clifford-vector subspace or the construction is supplemented by a
connection-dependent rule that transforms `c(X)` as part of the gauge data.

**Verdict:** good analogy, but not a canonical full-`Sp(64)` bracket from the present
data. It becomes viable only after adding extra structure, such as a reduction to the
Clifford-preserving subgroup or a soldering rule that makes the Clifford vector
insertion transform covariantly under the chosen gauge group.

### 4.3 Adjoint-Gaugino Attempt

A more standard gauge-theory-like choice is:

```
Q = Omega^0(Y, S tensor ad P).
```

This resembles a gaugino module: odd parameters carry spinor and adjoint labels. One
can try to combine:

- a spinor bilinear producing a 1-form;
- an invariant Lie-algebra operation producing an adjoint value.

This can be made formally `G`-equivariant after choosing the needed spinor bilinear
and exchange symmetry. But that choice is not specified by the IG/tau+ construction
itself, and the resulting object is closer to a super-Yang-Mills-style extension than
to the specific Dirac-DeRham RS sector in GU.

It also introduces new adjoint fermionic data. The required VZ guardian, if ever
needed, must act on the RS/spin-1/2 block decomposition of `D_GU`, not merely on the
connection variable.

**Verdict:** possible as an added model, not forced by the existing GU construction.

---

## 5. Comparison with Super-Poincare and Local SUSY

Only the following comparison is needed.

Super-Poincare has:

```
even = so(1,3) rtimes R^{1,3}
{Q, Q} = Gamma^mu P_mu
```

The translation generator `P_mu` acts on spacetime. In local SUSY/supergravity, the
odd symmetry is gauged; the gravitino is the gauge field for local SUSY, and the
Rarita-Schwinger subsidiary constraints are protected by first-class gauge symmetry.

Super-IG would instead have:

```
even = Omega^0(ad P) rtimes Omega^1(ad P)
{Q, Q} = beta(Q, Q) in Omega^1(ad P)
```

The odd square shifts the connection in the affine space `Conn(P)`. It is therefore
not spacetime SUSY and does not imply super-Poincare multiplets or collider-scale
spacetime superpartners. That part of the transcript claim is structurally coherent.

But this also means the minimal super-IG algebra is **not automatically a VZ guardian**.
VZ protection requires more than an odd square into connection translations. It requires
a local symmetry whose Ward identity preserves the RS constraint and the correct
spin-3/2 degree-of-freedom count.

---

## 6. Guardian-Symmetry Assessment

For VZ purposes, a guardian symmetry must supply at least:

1. a local odd parameter acting on the RS field;
2. a transformation law for the RS/spin-1/2 Dirac-DeRham block system;
3. closure on the GU equations of motion or on the relevant constraints;
4. preservation of the gamma-trace/domain condition defining the RS sector;
5. compatibility with `Sp(64)` gauge covariance and anomaly constraints.

The minimal `sig(Q,beta)` construction above supplies only item 1 in a weak algebraic
sense, and only after `Q` is chosen. It does not by itself give items 2-4.

Therefore:

```
super-IG_as_defined_here != local SUSY guardian
```

It may become a guardian only if a future construction extends it from an algebra
on `Conn(P)` to a local symmetry of the full `D_GU` Dirac-DeRham system.

---

## 7. Effect of VZ F6 Non-Decoupling

The current VZ chain makes the guardian question non-blocking.

The F6 note establishes, at reconstruction grade, that:

- the KK zero-mode projector commutes with horizontal Clifford multiplication;
- the `B/C` blocks remain `O(1)` and kinematic in the zero-mode sector;
- loop corrections cannot alter the principal Clifford identity;
- the RS sector does not become a standalone 4D Rarita-Schwinger EFT at the
  principal-symbol level.

That means the VZ hypothesis "standalone spin-3/2 field with external gauge coupling"
is not met. The protective mechanism is not super-IG; it is Dirac-DeRham
non-decoupling:

```
RS sector = constrained block inside a full Clifford module,
not an independent Rarita-Schwinger field.
```

**Consequence.** Super-IG is unnecessary as a guardian unless the named F6-loop
failure mode occurs: large IR loop effects drive `B/C -> 0` and produce a standalone
RS field. That is not established by current notes.

---

## 8. Falsification and Upgrade Conditions

### Falsifies canonical super-IG

Canonical super-IG, in the strong GU sense, is falsified if no nonzero
`Sp(64)`-equivariant symmetric bilinear

```
Sym^2 Q -> Omega^1(Y, ad P)
```

exists for the chosen physically relevant odd module `Q`, without reducing the gauge
group or adding non-IG structure.

The fundamental-spinor square attempt already shows the main obstruction: Clifford
vector insertion is not full-`Sp(64)` invariant by itself.

### Upgrades super-IG to a real GU construction

A future note could upgrade this from conditional to constructed by giving:

1. the physically intended odd module `Q`;
2. an explicit nonzero `Sp(64)`-equivariant `beta`;
3. a proof of all super-Jacobi identities;
4. an action of the odd symmetry on the full `D_GU` field content;
5. a Ward identity preserving `ker Gamma^{4D}` or the 14D gamma-trace domain;
6. compatibility with the existing anomaly and VZ computations.

Without items 4-5, the result is only a connection-space supertranslation algebra,
not a guardian symmetry.

---

## 9. Final Status

| Question | Answer | Grade |
|---|---|---|
| Can a super-extension of `IG` be defined abstractly? | Yes, given `(Q,beta)` | verified algebra |
| Does the existing IG/tau+ data determine canonical `(Q,beta)`? | No | reconstruction |
| Does the fundamental spinor-square bracket work for full `Sp(64)` automatically? | No; Clifford insertion obstructs full equivariance unless extra structure is added | reconstruction |
| Is super-IG equivalent to spacetime SUSY? | No; it squares to connection translations, not spacetime translations | reconstruction |
| Does it currently serve as VZ guardian? | No | reconstruction |
| Is a guardian currently necessary after F6? | No, unless future loop work makes the RS sector standalone | reconstruction |

**Bounded verdict.** Super-IG is a legitimate conditional algebraic target, but the
current GU construction does not yet specify a canonical nontrivial super-IG bracket.
For the Velo-Zwanziger program, this is acceptable: Dirac-DeRham non-decoupling is the
active evasion mechanism, and guardian symmetry is presently unnecessary.

---

## References

- `NEXT-STEPS.md`, "UCSD Transcript Analysis - New Tasks" section.
- `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md`, New Object F.
- `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`.
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`.
- `explorations/vz-evasion/vz-f6-eft-decoupling-2026-06-23.md`.
- `canon/no-go-class-relative-map.md`, section 2.5.
