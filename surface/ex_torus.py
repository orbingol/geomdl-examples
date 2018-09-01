#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Toroidal surface is contributed by Harshil Shah (@harshilsofeshah)
"""

import os
from geomdl import NURBS
from geomdl import exchange
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degress
surf.degree_u = 2
surf.degree_v = 2

# Set control points
surf.set_ctrlpts(*exchange.import_txt("ex_torus.cptw", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Set sample size and evaluate surface
surf.sample_size = 25
surf.evaluate()

# Import colormaps
from matplotlib import cm

# Plot the surface
vis_config = VisMPL.VisConfig(ctrlpts=True, axes=True, legend=False)
vis_comp = VisMPL.VisSurfTriangle(vis_config)
surf.vis = vis_comp
surf.render(colormap=cm.coolwarm)

# Good to have something here to put a breakpoint
pass
