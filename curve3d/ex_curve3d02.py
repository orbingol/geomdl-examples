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

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve3d02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve3D()
    curve.vis = vis_comp
    curve.render()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts3d02_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts3d02_orig.csv")

# Good to have something here to put a breakpoint
pass
