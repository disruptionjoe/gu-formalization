# Independent review: normal tensor class and restricted local response

**Later correction:** The mathematical reviews below verified the declared plus/reversion pairing. They did not authenticate its original source label, which was wrong: printed eq3.27 is minus/conjugation. Their plus theorem and auxiliary review survive; source transfer of the optional-C zero is withdrawn. See [correction review](2026-11-26-source-adjoint-placement-review.md).

Basis: GU736d965e076a82608cc8f2d1ca2016612de4142c. Internal review only, not external expert validation. Normal tensor classification has two independent mathematical reviewers and one hostile source reviewer; its author did not review that theorem. The auxiliary theorem has a separate independent mathematical reviewer; its author did not independently review it. Lean proves only the stated finite coefficient core.

## Integration and corrections

- Corrected two initially false probe controls: even-degree normal maps at4/6 and invariant middle5 forms exist. They are excluded by the declared parity, not nonexistent. Accepted multiplicities/ranks unchanged.
- Corrected rank-pairing explanation: C flips both complex chirality labels and the full-U A is C-odd; sharp flips H only. Added direct native controls. The all-parameter rank proof and counts are unchanged.
- Pinned Omega=omega_H omega_N; declared geometry-derived K95 versus asserted K77; held q/split in the primitive NE variation; retained correlated total/observed grades and source2+1.
- Retained nonzero moving-reduction countercontrol, full-U survivors and the opposite W2 pairing. No source-necessary exclusion.
- Auxiliary current includes every induced-Q, inclusion, second fundamental, frame and density term. Compact-support corollary cuts off only test perturbations, not matter solutions. It is not a physical ghost/propagation theorem.

## Verification

Exact finite replay, Lean and native gates are recorded in the linked evidence. No numerical rank or approximate zero is used for a class exclusion. Existing root/inverse certificates are reused at their authenticated scope.


## Mathematical review1

# Independent mathematical review: normal tensor class

Reviewed: 2026-11-26. Reviewer role: mathematical specialist, read-only over owner truth.
Baseline: `736d965e076a82608cc8f2d1ca2016612de4142c`; mounted HEAD and origin/main matched that parent-fetched revision.
Candidate reviewed: `/private/tmp/gu-normal-scope-20261126.md` and the corrected `tests/program-focus/source_normal_tensor_class_probe.py` in `/private/tmp/gu-normal-tensor-wt-20261126`.

Target: LB-CLASS normal-one-form alternative; T1 acceptance depth because the added fixed-symmetry/C category has a zero result. Expected delta: certify or correct the complete coefficient/contraction classification. Kill condition: only the declared pointwise fixed tensor category with the added C restriction. No source or class-C verdict is reviewed or authorized.

## Verdict

**Accept the mathematical classification and contraction theorem in the stated finite-dimensional, pointwise K95 convention and fixed-symmetry scope.** All advertised dimensions, contraction ranks and kernels, four-parameter classification, and spinor-rank strata are correct. The independent proof below does not rely on a finite matrix rank sample.

This review is one internal specialist review, not proof-assistant certification or external-expert certification. Parent remains responsible for the other required review roles, Lean scope, serialized native validation, source wording and final acceptance.

## 1. Completeness and independent multiplicity check

On full complex Dirac S128, `Cl_C(H+N)=End_C(S)` is an algebra isomorphism. Under connected proper block Spin(H), only exterior degrees0 and4 in the horizontal Clifford factor are invariant. They are `1,omega_H`; both are even. Ambient oddness therefore requires normal degrees1,3,5,7,9. This is an all-End argument, not a Clifford-degree ansatz.

Independently enumerated the1024 exterior subsets of the weights of

`N_C=(3,1,-2)+(3bar,1,2)+(1,2,3)+(1,2,-3)`.

Used the signed constant term with the positive A2×A1 roots to compute invariant multiplicities. Because N is self-dual, the trivial multiplicity in `N tensor Lambda^k N` is the required vector multiplicity. Independent output for degrees0 through10:

```text
dim (Lambda^k N)^SM:      1 0 2 0 3 2 3 0 2 0 1
dim Hom_SM(N,Lambda^kN):  0 4 0 8 4 10 4 8 0 4 0
```

Thus the admitted odd degrees give `(4,8,10,8,4)` and total complex dimension68 after the two horizontal factors. Real tensor invariants complexify to these spaces, so their real dimensions equal the displayed complex dimensions.

**Correction found and resolved:** an early candidate probe incorrectly asserted absence of all odd invariant forms and even-degree vector intertwiners. There are two invariant degree5 forms and four vector copies at each of degrees4 and6. The corrected probe now asserts those values and excludes the even-degree vector terms using ambient parity. I inspected that correction. This error does not change the proposed68-dimensional class.

## 2. Sharp and C restrictions

For a real normal k-form Clifford word, sharp acts by `(-1)^(k(k-1)/2)`. Multiplying by real `omega_H` preserves that sign: it is sharp-selfadjoint and commutes with every normal word. Hence sharp-skew coefficients are imaginary in degrees1,5,9 and real in degrees3,7. This gives68 real dimensions.

