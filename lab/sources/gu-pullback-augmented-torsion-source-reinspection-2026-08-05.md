---
title: "GU pullback and augmented-torsion source reinspection"
date: 2026-08-05
status: SOURCE_COLLISION_COMPLETE
grade: "Primary-source extraction plus typed comparison to the existing N1/N3 construction. The sources fix augmented torsion as a full adjoint-valued one-form on Y, obtained from two connections and intended to have superior tilted-gauge equivariance. They require an observer pullback to X, but do not publish the exact four-plus-ten Euler receiver, defect localization, moving-section Ward/BV identity, or common analytic domain constructed or held open here."
---

# GU pullback and augmented torsion source reinspection

## Question

The preceding receiver wave left three routes: prove the source-action Euler
image horizontal, reduce the action to a codimension-ten defect and vary it,
or retain ten normal equation components. Before choosing, this pass asks what
Weinstein's released material means by **augmented torsion** and by **pullback**.

Layer 0 keeps these objects distinct:

1. ordinary torsion;
2. contorsion;
3. augmented torsion, a difference of two connections on `Y`;
4. differential-form pullback along an observation section;
5. restriction of the coefficients of a one-form to the vertical bundle; and
6. the equation-dual map forced by the chosen field variables.

## Checked source rows

| source | locator | source content | disposition |
| --- | --- | --- | --- |
| Weinstein 2021 draft, transcribed in the primary-source pack | WGS-01, equations reproduced at pack lines 76--112 | `T_omega=varpi-epsilon^{-1}d_0 epsilon` is in `Omega1(Y,ad P)`; the bosonic action contains the quadratic `kappa_1/2` term and its displayed translation variation is `Upsilon^B=odot F_A+*kappa_1 T` | `SOURCE-CONFIRMS` the full upstairs carrier, action term, and displayed full translation-direction variation |
| Portal lecture | `02:27:46--02:28:42` | the inhomogeneous group gives a bi-connection; the difference of the two connections is an honest adjoint-valued one-form | `SOURCE-CONFIRMS` the two-connection carrier |
| Portal lecture | `02:32:38--02:33:13` | the shared inhomogeneous defect cancels in the difference; augmented torsion is relatively well behaved under the tilted embedding | `SOURCE-CONFIRMS` the intended equivariance mechanism, not a complete Ward theorem |
| Portal lecture | `02:40:19--02:41:48` | the Einsteinian replacement lives on `Y` and must be pulled back to `X`; the metric section observes upstairs content | `SOURCE-CONFIRMS` an observation obligation, without specifying an Euler-dual functor |
| Weinstein--Jaimungal 2025 | `00:29:45--00:30:49` | the observerse is the whole package of spaces, fibres, bundles, sections, relationships and pullbacks, not just the total space | `SOURCE-CORRECTS` a pullback-only reading of observation |
| Weinstein--Jaimungal 2025 | `01:29:19--01:29:47` | one Standard Model generation is described as a pullback of an upstairs Weyl spinor | `SOURCE-CONFIRMS` field/spinor pullback; it is not an equation-receiver formula |
| Weinstein--Jaimungal 2025 | `02:18:44--02:19:49` | ordinary torsion and contorsion are rejected in favour of using the gauge-rotated Levi-Civita connection in the contorsion slot, for improved inhomogeneous-gauge equivariance | `SOURCE-CONFIRMS` the augmented-torsion motivation |
| UCSD / Into the Impossible transcript | `00:20:xx--00:23:02` in local transcript paragraphs 71--80 | use any connection minus the gauge-transformed Levi-Civita connection; the two connection actions form the inhomogeneous group; the result is called a distortion with superior equivariance | `SOURCE-CONFIRMS` the modern spoken version |
| 2021 draft formalization candidates | sections 4 and 5, local lines 82--92 and 170--185 | `Y`-native fields are pulled to `X` as invasive fields; the connection decomposes under the chimeric splitting | `SOURCE-GUIDES` retaining both horizontal and vertical coefficient sectors |
| existing N1 construction | section 2.2, local lines 231--258 | `A_X=s^*A` and `v_s=res_s^V(A-A_0)` are separate maps; the latter is explicitly not differential-form pullback | `REPO-CONFIRMS` the needed vertical coefficient map already exists |
| existing N3 construction | moving-defect derivative, local lines 338--360 | the first variation contains both intrinsic defect variation and support motion | `REPO-CONFIRMS` that honest localization is an existing route rather than a new proposal |

## What the source fixes

The source-native object is not four-dimensional contorsion supplied in
advance. It is the full upstairs one-form

\[
T_\omega\in\Omega^1(Y,\operatorname{ad}P),
\]

built as the difference of two connections. The public motivation is that the
two affine transformation defects cancel in the difference, producing better
equivariance under the tilted subgroup. The 2021 action varies this object in
directions `varpi+s alpha`; no horizontal restriction on `alpha` is stated in
the displayed formula.

The observerse sources also do not reduce observation to the literal pullback
of every differential form. Weinstein calls the observerse a package of
spaces, fibres, sections, bundles, relationships and pullbacks. In the draft's
native/invasive grammar, connection data decomposes before or while it is
observed. This is consistent with retaining

\[
T_X=s^*T_\omega,
\qquad
v_T=\operatorname{res}_s^V T_\omega,
\]

the exact pair already present in N1.

## Source collision

The reinspection changes the successor route in two ways.

First, a naive statement that “pullback loses the ten normal components” is
incomplete. Ordinary form pullback loses them, but the source object is a
connection difference and the repo already has the separate vertical
coefficient restriction needed to retain them. Along a supplied section, the
pair `(s*,res_s^V)` is therefore the most source-compatible existing field
map to test before adding any new normal field or projector.

Second, the source does not support automatic horizontality of the action
image on the full displayed local translation domain. For nonzero `kappa_1`,
the explicit quadratic augmented-torsion term can emit a conormal Euler row
even when the constant one-generator curvature contribution vanishes. This is
a construction-level consequence of the published action, not a claim that
every admissible global source domain contains that local witness.

## Exact disposition

- `SOURCE-CONFIRMS`: augmented torsion is a full adjoint-valued one-form on
  `Y`; it is a two-connection difference; its intended tilted-equivariance;
  the nonzero-`kappa_1` term and the displayed translation variation; the need
  to observe/pull upstairs content to `X`.
- `SOURCE-CORRECTS-NAIVE-READING`: pullback is part of an observer package and
  is not permission to erase the vertical coefficient sector.
- `SOURCE-GUIDES`: combine ordinary section pullback with the existing
  vertical coefficient restriction; interpret the resulting ten coefficients
  only as vertical scalar-like fields until their representation and vacuum
  role are proved.
- `SOURCE-SILENT`: the exact bundle isomorphism `(s*,res_s^V)`, its
  inverse-transpose Euler receiver, the vertical-density/current operation,
  the full moving-section Ward/BV identity, global tilted descent, a common
  Green domain, and a physical Higgs or Standard Model identification.

Curt's explanatory track remains formally separate guidance inside the Eric
lane. No Curt formula is promoted to an Eric identity. P1, P2 and P3 do not
supply or select the receiver in this pass.
