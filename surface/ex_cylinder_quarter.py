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
from geomdl.visualization import VisMPL as vis


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degrees
surf.degree_u = 1
surf.degree_v = 2

# Set control points
surf.set_ctrlpts(*exchange.import_txt("ex_cylinder_quarter.cptw", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 1, 1, 1]

# Set evaluation delta
surf.delta = 0.05

# Evaluate surface
surf.evaluate()

# Plot the control point grid and the evaluated surface
vis_comp = vis.VisSurface()
surf.vis = vis_comp
surf.render()

# Good to have something here to put a breakpoint
pass
