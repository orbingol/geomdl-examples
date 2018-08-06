#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    3rd degree 3-dimensional Bezier curve
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a 3D B-Spline curve instance (Bezier Curve)
curve = BSpline.Curve()

# Set up the Bezier curve
curve.degree = 3
curve.ctrlpts = [[10, 5, 10], [10, 20, -30], [40, 10, 25], [-10, 5, 0]]

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.sample_size = 40

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve3D()
curve.vis = vis_comp

# Don't pop up the plot window, instead save it as a PDF file
curve.render(filename="bezier.pdf", plot=False)

pass
