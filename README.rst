NURBS-Python Examples
^^^^^^^^^^^^^^^^^^^^^

This repository contains API demonstration scripts for the NURBS-Python_ package. Please see the
`documentation <http://nurbs-python.readthedocs.io/en/latest>`_ for more details.

Branch Information
==================

* ``master`` branch contains examples compatible with NURBS-Python v4.x (currently beta)
* ``3.x`` branch contains examples compatible with NURBS-Python v3.x
* ``2.x`` branch contains examples compatible with NURBS-Python v2.x

Directory Structure
===================

* ``curve2d/`` contains 2D curve examples
* ``curve3d/`` contains 3D curve examples
* ``surface/`` contains surface examples
* ``grid/`` contains examples for surface grid generator
* ``visualization/`` contains advanced visualization examples. Please see NURBS-Python_ documentation for details.
* ``bezier/`` contains Bezier curve and surface examples
* ``shapes/`` contains examples demonstrating ``geomdl.shapes`` component
* ``exchange/`` contains examples demonstrating  ``geomdl.exchange`` module
* ``compat/`` contains examples which utilize ``geomdl.compatibility`` module for data conversion

Input Files
-----------

``*.cpt`` and ``*.cptw`` files are simple text files. They contain *control points* and *weighted control points*,
respectively. Please see the NURBS-Python_ documentation for details on the input file formats.

Author
======

* Onur Rauf Bingol (`@orbingol <https://github.com/orbingol>`_)

License
=======

NURBS-Python_ package and all the scripts in this repository are licensed under the `MIT License <LICENSE>`_.

Acknowledgments
===============

I would like to thank my PhD adviser, `Dr. Adarsh Krishnamurthy <https://www.me.iastate.edu/faculty/?user_page=adarsh>`_,
for his guidance and supervision throughout the course of this project.

In addition, I would like to thank
`all NURBS-Python contributors <https://github.com/orbingol/NURBS-Python/blob/master/CONTRIBUTORS.rst>`_
for their time and effort in fixing, extending and supporting this project.


.. _NURBS-Python: https://github.com/orbingol/NURBS-Python
