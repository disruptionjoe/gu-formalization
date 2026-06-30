---
title: "N3 Cech Sheaf Fixture: Full Specification for Temporal-Issuance Implementation"
date: 2026-06-23
problem_label: "n3-cech-fixture-specification"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# N3 Cech Sheaf Fixture: Full Specification for Temporal-Issuance Implementation

## 1. Problem Statement

**What is being computed.** Closure condition C2 for N3 requires executing a
`cech_sheaf_fixture` in the `temporal-issuance` repo. The fixture has existed only as a
route label (`E015 next_fixture: cech_sheaf_fixture`, `NEXT-TRIGGER-PLAN: W000 ->
cech_sheaf_fixture`) with no concrete inputs, test conditions, expected outputs, or
structural requirements written down anywhere in either repo.

This file produces that specification. It answers:

- What inputs must the fixture receive?
- What test conditions must it check?
- What expected cocycle outputs would confirm, refute, or leave open the C2 question?
- What structural requirements constrain a valid implementation?

**Why C2 matters.** H3 is the identification hypothesis underlying T63's Holonomy Theorem
identity form: the TaF finality presheaf sections are literally the same objects as flat
Z/2Z-gauge connections on GU observer sections. Without H3, the T63 theorem degrades from
identity to structural analogy. C2 is the test whether TI C-typed admissibility *forces*
cocycle values from source primitives (a theorem) or merely *accepts* pre-stipulated values
(a definition). If admissibility forces nontrivial cocycles, H3 gets a genuine derivation
path. If it only accepts them, H3 is permanently a stipulation.

**Relation to prior work.**

| file | contribution |
|------|-------------|
| `n3-h3-cech-holonomy-2026-06-23.md` | H3 anatomy, three closure conditions, High-confidence T63 entries are H3-independent |
| `n3-h3-cech-fixture-execution-2026-06-23.md` | Confirmed fixture is absent; precise missing-artifact record |
| `taf-h3-contact-2026-06-23.md` | W-H3 (weakened H3) established; BC-1 through BC-3 structural parallels; six falsification conditions |

This file is the implementation target that those three files call for.

---

## 2. Established Context

### 2.1 The Fixture Question (from E015 and NEXT-TRIGGER-PLAN)

The fixture tests one question:

> Specify the section-compatibility predicate for C-typed extensions on a two-patch cover
> of S^1. Does the admissibility rule independently determine which Cech cocycles are
> allowed, rather than merely accepting a preselected sheaf or transition function?

E015 analyzed a three-patch source fixture and found three options: (1) C_min does not
include transition values (no holonomy determined); (2) C_min includes transition values
and allows nonidentity product (transport data stipulated); (3) C_min includes a consistency
rule forcing identity product (holonomy trivially zero). "No fourth option appeared in the
minimal fixture." The cech_sheaf_fixture looks for a fourth option: C-typed admissibility
predicates force particular cocycle values as a consequence of the typing rules alone.

### 2.2 What H3 Requires of the Fixture

H3 (T63): F(U_alpha) [TaF finality presheaf section] is identified with a flat Z/2Z-gauge
connection on sigma_alpha(X_alpha) [GU gauge section], and the Cech coboundary condition
maps to the holonomy computation on Y_spin.

For C2 to advance H3, the fixture must find that C-typed admissibility in TI independently
forces the transition function value c(alpha, beta) in {+1, -1} subset Z/2Z, rather than
requiring it as an external parameter. The forced value must be derivable from the source
axioms and extension rules that define C_TaF(r_j).

### 2.3 The Type Mismatch (C1 prerequisite)

T63 identifies a type mismatch: TaF's presheaf is combinatorial (D1 finality profiles,
comparison preorders over a discrete set of finality-class assignments); GU's fields are
continuous (smooth flat Z/2Z gauge connections over Y_spin). The C1 condition requires
bridging this type gap before H3 can be stated as an isomorphism.

The fixture can be run *without* resolving C1 as a full type-bridge, but any cocycle-
forcing result from the fixture must be stated in combinatorial terms (Z/2Z-valued
transition functions on a finite cover), and the C1 bridge is then the subsequent step
needed to transport the fixture result into GU gauge language.

