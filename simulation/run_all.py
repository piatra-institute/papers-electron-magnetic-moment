"""Reproducible orchestration of all numerical claims cited in the paper.

Writes ``output/results.json`` and the figure files under ``output/figures/``.
Every numeric claim in the paper should be traceable to a key in the JSON file.

Run with:

    cd simulation
    uv run run_all.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from alpha_values import (
    AE_FAN_2023,
    CS_PARKER_2018,
    RB_MOREL_2020,
    cs_rb_tension_sigma,
    sigma_a_e_from_alpha,
)
from corrections import HADRONIC, WEAK, a_e_corrections, sigma_a_e_corrections
from extract_alpha import a_e_prediction, invert_alpha
from figures import plot_precision_history, plot_stratigraphy
from precision_history import HISTORY
from qed_series import (
    N_DIAGRAMS,
    a_e_qed_universal,
    order_contributions,
    sigma_a_e_qed_truncation,
)


OUT = Path(__file__).parent / "output"


# Fan, Myers, Sukra and Gabrielse (2023): g/2 = 1.001 159 652 180 59 (13).
G_OVER_2_FAN = 1.00115965218059
SIGMA_G_OVER_2_FAN = 1.3e-13
A_E_FAN = G_OVER_2_FAN - 1.0
SIGMA_A_E_FAN = SIGMA_G_OVER_2_FAN


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)

    # Experimental anchor.
    experimental = {
        "g_over_2": G_OVER_2_FAN,
        "sigma_g_over_2": SIGMA_G_OVER_2_FAN,
        "a_e": A_E_FAN,
        "sigma_a_e": SIGMA_A_E_FAN,
        "reference": "Fan, Myers, Sukra and Gabrielse (2023), PRL 130, 071801",
        "precision_ppt": SIGMA_G_OVER_2_FAN / G_OVER_2_FAN * 1e12,
    }

    # Alpha determinations.
    alpha_values = {
        "Cs_Parker_2018": CS_PARKER_2018.as_dict(),
        "Rb_Morel_2020": RB_MOREL_2020.as_dict(),
        "ae_inverted_Fan_2023": AE_FAN_2023.as_dict(),
        "Cs_vs_Rb_sigma": cs_rb_tension_sigma(),
    }

    # QED universal orders, evaluated at the Fan-inverted alpha.
    alpha = AE_FAN_2023.value
    contribs = order_contributions(alpha)
    a_e_qed_univ_total = a_e_qed_universal(alpha)
    sigma_qed_trunc = sigma_a_e_qed_truncation(alpha)

    qed_orders = {f"order_{oc.n}": oc.as_dict() for oc in contribs}
    qed_orders["sum_through_order_5_universal"] = a_e_qed_univ_total
    qed_orders["sigma_truncation_at_order_5"] = sigma_qed_trunc
    qed_orders["alpha_used"] = alpha
    qed_orders["alpha_inv_used"] = 1.0 / alpha

    # Mass-dependent residual: difference between measured a_e and our pure-electron
    # sum + hadronic + weak. This corresponds to the Aoyama-Kinoshita-Nio
    # A_2(m_e/m_mu) + A_2(m_e/m_tau) + A_3 contributions, plus residual five-loop
    # mass-dependent pieces and higher orders not separately modelled.
    corrections = {
        "hadronic": HADRONIC.as_dict(),
        "weak": WEAK.as_dict(),
        "sum_had_weak": a_e_corrections(),
        "sigma_sum_had_weak": sigma_a_e_corrections(),
    }
    mass_dep_residual = A_E_FAN - a_e_qed_univ_total - a_e_corrections()
    corrections["mass_dependent_residual"] = mass_dep_residual

    # Schwinger-dominance proposition.
    schwinger_contrib = contribs[0].contribution
    overshoot = schwinger_contrib - A_E_FAN
    schwinger_dominance = {
        "schwinger_contribution": schwinger_contrib,
        "a_e_fan": A_E_FAN,
        "schwinger_over_total_ratio": schwinger_contrib / A_E_FAN,
        "overshoot_absolute": overshoot,
        "overshoot_percent": overshoot / A_E_FAN * 100.0,
        "one_part_in": A_E_FAN / abs(overshoot),
        "higher_orders_total_universal": sum(oc.contribution for oc in contribs[1:]),
    }

    # Alpha-limited proposition.
    a_e_th_central = a_e_qed_univ_total + a_e_corrections() + mass_dep_residual
    sigma_a_e_from_Cs = sigma_a_e_from_alpha(CS_PARKER_2018, a_e_th_central)
    sigma_a_e_from_Rb = sigma_a_e_from_alpha(RB_MOREL_2020, a_e_th_central)

    a_e_pred_Cs = a_e_prediction(CS_PARKER_2018.value, mass_dep_residual)
    a_e_pred_Rb = a_e_prediction(RB_MOREL_2020.value, mass_dep_residual)
    a_e_pred_Fan = a_e_prediction(AE_FAN_2023.value, mass_dep_residual)

    Delta_Cs_Rb_pred = abs(a_e_pred_Cs - a_e_pred_Rb)
    sigma_comb_thy = math.sqrt(sigma_a_e_from_Cs ** 2 + sigma_a_e_from_Rb ** 2)
    Delta_in_thy_sigma = Delta_Cs_Rb_pred / sigma_comb_thy

    alpha_limited = {
        "a_e_th_central_at_Fan_alpha": a_e_th_central,
        "sigma_a_e_qed_truncation": sigma_qed_trunc,
        "sigma_a_e_had_weak": sigma_a_e_corrections(),
        "sigma_a_e_from_alpha_Cs": sigma_a_e_from_Cs,
        "sigma_a_e_from_alpha_Rb": sigma_a_e_from_Rb,
        "a_e_pred_Cs": a_e_pred_Cs,
        "a_e_pred_Rb": a_e_pred_Rb,
        "a_e_pred_Fan": a_e_pred_Fan,
        "Delta_a_e_Cs_vs_Rb": Delta_Cs_Rb_pred,
        "Cs_vs_Rb_a_e_sigma": Delta_in_thy_sigma,
        "ratio_alpha_Rb_to_truncation": sigma_a_e_from_Rb / sigma_qed_trunc,
        "ratio_alpha_Cs_to_truncation": sigma_a_e_from_Cs / sigma_qed_trunc,
        "sigma_a_e_exp_Fan_2023": SIGMA_A_E_FAN,
    }

    # Self-inversion check.
    alpha_inverted = invert_alpha(A_E_FAN, mass_dep_residual=mass_dep_residual)
    inversion = {
        "alpha_inverted": alpha_inverted,
        "alpha_inv_inverted": 1.0 / alpha_inverted,
        "alpha_inv_published_Fan": AE_FAN_2023.inv_value,
        "diff_alpha_inv": 1.0 / alpha_inverted - AE_FAN_2023.inv_value,
    }

    # Precision history.
    precision_history = [m.as_dict() for m in HISTORY]
    if len(HISTORY) >= 2:
        first, last = HISTORY[0], HISTORY[-1]
        precision_history_meta = {
            "years_span": last.year - first.year,
            "relative_uncertainty_improvement_factor": (
                first.relative_uncertainty / last.relative_uncertainty
            ),
            "log10_improvement": math.log10(
                first.relative_uncertainty / last.relative_uncertainty
            ),
        }
    else:
        precision_history_meta = {}

    results = {
        "experimental": experimental,
        "alpha_values": alpha_values,
        "qed_orders": qed_orders,
        "corrections": corrections,
        "schwinger_dominance": schwinger_dominance,
        "alpha_limited": alpha_limited,
        "inversion_check": inversion,
        "precision_history": precision_history,
        "precision_history_meta": precision_history_meta,
        "n_diagrams_by_order": N_DIAGRAMS,
    }

    # Figures.
    plot_stratigraphy(
        str(OUT / "figures" / "stratigraphy.png"),
        mass_dep_residual=mass_dep_residual,
    )
    plot_precision_history(str(OUT / "figures" / "precision_history.png"))

    # Persist.
    with (OUT / "results.json").open("w") as f:
        json.dump(results, f, indent=2, default=float)

    # Console summary.
    print(f"a_e (Fan 2023):                       {A_E_FAN:.18e}")
    print(f"a_e^QED universal (5-loop) at Fan a:  {a_e_qed_univ_total:.18e}")
    print(f"a_e^had:                              {HADRONIC.value:.6e}")
    print(f"a_e^weak:                             {WEAK.value:.6e}")
    print(f"mass-dep residual:                    {mass_dep_residual:+.6e}")
    print(f"Total a_e^th (matches by construction): {a_e_th_central:.18e}")
    print()
    print("Order by order (at Fan-inverted alpha):")
    for oc in contribs:
        print(
            f"  n={oc.n} ({oc.label[:45]:45s})  "
            f"c_n = {oc.coefficient:+.10f}  "
            f"contribution = {oc.contribution:+.6e}  "
            f"diagrams = {oc.n_diagrams}"
        )
    print()
    print(
        f"Schwinger overshoots a_e by:  {overshoot:+.3e}  "
        f"({overshoot / A_E_FAN * 100:+.3f}%, one part in {A_E_FAN / abs(overshoot):.1f})"
    )
    print()
    print(f"Cs vs Rb tension in alpha^-1: {cs_rb_tension_sigma():.2f} sigma")
    print(f"Cs vs Rb tension in predicted a_e: {Delta_in_thy_sigma:.2f} sigma")
    print(f"  Delta a_e (Cs vs Rb): {Delta_Cs_Rb_pred:.3e}")
    print(f"  sigma(a_e^th) from alpha_Cs: {sigma_a_e_from_Cs:.3e}")
    print(f"  sigma(a_e^th) from alpha_Rb: {sigma_a_e_from_Rb:.3e}")
    print(f"  sigma(QED truncation): {sigma_qed_trunc:.3e}")
    print(f"  sigma(a_e^exp Fan): {SIGMA_A_E_FAN:.3e}")
    print()
    print(
        f"Inverted alpha^-1 (target {AE_FAN_2023.inv_value:.9f}): "
        f"{1 / alpha_inverted:.9f}"
    )
    print(f"Wrote: {OUT / 'results.json'}")


if __name__ == "__main__":
    main()
