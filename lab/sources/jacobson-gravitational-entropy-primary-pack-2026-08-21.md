---
title: "Primary pack: Jacobson gravitational entropy, causal boundaries, and Lorentzian path integrals (2023--2025)"
status: active_research
doc_type: primary_source_pack
created: "2026-08-21"
source_grade: primary
directed_by: "Joe direct chat, 2026-08-21"
canon_verdict_change: none
---

# Jacobson gravitational entropy and Lorentzian path-integral primary pack

## Why this pack exists

The repository previously used Jacobson's 1995 equation-of-state argument and
the Eling--Guedens--Jacobson non-equilibrium extension, but did not recognize
the five newer papers below by title, identifier, or author combination. This
pack closes that source gap.

The papers are relevant because they ask how a gravitational state count can
remain informative when the underlying microphysics is unknown, and because
they make constraint projection, system boundaries, ensemble definition,
complex contours, and fluctuation convergence prior to physical
interpretation. They do not contain a Geometric Unity construction or select
a B5 domain.

## Verified bibliography

1. Batoul Banihashemi and Ted Jacobson, "The enigmatic gravitational
   partition function," *General Relativity and Gravitation* **57**, 43
   (2025), [arXiv:2411.00267v3](https://arxiv.org/abs/2411.00267),
   DOI [`10.1007/s10714-024-03347-0`](https://doi.org/10.1007/s10714-024-03347-0).
2. Batoul Banihashemi and Ted Jacobson, "On the lapse contour in the
   gravitational path integral," *Physical Review D* **111**, 066014 (2025),
   [arXiv:2405.10307v3](https://arxiv.org/abs/2405.10307),
   DOI [`10.1103/PhysRevD.111.066014`](https://doi.org/10.1103/PhysRevD.111.066014).
3. Bianca Dittrich, Ted Jacobson, and Jose Padua-Arguelles, "De Sitter
   horizon entropy from a simplicial Lorentzian path integral," *Physical
   Review D* **110**, 046006 (2024),
   [arXiv:2403.02119v2](https://arxiv.org/abs/2403.02119),
   DOI [`10.1103/PhysRevD.110.046006`](https://doi.org/10.1103/PhysRevD.110.046006).
4. Ted Jacobson and Manus R. Visser, "Entropy of causal diamond ensembles,"
   *SciPost Physics* **15**, 023 (2023),
   [arXiv:2212.10608v4](https://arxiv.org/abs/2212.10608),
   DOI [`10.21468/SciPostPhys.15.1.023`](https://doi.org/10.21468/SciPostPhys.15.1.023).
5. Batoul Banihashemi, Ted Jacobson, Andrew Svesko, and Manus Visser, "The
   minus sign in the first law of de Sitter horizons," *JHEP* **01** (2023)
   054, [arXiv:2208.11706v4](https://arxiv.org/abs/2208.11706),
   DOI [`10.1007/JHEP01(2023)054`](https://doi.org/10.1007/JHEP01(2023)054).

## Claim and limitation matrix

| source | primary-source result relevant here | explicit ceiling for this repository |
|---|---|---|
| `2411.00267` | In the de Sitter case the formal partition function is interpreted as `Tr I`, the dimension of a ball-of-space Hilbert space. Low-energy `G` can summarize inaccessible microphysics in the leading entropy. Observer-accessible states may include would-be gauge edge modes made physical by the inaccessible region. The authors work backward toward reduced-phase-space foundations. | The paper calls the interpretation formal and foundationally shaky. Its direct phase-space saddle treatment reaches an impasse, and it remains unclear whether the lapse prescription fixes the imaginary action sign from first principles. It does not show that GU's unknown source action is encoded by `G`, or that the B5 marked class is an edge mode. |
| `2405.10307` | Constraint projection requires both lapse signs. When momentum is integrated before lapse, the contour must pass below zero; this also gives convergent matter/gravity fluctuation Gaussians and the usual short-distance vacuum orientation. | The result presupposes a gravitational Hamiltonian constraint, lapse, phase space, and gauge fixing. The relevant gauge is not globally available, different observables may require different contours, and a nonperturbative covariant gravitational path integral remains unresolved. B5 has no typed gravitational lapse at present. |
| `2403.02119` | A finite `2+1` simplicial minisuperspace model demonstrates both-sign constraint projection, a convergence-selected complex contour, entropy enhancement, and cancellation of otherwise divergent large-area contributions. | The model has two edge-length variables, omits inhomogeneous fluctuations and microscopic entropy degrees of freedom, and retains discretization artifacts. It is neither a continuum theorem nor a `(9,5)` Rarita--Schwinger/BV result. |
| `2212.10608` | An explicit York boundary with fixed induced geometry and temperature defines a gravitational causal-diamond ensemble. In zero-cosmological-constant Einstein gravity the near-horizon entropy arises through a high-temperature approximate saddle. | The artificial boundary defines a different physical system from an unbounded causal diamond. There is no exact zero-cosmological-constant horizon saddle, and the Dirichlet boundary problem may be unstable or ill posed. The paper warns against mistaking an imposed boundary for a physically selected one. |
| `2208.11706` | The de Sitter first-law minus sign is resolved after distinguishing matter Killing energy from total Brown--York internal energy in a boundary-defined ensemble. In the zero-boundary limit total energy variation vanishes; generalized entropy is stationary in global equilibrium. | This is a semiclassical de Sitter/Einstein and stationary or quasistationary result. The thermodynamic sign is not a Krein norm sign, and generalized-entropy stationarity depends on the stated equilibrium and boundary construction. |

## What the five papers establish as a research method

At their shared, honest grade they support this ordering:

```text
define the physical system and boundary
  -> impose constraints and remove gauge redundancy
  -> identify the reduced state-space trace or ensemble
  -> derive any lapse/contour prescription
  -> require fluctuation and short-distance vacuum admissibility
  -> only then interpret entropy, signs, or state counts
```

This ordering is a `METHOD_PORT`, not an `EXACT_PORT`, for B5. It agrees with
the repository's existing demand that physical positivity follow a complete
constraint/BV--BFV reduction rather than being imposed on the unreduced Krein
carrier.

## Relation to existing repository work

- `explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md` owns the
  older Jacobson 1995 equation-of-state comparison and the exact
  Einstein-versus-`R^2` mismatch.
- `explorations/intake-verlinde-jacobson-entropic-2026-07-20.md` is an older
  intake centered on Jacobson 1995 and labels all transfers as imported
  shape evidence.
- `lab/sources/verlinde-jacobson-grok-source-pack-2026-07-20.md` is explicitly
  untrusted third-party summary material; this primary pack supersedes it only
  for claims about the five newer papers.
- W180/W203/W229/W230/W236 use a generic Sakharov/Jacobson induced-gravity
  stance. They do not own the newer constraint, contour, causal-boundary, or
  ensemble results.

## Transfer firewall

Do not infer any of the following from this pack:

- that the strict B5 witness is a horizon edge mode;
- that the B5 half-cylinder is a causal diamond or York ensemble;
- that a single gravitational lapse exists in signature `(9,5)`;
- that path-integral convergence is probability positivity;
- that a thermodynamic entropy sign is a Krein/Hilbert norm sign;
- that reproducing Bekenstein--Hawking entropy is a GU prediction;
- that unknown microscopic/source data are always compressed into one
  effective constant;
- or that any B5 extension is physically preferred.

## Native follow-up

The typed follow-up is recorded in
`explorations/jacobson-b5-entropy-boundary-transfer-council-2026-08-21.md`.
It feeds the already-live `B5-PHYSICAL-PAIRING-OWNER-PACKET`; it does not
reopen the closed generic positivity search.
