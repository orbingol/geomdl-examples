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
# from geomdl.visualization import VisMPL
from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.degree = 3
curve.ctrlpts = exchange.import_txt("ex_curve3d02.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisPlotly.VisCurve3D()
curve.vis = vis_comp
curve.render()

# Good to have something here to put a breakpoint
pass
