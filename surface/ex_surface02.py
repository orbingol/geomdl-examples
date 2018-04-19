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

# Try to load the visualization module
try:
    render_surf = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_surf = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.read_ctrlpts_from_txt("ex_surface02.cpt")

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 6)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 6)

# Set evaluation delta
surf.delta = 0.025

# Evaluate surface
surf.evaluate()

# Draw the control point grid and the evaluated surface
if render_surf:
    vis_comp = VisMPL.VisSurfScatter()
    surf.vis = vis_comp
    surf.render()

# Save control points and evaluated curve points
surf.save_surfpts_to_csv("surfpts02_orig.csv", mode='linear')
surf.save_ctrlpts_to_csv("ctrlpts02_orig.csv", mode='wireframe')

# Evaluate surface tangent and normal at the given u and v
uv = [0.2, 0.9]
surf_tangent = surf.tangent(uv[0], uv[1])
surf_normal = surf.normal(uv[0], uv[1])

# Good to have something here to put a breakpoint
pass
