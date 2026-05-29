# Simulation

Reconstructs every numeric claim in `../paper/PAPER.md`. Runs in seconds.

```
uv run run_all.py
```

Produces `output/results.json` (every numeric claim cited in the paper is a key there) and two figures under `output/figures/`.

Modules:

- `qed_series.py` — universal QED coefficients $c_1, \ldots, c_5$ from Aoyama, Kinoshita and Nio (2019) and earlier authors.
- `corrections.py` — hadronic and electroweak contributions.
- `alpha_values.py` — Parker (2018, Cs), Morel (2020, Rb), Fan (2023, $a_e$-inverted) values of $\alpha^{-1}$.
- `extract_alpha.py` — inverts the SM prediction of $a_e$ for $\alpha$ by Newton's method.
- `precision_history.py` — timeline of $g/2$ measurements 1948 to 2023.
- `figures.py` — stratigraphic bar plot, precision-history plot.
- `run_all.py` — orchestrator.

Dependencies: `numpy>=1.26`, `matplotlib>=3.8`. Python $\geq$ 3.10.
