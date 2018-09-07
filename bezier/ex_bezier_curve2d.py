#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    2nd degree and 3rd degree 2-dimensional Bezier curves
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# 2D CURVE 1
#

# Create a B-Spline curve instance (Bezier Curve)
curve1 = BSpline.Curve()

# Set up the Bezier curve
curve1.degree = 2
curve1.ctrlpts = [[10, 0], [20, 15], [30, 0]]


# Auto-generate knot vector
curve1.knotvector = utilities.generate_knot_vector(curve1.degree, len(curve1.ctrlpts))

# Set evaluation delta
curve1.sample_size = 40

# Evaluate curve
curve1.evaluate()

# Draw the control point polygon and the evaluated curve
vis_comp1 = VisMPL.VisCurve2D()
curve1.vis = vis_comp1
curve1.render()

#
# 2D CURVE 2
#

# Create another B-Spline curve instance (Bezier Curve)
curve2 = BSpline.Curve()

# Set up the Bezier curve
curve2.degree = 3
curve2.ctrlpts = [[10, 0], [20, 15], [20, 15], [30, 0]]

# Auto-generate knot vector
curve2.knotvector = utilities.generate_knot_vector(curve2.degree, len(curve2.ctrlpts))

# Set evaluation delta
curve2.sample_size = 40

# Evaluate curve
curve2.evaluate()

# Draw the control point polygon and the evaluated curve
vis_comp2 = VisMPL.VisCurve2D()
curve2.vis = vis_comp2
curve2.render()

pass