The declared antilinear C commutes with real Clifford vectors and therefore fixes real Clifford words. C-compatible complex-linear coefficients are precisely the real coefficients in this decomposition. Intersecting with sharp-skew leaves degrees3,7 only: `2*(8+8)=32` real dimensions. The result is32, not half of68. No additional constraint follows from `C^2=-1` on these commuting complex-linear maps.

The K95 premise is a declared derived geometric branch. The result should not be rephrased as source confirmation of K95 in place of the source's distinct signature assertions.

## 3. Complete contraction proof and actual NE map

Write `d_l=dim (Lambda^lN)^SM`. For any invariant `(k-1)`-form psi and `(k+1)`-form theta, the two equivariant lifts are

```text
alpha_psi(n)=n^flat wedge psi,    Gamma_N alpha_psi=(11-k) psi;
alpha_theta(n)=iota_n theta,     Gamma_N alpha_theta=(k+1) theta.
```

The opposite-degree component is zero in each case. These identities use the inverse metric in Gamma and hold for the indefinite normal metric. They prove surjectivity independently onto both adjacent even degrees; all shown integer factors are nonzero. The degreewise kernels are therefore

`m_k-d_(k-1)-d_(k+1)=(1,3,4,3,1)`.

Over C, all invariant even outputs occur, giving image24C and kernel44C. In the sharp-real category, neighboring odd degrees carry opposite real/imaginary coefficient phases. Contributions into a common even degree cannot cancel over R. The image has44R dimensions and the kernel24R dimensions. Restricting to degrees3 and7 gives image20R and kernel12R. Equivalently the C-compatible image consists exactly of the real invariant even degrees2,4,6,8, times either horizontal invariant factor.

For the primitive NE coefficient `delta D_NE[alpha] nu=alpha nu` and the held map `q=(P_H,Gamma_Y,identity)`, pure metric-normal covectors annihilate H. Thus exactly

`q delta D_NE[alpha] nu=(0,Gamma_N(alpha) nu,0)`.

Since b=0, sigma=tau in the alternate coordinates. This step is an algebraic contraction identity; it does not require identification with a physical positive pairing or W2 pairing.

**Wording requirement:** a nonzero alpha in ker Gamma_N is invisible to this particular NE observation, not a zero primitive NE tensor or a universally vanishing source current. The full uncontracted primitive coefficient may remain nonzero. The reported24/44/20 dimensions are coefficient-map dimensions; they are not ranks on S128, mode counts or family counts.

## 4. Endogenous Lorentz plus fixed geometric weak symmetry

The tensor action must be on `N* tensor End(S)`:

`(g.alpha)(n)=rho_S(g) alpha(rho_N(g)^(-1)n) rho_S(g)^(-1)`.

The existing trace-motion theorem applies to this honest representation. The same fixed tensor invariant under graph Lorentz and actual geometric weak is invariant under generated `so(H)+so(N)`. This implication does not require recomputing Lie closure and does not apply to spin-only weak action.

For Spin(N), the vector occurs exactly once in each of normal exterior degrees1 and9. Together with horizontal degrees0,4, this gives exactly four complex directions:

`alpha(n)=c_N(n) A`, `A in span_C{1,omega_H,omega_N,Omega}`.

Choose orientation convention `Omega=omega_H omega_N`. Each real tensor `c_N(n) B` for these four B is sharp-selfadjoint and C-even, including B=omega_N and Omega because both anticommute with c_N(n). Therefore the sharp-skew class is exactly

`A=i(a+b omega_H+c omega_N+d Omega)`, `a,b,c,d real`.

Its C-compatible subspace is zero. Conversely every one of these four imaginary tensors has the required symmetries, so this is an exact classification, not only an upper bound. The full-U sharp class remains nonzero.

For every member, `Gamma_N alpha=10 A`, so the coefficient contraction has zero kernel. With `omega_H^2=omega_N^2=-1`, the four simultaneous eigenspaces have dimension32. On signs `(s,t)`, A has eigenvalue

`i*(a-d*s*t+i*(b*s+c*t))`.

Reality of a,b,c,d pairs vanishing blocks `(s,t)` and `(-s,-t)`. Hence ranks are exactly0,64,128. More explicitly:

- rank0 iff both real pairs `(a+d,b-c)` and `(a-d,b+c)` vanish;
- rank64 iff exactly one pair vanishes;
- rank128 otherwise.

Each ambient input half contributes rank0 or64. This argument proves all parameter values, beyond any finite fixture sampling. A different orientation sign only relabels d.

## 5. Strongest counterconstruction and scope ceiling

Let J specify the fixed normal SM reduction, let kappa_J be its color Kahler2-form, and set `theta_J=kappa_J wedge kappa_J`. Then

`alpha_J(n)=iota_n theta_J`

