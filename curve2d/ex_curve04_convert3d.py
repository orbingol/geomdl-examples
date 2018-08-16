#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
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

# Convert to a 3D curve
curve3d = operations.add_dimension(curve)

# Translate curve to z = 5
operations.translate(curve3d, (0, 0, 5))

# Set evaluation delta
curve3d.delta = 0.01

# Plot the control point polygon and the evaluated curve
vis_config = VisMPL.VisConfig(ctrlpts=True)
vis_comp = VisMPL.VisCurve3D(vis_config)
curve3d.vis = vis_comp
curve3d.render()

# Good to have something here to put a breakpoint
pass
