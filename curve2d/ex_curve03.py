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
from geomdl import operations
# from geomdl.visualization import VisMPL
from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 3
curve.ctrlpts = exchange.import_txt("ex_curve03.cpt")

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
curvetan1 = operations.tangent(curve, 0.0, normalize=True)

# Evaluate curve tangent at u = 0.2
curvetan2 = operations.tangent(curve, 0.2, normalize=True)

# Evaluate curve tangent at u = 0.5
curvetan3 = operations.tangent(curve, 0.5, normalize=True)

# Evaluate curve tangent at u = 0.6
curvetan4 = operations.tangent(curve, 0.6, normalize=True)

# Evaluate curve tangent at u = 0.8
curvetan5 = operations.tangent(curve, 0.8, normalize=True)

# Evaluate curve tangent at u = 1.0
curvetan6 = operations.tangent(curve, 1.0, normalize=True)

# Good to have something here to put a breakpoint
pass