---

## 3. Fixture Specification

### 3.1 The Geometric Setup

**Base space.** Use the simplest topologically nontrivial base: the circle S^1. Label the
base points by an angular parameter theta in [0, 2*pi).

**Two-patch cover.** Choose two open sets:

```
U_+ = {theta : theta in (-pi/4, pi + pi/4)}      (upper semicircle plus overlap buffer)
U_- = {theta : theta in (pi - pi/4, 2*pi + pi/4)} (lower semicircle plus overlap buffer)
```

The overlaps are two connected arcs:

```
U_+ cap U_- = U_{cap,L} cup U_{cap,R}
```

where U_{cap,L} is near theta = 0 and U_{cap,R} is near theta = pi.

**Why two patches and two overlap components.** H^1(S^1, Z/2Z) = Z/2Z. For a two-patch
cover of S^1, a Cech 1-cochain assigns one element of Z/2Z to each connected component of
the overlap. With two overlap components (at theta = 0 and theta = pi), the cochain has
two values c_L, c_R in {+1, -1}. The coboundary of a 0-cochain (a pair of local sections)
is delta(f)(alpha, beta) = f(alpha)|_{overlap} / f(beta)|_{overlap}. For this to be a
coboundary, c_L * c_R = +1 (the product around the circle is trivial). The non-trivial
class has c_L * c_R = -1.

**The Z/2Z bundle.** A flat Z/2Z-principal bundle on S^1 is determined (up to isomorphism)
by its holonomy: an element of pi_1(S^1) = Z mapped to Z/2Z. There are exactly two
isomorphism classes:

- Trivial bundle: holonomy = +1 (contractible monodromy; global section exists).
- Mobius bundle: holonomy = -1 (non-contractible monodromy; no global section).

The non-trivial Cech 1-cocycle (with c_L * c_R = -1) represents the Mobius bundle.

### 3.2 The TI Schema Setup

**Records and extensions.** In temporal-issuance language, the fixture models a two-
observer schema extension scenario. There are two local schema domains:

```
S_+ : the schema on patch U_+  (Alice's admissibility domain)
S_- : the schema on patch U_-  (Bob's admissibility domain)
```

On each overlap arc, there is an extension record e_L (at U_{cap,L}) and e_R (at
U_{cap,R}) that specifies how S_+ and S_- are related on that overlap.

**C-typed admissibility.** Each extension record must pass the C_TaF admissibility check:
it must be consistent with the source axioms of both S_+ and S_- when restricted to the
overlap. Concretely:

```
C_TaF(e_L):  Ax(S_+)|_{U_{cap,L}} cup Ax(S_-)|_{U_{cap,L}} is consistent with e_L
C_TaF(e_R):  Ax(S_+)|_{U_{cap,R}} cup Ax(S_-)|_{U_{cap,R}} is consistent with e_R
```

**The critical question.** Does C_TaF force the transition values c_L = c(+, -)_{U_{cap,L}}
and c_R = c(+, -)_{U_{cap,R}} to specific elements of Z/2Z, or does it leave them free?

### 3.3 The Four Candidate Outcomes (Test Conditions)

The fixture should determine which of the following holds. These correspond to E015's three
options plus the new fourth option:

**Outcome A (E015 option 1 -- no transition data).**
C_TaF does not include any condition on transition values. The admissibility predicate
checks internal consistency of each schema domain separately but does not constrain the
gluing. Result: both c_L and c_R are free parameters; no holonomy is determined. H3
requires additional stipulation. VERDICT: H3 remains stipulation.

**Outcome B (E015 option 2 -- stipulated transition data).**
C_TaF checks transition data but the transition values are an input to the predicate (they
must be provided as a parameter). The admissibility predicate verifies consistency of the
given transition data but does not derive it. Result: holonomy is formally well-defined but
the specific value depends on what transition data was passed in. VERDICT: H3 is a
definitional choice, not a derived theorem.

