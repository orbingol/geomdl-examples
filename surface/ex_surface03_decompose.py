#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    The surface example is kindly contributed by John-Eric Dufour (@jedufour)
"""

import os
from geomdl import NURBS
from geomdl import exchange
from geomdl import operations
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degrees
surf.degree_u = 1
surf.degree_v = 2

# Set control points
surf.set_ctrlpts(*exchange.import_txt("ex_surface03.cptw", two_dimensional=True))

# Set knot vector
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Decompose the surface
surfaces = operations.decompose_surface(surf)

# Translate one of the surface patch
operations.translate(surfaces[1], (-0.25, 0.25, 0), inplace=True)

# Set number of samples for all split surfaces
surfaces.sample_size = 51

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurfWireframe()
surfaces.vis = vis_comp
surfaces.render()

# Good to have something here to put a breakpoint
pass
