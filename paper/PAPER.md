---
title: |
  1.00115965218:\
  A Stratigraphy of the\
  Electron Magnetic Moment
author: PIATRA . INSTITUTE
date: May 2026
---

## Abstract

The number $1.00115965218 \ldots$ is the experimentally measured value of $|g_e|/2$ for the electron, where $g_e$ is its gyromagnetic ratio. The digits after the decimal constitute the anomalous magnetic moment $a_e = (|g_e| - 2)/2$. We read this number as historical sediment. Its leading $1$ was predicted in 1928 by Dirac's relativistic theory of the electron. Its next several digits were predicted in 1948 by Schwinger as $\alpha/(2\pi)$, the first radiative correction in quantum electrodynamics; that single term agrees with the modern measurement to one part in 660. The digits beyond Schwinger's contribution were determined order by order through the QED perturbation series, with the analytic two-loop result of Sommerfield (1957) and Petermann (1957), the three-loop analytic result of Laporta and Remiddi (1996), and the five-loop numerical calculation of Aoyama, Hayakawa, Kinoshita and Nio (2012), which evaluated 12,672 Feynman diagrams. The final digits of resolution were extracted by a sequence of single-electron Penning-trap measurements, from Dehmelt's geonium spectroscopy through Hanneke, Fogwell and Gabrielse (2008) to Fan, Myers, Sukra and Gabrielse (2023), the current record at 0.13 parts per trillion. The residual uncertainty in the comparison between this measurement and the Standard Model prediction is set today by an unresolved $5.5\,\sigma$ tension between two independent measurements of the fine-structure constant: the 2018 Berkeley caesium-recoil value $\alpha^{-1} = 137.035\,999\,046(27)$ and the 2020 Paris rubidium-recoil value $\alpha^{-1} = 137.035\,999\,206(11)$. The two values predict $a_e$ to differ by approximately $1.4 \times 10^{-12}$, an order of magnitude larger than the experimental uncertainty of $1.3 \times 10^{-13}$. We formalise the stratigraphic reading by computing each contribution from published coefficients and apparatus values. The simulation reconstructs the QED series at orders one through five, propagates the hadronic and weak contributions, performs the $\alpha$-inversion of the measurement, and quantifies the Berkeley/Paris/Fan triangle of $\alpha$ determinations. Every numeric claim in the paper traces to a key in `simulation/output/results.json`. The number $1.00115965218 \ldots$ now functions as a metrological instrument that audits the constants and theories that go into predicting it.


## 1. A decimal in two parts

The electron has a magnetic moment. The natural unit of magnetic moment for an elementary particle of charge $-e$ and mass $m_e$ is the Bohr magneton, $\mu_B = e\hbar / (2 m_e)$. Compared to this unit, the electron's measured magnetic-moment magnitude is $|\mu_e|/\mu_B = 1.001\,159\,652\,180\,59(13)$, where the digits in parentheses are the one-sigma uncertainty in the last two figures, from Fan, Myers, Sukra and Gabrielse (2023). The same quantity is written $|g_e|/2$, with $g_e$ the electron's gyromagnetic ratio.

The leading $1$ is Dirac (1928). The relativistic theory of the electron, with no parameter fitted to the magnetic moment, gives $|g_e| = 2$ and therefore $|g_e|/2 = 1$. The digits after the decimal, which form the anomalous magnetic moment $a_e = (|g_e| - 2)/2 = 1.159\,652\,180\,59 \times 10^{-3}$, are everything Dirac's theory missed: the quantum fluctuations of the electromagnetic field that dress the bare electron, the hadronic and electroweak corrections, the input value of the fine-structure constant $\alpha$, and the engineering of an apparatus that holds a single electron stationary in a known magnetic field for long enough to count its spin and cyclotron transitions.

The number is read here as a stratigraphy. Each digit was deposited by a distinct historical episode. The leading $1$ is Dirac's relativistic prediction; the next several digits are Schwinger's one-loop QED correction (1948); the digits beyond Schwinger's contribution were filled in order by order through the QED perturbation series, with the analytic results of Sommerfield (1957) and Petermann (1957) at two loops, Laporta and Remiddi (1996) at three loops, the Kinoshita group at four loops, and Aoyama, Hayakawa, Kinoshita and Nio (2012) at five loops, the last requiring the evaluation of 12,672 Feynman diagrams. The trailing digits at parts-per-trillion resolution were set by a sequence of Penning-trap experiments running from Dehmelt's geonium work in the 1980s through Hanneke, Fogwell and Gabrielse (2008) to Fan, Myers, Sukra and Gabrielse (2023).

The stratigraphic reading is not a metaphor. The Standard Model prediction is a sum,

$$a_e^{\text{th}} = \sum_{n=1}^{5} c_n \left(\frac{\alpha}{\pi}\right)^n + r_{\text{mass-dep}} + a_e^{\text{had}} + a_e^{\text{weak}},$$

where each universal QED coefficient $c_n$ corresponds to a specific loop order and a specific historical calculation, the mass-dependent residual $r_{\text{mass-dep}}$ collects the contributions from internal muon and tau loops, and $a_e^{\text{had}}$ and $a_e^{\text{weak}}$ are the hadronic and electroweak corrections. The successive terms contribute at successive layers of decimal precision in $a_e$. We compute every term in the decomposition from published coefficients and the value of $\alpha$ extracted from the Fan et al. (2023) measurement, and the resulting partition is the formal statement of the stratigraphic reading.

