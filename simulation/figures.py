"""Two figures: stratigraphic decomposition, precision timeline."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from alpha_values import AE_FAN_2023
from corrections import HADRONIC, WEAK
from precision_history import HISTORY
from qed_series import order_contributions


def plot_stratigraphy(savepath: str, mass_dep_residual: float = 0.0) -> None:
    alpha = AE_FAN_2023.value
    contribs = order_contributions(alpha)

    labels = [
        "1\nSchwinger\n(1948)",
        "2\nSommerfield\n(1957)",
        "3\nLaporta-\nRemiddi (1996)",
        "4\nKinoshita\ngroup",
        "5\nAoyama et al.\n(2012)",
        "mass-dep\nresidual",
        "hadronic",
        "weak",
    ]
    values = [oc.contribution for oc in contribs] + [
        mass_dep_residual,
        HADRONIC.value,
        WEAK.value,
    ]
    abs_values = [abs(v) for v in values]
    signs = ["+" if v >= 0 else "-" for v in values]

    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    colors = ["#2b6cb0" if s == "+" else "#c53030" for s in signs]
    bars = ax.bar(range(len(labels)), abs_values, color=colors, log=True)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=7.5)
    ax.set_ylabel(r"$|\mathrm{contribution}|$ to $a_e$")
    ax.set_title(
        r"Layers of $a_e = (g-2)/2 = 0.00115965218059$ (blue: $+$, red: $-$)"
    )
    ax.grid(True, axis="y", which="both", linewidth=0.3, alpha=0.4)
    for i, v in enumerate(values):
        ax.annotate(
            f"{signs[i]}{abs_values[i]:.2e}",
            xy=(i, abs_values[i]),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            fontsize=6.5,
        )
    fig.tight_layout()
    fig.savefig(savepath, dpi=150)
    plt.close(fig)


def plot_precision_history(savepath: str) -> None:
    years = [m.year for m in HISTORY]
    rel = [m.relative_uncertainty for m in HISTORY]
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.semilogy(years, rel, "o-", color="#1a202c", markersize=7, linewidth=1.4)
    for m in HISTORY:
        ax.annotate(
            m.lab.split(" (")[0],
            xy=(m.year, m.relative_uncertainty),
            xytext=(7, 6),
            textcoords="offset points",
            fontsize=7,
            color="#2d3748",
        )
    ax.set_xlabel("year")
    ax.set_ylabel(r"relative uncertainty in $g/2$")
    ax.set_title(r"Precision of the electron $g/2$ measurement, 1948 to 2023")
    ax.grid(True, which="both", linewidth=0.3, alpha=0.5)
    fig.tight_layout()
    fig.savefig(savepath, dpi=150)
    plt.close(fig)
