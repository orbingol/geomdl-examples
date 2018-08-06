#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Split the surface
surfaces1 = surf.split_u(t=0.25)

# Split once more
surfaces = surfaces1[1].split_v(t=0.75)
surfaces.add(surfaces1[0])

# Set number of samples for all split surfaces
surfaces.sample_size = 20

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurfTriangle()
surfaces.vis = vis_comp
surfaces.render()

# Good to have something here to put a breakpoint
pass
