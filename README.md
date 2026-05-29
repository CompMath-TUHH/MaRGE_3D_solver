# MaRGE3D package

[![Read the Docs](https://img.shields.io/readthedocs/marge-3d-solver?logo=readthedocs)](https://marge-3d-solver.readthedocs.io/)
[![Repo status](https://www.repostatus.org/badges/latest/active.svg)](https://github.com/CompMath-TUHH/MaRGE_3D_solver)
[![CI pipeline](https://github.com/CompMath-TUHH/MaRGE_3D_solver/actions/workflows/ci_pipeline.yml/badge.svg)](https://github.com/CompMath-TUHH/MaRGE_3D_solver/actions/workflows/ci_pipeline.yml)
[![Coverage](https://codecov.io/github/CompMath-TUHH/MaRGE_3D_solver/graph/badge.svg?token=5Q6GS039XF)](https://codecov.io/github/CompMath-TUHH/MaRGE_3D_solver)
[![PyPI - Package](https://img.shields.io/pypi/v/marge3d?logo=python)](https://pypi.org/project/marge3d)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/marge3d?logo=pypi)](https://pypistats.org/packages/marge3d)

📜 _Solver for Maxey-Riley-Gatignol Equations (MaRGE) in 3D flow based on the method by [Daitche (2013)](https://doi.org/10.1016/j.jcp.2013.07.024). Analytical solution in simple vortex is provided to validate the method._

[![DOI](https://zenodo.org/badge/1090126264.svg)](https://doi.org/10.5281/zenodo.17601798)

MaRGE3D solves the full MaRGE, including the Basset history term, for inertial particles moving in three-dimensional fluid flow fields. The history term is treated with the specialized quadrature schemes of Daitche, matched with first, second, and third order Adams–Bashforth methods. The package also provides an analytical reference solution for a particle in a three-dimensional vortex flow under gravity, which can be used to verify any implementation of a 3D MaRGE solver.

## Attribition

You can freely use and reuse this code in line with its [license](https://github.com/CompMath-TUHH/MaRGE_3D_solver/blob/main/LICENSE). If you use it (or parts of it) for a publication, please cite
```bibtex
@article{Rathi2026,
  author  = {Rathi, Vamika and Ruprecht, Daniel},
  title   = {Numerical Modeling of Inertial Particles in Three-Dimensional Fluid Flow},
  journal = {Proceedings in Applied Mathematics and Mechanics},
  volume  = {26},
  number  = {2},
  pages   = {e70158},
  year    = {2026},
  doi     = {10.1002/pamm.70158},
  url     = {https://doi.org/10.1002/pamm.70158}
}
```


## Installation

```bash
pip install marge3d
```

> 🔔 _Checkout the [latest documentation build](https://marge-3d-solver.readthedocs.io/en/latest/) and_
> _in particular the [**notebook tutorials**](https://marge-3d-solver.readthedocs.io/en/latest/notebooks.html)_

## Links

- Documentation : https://marge-3d-solver.readthedocs.io
- Issues Tracker : https://github.com/CompMath-TUHH/MaRGE_3D_solver/issues

## Structure of the code

The main functionality is found in the modules located in the
`./marge3d`
folder:

* `numeric.py` — `NumericalSolver` class implementing Daitche's first, second, and third order schemes for the full 3D MaRGE.
* `analytic.py` — `AnalyticalSolver` class providing the analytical solution for a particle in a 3D vortex under gravity.
* `fields.py` — `VelocityField3D` class defining the vortex velocity field.
* `params.py` — `DaitcheParameters` class converting physical parameters into the dimensionless quantities (`R`, `S`, `G`) used by the solver.
* `utils.py` — helper routines.
Scripts to produce the figures from the paper can be found in the
`./scripts`
folder. Tests are located in
`./tests`
and can be run by typing

```bash
pytest ./tests/
```

while in the base folder of the code.

## How can I reproduce figures from the paper "Numerical Modeling of Inertial Particles in Three-Dimensional Fluid Flow"?

The scripts to reproduce the figures from this paper can be found [here](https://github.com/CompMath-TUHH/MaRGE_3D_solver/tree/main/scripts).

* Fig. 1 (left, positively buoyant particle trajectory) --> `scripts/run_analytical_solution.py` with `particle_density = 500`
* Fig. 1 (right, negatively buoyant particle trajectory) --> `scripts/run_Daitche_solution.py` with `particle_density = 1410`
* Fig. 2 (convergence, lighter particle, zero initial relative velocity) --> `scripts/run_convergence.py` with `particle_density = 500` and zero initial relative velocity `W0 = V0 - U0 = 0`; vary the Stokes number for `S = 3` (left) and `S = 0.3` (right)
* Fig. 3 (convergence, lighter particle, non-zero initial relative velocity) --> `scripts/run_convergence.py` with `particle_density = 500` and `W0 = (0, 0.1, 0)`; `S = 3` (left) and `S = 0.3` (right)
* Fig. 4 (convergence, heavier particle, zero initial relative velocity) --> `scripts/run_convergence.py` with `particle_density = 1410` and `W0 = 0`; `S = 3` (left) and `S = 0.3` (right)
* Fig. 5 (convergence, heavier particle, non-zero initial relative velocity) --> `scripts/run_convergence.py` with `particle_density = 1410` and `W0 = (0, 0.1, 0)`; `S = 3` (left) and `S = 0.3` (right)
> ℹ️ The Stokes number `S` is controlled through the particle radius, kinematic viscosity and characteristic time via `S = (1/3) a²/(ν T)`. The analytical solution is only valid for particles less dense than the fluid (`ρ_p/ρ_f < 5/8`) and assumes zero initial relative velocity; for the heavier particle and for non-zero initial relative velocity, the error is computed against a higher-resolution numerical reference solution instead of the analytical one. The analytical and numerical solutions agree only for the characteristic values `T = 0.1` and `U = 0.4` used in the paper.

## Acknowledgements

This project is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – SFB 1615 – 503850735. Open access funding enabled and organized by Projekt DEAL.


## Developers

- [Vamika Rathi](https://github.com/Vamika-Rathi)
- [Thibaut Lunet](https://github.com/tlunet)
