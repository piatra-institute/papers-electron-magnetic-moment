"""Hadronic and electroweak contributions to a_e.

Values from Aoyama, Kinoshita, and Nio (2019, Atoms 7, 28) and PDG reviews.
Both are positive and contribute at the $10^{-12}$ level.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Correction:
    label: str
    value: float
    sigma: float

    def as_dict(self) -> dict:
        return {"label": self.label, "value": self.value, "sigma": self.sigma}


HADRONIC = Correction(
    label="Hadronic (vacuum polarisation + light-by-light)",
    value=1.6927e-12,
    sigma=0.0120e-12,
)
"""Aoyama-Kinoshita-Nio (2019), summing the leading-order hadronic
vacuum-polarisation, NLO hadronic vacuum-polarisation, and hadronic
light-by-light contributions to $a_e$."""


WEAK = Correction(
    label="Electroweak (W, Z bosons)",
    value=0.02970e-12,
    sigma=0.00005e-12,
)
"""Czarnecki, Krause, and Marciano (1996), updated in PDG reviews."""


def a_e_corrections() -> float:
    return HADRONIC.value + WEAK.value


def sigma_a_e_corrections() -> float:
    return (HADRONIC.sigma ** 2 + WEAK.sigma ** 2) ** 0.5
