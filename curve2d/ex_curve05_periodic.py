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

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set evaluation delta
curve.delta = 0.001

# Set degree
curve.degree = 2

# Set control points for a periodic curve
curve.ctrlpts = [[1, 0], [-1, 0], [-0.5, 0.5], [0.5, -0.5], [1, 0], [-1, 0]]

# Knot vector
curve.knotvector = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Evaulate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    curve.vis = vis_comp
    curve.render()

# Good to have something here to put a breakpoint
pass
