---
title: "H6 Prior-Art Verification"
date: 2026-07-23
status: complete
scope: LNF hardening campaign, prior-art and novelty-delta lane
source_policy: primary papers and official publisher records only for technical claims
---

# H6 Prior-Art Verification — 2026-07-23

## Scope and method

This review verifies the LNF manuscript’s load-bearing prior-art claims against
primary papers and official publisher records. Search-engine results were used
only for discovery; every technical statement in the resulting delta is tied
to an author paper, official arXiv record/PDF, or publisher record.

The canonical LNF manuscript and embedded bibliography were read before the
search. No manuscript, `.tex`, queue, staging-note, reviewer, code, or other
agent-owned file was edited in this lane.

The review distinguishes six layers:

- L0: stable topology, framing, and characteristic-class normalization;
- L1: algebraic carrier or family representation;
- L2: 4d boundary/spectrum and anomaly constraints;
- L3: full higher-dimensional spacetime, bulk, compactification, or TQFT;
- L4: the delimited LNF Clifford–Rarita–Schwinger sector interior; and
- L5: the true GU \(Y^{14}\) source/action and an integer index.

This distinction prevents boundary anomaly results, bulk constructions,
indefinite carrier structure, and a still-unbuilt integer index from being
collapsed into one claim.

## Discovery queries recorded

The following focused queries were run on 2026-07-23:

| Query group | Exact query |
|---|---|
| primary decomposition | `site:arxiv.org "2-primary" "3-primary" fermion generations` |
| carrier precedent | `site:arxiv.org Clifford "Rarita-Schwinger" "generation" fermion families` |
| Krein/carrier precedent | `site:arxiv.org Krein "generation" "Rarita-Schwinger"` |
| bordism/family arithmetic | `site:arxiv.org "family puzzle" "Z/24" "Z/8" "Z/3"` |
| inverse terminology | `site:arxiv.org "arithmetically blind" generation` |
| alternate primary terminology | `site:arxiv.org "two-primary" "generation count"` |
| family-number terminology | `site:arxiv.org "2-primary" "family number"` |
| RS terminology | `site:arxiv.org "Rarita-Schwinger" "fermion generations"` |
| obstruction terminology | `site:arxiv.org fermion generation two-primary obstruction` |
| module terminology | `site:arxiv.org family number Rarita-Schwinger Clifford module` |
| stable-homotopy terminology | `site:arxiv.org stable homotopy generation number bordism 3-primary` |
| Krein terminology | `site:arxiv.org Krein space fermion family generation number` |

Additional title/identifier searches located official records for Adams’s
original paper and correction, McLaughlin, Sati–Shim, Furey–Hughes, and the
Dai–Freed erratum.

No returned primary paper matched the full conjunction “explicit
Clifford–Rarita–Schwinger carrier + scoped 2-primary sector-interior no-go +
inverse blindness to a separate 3-primary carrier.” This is only a bounded
negative search result; it is not proof that no such work exists.

## Named-paper verification