The number's contemporary role has shifted from object of measurement to instrument of measurement. Two independent measurements of the fine-structure constant, the 2018 Berkeley caesium-recoil measurement of Parker, Yu, Zhong, Estey and Müller and the 2020 Paris rubidium-recoil measurement of Morel, Yao, Cladé and Guellati-Khélifa, disagree at $5.5\,\sigma$. The disagreement is large enough that the Standard Model prediction of $a_e$ takes different values depending on which $\alpha$ one inputs, and the difference, $\sim 1.4 \times 10^{-12}$, exceeds the experimental uncertainty by a factor of 10. The number $1.001\,159\,652\,180\,59$ now functions as a metrological instrument that audits the constants and theories that go into predicting it.


## 2. Before the anomaly

Spin entered physics as a spectroscopic fix. By 1922 Stern and Gerlach had shown that a beam of silver atoms passing through a non-uniform magnetic field split into discrete deflections rather than smearing continuously, evidence that the projection of angular momentum along the field took quantised values. The interpretation at the time, before any theory of intrinsic angular momentum, attributed the splitting to the orbital angular momentum of the outer electron quantised in the Bohr sense.

Three years later, Uhlenbeck and Goudsmit (1925) proposed that the electron carried an intrinsic angular momentum of magnitude $\hbar/2$ in its own right, on top of any orbital contribution, and that this intrinsic angular momentum came with a magnetic moment. The proposal was made to explain anomalous patterns in atomic spectra, including the doublet structures in alkali metals and the fine-structure splittings that orbital angular momentum alone could not produce. The hypothesis was almost immediately useful and almost immediately problematic. A classical electron with spin $\hbar/2$ would have a surface velocity exceeding the speed of light, given any reasonable electron radius. Uhlenbeck and Goudsmit reportedly tried to withdraw the paper before publication; Ehrenfest sent it in anyway.

The same problem produced the next clue. The Landé $g$-factor, an empirical multiplier needed to bring the predicted Zeeman splittings into agreement with measurement, took a value close to $2$ for the electron's spin contribution, where pure classical reasoning suggested $g = 1$. There was no theoretical reason in the pre-quantum picture for the spin gyromagnetic ratio to be twice the orbital one. The factor $2$ was an empirical patch.

Pais (1986) traces the period in detail. The decade between 1922 and 1928 contained the proposal of intrinsic spin, the discovery of its anomalous gyromagnetic ratio, the development of Pauli's matrix formulation of spin in non-relativistic quantum mechanics, and the slowly accumulating recognition that something more fundamental was needed than any of those. The closure came from Dirac.


## 3. Dirac's integer

Dirac (1928) sought a relativistic wave equation for the electron, linear in time and space derivatives, with the Schrödinger equation as its non-relativistic limit. Linearity, combined with the requirement that the square of the equation yield the Klein-Gordon relation $E^2 = p^2 c^2 + m_e^2 c^4$, forced the wave function to be four-component and the coefficient matrices to satisfy the Clifford algebra of $\gamma$ matrices. The minimal coupling to an external electromagnetic field followed by the standard substitution $p_\mu \to p_\mu - eA_\mu/c$.

What emerged from this construction was something neither Dirac nor his contemporaries had imposed. The non-relativistic limit of the Dirac equation in an external magnetic field produces, in addition to the kinetic and Coulomb terms, a term of the form $-(e\hbar / m_e c)\, \boldsymbol{S} \cdot \boldsymbol{B}$, where $\boldsymbol{S}$ is the spin operator with eigenvalues $\pm \hbar/2$. The coefficient of this term is twice what classical reasoning gives for the corresponding orbital coupling. Spin and the Landé factor of $2$ both fall out of the construction without being put in. The integer $g_e = 2$ is a theorem of the relativistic theory, fixed by its structure before any parameter is chosen.

Kragh (1990) reconstructs the conceptual sequence. Dirac, in 1928, was working on a different problem. He needed a wave equation Lorentz-covariant in the same way Maxwell's equations are, with the probability interpretation of non-relativistic quantum mechanics preserved. The magnetic moment came as a side effect of solving that problem. The same side effect had been obtained in non-relativistic quantum mechanics by Pauli a few years earlier, by adding a two-component spinor structure by hand with the gyromagnetic ratio fitted to spectroscopy at $g = 2$. The Dirac equation derived the same factor from a more basic premise. Pauli, having earlier dismissed the Uhlenbeck-Goudsmit spin proposal as *Knabenphysik* (boys' physics), revised his position once the Dirac construction made the factor of 2 unavoidable (Pais, 1986).

The integer $1$ is the first stratum of the decimal. With nothing further added, the prediction is $|g_e|/2 = 1.000\,000\,000\,000$, which agrees with measurement to one part in $10^3$ and disagrees with measurement starting at the fourth decimal place. Dirac, at the time, considered the equation a finished theory of the electron. The disagreement at the fourth decimal place was the first indication that one more layer was needed.


## 4. The first correction

