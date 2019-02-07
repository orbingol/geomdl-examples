#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""

import os
from geomdl import NURBS
from geomdl import exchange
from geomdl import operations
from geomdl import multi
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS curve instance (full circle)
curve = NURBS.Curve()

# Set up the curve
curve.degree = 2
curve.ctrlptsw = exchange.import_txt("ex_curve04.cptw")

# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Decompose the curve into Bezier curve segments
curve_list = operations.decompose_curve(curve)
bezier = multi.CurveContainer(curve_list)

# Set sample size of the Bezier curves
bezier.sample_size = 25

# Plot the Bezier curves
vis_config = VisMPL.VisConfig(figure_size=[8, 8])
vis_comp = VisMPL.VisCurve2D(vis_config)
bezier.vis = vis_comp
bezier.render()

# Good to have something here to put a breakpoint
pass
