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
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 2

# Set control points for a periodic curve
curve.ctrlpts = [[1, 0], [-1, 0], [-1.5, 1.5], [1.5, -1.5], [1, 0], [-1, 0]]

# Knot vector
curve.knotvector = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Set evaluation delta
curve.sample_size = 100

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
vis_config = VisMPL.VisConfig(ctrlpts=False, legend=False)
vis_comp = VisMPL.VisCurve2D(vis_config)
curve.vis = vis_comp
curve.render()

# Good to have something here to put a breakpoint
pass
