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

# Decompose the curve into Bezier curve segments
bezier_curves = operations.decompose_curve(curve)
bezier = multi.CurveContainer(bezier_curves)

# Plot the curves using the curve container
bezier.sample_size = 40
vis_comp = VisMPL.VisCurve2D()
bezier.vis = vis_comp
bezier.render()

# Good to have something here to put a breakpoint
pass
