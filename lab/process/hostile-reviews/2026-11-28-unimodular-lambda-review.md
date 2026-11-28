# Unimodular Lambda internal T1 review

Two independent specialists and separate hostile review accepted the frozen source/variation and full-row scalar proof. Contributors were not acceptance reviewers. Root ran43 exactcontrols/replay and7finiteLeancores. Full geometric/PDE and source results remain written proofs, not fully Lean-formalized.

Source correction before acceptance: SC-COS52 is separately pinned to UCSD, rather than grouped with TOE. Finite threshold probe corrected a factor2 translation before certification.

## Frozen artifacts

- explorations/conditional-build/unimodular-lambda-and-scalar-2026-11-28.md: `471a58179b2f6b8551a422256789b856f689b6fe80231a827a51daabfcbd9ea6`
- tests/program-focus/unimodular_lambda_probe.py: `0f1a0a4f4b58bf0899a8084e80bb7e91578db1c7242b3f74e6ac70bc9cf0d4c7`
- lab/process/unimodular-lambda-certificates.json: `1d0b93842b00a49a047d48165f5c6d40caa55c50fda2f56a0cac276eb34e2307`
- Lean/GUFormalization/UnimodularLambda.lean: `828a4930f2bb108dbad18de6c16a984b00e51a914d9ee502f684e5ef6d2db10f`

## Independent review

{
  "reviewer_role": "Independent mathematical acceptance review; read-only contributor boundary",
  "accepted": true,
  "blockers": [],
  "review_scope": "Written variational and differential-geometric argument, exact-probe implementation and certificate consistency, and the scope of seven finite Lean statements. Acceptance is for the declared constant-coefficient four-dimensional local real metric class.",
  "findings": [
    "For the complete diffeomorphism-invariant constant-coefficient metric action, Noether conservation and E_TF=0 imply dT=0 and E=ell*g on each connected component. The c_eff=c+2*ell sign is correct under the stated inverse-metric Euler convention.",
    "The four-dimensional trace is 6*b*box(R)-A*R-2*c. Both quadratic Euler tensors vanish on an Einstein metric, including nonzero Weyl backgrounds. Consequently A!=0 fixes Lambda=-c/(2*A); a continuum at unchanged coefficients requires A=c=0.",
    "The metric path has determinant -exp(6*H*t) exactly and a tracefree tangent. Retaining N=(1+epsilon*q)^(-3/2) gives deltaH=(qdot+3*H*q)/2 and deltaR=3*(qddot+7*H*qdot+12*H^2*q). Dropping the lapse would change both the geometric calculation and constraint interpretation.",
    "The Ricci-squared/Weyl/Euler decomposition legitimately reduces every row on this Weyl-flat FLRW path to f(R). The probe computes the temporal and spatial rows from arbitrary-lapse Ricci and scalar Hessian expressions before substituting the mode; isotropy and homogeneity force all other rows to vanish.",
    "The positive dispersion root r and normalized q satisfy both full linearized metric rows without division by F0. This includes F0=0, where r=H and q=exp(H*t)/(60*H^2). The critical conformal control also works: deltaR=-3*(box+4*H^2)*psi=exp(H*t), and D(deltaR)=0.",
    "The critical conformal representative and the fixed-density tangent differ by a local diffeomorphism: one can take xi^0=(q-psi)/(2*H), xi^i=0. Nonzero deltaR cannot itself be pure gauge because the background scalar curvature is constant.",
    "The negative scalar mass and positive-F0 growth inequalities have the stated signs. Pure quadratic, b=0 Einstein, positive-mass R+R^2, critical-F0 and lapse-omission cases are meaningful countercontrols. A growing local curvature mode survives throughout the stated de Sitter family.",
    "With a conservation defect, E_TF=0 gives d ell=j. Closedness is necessary locally; global exactness requires vanishing periods. The externally held scalar-coefficient spurion identity has the correct minus-one-half sign. Its c(x) control demonstrates why tracefree stationarity alone does not yield a constant multiplier."
  ],
  "caveats": [
    "This review does not assert a source-required GU unimodular law, a finite native 14D reduction, a physical observer quotient, positive norm, spatial normalizability, nonlinear stability or a prediction of the observed cosmological constant.",
    "The exact path is a path of admissible metrics; only its tangent is proved to solve the linearized field equations. The growing solution is admitted in the explicitly stated ordinary local real solution class. Different global or physical state restrictions require their own analysis.",
    "Lean formalizes seven finite algebraic/order cores only. The Noether, differential-geometric and solution-domain arguments remain written proofs reviewed here. This is internal agent review, not external expert certification or full PDE formalization.",
    "Per the assigned serialization boundary, I did not rerun the symbolic suite or Lean build. I inspected their complete sources, the 43-check certificate and the proof scopes; the root integrator owns the reported replay and compilation results.",
    "The final report changes the source-custody table to distinguish SC-COS-52 UCSD from SC-COS-50/51 TOE. I reread this final text; the edit does not alter the mathematical argument. Source transcript custody is separately reviewed by the assigned native-source reviewer."
  ],
  "literature_checks": [
    {
      "url": "https://arxiv.org/pdf/1501.05848",
      "finding": "Section II.A supports the classical f(R) equivalence with conservation explicitly required."
    },
    {
      "url": "https://arxiv.org/html/1605.00993",
      "finding": "The Newton-law scalar-elimination calculation uses a flat static source and boundary conditions; it does not invalidate the independently constructed local de Sitter growing metric perturbation."
    }
  ],
  "artifact_hashes": {
    "explorations/conditional-build/unimodular-lambda-and-scalar-2026-11-28.md": "471a58179b2f6b8551a422256789b856f689b6fe80231a827a51daabfcbd9ea6",
    "tests/program-focus/unimodular_lambda_probe.py": "0f1a0a4f4b58bf0899a8084e80bb7e91578db1c7242b3f74e6ac70bc9cf0d4c7",
    "lab/process/unimodular-lambda-certificates.json": "1d0b93842b00a49a047d48165f5c6d40caa55c50fda2f56a0cac276eb34e2307",
    "Lean/GUFormalization/UnimodularLambda.lean": "828a4930f2bb108dbad18de6c16a984b00e51a914d9ee502f684e5ef6d2db10f"
  }
}

