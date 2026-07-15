# DESI and Late-Time Dark Energy in CPL Form

This report focuses on the background-only quantities most relevant for testing a CPL equation of state,
\[
w(a)=w_0+w_a(1-a),
\]
with an emphasis on exact published numbers from collaboration papers, release notes, and official data products. Where the literature itself distinguishes between pure BAO distances and model-derived \((w_0,w_a)\) posteriors, I keep those separate. Where a requested exact number was not retrievable from the sources opened in this pass, I say so explicitly rather than guess. citeturn50search8turn21view0turn13view2

## DESI BAO measurements and DESI’s own CPL fits

DESI DR2 BAO is the first three-year BAO release, based on more than 14 million galaxies and quasars. In the DR2 BAO analysis paper, DESI states that the effective volume per redshift bin increased relative to DR1 by factors ranging from 1.8 for QSO to 3.1 for ELG2, with the same redshift binning as DR1, making a direct DR1→DR2 comparison straightforward. citeturn50search8turn17view0

### DESI DR2 BAO distances

All values below are from **Abdul-Karim et al., DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints**, **arXiv:2503.14738**, released with the DR2 BAO papers on **2025-03-19**; distances are from **Table IV**, and sample sizes / effective volumes from **Table III**. citeturn50search16turn17view0turn7view0

| Tracer | Redshift bin | \(z_{\rm eff}\) | \(N_{\rm tracer}\) | \(V_{\rm eff}\) [Gpc\(^3\)] | Measurement |
|---|---:|---:|---:|---:|---|
| BGS | 0.1–0.4 | 0.295 | 1,188,526 | 3.8 | \(D_V/r_d=7.95\pm0.10\) |
| LRG1 | 0.4–0.6 | 0.510 | 1,052,151 | 4.9 | \(D_M/r_d=13.58\pm0.18,\ D_H/r_d=20.97\pm0.53,\ r=-0.469\) |
| LRG2 | 0.6–0.8 | 0.706 | 1,613,562 | 7.6 | \(D_M/r_d=16.84\pm0.24,\ D_H/r_d=20.08\pm0.56,\ r=-0.403\) |
| LRG3+ELG1 | 0.8–1.1 | 0.930 | 4,540,343 | 14.8 | \(D_M/r_d=21.77\pm0.25,\ D_H/r_d=17.83\pm0.31,\ r=-0.390\) |
| ELG2 | 1.1–1.6 | 1.317 | 3,797,271 | 8.3 | \(D_M/r_d=27.56\pm0.53,\ D_H/r_d=13.83\pm0.33,\ r=-0.435\) |
| QSO | 0.8–2.1 | 1.491 | 1,461,588 | 2.7 | \(D_V/r_d=26.10\pm0.45\) |
| Ly\(\alpha\) QSO | 1.8–4.2 | 2.330 | 1,289,874 | — | \(D_M/r_d=39.40\pm0.64,\ D_H/r_d=8.53\pm0.16,\ r=-0.452\) |
| LRG3 only | 0.8–1.1 | 0.932 | 1,802,770 | 9.8 | \(D_M/r_d=21.94\pm0.34,\ D_H/r_d=17.74\pm0.54,\ r=-0.371\) |
| ELG1 only | 0.8–1.1 | 0.928 | 2,737,573 | 5.8 | \(D_M/r_d=21.98\pm0.35,\ D_H/r_d=17.55\pm0.61,\ r=-0.438\) |

These rows come directly from DESI’s DR2 baseline BAO tables. For the anisotropic bins, DESI publishes the correlation coefficient \(r\) between \(D_M/r_d\) and \(D_H/r_d\); the full covariance matrices are distributed in the released BAO likelihood products rather than expanded in the paper. citeturn17view0turn7view0turn50search1

### DESI DR1 BAO distances

