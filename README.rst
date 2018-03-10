Examples for NURBS-Python Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This repository contains API demonstration scripts for the NURBS-Python_ package.

Requirements
============

NURBS-Python_ package is required to all examples in this repository. Please make sure that you have installed it
properly before running any of these examples.

The easiest method to install NURBS-Python_ is using `pip <https://pip.pypa.io/en/stable/>`_.

``pip install NURBS-Python``

Please see the NURBS-Python_ documentation for details.

Directory Structure
===================

* ``curve2d/`` contains 2D curve examples
* ``curve3d/`` contains 3D curve examples
* ``surface/`` contains surface examples
* ``grid/`` contains examples for surface grid generator
* ``visualization/`` contains visualization examples. Please see NURBS-Python_ documentation for details.
* ``bezier/`` contains Bezier curve and surface examples
* ``shapes/`` contains examples demonstrating ``geomdl.shapes`` component
* ``exchange/`` contains examples demonstrating  ``geomdl.exchange`` module
* ``compat/`` contains examples which utilize ``geomdl.compatibility`` module for data conversion

Input Files
-----------

``*.cpt`` and ``*.cptw`` files are simple text files. They contain *control points* and *weighted control points*,
respectively. Please see the NURBS-Python_ documentation for details on the input file formats.

Visualization
-------------

All examples in this repository uses Matplotlib visualization implementation, the ``VisMPL`` module.

``VisMPL`` module is designed to be a representative class for future visualization extensions therefore,
it might not be a perfect fit for advanced visualization purposes. More advanced visualization options and some
example figures with the instructions on how to generate them can be found under ``visualization/`` directory.

All the examples should work fine with the latest version of NURBS-Python_, but they might or might not work with the
older versions.

Branch Information
==================

* ``master`` branch contains examples compatible with the latest version of NURBS-Python v3.x series.
* ``2.x`` branch contains examples compatible with the latest version of NURBS-Python v2.x series.

Please note that there could be small API variations between the beta and the stable versions of the NURBS-Python
package.

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
