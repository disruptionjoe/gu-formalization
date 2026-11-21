---
title: Zero-total premise, grading descent and structural balance
status: exploration
doc_type: structural-result
created: '2026-11-20'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Source-premised cancellation and exact grading/zero-mechanism requirements
actual_delta: Same-grading and symmetry-descent requirements sharpened; no class-wide
  kill
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


# Zero total must be in the same grading

program_target: X-P1-P2-P3
tier: T2
expected_delta: Source-premised cancellation and exact grading/zero-mechanism requirements
actual_delta: Same-grading and symmetry-descent requirements sharpened; no class-wide kill

This completes Item1 step2 as reframed by Joe on 2026-11-20(b). It does not
retype the P3 row. The retained external-integer-count typing has a conditional
rival: **P3 = -ind_G(D_hidden)** only on an actual compatible observation
complex with independently justified total index zero and a physical-count
map. The source premise is retained as a premise, never promoted to a proof.

```gu-typed-objects
result: Source-premised observed-hidden cancellation and grading applicability audit
carrier: same graded Banach Fredholm observation complex; separate closed positive spin4 benchmark and native Lorentzian projected RS symbol LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: actual native indefinite tensor-spin pairing distinguished from positive auxiliary Hilbert topology ON=declared_carrier
real_structure: complex index first; Cl95 quaternionic and Cl77 real intertwiners tested separately
grading: ungraded selfadjoint operator, ambient chiY and coherent G=r tensor chiH are distinct
action_owner: N/A -- structural tests of supplied operators; no source action constructed
target: actual section contraction q and weak-current/physical-domain bridge MAP-TYPE=intertwiner
```

## A. Conditional theorem, with the source translation visible

**Source-premised conditional statement.** IF the total theory is non-chiral
in grading G in the sense asserted by SC-CHI-01/04, **and that assertion is
realized as ind_G(D_total)=0 on the specified Fredholm complex**, AND the
observed chiral grading descends from G through a compatible observation
complex, THEN `ind_obs = -ind_hidden` in that same grading.

The italicized mathematical content cannot be suppressed: SC-CHI-01/04 assert
non-chiral fundamental fields with effective decoupling/branching, not a
Fredholm operator, domain, grading or an index theorem. Balanced field
multiplicities alone do not imply zero index. To interpret this as *weak*
chirality or a family count, also prove that the descended grading and index
are the physical weak/current grading and the intended observable. Effective
one-sided weak currents may occur at index zero (Nov11 §5 correction).

Precisely: take a closed chiral operator, viewed as bounded `D:E→F` with
its graph domain E; fix positive Banach/Hilbert topologies and the single
G grading used to select this chiral arrow. Continuous surjections
`qE:E→Eo`, `qF:F→Fo` have closed kernels Eh,Fh, and satisfy
`qF D = Do qE`. Require D, Dh=D|Eh and Do all Fredholm on these actual
spaces. The degreewise short exact complexes give

`0→ker Dh→ker D→ker Do→coker Dh→coker D→coker Do→0`,

so `ind_G D = ind_G Dh + ind_G Do`. Add the separately identified balance
premise `ind_G D=0`. Cancellation follows. The hidden grading is the induced
one; reversing it to obtain a desired sign is not allowed. This reuses the
Nov11 additivity proof rather than claims a new Fredholm theorem.

The small Lean file `ObservedHiddenPremise.lean` checks the conditional integer
corollary and the closed-comparison arithmetic, without `sorry`. It assumes
additivity and balance. It does **not** complete packet step3's exact-sequence
formalization or certify an analytic domain.

## B. Grading audit on the actual observation carrier

Reuse the literal contraction `q:R_Y→B=H*⊗S`, `R_Y=ker Γ_Y`, with
`H⊕N` nondegenerate, dimensions4+10. It is surjective, and its hidden kernel
is `K=ker Γ_N` in the normal one-form slots. This is not an arbitrary
projection onto horizontal gamma-traceless states. A moving section is handled
through its actual split; no generic graph replacement is introduced.

| Object / grading | (i) Total zero? | (ii) Does the observed weak grading descend? |
|---|---|---|
| Full ungraded selfadjoint Fredholm operator | Yes, automatically: kernel and cokernel identify. This says nothing about the index of its chiral block. | No chiral grading supplied by this zero; it cannot answer (ii). |
| Ambient `χY=χHχN` on the projected RS symbol | All three integer indices are zero in the **closed positive spin4, rank10 normal** comparison, since `ch(S_N+−S_N−)` starts in degree10. Native Lorentzian/domain/physical index: open. | q descends χY to **χHχN**, not χH on the full observed B. Both normal grades survive. Thus it fails the plain horizontal-Weyl identification. A different physical weak/current identification is unproved, not disproved. |
| Naive slotwise χH on R_Y | Not a grading of R_Y: horizontal and normal gamma traces transform with opposite signs. | Fails already at carrier preservation. |
| Coherent `G=r⊗χH`, r=+1 on H*, −1 on N* | Not zero by general structure. Closed metric-normal comparison gives **−820 signature(X)**. Native global balance is an explicit source-realization premise still open. | **Yes kinematically:** `qG=χHq`, with hidden grade `−χH`. Physical weak-current projector and common domain descent remain unproved. |

