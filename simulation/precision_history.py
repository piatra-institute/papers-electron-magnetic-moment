"""Timeline of milestone measurements of the electron $g/2$.

Each entry sources the published $g/2$ central value and one-sigma uncertainty
at the time of publication. The relative uncertainty $\\sigma(g/2) / (g/2)$
falls by roughly seven orders of magnitude over seven and a half decades.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Measurement:
    year: int
    g_over_2: float
    sigma_g_over_2: float
    lab: str
    reference: str

    @property
    def relative_uncertainty(self) -> float:
        return self.sigma_g_over_2 / self.g_over_2

    def as_dict(self) -> dict:
        return {
            "year": self.year,
            "g_over_2": self.g_over_2,
            "sigma_g_over_2": self.sigma_g_over_2,
            "rel_unc": self.relative_uncertainty,
            "lab": self.lab,
            "reference": self.reference,
        }


HISTORY: list[Measurement] = [
    Measurement(
        year=1948,
        g_over_2=1.00119,
        sigma_g_over_2=5e-5,
        lab="Columbia (atomic-beam magnetic resonance)",
        reference="Kusch and Foley (1948), Phys. Rev. 74, 250",
    ),
    Measurement(
        year=1963,
        g_over_2=1.0011609,
        sigma_g_over_2=4.0e-6,
        lab="Michigan (precession of polarised free electrons)",
        reference="Wilkinson and Crane (1963), Phys. Rev. 130, 852",
    ),
    Measurement(
        year=1987,
        g_over_2=1.00115965221,
        sigma_g_over_2=4e-12,
        lab="Washington (single-electron Penning trap, geonium)",
        reference="Van Dyck, Schwinberg and Dehmelt (1987), PRL 59, 26",
    ),
    Measurement(
        year=2008,
        g_over_2=1.00115965218073,
        sigma_g_over_2=2.8e-13,
        lab="Harvard (cylindrical Penning trap, quantum cyclotron)",
        reference="Hanneke, Fogwell and Gabrielse (2008), PRL 100, 120801",
    ),
    Measurement(
        year=2023,
        g_over_2=1.00115965218059,
        sigma_g_over_2=1.3e-13,
        lab="Northwestern (rebuilt apparatus, cavity-shift mitigation)",
        reference="Fan, Myers, Sukra and Gabrielse (2023), PRL 130, 071801",
    ),
]
