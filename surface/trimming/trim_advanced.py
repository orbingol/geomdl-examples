#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from matplotlib import cm
from geomdl import BSpline
from geomdl import exchange
from geomdl import tessellate
from geomdl.visualization import VisMPL as vis
from geomdl import knotvector
from geomdl import trimming


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("../ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set sample size
surf.sample_size = 50

# Set surface tessellation component
surf.tessellator = tessellate.TrimTessellate()

# Set visualization component
visconf = vis.VisConfig(ctrlpts=False, legend=False)
surf.vis = vis.VisSurface(config=visconf)

# Generate a trim curve
tcrv = BSpline.Curve()
tcrv.degree = 1
tcrv.ctrlpts = [[0.5, 0.0], [0.5, 0.5], [0.0, 0.5]]
tcrv.knotvector = knotvector.generate(1, 3)
trim_curves = [tcrv]

# Set trim curves (as a list)
surf.trims = trim_curves

# Fix trimming curves
# trimming.fix_trim_curves(surf)

# Visualize surface
surf.render(colormap=cm.copper)

# # Save as Wavefront OBJ file
# exchange.export_obj(surf, "trim_advanced.obj")

# Good to have something here to put a breakpoint
pass
