# Tangential Adams e-Invariant for the Self-Dual Framing on RP^3

## Bottom line

On the **tangential** branch, the value you want is **correct in absolute value**: the natural framing on \(RP^3=L(2,1)\) coming from the charge-one self-dual \(SU(2)_+\) twist has framed-bordism class **\(\pm 2\in \pi_3^s\cong \mathbb Z/24\)**, so its real Adams \(e\)-invariant is **\(\pm 1/12\in \mathbb Q/\mathbb Z\)**. The sign depends on orientation and handedness conventions, but the magnitude does not. In particular, the tangential class has **nonzero 3-primary part**, because \(\pm 2\) is nonzero mod \(3\), equivalently because \(1/12\) still has a factor of \(3\) in its denominator. citeturn32view0turn37view0turn26view0turn23view3

The strongest published route is not a paper that says verbatim “the self-dual-framed \(RP^3\) has \(e=\pm 1/12\),” but rather a combination of two standard published ingredients. First, Kirby–Melvin compute the natural framing on \(L(2,1)=RP^3\) and show that for the corresponding disk-bundle filling one has relative Pontryagin number \(p_1=4\) and Hirzebruch defect \(h=1\). Second, the standard framed-bordism formula identifies the class in \(\pi_3^s\) with \(\pm p_1/48\in \mathbb Q/\mathbb Z\). Putting those together gives \(\pm 4/48=\pm 1/12\). citeturn26view0turn37view0

That means the “landed” tangential result is solid **provided** the GU end-framing is genuinely identified with this natural \(SO(3)\)-valued tangential twist. The mathematical computation is standard once that identification is made; the identification itself is the part that remains reconstruction-dependent because it lives inside your GU reconstruction rather than in the existing topology literature. citeturn25view0turn26view0

## Published derivation from the natural framing on the Euler-two circle bundle

A very clean published model for \(RP^3\) is as the oriented circle bundle \(E\to S^2\) of Euler class \(n=2\). Kirby–Melvin analyze exactly these fiber-preserving framings. They prove that for the disk bundle \(\Delta\) bounded by \(E\), the relative Pontryagin number of the natural framing is
\[
p_1(\Delta,\varphi)= n+\chi(S^2)^2/n,
\]
and the Hirzebruch defect is
\[
h(\varphi)= n+\chi(S^2)^2/n - 3\,\mathrm{sign}(n).
\]
With \(n=2\) and \(\chi(S^2)=2\), this gives
\[
p_1(\Delta,\varphi)=2+4/2=4,\qquad h(\varphi)=4-3=1.
\]
They also identify the quotient framing on \(L(2,1)=RP^3\) with the right-handed Lie framing. citeturn25view0turn26view0

citeturn38view0

The standard framed-bordism formula then converts that relative Pontryagin number into the class in the third stable stem. Randal-Williams states explicitly that the element of \(\mathbb Z/24\cong \pi_3^s\) represented by a framed \(3\)-manifold \(M\) is computed by
\[
-\frac{1}{48}\langle p_1(W,M),[W,M]\rangle \in \mathbb Q/\mathbb Z,
\]
for a Spin filling \(W\). In these conventions, \(p_1=4\) gives \(-1/12\); with the opposite sign convention for \(e\), or after reversing orientation/handedness, one gets \(+1/12\). So the convention-free statement is
\[
|e_R(RP^3,\varphi)|= \frac1{12}.
\]
citeturn37view0

citeturn38view2

This published route already answers your main question. It says the natural tangential framing on \(RP^3\) is **not** class \(1\in\mathbb Z/24\); it is class \(2\) up to sign. The fact that Kirby–Melvin report \(h=1\) does **not** contradict this, because \(h=p_1-3\sigma\), and for the Euler-two disk bundle the signature is \(+1\), so \(h=1\) and \(p_1=4\) coexist exactly as they should. citeturn26view0turn37view0

## Independent stable-homotopy derivation from the twist itself

There is also a clean first-principles derivation that matches your clutching-map argument.

Kirby–Melvin recall the standard generators \(\rho\in \pi_3(SO(3))\) and \(\sigma\in \pi_3(SO)\cong \mathbb Z\), and they state the key stabilization fact:
\[
\pi_3(SO(3))\to \pi_3(SO)
\quad\text{sends}\quad
\rho\mapsto 2\sigma.
\]
They also note that the corresponding \(SU(2)\)-generator maps to generators in the stable unitary groups, and that \(\pi_3(SO)\to\pi_3(SU)\) is multiplication by \(-2\). This is exactly the standard reason the stable obstruction seen by \(J\) is **twice** the basic stable generator, not four times. citeturn22view0turn23view3

If the charge-one \(SU(2)\) self-dual twist is treated tangentially, then the clutching map is a generator of \(\pi_3(SU(2))\cong \mathbb Z\); via the double cover \(SU(2)\to SO(3)\), that is the generator of \(\pi_3(SO(3))\). The standard classification of \(SU(2)\)-bundles over oriented \(4\)-manifolds by a single integer is also recorded in Waldron’s notes, which is enough to identify “charge one” with the basic clutching class. After stabilization, that class becomes \(2\sigma\). citeturn15view1turn22view0

Adams’ theorem identifies the image of \(J\) in stem \(4s-1\) as cyclic of order equal to the denominator of \(B_s/4s\). For \(s=1\), this order is \(24\), so \(\mathrm{Im}(J_3)\cong \mathbb Z/24\). Therefore the stabilized class \(2\sigma\) lands in class \(\pm 2\in \mathbb Z/24\). citeturn32view0