All values below are from **Adame et al., DESI 2024 VI: Cosmological Constraints from Measurements of Baryon Acoustic Oscillations**, **arXiv:2404.03002**, **Table 1** and **Table 3**; the exact submission day was not captured in the retrieved lines, but the paper is the April 2024 DESI DR1 BAO cosmology release. citeturn16view0turn13view2

| Tracer | Redshift bin | \(z_{\rm eff}\) | \(N_{\rm tracer}\) | \(V_{\rm eff}\) [Gpc\(^3\)] | Measurement |
|---|---:|---:|---:|---:|---|
| BGS | 0.1–0.4 | 0.295 | 300,017 | 1.7 | \(D_V/r_d=7.93\pm0.15\) |
| LRG1 | 0.4–0.6 | 0.510 | 506,905 | 2.6 | \(D_M/r_d=13.62\pm0.25,\ D_H/r_d=20.98\pm0.61,\ r=-0.445\) |
| LRG2 | 0.6–0.8 | 0.706 | 771,875 | 4.0 | \(D_M/r_d=16.85\pm0.32,\ D_H/r_d=20.08\pm0.60,\ r=-0.420\) |
| LRG3+ELG1 | 0.8–1.1 | 0.930 | 1,876,164 | 6.5 | \(D_M/r_d=21.71\pm0.28,\ D_H/r_d=17.88\pm0.35,\ r=-0.389\) |
| ELG2 | 1.1–1.6 | 1.317 | 1,415,687 | 2.7 | \(D_M/r_d=27.79\pm0.69,\ D_H/r_d=13.82\pm0.42,\ r=-0.444\) |
| QSO | 0.8–2.1 | 1.491 | 856,652 | 1.5 | \(D_V/r_d=26.07\pm0.67\) |
| Ly\(\alpha\) QSO | 1.77–4.16 | 2.330 | 709,565 | — | \(D_M/r_d=39.71\pm0.94,\ D_H/r_d=8.52\pm0.17,\ r=-0.477\) |

The headline DR1→DR2 change is not a large shift in the central distance ladder, but a substantial tightening. For example, BGS improved from \(7.93\pm0.15\) to \(7.95\pm0.10\), LRG1 \(D_M/r_d\) from \(13.62\pm0.25\) to \(13.58\pm0.18\), and QSO \(D_V/r_d\) from \(26.07\pm0.67\) to \(26.10\pm0.45\); those are all consistent central values with noticeably smaller DR2 errors. citeturn16view0turn7view0

### DESI’s own \(w_0w_a\)CDM constraints

For DR2, the relevant numbers come from **Table V** and the preference over flat \(\Lambda\)CDM from **Table VI** / **Figure 11** of **Abdul-Karim et al. 2025**, **arXiv:2503.14738**. citeturn21view0turn22view3turn23view0

| Data combination | \(w_0\) | \(w_a\) | Reported preference over flat \(\Lambda\)CDM |
|---|---:|---:|---:|
| DESI BAO alone | \(-0.48^{+0.35}_{-0.17}\) | \(< -1.34\) at 68% | \(1.7\sigma\) |
| DESI + CMB | \(-0.42\pm0.21\) | \(-1.75\pm0.58\) | \(3.1\sigma\) |
| DESI + CMB + Pantheon+ | \(-0.838\pm0.055\) | \(-0.62^{+0.22}_{-0.19}\) | \(2.8\sigma\) |
| DESI + CMB + Union3 | \(-0.667\pm0.088\) | \(-1.09^{+0.31}_{-0.27}\) | \(3.8\sigma\) |
| DESI + CMB + DESY5 | \(-0.752\pm0.057\) | \(-0.86^{+0.23}_{-0.20}\) | \(4.2\sigma\) |

