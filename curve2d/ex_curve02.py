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
from geomdl import evaluators
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 3
curve.ctrlpts = exchange.import_txt("ex_curve02.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve2D()
curve.vis = vis_comp
curve.render()

# Evaluate derivatives at u = 0.6
ders1 = curve.derivatives(0.6, 4)

# Change evaluator
curve.evaluator = evaluators.CurveEvaluator2()

# Evaluate derivatives at u = 0.6 using the new evaluator
ders2 = curve.derivatives(0.6, 4)

# Compute curve tangent at u = 0.6
curvetan = operations.tangent(curve, 0.6)

# Good to have something here to put a breakpoint
pass
