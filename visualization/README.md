# Visualization Examples

NURBS-Python package is focused on geometric evaluations of 2D/3D NURBS curves and surfaces and it does not include any visualization component. I think there is no need to reinvent the wheel. As you may already know, there are a variety of programs and libraries focused on data visualization. For instance;

* [VTK](https://www.vtk.org/)
* [Paraview](https://www.paraview.org/) -- uses VTK and has Python bindings
* [Matplotlib](https://matplotlib.org/)

and even [OpenGL](https://www.opengl.org/) can directly be used to visualize data and can also be integrated in a [Qt](https://www.qt.io/) application via its OpenGL bindings.


However, I am aware of the fact that the wheel does not rotate by itself and therefore, I implemented several methods to export the control points and the evaluated curve/surface points as CSV files. These methods are:

* `save_ctrlpts_to_csv`: For control points in all classes
* `save_curvepts_to_csv`: For evaluated curve points in _Curve_ and _Curve2D_ classes
* `save_surfpts_to_csv`: For evaluated surface points in _Surface_ classes

CSV saving functionality has several modes which are accessible via `mode=` parameter.

* `linear`: Saves the points as they are stored in the class
* `zigzag`: Saves the points in the way that generates a zig-zag shape
* `wireframe`: Saves the points in the way that generates a wireframe shape

Please see the NURBS-Python documentation on CSV saving functionality for further details.

## Matplotlib

### ex_surface01.py

* Control points: `mode='wireframe'`
* Surface points: `mode='linear'`
* Evaluation delta: 0.05

![Surface ex01 3D trisurface plot](images/ex_surface01_mpl.png)

### ex_surface02.py

* Control points: `mode='wireframe'`
* Surface points: `mode='linear'`
* Evaluation delta: 0.05

![Surface ex02 3D trisurface plot](images/ex_surface02_mpl.png)

### ex_surface03.py

* Control points: `mode='linear'`
* Surface points: `mode='wireframe'`
* Evaluation delta: 0.05

![Surface ex03 3D wireframe plot](images/ex_surface03_mpl.png)