## Independent review

{
  "reviewer_role": "independent source-native acceptance specialist; read-only, not a contributor",
  "basis": "fe43936285c50706eaeb54f942ba439dbde07bda",
  "preflight": {
    "target": "LB-CLASS unimodular scalar repair/source bridge",
    "tier": "T1",
    "expected_delta": "accept or return precise blockers on source custody, typed bridge and claim ceiling",
    "kill_condition": "an unsupported source necessity, conflated metric/volume construction, or mismatch between reported and certified statements defeats acceptance"
  },
  "accepted": true,
  "blockers": [],
  "artifact_hashes": {
    "explorations/conditional-build/unimodular-lambda-and-scalar-2026-11-28.md": "471a58179b2f6b8551a422256789b856f689b6fe80231a827a51daabfcbd9ea6",
    "tests/program-focus/unimodular_lambda_probe.py": "0f1a0a4f4b58bf0899a8084e80bb7e91578db1c7242b3f74e6ac70bc9cf0d4c7",
    "lab/process/unimodular-lambda-certificates.json": "1d0b93842b00a49a047d48165f5c6d40caa55c50fda2f56a0cac276eb34e2307",
    "Lean/GUFormalization/UnimodularLambda.lean": "828a4930f2bb108dbad18de6c16a984b00e51a914d9ee502f684e5ef6d2db10f"
  },
  "manifest": "/private/tmp/gu-lambda-frozen-hashes.json",
  "manifest_sha256": "ebdd537a893db4f0b7b2622970420cdd1558e9abd765f84cc134a9e290d944a6",
  "findings": [
    "The normal tr(S)=0 fibre seed hypersurface, a pointwise determinant restriction on observed metric variations, and a finite normalized fibre reference are explicitly separated. The seed theorem does not imply the new variational law.",
    "The 2021 primary draft at pp17/31, pp43-45 equations9.1/9.4/9.7-9.10, p62 equation12.21 and p64 itemiii supports the stated custody limits. MET(X) is the displayed action domain; equation9.7 varies varpi while holding the base section fixed; annotated Einstein recovery is not a derived tracefree observed metric equation.",
    "All eight named SC rows have ASSERTS polarity. The corrected report now attributes SC-COS-50/51 to TOE and SC-COS-52 separately to UCSD, including the correct seminar completion. This repairs the initial source-locus defect without altering any source claim.",
    "SOURCE conclusions are restricted to an unbuilt unimodular bridge. The candidate GU* modification is explicitly unadopted. The class exclusion is confined to ordinary local real metric solutions with b nonzero and A/(6b) negative.",
    "The native K95 contractions, added finite positive covariant reference, external fixed regulator, unregulated infinite fibre integral and conditional K77 construction are not exchanged. The finite-reference scalar result is not exported to a native finite reduction or a physical positive state space.",
    "Ambient adjoint-valued one-form coderivative identities are not identified with conservation of the observed symmetric Euler/stress tensor. The report correctly retains the action/reduction/identity bridge as unbuilt.",
    "The exact probe derives the arbitrary-lapse Ricci/scalar-Hessian temporal and spatial metric rows, verifies determinant tangency and a nonzero deltaR mode, includes the critical F0=0 case without division by F0, and carries contrary controls. Homogeneity/isotropy accounts for the vanishing remaining rows in the stated FLRW construction.",
    "All seven Lean statements are finite algebraic or order lemmas consistent with the report. No theorem in the file is a formal proof of the differential geometry, source applicability, Noether identity, complete PDE, or physical-domain claims."
  ],
  "resolved_review_findings": [
    {
      "id": "SOURCE-LOCUS-COS52",
      "initial_report_sha256": "9d2e1cad1a91d528e244e30e84fc95f8dc1cc414070293ca183d8d56ab990ffc",
      "issue": "SC-COS-52 was grouped under TOE despite its registered UCSD-seminar locus.",
      "resolution": "Final report separates TOE50/51 and UCSD52 and supplies the seminar transcript and timestamps.",
      "status": "resolved in accepted report hash"
    }
  ],
  "caveats": [
    "Acceptance concerns the declared local classical quadratic metric class. The result establishes a growing linear tangent, not a nonlinear nearby solution family, global normalizability, observed cosmology, quantum positivity or all-GU instability.",
    "The conditional source_bridge label names hypothetical application conditions; no source necessity or class-C representativeness is proved. Other coefficient signs, scalar-free classes, physical domains, reductions and source-compatible actions survive outside scope.",
    "The seven Lean cores and 43 exact controls do not independently certify source custody or the written geometric bridge arguments. This reviewer inspected their statements/code and did not rerun heavy computation; parent supplied successful replay/Lean results.",
    "Internal specialist review is not external expert certification or publication authorization."
  ],
  "source_checks": [
    "https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf",
    "lab/sources/source-claim-register.yaml:SC-GEO-03,SC-ACT-01,SC-ACT-02,SC-COS-01,SC-MAS-03,SC-COS-50,SC-COS-51,SC-COS-52",
    "lab/sources/transcripts/toe-weinstein-gu-40-years.md:02:14:44-02:16:33,02:22:20-02:23:28",
    "papers/drafts/Transcript into the impossible.md:00:02:05,00:25:56-00:27:00",
    "https://arxiv.org/html/1501.05848v2#S2.SS1",
    "https://arxiv.org/abs/1605.00993"
  ],
  "postflight": {
    "actual_delta": "Accepted final hash-bound artifact after one source-locus correction; no remaining blocker.",
    "owner_writes": "none",
    "heavy_computation": "none",
    "external_contact": "none"
  }
}

