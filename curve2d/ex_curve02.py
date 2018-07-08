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
from geomdl import evaluators

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

# Set up curve
curve.ctrlpts = exchange.import_txt("ex_curve02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
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
curvetan = curve.tangent(0.6)

# Good to have something here to put a breakpoint
pass
