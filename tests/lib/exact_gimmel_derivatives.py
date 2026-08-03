#!/usr/bin/env python3
r"""Exact (closed-form) derivatives of the gimmel/DeWitt metric on Y14.

Register item M-C2 / audit finding B4 / acceptance rule P-H29.

The RB6/RB7/W177 probes evaluate curvature and divergence tensors of the
explicit gimmel metric on

    Y14 = X4 x Sym^2(T*X),    G(h) = g(h) (+) f(h),

where, in the frozen probe conventions
(``tests/channel-swings/w177_ym_residual_and_mode_closure_probe.py``),

    g(h)   = vmat(h) = sum_i h_i E_i            (base block, LINEAR in h),
    f_ij(h) = tr(A_i A_j) - (1/2) tr(A_i) tr(A_j),   A_i = g^{-1} E_i,

with E_i the ten symmetric-pair basis elements and h the ten fibre
coordinates.  The metric depends on the fibre coordinates only; all base
partials vanish identically.

Those probes differentiate this metric by nested central finite differences.
The published RB7 "vertical residual" 0.00361491 is s^-3 roundoff of an
exactly-zero quantity (eleven-lens-audit B4); the W177 contracted-Bianchi
floor is FD-limited.  This library replaces every interior FD layer with the
closed forms

    d_k g          = E_k,                d_k d_l g = 0,
    d_k A_i        = -A_k A_i,
    d_k d_l A_i    =  A_k A_l A_i + A_l A_k A_i,
    d_k d_l d_m A_i = - sum_{perm p of (k,l,m)} A_{p1} A_{p2} A_{p3} A_i,

(each following from d_k g^{-1} = -g^{-1} E_k g^{-1}) and Leibniz on
f_ij = tr(A_i A_j) - (1/2) tr(A_i) tr(A_j).  From dG, d2G, d3G it assembles
exact Christoffel symbols, their first and second coordinate derivatives,
the lowered Riemann tensor, its first derivatives, Ricci, and dRicci --
everything the RB7/W177 pipelines previously obtained by FD.

Index conventions match the frozen probes exactly:

  * coordinates Q = 0..13; fibre coordinate i occupies slot Q = 4 + i;
  * derivative arrays are indexed with the FULL 14-dim coordinate on the
    derivative axes (base slots identically zero), e.g. dG[q, m, n] is
    partial_q G_mn;
  * Gamma[i, j, k] = Gamma^i_{jk};
  * riemann_low[i, j, k, l] = R_ijkl with
    R^i_jkl = d_k Gamma^i_jl - d_l Gamma^i_jk + Gamma^i_kp Gamma^p_jl
              - Gamma^i_lp Gamma^p_jk;
  * ricci[j, l] = G^{im} R_mjil.

Self-test (``python tests/lib/exact_gimmel_derivatives.py``): every closed
form is verified against central finite differences at two nested steps with
an O(step^2) convergence-ratio assert (ratio ~ 100 per 10x step refinement),
and the assembled Gamma / Riemann are verified against the frozen W177
probe's OWN FD constructions at its production steps.  The fully exact
contracted-Bianchi identity (direct divergence == Ricci-Codazzi form) is
asserted at the 1e-10 level as an end-to-end consistency check.

This module makes no verdict.  The re-verdicts live in
``tests/channel-swings/verify/rb7_exact_derivative_reverdict.py`` and
``tests/channel-swings/verify/w177_exact_derivative_reverdict.py``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations

import numpy as np


def einsum(*operands):
    """np.einsum with a contraction path; the naive multi-operand loop is
    prohibitively slow on the 14-index tensors used here."""
    return np.einsum(*operands, optimize=True)


N = 14
NF = 10
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]
EBASIS: list[np.ndarray] = []
for _pair in PAIRS:
    _matrix = np.zeros((4, 4))
    _a, _b = _pair
    _matrix[_a, _b] = 1.0
    _matrix[_b, _a] = 1.0
    EBASIS.append(_matrix)
EARRAY = np.stack(EBASIS)  # (10, 4, 4)


def vmat(components: np.ndarray) -> np.ndarray:
    """Symmetric 4x4 matrix from ten pair components (probe convention)."""
    matrix = np.zeros((4, 4))
    for component, (a, b) in zip(components, PAIRS, strict=True):
        matrix[a, b] = component
        matrix[b, a] = component
    return matrix


def comps_of(matrix: np.ndarray) -> np.ndarray:
    return np.array([matrix[a, b] for a, b in PAIRS])


def fibre_metric(base_metric: np.ndarray) -> np.ndarray:
    """f_ij = tr(A_i A_j) - (1/2) tr(A_i) tr(A_j), A_i = g^{-1} E_i."""
    inverse = np.linalg.inv(base_metric)
    raised = einsum("ab,ibc->iac", inverse, EARRAY)
    trace_pair = einsum("iab,jba->ij", raised, raised)
    trace_single = einsum("iaa->i", raised)
    return trace_pair - 0.5 * np.outer(trace_single, trace_single)


def gimmel(hvec: np.ndarray) -> np.ndarray:
    base_metric = vmat(hvec)
    result = np.zeros((N, N))
    result[:4, :4] = base_metric
    result[4:, 4:] = fibre_metric(base_metric)
    return result


# ---------------------------------------------------------------------------
# Closed-form fibre-block derivatives.
# ---------------------------------------------------------------------------


def fibre_block_derivatives(
    base_metric: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return (f, d1f, d2f, d3f) for the fibre block, all closed-form.

    Shapes: f (10,10); d1f (10,10,10) = d_k f_ij; d2f (10,10,10,10)
    = d_k d_l f_ij; d3f (10,10,10,10,10) = d_k d_l d_m f_ij, with the
    derivative axes FIRST and symmetric among themselves.
    """
    inverse = np.linalg.inv(base_metric)
    a1 = einsum("ab,ibc->iac", inverse, EARRAY)  # A_i
    # Products of A's.
    p2 = einsum("kab,lbc->klac", a1, a1)  # A_k A_l
    p3 = einsum("klab,mbc->klmac", p2, a1)  # A_k A_l A_m

    # Derivatives of A_i (derivative axes first, then the A index).
    d1a = -einsum("kab,ibc->kiac", a1, a1)  # d_k A_i = -A_k A_i
    d2a = einsum("klab,ibc->kliac", p2, a1) + einsum(
        "lkab,ibc->kliac", p2, a1
    )  # d_k d_l A_i = (A_k A_l + A_l A_k) A_i
    perm_sum = np.zeros_like(p3)
    for order in permutations((0, 1, 2)):
        perm_sum += p3.transpose(*order, 3, 4)
    d3a = -einsum("klmab,ibc->klmiac", perm_sum, a1)

    tr0 = einsum("iaa->i", a1)
    tr1 = einsum("kiaa->ki", d1a)
    tr2 = einsum("kliaa->kli", d2a)
    tr3 = einsum("klmiaa->klmi", d3a)

    f = einsum("iab,jba->ij", a1, a1) - 0.5 * np.outer(tr0, tr0)

    d1f = (
        einsum("kiab,jba->kij", d1a, a1)
        + einsum("iab,kjba->kij", a1, d1a)
        - 0.5
        * (
            einsum("ki,j->kij", tr1, tr0)
            + einsum("i,kj->kij", tr0, tr1)
        )
    )

    d2f = (
        einsum("kliab,jba->klij", d2a, a1)
        + einsum("kiab,ljba->klij", d1a, d1a)
        + einsum("liab,kjba->klij", d1a, d1a)
        + einsum("iab,kljba->klij", a1, d2a)
        - 0.5
        * (
            einsum("kli,j->klij", tr2, tr0)
            + einsum("ki,lj->klij", tr1, tr1)
            + einsum("li,kj->klij", tr1, tr1)
            + einsum("i,klj->klij", tr0, tr2)
        )
    )

    d3f = (
        einsum("klmiab,jba->klmij", d3a, a1)
        + einsum("kliab,mjba->klmij", d2a, d1a)
        + einsum("kmiab,ljba->klmij", d2a, d1a)
        + einsum("lmiab,kjba->klmij", d2a, d1a)
        + einsum("kiab,lmjba->klmij", d1a, d2a)
        + einsum("liab,kmjba->klmij", d1a, d2a)
        + einsum("miab,kljba->klmij", d1a, d2a)
        + einsum("iab,klmjba->klmij", a1, d3a)
        - 0.5
        * (
            einsum("klmi,j->klmij", tr3, tr0)
            + einsum("kli,mj->klmij", tr2, tr1)
            + einsum("kmi,lj->klmij", tr2, tr1)
            + einsum("lmi,kj->klmij", tr2, tr1)
            + einsum("ki,lmj->klmij", tr1, tr2)
            + einsum("li,kmj->klmij", tr1, tr2)
            + einsum("mi,klj->klmij", tr1, tr2)
            + einsum("i,klmj->klmij", tr0, tr3)
        )
    )

    return f, d1f, d2f, d3f