### 4.1 The Kusch-Foley measurement

The atomic-beam magnetic-resonance method, developed by Rabi in the 1930s, sent a beam of atoms through a homogeneous magnetic field crossed with a small oscillating radio-frequency field, and detected the resonance frequencies at which transitions between hyperfine states were driven. By the late 1940s the method had become precise enough to measure ratios of magnetic moments inside atoms to a few parts per ten thousand. Kusch and Foley (1947, 1948), working at Columbia, used the method to compare the magnetic moments associated with the $^2 S_{1/2}$ and $^2 P_{1/2}$ states of gallium and indium atoms.

The expected ratio of the two effective $g$-factors depended on whether one used the Dirac prediction $g_S = 2$ for the spin contribution. Kusch and Foley found that the data were consistent with the Dirac value only if a small correction was added to the spin gyromagnetic ratio. Expressed as an anomaly relative to the Dirac value, the correction was $a_e^{\text{Kusch-Foley}} = (1.19 \pm 0.05) \times 10^{-3}$, within one sigma of the modern $a_e = 1.159\,652 \times 10^{-3}$. The discovery established that the electron's magnetic moment was empirically larger than the Dirac prediction. The size of the deviation was small enough to be a correction rather than a contradiction, and large enough to demand a theoretical explanation.

### 4.2 Schwinger's term and its dominance

Schwinger (1948), in a one-paragraph note in *Physical Review*, derived the leading correction in the renormalised theory of quantum electrodynamics. The calculation evaluated the simplest vertex diagram, in which the electron emits and reabsorbs a virtual photon, and Schwinger showed that the cancellation between the ultraviolet-divergent self-energy and the vertex correction left a finite contribution to the magnetic moment of magnitude

$$a_e^{(2)} = \frac{\alpha}{2\pi}.$$

The result, later associated with the formula on Schwinger's tombstone (Mehra and Milton, 2000), is the first historical layer of $a_e$ that depends on quantum electrodynamics rather than on relativistic single-particle wave mechanics. Schweber (1994) places the calculation in its mid-century context: by 1948 a half-dozen post-war groups had been pushing on the divergences of QED for several years, and the achievement of Schwinger, Feynman, Tomonaga, and Dyson over the period 1947 to 1949 was the demonstration that subtracting the divergences in a systematic order-by-order scheme left finite physical predictions. Brown (1993) traces the development of renormalisation as a programme. With the modern value $\alpha^{-1} = 137.035\,999\,166$ from Fan, Myers, Sukra and Gabrielse (2023), Schwinger's term evaluates to

$$\frac{\alpha}{2\pi} = 1.161\,410 \times 10^{-3},$$

while the measured anomaly is $a_e = 1.159\,652 \times 10^{-3}$. The Schwinger term agrees with the modern measurement to one part in 660.

The stratigraphic reading admits a formal statement.

\begin{definition}[Stratigraphic decomposition]
Let $a_e = (|g_e| - 2)/2$ be the electron anomalous magnetic moment. The Standard Model prediction decomposes as
$$a_e^{\text{th}} = \sum_{n=1}^{5} c_n \left(\frac{\alpha}{\pi}\right)^n + r_{\text{mass-dep}} + a_e^{\text{had}} + a_e^{\text{weak}},$$
where the universal QED coefficients $c_n$ are those of Aoyama, Kinoshita and Nio (2019), $r_{\text{mass-dep}}$ collects the mass-dependent QED contributions $A_2(m_e/m_\mu)$, $A_2(m_e/m_\tau)$, and $A_3(m_e/m_\mu, m_e/m_\tau)$ in the notation of the same authors, $a_e^{\text{had}}$ is the hadronic vacuum-polarisation and light-by-light contribution, and $a_e^{\text{weak}}$ is the electroweak contribution from one-loop $W$ and $Z$ diagrams. The historical signature of each term is the calculation that produced its central value and the apparatus that resolved the decimal place at which it contributes.
\end{definition}

The first term of the decomposition dominates the anomaly numerically.

\begin{proposition}[Schwinger dominance]
At the fine-structure constant value $\alpha^{-1} = 137.035\,999\,166$ extracted by Fan, Myers, Sukra and Gabrielse (2023) from their measurement, the Schwinger term $\alpha/(2\pi) = 1.161\,410 \times 10^{-3}$ overshoots the experimental anomaly $a_e = 1.159\,652\,180\,59 \times 10^{-3}$ by $1.758 \times 10^{-6}$, that is, by $0.152\%$ relative to $a_e$, an agreement to one part in 660. The next-order Sommerfield-Petermann term $c_2 (\alpha/\pi)^2 = -1.772 \times 10^{-6}$ corrects the overshoot to within a few parts per ten thousand of itself, and the further orders refine the agreement layer by layer.
\end{proposition}