The corresponding DR2 nuisance-resolved context is equally important: DESI reports that **most of the role of the CMB anchor is to fix \(\Omega_m\)**, and that replacing the full CMB likelihood with a simple early-Universe prior on \((\theta_*,\omega_b,\omega_{bc})\) leaves the central \(w_0,w_a\) values very similar while reducing the formal rejection of \(\Lambda\)CDM from \(3.1\sigma\) to \(2.4\sigma\). They also state that **Pantheon+ does not strengthen the preference relative to DESI+CMB**, because its low-\(z\) distance-modulus trend lies closer to the \(\Lambda\)CDM prediction than Union3 or DESY5. citeturn27view1turn27view0turn27view2

For DR1, DESI’s own published \(w_0w_a\) values are in **Table 3** of **Adame et al. 2024**, **arXiv:2404.03002**, and the SNe-dependent significances are given in **Figure 6**. citeturn13view2turn13view3

| Data combination | \(w_0\) | \(w_a\) | DESI-stated preference over flat \(\Lambda\)CDM |
|---|---:|---:|---:|
| DESI BAO alone | \(-0.55^{+0.39}_{-0.21}\) | \(< -1.32\) at 68% | mild; DESI did not tabulate a single sigma in Table 3 |
| DESI + CMB | \(-0.45^{+0.34}_{-0.21}\) | \(-1.79^{+0.48}_{-1.0}\) | not tabulated as a single sigma in Table 3 |
| DESI + CMB + Pantheon+ | \(-0.827\pm0.063\) | \(-0.75^{+0.29}_{-0.25}\) | \(2.5\sigma\) |
| DESI + CMB + Union3 | \(-0.65\pm0.10\) | \(-1.27^{+0.40}_{-0.34}\) | \(3.5\sigma\) |
| DESI + CMB + DESY5 | \(-0.727\pm0.067)\) | \(-1.05^{+0.31}_{-0.27}\) | \(3.9\sigma\) |

So, on DESI’s own numbers, the DR1→DR2 shift is not that the signal suddenly appears only after supernovae. In DR2, **DESI+CMB alone already reaches \(3.1\sigma\)**, while the addition of SNe shifts the posterior differently depending on which compilation is used: Pantheon+ pulls toward less-evolving DE than either Union3 or DESY5. citeturn22view3turn13view3

## CMB anchors and sound-horizon calibration

### Planck 2018 baseline

For the standard Planck 2018 baseline, the clearest single reference remains **Planck Collaboration VI (2020), arXiv:1807.06209**, using **Planck TT,TE,EE+lowE+lensing**, with the core parameters from **Table 2** and the acoustic scale also quoted explicitly as Eq. (9). citeturn31view0

