#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline, NURBS
from geomdl import exchange
from geomdl.visualization import VisMPL as vis
from geomdl import render


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree.u = 3
surf.degree.v = 3

# Set control points
surf.set_ctrlpts(exchange.import_txt("ex_surface01.cpt"), 6, 6)

# Set knot vectors
surf.knotvector.u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector.v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
surf.evaluate()

nsurf = NURBS.Surface.from_bspline(surf)

# Plot the control point grid and the evaluated surface
render.render(nsurf, vis.VisSurfScatter())

# Good to have something here to put a breakpoint
pass
