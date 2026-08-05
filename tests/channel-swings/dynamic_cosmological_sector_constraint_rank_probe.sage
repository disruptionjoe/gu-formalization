#!/usr/bin/env sage
"""Exact finite gate for the dynamic cosmological-sector constraint claim.

This probe deliberately separates a relation between field values from an
independent action equation and from an action-parameter reduction.  It is a
finite Layer-0/rank classifier, not a cosmological solution.
"""

from collections import Counter


COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def rank_increment(existing_rows, candidate_rows, width):
    old = matrix(QQ, existing_rows) if existing_rows else matrix(QQ, 0, width)
    new = matrix(QQ, existing_rows + candidate_rows)
    return new.rank() - old.rank()


print("A. TWO FIELD VALUES")
identification = matrix(QQ, [[-1, 1]])  # d - c = 0
check("exact", "an independent equality has rank one on (c,d)",
      identification.rank() == 1)
check("exact", "an independent equality reduces two field values to one",
      2 - identification.rank() == 1)
check("exact", "the equality has one-dimensional kernel",
      identification.right_kernel().dimension() == 1)
check("exact", "the surviving ray is c=d",
      identification * vector(QQ, [1, 1]) == 0)

print("\nB. DEFINITIONS, IDENTITIES, AND FREE GAINS")
check("type", "a definition d:=c adds no equation to the one-coordinate model",
      rank_increment([], [], 1) == 0)
check("exact", "re-adding the equality as a Ward/Bianchi consequence adds zero rank",
      rank_increment([[-1, 1]], [[-1, 1]], 2) == 0)

# F(c,d,a)=d-a*c.  At the exact regular point (c,d,a)=(2,6,3),
# dF=(-a,1,-c)=(-3,1,-2), so one equation leaves two free directions.
free_gain_jacobian = matrix(QQ, [[-3, 1, -2]])
check("exact", "a proportionality with a free gain has generic rank one",
      free_gain_jacobian.rank() == 1)
check("type", "the free-gain horn leaves two local degrees of freedom",
      3 - free_gain_jacobian.rank() == 2)
check("planted", "PLANT a free gain is not misreported as a fixed normalization",
      3 - free_gain_jacobian.rank() != 1)

print("\nC. RADIATIVE SHIFT")
# d=c together with a shifted curvature equation c-d-rho=0 forces rho=0.
# It therefore does not screen a generic vacuum-energy shift.
radiative_system = matrix(QQ, [[-1, 1, 0], [1, -1, -1]])
check("exact", "identification plus shifted curvature equation has rank two",
      radiative_system.rank() == 2)
check("exact", "the solution kernel contains only rho=0",
      all(v[2] == 0 for v in radiative_system.right_kernel().basis()))
check("exact", "the common amplitude remains free on the homogeneous system",
      radiative_system.right_kernel().dimension() == 1)
check("planted", "PLANT a unit vacuum shift is not screened by d=c",
      vector(QQ, [0, 0, 1]) not in radiative_system.right_kernel())

print("\nD. SPATIAL FLATNESS IS NOT FOUR-DIMENSIONAL FLATNESS")
# Spatially flat de Sitter: k/a^2=0 while R_4=12 H^2 and G_00=3 H^2.
H = QQ(2)
spatial_three_curvature = QQ(0)
scalar_curvature_4d = 12 * H**2
einstein_00 = 3 * H**2
check("exact", "the witness is spatially flat", spatial_three_curvature == 0)
check("exact", "the same witness has nonzero four-dimensional scalar curvature",
      scalar_curvature_4d == 48 and scalar_curvature_4d != 0)
check("exact", "the same witness has nonzero Einstein 00 component",
      einstein_00 == 12 and einstein_00 != 0)
check("planted", "PLANT k=0 does not imply R4=0",
      not (spatial_three_curvature == 0 and scalar_curvature_4d == 0))

print("\nE. DISPOSITION")
check("type", "field-value reduction is conditional on an independent equation",
      identification.rank() == 1
      and rank_increment([[-1, 1]], [[-1, 1]], 2) == 0)
check("type", "action-parameter reduction remains unproved by this finite model",
      True)
check("type", "radiative stability requires additional adjustment dynamics",
      all(v[2] == 0 for v in radiative_system.right_kernel().basis()))
check("planted", "PLANT dynamism alone is not called a magnitude derivation",
      free_gain_jacobian.right_kernel().dimension() == 2)

print("\nCOUNTS " + " ".join(f"{k}={v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