is a nonzero real degree3 tensor, SM-equivariant at J, sharp-skew and C-compatible. It satisfies `Gamma_N alpha_J=4 theta_J`. As J transforms, the family is covariant under geometric transformations. Its value at one fixed J is not invariant under graph Lorentz. This supplies an explicit surviving moving-family countercontrol to any attempted extension of the zero theorem beyond common fixed-object isotropy.

The zero therefore requires both additional premises: fixed-object common symmetry and C preservation. Neither is supplied merely by source full U(64,64), effective chiral behavior, a moving reduction, or a VEV-dependent tensor family. No physical excitation, suppression estimate, source inconsistency, matrix/class-C exclusion or GU verdict follows.

The source-side convention `c(v)^sharp=+c(v)` is essential. If only the adjoint convention is changed to `c(v)^sharp=-c(v)` while retaining the same real Clifford/C data, all odd-word sharp signs reverse and the four real product tensors survive. This is a conditional convention check, not an established bridge to every W2 datum or physical pairing.

The source-named grade1 scalar line is properly distinguished from the larger oriented all-End class. Its normal component `i a c_N(n)` has `Gamma_N=10 i a I`; its full ambient equivariant completion includes the corresponding horizontal component. Extending the normal tensor by zero on H is not ambient Spin14 equivariant.

## 6. Review closeout

Actual delta: all proposed central numerical and structural claims accepted within the stated pointwise class; one erroneous probe control independently identified and confirmed corrected; observation-kernel and moving-family wording requirements made explicit.

No owner file was edited. No heavy verification was run. Independent execution was limited to a small standard-library exact integer character enumeration. I inspected the candidate probe but did not run its128-dimensional fixture because the parent owns serialized verification. All requested corrections above are mathematical scope/wording fences, not new governance or source verdicts.

## Mathematical review2

# Independent mathematical review 2 — normal tensor classification

Reviewed read-only at worktree `/private/tmp/gu-normal-tensor-wt-20261126`:

- `explorations/conditional-build/source-normal-tensor-class-2026-11-26.md`,
  sections1–5 and corresponding scope/claim grammar;
- `tests/program-focus/source_normal_tensor_class_probe.py`, normal-tensor
  character/Clifford/rank controls;
- `Lean/GUFormalization/NormalTensorClass.lean`;
- the existing `weak-endogenous-grading-2026-11-24.md` Lie-generation input.

**Verdict: mathematical PASS for the stated fixed pointwise tensor classes.**
No blocking correction found. This review does not certify source necessity,
physical VEV selection, class-C representativeness, physical ranks or GU claims.
Root owns serialized exact/Lean execution; I did not rerun heavy jobs.

I did not author the normal-tensor result. I DID author the separate auxiliary
scope proposal, so I exclude draft section6 and the probe's auxiliary_scope
routine from this independent review. That material requires the other reviewer.

## 1. Applying Lie generation to tensors is legitimate

The relevant representation is the honest tensor representation
`N* tensor End_C(S)`, with action
`rho_S(g) alpha(rho_N(g)^(-1)n) rho_S(g)^(-1)`.
If a vector is annihilated by the two stated generating Lie algebras, it is
annihilated by their brackets and real linear span in EVERY representation.
Consequently the prior trace-motion generation theorem applies to tensors just
as it applies to an endomorphism commutant. No false claim that the normal leg
is inert is used in Category E.

The imported theorem has the correct geometry: endogenous Lorentz fixes the
negative metric-trace vector, while a nonzero actual weak quaternionic generator
on the negative four-plane has no kernel there. A negative trace vector has
nonzero projection to that four-plane. Hence it moves the trace vector. The
generated algebra is indeed the independent product, under the declared fixed
weak reduction and simultaneous fixed-alpha condition. This is not a theorem
about a family alpha(J) with J transformed. The explicit moving-reduction
countercontrol properly demonstrates the distinction.

## 2. Completeness, real structure and the optional-C zero

For connected horizontal Spin(3,1), invariant horizontal exterior forms are
degrees0 and4. The complete Clifford algebra is End_C(S), so the two horizontal
factors and all normal odd degrees exhaust the ambient-odd block-Lorentz
category. For the product category, the normal vector occurs once in Lambda1N
and once in Lambda9N and nowhere else. Tensoring with horizontal degrees0/4
gives exactly four complex coefficients. No omitted middle-degree tensor is
being excluded by an ansatz.

The sharp calculation is correct in the DECLARED source convention
`c(v)^sharp=c(v)`: a real k-word has sign `(-1)^(k(k-1)/2)`.
Real omega_H is sharp-self. Thus normal degrees1,5,9 need imaginary coefficients
for sharp-skew, while3,7 need real coefficients. Every real Clifford word is
C-even, so imposing C compatibility removes the imaginary sectors, leaving
32 real parameters in Category B. There is no reason for this involution to
halve68; the draft's32 is correct.

In Category E all four real normal vector tensors are sharp-self, INCLUDING
`c(n) omega_N` and `c(n) Omega`: reversing omega_N contributes a minus, and
anticommuting it past c(n) contributes another. Thus sharp-skew makes all four
coefficients purely imaginary; optional C makes them real; their intersection
is zero. The finite Lean coefficient theorem exactly captures this last
implication and is honestly scoped below the representation premises.

