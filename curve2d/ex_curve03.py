#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
# from geomdl.visualization import VisMPL
from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline curve instance
curve = BSpline.Curve()

# Set up the NURBS curve
curve.ctrlpts = exchange.import_txt("ex_curve03.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaulate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
vis_comp = VisPlotly.VisCurve2D()
curve.vis = vis_comp
curve.render()

# Evaluate curve tangent at u = 0.0
curvetan1 = curve.tangent(0.0, normalize=True)

# Evaluate curve tangent at u = 0.2
curvetan2 = curve.tangent(0.2, normalize=True)

# Evaluate curve tangent at u = 0.5
curvetan3 = curve.tangent(0.5, normalize=True)

# Evaluate curve tangent at u = 0.6
curvetan4 = curve.tangent(0.6, normalize=True)

# Evaluate curve tangent at u = 0.8
curvetan5 = curve.tangent(0.8, normalize=True)

# Evaluate curve tangent at u = 1.0
curvetan6 = curve.tangent(1.0, normalize=True)

# Good to have something here to put a breakpoint
pass
