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

# Create a 3D B-Spline curve instance (Bezier Curve)
curve = BSpline.Curve()

# Set evaluation delta
curve.delta = 0.01

# Set up the Bezier curve
curve.ctrlpts = [[15, 5, 20], [7.5, 7.5, -25], [22.5, 7.5, 25], [14, 5, 0]]
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve3D()
    curve.vis = vis_comp
    curve.render()