| Source checked | Primary/official records | Full-text point verified | Bibliography/claim status |
|---|---|---|---|
| Juven Wang (2023) | [arXiv:2312.14928](https://arxiv.org/abs/2312.14928) and author PDF, v1 submitted 2023-12-22 | The paper gives a positive multiple-of-three argument using 4d-to-2d reduction, \(c_-=24\), framed/string-bordism data, the displayed \(24/8=3\), and a separate \(\mathbb Z/3\) datum. It does not state LNF’s carrier-specific inverse no-go. | Identifier, title, author, and year in the LNF bibliography are verified. Do not claim novelty for \(\mathbb Z/24\), \(24/8=3\), or positive extraction of a 3-primary factor. |
| Wan–Wang–Yau (2026) | [arXiv:2605.26202](https://arxiv.org/abs/2605.26202) and author PDF, v2 revised 2026-07-21 | The group-cohomology \(H^5(\mathbb Z_n,U(1))\) part can be canceled by an anomalous 4d \(\mathbb Z_n\) TQFT; the beyond-cohomology \(A_{\mathbb Z_n}p_1\) part has the stated finite-extension obstruction with special \(n=2,3\) behavior. Version 2 explicitly separates 2- and 3-primary parts and uses CRT. Its minimal \(N=N_c=N_f=3\) result also invokes the generalized SM without sterile \(\nu_R\), minimal cyclic extensions, oddness/Witten anomaly, color-center matching, and fermionic baryons. | Identifier, title, authors, and year are verified. The current prose is too compressed: the \(n=2,3\) exception alone does not “isolate three families” without the paper’s additional assumptions. WWY v2 also defeats novelty for the bare 2/3-primary split. |
| García-Etxebarria–Montero | [JHEP 08 (2019) 003](https://link.springer.com/article/10.1007/JHEP08%282019%29003), [arXiv:1808.00009](https://arxiv.org/abs/1808.00009) | The paper finds the analyzed SM, \(SU(5)\), and \(\mathrm{Spin}(10)\) spectra anomaly-free. With added baryon-triality \(\mathbb Z_3\), it finds a \(\mathbb Z_9\) anomaly canceled only when \(N_{\mathrm{gen}}\in3\mathbb Z\), with explicit UV-data caveats. | Current journal and arXiv metadata are verified. Keep the baryon-triality assumption attached; do not paraphrase this as the plain SM forcing three. |
| Dobrescu–Poppitz | [Phys. Rev. Lett. 87, 031801](https://doi.org/10.1103/PhysRevLett.87.031801), [arXiv:hep-ph/0102010](https://arxiv.org/abs/hep-ph/0102010) | For the stated 6d construction and chirality assignment, the \(SU(2)\) global anomaly requires a multiple of three generations. “Exactly three” uses further phenomenological/perturbative reasoning, and alternate chirality assignments weaken the selection. | Current journal and arXiv metadata are verified. Describe the theorem as conditional and multiple-of-three, not as an assumption-free exact derivation. |
| Kaplan–Sun | [Phys. Rev. Lett. 108, 181807](https://doi.org/10.1103/PhysRevLett.108.181807), [arXiv:1112.0302](https://arxiv.org/abs/1112.0302) | The 5d topological-insulator construction protects multiple surface modes through momentum-space topology. In the displayed three-mode case, the paper expressly chooses parameters to create three roots; it does not derive why nature selects three. | Current journal and arXiv metadata are verified. Characterize the result as protection of a selected multiplicity, not topological selection of the number three. |

## Directly load-bearing nearby work

| Source checked | Primary/official records | Relevance and verified limit | Bibliography action |
|---|---|---|---|
| Evans–Ibe–Kehayias–Yanagida | [Phys. Rev. Lett. 109, 181801](https://doi.org/10.1103/PhysRevLett.109.181801), [arXiv:1111.2481](https://arxiv.org/abs/1111.2481) | Positive three-generation result in specified supersymmetric GUT/discrete-\(R\) settings; product-group cases permit more possibilities. This is L2 model prior art, not a universal count theorem. | Current metadata verified; no correction required. |
| Furey–Hughes | [arXiv:2409.17948](https://arxiv.org/abs/2409.17948), [published DOI](https://doi.org/10.1016/j.physletb.2025.139473) | Algebraic three-generation construction from triality representations; distinct from the LNF carrier/no-go but prior art for algebraic family structure. | Update the arXiv-only entry to include *Physics Letters B* (2025), article 139473, DOI `10.1016/j.physletb.2025.139473`. |
| Besnard–Brouder | [Phys. Rev. D 103, 035003](https://doi.org/10.1103/PhysRevD.103.035003), [arXiv:2010.04960](https://arxiv.org/abs/2010.04960) | Lorentzian spectral Standard Model on a pre-Krein space with an explicit \(N\)-generation factor and \(N\times N\) mass matrices. It assumes \(N\); it does not derive the family count. | The manuscript cites raw `arXiv:2010.04960` in prose but has no bibliography item. Add a complete entry. |
| Adams | [Topology 5 (1966) 21–71](https://doi.org/10.1016/0040-9383(66)90004-8), [correction, Topology 7 (1968) 331](https://doi.org/10.1016/0040-9383(68)90010-4) | Foundational image-of-\(J\)/\(e\)-invariant input. It does not establish any family-number interpretation. | Existing original-paper metadata are correct; append the published correction and its DOI. |
| Kirby–Melvin | [arXiv:math/9903056](https://arxiv.org/abs/math/9903056) | The stable framing normalization sends the relevant \(SO(3)\) generator to twice the stable generator. This is a framing input, not family-number novelty. | Existing metadata verified; no correction required. |
| McLaughlin | [official Pacific Journal PDF](https://msp.org/pjm/1992/155-1/pjm-v155-n1-p08-s.pdf) | Primary source for the string/characteristic-class normalization used in the reconstruction. | Existing metadata verified; no correction required. |
| Sati–Shim | [arXiv:1504.02088](https://arxiv.org/abs/1504.02088), [published DOI](https://doi.org/10.1016/j.geomphys.2019.02.002) | Restates and develops the \(\tfrac12p_1\) string-class normalization for indefinite Lie groups. | Update the arXiv-only entry to *Journal of Geometry and Physics* **140** (2019) 246–264, DOI `10.1016/j.geomphys.2019.02.002`. |
| Dai–Freed | [arXiv:hep-th/9405012](https://arxiv.org/abs/hep-th/9405012), [publisher DOI](https://doi.org/10.1063/1.530747) | Foundational determinant-line/\(\eta\)-invariant bridge; not a generation-count result by itself. | Append the published erratum: *J. Math. Phys.* **42** (2001) 2343–2344. |

## Required claim correction: torsion order

This issue is arithmetic rather than bibliographic, but it is load-bearing and
must be corrected in any later authorized manuscript edit.

The reconstructed class is written as \(2\in\mathbb Z/24\), with
\(e_{\mathbb R}=1/12\in\mathbb Q/\mathbb Z\). Both have order \(12\), not order
\(3\):

\[
\operatorname{ord}_{\mathbb Z/24}(2)=\frac{24}{\gcd(24,2)}=12,\qquad
\operatorname{ord}_{\mathbb Q/\mathbb Z}(1/12)=12.
\]

Under CRT,
\[
2\longmapsto(2\bmod 8,\;2\bmod3).
\]
Only the projected 3-primary component \((0,2)\)—represented by
\(8\in\mathbb Z/24\)—has order \(3\). The defensible statement is therefore:
the class has a nonzero 3-primary torsion component that supplies a candidate
\(\mathbb Z/3\) carrier. It is not itself an order-three class and it is not an
integer index.

No homomorphism can turn this torsion datum into a nonzero integer count:
\(\operatorname{Hom}(\mathbb Z/3,\mathbb Z)=0\). A count of three would require
an integer-by-construction relative, equivariant, rank, or family-index home at
L5.

## Bibliography and wording corrections queued

No corrections were applied to the manuscript in this lane. A later authorized
edit should:

1. add a full Besnard–Brouder bibliography item for the currently unkeyed
   `arXiv:2010.04960` prose citation;
2. update the Wan–Wang–Yau discussion to v2 (2026-07-21), acknowledge its
   explicit 2/3-primary and CRT treatment, and state all assumptions behind its
   minimal \(N=N_c=N_f=3\) conclusion;
3. correct every description of \(2\in\mathbb Z/24\) or \(e_{\mathbb R}=1/12\)
   as “order 3,” reserving order three for the projected 3-primary component;
4. append Adams’s 1968 correction;
5. add the published Furey–Hughes metadata and DOI;
6. add the published Sati–Shim metadata and DOI;
7. append the Dai–Freed 2001 erratum;
8. keep the baryon-triality assumption explicit for
   García-Etxebarria–Montero;
9. describe Dobrescu–Poppitz as a conditional multiple-of-three theorem, with
   exact three requiring additional reasoning; and
10. describe Kaplan–Sun as topological protection of a parameter-selected
    multiplicity, not topological prediction of three.

The core bibliographic identifiers for Wang, Wan–Wang–Yau,
García-Etxebarria–Montero, Dobrescu–Poppitz, Kaplan–Sun, and
Evans–Ibe–Kehayias–Yanagida were verified as correct.

## Novelty assessment

The bare statements

- “topology can constrain family number,”
- “\(\pi_3^S\cong\mathbb Z/24\),”
- “\(24=8\cdot3\),”
- “2-primary and 3-primary parts can be separated,” and
- “an indefinite/Krein formulation can contain a generation space”

are prior art or standard input.

The only defensible candidate delta located by this review is the specific LNF
assembly: its reconstructed cross-chirality Clifford–Rarita–Schwinger carrier,
the delimited L4 2-primary no-go/selector result, and the inverse conclusion
that this L4 result cannot determine the carrier’s separate 3-primary torsion
projection.

Even that delta remains exposed to the following risks:

- the inverse step is an elementary consequence of primary decomposition once
  the L4 premises are accepted;
- terminology differences or non-arXiv work may conceal a closer precedent;
- the GU-specific carrier identification is reconstruction-grade;
- the unrestricted analytic/function-space no-go remains open;
- the true-\(Y^{14}\) source action and integer index are not built; and
- the relevant computations have no independent external replication.

## H6 disposition

H6 is complete at the scholarship-artifact level:

- exact source identifiers and official links are recorded;
- the named and nearby primary literature is compared by layer;
- the candidate novelty delta is narrowed;
- bibliography and claim corrections are queued without editing protected
  files; and
- unresolved novelty risks are explicit.

This completion does not change the manuscript’s theorem grades. The result
remains **located, not forced**.
