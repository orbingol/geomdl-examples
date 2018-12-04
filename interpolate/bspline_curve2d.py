#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

from geomdl import interpolate
from geomdl.visualization import VisMPL as vis


# The NURBS Book Ex9.1
points = ((0, 0), (3, 4), (-1, 4), (-4, 0), (-4, -3))
degree = 3  # cubic curve

# Do global curve interpolation
curve = interpolate.interpolate_curve(points, degree)

# Plot the curve
curve.delta = 0.01
curve.vis = vis.VisCurve2D()
curve.render()
