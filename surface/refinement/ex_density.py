#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from copy import deepcopy
from geomdl import NURBS
from geomdl import operations
from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Control points
ctrlpts = [[[25.0, -25.0, 0.0, 1.0], [15.0, -25.0, 0.0, 1.0], [5.0, -25.0, 0.0, 1.0],
            [-5.0, -25.0, 0.0, 1.0], [-15.0, -25.0, 0.0, 1.0], [-25.0, -25.0, 0.0, 1.0]],
           [[25.0, -15.0, 0.0, 1.0], [15.0, -15.0, 0.0, 1.0], [5.0, -15.0, 0.0, 1.0],
            [-5.0, -15.0, 0.0, 1.0], [-15.0, -15.0, 0.0, 1.0], [-25.0, -15.0, 0.0, 1.0]],
           [[25.0, -5.0, 5.0, 1.0], [15.0, -5.0, 5.0, 1.0], [5.0, -5.0, 5.0, 1.0],
            [-5.0, -5.0, 5.0, 1.0], [-15.0, -5.0, 5.0, 1.0], [-25.0, -5.0, 5.0, 1.0]],
           [[25.0, 5.0, 5.0, 1.0], [15.0, 5.0, 5.0, 1.0], [5.0, 5.0, 5.0, 1.0],
            [-5.0, 5.0, 5.0, 1.0], [-15.0, 5.0, 5.0, 1.0], [-25.0, 5.0, 5.0, 1.0]],
           [[25.0, 15.0, 0.0, 1.0], [15.0, 15.0, 0.0, 1.0], [5.0, 15.0, 5.0, 1.0],
            [-5.0, 15.0, 5.0, 1.0], [-15.0, 15.0, 0.0, 1.0], [-25.0, 15.0, 0.0, 1.0]],
           [[25.0, 25.0, 0.0, 1.0], [15.0, 25.0, 0.0, 1.0], [5.0, 25.0, 5.0, 1.0],
            [-5.0, 25.0, 5.0, 1.0], [-15.0, 25.0, 0.0, 1.0], [-25.0, 25.0, 0.0, 1.0]]]

# Generate surface
surf = NURBS.Surface()
surf.degree_u = 3
surf.degree_v = 3
surf.ctrlpts2d = ctrlpts
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.sample_size = 30

# Set visualization component
surf.vis = VisMPL.VisSurface(VisMPL.VisConfig(alpha=0.75, figure_size=[10.66, 8]))

# Visualize
surf.render(filename="surf01.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [1, 1])

# Visualize after knot vector refinement
surf_refined.render(filename="surf02.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [2, 1])

# Visualize after knot vector refinement
surf_refined.render(filename="surf03.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [1, 2])

# Visualize after knot vector refinement
surf_refined.render(filename="surf04.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [2, 2])

# Visualize after knot vector refinement
surf_refined.render(filename="surf05.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [3, 2])

# Visualize after knot vector refinement
surf_refined.render(filename="surf06.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [2, 3])

# Visualize after knot vector refinement
surf_refined.render(filename="surf07.png", plot=False)

# Create a deep copy of the surface
surf_refined = deepcopy(surf)

# Refine knot vectors
operations.refine_knotvector(surf_refined, [3, 3])

# Visualize after knot vector refinement
surf_refined.render(filename="surf08.png", plot=False)
