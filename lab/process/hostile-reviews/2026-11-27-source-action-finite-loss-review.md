# Internal T1 review: finite-loss completion classes

Basis: `523d8554d35825c9cbbba133aae9c42cbd9408cd`.

**PASS in the declared candidate/core/estimate class.** Two independent
specialists and one hostile reviewer accept the finite-loss packet theorem,
finite-order norm consequence and source-state custody. This is internal agent
review, not external peer review or full-PDE formalization.

## Critical proof checks

- Use the maximal real part of the FULL finite principal matrix. The owned
  spin7 block proves positivity but need not contain the maximizing eigenvector.
- The actual generator is classical order one on a non-null constant-rank cone.
  Finite Taylor expansion is controlled in global envelope Sobolev seminorms,
  including output tails, to logarithmic rescaled times. Corrections stay in a
  finite polynomial/derivative span of a compact smooth profile.
- All corrections grow at most exp(rho*tau) times a polynomial, even with Jordan
  blocks. Truncation leaves arbitrary chosen finite algebraic order. The two
  normalized estimate terms vanish for N=2ceil(ell)+2, c*rho=ceil(ell)+1.
- The tested forcing is the graph lift of the RANGE residual, not unweighted
  original PDE forcing. Parametrix errors can be placed beyond the chosen order.
  Microlocal support is asymptotic, not exact compact spatial and Fourier support.
- A locally bounded C0 realization agreeing on the smooth core paths supplies
  variation of constants. Finite Sobolev embeddings for paths, derivatives and
  graph residuals transfer it to the forbidden finite-loss estimate. Physical
  matter-source surjectivity and compact support preservation are not required.
- A finite-order elliptic parametrix does not establish global coercivity by
  itself. The stated sandwich bounds or their high-frequency version remain
  hypotheses. Arbitrary unbounded PT metrics, infinite-order weights, projections
  removing the channel and different boundary/Green problems are outside scope.
- SC-META52/53 leave upstairs boundary/shielding unresolved, not a source demand
  for unrestricted Cauchy data. Source dressing fixes Ahat; ordinary local gauge
  removal was already excluded. No invented odd action or BRST charge is made a
  prerequisite. Historical K77 fermion restrictions are not imported as K95
  bosonic physical selectors.

## Verification coverage

The lightweight --verify command passed in0.85s. It checks53 file bindings,
six inherited on-shell records, both exact400-term spectral moment/error sums,
28 scalar auxiliary inverse bounds and complete49,154 dimension custody,
four source polarity rows and universal loss-schedule algebra. It does NOT
rerun native matrix assembly, the preceding six-record native replay, or
verify analytic PDE remainder estimates. Reviewers independently read the
written proof and checked bound arithmetic/custody.

Six finite Lean lemmas passed a targeted single-thread compilation without
warnings/placeholders: formal coefficient residual order, universal exponent
schedule, logarithmic-power decay, shrinking time, vanishing-error contradiction
and norm-sandwich transfer. Supplying actual symbols, uniform remainders,
maximal-spectrum transport and graph/domain interpretations remains separate
written mathematics. No whole-project build or source theorem claimed.

### Independent PDE/source specialist

Receipt SHA256: `5d213bab61bcbf7f7fc287a49983ea5ad6344be2da9578b9e53a5e49015869e6`.

