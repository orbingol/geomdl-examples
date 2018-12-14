#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017

    This example is contributed by John-Eric Dufour (@jedufour)
"""

import os
from geomdl import NURBS
from geomdl import construct
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
surf.set_ctrlpts(*exchange.import_txt("ex_cylinder.cptw", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Set evaluation delta
surf.delta = 0.05

surf_curves = construct.extract_curves(surf)
plot_extras = [
    dict(
        points=surf_curves['u'][0].evalpts,
        name="u",
        color="cyan",
        size=15
    ),
    dict(
        points=surf_curves['v'][0].evalpts,
        name="v",
        color="magenta",
        size=5
    )
]

# Plot the control point grid and the evaluated surface
surf.vis = vis.VisSurface()
surf.render(extras=plot_extras)

# Good to have something here to put a breakpoint
pass
