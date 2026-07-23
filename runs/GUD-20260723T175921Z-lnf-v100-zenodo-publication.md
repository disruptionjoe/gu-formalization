# LNF v1.0.0 Zenodo publication

Status: complete

Run: `GUD-20260723T175921Z-lnf-v100-zenodo-publication`

Formal phase: `stewardship`

Mode: `execute`

Lane: `A`

Authority: Joe direct chat, 2026-07-23. Joe explicitly authorized publication
and confirmed the final irreversible Publish action after the complete Zenodo
draft was presented.

Starting revision: `2db8acbbfdc4e4d9abc56ef463c981d14845f3d1`

Objective: publish the frozen LNF v1.0.0 package on Zenodo, verify the public
record, and reconcile repository publication truth without changing the
immutable deposit files or any scientific claim.

Writable surfaces:

- `papers/candidates/located-not-forced/` release receipts only;
- `papers/published/INDEX.md`;
- publication-facing `README.md`, `NEXT-STEPS.md`, `LANE-STATE.yaml`, and
  `lab/process/research-portfolio.json`;
- this run receipt.

Collision check: all declared repositories were clean and upstream-even; writer
locks were absent; no overlapping active run was found on these publication
receipt surfaces.

## External action receipt

- Venue: Zenodo
- Published: 2026-07-23
- Version: `1.0.0`
- Version DOI: `10.5281/zenodo.21515143`
- Concept DOI: `10.5281/zenodo.21515142`
- Public record: `https://zenodo.org/records/21515143`
- Creator: Joseph Hernandez
- Affiliation: Independent Researcher
- Resource type: Preprint
- License: CC BY 4.0
- Source checkpoint: `020b682d3adf166d2b90017eb18b57be554af83c`
- Frozen release commit: `2db8acbbfdc4e4d9abc56ef463c981d14845f3d1`

The public record was inspected after publication. `main.pdf` is the default
18-page preview. Zenodo exposes both frozen files, the repository URL in both
the software and `is supplemented by` related-work fields, English, the full
keyword set, and Python/Lean software metadata.

Public MD5 values match the local artifacts:

```text
d25972628cb91ca299095c92a3a13278  main.pdf
7ddc66f4b95d35cb90b45f6bcd07f766  located-not-forced-v1.0.0.zip
```

No deposit file was modified after publication. Future file corrections require
a new Zenodo version. Optional external review, arXiv, journal, website, or
distribution work remains separately Joe-directed and does not gate this
publication.