| Quantity | Value | Source |
|---|---:|---|
| \(100\,\theta_*\) | \(1.04109\pm0.00030\) | Eq. (9), TT,TE,EE+lowE citeturn31view0 |
| \(100\,\theta_{\rm MC}\) | \(1.04092\pm0.00031\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(r_d\) [Mpc] | \(147.09\pm0.26\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(\omega_b=\Omega_b h^2\) | \(0.02237\pm0.00015\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(\omega_c=\Omega_c h^2\) | \(0.1200\pm0.0012\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(\omega_m=\Omega_m h^2\) | \(0.1430\pm0.0011\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(n_s\) | \(0.9649\pm0.0042\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(H_0\) [km s\(^{-1}\) Mpc\(^{-1}\)] | \(67.36\pm0.54\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |
| \(\sigma_8\) | \(0.8111\pm0.0060\) | Table 2, TT,TE,EE+lowE+lensing citeturn31view0 |

### Later Planck reanalyses

The two main “post-2018” Planck reanalyses in use are **PR4/NPIPE with CamSpec** and **PR4 with HiLLiPoP**. The CamSpec PR4 abstract states that PR4/NPIPE gives parameter-level agreement with Planck 2018 and about **10% tighter** constraints, while the HiLLiPoP PR4 paper gives an explicit \(\Lambda\)CDM table. citeturn28search2turn29search1

For **HiLLiPoP PR4 TTTEEE**, **Tristram et al. (2024), A&A 682 A37, arXiv:2309.10034**, **Table 3** gives: \(\omega_b=0.02226\pm0.00013\), \(\omega_c=0.1188\pm0.0012\), \(100\theta_*=1.04108\pm0.00026\), \(n_s=0.9681\pm0.0039\), \(H_0=67.64\pm0.52\), \(\sigma_8=0.8070\pm0.0065\), and \(\Omega_m=0.3092\pm0.0070\). The same paper states that adding PR4 lensing gives the “best of PR4” CMB-only Planck combination, and compares its curvature result directly to **CamSpec PR4**, finding that CamSpec PR4 preferred \(\Omega_K=-0.025^{+0.013}_{-0.010}\), while HiLLiPoP PR4 moved that toward \(-0.0078\pm0.0058\). citeturn35view0turn36view0turn36view4

A practical point for reproduction: the HiLLiPoP PR4 paper does **not** tabulate \(100\theta_{\rm MC}\) or \(r_d\) in its main \(\Lambda\)CDM table; those are obtainable from the released PR4 chains rather than from Table 3 itself. citeturn35view0turn50search6

### ACT DR6 and SPT-3G D1

For ACT DR6, the most useful pure-CMB anchor in the newest official paper is the **P-ACT** combination in **ACT DR6 Power Spectra, Likelihoods and \(\Lambda\)CDM Parameters** (Louis et al. 2025), whose **Table 9** gives \(\theta_{\rm MC}=0.0104073\pm0.0000025\), i.e. \(100\theta_{\rm MC}=1.04073\pm0.00025\), \(\omega_b=0.02250\pm0.00011\), \(\omega_c=0.1193\pm0.0012\), \(n_s=0.9709\pm0.0038\), \(H_0=67.62\pm0.50\), \(\sigma_8=0.8149\pm0.0063\), \(\theta_*=1.04094\pm0.00025\), and \(r_d=147.14\pm0.29\) Mpc. The same table also gives the BAO+lensing-augmented **P-ACT-LB** row, which is no longer a pure CMB anchor but yields \(H_0=68.22\pm0.36\) and \(r_d=147.45\pm0.23\) Mpc. citeturn39view0turn38view0

For SPT, the newest high-\(\ell\) cosmology paper is **Camphuis et al., SPT-3G D1**, **arXiv:2506.20707**. Its **Table I** gives the SPT-3G-only combination (which includes T&E, SPT lensing, and a Planck PR4 \(\tau\) prior): \(10^4\theta_s=104.171\pm0.060\), i.e. \(100\theta_*=1.04171\pm0.00060\), \(\omega_b=0.02221\pm0.00020\), \(\omega_c=0.1214\pm0.0016\), \(n_s=0.951\pm0.011\), \(H_0=66.66\pm0.60\), \(r_d=146.92\pm0.47\) Mpc, \(\Omega_m=0.3246\pm0.0091\), and \(\sigma_8=0.8158\pm0.0058\). The same table’s combined **CMB-SPA** row for Planck+SPT+ACT tightens this to \(H_0=67.24\pm0.35\), \(r_d=147.07\pm0.22\) Mpc, and \(\sigma_8=0.8137\pm0.0038\). citeturn43view0turn42view0

### What counts as the CMB–BAO “sound-horizon tension”

Strictly speaking, BAO by itself measures **distances divided by \(r_d\)**, or equivalently combinations such as \(H_0r_d\), not \(r_d\) alone. DESI DR2 therefore frames the issue as a **BAO–CMB tension within flat \(\Lambda\)CDM**: for DR2 BAO alone, DESI finds \(\Omega_m=0.2975\pm0.0086\) and \(h\,r_d=(101.54\pm0.73)\,\mathrm{Mpc}\), with a correlation coefficient \(r=-0.92\), and says the BAO-preferred parameters are in **mild \(2.3\sigma\)** tension with the CMB in flat \(\Lambda\)CDM. The new SPT-3G D1 analysis goes further and states a **\(2.8\sigma\)** discrepancy between combined CMB and DESI DR2 BAO in the \(\Omega_m\)–\(h r_d\) plane. citeturn20view0turn44search6turn43view0turn42view0

## Supernova samples and why they move the contour

### Sample definitions and DESI-combined CPL constraints

DESI DR2 combines its BAO likelihood with each SN sample separately. The exact DR2 combined results are the ones in the table above: Pantheon+ gives \((w_0,w_a)=(-0.838\pm0.055,\,-0.62^{+0.22}_{-0.19})\), Union3 gives \(( -0.667\pm0.088,\,-1.09^{+0.31}_{-0.27})\), and DESY5 gives \(( -0.752\pm0.057,\,-0.86^{+0.23}_{-0.20})\). citeturn21view0turn22view3

The three SN compilations are not interchangeable. **Pantheon+** is the largest of the three legacy compilations with **1701 light curves of 1550 distinct SNe Ia spanning \(z=0.001\) to \(2.26\)** in the official Pantheon+ cosmology paper. **Union3** contains **2087 cosmologically useful SNe Ia from 24 datasets** in the official Union3 / UNITY1.5 paper. **DES-SN5YR** reports **1635 DES SNe passing quality cuts in \(0.10<z<1.13\)** in the main DES five-year cosmology paper; the DES cosmology analysis then uses this with a low-\(z\) anchor sample. citeturn45search4turn47view0turn45search10

| SN compilation | Official sample statement | DESI DR2 + CMB result |
|---|---|---|
| Pantheon+ | 1701 light curves, 1550 distinct SNe Ia, \(z=0.001\)–2.26; Brout et al. 2022, arXiv:2202.04077 | \(w_0=-0.838\pm0.055,\ w_a=-0.62^{+0.22}_{-0.19}\) citeturn45search4turn21view0 |
| Union3 | 2087 cosmologically useful SNe Ia from 24 datasets; Rubin et al. 2025, arXiv:2311.12098 | \(w_0=-0.667\pm0.088,\ w_a=-1.09^{+0.31}_{-0.27}\) citeturn47view0turn21view0 |
| DES-SN5YR | 1635 DES SNe in \(0.10<z<1.13\) passing quality cuts; DES Collaboration 2024, arXiv:2401.02929 | \(w_0=-0.752\pm0.057,\ w_a=-0.86^{+0.23}_{-0.20}\) citeturn45search10turn21view0 |

### Why the three SN samples pull differently

DESI’s own DR2 interpretation is very explicit on the mechanism. The collaboration says the SN leverage on \(w(z)\) comes mainly from the **comparison of low-redshift (\(z<0.1\)) and higher-redshift (\(z>0.1\)) supernovae**. For \(z>0.1\), DESI’s best-fit \(\Lambda\)CDM model is already a reasonable fit to the SNe. The different pull comes from the **low-\(z\)** calibration part of the Hubble diagram: DESI says DESY5 and Union3 clearly favor the \(w_0w_a\)CDM prediction, while Pantheon+ lies closer to \(\Lambda\)CDM, so adding Pantheon+ to DESI+CMB does not strengthen the evolving-DE preference, whereas Union3 and DESY5 do. citeturn27view0turn27view2

That interpretation is backed up by the direct DESI robustness tests in DR2. In Figure 14, DESI shows that **removing \(z<0.1\) DESY5 SNe greatly enlarges the uncertainties but only weakly shifts the best-fit \(w_0,w_a\)**, which DESI reads as evidence that the contour location is not being set by a handful of nearby objects, even though the statistical significance is. citeturn27view0turn27view1

The strongest comparison paper on Pantheon+ versus DES-SN5YR is **Vincenzi et al. (2025)**, which concludes that the Pantheon+–DES-SN5YR offset is **mostly due to different Malmquist-bias corrections**, and that DES-SN5YR used an improved SN-Ia luminosity-scatter model relative to Pantheon+, with the corresponding scatter-model uncertainty propagated in its error budget. In other words, the shift is not best interpreted as “one sample is right, one sample is wrong,” but as a concrete analysis-choice difference in selection-bias treatment. citeturn45search3turn45search7

The later **Union3.1** host-mass reanalysis strengthens this point. Hoyt et al. (2026) find that low-\(z\) host masses in Union3 and Pantheon+ were biased in opposite directions; after re-deriving host properties self-consistently, the **previously \(>0.03\) mag** low-\(z\) discrepancy shrinks to **0.01 mag**, and the DESI-combined CPL significances move closer together: Union3.1 gives \(w_0=-0.719\pm0.084,\ w_a=-0.95^{+0.29}_{-0.26}\), corresponding to **\(3.4\sigma\)** rather than **\(3.8\sigma\)** against a cosmological constant. The same paper says that updating Pantheon+ and DES-SN5YR calibrations yields **\(3.2\sigma\)** and **\(3.4\sigma\)**, respectively, improving cross-sample consistency. citeturn46search3

The bottom line is that the evolving-DE preference is **not absent** in all but one SN sample. It is present in all three DESI DR2 combinations, but the **strength is sample-dependent**, and the clearest currently identified driver of that dependence is **low-\(z\) SN calibration and selection-bias treatment**, not a large disagreement in the redshift evolution at \(z\gtrsim0.1\). citeturn22view3turn27view0turn45search3turn46search3

## Independent BAO cross-checks before DESI

Before DESI, the strongest BAO ladder came from low-\(z\) 6dFGS / SDSS MGS and the final SDSS BOSS/eBOSS program. In the retrieved sources, the exact pre-DESI values I could verify are the following. Where I could not retrieve the exact table page in this pass, I say so.

| Dataset | \(z_{\rm eff}\) | Published BAO observable |
|---|---:|---|
| 6dFGS | 0.106 | \(D_V=456\pm27\) Mpc; equivalently \(r_s(z_d)/D_V=0.336\pm0.015\) |
| SDSS MGS (DR7) | 0.15 | \(D_V=(664\pm25)\,(r_d/r_{d,\rm fid})\) Mpc |
| SDSS/eBOSS LRG+ELG | 0.70 | \(D_M/r_d=17.96\pm0.51,\ D_H/r_d=21.22\pm1.20\) |
| SDSS/eBOSS LRG+ELG | 0.845 | \(D_M/r_d=18.90\pm0.78,\ D_H/r_d=20.91\pm2.86\) |
| SDSS LRG, as quoted in DESI DR1 comparison | 0.51 | \(D_M/r_d=13.26\pm0.25,\ D_H/r_d=22.33\pm0.58\) |
| SDSS LRG, as quoted in DESI DR1 comparison | 0.70 | \(D_M/r_d=17.86\pm0.33,\ D_H/r_d=19.33\pm0.53\) |

The 6dFGS and MGS low-\(z\) values above come from the survey BAO papers themselves. The two \(z=0.70\) and \(z=0.845\) values are from the eBOSS multi-tracer Fourier-space abstract. The \(z=0.51\) and \(z=0.70\) SDSS LRG entries are the exact comparison values DESI reproduced in its DR1 paper when contrasting DESI Year 1 to the earlier SDSS ladder. citeturn51search4turn52search0turn51search0turn14view0

For high redshift, the exact eBOSS **Ly\(\alpha\)** final-paper numbers were **not** retrievable from the opened sources in this pass, but the official final-paper abstract confirms the measurement at **\(z_{\rm eff}=2.33\)** using the full DR16 Ly\(\alpha\) sample. Likewise, the final eBOSS DR16 quasar paper was located, but the exact \(D_V/r_d\) value was not displayed in the abstract snippet I retrieved. For coding a clean pre-DESI cross-check likelihood, those two exact rows should be taken directly from the final DR16 quasar and Ly\(\alpha\) tables. citeturn51search2turn52search2

## What is coming next

### DESI after DR2

The official DESI data-release documentation says DR1 is the first public release and that future public releases continue through the survey program. A later DESI cosmology-release note says that the **DR2 cosmology chains and data products were released on 2025-10-06**, and community presentations in late 2025 described the next large public release as the **5-year** release, available **late 2026 / early 2027**. Fermilab and NOIRLab also announced in April 2026 that DESI had completed its planned 5-year map. citeturn50search0turn50search1turn49search4turn49search8turn49search12

A precise official DR3 \(w_0,w_a\) forecast table was not retrieved in this pass. But if one makes the simplest statistics-dominated scaling from the public **3-year DR2 BAO** sample to the **5-year public release**, then fractional 1D errors should shrink approximately as \(\sqrt{3/5}\approx0.77\), i.e. by about **23%**, and a DETF-like figure of merit would grow by about **\(5/3\approx1.7\)**. That is an inference from survey duration, not a collaboration-published forecast. citeturn50search8turn49search4turn49search8

### Euclid, Roman, and Rubin

For **Euclid**, the clearest current official timing signal is that **DR1 Foundation** is expected in **November 2026**, with **DR1 Complete** in **mid-2027**. Euclid’s own public pages also continue to frame DR1 as the first major survey-data release containing the mission’s core dark-energy products. I did **not** retrieve a single official Euclid mission-page table with a unique CPL FoM number in this pass, so I am not forcing one here. citeturn49search1turn49search9turn49search17

For **Roman**, the strongest exact forecast number I retrieved is from the official Roman multiprobe cosmology paper: the **High Latitude Survey reference program alone can reach a DETF FoM \(>300\)** when all probes are combined. Roman’s mission pages likewise explicitly frame the survey as one designed to measure the dark-energy equation of state and its time evolution. citeturn49search22turn49search6turn53search2

For **Rubin/LSST DESC**, the official Science Requirements Document states that the collaboration’s combined dark-energy probes should achieve a **FoM \(>500\)** with the **full 10-year LSST Y10 dataset**, including both statistical and systematic uncertainties and Stage III priors. That is a requirements-level target rather than a finished-data prediction, but it is still the cleanest official figure of merit target in current public DESC documentation. citeturn53search1turn53search10

The practical answer to your “by how much do the uncertainties shrink, and when?” question is therefore:

- **DESI**: next decisive public step is the 5-year release, likely **late 2026 / early 2027**, with an inference-level expectation of roughly **20–25% smaller background-distance errors** than DR2 if statistics stay dominant. citeturn49search4turn49search8
- **Euclid**: first wide core-science release begins **November 2026**, likely the first external dataset capable of rapidly stress-testing whether the DESI+SN contour geometry persists. citeturn49search1turn49search9
- **Roman**: official multiprobe forecasts remain Stage-IV-class, with **FoM \(>300\)** for the HLS reference survey. citeturn49search22turn53search2
- **Rubin/LSST**: on the full Y10 baseline, DESC’s stated target is **FoM \(>500\)**. citeturn53search1

## Robustness and the current debate

The strongest “signal is real enough to take seriously” case is still the DESI collaboration’s own one. In DR2, DESI stresses that the evidence grows from the internal **DESI+CMB \(3.1\sigma\)** case to **\(4.2\sigma\)** for DESI+CMB+DESY5, and that the central \(w_0,w_a\) location is fairly stable to replacing the full CMB likelihood by a stripped-down early-Universe prior or to excluding \(z<0.1\) DESY5 SNe. DESI also says that removing the evolving-DE signal by changing the DESI BAO measurements themselves would require BAO systematics far larger than any found in their tests. citeturn22view3turn27view1turn27view2

The strongest “it is sample-dependent / calibration-sensitive” case comes from the SN-comparison literature. Vincenzi et al. argue that the Pantheon+–DES-SN5YR offset is mostly a **Malmquist-bias correction** issue, and Hoyt et al. show that host-mass inconsistencies in Union3 and Pantheon+ low-\(z\) galaxies can be reduced enough to bring the two studies to **0.01 mag** agreement at low redshift, with the DESI-combined significance for Union3.1 dropping from **\(3.8\sigma\)** to **\(3.4\sigma\)**. These are not “no signal” results, but they do say the exact sigma count remains calibration-sensitive. citeturn45search3turn46search3

A stronger skepticism appears in **“On DESI’s DR2 exclusion of \(\Lambda\)CDM”**. The key claim there is statistical rather than astrophysical: the DESI paper quotes **2.8σ, 3.8σ, and 4.2σ** for three **overlapping** SN compilations, but those should not be informally combined or averaged as if they were independent evidence. That critique’s preferred “principled” combination gives an overall exclusion significance of about **3.1σ** instead. citeturn46search12

There are also “reanalysis by changed assumptions” papers that try to relax the tension without invoking CPL evolution. The SPT-3G D1 paper emphasizes that the CMB–DESI discrepancy is sensitive to analysis choices in joint fits and finds a **2.8σ** CMB–DESI difference in \(\Omega_m\)–\(h r_d\) within \(\Lambda\)CDM, while DESI’s own neutrino section notes that allowing negative “effective” neutrino masses can reduce the preference for evolving DE, but **not below the level already seen in the BAO+SNe-only combinations**. In other words, these reanalyses reduce the significance, but they do not presently knock it to zero in a broadly accepted way. citeturn42view0turn44search14turn22view4turn27view1

## Reproducibility and direct data access

The most useful official entry points for reproducing the exact likelihood-level comparisons are these.

```text
DESI DR1 release page
https://data.desi.lbl.gov/doc/releases/dr1/

DESI DR2 BAO paper guide
https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

DESI DR2 cosmology chains and data products release
https://www.desi.lbl.gov/2025/10/06/desi-dr2-cosmology-chains-and-data-products-released/

Planck Legacy Archive
https://pla.esac.esa.int/

Planck 2020 NPIPE products at NERSC
https://portal.nersc.gov/project/cmb/planck2020/

Cobaya Planck likelihood documentation
https://cobaya.readthedocs.io/en/latest/likelihood_planck.html

Pantheon+ public data release
https://github.com/PantheonPlusSH0ES/DataRelease

Union3 data files distributed through Cobaya SN data
https://github.com/CobayaSampler/sn_data

DES-SN5YR public repository
https://github.com/des-science/DES-SN5YR

DES Supernova 5YR Zenodo release
https://zenodo.org/records/12720778

SPT-3G data products portal
https://lambda.gsfc.nasa.gov/product/spt/spt3g_d1_high_ell_info.html
```

The support for those links comes from the official release and archive pages retrieved here: DESI’s DR1 documentation, DESI’s DR2 cosmology-release note, the ESA Planck Legacy Archive, the NERSC PR4/NPIPE page, the Cobaya Planck-likelihood documentation, the DES-SN5YR repository and Zenodo release, and the Cobaya SN-data repository that explicitly includes Union3 data files. citeturn50search0turn50search1turn50search2turn50search6turn50search13turn50search7turn50search10turn50search3

## What could move this

The single most decisive near-term dataset is **Euclid DR1 Foundation**, expected in **November 2026**. It is the nearest truly independent Stage-IV geometric probe that can test whether the DESI-preferred redshift evolution in the distance ladder survives with a different instrument, different selection function, and different systematics stack. citeturn49search1turn49search9

The single systematic most likely to change the current picture is **the low-\(z\) SN calibration / selection-bias treatment**, especially the way nearby supernova anchors are tied to the higher-\(z\) Hubble diagram. That is exactly where DESI says the SN leverage comes from, and it is exactly where the Pantheon+, Union3, and DES-SN5YR comparison papers find the most consequential differences. citeturn27view0turn45search3turn46search3