**Outcome C (E015 option 3 -- forced trivial).**
C_TaF includes a consistency rule that forces identity transitions: any C-typed extension
across an overlap must have c = +1 (identity in Z/2Z). This would arise if, for example,
the admissibility predicate requires that the restriction maps of S_+ and S_- agree exactly
on the overlap, without any nontrivial monodromy. Result: all C-typed coverings have trivial
holonomy; the Mobius bundle is not C-type-admissible. VERDICT: H3 can only identify the
trivial Cech class with the trivial bundle; the T63 non-trivial class (holonomy = -1) is
not derivable from TI admissibility.

**Outcome D (the new fourth option -- forced nontrivial).**
C_TaF includes a consistency rule that forces nontrivial transitions: under specific
source-axiom configurations (e.g., a pair of schemas whose overlap is provably incomplete
under the no-anticipation constraint), the admissibility predicate forces c_L * c_R = -1.
This is the target outcome. It would arise if the SBP no-anticipation condition (a schema
on U_+ cannot contain any axiom about U_- that is not derivable from their overlap) creates
an asymmetry that forces a nontrivial cocycle to maintain global consistency. VERDICT: H3
gets a genuine derivation path; the fixture result should be transported via C1 to GU gauge
language to close the bridge.

**Outcome D' (forced nontrivial under specific conditions).**
Outcome D holds only for specific schema configurations (not all C-typed two-patch covers
of S^1 produce nontrivial holonomy; only those satisfying an additional axiom-configuration
condition). This is a weaker version of Outcome D and is still useful: it identifies the
precise extra condition on TI schema data that is needed to force H3. VERDICT: partial
derivation; H3 holds as a conditional theorem (if the TI schema data is in the specific
configuration, then the holonomy is forced).

### 3.4 Expected Cocycle Outputs

For each outcome, here are the concrete cocycle-level outputs the fixture should produce:

**For Outcome A:** The fixture returns c_L = "unspecified", c_R = "unspecified". Any
value in {+1, -1} is admissible for each. Holonomy = c_L * c_R = undetermined.

**For Outcome B:** The fixture takes (c_L, c_R) as inputs and verifies them. For any
input pair satisfying external constraints (e.g., c_L * c_R = -1 is given), it returns
"admissible". The fixture does not generate c_L, c_R from axioms.

**For Outcome C:** The fixture returns c_L = +1 and c_R = +1 as the unique C-admissible
transition values. The cocycle condition c_L * c_R = +1 = holonomy: trivial. The Mobius
cover (c_L = +1, c_R = -1 or vice versa) fails admissibility.

**For Outcome D:** The fixture returns c_L = f(Ax(S_+), Ax(S_-), U_{cap,L}) and
c_R = f(Ax(S_+), Ax(S_-), U_{cap,R}) as specific elements of Z/2Z determined by the
schema data. The fixture exhibits at least one schema configuration (Ax_+, Ax_-) for
which c_L * c_R = -1 and no external input determined this value -- it was forced by
the admissibility rules. The Mobius Z/2Z bundle is realizable from TI admissibility.

**For Outcome D':** Same as Outcome D, but only for a specified subclass of schema
configurations. The fixture exhibits the subclass criterion explicitly.

---

## 4. Structural Requirements for a Valid Implementation

### 4.1 The No-Anticipation Constraint Must Be Stated Explicitly

The NEXT-TRIGGER-PLAN.md entry (RUN-0041) warns: "Do not run the Cech/sheaf fixture as a
free-standing novelty claim until the no-hidden-schema / no-anticipation class is explicit."

A valid fixture must explicitly state what no-anticipation means in the two-patch setting.
Candidate formulation:

```
No-anticipation (NAC): Ax(S_+) restricted to U_{cap,L} is derivable from Ax(S_+)
restricted to U_+ intersect U_{cap,L} alone. Ax(S_+) cannot contain axioms about
U_- that are not derivable from the overlap.
```

