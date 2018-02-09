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
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Decompose the curve into Bezier curve segments
bezier = curve.decompose()

# Move the curves a little bit away from each other (for display purposes only)
c2tan1 = bezier[1].tangent(0.0, normalize=True)
c2tanvec1 = [-1 * p for p in c2tan1[1]]
bezier[0].translate(c2tanvec1)

c2tan2 = bezier[1].tangent(1.0, normalize=True)
c2tanvec2 = [1 * p for p in c2tan2[1]]
bezier[2].translate(c2tanvec2)

# Plot the curves using the curve container
bezier.delta = 0.01

if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    bezier.vis = vis_comp
    bezier.render()

# Good to have something here to put a breakpoint
pass
