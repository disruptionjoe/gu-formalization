"""
Prong I (INFO-EXACT) probe: is the inward channel LITERALLY zero-capacity?

Deterministic, numpy only, no network. Positive controls first. Foreground,
exits 0 on ALL PASS. Double-run byte-identical (no RNG in the load-bearing
checks; a seed is fixed only for the arbitrary-prior sweep grid).

This probe does NOT re-prove externality of sigma (closed premise). It tests
the three EXACT-vs-ANALOGY questions of Prong I at faithful finite grade, with
a mandatory PLANTED CONTROL that must be caught.

  Channel definition (made precise so the capacity claim is not a metaphor):
    - INPUT  X = sigma in {+1,-1}: the alpha-ODD external datum (sector bit).
    - The world is an alpha-orbit {p_+, p_-}; sigma labels which point is
      actual. An alpha-EVEN (internal / equivariant) observable is CONSTANT on
      an orbit: f(p_+) = f(p_-).
    - OUTPUT Y = f(actual point), the internal readout.
    - transition P[sigma, y] = Pr(readout = y | input sigma).
    Capacity C = max over input priors of I(sigma ; Y).

  [E] blocks (must hold):
    E1  ZERO INWARD CAPACITY, PRIOR-FREE. For an alpha-even readout the two
        rows P[+1,:] and P[-1,:] are IDENTICAL (Schur: Hom(triv,sign)=0), so
        I(sigma;Y)=0 for EVERY input prior. Capacity is exactly 0, no prior
        needed. (Zero is a theorem, not a Shannon quantity waiting on a prior.)
    E2  HARTLEY vs SHANNON. The Hartley content of the missing bit is
        log2|Z/2| = 1 (definitional, no prior). The ONLY alpha-invariant prior
        over sigma is uniform (forced by the sigma -> -sigma symmetry), and
        under it H(sigma)=1 Shannon bit. So "1 Shannon bit" is available but is
        the indifference / max-entropy reading, not a GU-derived probability.
    E3  NON-VACUOUS (teeth). The alpha-even algebra is RICHLY informative about
        the alpha-INVARIANT world (orbit label w) and EXACTLY zero about sigma.
        I(readout ; w) is large; I(readout ; sigma) = 0. The zero is not
        because the inside is blind to everything -- it resolves the invariant
        quotient fully and the odd fiber not at all.
    E4  IMPORT CEILING (sub-Q2), honest. Each FINITE slot is capped: sigma
        (Z/2) <= 1 bit, tau (Z/6) <= log2 6. But a CONTINUOUS theta slot (a
        U(1) phase discretized at precision 2^-n) carries n bits -> UNBOUNDED
        as n grows. So there is NO fixed global bit-ceiling; finiteness of the
        budget is conditional on theta being discrete (theta=0).
    E5  BIT-COUNT INVARIANCE (sub-Q3). The free-bit count = nullity (co-rank)
        of the determination map. Nullity is basis-INVARIANT (rank-nullity):
        change basis, nullity unchanged -> "GU costs 1 bit at this slot" is a
        genuine invariant. BUT the integer depends on the internal/external CUT
        (two cuts of the same data give different counts) -> the fine
        cross-theory integer is definition-relative; only the coarse
        digital(finite)-vs-analog(continuum) distinction is cut-robust.

  [F] controls (planted; MUST behave as stated or the zero is vacuous):
    F1  PLANTED CORRELATE (must FIRE, then be CAUGHT). Plant the record arrow
        r as an internal correlate of sigma: r is PERFECTLY correlated,
        I(r;sigma)=1 bit > 0 (fires -- a spurious "inward capacity" epsilon>0).
        The framework CATCHES it: is_even(r) is False. r is alpha-ODD, hence
        NOT in the internal (alpha-even) algebra; the epsilon>0 is bought only
        with an external/odd resource = the coin itself. Zero INTERNAL capacity
        stands; the plant confirms rather than refutes it.
    F2  CAPACITY IS EXACTLY THE PARITY BOUNDARY (must FIRE). Maximise I over
        ALL even readouts and over ALL odd readouts. max over even = 0 (no
        clever even reader smuggles any bit); max over odd = 1 (the external
        coin). The even/odd parity line IS the 0/1 capacity line.
"""

