#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl import operations
from geomdl import knotvector
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 4

# Set control points
curve.ctrlpts = exchange.import_txt("ex_curve01.cpt")

# Auto-generate knot vector
curve.knotvector = knotvector.generate(curve.degree, curve.ctrlpts_size)

# Set visualization component
curve.vis = VisMPL.VisCurve2D()

# Plot the control point polygon and the evaluated curve
curve.render()

# Apply knot refinement w/ density = 0 (no refinement)
operations.refine_knotvector(curve, [0])

# Plot the control point polygon and the evaluated curve (should be same as the previous one)
curve.render()

# Apply knot refinement w/ density = 1 (default)
operations.refine_knotvector(curve, [1])

# Plot the control point polygon and the evaluated curve after knot refinement
curve.render()

# Apply knot refinement w/ density = 2
operations.refine_knotvector(curve, [2])

# Plot the control point polygon and the evaluated curve after knot refinement
curve.render()

# Apply knot refinement w/ density = 3
operations.refine_knotvector(curve, [3])

# Plot the control point polygon and the evaluated curve after knot refinement
curve.render()

# Good to have something here to put a breakpoint
pass