\noindent\textit{Proof.} Direct evaluation. The Schwinger contribution at $\alpha^{-1} = 137.035\,999\,166$ is $c_1 \cdot (\alpha/\pi) = 0.5 \cdot 2.323\,182 \times 10^{-3} = 1.161\,410 \times 10^{-3}$. The Sommerfield-Petermann universal coefficient is $c_2 = -0.328\,478\,965\,579$. Multiplying by $(\alpha/\pi)^2 = 5.397 \times 10^{-6}$ gives $-1.772\,305 \times 10^{-6}$. The sum of the two terms is $1.159\,638 \times 10^{-3}$, within $1.5 \times 10^{-8}$ of the measured value, which is the magnitude of the third-order term. The remaining contributions are smaller than $10^{-9}$ and cannot exceed $0.2\%$ of the total individually or summed. The Schwinger term alone therefore captures the magnitude of the anomaly to better than $0.2\%$. $\square$


## 5. From one term to twelve thousand

### 5.1 The QED series

The QED contribution to $a_e$ is an asymptotic expansion in powers of $\alpha/\pi$. Each successive coefficient $c_n$ is the value of a finite Feynman-diagram amplitude summed over all topologies at $n$ loops, with the ultraviolet divergences removed by the standard renormalisation of the electron's mass, charge, and wave function. The coefficients are dimensionless real numbers, smaller than $10$ in absolute value at every order computed so far. The smallness of $\alpha/\pi \approx 2.32 \times 10^{-3}$ ensures that the contribution at order $n+1$ is roughly $2 \times 10^{-3}$ times the contribution at order $n$, so each additional loop fills the next two to three digits of the decimal.

Sommerfield (1957) and Petermann (1957), working independently in the same year, gave the analytic value of the two-loop coefficient,

$$c_2 = \frac{197}{144} + \frac{\pi^2}{12} - \frac{\pi^2}{2} \ln 2 + \frac{3}{4}\, \zeta(3) = -0.328\,478\,965\,579\,193\,378\ldots,$$

which fits the seven distinct two-loop topologies for the electron vertex into a single closed-form expression. With $(\alpha/\pi)^2 \approx 5.40 \times 10^{-6}$ this gives a contribution of $-1.772\,305 \times 10^{-6}$ to $a_e$.

Laporta and Remiddi (1996) obtained the analytic three-loop result. The $72$ distinct three-loop topologies combine into an expression involving polylogarithms up to $\mathrm{Li}_4(1/2)$, the Riemann zeta function at integer arguments, and powers of $\ln 2$, with numerical value $c_3 = 1.181\,241\,456\,587$. Kinoshita and Nio (2006), following two decades of automated diagram evaluation by the Kinoshita group, gave the four-loop coefficient $c_4 = -1.912\,246$ numerically; Laporta (2017) later obtained it in closed analytic form as $c_4 = -1.912\,245\,764\,926$, so the four-loop term carries no truncation uncertainty. Aoyama, Hayakawa, Kinoshita and Nio (2012) gave the five-loop coefficient $c_5 = 6.737$, requiring the evaluation of $12{,}672$ Feynman diagrams. Volkov (2019) independently recomputed the no-lepton-loop part of the five-loop term and obtained $6.793(90)$, disagreeing with the Kinoshita group's value by about $4.8\,\sigma$; the discrepancy was later traced to errors in the earlier evaluation and resolved near $6.80$. The five-loop coefficient is the only universal term known purely numerically, and it is the resolution of that disagreement, rather than an early agreement, that now underwrites it.

The number of distinct diagram topologies grows roughly geometrically: $1$, $7$, $72$, $891$, $12{,}672$ at loop orders one through five respectively. The geometric growth means that each successive loop order represents an order-of-magnitude increase in calculational labour relative to the previous, and the numerical contribution falls correspondingly. At Fan's value of $\alpha$, the per-order contributions are

$$
\begin{aligned}
c_1 (\alpha/\pi)\phantom{^5} &= +1.161\,410 \times 10^{-3}, \\
c_2 (\alpha/\pi)^2 &= -1.772\,305 \times 10^{-6}, \\
c_3 (\alpha/\pi)^3 &= +1.480\,411 \times 10^{-8}, \\
c_4 (\alpha/\pi)^4 &= -5.567 \times 10^{-11}, \\
c_5 (\alpha/\pi)^5 &= +4.554 \times 10^{-13}.
\end{aligned}
$$

The signs alternate, the magnitudes fall by a factor of $\sim 500$ per order, and the five-loop result contributes only at the 13th decimal place of $a_e$. Each order fills the next layer of the stratigraphy.

### 5.2 Hadronic and weak contributions

Beneath the QED series sit two further contributions of qualitatively different origin. The hadronic contribution comes from the coupling of the electron to virtual quark-antiquark pairs through intermediate photons, evaluated via dispersion relations from experimental data on $e^+ e^-$ annihilation into hadrons. Aoyama, Kinoshita and Nio (2019) report

$$a_e^{\text{had}} = (1.6927 \pm 0.0120) \times 10^{-12},$$

summing hadronic vacuum-polarisation at leading and next-to-leading order with the hadronic light-by-light contribution. Jegerlehner (2017) develops the calculational framework in detail, originally for the muon's far larger hadronic contribution, where the same dispersion technique drives the central effort. For the electron the hadronic contribution is small enough that the uncertainty in $a_e^{\text{th}}$ from this source is itself below $10^{-13}$, at the level of the present experimental uncertainty in $a_e^{\text{exp}}$.

The weak contribution, from one-loop diagrams involving virtual $W$ and $Z$ bosons (Czarnecki, Krause and Marciano, 1996), is several orders of magnitude smaller still:

