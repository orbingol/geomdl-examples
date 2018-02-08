#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
from geomdl.shapes import curve2d

# Try to load the visualization module
try:
    render = True
    from geomdl.visualization import VisMPL
except ImportError:
    render = False

# Generate a NURBS full circle from 9 control points
circle = curve2d.full_circle(radius=5.0)
circle.delta = 0.01

# Render the circle and the control points polygon
if render:
    vis_comp = VisMPL.VisCurve2D(plot_ctrlpts=True)
    vis_comp.figure_size([8, 8])
    circle.vis = vis_comp
    circle.render()

# Good to have something here to put a breakpoint
pass
