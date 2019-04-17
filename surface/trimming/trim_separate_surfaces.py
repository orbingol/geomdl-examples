#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from copy import deepcopy
from geomdl import BSpline
from geomdl import operations
from geomdl import multi
from geomdl import tessellate
from geomdl.visualization import VisVTK as vis
from geomdl import knotvector


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a planar BSpline surface (surface 1)
surf1 = BSpline.Surface()
surf1.degree = (1, 1)
surf1.ctrlpts_size_u = 2
surf1.ctrlpts_size_v = 2
surf1.ctrlpts = (
    (0, 0, 0), (0, 1, 0),
    (1, 0, 0), (1, 1, 0)
)
surf1.knotvector = ((0, 0, 1, 1), (0, 0, 1, 1))

# Create another surface from the initial one (surface 2)
surf2 = operations.rotate(surf1, 90, axis=1)
operations.translate(surf2, (0.5, 0, 1), inplace=True)

# Create another surface from the initial one (surface 3)
surf3 = operations.rotate(surf1, 45, axis=0)
operations.translate(surf3, (1, 0.25, 0.5), inplace=True)

# Create trim curves
trim1 = BSpline.Curve()
trim1.degree = 1
trim1.ctrlpts = (
    (1, 0), (0.95, 0.5), (1, 1), (0, 1), (0.05, 0.5), (0, 0), (1, 0)
)
trim1.knotvector = knotvector.generate(trim1.degree, trim1.ctrlpts_size)
trim1.delta = 0.001
trim1.opt = ['reversed', 1]
# operations.scale(trim1, 0.5, inplace=True)

trim2 = deepcopy(trim1)
trim2.opt = ['reversed', 0]

# Add trim to surface 1
surf1.trims = [trim1]

# Add trim to surface 3
surf3.trims = [trim2]

# Visualize all surfaces
mult = multi.SurfaceContainer(surf1, surf2, surf3)
mult.sample_size = 30
mult.tessellator = tessellate.TrimTessellate()

# Show trim curves but don't show control points
vis_conf = vis.VisConfig(trims=True, ctrlpts=False)
mult.vis = vis.VisSurface(vis_conf)

# Render with colors
# mult.render(evalcolor=["steelblue", "red", "green"])

from geomdl import exchange
exchange.export_json(mult, "mult.json")