- Read final report in full, including global envelope/tail estimates, exact graph forcing, variation-of-constants hypotheses, local boundary corollary, asymptotic microlocal localization and source table. Source-return link correction confirmed.
- Independently checked classical-PDO scaling h=k^-1/2 and finite expansion: homogeneous symbol terms start at h^(2m); x/xi/time Taylor terms give polynomial differential corrections; finite smoothness jets and rapidly decreasing envelope tails suffice for each fixed requested order.
- Checked uniform remainder in global envelope Sobolev norms including off-support output. Proper-support, Fourier-tail and off-diagonal errors can be placed below any chosen finite order and carry the same exp(rho*tau) polynomial time envelope.
- Checked maximal FULL principal spectral abscissa selection, Jordan polynomial bound and triangular correction recurrence. Every correction stays in a finite polynomial/derivative span and has no exponential faster than exp(rho*tau). Maximal packets are not identified with prior current-visible signed-energy germs.
- Checked logarithmic observation time and universal loss schedule q=ceil(ell), c*rho=q+1, N=2q+2. Normalized initial and residual exponents are at most -1 and -3/2; physical residual k and time-integration k^-1 cancel. Different finite data/forcing losses and fixed negative/fractional Sobolev indices are covered.
- Checked reconstruction to exact primary constraints and all-finite-order graph norm transfer using injective symbol of JS. Residual is Jf=(f,-df) for range f=(partial_t-L)v; it is not unweighted full first-order equation forcing K_dt f.
- Checked finite Sobolev sandwich corollary and variation of constants: same-core smooth paths are C1 in Y and generator-continuous under upper embeddings. A locally bounded semigroup/evolution family would imply the prohibited finite-loss estimate. Physical matter-source surjectivity is not a premise.
- Checked local boundary corollary only when the domain retains compact interior graph paths and matching forcing; no finite propagation, global coercivity, unchanged supports of actual trajectories or arbitrary unbounded-PT theorem is claimed.
- Checked source custody independently against SC-META52/53, SC-GEO51, SC-GRP05, SC-GEO54/55, SC-OP04/05 and SC-META56. No unrestricted physical Cauchy requirement or supplied selector is inferred; fullU/optionalSp, K95/K77, independent bars, primary-minus and 2+1 distinctions remain explicit.
- Hashed final report/probe/manifest/lightweight verify receipt. All53 manifest file bindings match actual files; both stored intrinsic exact lower moments exceed19/80. Read verify PASS and its explicit flags that neither native assembly/replay nor the analytic remainder was executed by that check.

caveats: The theorem excludes every FIXED finite spatial derivative-loss local graph/Duhamel estimate only on the declared unrestricted compact non-null microlocal core and with the matching graph residual norm.; Norm exclusion requires explicit finite Sobolev upper/lower bounds, retention of the test core and the actual generator/variation-of-constants identity. Arbitrary unbounded/noncoercive PT metrics, infinite-order/exponential norms, projections, quotients and different boundary-selected cores are outside scope.; High-order packets are approximate solutions with controlled residuals. No exact exponentially growing solution, disappearance of analytic germs, nonlinear instability, forced negative-mode exchange or observed physical signal is proved.; The source does not require the tested unrestricted upstairs Cauchy completion. No source, physics-ledger, class-C, canon, paper or GU verdict changes.; The lightweight verification authenticates inherited inputs and scalar arithmetic. Native spectrum/full-M facts remain inherited; analytic PDE and norm-transfer arguments are written mathematical review, not machine-verified PDE theorems..

not_run: No native matrix assembly, former replay, inverse regeneration, probe execution, Lean compilation or heavy verification run by this reviewer.; No owner-repository edits. Six Lean checks are reported by the owner; this receipt does not claim reviewer execution or full-PDE Lean formalization..

### Independent algebra/operator specialist

Receipt SHA256: `366d6c49783b16c74dd189cd5b5194c4dad352d45d3958a9f264e9a8189e3ea8`.

- Read final report and independently checked maximum-full-spectrum packet choice, arbitrary finite-loss schedule, physical-time cancellation, and separation from earlier signed-energy/current germs.
- Proved the norm-sandwich transfer via variation of constants on C1 Y test paths, with generator continuity, actual graph residuals, local semigroup bounds, and loss a+b at index -a.
- Checked the original forcing is the graph lift (f,-df) of the range residual; no identification with unweighted original-PDE forcing or physical matter-source surjectivity.
- Checked boundary/core qualifications and the distinction between finite-order ellipticity, a parametrix estimate with remainder, and global low-frequency coercivity.
- Hashed report, probe, manifest, lightweight verify receipt, and all 53 manifest-bound native files.
- Independently decoded and authenticated all six inherited on-shell bundle records and recomputed both exact 20x20 intrinsic trace-square centers and error sums (400 product terms per root), zero center traces, and strict lower bounds greater than 19/80.
- Independently authenticated 14 full-auxiliary bundles and checked all 28 rational scalar Neumann sums, root-radius perturbation formulas, certificate dimensions/hashes, and 25082+24072=49154 dimension accounting.
- Checked the five stored rational loss-schedule controls and the universal algebraic exponents -delta-1 and -delta-3/2 for delta=ceil(ell)-ell>=0.
- Verified the supplied lightweight receipt reports PASS for two intrinsic roots, 28 scalar bounds, and the complete 49154-dimensional time kernel, and binds the current probe and manifest.

