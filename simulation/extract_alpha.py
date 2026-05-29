"""Invert the Standard-Model prediction of a_e to extract alpha.

Given $a_e^{\\text{exp}} = \\sum_n c_n (\\alpha/\\pi)^n + a_e^{\\text{had}} +
a_e^{\\text{weak}} + r_{\\text{mass-dep}}$, solve for $\\alpha$. The
mass-dependent residual $r_{\\text{mass-dep}}$ is fixed externally
(by run_all.py) from the published total $a_e^{\\text{QED}}$ at a reference
$\\alpha$. Newton's method.
"""
from __future__ import annotations

from corrections import a_e_corrections
from qed_series import a_e_qed_universal


def a_e_prediction(alpha: float, mass_dep_residual: float = 0.0) -> float:
    return a_e_qed_universal(alpha) + a_e_corrections() + mass_dep_residual


def invert_alpha(
    a_e_exp: float,
    alpha_guess: float = 1.0 / 137.036,
    mass_dep_residual: float = 0.0,
    max_iter: int = 80,
) -> float:
    alpha = alpha_guess
    for _ in range(max_iter):
        f = a_e_prediction(alpha, mass_dep_residual) - a_e_exp
        h = alpha * 1e-8
        fp = (
            a_e_prediction(alpha + h, mass_dep_residual)
            - a_e_prediction(alpha - h, mass_dep_residual)
        ) / (2 * h)
        step = f / fp
        alpha -= step
        if abs(step) < 1e-22:
            break
    return alpha
