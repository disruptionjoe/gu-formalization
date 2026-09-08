# scripts

This folder holds repository tooling for contributors and scheduled local checks. These scripts
support reproducibility and review; they do not validate research claims by themselves.

## Live tools

- [`research_context.py`](research_context.py) - read-only entry view from
  `CURRENT-STATE.yaml` and the first complete level-two section of
  `VERIFICATION.md`, including grades and reproduction commands. Run
  `python3 scripts/research_context.py` from the repository root with
  `requirements.txt` installed (the reader uses PyYAML). It omits the accumulated
  summary and all but the lead of `next_condition`, explicitly labeled partial.
  It writes no files, keeps no cache, and does not select work or certify
  freshness. Read the full relevant state, remaining verification sections,
  source-routing rules, and exact artifacts before reusing a claim. The section
  is shown in file order; the reader does not infer which result is newest or
  most important.
- [`reproduce_all.py`](reproduce_all.py) - one-step Python certificate runner. Quick mode runs
  the tracked `tests/` certificates; full mode also includes paper candidate and draft
  certificates. Use `--tracked-only` for local or scheduled runs that should ignore unrelated
  untracked certificate work, `--list` to inspect the sweep without running it, and `-k SUBSTR`
  for a focused subset.

## Boundaries

- The public reproduction guide is [`../REPRODUCE.md`](../REPRODUCE.md).
- The computational certificate map is [`../tests/README.md`](../tests/README.md).
- Process gates, including the reproduction harness scope check, live under
  [`../process_gates/`](../process_gates/).
- A green script run means the selected certificates reproduced on the local machine. It does
  not change claim status, canon verdicts, public posture, or research truth.