caveats: Acceptance is the stated actual-candidate finite-loss graph/completion theorem on the unchanged non-null compact microlocal core, not GU falsification or a source-mandated physical Cauchy-domain claim.; The field named replay_sha256 binds a lightweight custody/scalar verification receipt; it is not a new native matrix replay or PDE verification.; Native ranks, complete-carrier construction, whole-family reflection trace-zero proof, matrix inverse defects, and prior native replays are inherited at their previously reviewed scope.; The classical-PDO remainder and graph-transfer analysis are written mathematical arguments, not certified by the scalar probe or the finite Lean core.; No exclusion of infinite-order/analytic weights, projections or quotients removing the tested core, different time-boundary/Green problems, or unspecified physical state spaces is asserted.; No exact exponentially growing solution, negative-energy exchange, Ward-nontrivial coupling, nonlinear instability, or physical observed signal is established here..

not_run: No native operator assembly, inverse regeneration, carrier/rank construction, heavy native replay, or PDE simulation.; Did not execute the reviewed probe; independent standard-library file/hash/Fraction checks only.; Did not rerun Lean or repository gates; six Lean passes are supplied owner evidence.; No owner-repository files modified..

### Hostile reviewer

Receipt SHA256: `3a60a4f193f704c971400aed6c2de1951f3f0db445d34efa41f4d43f956530d5`.

- Independent written review of finite-order classical-PDO coherent packet expansion with global envelope/tail control uniform to c log k.
- Checked use of maximal full principal spectral abscissa, finite-dimensional Jordan polynomial control, correction recursion, nonvanishing leading packet and loss-dependent order-of-limits argument.
- Checked exact universal loss-schedule algebra, physical residual/integration k-factor cancellation, and all stored rational arithmetic controls.
- Checked graph reconstruction for states and range residuals, arbitrary smoothing order for each finite loss, and same-core Sobolev-sandwich implication.
- Checked final asymptotic-cone, C1 smooth-path/semigroup, no physical source-surjectivity, boundary-condition and elliptic low-frequency qualifications.
- Read SC-META-52/53 source claims and authenticated all four source-polarity record hashes; the tested core is not a source-required domain.
- Authenticated all 53 referenced current files, final probe/certificate/verify receipt and separately accepted actual-symbol/full-M custody.
- Checked both inherited exact intrinsic lower bounds exceed 19/80 and all 28 inherited complete-M scalar bounds lie in [0,1), without regenerating native matrices.

caveats: The analytic packet remainder and graph theorem are independently reviewed mathematics, not verified by the lightweight probe or the finite Lean core.; Exclusion applies to every fixed finite spatial-loss graph Duhamel estimate and norms with the stated finite Sobolev sandwich on the unchanged compact microlocal core and graph forcing identity.; No exact exponentially growing solutions or current coupling of the maximal full-spectrum packet are constructed.; Infinite-order norms, non-elliptic channel deletion, quotients, source-selected boundary/Green domains and physical cohomology can fall outside the tested class; their success or failure remains undetermined.; No source-required unrestricted Cauchy domain, physical ghost, GU/class-C falsification, new choice family or source/ledger verdict follows..

not_run: Native operator assembly, eigenvalue search, basis/rank regeneration or dense inverse defects; Prior six-record native replay (authenticated accepted artifact custody); Lean build (six targeted lemmas reported PASS by parent; not rerun); PDE simulation or external peer review.

## Reproduction

From the repository root, using Python standard library only:

```sh
python3 tests/program-focus/source_action_finite_loss_probe.py --verify
```

This is a read-only exact input/certificate verifier, not a PDE solver.
Optional --output writes its receipt to the requested path. --write-certificate
is the producer mode and is not an inspection command.

## Claim ceiling

A class of same-core candidate completions is excluded. Source-required GU,
whole classC, a negative-norm physical particle, exact growing solutions,
nonlinear exchange and observed instability are not established. Analytic,
infinite-order, nonlocal or properly restricted physical domains remain
undetermined. No choice, obligation or prediction credit, source/physics/canon
verdict, governance or schedule changes. Nov26g remains proposal-only.

## Accepted artifact bindings

- report_sha256: `95e8994a935195b57ddeabfdd1ed9f7a7022eec85a8eeaef0b69b01495af0485`.
- probe_sha256: `eb9ba01f3028463a24cbffde955c69f8b0e390fef4541c382fe3e3a0e2d004d8`.
- manifest_sha256: `d46d7216d814a872167eb0471747986622b84eebaa57b3f99c9733486a993507`.
- replay_sha256: `71fa86ef197da93365d7385ea461beb0b6e44809854078ba1171ea06e7600735`.
- Lean source SHA256: `27ac2ac097724d1fdd9218764ebc18ee17e51d52b562ca928defa3f2d362a5cb`.
