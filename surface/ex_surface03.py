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

# Set evaluation delta
surf.delta = 0.025

# Set degrees
surf.degree_u = 1
surf.degree_v = 2

# Set control points
surf.read_ctrlpts_from_txt("ex_surface03.cptw")

# Set knot vectors
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Evaluate surface
surf.evaluate()

# Draw the control point grid and the evaluated surface
if render_surf:
    # Previously using VisMPL.VisSurfWireframe()
    vis_comp = VisMPL.VisSurface()
    surf.vis = vis_comp
    surf.render()

# Save control points and evaluated curve points
surf.save_surfpts_to_csv("surfpts03_orig.csv", mode='triangle')
surf.save_ctrlpts_to_csv("ctrlpts03_orig.csv")

# Good to have something here to put a breakpoint
pass