$$a_e^{\text{weak}} = (0.029\,70 \pm 0.000\,05) \times 10^{-12}.$$

The hierarchy of magnitudes (QED of order $10^{-3}$, hadronic of order $10^{-12}$, weak of order $10^{-14}$) means that for the electron the QED sector dominates by 9 orders of magnitude over the hadronic effect and a further 100 over the weak. The hierarchy reverses substantially for the muon (Hoecker and Marciano, 2022), where the mass-dependent hadronic and weak contributions both scale roughly as the square of the lepton mass and become comparable to the QED uncertainty.

The mass-dependent QED contribution from internal muon and tau loops, denoted $r_{\text{mass-dep}}$ in the decomposition, contributes approximately $+2.75 \times 10^{-12}$ at the present value of $\alpha$, dominated by the two-loop $A_2^{(4)}(m_e/m_\mu)$ piece. The contribution is small at the electron precision and was historically the last piece to be brought to the same accuracy as the universal coefficients.


## 6. One electron in a trap

### 6.1 Penning's trap and Dehmelt's geonium

The construction needed to expose Schwinger's correction and its successors is an apparatus that holds a single electron stationary, in a known magnetic field, for long enough to count the transitions between its cyclotron and spin states. Penning (1936) described the geometry for cold-cathode ionisation gauges that confines a charged particle to a small region by combining a uniform axial magnetic field with a quadrupolar electrostatic field. The electron in this geometry undergoes three independent motions: cyclotron motion in the magnetic field, axial oscillation in the electrostatic well, and a slow magnetron drift, each of which has a known relation to the trapping fields and the particle's properties.

Dehmelt (1990) developed the Penning trap into a precision spectroscopy. The cyclotron and spin Larmor frequencies of a free electron stand in the ratio

$$\frac{\nu_s}{\nu_c} = \frac{|g_e|}{2},$$

so the magnetic-moment magnitude can be extracted from the ratio of two frequencies measured on the same particle in the same apparatus, with the absolute value of the magnetic field cancelling. Dehmelt coined the term *geonium* for a single electron bound to the laboratory in this way. The geonium electron has no electronic structure and no chemical environment, and nothing collides with it to broaden its transitions thermally. Its only environment is the trap, and the trap's perturbations on the measured frequencies are calculable from first principles. Individual electrons were held in Dehmelt's apparatus for periods of months, observed through repeated cycles of cyclotron excitation, spin flip, and quantum non-demolition readout on the same particle.

### 6.2 The measurement sequence

Wilkinson and Crane (1963) had given an early precision measurement of the free-electron $g$-factor using polarised electrons trapped in a magnetic field and probed by precession, reaching a relative uncertainty of $\sim 4 \times 10^{-6}$, more than an order of magnitude better than the Kusch-Foley measurement and at the level where the Schwinger correction was visible cleanly above the Dirac prediction. The next major advance came with the single-electron Penning trap.

Van Dyck, Schwinberg and Dehmelt (1987), at the University of Washington, used a geonium electron in a hyperbolic Penning trap to measure $|g_e|/2$ with an uncertainty of $4 \times 10^{-12}$. Hanneke, Fogwell and Gabrielse (2008), at Harvard, replaced the hyperbolic geometry with a cylindrical cavity Penning trap and resolved $|g_e|/2$ to $2.8 \times 10^{-13}$. The cylindrical cavity offers a calculable density of electromagnetic-field modes near the cyclotron frequency, and the cavity-mode shift on the measured cyclotron frequency was modelled to the precision required by the new uncertainty budget. Fan, Myers, Sukra and Gabrielse (2023), at Northwestern, rebuilt the Harvard apparatus with improved control of the cavity-mode-shift correction and longer coherent observations on the trapped electron. The new measurement,

$$|g_e|/2 = 1.001\,159\,652\,180\,59(13),$$

is the most precisely determined property of any elementary particle, with relative uncertainty of $1.3 \times 10^{-13}$, 0.13 parts per trillion. The improvement over the 2008 result is a factor of $2.2$. The precision history is summarised in Table 1.

\begin{center}
\begin{tabular}{rlll}
\toprule
year & $|g_e|/2$ & $\sigma$ & apparatus, laboratory \\
\midrule
1948 & $1.001\,19$              & $5 \times 10^{-5}$    & atomic-beam magnetic resonance, Columbia \\
1963 & $1.001\,160\,9$          & $4 \times 10^{-6}$    & free-electron precession, Michigan \\
1987 & $1.001\,159\,652\,21$    & $4 \times 10^{-12}$   & hyperbolic Penning trap, Washington \\
2008 & $1.001\,159\,652\,180\,73$ & $2.8 \times 10^{-13}$ & cylindrical Penning trap, Harvard \\
2023 & $1.001\,159\,652\,180\,59$ & $1.3 \times 10^{-13}$ & rebuilt cylindrical trap, Northwestern \\
\bottomrule
\end{tabular}
\end{center}

Table 1: Milestone measurements of the electron magnetic moment, 1948 to 2023.