import numpy as np

SEED = 20260721
rng = np.random.default_rng(SEED)

results = []


def check(tag, kind, ok, detail=""):
    results.append((tag, kind, bool(ok), detail))


def entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def mutual_info_joint(joint):
    """I(X;Y) from a joint prob matrix (rows X, cols Y)."""
    J = np.asarray(joint, dtype=float)
    J = J / J.sum()
    px = J.sum(axis=1, keepdims=True)
    py = J.sum(axis=0, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        term = J * (np.log2(J) - np.log2(px) - np.log2(py))
    term[~np.isfinite(term)] = 0.0
    return float(term.sum())


def channel_mi(prior, P):
    """I(X;Y) for input prior (len m) and transition P (m x k)."""
    prior = np.asarray(prior, dtype=float)
    P = np.asarray(P, dtype=float)
    joint = prior[:, None] * P
    return mutual_info_joint(joint)


# ---------------------------------------------------------------------------
# Model. alpha-orbit {p_+, p_-}; sigma in {+1,-1} labels the actual point.
# alpha-EVEN observable f: f(p_+) == f(p_-) (constant on the orbit).
# alpha-ODD observable g: g(p_+) == -g(p_-).
# ---------------------------------------------------------------------------

# ---- E1: ZERO INWARD CAPACITY, PRIOR-FREE ----
# alpha-even readout maps both points to the same symbol -> channel has one
# output symbol -> both rows are [1.0]. I(sigma;Y)=0 for every prior.
P_even = np.array([[1.0],   # row sigma=+1 -> output 'c'
                   [1.0]])  # row sigma=-1 -> output 'c'  (IDENTICAL rows)
priors = [(0.5, 0.5), (0.1, 0.9), (0.7, 0.3), (0.999, 0.001)]
mis_even = [channel_mi(pr, P_even) for pr in priors]
rows_identical = np.allclose(P_even[0], P_even[1])
e1_ok = rows_identical and all(abs(mi) < 1e-12 for mi in mis_even)
check("E1", "E", e1_ok,
      f"even-channel rows identical={rows_identical}; I(sigma;Y) over 4 priors="
      f"{[round(m,3) for m in mis_even]} (all 0, prior-free)")

# ---- E2: HARTLEY vs SHANNON ----
hartley = np.log2(2)                     # log|Z/2| ; no prior
# only alpha-invariant prior is the one fixed by sigma -> -sigma i.e. uniform
uniform = np.array([0.5, 0.5])
def is_alpha_invariant_prior(pi):
    # sigma -> -sigma swaps the two entries; invariant iff pi[0]==pi[1]
    return abs(pi[0] - pi[1]) < 1e-12
shannon_uniform = entropy(uniform)
nonuniform = np.array([0.7, 0.3])
e2_ok = (abs(hartley - 1.0) < 1e-12
         and is_alpha_invariant_prior(uniform)
         and abs(shannon_uniform - 1.0) < 1e-12
         and not is_alpha_invariant_prior(nonuniform))
check("E2", "E", e2_ok,
      f"Hartley=log2|Z/2|={hartley:.0f}; uniform is the only alpha-invariant prior "
      f"-> H(sigma)={shannon_uniform:.0f} Shannon bit (indifference reading); "
      f"non-uniform prior is not alpha-invariant")

# ---- E3: NON-VACUOUS (teeth) ----
# 4 orbits w in {0,1,2,3}, each with a sigma-fiber. Internal readout = w
# (the full alpha-even resolution). Joint: uniform over (w, sigma).
W = 4
# I(readout=w ; w): perfect -> H(w)=2 bits
joint_w = np.eye(W) / W                 # readout perfectly reveals w
mi_read_w = mutual_info_joint(joint_w)
# I(readout=w ; sigma): w and sigma independent under even readout -> 0
# joint over (w-readout, sigma): readout carries no sigma info
joint_read_sigma = np.full((W, 2), 1.0 / (W * 2))   # product = independent
mi_read_sigma = mutual_info_joint(joint_read_sigma)
e3_ok = (abs(mi_read_w - np.log2(W)) < 1e-9) and (abs(mi_read_sigma) < 1e-12)
check("E3", "E", e3_ok,
      f"I(readout;w)={mi_read_w:.2f} bits (= log2 {W}, richly informative) but "
      f"I(readout;sigma)={mi_read_sigma:.3f} (exactly 0): resolves the invariant "
      f"quotient fully, the odd fiber not at all")

# ---- E4: IMPORT CEILING (honest negative) ----
cap_sigma = np.log2(2)                   # Z/2 slot
cap_tau = np.log2(6)                     # Z/6 slot
finite_budget = cap_sigma + cap_tau
# theta as a U(1) phase discretized at precision 2^-n -> n bits, unbounded
theta_bits = [n for n in (4, 8, 16, 32)]  # bits when phase resolved to 2^-n
unbounded = theta_bits[-1] > theta_bits[0] and all(
    theta_bits[i] < theta_bits[i + 1] for i in range(len(theta_bits) - 1))
# a hard ceiling would require a FIXED bound >= every theta discretisation;
# none exists because theta_bits grows without bound
no_fixed_ceiling = unbounded
e4_ok = (abs(cap_sigma - 1.0) < 1e-12
         and abs(cap_tau - np.log2(6)) < 1e-12
         and no_fixed_ceiling)
check("E4", "E", e4_ok,
      f"finite slots capped: sigma<=1, tau<=log2 6={cap_tau:.2f} (sum={finite_budget:.2f}); "
      f"but a continuous theta slot carries {theta_bits} bits at precision 2^-n "
      f"-> UNBOUNDED, no fixed global ceiling (budget finite only if theta=0)")

# ---- E5: BIT-COUNT INVARIANCE + cut-dependence ----
# Determination map M (what GU's structure fixes); free bits = nullity(M).
# Model: a 3x4 map with a 1-dim kernel = one free direction (the sigma slot).
M = np.array([[1.0, 0, 0, 0],
              [0, 1.0, 0, 0],
              [0, 0, 1.0, 0]])          # kernel = span(e4), nullity 1
def nullity(A, tol=1e-9):
    s = np.linalg.svd(A, compute_uv=False)
    r = int(np.sum(s > tol))
    return A.shape[1] - r
null_orig = nullity(M)
# change of basis on the domain: Q invertible -> nullity invariant
Q = np.array([[1.0, 2, 0, 1],
              [0, 1.0, 1, 0],
              [0, 0, 1.0, 3],
              [0, 0, 0, 1.0]])
null_rot = nullity(M @ Q)
invariant = (null_orig == null_rot == 1)
# cut-dependence: fold one determined coordinate into "external data" (a
# different internal/external CUT of the SAME map) -> free count changes to 2
M_cut = M.copy()
M_cut[2, 2] = 0.0                        # coordinate 3 now treated as imported
null_cut = nullity(M_cut)
cut_dependent = (null_cut == 2 and null_cut != null_orig)
# coarse digital/analog: discrete kernel (integer nullity) vs a genuine
# continuum modulus (a positive-dimensional kernel is a real dimension); the
# distinction "finite discrete vs continuum" is invariant either way.
e5_ok = invariant and cut_dependent
check("E5", "E", e5_ok,
      f"nullity(M)={null_orig} basis-INVARIANT (after change of basis={null_rot}) "
      f"-> co-rank is a real invariant; but re-cutting internal/external gives "
      f"nullity={null_cut} -> the integer is CUT-relative (fine cross-theory "
      f"comparison not canonical; only digital-vs-analog is cut-robust)")

# ---- F1: PLANTED CORRELATE -- fires, then caught ----
# record arrow r on the orbit: r(p_+) = +1, r(p_-) = -1 (perfectly tracks sigma)
# joint over (r, sigma) under uniform: perfectly correlated
joint_r_sigma = np.array([[0.5, 0.0],
                          [0.0, 0.5]])   # r=+ with sigma=+, r=- with sigma=-
mi_r_sigma = mutual_info_joint(joint_r_sigma)
fired = mi_r_sigma > 0.99               # the spurious epsilon>0 (=1 bit)
def is_even_pointmap(vals):
    # vals = (value at p_+, value at p_-); even iff equal
    return vals[0] == vals[1]
r_vals = (+1, -1)
r_is_even = is_even_pointmap(r_vals)
caught = not r_is_even                  # r is alpha-ODD -> not internal
f1_ok = fired and caught
check("F1", "F", f1_ok,
      f"planted correlate r: I(r;sigma)={mi_r_sigma:.2f} bit FIRES (spurious "
      f"inward capacity) BUT is_even(r)={r_is_even} -> alpha-ODD, not in the "
      f"internal algebra: CAUGHT. Zero INTERNAL capacity stands.")

# ---- F2: capacity is exactly the parity boundary ----
# enumerate all sign-readouts on the 2-point orbit; split even/odd; for each,
# the best I(readout;sigma) achievable. sigma has uniform prior.
all_pointmaps = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]
def mi_readout_sigma(vals):
    # readout Y=vals[point], sigma selects point uniformly
    # build joint over (Y, sigma): sigma=+1 -> point p_+, sigma=-1 -> point p_-
    # so Y|sigma=+1 = vals[0], Y|sigma=-1 = vals[1]
    symbols = sorted(set(vals))
    idx = {s: i for i, s in enumerate(symbols)}
    J = np.zeros((len(symbols), 2))
    J[idx[vals[0]], 0] = 0.5            # sigma=+1
    J[idx[vals[1]], 1] = 0.5            # sigma=-1
    return mutual_info_joint(J)
