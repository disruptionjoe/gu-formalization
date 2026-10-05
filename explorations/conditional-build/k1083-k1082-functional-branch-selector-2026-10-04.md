---
title: "K1083 functional branch selector"
status: active_research
doc_type: conditional_functional_normal_mode_selector
created: 2026-10-04
claim_ceiling: exact translation-invariant flat-torus branch theorem; no source coefficient or dimensional ruler
manifest: lab/process/k1083-k1082-functional-branch-selector.json
probe: tests/channel-swings/k1083_k1082_functional_branch_selector_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1083 functional branch selector

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> spectral selector, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_SELECTOR`.

```gu-typed-objects
result: commuting constant internal blocks yield one Fourier/internal product basis and affine squared-frequency branches
carrier: H2(T3;R^r) inside L2(T3;R^r) LAYER=observed CHIRALITY=N/A
pairing: A-normalized positive kinetic form ON=candidate_action
real_structure: real fields with conjugate Fourier modes
grading: spatial momentum and joint internal eigenspaces
action_owner: repository-construction -- K1036 scalar horn is certified but not source selected
target: K1077-K1078 functional transfer MAP-TYPE=evaluation
```

For constant `A>0`, `B`, and `C`, one spatial-mode-independent internal basis
exists exactly when `[A^-1B,A^-1C]=0`. In that basis,

```text
omega_j(k)^2 = b_j |k|^2+c_j.
```

The fixtures `(b,c)=(2,6),(3,15)` recover ratios `u=3,5` from modes
`|k|^2=0,1,2`. The K1036 specialization `B=I,C=m^2I` therefore has
`u=m^2` on the common `H2` domain. This is action compatibility and coefficient
reading inside a supplied candidate, not source selection. An absolute mass
still requires an independently owned spatial ruler, and repeated joint pairs
select only a subspace.

The producer passes `9/9`; the hostile probe rejects `10/10` commutator,
branch, recovery, ruler, degeneracy and ownership mutations.