def metric_derivatives(
    hvec: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return (G, dG, d2G, d3G), coordinate axes full-14 (base slots zero).

    dG[q, m, n] = partial_q G_mn and so on; the base block of dG is exactly
    E_k (the metric is linear in h there), and its higher derivatives vanish.
    """
    base_metric = vmat(hvec)
    f, d1f, d2f, d3f = fibre_block_derivatives(base_metric)

    metric = np.zeros((N, N))
    metric[:4, :4] = base_metric
    metric[4:, 4:] = f

    d_metric = np.zeros((N, N, N))
    d_metric[4:, :4, :4] = EARRAY
    d_metric[4:, 4:, 4:] = d1f

    d2_metric = np.zeros((N, N, N, N))
    d2_metric[4:, 4:, 4:, 4:] = d2f

    d3_metric = np.zeros((N, N, N, N, N))
    d3_metric[4:, 4:, 4:, 4:, 4:] = d3f

    return metric, d_metric, d2_metric, d3_metric


# ---------------------------------------------------------------------------
# Exact geometry assembled from the closed forms.
# ---------------------------------------------------------------------------


@dataclass
class ExactGeometry:
    """All exactly differentiated objects at one gimmel point."""

    metric: np.ndarray  # G_mn
    inverse: np.ndarray  # G^mn
    d_metric: np.ndarray  # dG[q,m,n]
    d_inverse: np.ndarray  # d(G^{-1})[q,m,n]
    gamma: np.ndarray  # Gamma^i_{jk} as [i,j,k]
    d_gamma: np.ndarray  # d_q Gamma^i_{jk} as [q,i,j,k]
    d2_gamma: np.ndarray  # d_q d_r Gamma^i_{jk} as [q,r,i,j,k]
    riemann_low: np.ndarray  # R_ijkl
    d_riemann_low: np.ndarray  # d_q R_ijkl as [q,i,j,k,l]
    ricci: np.ndarray  # Ric_jl
    d_ricci: np.ndarray  # d_q Ric_jl as [q,j,l]


def exact_geometry(hvec: np.ndarray) -> ExactGeometry:
    metric, d_g, d2_g, d3_g = metric_derivatives(hvec)
    inverse = np.linalg.inv(metric)

    d_inv = -einsum("ma,qab,bn->qmn", inverse, d_g, inverse)
    d2_inv = (
        einsum("ma,rab,bc,qcd,dn->qrmn", inverse, d_g, inverse, d_g, inverse)
        + einsum(
            "ma,qab,bc,rcd,dn->qrmn", inverse, d_g, inverse, d_g, inverse
        )
        - einsum("ma,qrab,bn->qrmn", inverse, d2_g, inverse)
    )

    # C_pjk = (1/2)(d_j G_pk + d_k G_pj - d_p G_jk) and its derivatives.
    c0 = 0.5 * (
        einsum("jpk->pjk", d_g)
        + einsum("kpj->pjk", d_g)
        - d_g
    )
    c1 = 0.5 * (
        einsum("qjpk->qpjk", d2_g)
        + einsum("qkpj->qpjk", d2_g)
        - einsum("qpjk->qpjk", d2_g)
    )
    c2 = 0.5 * (
        einsum("qrjpk->qrpjk", d3_g)
        + einsum("qrkpj->qrpjk", d3_g)
        - einsum("qrpjk->qrpjk", d3_g)
    )

    gamma = einsum("ip,pjk->ijk", inverse, c0)
    d_gamma = einsum("qip,pjk->qijk", d_inv, c0) + einsum(
        "ip,qpjk->qijk", inverse, c1
    )
    d2_gamma = (
        einsum("qrip,pjk->qrijk", d2_inv, c0)
        + einsum("qip,rpjk->qrijk", d_inv, c1)
        + einsum("rip,qpjk->qrijk", d_inv, c1)
        + einsum("ip,qrpjk->qrijk", inverse, c2)
    )

    # R^i_jkl = d_k Gamma^i_jl - d_l Gamma^i_jk
    #           + Gamma^i_kp Gamma^p_jl - Gamma^i_lp Gamma^p_jk.
    riemann_up = (
        einsum("kijl->ijkl", d_gamma)
        - einsum("lijk->ijkl", d_gamma)
        + einsum("ikp,pjl->ijkl", gamma, gamma)
        - einsum("ilp,pjk->ijkl", gamma, gamma)
    )
    d_riemann_up = (
        einsum("qkijl->qijkl", d2_gamma)
        - einsum("qlijk->qijkl", d2_gamma)
        + einsum("qikp,pjl->qijkl", d_gamma, gamma)
        + einsum("ikp,qpjl->qijkl", gamma, d_gamma)
        - einsum("qilp,pjk->qijkl", d_gamma, gamma)
        - einsum("ilp,qpjk->qijkl", gamma, d_gamma)
    )

    riemann_low = einsum("im,mjkl->ijkl", metric, riemann_up)
    d_riemann_low = einsum("qim,mjkl->qijkl", d_g, riemann_up) + einsum(
        "im,qmjkl->qijkl", metric, d_riemann_up
    )

    ricci = einsum("im,mjil->jl", inverse, riemann_low)
    d_ricci = einsum("qim,mjil->qjl", d_inv, riemann_low) + einsum(
        "im,qmjil->qjl", inverse, d_riemann_low
    )

    return ExactGeometry(
        metric=metric,
        inverse=inverse,
        d_metric=d_g,
        d_inverse=d_inv,
        gamma=gamma,
        d_gamma=d_gamma,
        d2_gamma=d2_gamma,
        riemann_low=riemann_low,
        d_riemann_low=d_riemann_low,
        ricci=ricci,
        d_ricci=d_ricci,
    )


# ---------------------------------------------------------------------------
# Probe-convention divergence assemblies (identical formulas to the frozen
# probes, fed here with exact ingredients).
# ---------------------------------------------------------------------------


def covariant_derivative_two_tensor(
    partial_tensor: np.ndarray,
    tensor: np.ndarray,
    gamma: np.ndarray,
) -> np.ndarray:
    """nabla_Q T_AB for a covariant two-tensor (probe convention)."""
    return (
        partial_tensor
        - einsum("pqa,pb->qab", gamma, tensor)
        - einsum("pqb,ap->qab", gamma, tensor)
    )


def codazzi_residual(nabla_ricci: np.ndarray) -> np.ndarray:
    """Y_MJL = nabla_M Ric_LJ - nabla_J Ric_LM (probe convention)."""
    first = einsum("mlj->mjl", nabla_ricci)
    second = einsum("jlm->mjl", nabla_ricci)
    return first - second


def direct_divergence(
    metric: np.ndarray,
    gamma: np.ndarray,
    riemann_low: np.ndarray,
    partial_riemann: np.ndarray,
) -> np.ndarray:
    """G^KQ nabla_Q R_MJKL, all four connection terms (probe convention)."""
    nabla = (
        partial_riemann
        - einsum("pqm,pjkl->qmjkl", gamma, riemann_low)
        - einsum("pqj,mpkl->qmjkl", gamma, riemann_low)
        - einsum("pqk,mjpl->qmjkl", gamma, riemann_low)
        - einsum("pql,mjkp->qmjkl", gamma, riemann_low)
    )
    return einsum("kq,qmjkl->mjl", np.linalg.inv(metric), nabla)


def exact_codazzi_and_direct(
    hvec: np.ndarray,
) -> tuple[ExactGeometry, np.ndarray, np.ndarray]:
    """Fully exact (Y_codazzi, Y_direct) at hvec: zero FD layers anywhere."""
    geo = exact_geometry(hvec)
    nabla_ricci = covariant_derivative_two_tensor(
        geo.d_ricci, geo.ricci, geo.gamma
    )
    codazzi = codazzi_residual(nabla_ricci)
    direct = direct_divergence(
        geo.metric, geo.gamma, geo.riemann_low, geo.d_riemann_low
    )
    return geo, codazzi, direct


def outer_fd_codazzi_and_direct(
    hvec: np.ndarray, ricci_step: float
) -> tuple[ExactGeometry, np.ndarray, np.ndarray]:
    """(Y_codazzi, Y_direct) with EXACT inner layers and one outer FD layer.

    Gamma and Riemann are exact everywhere; only the outermost derivative
    (d_q Ric, d_q Riemann entering the divergence) is a central finite
    difference of exact functions, mirroring the frozen probes' outermost
    ``ricci_step`` layer.  Used to exhibit the clean O(step^2) truncation
    behaviour that the all-FD pipeline buried in s^-3 roundoff.
    """
    geo = exact_geometry(hvec)
    partial_ricci = np.zeros((N, N, N))
    partial_riemann = np.zeros((N, N, N, N, N))
    for fibre_index in range(NF):
        plus = hvec.copy()
        minus = hvec.copy()
        plus[fibre_index] += ricci_step
        minus[fibre_index] -= ricci_step
        geo_plus = exact_geometry(plus)
        geo_minus = exact_geometry(minus)
        partial_ricci[4 + fibre_index] = (
            geo_plus.ricci - geo_minus.ricci
        ) / (2.0 * ricci_step)
        partial_riemann[4 + fibre_index] = (
            geo_plus.riemann_low - geo_minus.riemann_low
        ) / (2.0 * ricci_step)

    nabla_ricci = covariant_derivative_two_tensor(
        partial_ricci, geo.ricci, geo.gamma
    )
    codazzi = codazzi_residual(nabla_ricci)
    direct = direct_divergence(
        geo.metric, geo.gamma, geo.riemann_low, partial_riemann
    )
    return geo, codazzi, direct


# ---------------------------------------------------------------------------
# Self-test: exact-vs-FD convergence and coarse-step agreement with the
# frozen probes' own finite differences.
# ---------------------------------------------------------------------------


def _self_test() -> int:
    import os
    import sys

    here = os.path.dirname(os.path.abspath(__file__))
    swings = os.path.join(os.path.dirname(here), "channel-swings")
    if swings not in sys.path:
        sys.path.insert(0, swings)
    import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402

    failures: list[str] = []

    def check(label: str, condition: bool, detail: str = "") -> None:
        passed = bool(condition)
        suffix = f" ({detail})" if detail else ""
        print(f"{'PASS' if passed else 'FAIL'}: {label}{suffix}")
        if not passed:
            failures.append(label)

    hvec = w177.fixed_w177_point()

    # 0. Convention identity: this module's gimmel is the probe's gimmel
    # (vectorized trace order differs from the probe's loop by <= 1 ulp).
    check(
        "library gimmel/vmat reproduce the probe's own to 1e-14",
        float(np.max(np.abs(gimmel(hvec) - w177.gimmel(hvec)))) < 1.0e-14
        and float(np.max(np.abs(vmat(hvec) - w177.vmat(hvec)))) == 0.0,
    )

    metric, d_g, d2_g, d3_g = metric_derivatives(hvec)

    def fd_error_dg(step: float) -> float:
        fd = np.zeros((N, N, N))
        for k in range(NF):
            plus = hvec.copy()
            minus = hvec.copy()
            plus[k] += step
            minus[k] -= step
            fd[4 + k] = (gimmel(plus) - gimmel(minus)) / (2.0 * step)
        return float(np.max(np.abs(fd - d_g)))

    def fd_error_d2g(step: float) -> float:
        fd = np.zeros((N, N, N, N))
        for k in range(NF):
            plus = hvec.copy()
            minus = hvec.copy()
            plus[k] += step
            minus[k] -= step
            fd[4 + k] = (
                metric_derivatives(plus)[1] - metric_derivatives(minus)[1]
            ) / (2.0 * step)
        return float(np.max(np.abs(fd - d2_g)))

    def fd_error_d3g(step: float) -> float:
        fd = np.zeros((N, N, N, N, N))
        for k in range(NF):
            plus = hvec.copy()
            minus = hvec.copy()
            plus[k] += step
            minus[k] -= step
            fd[4 + k] = (
                metric_derivatives(plus)[2] - metric_derivatives(minus)[2]
            ) / (2.0 * step)
        return float(np.max(np.abs(fd - d3_g)))

    # 1-3. O(step^2) convergence of each closed form (ratio ~100 per 10x).
    # The fine-step bound is the FD truncation of the comparator, which grows
    # with derivative order; the load-bearing assert is the ratio.
    for label, fd_error, fine_bound in (
        ("dG", fd_error_dg, 1.0e-4),
        ("d2G", fd_error_d2g, 1.0e-3),
        ("d3G", fd_error_d3g, 1.0e-2),
    ):
        coarse = fd_error(1.0e-2)
        fine = fd_error(1.0e-3)
        ratio = coarse / max(fine, 1.0e-300)
        check(
            f"exact {label} matches central FD with O(step^2) convergence",
            60.0 < ratio < 140.0 and fine < fine_bound,
            f"err(1e-2)={coarse:.6e}, err(1e-3)={fine:.6e}, ratio={ratio:.2f}",
        )

    geo = exact_geometry(hvec)

    # 4. Exact Gamma against the probe's OWN production-step FD Christoffel.
    gamma_probe = w177.christoffel(hvec, 1.0e-5)[2]
    check(
        "exact Gamma agrees with the frozen probe's FD Gamma (step 1e-5)",
        float(np.max(np.abs(geo.gamma - gamma_probe))) < 1.0e-7,
        f"max diff={float(np.max(np.abs(geo.gamma - gamma_probe))):.3e}",
    )
    # ... and the probe's FD converges to the exact value at O(step^2).
    gamma_coarse = float(
        np.max(np.abs(w177.christoffel(hvec, 1.0e-2)[2] - geo.gamma))
    )
    gamma_fine = float(
        np.max(np.abs(w177.christoffel(hvec, 1.0e-3)[2] - geo.gamma))
    )
    check(
        "probe FD Gamma converges to exact Gamma at O(step^2)",
        60.0 < gamma_coarse / max(gamma_fine, 1.0e-300) < 140.0,
        f"err(1e-2)={gamma_coarse:.3e}, err(1e-3)={gamma_fine:.3e}, "
        f"ratio={gamma_coarse / max(gamma_fine, 1.0e-300):.2f}",
    )

    # 5. Exact Riemann against the probe's production-step FD Riemann.
    riemann_probe = w177.riemann_data(hvec, 1.0e-5, 1.0e-4)[3]
    check(
        "exact Riemann agrees with the frozen probe's FD Riemann",
        float(np.max(np.abs(geo.riemann_low - riemann_probe))) < 1.0e-5,
        f"max diff="
        f"{float(np.max(np.abs(geo.riemann_low - riemann_probe))):.3e}",
    )

    # 6. Exact d_gamma / d_riemann / d_ricci against FD of exact functions.
    def fd_of_exact(attr: str, step: float) -> float:
        exact_value = getattr(geo, attr)
        source = {
            "d_gamma": "gamma",
            "d_riemann_low": "riemann_low",
            "d_ricci": "ricci",
        }[attr]
        fd = np.zeros_like(exact_value)
        for k in range(NF):
            plus = hvec.copy()
            minus = hvec.copy()
            plus[k] += step
            minus[k] -= step
            fd[4 + k] = (
                getattr(exact_geometry(plus), source)
                - getattr(exact_geometry(minus), source)
            ) / (2.0 * step)
        return float(np.max(np.abs(fd - exact_value)))

    for attr in ("d_gamma", "d_riemann_low", "d_ricci"):
        coarse = fd_of_exact(attr, 1.0e-2)
        fine = fd_of_exact(attr, 1.0e-3)
        ratio = coarse / max(fine, 1.0e-300)
        check(
            f"exact {attr} matches FD of the exact parent at O(step^2)",
            60.0 < ratio < 140.0 and fine < 1.0e-2,
            f"err(1e-2)={coarse:.6e}, err(1e-3)={fine:.6e}, ratio={ratio:.2f}",
        )

    # 7. Exact metric compatibility: nabla G = 0 to roundoff.
    nabla_metric = covariant_derivative_two_tensor(
        geo.d_metric, geo.metric, geo.gamma
    )
    check(
        "exact Levi-Civita metric compatibility holds to roundoff",
        float(np.linalg.norm(nabla_metric)) < 1.0e-12,
        f"|nabla G|={float(np.linalg.norm(nabla_metric)):.3e}",
    )

    # 8. Fully exact contracted Bianchi: direct == codazzi to roundoff.
    _geo, codazzi, direct = exact_codazzi_and_direct(hvec)
    defect = float(np.linalg.norm(direct - codazzi))
    check(
        "fully exact contracted-Bianchi identity holds to 1e-10",
        defect < 1.0e-10,
        f"|direct - codazzi|={defect:.3e}",
    )

    if failures:
        print("FAILED SELF-TESTS:")
        for name in failures:
            print(f"  - {name}")
        return 1
    print("EXACT GIMMEL DERIVATIVE LIBRARY: ALL SELF-TESTS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(_self_test())
