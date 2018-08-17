#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    3-dimensional B-Spline curve
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange

from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.degree = 4
curve.ctrlpts = exchange.import_txt("ex_curve3d01.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.001

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve3D()
curve.vis = vis_comp
curve.render()

# Insert a knot
u = 0.2
curve.insert_knot(u)

# Draw the control point polygon and the evaluated curve after knot insertion
curve.render()

# Good to have something here to put a breakpoint
pass
