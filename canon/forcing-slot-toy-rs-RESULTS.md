---
title: "Four forcing-slot comparators do not derive three; the reconstructed K3 plus Pati-Salam/HP2 sum is distinct from source-native 2+1"
status: active
doc_type: result
created: 2026-06-29
grade: "computed + adversarially verified. 8 python scripts in tests/forcing-slot/ (4 construct + 2 decomposition + 2 independent adversarial rechecks); the two decisive scripts re-run inline in the main loop and reproduced exactly. 4 angles x (construct + independent from-scratch refutation). The adversary did real work: it knocked down two oversold 'A-mechanism is real' claims -- the +256 projector-sandwich artifact (genuine physical-sector index = 0) and the flat-16 gravitational-only chirality. Verdict: Horn B; the tested integers are not3; A index residues vanish mod3; no 3 fabricated; the suspect +8 RS leg never appeared (forward computation gives -42, -672, 256, 0)."
method: "forcing-slot workflow wf_bff346ca-69d: 4 construct angles (BRST/FP stabilization; twisted spin-3/2 index on K3; RS frame-index operator on the Cl(9,5)=M(64,H) substrate; AGW gravitino anomaly 3-primary content) each running python -> independent adversarial verify vs the 4 fabrication patterns -> barrier synthesis. 9 agents, ~696k subagent tokens."
depends_on:
  - canon/single-decider-integer-index-RESULTS.md
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - explorations/firewall-and-two-geometries/firewall-as-obfuscation-and-reverse-engineered-trapdoor-2026-06-29.md
  - canon/two-primary-lemma.md
---

# Forcing-Slot Test -- Campaign Verdict

## Construction scope correction — Joe approved, 2026-11-20

Authority: `joe_direct_chat_2026_11_20_b`; wording correction, with existing
status and grade retained. The Nikulin order-3 **ghost-subtracted** benchmark A
has index -42 and zero rho class. The **geometric gamma-traceless** benchmark B
has index -38 and nonzero classes (0,2,1)/3. The source-native **Krein-graded**
complex remains unidentified at this invariant: retaining ghosts does not
specify their index grading or trace. A/B is a comparison, not an exhaustive
classification of source constructions. Neither residue supplies an integer
family count. Statements below about a binary or sole decider are restricted
to their declared comparison; they do not require building the source action
before testing defined structural subfamilies. Paper and released bytes are
unchanged. See the [approved-scope audit](../explorations/conditional-build/native-complex-order3-fork-2026-11-20.md)
and [follow-up benchmark and map test](../explorations/conditional-build/krein-order3-observation-label-2026-11-20.md).

## 1. Verdict

The toy stabilized twisted Rarita-Schwinger (RS) sector does **not** fill the forcing slot. Across all four
angles -- BRST/Faddeev-Popov stabilization, the twisted spin-3/2 index on K3, the RS frame-index operator on
the Cl(9,5) substrate, and the AGW gravitino anomaly polynomial -- no construction produces a forcing term that
is simultaneously (a) tangential, (b) net-chiral, and (c) non-frame-trivial with a 3-primary net-chiral integer.
The campaign lands on **Horn B**. The most generous defensible reading is the **A-mechanism / B-ontology**
synthesis, and it applies only on the two index angles, where the RS object is genuinely non-frame-trivial and
carries a nonzero signed index; but even there the "A-mechanism" is partial (the net-chiral leg is gravitational
or tautological, not a genuine Spin(10)-chiral asymmetry), and the tested integers are not3. The A-derived index residues vanish mod3;
this does not make the integers 2-primary. A strict reading collapses to plain Horn B. The trapdoor, where it opens
at all, opens onto the wrong arena. The count is not derived from the geometry; it is issued.

## 2. Forcing-slot table -- RS frame-index operator (campaign headline object)