The W2 contrast is also sound as stated conditionally: replacing the Clifford
sharp sign by minus reverses the sign on odd grades, so the four real tensors
survive if the same real Clifford/C laws are retained. The result may not be
silently imported into W2, and the draft explicitly forbids that transfer.

## 3. Normal contraction and real rank-nullity

For a degree-k normal coefficient map, Clifford multiplication sends its
contraction only to degrees k-1 and k+1. The two written constructions are
genuine independent right inverses:

    sum_i eta_i c(n_i)(n_i^flat wedge psi)=(11-k)psi,
    sum_i eta_i c(n_i)iota_(n_i) theta=(k+1)theta.

The opposite-grade terms vanish. The inverse metric cancels the indefinite
signature, and the factors are nonzero for all admitted k. Thus the degreewise
kernel dimensions m_k-I_(k-1)-I_(k+1) follow by rank-nullity, rather than an
unverified numerical rank.

The real contraction ranks are larger than the complex dimension of its
complex image because this is a restricted real source space. Adjacent odd
degrees have opposite coefficient phases, so their shared even-degree output
subspaces are linearly independent over R. The exact arithmetic is:

- complex source68, image2*(1+2+3+3+2+1)=24, kernel44;
- source-sharp real68, image2*(1+4+6+6+4+1)=44, kernel24;
- C-compatible real32, image2*(2+3+3+2)=20, kernel12.

No cancellation between different Clifford degrees or horizontal factors was
missed. In particular omega_H times a normal form is a different Clifford
subspace from the form without omega_H.

For Category E, writing alpha(n)=c(n)A yields exactly Gamma_N(alpha)=10A.
The four A coefficients are independent, so the coefficient map is injective.
It would be a mistake to identify this coefficient rank4 with spinor rank;
the draft keeps those quantities separate.

## 4. Arbitrary-parameter spinor rank strata

On the joint h/n eigenspace with h=i*s, n=i*t, s,t in {+1,-1},

    A=i(a+b h+c n+d h n)

has eigenvalue `i(a-d*s*t)-(b*s+c*t)`. Each joint block has dimension32.
Opposite (s,t) and(-s,-t) blocks vanish together because all a,b,c,d are real.
For st=-1 the vanishing condition is `(a+d,b-c)=(0,0)`; for st=+1 it is
`(a-d,b+c)=(0,0)`. This proves rank0/64/128 for ALL parameters, not only the
81 sampled coefficient fixtures. Each paired set is an entire ambient half.
The draft correctly denies physical chirality or generation inference.

I re-read the corrected attribution in section4: same-ambient pairing follows
from the antilinear C law (C flips both labels, and C A C^-1=-A gives paired
eigenvalues lambda and minus-conjugate(lambda)). Sharp instead flips only the
horizontal spectral projector: h^sharp=h while n^sharp=-n. Thus the corrected
text is sound. The rank calculation above uses the exact eigenvalues directly
and does not rely on the withdrawn sharp attribution. The newly pinned
orientation Omega=h*n also matches these eigenvalue/rank formulas.

## 5. Probe and Lean reproducibility seam

The character enumerator computes all1024 exterior weights with exact integer
hypercharge and Weyl-denominator extraction. Summing multiplicities of the four
distinct irreducible summands in N_C computes Hom_G(N,Lambda^kN), not a spinor
multiplicity. The retained even-degree and odd-invariant controls guard the
parity exclusion; those spaces are not silently assumed absent.

The native matrix fixtures use signed monomial Clifford matrices and binary
fractions. The displayed comparisons are exact at their small integer bounds,
not floating tolerance rank tests. The1800 equations test all45 normal
bivectors against10 vector slots for4 tensors, including indefinite generators.
They validate the native conventions; the written representation argument
supplies the exhaustiveness they cannot provide alone.

The Lean file proves coefficient incompatibility, injective multiplication by10,
rank-pair zero arithmetic and dimension sums. It does not formalize the Lie
generation or Clifford completeness. Its header and the artifact explicitly
preserve that ceiling. No overclaim found in that division of labor.

## Strongest overclaim / counterconstruction

The strongest invalid inference would be: “normal source connection mixing is
impossible because the optional-C fixed class is zero.” The source full-U class
retains four real tensors; block-only C retains32; moving reductions retain the
explicit degree3 tensor; W2 uses a different sharp convention. The draft states
all these survivors and does not identify optional C/fixed isotropy with a
source necessity. Those distinctions are essential to acceptance.

## Hostile source review

# Hostile source and scope review: normal tensor class

Review target: `explorations/conditional-build/source-normal-tensor-class-2026-11-26.md` in `/private/tmp/gu-normal-tensor-wt-20261126`.
Frozen source basis: `736d965e076a82608cc8f2d1ca2016612de4142c`; this is review of the working candidate, not a claim that the draft is published upstream truth.
Role: required Tier-1 hostile source/scope reviewer. Read-only research review; no owner edits, heavy computations, external review, or claim promotion performed. Temporary review output only.

