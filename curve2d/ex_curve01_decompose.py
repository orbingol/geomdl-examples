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
from geomdl import exchange
from geomdl import operations

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.ctrlpts = exchange.import_txt("ex_curve01.cpt")
curve.degree = 4

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Decompose the curve into Bezier curve segments
bezier = operations.decompose_curve(curve)

# Plot the curves using the curve container
bezier.sample_size = 40

if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    bezier.vis = vis_comp
    bezier.render()

# Good to have something here to put a breakpoint
pass
