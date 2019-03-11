#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from geomdl import BSpline
from geomdl import multi
from geomdl import operations
from geomdl import exchange
from geomdl.visualization import VisMPL as vis


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf1 = BSpline.Surface()

# Set degrees
surf1.degree_u = 3
surf1.degree_v = 3

# Set control points
surf1.set_ctrlpts(*exchange.import_txt("ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf1.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf1.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set evaluation delta
surf1.delta = 0.025

# Rotate surf1 and generate a copy in surf2
surf2 = operations.rotate(surf1, 45, axis=2)

# Visualize surfaces
msurf1 = multi.SurfaceContainer(surf1, surf2)
msurf1.vis = vis.VisSurface()
msurf1.render()

# Decompose surf1
surf1_decomposed = operations.decompose_surface(surf1)
msurf2 = multi.SurfaceContainer(surf1_decomposed)

# Rotate decomposed surface
msurf2_rotated = operations.rotate(msurf2, 90, axis=1)

# Visualize decomposed and decomposed-rotated surfaces
msurf3 = multi.SurfaceContainer(msurf2, msurf2_rotated)
msurf3.vis = vis.VisSurface()
msurf3.render()

# Good to have something here to put a breakpoint
pass
