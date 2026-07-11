"""Nielsen-Ninomiya, its domain-wall escape, and the records-as-rows reading -- one computable object.

THE QUESTION (six-axis L3/L6 lane). Does the records-as-rows / causal-masked-attention structure give a
genuine SHADOW of the Nielsen-Ninomiya lattice-chirality no-go (a real evasion via a smoothing functor),
or does it merely relabel the unit (scope-exit)? The disciplined test needs a concrete object in
N-N's category and a concrete mechanism.

THE TIE TO THE GENERATION-COUNT TERMINUS. The located-not-forced paper's Theorem 2 -- "every linear
Krein-isometric operator conserves the net chiral index at zero" -- is a Nielsen-Ninomiya-shaped
statement: net chirality vanishes on a closed/compact structure. Its escape ("the count is EXTERNAL by
structure, supplied by a boundary / anomaly inflow") is exactly the DOMAIN-WALL FERMION escape from
N-N (Kaplan 1992; Jackiw-Rebbi 1976): a single chiral mode lives on the boundary of an extra dimension
while the bulk stays vectorlike. The records-as-rows reading of that extra dimension is TIME (records
accumulating); the boundary is the AUTOREGRESSIVE FRONTIER (the causal mask's edge, "the present").

THE COMPUTABLE OBJECT. A 2-band Chern-insulator lattice, `h(k) = (sin kx, sin ky, M + cos kx + cos ky)`,
`H(k) = h.sigma`. It makes all three statements one object:
  (1) N-N: on the CLOSED strip (both edges) the net chirality is 0 -- the compact Brillouin torus / the
      closed sample forces left- and right-movers to cancel (fermion doubling).
  (2) Domain-wall escape: a SINGLE edge (a domain wall between a topological and a trivial region)
      carries net chirality = the bulk Chern number = +/-1 -- chirality as a boundary mode.
  (3) Anomaly inflow: (1) and (2) are the same fact -- the two edges carry opposite net chirality, so the
      closed system is net-0 while each boundary is chiral. This IS the paper's "external by structure."

Controls: the trivial phase (|M|>2, Chern 0) has NO chiral edge mode -- so the edge chirality is not an
artifact of having a boundary, it is sourced by the bulk topology. numpy; deterministic (no RNG).

Run: python tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py
"""
from __future__ import annotations

import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- 1D Nielsen-Ninomiya: fermion doubling on the compact Brillouin zone ------------------------

def nn_1d_doubling(n_k: int = 2000) -> tuple[list[float], float, int]:
    """Naive 1D lattice fermion E(k)=sin(k): find its zeros and the chirality (dE/dk sign) at each.

    Returns (chiralities at the zeros, their sum, zero count). Uses a MIDPOINT grid so no sample lands
    exactly on a zero (k=0 or k=+/-pi), and circular sign-change detection (the loop wraps at +/-pi,
    which are the same BZ point). The continuum control E(k)=k has one zero of chirality +1; the lattice
    periodicity forces a second zero of opposite chirality at the BZ edge -> net 0 (fermion doubling).
    """
    ks = -np.pi + (np.arange(n_k) + 0.5) * (2 * np.pi / n_k)  # midpoint grid, endpoints excluded
    e = np.sin(ks)
    zeros_chirality: list[float] = []
    for i in range(n_k):
        j = (i + 1) % n_k  # circular: last -> first wraps across the +/-pi identification
        if (e[i] < 0) != (e[j] < 0):  # a sign change between adjacent samples = a band-touch
            zeros_chirality.append(float(np.sign(e[j] - e[i])))  # +1 right-mover, -1 left-mover
    return zeros_chirality, float(sum(zeros_chirality)), len(zeros_chirality)


# ---- Bulk Chern number (Berg-Luscher solid-angle sum over the BZ) --------------------------------

def h_vec(kx: np.ndarray, ky: np.ndarray, m: float) -> np.ndarray:
    return np.stack([np.sin(kx), np.sin(ky), m + np.cos(kx) + np.cos(ky)], axis=-1)