## Disposition

**Accept the scoped internal classification and exclusion after the specific corrections below, subject to the other mathematical reviews and native verification. Reject every interpretation of it as a GU falsification, an exclusion of the source curvature/VEV mechanism, or a physical family/chirality result.**

The mathematical scope is materially stronger than a Clifford-degree ansatz: the pointwise all-End normal coefficient class is covered. Its source scope remains conditional because neither fixed simultaneous isotropy nor quaternionic-compatible connections are source-required. The draft correctly states this distinction and retains live counterconstructions. I did not independently replay its character or Clifford probe, so this review is not an additional numerical certificate.

Prerequisites checked: repository AGENTS; GEOMETER-VS-PHYSICS-OBJECTS; source-native comparator routing and its relevant VEV, signature, chirality and 2+1 pointers; source register SC-GEO-51, SC-CHI-51/52, SC-MAS-02 and SC-GEN-01/52; the Nov24 horizontal/reality and weak/endogenous results; the Nov20 actual observation-label correction; the source primary pack WGS-05; and the Aug8 K77/K95 correction. Older comparator verdicts in historical prerequisite documents are not adopted as current source verdicts.

## Corrections and the rank argument

1. **Mandatory correction, already integrated during review:** the initial draft attributed same-ambient paired joint-chirality blocks to `sharp`. Its own laws give

       chi_H = i omega_H, chi_H^sharp = -chi_H,
       chi_N = i omega_N, chi_N^sharp = +chi_N,
       Omega^sharp = -Omega.

   Sharp exchanges horizontal labels, preserves normal labels, and pairs opposite ambient halves. It does not explain a same-ambient rank-64 pair. Instead the fixed antilinear `C` flips both complex chirality labels and preserves ambient Omega. For the four-real-parameter full-U family, `C A C^-1 = -A`; hence paired eigenvalues are `lambda` and `-conjugate(lambda)`. Their zero sets agree, yielding two blocks of dimension32 at a time. The rank0/64/128 result survives; its explanation needed repair. The updated paragraph correctly separates this algebraic use of C from imposing `[alpha,C]=0`.

2. **Pin the orientation in the explicit rank formula.** The draft allows `Omega=±omega_H omega_N`, while the displayed conditions `(a+d,b-c)=0` and `(a-d,b+c)=0` use the plus choice. Say `For Omega=omega_H omega_N` before that formula; reverse the d convention for the opposite orientation. The rank stratification itself is orientation independent.

3. **Avoid “source K95” as an unconditional carrier identity.** Use “geometry-derived K95 branch, H(3,1)+N(6,4), with the declared source-side sharp convention.” The source explicitly asserts/uses K77, while the displayed metric-block calculation yields K95. The ambient signature bridge remains open; neither the quaternionic reality law nor this sharp result transfers silently to K77. The current theorem is valid on its declared K95 branch.

4. **Name the held primitive slice.** The actual `q delta D_NE` formula keeps the observation map, metric/split and epsilon wrapper fixed while varying `varpi` independently. This is the authenticated primitive source variation from Nov24. It does not assert closure of every block of the fluctuated operator or compute a variation of q caused by changing geometry. No cancellation by unrelated metric variations is licensed on this independently varied primitive slice either.

## Strongest attempted false falsification

Tempting claim: “The normal mass/VEV tensor must be geometric, Lorentz covariant, weak invariant and real; the complete class is zero; therefore GU cannot implement its curvature-induced mass or effective chiral split.”

This fails at two independent premise transfers:

- **Full-U is the source parent.** SC-GEO-51 names U(64,64), not the additional fixed-quaternionic-compatible subgroup. The four-real-parameter source-sharp-skew family survives with no C-compatibility restriction. A zero intersection after adding C is an exclusion of that conditional internal class only.
- **Covariance of a moving family is not isotropy of one fixed tensor.** The same fixed alpha invariant under graph Lorentz and the same fixed geometric weak group falls under Lie generation. A family depending on a moving reduction does not satisfy this hypothesis merely by covariance. The explicit `theta(J)=omega_c(J)^2`, `alpha_J(n)=iota_n theta(J)` control is nonzero, real degree3, sharp-skew and C-compatible, and `Gamma_N alpha_J=4 theta(J)`. It survives in the covariant-family category. It is neither an omitted member of Category E nor a selected physical completion.

Conversely, these survivors do not establish successful GU dynamics. Pointwise permission is not on-shell excitation, normalization, propagation, quotient admission or absence of low-curvature suppression. SC-CHI-51/52 require effective behavior; they do not require every allowed raw coefficient to vanish as a background VEV becomes small.

## Observation, grading and source labels

The normal contraction is the actual source-held map: `q(alpha nu,0)=(0,Gamma_N(alpha)nu,0)`, and switching to sigma coordinates changes nothing because b=0. This is not a scalar Kaluza–Klein projection. A tensor in the coefficient kernel is invisible in this one observed primitive arrow; it is not thereby zero as a primitive coefficient or guaranteed invisible to every current or operator block.

