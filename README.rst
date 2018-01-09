NURBS-Python Example Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This repository contains examples for the NURBS-Python_ package.

Directory Structure
===================

* ``curve2d/`` contains examples for :code:`BSpline.Curve2D` and :code:`NURBS.Curve2D` classes
* ``curve3d/`` contains examples for :code:`BSpline.Curve` and :code:`NURBS.Curve` classes
* ``surface/`` contains examples for :code:`BSpline.Surface` and :code:`NURBS.Surface` classes
* ``grid/`` contains examples for :code:`CPGen.Grid` and :code:`CPGen.GridWeighted` classes
* ``visualization/`` contains some visualization examples. Please see the `README <visualization/README.md>`_ file inside the directory for details.

Input Files
-----------

``*.cpt`` and ``*.cptw`` files are simple text files. They contain *control points* and *weighted control points*,
respectively. Please see the `NURBS-Python repository <https://github.com/orbingol/NURBS-Python>`_  on details of the
file formats.

Visualization
-------------

The examples ``curve2d/ex_curve01.py`` and ``curve3d/ex_curve3d01.py`` illustrate usage of the optional visualization
component which comes with the NURBS-Python package.

More advanced visualization options and some example figures with the instructions on how to generate them can be
found under ``visualization/`` directory.

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