To convert that to \(e\), one can normalize on the basic \(S^3\) framing. Kirby–Melvin compute that the right-handed Lie framing on \(S^3\) has relative Pontryagin number \(p_1=2\), and the framed-bordism formula then gives \(\pm 2/48=\pm 1/24\) for the generator. Doubling the stable generator gives \(\pm 1/12\). So your statement

\[
\text{stable degree seen by \(J\)} = |p_1/2| = 2
\quad\Longrightarrow\quad
e_R = \pm 2/24 = \pm 1/12
\]

is mathematically right. citeturn25view1turn37view0

This also answers the normalization issue you highlighted. The number that \(J\) sees is **not** the Dynkin index \(4\) by itself. The stable class is measured after passing through
\[
\pi_3(SO(3)) \to \pi_3(SO),
\]
and that passage is multiplication by \(2\). Equivalently, the relative Pontryagin number is \(4\), and the stable obstruction is \(p_1/2=2\). citeturn22view0turn23view3

## Why the gauge branch gives something different

The tangential computation and the gauge-coefficient computation are measuring different objects.

On the tangential side, you are modifying the **stable tangent framing**, so the invariant naturally lands in framed bordism \(\pi_3^s\) and is governed by the relative Pontryagin class of a filling. That is why the answer comes out as class \(\pm 2\in \mathbb Z/24\), with \(e_R=\pm 1/12\). citeturn37view0turn23view3

On the gauge side, the quantity you quoted, \(\pm 3/8\), is an eta-reduced spectral asymmetry value for a twisted operator with coefficients in the adjoint representation. Arithmetically, \(\pm 3/8\) has order dividing \(8\), so it has **no** 3-primary part. By contrast, \(\pm 1/12\) has order \(12\), hence a nontrivial 3-primary component. So the fact that the \(3\)-part survives on the tangential branch but vanishes on the gauge branch is not an inconsistency; it is the expected consequence of computing in two different receptacles. 

## Audit of the chain

What follows is the honest grading, step by step.

- **“\(\pi_3^s\cong \mathbb Z/24\), and the image of \(J\) in the 3-stem has order \(24\).”**  
  **Grade: theorem.** This is Adams’ classical result; a modern summary states that in stem \(4s-1\), the image of \(J\) is cyclic of order the denominator of \(B_s/4s\), which for \(s=1\) is \(24\). citeturn32view0

- **“The stabilization \(\pi_3(SO(3))\to \pi_3(SO)\) is multiplication by \(2\).”**  
  **Grade: theorem.** Kirby–Melvin state this explicitly in terms of their generators \(\rho\) and \(\sigma\): \(\rho\) goes to \(2\sigma\). citeturn22view0turn23view3

- **“A charge-one \(SU(2)\) tangential twist determines the generator of \(\pi_3(SO(3))\).”**  
  **Grade: standard-result-applied.** The classification of \(SU(2)\)-bundles over \(4\)-manifolds by one integer is standard, and a charge-one bundle is the basic class. Passing to \(SO(3)\) through the double cover is likewise standard. What is *not* standard is the identification of your GU \(SU(2)_+=\Lambda^2_+\) twist with this topological clutching class; that identification depends on your reconstruction. citeturn15view1turn22view0

- **“The stable degree seen by \(J\) is \(2\), not \(4\).”**  
  **Grade: theorem / standard-result-applied.** This is exactly what the stabilization fact above means. In relative Pontryagin-number language, the natural framing has \(p_1=4\), so the stable obstruction is \(p_1/2=2\). citeturn23view3turn26view0

- **“\(RP^3=L(2,1)\) with the natural tangential framing has \(p_1=4\) and \(h=1\).”**  
  **Grade: standard-result-applied with a published computation.** Kirby–Melvin compute the natural quotient framing on \(L(2,1)\), and their circle-bundle formula gives \(p_1=4\), \(h=1\) for the Euler-two disk bundle filling. This is the closest published reference to your exact target. citeturn25view0turn26view0

- **“Therefore \(e_R=\pm 1/12\).”**  
  **Grade: standard-result-applied.** This follows from the standard framed-bordism formula \(e=\pm p_1/48\) together with \(p_1=4\). The only ambiguity is the overall sign convention. citeturn37view0

- **“The 3-primary part survives to the boundary on the tangential branch.”**  
  **Grade: theorem plus arithmetic.** Since the class is \(\pm 2\in \mathbb Z/24\), its image in the \(\mathbb Z/3\) summand is nonzero. Equivalently, \(1/12\) still carries a factor of \(3\) in the denominator. citeturn32view0turn37view0

- **“The same survival should encode some deeper GU physical datum.”**  
  **Grade: speculative.** The topology says the 3-primary piece is there on the tangential branch. Any further physical interpretation is not forced by the mathematics alone.

## Final assessment

The **tangential** claim you wanted hardened survives scrutiny:

\[
e_R(RP^3,\text{self-dual tangential framing at charge }1)=\pm \frac{1}{12},
\qquad
[RP^3,\varphi]=\pm 2\in \pi_3^s\cong \mathbb Z/24.
\]

That is the mathematically correct value, and its **3-primary piece is genuinely nonzero**. The cleanest published support is Kirby–Melvin’s computation of the natural framing on \(L(2,1)=RP^3\), together with the standard \(e=\pm p_1/48\) formula for framed \(3\)-manifolds. The place where caution is still warranted is not the topology; it is the identification of your particular GU-induced framing with that natural tangential framing. Once that identification is granted, the \(1/12\) result is no longer speculative. citeturn25view0turn26view0turn37view0turn32view0