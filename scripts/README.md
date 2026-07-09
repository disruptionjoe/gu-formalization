# scripts

This folder holds repository tooling for contributors and scheduled local checks. These scripts
support reproducibility and review; they do not validate research claims by themselves.

## Live tools

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
