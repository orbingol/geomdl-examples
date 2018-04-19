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
from geomdl import Multi

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Split the curve
curve1, curve2 = curve.split(0.2)

# Move the 1st curve a little bit far away from the 2nd curve
c2tan = curve2.tangent(0.0, normalize=True)
c2tanvec = [-1 * p for p in c2tan[1]]
curve1.translate(c2tanvec)

# Plot the curves using the curve container
curves = Multi.MultiCurve()
curves.sample_size = 40
curves.add(curve1)
curves.add(curve2)
if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    curves.vis = vis_comp
    curves.render()

# Good to have something here to put a breakpoint
pass