The RS frame-index operator `O_RS = sum_{mu,nu in TX^4} |mu><nu| (x) gamma_mu gamma_nu` on the verified bridge
(N=14 frame factor, DIM=128 quaternionic spinor, V(x)S=1792), untwisted and twisted by the chiral 16 of
internal Spin(10). Controls reproduced first: Lambda^2_+ carrier frame charge 33.94 / net chirality 0;
chiralizer C=J.G frame charge 0.00 / net chirality +96.

| Property | Verdict | Measured number | What it means |
|---|---|---|---|
| (a) TANGENTIAL | **no** | frame charge 48.0 (untw) / 33.94 (tw), but net self-dual SD-ASD = 0 exactly (SD=ASD=24.0 untw; 16.971/16.971 tw) | Touches the frame but carries **no net p_1**; cannot feed the -p_1/24 channel where the order-3 lives. Contrast genuine carrier Lambda^2_+: SD 33.94 / ASD 0.00, net self-dual 33.94. |
| (b) NET-CHIRAL | **partial / refuted** | physical-sector index = 0 for every grading (twisted and untwisted); operator trace Tr(gamma5_int . O_RS_tw) = +256 | The legitimate physical-sector measure (the one that correctly returns +96 for the chiralizer control) returns 0. The +256 is a graded operator trace, not a net index (see sec. 3). |
| (c) NON-FRAME-TRIVIAL | **yes** | frame charge 48.0 (untw) / 33.94 (tw); Hermitian dev 0.0 | The vector index couples the frame off-diagonally; genuinely **not** of the form id_14 (x) U. This is the one leg the linear operators could not combine with chirality. |

**Achieves: (c) cleanly; (a) and a genuine (b) both fail.** At most one-and-a-half of three. This matches the
campaign ceiling: the best any object reaches is two of three -- Lambda^2_+ gives (a)+(c) but is vectorlike (no
b); the chiralizer gives (b) but is frame-trivial (no c); the RS operator gives (c), a contested (b), and fails
(a).

## 3. The net-chiral integer and its primary decomposition

Three integers were produced across the angles; none is 3.

- **RS frame operator twist: 256 = 2^8.** 3-part = 1 (= 3^0, zero order-3). Purely 2-primary. Forward
  decomposition +256 = |TX^4| * Tr(gamma5_int . P16) = 4 * 64. This is a **projector-sandwich trace**, not a
  measured asymmetry: after the P16 sandwich the operator lives only on the +chirality sector (minus-sector
  content deleted), so gamma5 acts as +1 and the trace returns +dim(+sector) = 64 by construction. n+ = 64,
  n- = 0 is forced, not measured.
- **Twisted spin-3/2 on K3: -672 = -2^5 . 3 . 7** (pure gravitino -42 = -2 . 3 . 7). Divisible by3 as an integer; zero Z/3 component after reduction mod24. Cross-checked against the repo's `rs_k3_symbol_index` q=-1 branch (-672, match).
- **AGW gravitino RS index on K3: -42 = -2 . 3 . 7**, mod 24 = 6 -> CRT (6 in Z/8, 0 in Z/3). Across the
  manifold scan: K3 -42, K3#K3 -84, T^4 0 (all == 0 mod 3); HP^2 -1 (unit, the twisted-Dirac escape "1"). Every
  spin-3/2 polynomial coefficient has its only factor 3 in the **denominator** (von Staudt-Clausen of Ahat);
  `rs_numerator_3_anywhere = False`.

**Is the integer 3? No, on every angle.** 256 has no factor of 3 at all. The -42 / -672 family carries only
3^1, and that 3 is the Hirzebruch signature factor p_1 = 3 sigma, which is homotopy-fixed (identical for 1, 3,
or 5 generations) and carries no generation number.

**Disguised-chi (K3 chi = 24) check, by name:** the only integer-level 3 anywhere is the signature-3 in
p_1 = 3 sigma. On K3 this equals -2 chi via 2 chi + 3 sigma = 0 (chi = 24, sigma = -16), so -672 = -28 chi and
-42 = -7 chi/4 **exactly**. The `twisted-rs-k3` construct called this "coincidental"; that characterization is
**false** and was corrected by the adversary -- the chi-route is structurally forced. It does not, however,
manufacture a fabricated 3: the integer is -672 / -42, not 3, and its 3-part is generation-independent. The 256
from the RS frame operator is not divisible by 24 (256/24 is non-integer) and has no chi route. No
2 chi + 3 sigma = 0 relation was invoked to produce any reported count.