def bulk_chern(m: float, n: int = 200) -> int:
    """Skyrmion number of the normalized h-field over the BZ torus (robust integer)."""
    ks = np.linspace(-np.pi, np.pi, n, endpoint=False)
    kx, ky = np.meshgrid(ks, ks, indexing="ij")
    h = h_vec(kx, ky, m)
    h = h / np.linalg.norm(h, axis=-1, keepdims=True)
    total = 0.0
    for (i0, i1) in ((slice(None), np.roll(np.arange(n), -1)),):  # noqa: B007
        pass
    # signed solid angle of each plaquette's two triangles
    hr = np.roll(h, -1, axis=0)  # +kx neighbor
    hu = np.roll(h, -1, axis=1)  # +ky neighbor
    hru = np.roll(hr, -1, axis=1)
    for a, b, c in ((h, hr, hru), (h, hru, hu)):
        num = np.einsum("...i,...i->...", a, np.cross(b, c))
        den = 1.0 + np.einsum("...i,...i->...", a, b) + np.einsum("...i,...i->...", b, c) + np.einsum("...i,...i->...", c, a)
        total += np.sum(2.0 * np.arctan2(num, den))
    return int(round(total / (4.0 * np.pi)))


# ---- Chern strip: edge modes and their chirality (the domain-wall escape) ------------------------

def strip_hamiltonian(kx: float, m: float, ny: int) -> np.ndarray:
    """H(kx) for a strip: periodic in x (kx good), OPEN in y (two edges = two domain walls vs vacuum)."""
    dim = 2 * ny
    H = np.zeros((dim, dim), dtype=complex)
    onsite = np.sin(kx) * SX + (m + np.cos(kx)) * SZ  # ky-independent part
    # forward y-hop (H_{y,y+1}) = e^{+iky} coefficient of cos ky*SZ + sin ky*SY = SZ/2 - i SY/2,
    # so that hop*e^{iky}+h.c. reconstructs +cos ky*SZ + sin ky*SY exactly (same model as h_vec).
    hop_y = 0.5 * SZ - 0.5j * SY
    for y in range(ny):
        H[2 * y:2 * y + 2, 2 * y:2 * y + 2] = onsite
        if y + 1 < ny:
            H[2 * y:2 * y + 2, 2 * (y + 1):2 * (y + 1) + 2] = hop_y
            H[2 * (y + 1):2 * (y + 1) + 2, 2 * y:2 * y + 2] = hop_y.conj().T
    return H