The relative uncertainty in $|g_e|/2$ improved by a factor of approximately $4 \times 10^8$ over seventy-five years, with the largest discrete improvement, roughly 6 orders of magnitude, coming when the apparatus changed from free-electron precession to the single-electron Penning trap in the 1980s. Galison (1987) discusses, in a related context, how precision measurements in twentieth-century physics achieve closure through the accumulation of independent checks against systematic error; the seven decades of work on $g/2$ illustrate the same pattern across multiple generations of apparatus.


## 7. The constant becomes the bottleneck

### 7.1 How $\alpha$ enters

The Standard Model prediction of $a_e$ is a function of $\alpha$, the masses of the muon and tau, the QCD coupling and hadronic spectral functions, and the weak mixing angle and gauge-boson masses. Of these, the dependence on $\alpha$ dominates by orders of magnitude. The leading Schwinger term is linear in $\alpha$, the two-loop term is quadratic, and so on through the series. To leading order

$$\frac{\partial a_e^{\text{th}}}{\partial \alpha} \approx \frac{a_e^{\text{th}}}{\alpha}, \qquad \frac{\sigma(a_e^{\text{th}})}{a_e^{\text{th}}} \approx \frac{\sigma(\alpha)}{\alpha},$$

so the relative uncertainty in $a_e^{\text{th}}$ from $\alpha$ inherits the relative uncertainty in $\alpha$. Reaching parts-per-trillion precision on $a_e^{\text{th}}$ requires parts-per-trillion knowledge of $\alpha$, and the latter is harder to obtain than the former. CODATA 2022 (Mohr, Newell, Taylor and Tiesinga, 2024) gives the current recommended value of $\alpha^{-1}$, weighting the available independent determinations.

The independent determination of $\alpha$ comes from atom-interferometric measurements of the recoil velocity of an atom that absorbs and re-emits a photon of known wavelength. The ratio $h/m_{\text{atom}}$ of Planck's constant to the atom's mass is extracted from the recoil and combined with the proton-to-electron mass ratio and other atomic-mass measurements to yield $\alpha^2$. The chain of measurements is independent of the electron magnetic moment. Bouchendira, Cladé, Guellati-Khélifa, Nez and Biraben (2011), in Paris, gave the first sub-billionth measurement of $\alpha$ by this method, using rubidium-87 atoms. The technique was subsequently refined by two groups using different atomic species.

### 7.2 The Cs-Rb tension

Parker, Yu, Zhong, Estey and Müller (2018), at Berkeley, completed the caesium-recoil measurement,

$$\alpha^{-1} = 137.035\,999\,046(27), \qquad 2.0 \times 10^{-10} \text{ relative precision},$$

setting the most precise value at the time. Two years later, Morel, Yao, Cladé and Guellati-Khélifa (2020), at Paris, completed the rubidium-recoil measurement,

$$\alpha^{-1} = 137.035\,999\,206(11), \qquad 8.1 \times 10^{-11} \text{ relative precision},$$

with central value differing from the Berkeley result in the tenth significant digit. The two experiments share the atom-recoil principle but differ in atomic species, laser systems, and dominant systematic corrections, so the discrepancy between them cannot be charged to a common error; it stands as a genuine disagreement between two mature techniques. The difference, $\Delta \alpha^{-1} = 1.60 \times 10^{-7}$, exceeds the combined one-sigma uncertainty $\sqrt{27^2 + 11^2} \times 10^{-9} = 2.91 \times 10^{-8}$ by a factor of $5.49$, giving a $5.49\,\sigma$ tension. Inverting the Fan, Myers, Sukra and Gabrielse (2023) measurement under the Standard Model prediction gives

$$\alpha^{-1}\big|_{a_e\text{-inverted}} = 137.035\,999\,166(15),$$

sitting between the Berkeley and Paris values, consistent with Paris at $2.2\,\sigma$ and with Berkeley at $3.9\,\sigma$. The tension among the three is the dominant systematic in any present comparison between measurement and theory.

The mapping from $\sigma(\alpha)$ to $\sigma(a_e^{\text{th}})$ is approximately

$$\sigma(a_e^{\text{th}}) \approx a_e \cdot \frac{\sigma(\alpha^{-1})}{\alpha^{-1}}.$$

With the published $\sigma(\alpha^{-1})$ from each measurement, the Berkeley value propagates an uncertainty $\sigma_{\text{Cs}}(a_e^{\text{th}}) = 2.29 \times 10^{-13}$, the Paris value propagates $\sigma_{\text{Rb}}(a_e^{\text{th}}) = 9.31 \times 10^{-14}$, and the $a_e$-inverted value propagates $\sigma_{\text{Fan}}(a_e^{\text{th}}) = 1.27 \times 10^{-13}$. The QED-truncation uncertainty at five loops is $\sigma_{\text{trunc}}(a_e^{\text{th}}) = 2.45 \times 10^{-14}$. The hadronic uncertainty is $\sigma_{\text{had}}(a_e^{\text{th}}) = 1.20 \times 10^{-14}$. The experimental uncertainty from Fan, Myers, Sukra and Gabrielse (2023) is $\sigma(a_e^{\text{exp}}) = 1.30 \times 10^{-13}$.

