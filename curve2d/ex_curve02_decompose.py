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

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 3
curve.ctrlpts = exchange.import_txt("ex_curve02.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Decompose the curve into Bezier curve segments
curve_list = operations.decompose_curve(curve)
bezier = multi.CurveContainer(curve_list)

# Move the curves a little bit away from each other (for display purposes only)
c2tan1 = bezier[1].tangent(0.0, normalize=True)
c2tanvec1 = [-1 * p for p in c2tan1[1]]
operations.translate(bezier[0], c2tanvec1, inplace=True)

c2tan2 = bezier[1].tangent(1.0, normalize=True)
c2tanvec2 = [1 * p for p in c2tan2[1]]
operations.translate(bezier[2], c2tanvec2, inplace=True)

# Set sample size of the Bezier curves
bezier.sample_size = 20

# Plot the Bezier curves
vis_comp = VisMPL.VisCurve2D()
bezier.vis = vis_comp
bezier.render()

# Good to have something here to put a breakpoint
pass
