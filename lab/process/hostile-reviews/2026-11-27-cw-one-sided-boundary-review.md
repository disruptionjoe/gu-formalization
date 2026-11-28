# One-sided CW boundary internal T2 review

Independent reviewers accepted the frozen actual descriptor, packet and forward-time argument. Contributors do not count as acceptance reviewers. Root46exactcontrols pass. No new Lean or full nonlinear/physical/source claim.

## Frozen artifacts

- explorations/conditional-build/cw-one-sided-boundary-2026-11-27.md: `220b44e29aa64ba32906141215dc17c77d3d08005117bc90ac6566dd5d3cdc05`
- tests/program-focus/cw_one_sided_boundary_probe.py: `856bf6d0bd3bd5f387b20f404c0e7aeb5d3010a4bcebcfc04d7c4db5a8fc1266`
- lab/process/cw-one-sided-boundary-certificates.json: `f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2`

## metric_family_second_review

{
  "accepted": true,
  "blockers": [],
  "reviewer": "metric_family_second_review",
  "tier": "T2 independent mathematical/PDE review",
  "basis": "23b22b482fcd0aab12ccafdb538b08ca6dc6f156",
  "artifact_hashes": {
    "explorations/conditional-build/cw-one-sided-boundary-2026-11-27.md": "220b44e29aa64ba32906141215dc17c77d3d08005117bc90ac6566dd5d3cdc05",
    "tests/program-focus/cw_one_sided_boundary_probe.py": "856bf6d0bd3bd5f387b20f404c0e7aeb5d3010a4bcebcfc04d7c4db5a8fc1266",
    "lab/process/cw-one-sided-boundary-certificates.json": "f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2"
  },
  "findings": [
    {
      "topic": "Genuinely changed premise",
      "finding": "Accepted. The future boundary relation retains independent decaying off-band state. It is not an instantaneous elimination graph over CW-only data and does not contradict the prior C2 ordinary-Sobolev graph exclusion."
    },
    {
      "topic": "Actual singular descriptor reduction",
      "finding": "Accepted. Analytic division of the owned two-sided inverse by z^2-delta gives the paired polar part U+zV. On the finite Weierstrass block, Pi=V A_t and N=U A_t obey Pi^2=Pi, N^2=delta Pi, Pi V=V and NV=U; additionally VC=-N yields the forced equation x_prime=Nx-VF. No inverse of singular A_t is required. This is a general regular-pencil argument applied to the authenticated native scalarizer, not merely the scalar calibration."
    },
    {
      "topic": "Whole threshold cluster and complementary equations",
      "finding": "Accepted. Extending every ker C vector to a temporal chain, while the scalar annihilator excludes length greater than two, excludes isolated Jordan1 blocks. The smooth (N e_j,e_j) frame therefore covers every threshold channel. The analytic/complementary forced piece H(i nu,K)F is retained and is regular on the held phase patches; the report does not discard algebraic rows or claim closure at all generated outputs."
    },
    {
      "topic": "Actual forcing and finite controls",
      "finding": "Accepted. The native left row gives ell_b F=104448 and ell_b UF=626688. The new sparse first temporal jet correctly computes the polynomial scalarizer modulo z^2, because q and R(q) have zero first derivative at z=0. The certificate records C0 UF=0, C0 VF+A_t UF=0, 30 UF terms, 19 VF terms and ell_b VF/6=0. The report appropriately retains both forcing components in the general boundary formula."
    },
    {
      "topic": "Boundary sign and regular coordinates",
      "finding": "Accepted. For q_prime=p-g0 and p_prime=lambda^2 q-g1, b=p+lambda q obeys b_prime=lambda b-(g1+lambda g0). Future tuning yields the stated positive Laplace integral and divisor lambda-i nu. q0 remains free with decaying slope -lambda q0; use of a singular individual growing projector is unnecessary."
    },
    {
      "topic": "Fixed-packet threshold estimate",
      "finding": "Accepted. The nonzero relative-phase derivative supplies smooth compact coarea densities. Subtracting an even cutoff times rho(0) gives a uniformly bounded Cauchy integral and the stated delta/PV limit. All full-frame coefficients are smooth, so the argument covers the actual vector forcing and gives Fourier-local L2 through the threshold."
    },
    {
      "topic": "Forward-uniform estimate",
      "finding": "Accepted. On the small nonstationary patches the fixed smooth amplitudes give uniformly Schwartz time forcing. Fubini bounds the L1 norm of b by the first time moment of h=g1+lambda g0. The damped equation q_prime=-lambda q+b-g0 then gives the stated bound uniformly for lambda tending to zero and t>=0. The q0=0 response is bounded; arbitrary locally L2 free q0 yields a uniform Fourier-local L2 bound, not necessarily a pointwise bound. The final headline now states that distinction."
    },
    {
      "topic": "Counterexamples and remaining topology",
      "finding": "The constant plane-character secular response remains valid because its forcing lacks the required time moment. Constants in the packet estimates depend on Fourier derivatives and may diverge when packets concentrate. Consequently neither a uniform ordinary-Sobolev bilinear bound nor a nonlinear invariant manifold follows. The report preserves these limits."
    },
    {
      "topic": "Source and physical claim ceiling",
      "finding": "Accepted as an internal conditional GU* component survivor for the selected frozen low-Phi K95 printed realization and isolated output collar. SC-ACT-02 supplies an endpoint template, while SC-META-52/53 do not select this future law, topology or physical state. There is no source-GU verdict, all-class-C theorem, wedge-action transfer, physical positive energy or prediction claim."
    }
  ],
  "qualifications": [
    "The mathematical descriptor/coarea/time-moment arguments are written proofs reviewed here, not fully Lean-formalized.",
    "The certificate reports 46 exact controls; I authenticated its producer and 13 dependency hashes and inspected the code, but did not rerun any control.",
    "Acceptance is limited to the frozen report scope. Uniform data-space bounds, nonlinear interactions with the free decaying states, all-output closure and a source-selected physical law remain open."
  ],
  "review_method": "Independent read-only specialist analysis of the report, probe, certificate, existing full-system and nonlinear CW proofs, owner instructions, program_focus, geometer/source-native routing and SC-ACT-02/SC-META-52/SC-META-53. Independently derived the finite-pencil projection and boundary estimates and challenged the strongest threshold and forward-time claims. Only read/hash operations and this scratch receipt were performed; no tests, builds, owner edits or external effects.",
  "reviewer_scope": "Independent reviewer, not a contributor to the candidate derivation. Mathematical acceptance of the exact three frozen artifacts; no governance or ledger change.",
  "administrative_amendment": {
    "change": "Four body metadata lines for the legacy program_focus parser, plus their separating blank line.",
    "prior_report_sha256": "21de3ac1b91f4529c9a7b517f1422bb12df8dfbd69e7a1a5de011fa19804d129",
    "new_report_sha256": "220b44e29aa64ba32906141215dc17c77d3d08005117bc90ac6566dd5d3cdc05",
    "verification": "Removing exactly that insertion reproduces the previously accepted report hash. Probe and certificate hashes unchanged. No scientific change; acceptance retained."
  }
}

