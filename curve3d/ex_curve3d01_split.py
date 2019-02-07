#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    A 3-dimensional B-Spline curve is split at u=0.3 and one of the split curves is translated using the tangent vector
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations
from geomdl import multi
from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.degree = 4
curve.ctrlpts = exchange.import_txt("ex_curve3d01.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Split the curve
split_curves = operations.split_curve(curve, 0.3)
curves = multi.CurveContainer(split_curves)

# Move the 1st curve a little bit far away from the 2nd curve
c2tan = operations.tangent(curves[1], 0.0, normalize=True)
c2tanvec = [-1 * p for p in c2tan[1]]
operations.translate(curves[0], c2tanvec, inplace=True)

# Plot the curves using the curve container
curves.sample_size = 100

# Plot the control point polygon and the evaluated curve
vis_comp = VisPlotly.VisCurve3D()
curves.vis = vis_comp
curves.render()

# Good to have something here to put a breakpoint
pass
