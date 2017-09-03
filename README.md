# NURBS-Python Examples

This repository contains examples for the [NURBS-Python](https://github.com/orbingol/NURBS-Python) package.

## Contents of the repository

* `ex*.py` files are testing scripts for demonstrating curve and surface evaluations
* `data\` directory contains sample control points for the testing scripts

## How to use NURBS-Python Package

### Coding Examples

**Curves:**

* [ex_curve01.py](ex_curve01.py)
* [ex_curve02.py](ex_curve02.py)
* [ex_curve03.py](ex_curve03.py)
* [ex_curve04.py](ex_curve04.py) _(A full circle)_

**Surfaces:**

* [ex_surface01.py](ex_surface01.py)
* [ex_surface02.py](ex_surface02.py)
* [ex_surface03.py](ex_surface03.py)

**Grid Generator**

* [ex_grid01.py](ex_grid01.py)

### Plots

The following plots are generated using [Matplotlib](http://matplotlib.org/).

#### File: ex_curve01.py

Displays the control points polygon and the evaluated curve using the an auto-generated uniform knot vector.

![2D line plots using Matplotlib](ex_curve01.png)

#### File: ex_curve02.py

Displays the evaluated curve using an auto-generated uniform knot vector and the tangent vector at u = 0.6.

![2D line plots using Matplotlib](ex_curve02.png)

#### File: ex_curve03.py

Displays the control points polygon and the evaluated curve using the an auto-generated uniform knot vector. Tangent vectors are shown in quiver plots.

![2D line plots using Matplotlib](ex_curve03.png)

#### File: ex_curve04.py

Displays the control points polygon and the evaluated NURBS curve for a full circle.

![2D line plots using Matplotlib](ex_curve04.png)

#### File: ex_surface01.py

![3D scatter plot using Matplotlib](ex_surface01.png)

#### File: ex_surface02.py

![3D scatter plot using Matplotlib](ex_surface02.png)

#### File: ex_surface03.py

![3D scatter plot using Matplotlib](ex_surface03.png)

Thanks to [@jedufour](https://github.com/jedufour) for `ex_surface03.py` example.

## License

[MIT](LICENSE)