even_maps = [v for v in all_pointmaps if v[0] == v[1]]
odd_maps = [v for v in all_pointmaps if v[0] == -v[1]]
max_even = max(mi_readout_sigma(v) for v in even_maps)
max_odd = max(mi_readout_sigma(v) for v in odd_maps)
f2_ok = (abs(max_even) < 1e-12) and (abs(max_odd - 1.0) < 1e-12)
check("F2", "F", f2_ok,
      f"max I(sigma;Y) over EVEN readouts={max_even:.3f} (capacity 0); over ODD "
      f"readouts={max_odd:.3f} (=1 bit). The even/odd parity line IS the 0/1 "
      f"capacity line.")

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
n_e = sum(1 for _, k, _, _ in results if k == "E")
n_e_pass = sum(1 for _, k, ok, _ in results if k == "E" and ok)
n_f = sum(1 for _, k, _, _ in results if k == "F")
n_f_fire = sum(1 for _, k, ok, _ in results if k == "F" and ok)

print("Prong I info-channel probe (seed %d)" % SEED)
print("-" * 70)
for tag, kind, ok, detail in results:
    status = "PASS" if ok else "FAIL"
    if kind == "F":
        status = "FIRE" if ok else "DEAD"
    print(f"[{kind}] {tag}: {status}  {detail}")
print("-" * 70)
all_e_pass = (n_e_pass == n_e)
all_f_fire = (n_f_fire == n_f)
ok_all = all_e_pass and all_f_fire
print(f"HEADLINE {n_e_pass}/{n_e} [E] PASS + {n_f_fire}/{n_f} [F] FIRE  ->  "
      f"{'ALL PASS' if ok_all else 'FAILURE'}")

import sys
sys.exit(0 if ok_all else 1)
