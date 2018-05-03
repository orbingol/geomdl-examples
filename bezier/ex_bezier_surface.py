#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
import os
from geomdl import BSpline
from geomdl import utilities

# Try to load the visualization module
try:
    render_surf = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_surf = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance (Bezier surface)
surf = BSpline.Surface()

# Set up the Bezier surface
surf.degree_u = 3
surf.degree_v = 2
control_points = [[0, 0, 0], [0, 4, 0], [0, 8, -3],
                  [2, 0, 6], [2, 4, 0], [2, 8, 0],
                  [4, 0, 0], [4, 4, 0], [4, 8, 3],
                  [6, 0, 0], [6, 4, -3], [6, 8, 0]]
surf.set_ctrlpts(control_points, 4, 3)
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 4)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 3)

# Set evaluation delta
surf.sample_size = 25

# Evaluate surface
surf.evaluate()

# Draw the control point grid and the evaluated surface
if render_surf:
    # Previously using VisMPL.VisSurfWireframe()
    vis_comp = VisMPL.VisSurface()
    surf.vis = vis_comp
    surf.render()
