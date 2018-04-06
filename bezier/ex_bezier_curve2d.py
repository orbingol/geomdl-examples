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

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# 2D CURVE 1
#

# Create a B-Spline curve instance (Bezier Curve)
curve1 = BSpline.Curve()

# Set evaluation delta
curve1.delta = 0.01

# Set up the Bezier curve
curve1.ctrlpts = [[10, 0], [15, 15], [20, 0]]
curve1.degree = 2

# Auto-generate knot vector
curve1.knotvector = utilities.generate_knot_vector(curve1.degree, len(curve1.ctrlpts))

# Evaluate curve
curve1.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp1 = VisMPL.VisCurve2D()
    curve1.vis = vis_comp1
    curve1.render()

#
# 2D CURVE 2
#

# Create another B-Spline curve instance (Bezier Curve)
curve2 = BSpline.Curve()

# Set evaluation delta
curve2.delta = 0.01

# Set up the Bezier curve
curve2.ctrlpts = [[10, 0], [15, 15], [15, 15], [20, 0]]
curve2.degree = 3

# Auto-generate knot vector
curve2.knotvector = utilities.generate_knot_vector(curve2.degree, len(curve2.ctrlpts))

# Evaluate curve
curve2.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp2 = VisMPL.VisCurve2D()
    curve2.vis = vis_comp2
    curve2.render()