Under NAC, the schemas on each patch are "locally determined" without foreknowledge of
the other patch. This is the constraint that makes the overlap comparison nontrivial: if
Ax(S_+) and Ax(S_-) are each locally determined and their overlap data is inconsistent
in a specific way, the admissibility predicate must choose between (i) rejecting one
extension, (ii) requiring a nontrivial cocycle to resolve the inconsistency, or (iii)
producing a contradiction. The fixture must not smuggle the cocycle value into the schema
through the back door of cross-patch axioms.

### 4.2 The Cocycle Must Be Derived, Not Input

The fixture must demonstrate a clean separation between:

- Schema input data: Ax(S_+), Ax(S_-), overlap sets U_{cap,L}, U_{cap,R}.
- Derived output: transition values c_L, c_R in {+1, -1}.

The transition values are the output of the admissibility computation, not part of its
input. If the fixture implementation requires setting c_L and c_R before running the
admissibility check, it implements Outcome B and must be labeled as such.

### 4.3 The Two-Patch Nontriviality Test

A valid fixture for Outcome D or D' must include a concrete nontriviality test:

```
Nontriviality test: Exhibit schema data (Ax_+, Ax_-) such that:
  (1) C_TaF(e_L) passes
  (2) C_TaF(e_R) passes
  (3) c_L * c_R = -1 (Mobius holonomy)
  (4) Neither c_L nor c_R was provided as an external input
  (5) The derivation of c_L and c_R uses only Ax_+, Ax_-, and the NAC constraint
```

If no such (Ax_+, Ax_-) pair exists, the fixture must return Outcome C or A and explain
why the nontrivial Mobius bundle is not C-type-admissible.

### 4.4 The Globality Test