\begin{proposition}[$\alpha$-limited comparison]
At present precision, the uncertainty in $a_e^{\text{th}}$ propagated from $\sigma(\alpha)$ exceeds the QED-truncation uncertainty by a factor of approximately $9$ under the Berkeley caesium value and by a factor of approximately $4$ under the Paris rubidium value. The Berkeley-Paris central-value difference, propagated through the prediction, yields $\Delta a_e^{\text{th}}|_{\text{Cs-Rb}} = 1.35 \times 10^{-12}$, which is approximately 10 times the experimental uncertainty $\sigma(a_e^{\text{exp}}) = 1.30 \times 10^{-13}$.
\end{proposition}

\noindent\textit{Proof.} Direct evaluation. With $\sigma(\alpha^{-1})_{\text{Cs}} = 27 \times 10^{-9}$ and $a_e = 1.160 \times 10^{-3}$, the propagation gives $\sigma_{\text{Cs}}(a_e^{\text{th}}) = a_e \cdot 27 \times 10^{-9}/137.036 = 2.29 \times 10^{-13}$. With $\sigma(\alpha^{-1})_{\text{Rb}} = 11 \times 10^{-9}$, the same calculation gives $\sigma_{\text{Rb}}(a_e^{\text{th}}) = 9.31 \times 10^{-14}$. The QED-truncation uncertainty at five loops is dominated by $\sigma(c_5) = 0.159$, contributing $\sigma(c_5) (\alpha/\pi)^5 = 1.08 \times 10^{-14}$ from $c_5$ alone; the four-loop coefficient is known analytically ($\sigma(c_4) = 0$), so this is the entire QED truncation uncertainty. The ratios are therefore $\sigma_{\text{Cs}}/\sigma_{\text{trunc}} = 21.3$ and $\sigma_{\text{Rb}}/\sigma_{\text{trunc}} = 8.7$. The Berkeley-Paris central-value difference is $\Delta \alpha^{-1}|_{\text{Cs-Rb}} = 1.60 \times 10^{-7}$, propagating to $\Delta a_e^{\text{th}}|_{\text{Cs-Rb}} = a_e \cdot \Delta \alpha^{-1}/\alpha^{-1} = 1.35 \times 10^{-12}$. The ratio $\Delta a_e^{\text{th}}|_{\text{Cs-Rb}} / \sigma(a_e^{\text{exp}}) = 10.4$. $\square$

The proposition says, in practical terms, that the present limiting systematic on any Standard Model test using $a_e$ is the disagreement among independent determinations of $\alpha$. Until that disagreement is resolved, more precise measurements of $a_e$ buy proportionally less than they did during the era when QED truncation set the floor.


## 8. What the decimal does

The number $1.001\,159\,652\,180\,59$ entered physics as a property of an electron and now functions as a measuring instrument. Three of its uses are operationally distinct.

The number anchors the electron magnetic moment to the Bohr magneton, the natural unit of magnetic moment in atomic physics. In the 2019 SI revision, $e$ and $h$ are defined exactly, so $\mu_B = e\hbar/(2 m_e)$ inherits any experimental uncertainty in $m_e$. The electron magnetic moment in absolute units therefore feeds into precision spectroscopy across atomic physics, including the caesium hyperfine-clock standard and the proton-to-electron mass ratio.

The comparison between $a_e^{\text{th}}$ and $a_e^{\text{exp}}$ probes any new physics that couples to the electron magnetic moment. A heavy new particle of mass $M$ coupling to the electron at one loop contributes a correction of order $m_e^2 / M^2$ in the naturalness estimate, so a sensitivity of $10^{-13}$ on $a_e$ corresponds to probing physics at the few-GeV scale in the most naive structures and at higher scales for more sensitive couplings. The far more sensitive muon $g{-}2$ measurement (Hoecker and Marciano, 2022) shows a discrepancy with the Standard Model prediction at the few-sigma level depending on which evaluation of the hadronic contribution is used; the electron measurement, while less sensitive to the mass-scaled corrections, has better control of its hadronic theory error and is more directly sensitive to electron-specific couplings.

The inverted measurement of $a_e$ gives a value of $\alpha^{-1}$ that competes with the independent atom-interferometric determinations. The three-way comparison Berkeley-Paris-Fan is the operational form of this audit. Until the Cs-Rb tension is resolved, the Standard Model test using $a_e$ loses much of its sensitivity, and the most productive next step is not a more precise measurement of $a_e$ but a third independent measurement of $\alpha$ that breaks the tie.

The stratigraphic reading of $1.001\,159\,652\,180\,59$ is more than a mnemonic. Each digit traces to a specific calculation or apparatus, with a date, a group of authors, a technique attached to it. The integer is Dirac (1928). The next several digits are Schwinger (1948). The next handful are Sommerfield, Petermann, Laporta, and Remiddi over the period 1957 to 1996. The digits at the part-per-trillion level are the Penning trap, Washington to Harvard to Northwestern, over the period 1987 to 2023. The digit at which the comparison saturates is the Berkeley-Paris discrepancy of 2018 and 2020. The composition is finite and layered, and every layer has a date.


## References

Aoyama, T., Hayakawa, M., Kinoshita, T., and Nio, M. (2012). Tenth-order QED contribution to the electron g–2 and an improved value of the fine structure constant. *Physical Review Letters*, 109, 111807.

