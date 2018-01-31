NURBS-Python Example Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This repository contains examples for the NURBS-Python_ package.

Directory Structure
===================

* ``curve2d/`` contains examples for ``BSpline.Curve2D`` and ``NURBS.Curve2D`` classes
* ``curve3d/`` contains examples for ``BSpline.Curve`` and ``NURBS.Curve`` classes
* ``surface/`` contains examples for ``BSpline.Surface`` and ``NURBS.Surface`` classes
* ``grid/`` contains examples for ``CPGen.Grid`` and ``CPGen.GridWeighted`` classes
* ``visualization/`` contains some visualization examples. Please see NURBS-Python_ documentation for details.
* ``bezier/`` contains examples for Bezier surfaces and 2D/3D curves generated using ``BSpline`` module

Input Files
-----------

``*.cpt`` and ``*.cptw`` files are simple text files. They contain *control points* and *weighted control points*,
respectively. Please see the NURBS-Python_ documentation for details on the input file formats.

Visualization
-------------

The following examples illustrate usage of the optional visualization component:

**2D Curves:**

* ``curve2d/ex_curve01.py``
* ``curve2d/ex_curve02.py``
* ``curve2d/ex_curve03.py``

**3D Curves:**

* ``curve3d/ex_curve3d01.py``
* ``curve3d/ex_curve3d02.py``

**Surfaces:**

* ``surface/ex_surface01.py``
* ``surface/ex_surface02.py``
* ``surface/ex_surface03.py``

More advanced visualization options and some example figures with the instructions on how to generate them can be
found under ``visualization/`` directory.

Branch Information
==================

* ``master`` branch contains examples compatible with the latest version of NURBS-Python v3.x series.
* ``2.x`` branch contains examples compatible with the latest version of NURBS-Python v2.x series.

Please note that there could be small API variations between the beta and the stable versions of the NURBS-Python package.

Author
======

* Onur Rauf Bingol (`@orbingol <https://github.com/orbingol>`_)

Contributors
============

I would like to thank all contributors for their help and support in testing, bug fixing and improvement of the NURBS-Python_
project.

* Luke Frisken (`@kellpossible <https://github.com/kellpossible>`_)
* John-Eric Dufour (`@jedufour <https://github.com/jedufour>`_)
* Jan Heczko (`@heczis <https://github.com/heczis>`_)

License
=======

NURBS-Python_ package and all example scripts are licensed under `The MIT License <LICENSE>`_.

Acknowledgments
===============

I would like to thank my PhD adviser, `Dr. Adarsh Krishnamurthy <https://www.me.iastate.edu/faculty/?user_page=adarsh>`_,
for his guidance and supervision throughout the course of this project.


.. _NURBS-Python: https://github.com/orbingol/NURBS-Python