Ambient alpha oddness and contracted Gamma-evenness must remain separate from observed physical chirality. With the retained correlated grades

    G = diag(Omega,-Omega) on (zeta,nu),
    G_o = diag(Omega,-Omega,-Omega) on (b,tau,nu),

an ambient-odd alpha gives a grade-even NE vertex. Gamma-evenness does not restore the operator's graded decoupling. With the actual independent barred fields and Krein density duality, the prior primitive opposite-sector bilinear conclusion remains a field-type statement; physical readout and suppression remain open. The existing eq9.16/section11.2 half-label collision is not resolved here.

The source total remains non-chiral; this theorem does not settle the effective observed chiral separation. Rank64 is support on an entire ambient input half, not a chosen four-dimensional Weyl family. The source 2+1 provenance, imposter128 versus RS384 distinction, and SC-GEN-52 gamma-trace/gamma-traceless labeling uncertainty remain intact. No coefficient dimension, kernel dimension, spinor rank or Clifford multiplicity is a family count.

## SC-MAS-02 and the spinless line

The draft's distinction is correct and necessary. SC-MAS-02 specifically identifies the true-spin-zero invariant inside `Lambda1 tensor Lambda1`, not every oriented-Spin-invariant all-End tensor. On this split its normal grade1 component is `alpha(n)=i a c_N(n)`. It has nonzero `10ia I` contraction and rank128 for a nonzero a, and is absent only after imposing optional C-compatibility.

The normal component extended by zero on H is not a full ambient Spin-equivariant scalar one-form. The corresponding full ambient grade1 invariant is `v -> i a c_Y(v)`, with linked horizontal and normal components. The all-End `c(v)Omega` partner belongs to Clifford degree13 and is a pseudoscalar; source MAS-02 does not automatically select it. This is true-spin decomposition of an ad-valued one-form, not a claim that a vertical one-form becomes a four-dimensional scalar. WGS-05 still leaves equality with the stylized R/4 mass and the full observed operator placement unconstructed.

## Counts versus physical constraints

The proposed block counts `68 real -> image44/kernel24` and optional `32 real -> image20/kernel12` are coefficient-map dimensions under the specified sharp phases. The complex class has the different `68 -> image24/kernel44` count. It is correct to keep these separate. The stronger fixed class gives four real coefficients, an injective factor10 map, and spinor ranks0/64/128. None measures the number of independent propagating modes, physical constraints, mass eigenstates, generations, or source-selected free choices.

Section6 now explicitly owns W2's opposite Clifford-adjoint convention and candidate scope. Its local constrained-Q construction is a separate diagnostic; source class-C representativeness, full-R realizability, global physical support and nonlinear field equations do not follow. Nonzero reached spin4 support is not an adjoint-cokernel obstruction. This section's geometric argument needs its designated specialist review, not an acceptance inferred from the normal tensor theorem.

## Next source-relevant test

The best source bridge discriminator is the **actual mass-carrier/observed-operator placement and transformation law**: determine, from the source-owned displaced connection and its existing observation map, whether the MAS-02 spinless projection is the linked full ambient grade1 line and whether the accompanying reduction is fixed or transforms. Track this line through the full declared operator and correlated grades; preserve independent bars, the actual pairing, and the source 2+1 provenance. Compare the result with the source's R/4 effective mass statement without identifying them by the word “scalar.” This is a structural bridge question, not permission to invent an action or require C.

For the already-owned W2 candidate, the separate executable continuation is the actual induced-connection receiver/cokernel calculation for the reached spin4 sources (plus any uncaptured spin5 remainder). It can advance candidate consistency without pretending to close the source bridge above. Repeating the normal all-End solve or converting its optional-C zero into a Higgs/chirality no-go would have less source relevance.

No source verdict, physical ledger movement, class-C exclusion, source necessity claim, or GU verdict is supported by this review.

## Independent auxiliary review

# Independent T2 mathematical review: smooth restricted-Q auxiliary elimination

Reviewer: normal_tensor_scope agent, reviewing the other specialist's auxiliary proposal; not reviewing my own normal-tensor result.
Date: 2026-11-26.
Basis: supplied fetched main `736d965e076a82608cc8f2d1ca2016612de4142c`.
Candidate reviewed: `/private/tmp/gu-jet-scope-20261126.md`, sections A1–A5 and B; associated sparse diagnostic `.py` and `.json`.

## Verdict

**ACCEPT the analytic restricted-Q local-elimination argument at conditional internal T2 scope**, with the coefficient-transfer explanation below carried into the artifact. No need for a whole auxiliary inverse or a new source datum. The result upgrades the four existing specified scalar weak coefficients from contracted formal values to actual coefficients of a smooth local constraint-satisfying diagnostic lift. It does not establish the remaining range equation, full-range auxiliary jets, a physical domain, normalized observable, source necessity or GU failure.

The domain is a deliberately restricted family of test connection variations generated by the two already-tested range vectors. This is a diagnostic selection and must not be described as a physical state restriction, selected superselection sector, or new dynamical completion.