## 4. Mechanism -- why the slot is empty

Each angle fails a different leg, and the failures are structural, not incidental:

- **BRST/FP** fails (a) and (b). The Faddeev-Popov operator is the ghost Dirac operator gamma^mu D_mu = c(xi):
  the gamma-trace **contracts the frame index away**, leaving a 128x128 operator on the spinor with no free
  vector index, so its lift id_14 (x) c(xi) is frame-trivial (frame charge 0). And ghost subtraction is
  chirality-symmetric -- the ghost carries the same chiral rep as the gauge variation, so equal numbers of n+
  and n- are removed; every RS-minus-ghost net-chiral integer is 0, even under the chiral-16 twist. Two of
  three at best, and decisively no (b).
- **RS frame-index operator** gives (c) for real (the vector index is genuinely off-diagonal, not id_14 (x) U)
  but the **gauge/frame coupling is vectorlike**: SD = ASD exactly, net self-dual = 0, so no net p_1 -- (a)
  fails. The twist buys a nonzero (b) only as a tautological projector trace (256 = 2^8); the honest
  physical-sector index is 0.
- **The index angles (twisted-spin-3/2, AGW)** are the place (a), (b), (c) come closest to co-existing -- the
  RS field is tangential (the density is exactly 7 p_1 / 8), net-chiral (a genuine signed index), and
  non-frame-trivial (the vector character ch(TM_C), not an internal id (x) U). But the integer is
  not3, with A indices ==0 mod3 and a separate HP2 unit control. The actual **twisted-by-16**
  object too: index = 16(-42) + 3 ch2(V) == 0 mod 3 for every integer twist. The trapdoor stays shut even for
  the real object.

**Scoped comparison:** none of the tested integers is3. The A indices are
divisible by3, not 2-primary integers. This does not rule out a located
order-3 invariant in another construction: geometric Q already supplies one.
Nor would a nonzero mod-3 residue equal integer3, whose residue is0.

## 5. Integrity note

**No 3 was fabricated.** Every integer produced is honestly not 3, and the gated/empty result is reported as
such.

Fabrication flags that surfaced, and how they were handled:

- **twisted-rs-k3 (3 flags):** (i) disguised-chi mislabel -- "-672 = 24 . -28 coincidental" is false; it is
  forced via 2 chi + 3 sigma = 0. Corrected; does not yield a fabricated 3. (ii) net-chiral overclaim -- the
  "twist by the chiral 16" uses a **flat** bundle (ch2F = 0), which is vectorlike; the -42 net-chirality is
  purely gravitational, not Spin(10)-chiral. (iii) non-frame-trivial asserted in the 4-dim SO(4) tangent of K3,
  not measured in the campaign's 14-dim frame factor -- category mismatch. Net effect: the angle's "A-mechanism
  is real" half is only partially supported; the bottom line (integer not 3, slot empty) survives.
- **rs-frame-charge-substrate (2 flags):** oversold net-chiral leg (headline switched from the physical-sector
  index = 0 to the weaker graded trace +256 to manufacture a nonzero b); tautological integer
  (256 = 4 . Tr(gamma5 . P16) is a projector trace carrying zero asymmetry information). Adversary pushed the
  verdict from "A-mechanism-B-ontology" to **Horn B**. The 256 itself is fabrication-clean (genuinely 2^8, no
  factor 3, forward-derived).
- **agw-gravitino (1 flag):** disguised-chi present and **self-caught** -- the lone factor 3 is the
  signature/chi-route 3, flagged by the construct itself; reverse-engineered-+8, circular-rank-4, and
  fitted-holonomy all genuinely clean (forward computation gives -42, not +8; no rank injected; cross-checks
  sig(HP^2)=1 and Ahat(HP^2)=0 reproduced).
