# Changelog

📜 _History of the main changes in the code, in complement to the commit history._

## From scripts to a proper package

### Package structure

Creation of the `marge3D` folder, containing a `__init__.py` file so it can be imported as a python package. Then :

- `Dtche_J_parameters_3D.py` -> [`marge3D/params.py`](../marge3d/params.py)
- `Dtche_J_cls_3D.py` -> [`marge3D/numeric.py`](../marge3d/numeric.py)
- `Analy_obj_3D.py` -> [`marge3D/analytic.py`](../marge3d/analytic.py)
- `Vortex_Fld_3D.py` -> [`marge3D/fields.py](../marge3d/fields.py)

> 💡 All import statements have been updated


### Class naming

Most class in `marge3D` have been renamed to follow the [standard Python conventions (PEP8)](https://peps.python.org/pep-0008), that is :

- `mr_parameter` -> `DaitcheParameters`
- `maxey_riley_analytic_3d` -> `AnalyticalSolution`
- `maxey_riley_Daitche_3d` -> `NumericalSolution`
- `velocity_field_3d` -> `VelocityField3D`

> 💡 All import statements have been updated, and unnecessary inheritances to the base `object` class have been removed


### Package setup

Created the `pyproject.toml` file at the root of the repository, containing this :

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "marge3d"
version = "0.0.1"
description = "Solver for Maxey-Riley-Gatignol (MaRGE) in 3D"
dependencies = [
    "numpy",
    "scipy",
    "matplotlib",
]
requires-python = ">=3.10"
maintainers = [
    {name = "Vamika Rathi", email = "vamika.rathi@tuhh.de"},
    {name = "Finn Sommer", email = "finn.sommer@tuhh.de"},
]
readme = "README.md"
classifiers = [
    "Development Status :: 3 - Alpha",

    "Topic :: Scientific/Engineering :: Mathematics",

    "License :: OSI Approved :: BSD License",

    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]

[project.urls]
Homepage = "https://github.com/CompMath-TUHH/MaRGE_3D_solver"
Tracker = "https://github.com/CompMath-TUHH/MaRGE_3D_solver/issues"
```

This allows to install locally the package now using

```bash
pip install -e .
```

> 💡 The `-e` option installs in editable mode, creating link to the `marge3d` package in the Python environment rather than copying the package into it.
> That way, any local modification on the package is automatically taken into account.