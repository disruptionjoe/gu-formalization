---
title: "Witten and Bar-Natan–Witten: the precise positivity and unitarity claims"
status: active_research
doc_type: primary_source_audit
created: "2026-10-08"
target_claim: NONE-NOT-A-KILL
bears_on: SC-META-53
canon_verdict_change: none
receipt: lab/sources/witten-noncompact-quantization-source-audit-2026-10-08.json
---

# Source audit

The inspected Witten report distinguishes an indefinite ordinary Yang–Mills
kinetic form from complex Chern–Simons quantization. Its explicit theorem
concerns a projectively flat connection over Teichmüller space, preserving a
positive Hilbert pairing when `s` is real. Its separate zero-Hamiltonian
statement belongs to constrained bulk Chern–Simons theory with closed spatial
surface. These results challenge a claim based on complexification alone;
they do not answer an objection with an additional propagating Yang–Mills
action premise, and they do not construct GU physical dynamics.

This is a source reinspection, not a new mathematical result or a change to
the GU positivity verdict. The custody receipt records the distinction between
the inspected reports and the journal publications.

## Witten: carrier, action and result

The primary is Edward Witten, *Quantization of Chern-Simons Gauge Theory with
Complex Gauge Group*, IASSNS-HEP-89/65, December 1989,
[44-page report](https://lib-extopc.kek.jp/preprints/PDF/1990/9009/9009085.pdf).
Publication metadata was checked against the
[publisher record](https://doi.org/10.1007/BF02099116): *Communications in
Mathematical Physics* **137** (1991), 29–66. The published typesetting was
not recovered in this audit: the publisher PDF endpoint returned subscription
HTML, and Project Euclid returned a security page. **All substantive page
locators below are report pages, also equal to this local PDF's page numbers.**
No journal-page conversion is inferred.

| Inspected report locator | Source-confirmed content and claim ceiling |
| --- | --- |
| Introduction, p2, (1.1)–(1.3) | The conventional Yang–Mills action uses an invariant nondegenerate quadratic form. When that form is indefinite, the real bosonic canonical theory can retain unitarity while its energy is unbounded below. The statement is action-specific. The elementary canonical-commutator argument is not a theorem that every real bosonic Lagrangian defines an interacting quantum field theory. |
| Introduction, p3 | Chern–Simons is presented as unitary with vanishing Hamiltonian, including noncompact groups. The gravitational example immediately specifies compact spatial slice. The construction developed later is for a complexification of compact `G`, not a completed quantization for every noncompact real group. |
| §2, pp5–7, (2.1)–(2.3) | The action contains both the complex connection and its conjugate, with `t=k+is` and the second coupling `k-is`. Integral `k` is imposed with the stated trace normalization; real `s` makes the two couplings conjugate and the Lorentzian action real. A further Euclidean reality interpretation involves imaginary `s` and an involution under orientation reversal. |
| §3, pp8–9, (3.1)–(3.2) | Spacetime is `Σ × R`, with `Σ` oriented and **closed**. Flatness is the Gauss constraint. The physical phase space is the moduli of flat complex-group connections. The approach formally quantizes all connections, chooses a polarization, and imposes constraints. |
| §3.4, pp16–17, (3.18)–(3.19) | Constrained wavefunctions descend through the dense stable locus to the moduli `M_J` of stable holomorphic bundles. Narasimhan–Seshadri identifies this with compact-group flat moduli `M`. The physical Hilbert space is represented by square-integrable sections of `L^k` on `M`; it is not limited to holomorphic sections. This explains its infinite dimension. |
| §4, pp18–21, (4.3)–(4.11) | The connection descends to finite-dimensional `M × T`, with `T` Teichmüller space. The provisional formulas involve formal reduction and regularization. Corrections are selected by requiring projective flatness and assuming anomalies change coefficients without changing the types of terms. The source explicitly distinguishes this heuristic route from the precise theorem for the finally defined connection. |
| §4, pp21–22, theorem following (4.11) | For the connection **defined by (4.9)–(4.10)** on the Hilbert bundle over `T`, the curvature is central and of type `(1,1)`, and the connection is unitary for real `s`. Its proof imports differential-geometric and determinant-curvature identities. This is the strongest precise named theorem relevant here. |
| §4.1, pp22–23, (4.12)–(4.16) | The preserved pairing is `∫_M H(χ,ψ) dμ`, with the Hermitian line-bundle metric and `H` the regularized Laplacian determinant. Multiplication by `H^(1/2)` converts it into the ordinary positive `L²` pairing and conjugates the connection accordingly. The adjoint calculation concerns the connection's differential operators. |

The displayed connection contains `1/t` and `1/(k-is)`. For the real-`s`
branch both couplings must be nonzero, so `(k,s)=(0,0)` is excluded from these
formulas. For example, `k=1`, `s=1` avoids this degeneracy. The theorem is
projective: flat identification is available up to a central factor, rather
than as an unqualified strictly flat bundle. Preserved transport over `T`
identifies polarizations as complex structure varies; `T` is **not physical
time**. Physical bulk time evolution in the closed constrained topological
setting is separately trivial, with `H_phys=0`. Its energy is then bounded
below, but this is not stability of propagating local Yang–Mills modes.

Witten calls the final connection analysis rigorous after its definition. It
is legitimate to credit that theorem. It is stronger than the audited source
to turn it into a complete constructive quantum field theory theorem,
including all singular strata, operator closures, boundary dynamics and a
nonperturbative measure: the theorem as stated does not enumerate or prove
those additional claims.

## Branch and boundary qualifications

For nonreal `s`, the real-`s` pairing need not be preserved as a positive
Hermitian form on one Hilbert space. In §4.1, p23, (4.17)–(4.18), the proposed
alternative first pairs spaces at conjugate parameters and needs an
additional isomorphism. Existence of that pairing alone is not positivity.
The imaginary-`s` positive construction is explicit only in genus one
(§5.3, pp33–34). For `k≠0`, (5.18) gives the operator `u^N`, where
`u=(is-k)/(is+k)` and `N` has nonnegative integer spectrum. The displayed
positive bounded range is `0<u<1`. A hand insertion of `(-1)^N` can repair
the range `-1<u<0` in genus one, and the author expressly doubts its
extension to higher genus. For `k=0`, (5.13) instead uses `r=1/(2is)`;
the zero-coupling singularity remains. The general real-`s` branch suffices
for the scoped comparison; imaginary `s` should not be cited as an
unqualified all-genus positive theorem.

The disk discussion in §6.3, pp40–42, changes the gauge quotient: gauge
transformations are fixed to the identity on the boundary. It leads to loop
group and current-algebra data and is explicitly partly formal. Thus the
closed-surface zero-Hamiltonian claim supplies no theorem that arbitrary
boundary or asymptotic Hamiltonians vanish. Likewise, §6.1, pp37–39,
distinguishes the `SL(2,C)` gauge Hilbert space from the proposed larger
gravitational Hilbert space; the gravity identification should not be
treated as a fully settled consequence of the gauge quantization.

## Bar-Natan–Witten: what the compact reduction changes

The primary is Dror Bar-Natan and Edward Witten, *Perturbative Expansion of
Chern-Simons Theory with Non-Compact Gauge Group*, IASSNS-HEP-91/4,
January 1991,
[29-page author report](https://www.math.toronto.edu/~drorbn/papers/NonCompact/NonCompact.pdf),
published in *Communications in Mathematical Physics* **141** (1991),
423–440, DOI [10.1007/BF02101513](https://doi.org/10.1007/BF02101513).
The inspected file is a report, not the 18-page journal typesetting.

The scope is perturbative pure Chern–Simons theory with semisimple gauge
group. The working background is an **isolated irreducible flat connection**,
chosen to avoid collective coordinates and zero modes (§2, pp5–6). The
explicit calculation is leading/one-loop; its introductory discussion says
that a Hamiltonian treatment for other noncompact real groups was not then
adequately understood (p4).

Section 3, pp11–13, explains the failure of the naive gauge: operators
self-adjoint in an indefinite form can have null eigenvectors with complex
eigenvalues, and introducing a positive metric alone does not make those
unchanged operators self-adjoint. Section 4, pp14–16, replaces the gauge
fixing and kinetic operators together. A maximal-compact reduction defines
an involution **`T`**, with `+1` on the compact algebra and `-1` on its
complement. The modified star is `*T`, and (4.4) gives the positive form
`-∫ Tr(ū ∧ *T v)`. The new bosonic and ghost operators, and the resulting
one-loop determinant and eta invariant, belong to this changed gauge
fixing. In this paper `J` already denotes a distinct form-grading operator;
calling the compact-reduction involution `J` without declaring a renaming
obscures the formulas.

The reduction is auxiliary. Equations (4.37)–(4.39), pp22–23, add a local
counterterm to remove its dependence at one loop; (4.11), p18, handles metric
dependence up to the framing anomaly. This is evidence for a specific
perturbative Chern–Simons repair, not a physical positive-energy theorem for
a general noncompact gauge action or GU's first-order/residual-square
actions.

## Consequence for the proposed rebuttal

Nguyen–Polya §3.1, p6, writes an inference from complexifying connections and
the group to nonunitarity or energy unbounded in both directions. Witten
does not establish that inference without an action premise. His own
closed-surface real-`s` complex Chern–Simons construction is the relevant
source-backed exception, with the precise qualifications above. A charitable
reading motivated by the response's Yang–Mills-recovery claim (§3.4, p8)
instead concerns an indefinite kinetic form in a surviving propagating
Yang–Mills sector. The Chern–Simons exception does not remove that
conditional obstruction.

Accordingly, the defensible rebuttal identifies the missing action and
physical-reduction premises and credits Witten's actual construction. It
does not identify his parameter-space theorem with physical-time evolution,
claim complete rigorous quantization, or transfer the maximal-compact
gauge-fixing pairing to GU. Whether GU satisfies the Yang–Mills premises or
constructs a positive physical alternative remains a separate research
question under SC-META-53.
