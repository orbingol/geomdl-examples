#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    The surface example is kindly contributed by John-Eric Dufour (@jedufour)
"""
import os
from geomdl import NURBS

# Try to load the visualization module
try:
    render_surf = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_surf = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degrees
surf.degree_u = 1
surf.degree_v = 2

# Set control points
surf.read_ctrlpts_from_txt("ex_surface03.cptw")

# Set knot vector
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Decompose the surface
surfaces = surf.decompose()

# Set number of samples for all split surfaces
surfaces.sample_size = 51

# Draw the control point grid and the evaluated surface
if render_surf:
    vis_comp = VisMPL.VisSurfWireframe()
    surfaces.vis = vis_comp
    surfaces.render()

# Good to have something here to put a breakpoint
pass
