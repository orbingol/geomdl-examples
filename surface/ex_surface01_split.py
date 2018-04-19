#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
import os
from geomdl import BSpline

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
surf.read_ctrlpts_from_txt("ex_surface01.cpt")

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Split the surface in V-direction
surfaces = surf.split_v(t=0.5)

# Translate one of the surfaces by a vector
surfaces[0].translate((0, -2.5, 0))

# Set number of samples for all split surfaces
surfaces.sample_size = 20

# Draw the control point grid and the evaluated surface
if render_surf:
    vis_comp = VisMPL.VisSurfTriangle()
    surfaces.vis = vis_comp
    surfaces.render()

# Good to have something here to put a breakpoint
pass