## What I checked independently

I read the actual closed-dt projector cancellation in `source-action-kappa1-constraints-2026-11-25.md` section1; affine isometry, spin/Krein lift and naturality in `source-action-homogeneous-analytic-vacuum-2026-11-25.md` A1–A3; all-six-Lorentz invariance of the59 family in `source-action-dynamics-and-continuation-2026-11-25.md`; exact reached inverse and scalar-coefficient scopes in `source-action-weak-response-2026-11-26.md`; and source/control/known-response/current-jet implementation in `source_action_weak_response_probe.py` and `source_action_paired_response_probe.py`.

I independently reran ONLY the small standard-library sparse rational diagnostic with `PYTHONDONTWRITEBYTECODE=1`. Its entire parsed JSON exactly equals the supplied result. This checks the Gram, conjugation/halfturn, nonzero range-spin6 and normal-source-spin4 diagnostics. No inverse, 7080-closure, scalar-goal, large matrix, Lean or physical calculation was rerun by this reviewer.

## Analytic review

### 1. Transitivity and time projector

The affine subgroup preserving the positive dt line has dimension17 (13 linear plus4 translations); its connected isotropy at (0,eta) is SO3, dimension3, giving the required14-dimensional orbit. The explicit local boost construction is valid because dt*g is a timelike row for eta exactly when dt is timelike for the transported inverse metric. A local analytic pure boost sending it to a positive multiple of dt exists near the origin.

The isotropy scales dt by1, not a nontrivial positive constant. Away from the origin a positive constant group scaling of dt does not change ker K_dt or its native orthogonal projector. The original closed dt remains the one-form used in the differential cancellation. It would be an error to substitute an arbitrary rotating/nonclosed normalized time form into that theorem; the proposal explicitly avoids doing so.

The59 background coefficients have published full connected-Lorentz invariance. Therefore each fixed certified root extends as an affine-homogeneous analytic background. This suffices to transport the M restriction by conjugacy on the timelike-dt patch. The observation section and matter completion need not share affine invariance, and the proposal does not use that false premise.

### 2. Real Q and nondegenerate complement

The highest-weight Gram is exactly diag(3145728,-9437184), with zero cross term. Together with the checked rotation-to-conjugation relation, SO3 invariance and nonzero lowering constants, this establishes two real spin7 copies, real dimension30, with nondegenerate native pairing. It does not establish positivity. The native orthogonal projector Pi_Q therefore exists and gives an actual metric induced connection; no arbitrary complement needs to be selected.

SO3-invariant Q_p transports independently of the adapted-frame choice. Only local smooth/analytic associated-bundle transport is claimed; no global spin/frame section is required.

### 3. Source coverage and inverse transport

Tangent SO3 types have spin at most2; Q has spin7 and the complete carrier has no spin above7. Thus principal Q sources can only have spins5,6,7. The tangent spin2 copy occurs once. The spin5 Clebsch-Gordan arrow V2 tensor V7→V5 has multiplicity1, separately for each of the two Q copies. The two previously certified nonzero highest5 source vectors therefore determine this entire coupling; E plus its rotation orbit covers it. Complete6/7 certificates cover the rest.

Finite-dimensional sums of invariant invertible subspaces remain invertible here. More explicitly, M is injective on their intersections and hence bijective there; restricted inverses agree on intersections, defining an inverse on the sum. This is a finite linear-algebra fact, not a spectral or PDE assumption. Reality and the SO3 action commute with M, so the real generated bundle is covered.

Conjugate transport supplies an actual analytic Y_Q, not merely an assigned first derivative. Its individual covariant differentiated identities follow by differentiation, with the actual Hom(Q,N) and tangent-index connections. They need not be solved as new independent algebraic unknowns. This argument does not extend Y to Hom(R,N).

### 4. Lower terms and differentiating the inclusion

The correct restriction is

    P H(i_Q v)=L_Q^a nabla_a^Q v+C_Q v,
    C_Q=P J i_Q+sum_a P K^a B_a.

The derivative of i_Q has both R and N parts. Its R/Q-perpendicular part is B_a and must remain. Its N part is killed by P K^a P=0, separately for each a. This is why the proposal's formula includes the second fundamental correction without an omitted N derivative.

The fully contracted C_Q is an SO3 intertwiner Q7→N at the isotropy point, so it lies in complete N7. The already-certified N7 inverse supplies Z_Q. Individual B_a can leak into spin6 and individual K^b B_a into spin4; that does not contradict the spin7 statement for the natural fully contracted map. Dropping B_a would invalidate the proof even though its final contracted current is blind.

For every smooth compactly supported local Q section v,

    n=-Y_Q^a nabla_a^Q v-Z_Q v

is smooth, has the same support, and obeys P H(i_Q v+n)=0 using the actual closed-dt identity P H n=M n. No time derivative of v is introduced by the principal response because P K_dt=0. This proves constraint elimination only; the remaining range Euler equation is not imposed.

### 5. Transfer of the four matched coefficients

