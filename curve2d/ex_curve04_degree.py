#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017-2019
"""

import os
from geomdl import NURBS
from geomdl import exchange
from geomdl import operations
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS curve instance (full circle)
curve = NURBS.Curve()

# Set up curve
curve.degree = 2
curve.ctrlptsw = exchange.import_txt("ex_curve04.cptw")

# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
curve.vis = VisMPL.VisCurve2D()
curve.render()

# Degree elevation
operations.degree_operations(curve, [1])
curve.render()

# Degree reduction
operations.degree_operations(curve, [-1])
curve.render()

# Good to have something here to put a breakpoint
pass