def edge_chirality(m: float, ny: int = 40, n_k: int = 401) -> dict:
    """Count net chiral edge crossings on the TOP edge and BOTTOM edge across the bulk gap.

    A chiral edge mode crosses zero energy with a definite velocity sign, localized on one edge. Net
    chirality of an edge = sum of sign(velocity) over its mid-gap crossings. Returns per-edge nets and
    the closed-strip total.
    """
    ks = -np.pi + (np.arange(n_k) + 0.5) * (2 * np.pi / n_k)  # midpoint grid: no sample on a crossing
    top_cross = 0.0
    bot_cross = 0.0
    top_q = slice(2 * (ny - ny // 4), 2 * ny)   # top quarter of the strip
    bot_q = slice(0, 2 * (ny // 4))             # bottom quarter
    prev_w = None
    prev_v = None
    for kx in ks:
        w, v = np.linalg.eigh(strip_hamiltonian(kx, m, ny))
        if prev_v is not None:
            # follow bands by max eigenvector overlap (sorted index does NOT track a band across crossings)
            match = np.abs(prev_v.conj().T @ v).argmax(axis=0)  # for each now-state, its prev-state index
            for now_idx in range(len(w)):
                e_old = prev_w[match[now_idx]]
                e_now = w[now_idx]
                if (e_old < 0) != (e_now < 0):  # this tracked band crosses E=0 between the two kx
                    psi = v[:, now_idx]
                    tw = float(np.sum(np.abs(psi[top_q]) ** 2))
                    bw = float(np.sum(np.abs(psi[bot_q]) ** 2))
                    vel = float(np.sign(e_now - e_old))  # ks increasing -> dE/dk sign = chirality
                    if tw > 0.5:
                        top_cross += vel
                    elif bw > 0.5:
                        bot_cross += vel
        prev_w, prev_v = w, v
    return {
        "top_net_chirality": int(round(top_cross)),
        "bottom_net_chirality": int(round(bot_cross)),
        "closed_strip_net": int(round(top_cross + bot_cross)),
    }


def main() -> None:
    print("[Nielsen-Ninomiya + domain-wall escape + records-as-rows]\n")

    # (1) N-N in 1+1: naive lattice fermion doubles; net chirality 0. Continuum control: net +1.
    chir, net, count = nn_1d_doubling()
    print(f"  1D N-N: lattice E(k)=sin k has {count} zeros, chiralities {chir}, net = {net:.0f}")
    print("          continuum control E(k)=k on the real line: 1 zero, net = +1 (no doubling).")
    check("Nielsen-Ninomiya doubling: the compact-BZ lattice fermion has net chirality 0 (>=2 zeros)",
          count >= 2 and abs(net) < 1e-9,
          f"{count} zeros, net {net:.0f}")

    # (2) Bulk topology: Chern +/-1 in the topological window, 0 in the trivial one (control).
    m_topo, m_triv = -1.0, -3.0
    c_topo = bulk_chern(m_topo)
    c_triv = bulk_chern(m_triv)
    print(f"\n  bulk Chern number: M={m_topo:+g} -> C={c_topo:+d} (topological);  "
          f"M={m_triv:+g} -> C={c_triv:+d} (trivial)")
    check("bulk is topological at M=-1 (|Chern|=1) and trivial at M=-3 (Chern=0)",
          abs(c_topo) == 1 and c_triv == 0)

    # (3) The strip: single-edge chirality = the escape; closed strip = N-N (net 0); trivial = control.
    topo = edge_chirality(m_topo)
    triv = edge_chirality(m_triv)
    print("\n  Chern strip (periodic x, open y = two domain walls vs vacuum):")
    print(f"    topological (M={m_topo:+g}): top edge net = {topo['top_net_chirality']:+d}, "
          f"bottom edge net = {topo['bottom_net_chirality']:+d}, "
          f"CLOSED strip net = {topo['closed_strip_net']:+d}")
    print(f"    trivial     (M={m_triv:+g}): top edge net = {triv['top_net_chirality']:+d}, "
          f"bottom edge net = {triv['bottom_net_chirality']:+d}, "
          f"CLOSED strip net = {triv['closed_strip_net']:+d}")

    check("DOMAIN-WALL ESCAPE: a single edge carries net chirality = bulk Chern = +/-1 (topological phase)",
          abs(topo["top_net_chirality"]) == 1 and abs(topo["bottom_net_chirality"]) == 1)
    check("N-N ON THE CLOSED STRIP: the two edges are opposite, so the closed system is net chirality 0",
          topo["top_net_chirality"] == -topo["bottom_net_chirality"]
          and topo["closed_strip_net"] == 0)
    check("CONTROL: the trivial bulk has NO chiral edge mode on either edge (net 0 everywhere)",
          triv["top_net_chirality"] == 0 and triv["bottom_net_chirality"] == 0)

    print("\n[verdict]")
    if not FAIL:
        print("  * The three statements are ONE object. (1) N-N: the closed strip / compact BZ forces net")
        print("    chirality 0 (fermion doubling) -- the lattice shadow of the paper's Theorem 2 (net chiral")
        print("    index 0 on a closed Krein structure). (2) Domain-wall escape: a SINGLE edge (a domain wall")
        print("    between topological and vacuum) carries net chirality = the bulk Chern number = +/-1 --")
        print("    chirality as a boundary mode, the Kaplan/Jackiw-Rebbi escape. (3) Anomaly inflow: the two")
        print("    edges are opposite, so 'chiral boundary + net-0 bulk' is one fact -- the paper's 'external")
        print("    by structure, supplied by a net-self-dual chiral background/boundary'.")
        print("  * RECORDS-AS-ROWS READING (analysis grade): read the open y-direction as TIME (records")
        print("    accumulating) and the edge/domain-wall as the AUTOREGRESSIVE FRONTIER. The chiral edge")
        print("    mode is then chirality ISSUED at the present -- the frontier carries the net chirality the")
        print("    closed bulk cannot. This gives the records-as-rows frame a CONCRETE mechanism for the")
        print("    'external' chirality the generation-count terminus said had to come from outside the")
        print("    closed structure: it comes from the temporal boundary, by bulk-boundary correspondence.")
        print("  * SIX-AXIS DISPOSITION: this is a genuine SHADOW, not a mere relabel -- the object maps onto")
        print("    N-N's category (a lattice Dirac operator with a boundary) and REPRODUCES N-N's image (net-0")
        print("    bulk) AND its known escape (chiral edge). What stays SCOPE-EXIT is the identification of the")
        print("    frontier-as-domain-wall with GU's actual field content: the mechanism is real and generic;")
        print("    that GU's specific chiral sector is THIS edge mode is unbuilt (it rides SG4, as ever).")
        print("  * NOT CLAIMED: a derivation of 3 (or any) generations, a metric, or that the analogy is an")
        print("    identity. Toy/analysis grade; a mechanism demonstration with discriminating controls.")
    else:
        print(f"  * toy did not behave as expected: {FAIL} -- report honestly, do not force the reading.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = N-N doubling, the domain-wall chiral-edge escape, and anomaly inflow all reproduced.")


if __name__ == "__main__":
    main()