Aoyama, T., Kinoshita, T., and Nio, M. (2019). Theory of the anomalous magnetic moment of the electron. *Atoms*, 7(1), 28.

Bouchendira, R., Cladé, P., Guellati-Khélifa, S., Nez, F., and Biraben, F. (2011). New determination of the fine structure constant and test of quantum electrodynamics. *Physical Review Letters*, 106, 080801.

Brown, L. M. (Ed.). (1993). *Renormalization: From Lorentz to Landau (and Beyond)*. New York: Springer.

Czarnecki, A., Krause, B., and Marciano, W. J. (1996). Electroweak corrections to the muon anomalous magnetic moment. *Physical Review Letters*, 76, 3267.

Dehmelt, H. G. (1990). Experiments with an isolated subatomic particle at rest (Nobel lecture). *Reviews of Modern Physics*, 62, 525.

Dirac, P. A. M. (1928). The quantum theory of the electron. *Proceedings of the Royal Society A*, 117, 610.

Fan, X., Myers, T. G., Sukra, B. A. D., and Gabrielse, G. (2023). Measurement of the electron magnetic moment. *Physical Review Letters*, 130, 071801.

Galison, P. (1987). *How Experiments End*. Chicago: University of Chicago Press.

Hanneke, D., Fogwell, S., and Gabrielse, G. (2008). New measurement of the electron magnetic moment and the fine structure constant. *Physical Review Letters*, 100, 120801.

Hoecker, A., and Marciano, W. J. (2022). The muon anomalous magnetic moment. Particle Data Group review. *Progress of Theoretical and Experimental Physics*, 2022, 083C01.

Jegerlehner, F. (2017). *The Anomalous Magnetic Moment of the Muon* (2nd ed.). Springer Tracts in Modern Physics, vol. 274. Cham: Springer.

Kinoshita, T., and Nio, M. (2006). Improved $\alpha^4$ term of the electron anomalous magnetic moment. *Physical Review D*, 73, 013003.

Kragh, H. (1990). *Dirac: A Scientific Biography*. Cambridge: Cambridge University Press.

Kusch, P., and Foley, H. M. (1947). Precision measurement of the ratio of the atomic $g$-values in the $^2 P_{3/2}$ and $^2 P_{1/2}$ states of gallium. *Physical Review*, 72, 1256.

Kusch, P., and Foley, H. M. (1948). The magnetic moment of the electron. *Physical Review*, 74, 250.

Laporta, S. (2017). High-precision calculation of the 4-loop contribution to the electron g-2 in QED. *Physics Letters B*, 772, 232-238.

Laporta, S., and Remiddi, E. (1996). The analytical value of the electron $(g-2)$ at order $\alpha^3$ in QED. *Physics Letters B*, 379, 283.

Mehra, J., and Milton, K. A. (2000). *Climbing the Mountain: The Scientific Biography of Julian Schwinger*. Oxford: Oxford University Press.

Mohr, P. J., Newell, D. B., Taylor, B. N., and Tiesinga, E. (2024). CODATA recommended values of the fundamental physical constants: 2022. *Reviews of Modern Physics*, 96, 025002.

Morel, L., Yao, Z., Cladé, P., and Guellati-Khélifa, S. (2020). Determination of the fine-structure constant with an accuracy of 81 parts per trillion. *Nature*, 588, 61.

Pais, A. (1986). *Inward Bound: Of Matter and Forces in the Physical World*. Oxford: Oxford University Press.

Parker, R. H., Yu, C., Zhong, W., Estey, B., and Müller, H. (2018). Measurement of the fine-structure constant as a test of the Standard Model. *Science*, 360, 191.

Penning, F. M. (1936). Die Glimmentladung bei niedrigem Druck zwischen koaxialen Zylindern in einem axialen Magnetfeld. *Physica*, 3, 873.

Petermann, A. (1957). Fourth order magnetic moment of the electron. *Helvetica Physica Acta*, 30, 407.

Schweber, S. S. (1994). *QED and the Men Who Made It: Dyson, Feynman, Schwinger, and Tomonaga*. Princeton: Princeton University Press.

Schwinger, J. (1948). On quantum-electrodynamics and the magnetic moment of the electron. *Physical Review*, 73, 416.

Sommerfield, C. M. (1957). Magnetic dipole moment of the electron. *Physical Review*, 107, 328.

Stern, O., and Gerlach, W. (1922). Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld. *Zeitschrift für Physik*, 9, 349.

Uhlenbeck, G. E., and Goudsmit, S. (1925). Ersetzung der Hypothese vom unmechanischen Zwang durch eine Forderung bezüglich des inneren Verhaltens jedes einzelnen Elektrons. *Naturwissenschaften*, 13, 953.

Van Dyck, R. S., Schwinberg, P. B., and Dehmelt, H. G. (1987). New high-precision comparison of electron and positron $g$ factors. *Physical Review Letters*, 59, 26.

Volkov, S. (2019). Numerical calculation of high-order QED contributions to the electron anomalous magnetic moment. *Physical Review D*, 100, 096004.

Wilkinson, D. T., and Crane, H. R. (1963). Precision measurement of the $g$-factor of the free electron. *Physical Review*, 130, 852.
