"""Independent determinations of the fine-structure constant.

Three values appear in the paper:

* Parker, Yu, Zhong, Estey, Müller (2018, Science 360, 191) -- cesium recoil
  via matter-wave atom interferometry. $\\alpha^{-1} = 137.035999046(27)$.
* Morel, Yao, Cladé, Guellati-Khélifa (2020, Nature 588, 61) -- rubidium recoil
  via matter-wave atom interferometry. $\\alpha^{-1} = 137.035999206(11)$.
* Fan, Myers, Sukra and Gabrielse (2023, PRL 130, 071801) -- $\\alpha^{-1}$
  extracted from the measurement of $g/2$ by inverting the Standard-Model
  prediction. $\\alpha^{-1} = 137.035999166(15)$.

The Cs and Rb values disagree at 5.4 sigma; the $a_e$-inverted value sits
between them but closer to Rb.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class AlphaValue:
    label: str
    short: str
    inv_value: float
    inv_sigma: float

    @property
    def value(self) -> float:
        return 1.0 / self.inv_value

    @property
    def sigma(self) -> float:
        return self.inv_sigma / self.inv_value ** 2

    @property
    def rel_sigma(self) -> float:
        return self.inv_sigma / self.inv_value

    def as_dict(self) -> dict:
        return {
            "label": self.label,
            "short": self.short,
            "alpha_inv": self.inv_value,
            "sigma_alpha_inv": self.inv_sigma,
            "alpha": self.value,
            "sigma_alpha": self.sigma,
            "rel_sigma": self.rel_sigma,
        }


CS_PARKER_2018 = AlphaValue(
    label="Parker, Yu, Zhong, Estey, Müller (2018), Berkeley, Cs recoil",
    short="Cs (Berkeley 2018)",
    inv_value=137.035999046,
    inv_sigma=27e-9,
)


RB_MOREL_2020 = AlphaValue(
    label="Morel, Yao, Cladé, Guellati-Khélifa (2020), Paris, Rb recoil",
    short="Rb (Paris 2020)",
    inv_value=137.035999206,
    inv_sigma=11e-9,
)


AE_FAN_2023 = AlphaValue(
    label="Fan, Myers, Sukra, Gabrielse (2023), inverted from $a_e$ via QED+had+weak",
    short="$a_e$-inverted (Fan 2023)",
    inv_value=137.035999166,
    inv_sigma=15e-9,
)


def cs_rb_tension_sigma() -> float:
    delta = CS_PARKER_2018.inv_value - RB_MOREL_2020.inv_value
    combined = math.sqrt(
        CS_PARKER_2018.inv_sigma ** 2 + RB_MOREL_2020.inv_sigma ** 2
    )
    return abs(delta) / combined


def sigma_a_e_from_alpha(alpha_value: AlphaValue, a_e_central: float) -> float:
    """Uncertainty in a_e^th propagated from sigma(alpha).

    To leading order $a_e \\propto \\alpha$, so $\\sigma(a_e) / a_e \\approx
    \\sigma(\\alpha)/\\alpha$. Higher-order QED contributions soften this slightly
    but the leading-order relation is accurate to one part in 700 for the present
    central values.
    """
    return a_e_central * alpha_value.rel_sigma
