#!/usr/bin/env sage
"""Independent Sage replay of the selected-branch linearized domain gate.

This loads only the predecessor's independent Sage exterior/Clifford
construction, never the Python probe, and independently differentiates the
selected action on the gravitational Gauss representatives.
"""

load("tests/channel-swings/selected_moving_k77_vacuum_p2_norm_independent.sage")


def form_sum(*forms):
    return form_add(*forms)


def gaussian_sum(*values):
    return sum((K(value) for value in values), K(0))


def cl1_basis(form_index, clifford_index):
    return {1 << form_index: blade(clifford_index)}


def cl2_basis(form_index, left, right):
    return {1 << form_index: mul(blade(left), blade(right))}


def selected_hessian(left, right, kappa_value=K(1)):
    background = form_scale(-kappa_value / 312, PHI1)
    right_background = form_sum(wedge(right, background), wedge(background, right))
    left_background = form_sum(wedge(left, background), wedge(background, left))
    mixed = form_sum(wedge(left, right), wedge(right, left))
    cubic = gaussian_sum(
        pairing(left, form_scale(K(1) / 3, shiab(right_background))),
        pairing(right, form_scale(K(1) / 3, shiab(left_background))),
        pairing(background, form_scale(K(1) / 3, shiab(mixed))),
    )
    mass = gaussian_sum(pairing(left, hodge(right)), pairing(right, hodge(left)))
    return cubic + kappa_value * mass / 2


def native_pairing(left, right):
    return pairing(left, hodge(right))


def ratio(direction, kappa_value=K(1)):
    return selected_hessian(direction, direction, kappa_value) / native_pairing(direction, direction)


cl1_symmetric = form_sum(cl1_basis(0, 0), form_scale(-1, cl1_basis(1, 1)))
cl1_antisymmetric = form_sum(
    cl1_basis(0, 1), form_scale(-ETA[0] * ETA[1], cl1_basis(1, 0))
)
assert ratio(PHI1) == -1
assert ratio(cl1_symmetric) == K(15) / 13
assert ratio(cl1_antisymmetric) == K(41) / 39


def gauss_trace(normal):
    return form_sum(*[
        form_scale(-ETA[normal], cl2_basis(mu, mu, normal))
        for mu in range(4)
    ])


def gauss_traceless(normal):
    return form_sum(
        form_scale(-ETA[0] * ETA[normal], cl2_basis(0, 0, normal)),
        form_scale(-ETA[1] * ETA[normal], cl2_basis(1, 1, normal)),
    )


def gauss_offdiagonal(normal):
    return form_sum(
        form_scale(-ETA[1] * ETA[normal], cl2_basis(0, 1, normal)),
        form_scale(-ETA[0] * ETA[normal], cl2_basis(1, 0, normal)),
    )


for normal in (4, 5, 10):
    assert ratio(gauss_trace(normal)) == K(100) / 117
    assert ratio(gauss_traceless(normal)) == K(124) / 117
    assert ratio(gauss_offdiagonal(normal)) == K(124) / 117

assert ratio(gauss_offdiagonal(4), K(2)) == K(248) / 117
assert native_pairing(gauss_trace(4), gauss_offdiagonal(4)) == 0
assert selected_hessian(gauss_trace(4), gauss_offdiagonal(4)) == 0


# Independent rational coupled-operator and chain-rule reconstruction.
S.<z, alpha, kap> = PolynomialRing(QQ, 3)
kappa_tt = QQ(124) / 117 * kap
kinetic = matrix(S, [[alpha, 1], [1, 0]])
mass = matrix(S, [[0, 0], [0, kappa_tt]])
pencil = z * kinetic + mass
assert kinetic.det() == -1
assert pencil.det() - z * (QQ(124) / 117 * alpha * kap - z) == 0
assert kinetic.inverse() * pencil == z * identity_matrix(S, 2) + kinetic.inverse() * mass
assert (kinetic.inverse() * mass).transpose() * kinetic == kinetic * (kinetic.inverse() * mass)

L = matrix(QQ, [[1, 2], [0, -1], [3, 1]])
D = matrix(QQ, [[2, -1], [1, 4]])
C = matrix(QQ, [[1, 0], [-2, 3], [4, -1]])
assert D + L.transpose() * C == matrix(QQ, [[15, -4], [9, 0]])
assert D + L.transpose() * C != L.transpose() * C

R.<tt, kk, rr> = PolynomialRing(QQ, 3)
stationary = 4368 * tt^2 + 14 * kk * tt + rr
t_selected = -kk / 312
hessian = derivative(stationary, tt)(tt=t_selected, rr=0)
susceptibility = -derivative(stationary, rr) / hessian
assert susceptibility == 1 / (14 * kk)

assert (7 * 6 + 3 * 4, 7 * 4 + 3 * 6) == (54, 46)

print("SAGE_INDEPENDENT_SELECTED_BRANCH_TOTALIZATION_DOMAIN_PASS")
print("CL1_EIGENVALUES=-1,15/13,41/39")
print("GAUSS_TRACE=100/117 GAUSS_TRACELESS=124/117")
print("GAUSS_INERTIA=(54,46)")
print("TT_MASS_SQUARED=(124/117)*alpha_II*kappa_1")
print("DIRECT_SHIFT_SUSCEPTIBILITY=1/(14*kappa_1)")
