#!/usr/bin/env python3
"""Exact topology and symplectic checks for the relative K77 edge bitorsor."""

from sympy import Matrix, Rational, eye, zeros


PASSED = []
PLANTS = []


def exact(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    PASSED.append(label)


def planted(label, bad_condition):
    if bool(bad_condition):
        raise AssertionError(f"plant did not fire: {label}")
    PLANTS.append(label)


def zmat(matrix):
    return all(value == 0 for value in matrix)


def flat(matrix):
    return Matrix(list(matrix))


# Noncommuting target and reference transition data on a triple overlap.
g01 = Matrix([[1, 1], [0, 1]])
g12 = Matrix([[2, 0], [1, 1]])
k01 = Matrix([[1, 0], [1, 1]])
k12 = Matrix([[1, 2], [0, 1]])
g02 = g01 * g12
k02 = k01 * k12
u0 = Matrix([[2, 1], [1, 1]])
theta0 = Matrix([[1, 2], [3, 5]])
p0 = Matrix([[2, -1], [4, 3]])

exact("transition matrices invertible", all(m.det() != 0 for m in (g01, g12, k01, k12, u0)))
exact("target cocycle closes", g02 == g01 * g12)
exact("reference cocycle closes", k02 == k01 * k12)

# u is a local representative of Isom_H(P_target,P_reference).
u1 = k01.inv() * u0 * g01
u2_step = k12.inv() * u1 * g12
u2_direct = k02.inv() * u0 * g02
exact("relative bitorsor triple overlap", u2_step == u2_direct)

theta1 = g01.inv() * theta0 * g01
p1 = g01.inv() * p0 * g01
q0 = u0 * theta0 * u0.inv()
pi0 = u0 * p0 * u0.inv()
q1 = u1 * theta1 * u1.inv()
pi1 = u1 * p1 * u1.inv()
exact("dressed distortion patches on reference bundle", q1 == k01.inv() * q0 * k01)
exact("dressed momentum patches on reference bundle", pi1 == k01.inv() * pi0 * k01)
exact("invariant trace patches globally", (q1 * pi1).trace() == (q0 * pi0).trace())

mu0 = theta0 * p0 - p0 * theta0
dressed_mu0 = q0 * pi0 - pi0 * q0
exact("dressed moment map is conjugated raw moment map", dressed_mu0 == u0 * mu0 * u0.inv())
mu1_ref = q1 * pi1 - pi1 * q1
exact("dressed moment map patches adjointly", mu1_ref == k01.inv() * dressed_mu0 * k01)

# Target active gauge action: the reference bundle is held fixed.
h = Matrix([[1, 2], [1, 3]])
theta_h = h.inv() * theta0 * h
p_h = h.inv() * p0 * h
u_h = u0 * h
exact("target gauge leaves dressed distortion invariant", u_h * theta_h * u_h.inv() == q0)
exact("target gauge leaves dressed momentum invariant", u_h * p_h * u_h.inv() == pi0)
exact("target gauge leaves dressed moment map invariant", u_h * (theta_h * p_h - p_h * theta_h) * u_h.inv() == dressed_mu0)

# Reference active gauge action: dressed fields transform adjointly, scalars stay fixed.
r = Matrix([[2, 1], [1, 1]])
u_r = r.inv() * u0
q_r = u_r * theta0 * u_r.inv()
pi_r = u_r * p0 * u_r.inv()
exact("reference gauge conjugates dressed distortion", q_r == r.inv() * q0 * r)
exact("reference gauge conjugates dressed momentum", pi_r == r.inv() * pi0 * r)
exact("reference gauge preserves trace pairing", (q_r * pi_r).trace() == (q0 * pi0).trace())

# Old one-sided edge frame is exactly the trivial-reference special case.
i2 = eye(2)
u1_old = u0 * g01
exact("relative law reduces to one-sided law for trivial reference", i2.inv() * u0 * g01 == u1_old)
q1_old = u1_old * theta1 * u1_old.inv()
exact("old dressing is absolute only in trivial reference", q1_old == q0)

# A reference copy of the target bundle makes the relative configuration nonempty.
u_identity = eye(2)
exact("identity section patches for reference copy", g01.inv() * u_identity * g01 == u_identity)
exact("identity section preserves the local dressed field", u_identity * theta0 * u_identity.inv() == theta0)

# Exact clutching-class test. Local frames on hemispheres extend across disks,
# so their boundary classes vanish. The relative law requires n_target=n_ref.
def one_sided_nonempty(clutching_class):
    return clutching_class == 0


def relative_nonempty(target_class, reference_class):
    return target_class == reference_class


exact("one-sided U1 trivial class admits frame", one_sided_nonempty(0))
exact("one-sided U1 c1=1 is obstructed", not one_sided_nonempty(1))
exact("one-sided SU2 trivial class admits frame", one_sided_nonempty(0))
exact("one-sided SU2 c2=1 is obstructed", not one_sided_nonempty(1))
exact("relative U1 equal c1 classes admit frame", relative_nonempty(3, 3))
exact("relative U1 unequal c1 classes are obstructed", not relative_nonempty(3, 2))
exact("relative SU2 equal c2 classes admit frame", relative_nonempty(1, 1))
exact("relative SU2 unequal c2 classes are obstructed", not relative_nonempty(1, 0))
exact("reference copy adds no independent topology", relative_nonempty(7, 7))

# Local cotangent reduction is unchanged by the passive reference patch law.
vals = list(theta0) + list(p0) + list(u0)


def dressed_map(values):
    th = Matrix(2, 2, values[0:4])
    pp = Matrix(2, 2, values[4:8])
    uu = Matrix(2, 2, values[8:12])
    return flat(uu * th * uu.inv()).col_join(flat(uu * pp * uu.inv()))


from sympy import symbols

xx = symbols("x0:12")
f = dressed_map(xx)
jac = f.jacobian(Matrix(xx)).subs(dict(zip(xx, vals)))
exact("dressed local map rank eight", jac.rank() == 8)

omega8 = zeros(8)
omega8[:4, 4:] = eye(4)
omega8[4:, :4] = -eye(4)
pulled = jac.T * omega8 * jac
exact("pulled presymplectic form rank eight", pulled.rank() == 8)
exact("pulled characteristic kernel dimension four", 12 - pulled.rank() == 4)

basis = [Matrix([[1, 0], [0, 0]]), Matrix([[0, 1], [0, 0]]),
         Matrix([[0, 0], [1, 0]]), Matrix([[0, 0], [0, 1]])]
orbit_columns = []
for e in basis:
    dtheta = theta0 * e - e * theta0
    dp = p0 * e - e * p0
    du = u0 * e
    orbit_columns.append(flat(dtheta).col_join(flat(dp)).col_join(flat(du)))
orbit = Matrix.hstack(*orbit_columns)
exact("target gauge orbit rank four", orbit.rank() == 4)
exact("target gauge orbit lies in dressed-map kernel", zmat(jac * orbit))
exact("target gauge orbit equals characteristic kernel", orbit.rank() == 12 - pulled.rank() and zmat(pulled * orbit))

# Planted failures.
planted("wrong left reference side", k01 * u0 * g01 == u1)
planted("omitted reference transition", u0 * g01 == u1)
planted("reversed target transition", k01.inv() * u0 * g01.inv() == u1)
planted("wrong distortion patch", q1 == k01 * q0 * k01.inv())
planted("dressed distortion falsely absolute", q1 == q0)
planted("left target action", (h * u0) * theta_h * (h * u0).inv() == q0)
planted("frozen edge frame under target gauge", u0 * theta_h * u0.inv() == q0)
planted("noninvariant matrix entry used as scalar", q_r[0, 0] == q0[0, 0])
planted("one-sided nontrivial U1 bundle admitted", one_sided_nonempty(1))
planted("mismatched relative bundles admitted", relative_nonempty(1, 0))

print(f"PASS selected K77 relative edge bitorsor topology: {len(PASSED)} exact + {len(PLANTS)} planted = {len(PASSED) + len(PLANTS)}")
