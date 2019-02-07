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
from geomdl import multi
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 4
curve.ctrlpts = exchange.import_txt("ex_curve01.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Split the curve
curve_list = operations.split_curve(curve, 0.6)
curves = multi.CurveContainer(curve_list)

# Move the 1st curve a little bit far away from the 2nd curve
c2tan = curves[1].tangent(0.0, normalize=True)
c2tanvec = [-3 * p for p in c2tan[1]]
operations.translate(curves[0], c2tanvec, inplace=True)

# Plot the curves using the curve container
curves.sample_size = 40

# Plot the curve
vis_comp = VisMPL.VisCurve2D()
curves.vis = vis_comp
curves.render()

# Good to have something here to put a breakpoint
pass
