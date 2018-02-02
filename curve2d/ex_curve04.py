#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
import os
from geomdl import NURBS

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS curve instance (full circle)
curve = NURBS.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve04.cptw")
curve.degree = 2
# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve2D(plot_ctrlpts=True)
    vis_comp.figure_size([8, 8])
    curve.vis = vis_comp
    curve.render()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts04_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts04_orig.csv")

# Good to have something here to put a breakpoint
pass
