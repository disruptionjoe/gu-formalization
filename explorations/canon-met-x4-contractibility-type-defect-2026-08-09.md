---
artifact_type: hostile_review_finding
created: 2026-08-09
status: TWO_INTERNAL_CONTRADICTIONS_IN_canon-no-go-class-relative-map__ONE_LOAD_BEARING_FOR_THE_FREED_HOPKINS_OPTION_B_ELIMINATION__NO_STANDING_VERDICT_OVERTURNED
grade: "DOCUMENTATION DEFECT, verified by direct read of the cited lines. Both statements in D8 are
  individually TRUE -- of DIFFERENT objects. No new mathematics is claimed here and no verdict flips.
  D8's blast radius is bounded because the affected lane is already held CONDITIONALLY_RESOLVED under
  correction FH-01."
review_charge: "AGENTS.md hostile-review charge 2 -- 'find where rigor is defending a superseded or
  mistyped object.'"
target: canon/no-go-class-relative-map.md
canon_verdict_change: none
found_during: "Y14/X4 systems spec drafting, 2026-08-09"
---

# Finding: `Met(X^4)` is typed two incompatible ways inside one canon file

## D8 — the contractibility type error

**Both statements are in `canon/no-go-class-relative-map.md`.**

- **Sec 2.3 (line ~219):** *"Met(X^4) is contractible (convex cone)"*
- **Sec 2.1 (lines ~37, ~91):** fiber `GL(4,R)/O(3,1)`, *"non-compact; homotopy type `RP^3 x R^+`"*

### Diagnosis

The space of **Riemannian** metrics is a convex cone and *is* contractible. Standard, and true.

The space of **Lorentzian** metrics is **not** convex — the sum of two Lorentzian metrics need not be
Lorentzian — and the pointwise fiber `GL(4,R)/O(3,1)` has homotopy type `RP^3 x R^+ ~= RP^3`, which is
**not contractible**.

The program defines `Y14 = Met(X4)` as the bundle of **pointwise Lorentzian** metrics
(`canon/w2-y14-spin-structure.md:20`). **Sec 2.3 is therefore applying the Riemannian fact under the
Lorentzian name.**

This is the exact failure mode `GEOMETER-VS-PHYSICS-OBJECTS.md` exists to prevent — *"NEVER default
silently -- to either side."* A file that warns against silent defaulting in one section performs it in
another. That is also why it survived: **both sentences are true**, so neither reads as wrong in isolation.

### Blast radius — bounded, and stated honestly

At Sec 2.3 the contractibility is used to **eliminate `Met(X^4)`** as a candidate noncontractible
observer-state space `X_obs`, inside an argument concluding that all three candidates die and *"the no-go
lemma's two escape doors never open together."*

**If `Met(X^4)` is non-contractible, that first elimination fails and one door reopens.**

What this does **not** do: overturn a standing verdict. The lane is already held `CONDITIONALLY_RESOLVED`
and explicitly **not** promoted, per correction FH-01, on grounds of same-session circularity and an OPEN
root (RC1).

What it **does** do: supply **an independent additional reason that lane cannot close** — one FH-01 does not
list. FH-01's reasons are all provenance-grade (same-session, unverified, open root). This one is
mathematical: a load-bearing premise is mistyped.

### Recommended fix

1. Type the two objects separately wherever `Met(X^4)` appears — `Met_Riem(X^4)` (contractible convex cone)
   vs `Met_Lor(X^4)` (fiber `GL(4,R)/O(3,1)`, homotopy `RP^3 x R^+`, non-contractible).
2. Re-run the Sec 2.3 Option-B elimination with `Met_Lor`. If `Met_Lor` survives as a noncontractible
   candidate, the FH Option-B closure needs the **second** door (non-extendability) argued for it directly,
   which as far as this pass can tell has not been done.
3. Sweep for the same substitution elsewhere; the two names are used interchangeably across the file.

---

## D9 — stale `CP^2` scope tag (same file)

- **Sec 2.3 scope tag (CANON-5):** *"The Witten Met(X4) entry (Sec 2.1) and `canon/w2-y14-spin-structure.md`
  treat X4 as generic-orientable and **explicitly admit X4 = CP2**"*
- **Sec 2.1 own text:** *"CP2 is **excluded** -- it is non-spin"*; and per W2-FC1, *"X4 spin is a genuine
  standing PRECONDITION, not a free structure choice."*

Almost certainly a scope tag written before W2-FC1 was applied and not swept afterward.

**Severity low, fix mechanical, and worth doing:** a cross-reference that misreports what it points at is
worse than no cross-reference, because it gets trusted. Anyone reading Sec 2.3 to learn Sec 2.1's scope
gets the opposite of Sec 2.1's stated scope.

---

## What is NOT claimed here

- No new mathematics. Both D8 statements were already in the file; this pass only observed that they cannot
  both be about the same object.
- No verdict flip, no canon promotion, no status change. Per `AGENTS.md`, a verdict change would require a
  hostile adversarial review by field specialists filed alongside it; nothing here rises to that.
- No claim that the Freed-Hopkins Option-B conclusion is **wrong** — only that one of its three eliminations
  is unsupported as written, in a lane already held conditional for independent reasons.

## Suggested disposition

Per the `AGENTS.md` over-determined-row protocol: **the finder escalates, an independent owner adjudicates.**
This note is the escalation. D9 can be swept immediately by anyone. D8 wants an owner who can decide whether
the Option-B elimination survives retyping.
