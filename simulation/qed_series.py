"""QED perturbation series for the electron anomalous magnetic moment.

Each coefficient $c_n$ is the universal (mass-independent) QED contribution at
order $(\\alpha/\\pi)^n$. Values from Aoyama, Kinoshita, and Nio (2019,
Atoms 7, 28, Table 1), with the lower-order analytic results due to Schwinger
(1948), Sommerfield (1957), Petermann (1957), Laporta and Remiddi (1996), and
the Kinoshita group.

Note: the universal coefficients are denoted $A_1^{(2n)}$ in Aoyama-Kinoshita-Nio.
The full a_e^QED also receives mass-dependent contributions from muon and tau
loops (denoted $A_2$, $A_3$) that are smaller than $10^{-12}$ for the electron
and are accounted for separately in run_all.py via a published residual.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


C1 = 0.5
"""Schwinger (1948), exact."""

C2 = -0.328478965579193378
"""Sommerfield (1957), Petermann (1957), analytic value given to 18 digits."""

C3 = 1.181241456587
"""Laporta and Remiddi (1996), analytic three-loop result; 12-digit numerical."""

C4 = -1.912245764926
"""Laporta (2017), analytic four-loop result. Known in closed form, so its
truncation uncertainty is taken as zero."""

C5 = 6.737
"""Aoyama, Hayakawa, Kinoshita and Nio (2012), revised in Aoyama-Kinoshita-Nio
(2019) to 6.737(159). The fifth-order coefficient required evaluating 12,672
Feynman diagrams and is the only universal coefficient still known purely
numerically, so its uncertainty sets the QED truncation error."""


SIGMA_C4 = 0.0
SIGMA_C5 = 0.159


N_DIAGRAMS = {
    1: 1,
    2: 7,
    3: 72,
    4: 891,
    5: 12672,
}


LABELS = {
    1: "Schwinger (1948)",
    2: "Sommerfield (1957), Petermann (1957)",
    3: "Laporta and Remiddi (1996)",
    4: "Laporta (2017)",
    5: "Aoyama, Hayakawa, Kinoshita and Nio (2012)",
}


COEFFS = {1: C1, 2: C2, 3: C3, 4: C4, 5: C5}
SIGMA_COEFFS = {1: 0.0, 2: 0.0, 3: 0.0, 4: SIGMA_C4, 5: SIGMA_C5}


@dataclass
class OrderContribution:
    n: int
    label: str
    coefficient: float
    sigma_coefficient: float
    contribution: float
    sigma_contribution: float
    n_diagrams: int

    def as_dict(self) -> dict:
        return {
            "n": self.n,
            "label": self.label,
            "coefficient": self.coefficient,
            "sigma_coefficient": self.sigma_coefficient,
            "contribution": self.contribution,
            "sigma_contribution": self.sigma_contribution,
            "n_diagrams": self.n_diagrams,
        }


def order_contributions(alpha: float) -> list[OrderContribution]:
    a_over_pi = alpha / math.pi
    out: list[OrderContribution] = []
    for n in range(1, 6):
        factor = a_over_pi ** n
        contrib = COEFFS[n] * factor
        sigma_contrib = SIGMA_COEFFS[n] * factor
        out.append(
            OrderContribution(
                n=n,
                label=LABELS[n],
                coefficient=COEFFS[n],
                sigma_coefficient=SIGMA_COEFFS[n],
                contribution=contrib,
                sigma_contribution=sigma_contrib,
                n_diagrams=N_DIAGRAMS[n],
            )
        )
    return out


def a_e_qed_universal(alpha: float) -> float:
    """Sum of the universal QED contributions through five loops (orders 1 to 5)."""
    return sum(oc.contribution for oc in order_contributions(alpha))


def sigma_a_e_qed_truncation(alpha: float) -> float:
    """Truncation uncertainty from the published $\\sigma(c_4)$ and $\\sigma(c_5)$."""
    contribs = order_contributions(alpha)
    return math.sqrt(sum(oc.sigma_contribution ** 2 for oc in contribs))
