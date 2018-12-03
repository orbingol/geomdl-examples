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
from geomdl import multi
from geomdl import exchange
from geomdl import operations
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

# Split the curve
curve1, curve2 = operations.split_curve(curve, 0.2)

# Move the 1st curve a little bit far away from the 2nd curve
c2tan = curve2.tangent(0.0, normalize=True)
c2tanvec = [-1 * p for p in c2tan[1]]
operations.translate(curve1, c2tanvec, inplace=True)

# Plot the curves using the curve container
curves = multi.CurveContainer()
curves.sample_size = 40
curves.add(curve1)
curves.add(curve2)

vis_comp = VisMPL.VisCurve2D()
curves.vis = vis_comp
curves.render()

# Good to have something here to put a breakpoint
pass