This is the most delicate step and should be explicit in the final artifact. With native density and induced connections,

    j_eff,Q = j_R i_Q - j_N Z_Q
              + (nabla j_N) Y_Q + j_N div Y_Q,

where density/frame/tangent-index terms are included in the divergence notation. At p the two terms before the differentiated-current term and the fully contracted geometric remainder map Q7 into the COMPLETE spin7 connection carrier. The existing canonical seed-current map annihilates that whole carrier, so their seed-current values vanish.

The differentiated-current term depends only on the pointwise values Y_Q^a(p)V. Those are exactly the previously authenticated particular responses. Passing between the original Nomizu frame and a time-adapted frame, or between nabla^R and nabla^Q, adds derivative-of-inclusion/projector/frame terms to the geometric remainder; it does not alter that pointwise current-derivative term. All such terms must be collected with B, induced Q-index and density corrections BEFORE applying SO3 equivariance. They form contracted natural maps Q7→spin7 and are seed-current blind.

Consequently the four old nonzero interval certificates apply to the actual restricted local weak density coefficient. This is not equality of full-R operator derivatives. Seed blindness here belongs to the same canonical injection, literal readout and prescribed independent barred/column seed convention used by the old certificate; it is not a universal theorem for arbitrary matter rows, altered observation maps or arbitrary normalized physical currents.

The sparse code's `full_jet` retains the row/column seed derivative and moving A^t inverse; `tangent_matrix` retains the other normal derivative contributions. The matched formula uses the same pointwise u8/u10/u12 responses, so these facts support the stated comparison. This reviewer found no missing sign-changing uncontracted term in the covariant product-rule comparison. The current's particular old realification/phase must remain unchanged.

## Full-R diagnostic: correctly limited

The exact boost leakage into range spin6 and then source spin4 is real. It demonstrates that the previously inverted5/6/7 source bundle is insufficient to claim full-R differentiated closure. It does NOT demonstrate a cokernel obstruction, lack of a local full auxiliary solution, or a need for external source data. A reached spin4 source could be invertible in a further finite invariant module. The proposal states this correctly.

## Scope and integration requirements

- Label Q a restricted test-variation bundle, with its explicit30-real-dimensional construction, not a physical carrier.
- State the analytic upgrade at the fixed W2 candidate and either of the two certified homogeneous roots, on a local timelike-dt patch.
- Carry the product-rule coefficient argument above, especially derivative-of-inclusion, B and density accounting.
- Keep canonical seed/readout/phase custody for the four coefficient intervals. Do not claim all-Gram nonvanishing, remaining Euler dynamics or physical forcing.
- Keep the full-R spin4 successor separate. Do not relabel the restricted-Q proof as a full-R solution or the spin4 leakage as an obstruction.

No additional approval, new action, new physical domain or whole inverse is needed for this scoped mathematical result. Independent specialist review is not external expert certification.


## Additional reviewed corollary: nonzero compact local constrained test variation

**Accepted.** The same argument also closes the local weak-test-support step for this diagnostic; it does not need a global L2 matter domain or a full auxiliary inverse.

Choose one of the certified real Q directions w_p (the appropriate realification of the old highest7 vector). A nonzero Hermitian coefficient matrix has a vector z with nonzero real quadratic polarization z†Hz. The existing noncharacteristic analytic column and independent formal-dual equations realize the prescribed local seeds and fixed phase used by that certificate. These are local solution germs; no positivity or normalizability is claimed.

Extend w_p to a smooth local real section w of Q. The resulting real density coefficient j_eff,Q(w) is continuous and nonzero at p. Shrink the chart so it has one strict sign, retaining timelike dt, both matter germs and the analytic auxiliary coefficients. Pick a nonnegative nonzero compactly supported smooth bump chi there and set

    v=chi w,
    n=-Y_Q^a nabla_a^Q v-Z_Q v,
    u=i_Q v+n.

All fields here are in the declared real variation convention (including the old physical-i factor when represented by real Clifford coefficients). Both v and n are compactly supported, and the exact theorem gives P H u=0. With the same native density, integration by parts has no boundary term and gives

    integral j(u) = integral j_eff,Q(v)
                  = integral chi j_eff,Q(w) != 0.

Only the test perturbation is cut off. The independent matter and dual solutions are not multiplied by a bump and keep satisfying their equations.

This proves a genuine nonzero **local matter-current first-variation functional on compact test connection perturbations satisfying the homogeneous linearized auxiliary constraint**. The phrase must retain that qualifier: no remaining range Euler equation, inhomogeneous sourced/full nonlinear constraint, propagated forced response, physical ghost, physical-domain selection, full-domain positivity or all-Gram robustness follows. The old candidate's stationary bosonic background and held linear matter/dual germs suffice for the stated variational diagnostic.

## Final integrated validation

PASS:438 exact controls,1800 native vector equations; sparse auxiliary replay and Q Gram/reality agree independently; ten new Lean finite lemmas compiled without placeholders. All seven native gates pass. Targeted certificate compilation only, no whole-project rebuild. The corrected source scopes above are retained.