The quotient condition for projectors is equally explicit:
`q (1±G)/2 = (1±χH)/2 q`. It proves kinematic Weyl descent, not a
selected interacting weak-sector projector or decoupling law. Neither source
claim supplies the missing operator/current/physical-domain map. Ambient
χY can agree with χH after a separately justified normal-chirality selection,
but that changes the observed complex and its balance calculation; it is not
the full q above.

### The closed comparison rules out the shortcut, not the source class

For the positive closed spin4 benchmark with `N≅Sym²T*X`, the SAME G gives

`(ind_total, ind_hidden, ind_observed)=(-820,-1188,368) signature(X)`.

The probe re-derives these from `p1(N)=6p1(TX)` and the spin characters.
If signature is nonzero, premise (i) fails. If signature is zero, all three
indices vanish, so this benchmark gives no nonzero observed count either.
On K3 specifically the triple is `(13120,19008,-5888)` in this convention.
These are not native GU predictions. No topology is chosen to fit a count.
The already-owned full-Clifford companion also changes the observable to
`300 signature(X)` with the opposite trace grade; it cannot be silently
substituted for the isolated R_Y calculation or source scalar ν.

Thus no **tested full-carrier closed-comparison route** has both a balanced
total and a nonzero observed index identified with the desired weak grading.
That is a structural restriction, **not** a proof that no grading/realization
in action C can do so. Native noncompact ends, coupled operators and physical
selection remain outside this completed comparison. The requested universal
kill condition is not established; X-P1-P2-P3 remains constrained/open.

## C. Structural routes to zero: exact hypotheses

### Cross-chirality Krein route

For a supplied odd selfadjoint Fredholm operator A on `H+⊕H−`, suppose a
bounded invertible K preserves its actual closed domain, exchanges grades,
and satisfies `A*=A` and `A* K=K A` as operator/domain identities. Then
`[A,K]=0`, so K identifies its two zero-mode spaces and the chiral index is
zero. In the involutive model identify the halves so K=σ1⊗I. Oddness gives
`A=[[0,B],[C,0]]`; Krein selfadjointness gives B*=B and C*=C, while positive
Hilbert selfadjointness gives C=B*. Together B=C=B* and A=σ1⊗B.

**Oddness plus Krein selfadjointness alone is insufficient for that normal
form.** `[[0,1],[2,0]]` is an exact countercontrol. The function-space theorem
lists Hilbert selfadjointness, but its short structural summary suppresses it;
we use the complete premise list. Spectral ± pairing by itself also leaves
chiral zero modes unpaired: an odd selfadjoint doubled rectangular map has
ungraded index0 and chiral index1. Kramers doubling can give index2, not0.

For the actual Lorentzian *spacetime* tangential Q symbol there is a further
positive-adjoint obstruction: on R_Y,
`tr(Qξ²) = dim(S)(m−1)(1−4/m²) g⁻¹(ξ,ξ)`.
The formula follows from `Q²=kI−(4/m)U V` and
`V U=(m−1)k/m`. For m14 the factor is positive. Spacelike and timelike ξ
therefore have opposite nonzero square traces. No single scalar phase and
positive fiber metric can make every such principal symbol Hermitian (a
Hermitian matrix has nonnegative real square trace). This prevents directly
applying the positive-Hilbert σ1⊗B package to that spacetime symbol. It is
not a statement about an extracted Hamiltonian, a changed coupled completion,
or the separate positive elliptic comparison.

There is a **weaker zero-index route that does not need the σ1⊗B normal
form**. With K=σ1, genuine Krein selfadjointness already makes the two
chiral blocks individually selfadjoint on their identified Hilbert spaces.
If the relevant block is Fredholm, its index is zero even when the other
block differs. More generally write the nondegenerate cross-G form as
`K=[[0,L],[L*,0]]`, with bounded invertible L. Krein selfadjointness gives
`C*L*=LC` for the lower chiral block C; if this holds with the actual
adjoint domains, LC is selfadjoint, so `ind C=ind(LC)=0`. Thus failure of positive Hilbert selfadjointness only
prevents the canonical normal-form route; it does not eliminate this second
route. Its exact unproved native hypothesis is a **bounded nondegenerate
cross-G pairing and genuine adjoint-domain/Fredholm realization**, not merely
formal coefficient compatibility.

