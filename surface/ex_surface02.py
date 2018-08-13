#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations
from geomdl.visualization import VisPlotly


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("ex_surface02.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 6)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 6)

# Set evaluation delta
surf.delta = 0.025

# Evaluate surface
surf.evaluate()

# Plot the control point grid and the evaluated surface
vis_comp = VisPlotly.VisSurface()
surf.vis = vis_comp
surf.render()

# Evaluate surface tangent and normal at the given u and v
uv = [0.2, 0.9]
surf_tangent = operations.tangent(surf, uv)
surf_normal = operations.normal(surf, uv)

# Good to have something here to put a breakpoint
pass
