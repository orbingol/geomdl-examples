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

# Create a B-Spline curve instance (Bezier Curve)
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up the Bezier curve
curve.ctrlpts = [[10, 0], [15, 15], [20, 0]]
curve.degree = 2

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    curve.vis = vis_comp
    curve.render()
