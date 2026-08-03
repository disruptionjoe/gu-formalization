# Exact computational evidence

This directory contains the two independent executable certificates relied on
by the manuscript:

- `compact_image_obstructions_exact.py` uses SageMath rational quaternions.
- `compact_image_obstructions_properties.py` uses a separate, minimal exact
  integer-quaternion implementation plus deterministic Hypothesis generation.

Neither certificate uses floating point or substitutes for the written proof.
The Python dependency graph is locked in `uv.lock`. Exact commands and expected
outputs are recorded one directory above in `REPRODUCE.md` and `VERIFICATION.md`.
