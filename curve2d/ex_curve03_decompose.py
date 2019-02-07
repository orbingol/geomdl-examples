#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl import operations
from geomdl import multi
# from geomdl.visualization import VisMPL as vis
from geomdl.visualization import VisPlotly as vis


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 3

# Read control points from a file
curve.ctrlpts = exchange.import_txt("ex_curve03.cpt")

# Set knot vector
curve.knotvector = [0, 0, 0, 0, 0.25, 0.25, 0.5, 0.75, 0.75, 1, 1, 1, 1]

# Decompose the curve
curve_list = operations.decompose_curve(curve)
curve_decomposed = multi.CurveContainer(curve_list)

# Set sample size for the decomposed curve
curve_decomposed.sample_size = 25

# Plot the decomposed curve
vis_comp = vis.VisCurve2D()
curve_decomposed.vis = vis_comp
curve_decomposed.render()

# Good to have something here to put a breakpoint
pass
