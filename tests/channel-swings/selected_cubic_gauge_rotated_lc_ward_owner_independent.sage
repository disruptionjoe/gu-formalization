"""Independent Sage corner-polarization check of the LC/Ward owner."""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_cubic_augmented_torsion_d3_owner_independent.sage"
capture = StringIO()
with redirect_stdout(capture):
    I = runpy.run_path(str(PREDECESSOR), init_globals={"QQ": QQ})
assert "INDEPENDENT_SAGE_PASS" in capture.getvalue()

P = I["PHI1"]
ZERO = I["ZERO"]
corner_d3 = I["corner_d3"]
cl2_basis = I["B"]["cl2_basis"]
fscale = I["fscale"]
form_sum = I["form_sum"]


def F(n, d=1):
    """Fraction constructor that preserves an already-rational numerator."""
    denominator = Fraction(int(d))
    if isinstance(n, Fraction):
        return n / denominator
    return Fraction(int(n)) / denominator


def lc(momentum, wave):
    terms = []
    for mu in range(4):
        for a in range(4):
            for b in range(a + 1, 4):
                coefficient = F(
                    momentum[b] * wave[mu][a] - momentum[a] * wave[mu][b], 2
                )
                if coefficient:
                    terms.append(fscale(coefficient, cl2_basis(mu, a, b)))
    return form_sum(*terms)


def gauge(momentum, a, b):
    return form_sum(*[
        fscale(momentum[mu], cl2_basis(mu, a, b))
        for mu in range(4) if momentum[mu]
    ])


plus = [[F(0) for _ in range(4)] for _ in range(4)]
plus[1][1] = F(1)
plus[2][2] = F(-1)
cross = [[F(0) for _ in range(4)] for _ in range(4)]
cross[1][2] = cross[2][1] = F(1)
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]

for scalar_mass, partner_mass in ((F(3), F(1)), (F(5), F(3)), (F(7), F(1))):
    momentum = (scalar_mass * scalar_mass - partner_mass * partner_mass) / (F(2) * scalar_mass)
    energy = (scalar_mass * scalar_mass + partner_mass * partner_mass) / (F(2) * scalar_mass)
    p0 = (momentum, F(0), F(0), momentum)
    pm = (energy, F(0), F(0), -momentum)
    dot = momentum * (energy + momentum)
    for polarization in (plus, cross):
        value = corner_d3(P, lc(p0, polarization), lc(pm, polarization))
        expected = F(28, 3) * dot
        assert value == (expected, F(0)), (value, expected)
    assert corner_d3(P, lc(p0, plus), lc(pm, cross)) == ZERO
    block = matrix(QQ, 6, 6, [
        QQ(corner_d3(P, gauge(p0, *left), gauge(pm, *right))[0].numerator)
        / QQ(corner_d3(P, gauge(p0, *left), gauge(pm, *right))[0].denominator)
        for left in pairs for right in pairs
    ])
    assert block.rank() == 5

print("INDEPENDENT_SAGE_LC_WARD_PASS")
print("LC_TT_KERNEL=(14/3)*(P_DOT_Q)*(H_DOT_K)")
print("GAUGE_GAUGE_RANK=5")
print("DISPOSITION=NONZERO_REPRESENTATIVE_WARD_REQUIRED")
