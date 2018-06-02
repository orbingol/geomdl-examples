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

from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up curve
curve.ctrlpts = exchange.read_txt("ex_curve3d01.cpt")
curve.degree = 4

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Split the curve
curves = curve.split(0.3)

# Move the 1st curve a little bit far away from the 2nd curve
c2tan = curves[1].tangent(0.0, normalize=True)
c2tanvec = [-1 * p for p in c2tan[1]]
curves[0].translate(c2tanvec)

# Plot the curves using the curve container
curves.sample_size = 100

# Plot the control point polygon and the evaluated curve
vis_comp = VisPlotly.VisCurve3D()
curves.vis = vis_comp
curves.render()

# Good to have something here to put a breakpoint
pass