## Independent review

{
  "accepted": true,
  "reviewer_role": "Independent hostile T2 mathematical and source-scope reviewer; not an author or contributor to this wave",
  "reviewer_scope": "Read-only review of the frozen report, probe and certificate, prior owned CW/no-go scope, and source-native rules. Internal agent acceptance for the stated T2 result only.",
  "basis": "23b22b482fcd0aab12ccafdb538b08ca6dc6f156",
  "blockers": [],
  "artifact_hashes": {
    "explorations/conditional-build/cw-one-sided-boundary-2026-11-27.md": "220b44e29aa64ba32906141215dc17c77d3d08005117bc90ac6566dd5d3cdc05",
    "tests/program-focus/cw_one_sided_boundary_probe.py": "856bf6d0bd3bd5f387b20f404c0e7aeb5d3010a4bcebcfc04d7c4db5a8fc1266",
    "lab/process/cw-one-sided-boundary-certificates.json": "f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2"
  },
  "findings": [
    "The regular-pencil reduction preserves the singular time matrix. The polar part gives Pi=V At and N=U At, with N^2=delta Pi and NV=U; the forcing equation x_prime=Nx-VF has the correct sign. The analytic/complementary forced response is explicitly reconstructed rather than silently discarded.",
    "The inherited length-two threshold-chain argument supports a regular full-cluster (Ne,e) frame. The result is not inferred solely from a scalar receiver or from the small descriptor control.",
    "The sparse first temporal jet of the scalarizer is correctly formed at delta=0: q=36-z^2 has no first-order z term. Static code inspection preserves P0/At order in the derivative recurrence. The stored native controls bind C0 UF=0 and C0 VF+At UF=0, receiver UF/6=104448 and VF/6=0 to the previously authenticated actual force.",
    "The future no-growth condition for b=p+lambda q is b(t)=integral_t^infinity exp(-lambda(s-t)) (g1+lambda g0)(s) ds. The free decaying q0 is retained. This is not retarded zero-data evolution and does not select a unique history.",
    "The nonstationary relative phase on the sufficiently small held compact patches provides uniform smooth coarea densities and rapid time decay for each fixed smooth input pair. The Cauchy boundary kernel has a finite one-sided limit; it is distinct from the earlier frequency-locked 1/(delta+nu^2) inverse.",
    "The first-time-moment bounds establish uniform forward-time bounds for the forced representative through lambda=0. Arbitrary locally L2 free q0 preserves a uniform local L2 bound, but need not be pointwise bounded. The final headline states this distinction correctly.",
    "The old C2 instantaneous graph exclusion is retained honestly: the new affine boundary relation has independent off-band state and future forcing data, so it is outside the old elimination hypothesis.",
    "SC-ACT-02 supplies an endpoint template; SC-META-52 and SC-META-53 retain their UNCERTAIN boundary/physical-space status. Neither they nor SC-ACT-06 select this realization, future prescription, positive norm or physical state space. K95, W2, corrected wedge and source-GU remain distinct."
  ],
  "own_checks": [
    "Read the complete final report and probe, including the administrative body metadata mirror and revised forced-versus-free-data headline.",
    "Checked future-condition signs, regular-frame reconstruction, coarea cancellation, first-time-moment estimates, realification scope and the distinct hypothesis of the prior graph exclusion by mathematical reasoning.",
    "Read relevant AGENTS, program_focus, source-native routing, GEOMETER T11/T13/T15, and source-register SC-ACT-02/06 and SC-META-52/53.",
    "Authenticated all three frozen SHA256 values, certificate producer binding, 46 named stored controls and all 13 pinned dependency hashes using file reads only."
  ],
  "cautions": [
    "The accepted result concerns the isolated cross-output collar and selected frozen printed P,Q at quadratic order. It does not establish closure for all pair outputs, interaction with arbitrary free decaying states, curved geometry or a nonlinear invariant domain.",
    "Constants depend on Fourier derivatives of the held smooth input amplitudes. No uniform bilinear estimate on ordinary Sobolev/L2 inputs, continuous nonlinear state manifold or all-data well-posedness is accepted.",
    "The bounded complementary particular solution is an existence construction; arbitrary complementary growing homogeneous data are not asserted to remain bounded.",
    "Future no-growth is a tested mathematical prescription, not source-derived causality, a physical Hilbert/BRST quotient, positive energy, a selected observed history or GU viability.",
    "No physical choice family is adopted by this comparison. A future adoption would need explicit topology, boundary law and off-band-state specification; current historical choice-budget accounting is not evidence that these requirements are source supplied.",
    "Finite controls calibrate and bind the native algebra but do not formalize the general pencil/coarea/PDE proof. This is internal review, not independent external validation."
  ],
  "not_run": [
    "No probe execution, symbolic/native operator recomputation, shell census, dense projector assembly, Lean build, test suite or process gate was run by this reviewer.",
    "No repository-owner artifact was edited; only this scratch receipt was written."
  ]
}