- **brst:** fabrication sweep clean, no flags.

In every case the suspect "+8 RS leg" never appeared: the honest forward computations give -42, -672, 256, and
0 -- conspicuously not 3 and not +8.

**Computed vs analytic.** All load-bearing numbers were **computed** -- the workflow re-ran the scripts under
Python 3.14.3 in `tests/forcing-slot/`, and the two decisive scripts (`agw_gravitino_3primary.py`,
`rs_index_carrier_arena_scan.py`) were re-run a third time inline in the main loop and reproduced exactly
(`rs_numerator_3_anywhere = False`, `rs_index_K3 = -42`, `spin_half_index_K3 = 2`, `{K3:-42, T^4:0,
K3#K3:-84}` all == 0 mod 3, `HP^2 = -1`). The single **analytic, not computed** quantity is the
non-frame-trivial leg of the AGW angle (the construct admits "not re-measured numerically in this angle"); it
is, however, directly **measured** in the rs-frame-charge-substrate angle (frame charge 48.0 / 33.94), so the
property is not left unsupported campaign-wide.

## 6. What it does to the paper

The four named comparators did not derive the count. The ghost-subtracted
index calculation constrains A and its stated twists; geometric Q is a
different complex. These calculations neither identify the source's observed
carrier nor refute its native2+1 mechanism. Paper revisions remain staged for
Joe; this approved correction changes only this canon-side wording.

The non-flat16-twist remains a comparison with index16(-42)+3ch2(V), always
0mod3. Choosing ch2(V)=225 would fit index3, not derive it. Divisibility alone
does not exclude integer3. No source-action construction is authorized here.

## 7. The reconstructed K3 plus Pati-Salam/HP2 sum (not source-native2+1)

The campaign once framed the count as "2+1 effective": the **"2"** = `A-hat(K3) = 2` (arriving through the
spin-1/2 / Dirac leg), the **"1"** = Pati-Salam `Spin(7,7) -> 16` chiral = one anomaly-free generation. The
open question was whether `2 + 1 = 3` is a single legitimate computation or numerology from adding two numbers
that live in different frameworks. This workflow answers it as a byproduct, because two angles compute the
spin-1/2 **and** spin-3/2 indices in the **same** framework (the character-valued index on K3):

- spin-1/2 Dirac index on K3 = **2** (the "2"; `spin_half_index_K3 = 2`, verified control).
- ghost-subtracted A gravitino index on K3 = **-42 = -2 . 3 . 7**, which is **== 0 mod 3** (the Z/3 identity).

So when the RS sector -- the natural candidate to host the missing leg -- is placed in the *same* framework as
the "2", it does **not** supply a clean +1 to complete `2 + 1 = 3`. It supplies -42. The "+1" appears only as
the twisted-Dirac **unit** (HP^2 RS index = -1; or the Pati-Salam branching) -- a **different**
framework/manifold from the "2". The `dim4_RS_indices` scan confirms the RS leg is `== 0 mod 3` on every spin
4-manifold (K3 -42, T^4 0, K3#K3 -84; lemma for A: index = 21 sigma/8, the factor 21 = 3.7 forcing == 0 mod 3),
never a clean +1 sitting alongside the "2".

**Conclusion on this reconstructed sum:** the K3 Dirac2 and Pati-Salam/HP2
unit are not a single demonstrated count. This is not SC-GEN-02/03/50's
observation-based2+1 mechanism. The finite CRT theorem retains its own scope;
neither it nor this A comparison rules out every source-native construction.

---

Files: all anchor scripts in `tests/forcing-slot/` (`rs_frame_index_operator.py`, `agw_gravitino_3primary.py`,
`twisted_spin32_index_k3.py`, `rs_index_carrier_arena_scan.py`, `brst_fp_stabilization_sector.py`,
`rs_net_chiral_decomposition.py`, plus the adversarial rechecks `adv_verify_brst.py`,
`adv_verify_rs_independent.py`). Workflow run id wf_bff346ca-69d.