## Independent review

{
  "reviewer_role": "independent hostile acceptance reviewer; no contribution to candidate artifacts",
  "accepted": true,
  "acceptance_scope": "Conditional classical local linear metric theorem and scoped conservation/source-custody conclusions only; no GU source, physical-state, ledger, canon, or observed-Lambda promotion.",
  "blockers": [],
  "preflight": {
    "target": "LB-CLASS: unimodular Lambda datum and scalar persistence",
    "tier": "T1 hostile independent review",
    "expected_delta": "Accept or reject the concrete frozen theorem and wording under declared premises.",
    "kill_condition": "A missing full metric row, invalid determinant tangent, F0 division, pure-gauge curvature mode, unmarked domain transfer, or source-object conflation blocks acceptance."
  },
  "actual_delta": "Accepted after correction of the SC-COS-52 source locus; no mathematical blocker found in the declared local linear class.",
  "artifact_hashes": {
    "explorations/conditional-build/unimodular-lambda-and-scalar-2026-11-28.md": "471a58179b2f6b8551a422256789b856f689b6fe80231a827a51daabfcbd9ea6",
    "tests/program-focus/unimodular_lambda_probe.py": "0f1a0a4f4b58bf0899a8084e80bb7e91578db1c7242b3f74e6ac70bc9cf0d4c7",
    "lab/process/unimodular-lambda-certificates.json": "1d0b93842b00a49a047d48165f5c6d40caa55c50fda2f56a0cac276eb34e2307",
    "Lean/GUFormalization/UnimodularLambda.lean": "828a4930f2bb108dbad18de6c16a984b00e51a914d9ee502f684e5ef6d2db10f"
  },
  "manifest_match": true,
  "findings": [
    {
      "attack": "Pointwise volume restriction removes the scalar trace.",
      "disposition": "Not a blocker.",
      "reason": "The exact lapse/scale path has determinant -exp(6Ht), zero metric tangent trace, and nonzero delta R. Removing a trace coordinate does not remove all curvature variations. The report distinguishes pointwise density, total volume, and fibre-seed volume."
    },
    {
      "attack": "F0=0 invalidates the growing full-row solution.",
      "disposition": "Not a blocker.",
      "reason": "The normalization divides only by 3(r+3H)(r+4H), nonzero for H,r>0. F0=6b(H-r)(r+4H); at F0=0, r=H and both independent linear metric rows vanish without dividing by F0. The conformal control can be mapped to the determinant tangent with xi^0=(q-psi)/(2H), since psi_dot-H psi=q_dot+3Hq."
    },
    {
      "attack": "Constrained lapse was dropped or reduced variation omitted a tensor constraint.",
      "disposition": "Not a blocker.",
      "reason": "The probe retains N=(1+epsilon q)^(-3/2) before differentiation and constructs E00 and Eii/gii from arbitrary-lapse Ricci and scalar Hessian formulas. Independent hand derivation gives delta H=(q_dot+3Hq)/2 and delta R=3(q_ddot+7H q_dot+12H^2q). Homogeneity/isotropy forces the mixed rows to vanish. The Weyl-square term is zero on the entire conformally flat FLRW path, not merely on its background."
    },
    {
      "attack": "The growing curvature is pure diffeomorphism gauge.",
      "disposition": "Not a blocker.",
      "reason": "A diffeomorphism variation of constant background R is Lie_xi Rbar=0; the normalized delta R=exp(rt) is nonzero. This establishes non-pure-diffeomorphism status only, not a physical-state quotient."
    },
    {
      "attack": "A nonnormalizable homogeneous mode is being used as a global physical instability.",
      "disposition": "Scope explicitly prevents that inference.",
      "reason": "The theorem quantifies over ordinary real local solution germs, and the report expressly excludes infinite-slice normalizability, positive norm, physical observer identification, nonlinear stability, and a global domain conclusion."
    },
    {
      "attack": "A variable nonconserved source can be absorbed into a constant integration datum.",
      "disposition": "Not a blocker.",
      "reason": "For E=ell g, divergence is d ell. Thus conservation makes ell constant; a nonzero current requires a local primitive and globally zero periods. The held-scalar spurion Ward identity has the correct -1/2 sign for inverse-metric variation and is explicitly separated from metric-dependent or dynamical coefficients."
    },
    {
      "attack": "Source GU requires a different Lambda object.",
      "disposition": "Correctly fenced after source-locus repair.",
      "reason": "The corrected table binds SC-COS-50/51 to the TOE interview and SC-COS-52 to the UCSD seminar. The source one-form/VEV replacement is explicitly not identified with the constant integration datum. The report leaves the source-to-unimodular bridge unbuilt."
    },
    {
      "attack": "Literature already proves scalar elimination.",
      "disposition": "Not a blocker for this theorem.",
      "reason": "Eichhorn II A, equations (6)-(7), derives conserved classical f(R) equivalence. Nojiri et al. II equations (8)-(17) perform a flat static boundary-conditioned Newton-law calculation before their broad scalar-elimination wording; III separately discusses the covariant theory. Neither supplies a rejection of the explicit fixed-density de Sitter local metric solution checked here."
    }
  ],
  "corrections_during_review": [
    {
      "kind": "source-custody",
      "old_report_hash": "9d2e1cad1a91d528e244e30e84fc95f8dc1cc414070293ca183d8d56ab990ffc",
      "issue": "SC-COS-52 was grouped with the TOE interview despite the source register explicitly locating it in the UCSD seminar and warning against that misattribution.",
      "resolution": "Lead separated SC-COS-52 into its own UCSD row at 00:02:05, with completion at 00:25:56-00:27:00; reviewer checked the revised text, transcript excerpt, and final manifest."
    }
  ],
  "caveats": [
    "Acceptance establishes an explicit local solution of the linearized equations. The exact volume-preserving metric path is a variational path, not a family of nonlinear solutions.",
    "The spatially homogeneous mode is not proved normalizable on infinite slices. No boundary-conditioned physical state space, norm, quantum spectrum, or observer map is certified.",
    "At critical F0 the positive-kinetic interpretation is unavailable and linearization may have additional degeneracy; the result remains the stated non-pure-diffeomorphism local metric solution.",
    "The Weyl/Bach reduction works for the exhibited conformally flat path; this is an existence witness for every action in the named class, not a classification of all perturbations.",
    "The seven Lean results cover only finite algebraic/order cores. Differential geometry, Ward identities, source custody, and the local interpretation remain written arguments.",
    "Independent review inspected the exact probe and certificate but did not rerun the 43-control replay or Lean build; execution evidence is supplied by the lead as requested.",
    "The source bridge remains unbuilt. No source-negative conclusion, GU-wide stability result, new adopted physical choice, or observed cosmological-constant prediction is accepted."
  ],
  "primary_literature_checked": [
    {
      "url": "https://arxiv.org/pdf/1501.05848",
      "locus": "Section II A, equations (6)-(7), and continuation on PDF page 3",
      "use": "Classical f(R) equivalence depends on conserved matter/effective residual; no quantum equivalence inferred."
    },
    {
      "url": "https://arxiv.org/html/1605.00993",
      "locus": "Section II equations (8)-(17), (25)-(29); Section III equations (30)-(31)",
      "use": "Separate flat static Newton calculation and its scalar-elimination wording from the de Sitter local witness and covariant construction."
    }
  ],
  "local_source_evidence": [
    "AGENTS.md",
    "CURRENT-STATE.yaml#program_focus",
    "GEOMETER-VS-PHYSICS-OBJECTS.md",
    "lab/methods/source-native-comparator-routing.md",
    "lab/specifications/six-axis/six-axis-template.md",
    "RESEARCH-POSTURE.md",
    "CONTRIBUTING.md",
    "VERIFICATION.md#verification-standard-under-program_focus",
    "lab/sources/source-claim-register.yaml#SC-COS-50--SC-COS-52",
    "lab/sources/transcripts/toe-weinstein-gu-40-years.md",
    "papers/drafts/Transcript into the impossible.md"
  ],
  "owner_edits": false,
  "external_contact": false
}