H3 requires that the fixture result can be extended to a full cover (not just two patches).
The two-patch S^1 fixture is the minimal case. A valid fixture should note whether its
outcome (A/B/C/D/D') generalizes to:

- Any finite cover of S^1: the Cech cohomology H^1(S^1, Z/2Z) = Z/2Z must be reproduced
  by the admissibility predicate for all covers with sufficient patches.
- The GU four-context CHSH cover: the T63 cover has four context patches with a 4-cycle
  structure; the fixture result must extend to covers with more than two patches and with
  multiple overlap components.

If the fixture result does not generalize to the CHSH cover, the H3 contact remains
partial even for Outcome D.

### 4.5 Independence from Berry Phase Data

The T63 High-confidence entries establish that the non-trivial Cech class has holonomy = -1
via a Berry phase computation (the exp(i*pi) = -1 phase around the 4-cycle). This is a
separate derivation. The cech_sheaf_fixture must NOT rely on Berry phase data as an input.
It must derive the cocycle from schema admissibility alone. If the fixture uses Berry phase
data to set up the schema, it is circular with respect to T63's Berry phase argument.

---

## 5. Test Conditions Summary

The following test conditions constitute the fixture specification as a checklist:

```
TC-1: The fixture specifies a two-patch open cover of S^1 with explicit overlap data.
TC-2: Local TI schemas Ax(S_+) and Ax(S_-) are defined as data inputs.
TC-3: The no-anticipation constraint (NAC) is stated and enforced.
TC-4: C-typed admissibility C_TaF is applied to extension records at each overlap.
TC-5: Transition values c_L, c_R are computed as outputs (not inputs) of C_TaF.
TC-6: The cocycle condition c_L * c_R is computed and compared to +1/-1.
TC-7: The outcome is classified as A/B/C/D/D' with justification.
TC-8: If Outcome D or D': exhibit explicit (Ax_+, Ax_-) passing the nontriviality test.
TC-9: If Outcome D or D': state the schema-level condition that forced the nontrivial value.
TC-10: The fixture result does not use Berry phase as an input.
TC-11: The globality test (generalization to CHSH four-patch cover) is assessed.
```

---

## 6. Connection to C2 Closure Condition

C2 states (from `n3-h3-cech-holonomy-2026-06-23.md`):

> Execute the planned `cech_sheaf_fixture` (E015 next_fixture) to test whether C-typed
> admissibility independently forces Z/2Z transition values on a two-patch cover of S^1.
> If it does (fourth option found), carry the result to T63 to ask whether the TaF
> admissibility predicate forces c(alpha,beta). If it does not, H3 is a stipulation
> rather than a theorem.

This specification file is the implementation target for C2. Running the fixture as
specified above and obtaining one of the five outcomes (A/B/C/D/D') constitutes executing
C2. The outcome classification then determines H3's epistemic status:

| fixture outcome | H3 status after C2 execution |
|----------------|------------------------------|
| Outcome A | H3 stipulation (no cocycle data generated by admissibility) |
| Outcome B | H3 stipulation (cocycle data accepted but not derived) |
| Outcome C | H3 derivable only for trivial class; T63 non-trivial class cannot be identified |
| Outcome D | H3 derivation path open; carry result to T63 via C1 type-bridge |
| Outcome D' | H3 conditional derivation; additional schema condition required |

---

## 7. Connection to C1 (Type-Bridge) and C3 (Spacelike Overlap)

**C1 and C2 are decoupled at the specification level.** The fixture can determine Outcome
D or D' in purely combinatorial TI terms without constructing the type-bridge to smooth
Z/2Z gauge connections. The C1 type-bridge becomes the next step after a successful
Outcome D fixture:

```
C2 result: TI admissibility forces cocycle c_L * c_R = -1 for schema (Ax_+, Ax_-)
C1 goal: Show that (Ax_+, Ax_-) maps to flat Z/2Z-connection data on Y_spin
         via a functor F: {TI schema pairs} -> {Z/2Z bundles on Y_spin}
         such that F(Ax_+, Ax_-) has holonomy = c_L * c_R.
```

If C1 can be constructed, then H3 becomes a theorem about the image of TI admissible
schema data under the functor F. The fixture provides the cocycle value; C1 provides the
embedding.

**C3 (spacelike overlap).** The fixture is set up over S^1 with geometric overlaps. The
C3 condition (spacelike-separated observers may have empty geometric overlap sigma_A(X_A)
cap sigma_B(X_B)) is not a problem for the fixture on S^1, where overlaps are specified
by the cover data. The C3 fix (replacing geometric overlap with fiber-bundle identification
over distinct spacetime points connected by a shared label) becomes relevant when
transporting the fixture result to the actual GU observer scenario. The fixture does not
need to solve C3; it provides the algebraic prototype that C3 must lift into the geometric
GU setting.

---

## 8. Result: Reconstruction-Grade Specification

**What has been computed.** This file provides a complete specification for the
`cech_sheaf_fixture`: explicit geometric setup (two-patch S^1 cover with two overlap
components), TI schema setup (Ax_+, Ax_- under NAC), four candidate outcomes (A/B/C/D)
plus the partial Outcome D', expected cocycle outputs for each outcome, eleven test
conditions (TC-1 through TC-11), and a table mapping fixture outcomes to H3 epistemic
status.

**Grade achieved: reconstruction.** The specification is fully explicit and runnable.
The remaining gap between this file and a verified implementation is:

1. An agent in the temporal-issuance repo must instantiate Ax_+ and Ax_- as concrete TI
   schema objects (specific SBP axiom sets, specific C-typed extension records) and run
   TC-1 through TC-11.
2. The outcome classification (A/B/C/D/D') must be derived from that execution, not
   assumed.
3. If Outcome D or D' is found, the explicit (Ax_+, Ax_-) pair must be recorded and
   transported to T63 for the C1 type-bridge step.

This file is the specification that the temporal-issuance team needs to build the fixture.
It is not yet the execution of the fixture.

---

## 9. Verdict

**Verdict: CONDITIONALLY_RESOLVED**

The full cech_sheaf_fixture specification (inputs, test conditions, expected cocycle
outputs, structural requirements) is now written down precisely enough to serve as a
concrete implementation target. C2 can be advanced to execution by any agent or contributor
who can instantiate TI schema objects (Ax_+, Ax_-) and run the eleven test conditions.

The N3 closure condition C2 is not yet discharged (no fixture has been run), but it is
no longer specification-blocked: the blocking status recorded in
`n3-h3-cech-fixture-execution-2026-06-23.md` was "missing C-typed section-compatibility
predicate, missing two-patch S^1 cover data, missing rule deciding allowed overlap
cocycles." All three are now specified in this file.

**Remaining gap.** Execute the fixture as specified. Record whether the execution yields
Outcome A, B, C, D, or D'. Update H3 status accordingly.

---

## 10. Explicit Failure Conditions

The specification itself is falsified if any of the following hold:

**FS-1 (NAC inconsistency):** The no-anticipation constraint as stated is inconsistent
with TI's actual SBP architecture. If NAC cannot be enforced at the schema level (because
TI axioms are necessarily global and cannot be restricted to patches), the two-patch setup
breaks down and a different fixture geometry is needed.

**FS-2 (E015 options are exhaustive):** E015's claim that no fourth option exists turns out
to be a theorem rather than a conjecture based on limited fixture size. If the two-patch
S^1 case with NAC provably falls into Outcome A, B, or C, then Outcome D is impossible and
H3 cannot be derived from TI admissibility at all.

**FS-3 (C1 is provably unconstructible):** Even if Outcome D is achieved (TI admissibility
forces nontrivial cocycles), if the D1 finality profiles contain non-Z/2Z structure (e.g.,
a richer order type, or a feature that requires more than Z/2Z to represent), then the C1
type-bridge to smooth Z/2Z gauge connections on Y_spin cannot be built and Outcome D
does not advance H3 in GU terms.

**FS-4 (Spacelike overlap is empty by construction):** If the C3 spacelike-overlap problem
is not a fixable oversight but is a fundamental obstruction (Alice's and Bob's observer
sections sigma_A, sigma_B never share a fiber in Y_spin for spacelike-separated events),
then H3 cannot be stated geometrically even if the fixture succeeds. C3 must be resolved
independently.

**FS-5 (Fixture result uses Berry phase):** If the only TI schema configurations (Ax_+,
Ax_-) that force nontrivial cocycles are those that encode Berry phase data implicitly,
the fixture is circular with respect to T63's Berry phase argument. The result is
self-consistent but not an independent derivation.

**FS-6 (Fixture forces trivial holonomy universally):** If TC-6 always returns c_L * c_R
= +1 for all C-typed schema data under NAC (Outcome C universally), then TI admissibility
is structurally unable to produce the Mobius bundle. H3 would then require a GU-side
mechanism that has no TI counterpart, and the T63 non-trivial class is not derivable from
TI admissibility.

---

## 11. Open Questions

1. **Which TI schema objects instantiate Ax_+ and Ax_-?** The specification leaves the
   schema data abstract. A TI agent must choose specific SBP axiom sets. Candidate: Ax_+
   is the schema of Alice's observation domain; Ax_- is the schema of Bob's observation
   domain; the overlap records encode joint measurement outcomes. This is the natural
   instantiation for the CHSH scenario, but it must be made precise in TI terms.

2. **Does NAC follow from TI's existing no-hidden-schema governance rule?** If NEXT-
   TRIGGER-PLAN's "no-hidden-schema" condition is precisely NAC, the specification already
   uses an existing TI governance constraint and no new rule is needed. Verify this before
   implementing the fixture.

3. **Is the two-patch S^1 cover sufficient, or is the CHSH four-patch cover needed?** The
   two-patch cover is the minimal case, but T63's actual claim involves a four-patch cover
   (four CHSH contexts). The fixture should be implementable on two patches and then lifted
   to four patches. State explicitly whether the Outcome D result on two patches automatically
   implies the result on four patches via Mayer-Vietoris, or whether the four-patch case
   requires separate analysis.

4. **What is the connection between Outcome D and the W-H3 structural parallel established
   in `taf-h3-contact-2026-06-23.md`?** That file identified the candidate Z -> Z/2Z
   reduction map c(alpha, beta) = (-1)^{delta_{-}(alpha cap beta)} (where delta_{-}(S)
   is the parity of negatively-weighted records in S). If the fixture is run with TI schema
   data encoding a GU-type record-graph, does this reduction map produce the forced cocycle
   value? This would be a concrete link between the two contact analyses.
