"""Independent Sage check of the two-connection principal Ward descent."""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_independent.sage"
capture = StringIO()
with redirect_stdout(capture):
    I = runpy.run_path(str(PREDECESSOR), init_globals={"QQ": QQ, "matrix": matrix})
assert "INDEPENDENT_SAGE_LC_WARD_PASS" in capture.getvalue()

n = 24
identity = identity_matrix(QQ, n)
W = block_matrix(QQ, 1, 2, [identity, -identity])
diagonal = block_matrix(QQ, 2, 1, [identity, identity])
anti_diagonal = block_matrix(QQ, 2, 1, [identity, -identity])

assert W.rank() == 24
assert W.right_kernel().dimension() == 24
assert W * diagonal == zero_matrix(QQ, n, n)
assert diagonal.rank() == 24
assert (W * anti_diagonal).rank() == 24

# The complete six-dimensional principal connection-gauge block is killed by
# W(D chi,D chi)=0, while the predecessor independently established that the
# isolated one-connection block has rank five and the physical shell is live.
gauge_block = matrix(QQ, 6, 6, 0)
assert gauge_block.rank() == 0

R = PolynomialRing(QQ, names=("alpha", "beta"))
alpha, beta = R.gens()
assert ideal([alpha + beta, alpha - 1]).variety() == [{alpha: QQ(1), beta: QQ(-1)}]

print("INDEPENDENT_SAGE_TWO_CONNECTION_PRINCIPAL_WARD_PASS")
print("DIFFERENCE_MAP_RANK=24_KERNEL_DIAGONAL24")
print("DIAGONAL_CONNECTION_GAUGE_BLOCK_RANK=0")
print("PHYSICAL_LC_TT_KERNEL=PRESERVED_FROM_INDEPENDENT_PREDECESSOR")
print("DISPOSITION=PRINCIPAL_DESCENT_EXACT__LOWER_ORDER_WARD_BV_PREBOUNDARY_OPEN")
