# Observers Select Values by Symmetry-Breaking: A Non-Circular Arena/Value Partition and a Lawvere No-Closure Theorem

**Draft, 2026-07-11. GU-INDEPENDENT by design: the results are a structural theorem about observers,
admissibility, and symmetry-breaking; a physical theory (Geometric Unity) is one instance, and the theorem's
value does NOT depend on it. Every quantitative/logical claim ties to a reproducible test in `tests/` (W62,
W67-W70, W73-W77, all exit 0). External publication is Joe-gated.**

## Abstract

We formalize the intuition that the laws of physics separate into an observer-INVARIANT structure and
observer-SELECTED values, and prove a structural theorem for it. **First (the non-circular partition):** we give
a characterization of "arena" (forced) vs "value" (selected) that does NOT reference forcing and is therefore not
true-by-definition -- ARENA = invariant of the unbroken observer-symmetry / renormalization-group fixed-point
data; VALUE = a quantity requiring symmetry-BREAKING (a vacuum/frame/direction choice) to specify. This is
computable a priori (Schur's lemma, invariant-subspace lattices, one-loop beta signs) and it sorts every test
case correctly where dimensional and discrete-vs-continuous characterizations fail. **Second (the theorem):** we
model an observer as a self-referential admissibility algebra with a firewall (a grading `J` separating admissible
from inadmissible states), and prove -- via Lawvere's fixed-point theorem -- that no self-referential closure of
the admissibility structure across the firewall exists without a residual selection, AND that any DEFINITE
admissibility valuation the observer commits to necessarily BREAKS the firewall symmetry, i.e. is a vacuum choice.
The value is therefore not merely unforced but forced-to-be-a-selection. The identification "value = the
observer's symmetry-breaking selection" is thus a theorem, not a postulate. We give its rigorous skeleton
(machine-checked), the two lemmas its physical realization reduces to, and the honest residual: a rank-`>1`
indefinite-metric (Krein) Tomita-Takesaki modular theory, currently an operator-algebra frontier.

## 1. Introduction

It is often said that a fundamental theory should fix the STRUCTURE of physics while leaving certain VALUES (a
scale, a vacuum, a mixing pattern) to be chosen. Made precise, this is a claim about a partition of physical
quantities into forced and selected, and about who does the selecting. We make it precise and prove the load-
bearing part.

Two obstacles have kept such claims informal. (i) CIRCULARITY: if "arena" just means "the forced quantities" and
"value" the unforced ones, the claim "the arena is forced, the value selected" is vacuous. (ii) The selector: what
performs the selection, and why is the residual a genuine selection rather than mere ignorance. We resolve (i)
with a characterization of arena/value that is defined independently of forcing (Section 3), and (ii) with a
fixed-point theorem that identifies the selector's act with symmetry-breaking and forces the residual to be one
(Sections 4-5).

## 2. Setup: the observer as a self-referential admissibility structure

Model the observer as an operator algebra `A` of admissible observables on an indefinite-metric (Krein) space,
with a grading operator (the "firewall") `J` separating admissible (positive-norm) from inadmissible (negative-
norm) states, and a self-reference: the observer is a state on the very algebra it grades. The physical inner
product is the graded (keep-and-grade / PT) one; the firewall is the selection surface between the observer's
admissible arena and the individual selected state. This is the abstract skeleton; a physical realization
identifies `A` with a region's admissibility algebra and `J` with a modular conjugation (Section 6).

## 3. The non-circular arena/value partition (`tests/W73`)

**Definition.** ARENA = a quantity fixed as an INVARIANT of the unbroken observer-symmetry, or as renormalization-
group fixed-point data. VALUE = a quantity that requires symmetry-BREAKING (a choice of vacuum, frame, or
direction) to specify.

**Non-circularity.** Invariance-vs-breaking is a group-theoretic / RG fact -- decided by Schur's lemma, the
invariant-subspace lattice of a representation, or the sign of a one-loop beta function -- computable BEFORE and
INDEPENDENTLY of any analysis of what is forced. Hence "invariant => forced" is a synthetic claim one can test,
not an analytic identity. The characterization is falsifiable: a forced symmetry-breaking value, or an unforced
invariant, would refute it.

**It sorts the cases where rivals fail (`tests/W73`).** Against a battery of physical quantities, the symmetry
characterization sorts every decided case correctly (0 misses), while a DIMENSIONAL characterization
(arena = dimensionless) misses the dimensionless-but-selected mass ratios, and a DISCRETE/CONTINUOUS
characterization misses the continuous-but-forced dimensionless couplings pinned at a fixed point. The
discriminating cases are exactly those: a dimensionless mass ratio that is nonetheless a VALUE (it requires
breaking a family symmetry that Schur otherwise forces to degeneracy), and a continuous coupling that is
nonetheless ARENA (pinned by an asymptotically-free fixed point, requiring no vacuum choice).

## 4. The firewall, the self-reference, and the Lawvere frame (`tests/W70, W75`)

The three ingredients of an impossibility theorem are present: the FIREWALL is a partition; ADMISSIBILITY is an
agreement predicate across it; the SELF-REFERENCE (the observer as a state on its own admissibility algebra) is a
diagonal. Lawvere's fixed-point theorem -- the categorical core of Cantor, Godel, Tarski, and the halting problem
-- states that in a cartesian-closed category a point-surjection `A -> B^A` forces every endomorphism of `B` to
have a fixed point; contrapositive, a FIXPOINT-FREE endomorphism obstructs the self-referential closure. The
firewall grading-flip -- the swap on `{admissible, inadmissible}` induced by `J` -- is fixpoint-free for the
identical reason negation is in Cantor/Godel. This is the correct impossibility frame; it requires only the
partition and agreement predicate the firewall supplies.

## 5. The theorem: any definite valuation breaks the symmetry (`tests/W75`)

**Proposition (machine-checked, exhaustive over finite models + Cantor cross-check).** Let the firewall involution
`alpha` (the grading-flip on `{admissible, inadmissible}`) be fixpoint-free. Then there is no `alpha`-invariant
admissibility valuation `p: A -> {admissible, inadmissible}`: the fixed-point count shows `alpha . p = p` forces
every value `p(a)` to be an `alpha`-fixed point, of which there are none. Therefore any DEFINITE valuation the
observer commits to is non-`alpha`-invariant -- it BREAKS the firewall symmetry.

**Consequence.** Combined with Section 3's definition (VALUE = requires symmetry-breaking), the residual selection
forced by the Lawvere obstruction IS a value in the precise, non-circular sense. So "the observer selects the
value by breaking the symmetry" is a THEOREM, not a postulate: the self-referential admissibility structure cannot
close across its firewall without a residual, and the residual is necessarily a symmetry-breaking selection. The
control case `alpha = identity` yields only invariant valuations (every choice symmetric), confirming that the
symmetry-breaking is contributed by the fixpoint-free firewall, not by "a residual exists" alone.

**Honest core.** The Lawvere diagonal ALONE forces only a generic residual; the symmetry-BREAKING character is
supplied by the fixpoint-freeness of `alpha` -- a named hypothesis of the theorem, hence forced, not smuggled.

## 6. Physical realization and the residual (`tests/W67-W69, W77`)

A physical instance identifies `A` with the admissibility (von Neumann) algebra of a spacetime region and `alpha`
with the grading of a Krein modular conjugation `J = C.PT`; the observer's record structure maps to a source
action / a choice of state via the Connes Radon-Nikodym cocycle bijection (which realizes the observer-record
<-> selection map at the SELECTION level and provably does not reintroduce a rate-dependent reading). Two lemmas
complete the physical theorem: L1 (the record<->selection map is a point-surjection -- the Connes bijection) and
L2 (the grading-flip is fixpoint-free -- the modular conjugation `J^2 = 1`).

**The residual (honest).** L2 requires modular theory in an INDEFINITE metric. The modular FLOW survives a Krein
space (Gottschalk 2002) and, at rank of indefiniteness 1, a full Tomita theorem with the antilinear conjugation
exists (Shulman 1997). At rank `> 1` the conjugation extends IFF the Krein modular operator `Delta = S^+ S` has
real-positive spectrum ("modular-PT-unbroken"); it obstructs on the exceptional (non-real) locus. Whether a given
physical algebra is PT-unbroken is a concrete question (in the fourth-order-gravity instance it is unbroken on the
physical spin-2 sector across the interacting regime, with a conformal-sector subtlety governed by a coupling
sign). So the ABSTRACT theorem (Sections 3-5) is complete and machine-checked; its physical realization is
complete modulo one operator-algebra frontier problem: rank-`>1` Krein Tomita-Takesaki.

## 7. Relation to prior work

- **Self-reference / impossibility:** Lawvere's fixed-point theorem (unifying Cantor/Godel/Tarski/halting).
  Delta: applied to an admissibility firewall to force a symmetry-breaking selection, supplying the
  agreement-under-partition predicate that generic diagonal arguments in physics have lacked.
- **Modular theory:** Tomita-Takesaki; Bisognano-Wichmann (modular flow = boost, fixed surface = horizon);
  Gottschalk (Krein flow); Shulman (Pi_1 conjugation). Delta: the rank-`>1` extension as the identified residual,
  and the identification of the firewall with the modular conjugation.
- **Indefinite-metric / PT quantization:** Bender-Mannheim; Mannheim. Delta: the grading as the observer's firewall
  and the no-distinguished-positive-state as the value-selection.
- **Curie's principle:** the folk principle that symmetric causes have symmetric effects, so asymmetry
  (a value) requires broken symmetry. Delta: we make it a non-circular partition + a fixed-point theorem, and we
  note honestly that the result may be GENERIC in Curie's sense rather than unique to any one theory -- which is a
  FEATURE for a structural theorem (it applies broadly), not a defect.

## 8. Status / grade

The abstract results (the non-circular partition, Sections 3; the no-closure + symmetry-breaking theorem,
Sections 4-5) are machine-checked (`tests/W73, W70, W75`, exit 0) and stand independently of any physical theory.
The physical realization (Section 6) is complete modulo the rank-`>1` Krein Tomita-Takesaki residual. Honest
caveat carried throughout: the structure may be generic (Curie), so the claim is a GU-INDEPENDENT structural
theorem about observers and symmetry-breaking, of which any specific unified theory is one instance. Target:
math-ph / foundations. External publication Joe-gated.