For the native nondegenerate normal split, `ker Γ_N` has a nondegenerate
inherited tensor-spin form: the normalized metric-dual gamma insertion gives
its orthogonal complement. Therefore, if total, hidden and quotient operators
all have compatible closed domains and the same cross-G Krein-selfadjoint
package, each chiral index is zero separately. The quotient pairing here
means the form transported from the orthogonal complement, not a claim that
an arbitrary form descends through a nonradical kernel. This is a stronger
conditional obstruction to a nonzero observed integer, still not a native
analytic certificate.

An indefinite K-adjoint differential expression is not a positive Hilbert
selfadjoint operator. Existing LC moving-section leakage and later structural
repairs also do not supply a common selfadjoint Fredholm domain. No actual
source operator in the desired G with all these premises has been identified.

### Real or quaternionic route

For an odd **Hilbert-selfadjoint Fredholm** A, a bounded invertible
antilinear J with `JG=-GJ`, `JA=±AJ`, and preservation of the actual domain
pairs the two chiral zero-mode spaces, hence gives index0. Equivalently prove
a direct J-induced isomorphism `ker D+ ≅ ker (D+)*` with the actual adjoint
domain. For a non-selfadjoint odd A, pairing ker D+ with ker D− does not
suffice: D− need not be (D+)*. For example `σ1⊗S` with unilateral shift S
has a grade-exchanging real symmetry but chiral index−1.
Either J²=+1 or −1 works when it **exchanges grades**. If J preserves grades,
J²=−1 only forces even complex multiplicities; J²=+1 forces no parity rule.
Neither alone forces zero. The exact finite controls distinguish all cases.

In the native Clifford fixture and a separate signature control, the Cl(9,5)
quaternionic J and Cl(7,7) real J
commute with gamma multiplication. The K77 control is not a proved physical
K77↔K95 transfer. They preserve the ambient volume grade,
but exchange Lorentzian χH (its normalization contains i), and hence the
coherent G. This gives a precise candidate symmetry for G, **provided** the
connection, lower terms and analytic domain also preserve it.

That provision does real work. The source-permitted primitive complex
K-unitary connection category contains `iI`: it is K-skew, but
`J(iI)=-iJ`. With a nonzero real Clifford principal part, adding such a
connection term does not preserve a single commuting/anticommuting J law.
Consequently general complex K-unitarity does not imply the needed real or
quaternionic connection reduction. The native domain/end and physical weak
selection are additional unproved premises. In a positive Euclidean transfer
J's grading relation changes; do not import the Lorentzian exchange law to
explain away the nonzero closed comparison.

### Stronger consequence: a balancing symmetry inherited by q kills observed index too

If a domain-compatible grade-exchanging balancing symmetry preserves the
hidden complex and descends through q **with adjoint-compatible selfadjoint
realizations on all three complexes**, its restrictions pair hidden and
observed kernels with their adjoint kernels as well. One may instead directly
prove these kernel–cokernel identifications. Thus total=hidden=observed=0. Equivalently,
total0 and hidden0 in the exact sequence imply observed0.

For the real Clifford contraction, J commutes with q and preserves `ker Γ_N`.
So a fully J-compatible operator/domain/observation package cannot produce a
nonzero observed chiral index merely by taking this quotient. A nonzero
observed index requires a failure of symmetry inheritance at the hidden,
observed-domain, or physical-selection stage, while total balance still has
its own justification. Source low-curvature decoupling may motivate testing
such a split; no dynamics or index change is inferred from the claim itself.

## Matrix and packet disposition

X-P1-P2-P3 receives the same-grading requirement, the closed-comparison table,
and the symmetry-descent condition. No P3 row is retyped, no cell becomes
empty/decided_for_C, and no source/ledger/canon verdict moves. The exact failed
routes are named above; absence of a physical weak projector is an open
hypothesis rather than a manufactured falsification. The general conditional
candidate survives with a sharply identified burden.

Item1step2 is complete at internal T2 after specialist review. Next ready step
is packet step3, the finite exact-sequence Lean formalization. The small Lean
corollary here is reusable input, not a claim that that larger step is done.

## Evidence and review

- Existing [Nov11 actual symbol and grading calculation](native-rs-moving-section-index-2026-11-11.md), §§4–6 and coherent connection repair.
- Existing [Fredholm additivity](p1-p2-domain-index-2026-11-11.md), §3 and weak-current countercontrol.
- [Exact controls](../../tests/program-focus/zero_total_grading_probe.py) and [structured result](../../lab/process/zero-total-grading-premise.json).
- [Lean conditional kernel](../../Lean/GUFormalization/ObservedHiddenPremise.lean), compiled with repository-pinned Lean4.32.0-rc1; no sorry, analytic hypotheses assumed.
- [Independent internal review](../../lab/process/hostile-reviews/2026-11-20-zero-total-grading-review.md). Internal acceptance is not external certification.
