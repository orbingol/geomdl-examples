#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 2

# Set control points for a periodic curve
curve.ctrlpts = [[-1, 0], [-0.5, 0.5], [0.5, -0.5], [1, 0]]

# Knot vector for unclamped curve
curve.knotvector = [0, 1, 2, 3, 4, 5, 6]

# Set evaluation delta
curve.delta = 0.01

# Evaulate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve2D()
curve.vis = vis_comp
curve.render()

# Good to have something here to put a breakpoint
pass
