---
status: CONDITIONALLY_RESOLVED
claim_verdict: CONDITIONALLY_RESOLVED
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K292 — exact disjoint native tube atlas

K284's continuously centered boxes overlap, but their union has a simple
almost-everywhere disjoint native parameterization. Write the ray as
`g_i=b_i t`, take `1 <= t <= 5/4`, and set `h=1/32768`. The start stratum is
the full six-dimensional box at `t=1`. Outside it, define

`t_*(g)=max_i (g_i-h)/b_i`.

At least one coordinate satisfies `g_k=b_k t_*+h`. Assign the point to the
smallest such `k`; all other coordinates have the unique form
`g_j=b_j t_*+eta_j`, `|eta_j|<=h`. Multiple maximizers are lower-dimensional
ties and have native six-volume zero.

The swept-face Jacobian is exactly `b_k`, so the native tube volume is

`(2h)^6 + (1/4)(2h)^5 sum_k b_k`.

The producer serializes all six faces, exact rational Jacobians and volumes,
and the tie convention. The independent probe recomputes every identity and
rejects eight hostile mutations. This closes only the K284 interior tube
geometry; it adds no exterior-domain or action-column claim.
