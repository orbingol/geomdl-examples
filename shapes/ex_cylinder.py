#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
from geomdl.shapes import surface

# Try to load the visualization module
try:
    render = True
    from geomdl.visualization import VisMPL
except ImportError:
    render = False

cylinder = surface.cylinder(radius=5.0, height=22.5)
cylinder.delta = 0.05

# Render the surface
if render:
    vis_comp = VisMPL.VisSurface(plot_ctrlpts=False)
    cylinder.vis = vis_comp
    cylinder.render()

# Good to have something here to put a breakpoint
pass
