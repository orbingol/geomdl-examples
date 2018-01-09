# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""
from geomdl import BSpline
from geomdl import utilities

# Try to load the visualization module
try:
    render_curve = True
    from geomdl.visualization import VisMPL
except ImportError:
    render_curve = False

# Create a B-Spline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve01.cpt")
curve.degree = 4

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaluate curve
curve.evaluate()

# Draw the control point polygon and the evaluated curve
if render_curve:
    vis_comp = VisMPL.VisCurve2D()
    curve.vis = vis_comp
    curve.render()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts01_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts01_orig.csv")

# Insert a knot
u = 0.2
curve.insert_knot(u)

# Draw the control point polygon and the evaluated curve after knot insertion
if render_curve:
    curve.render()

# Save control points and evaluated curve points after knot insertion
curve.save_curvepts_to_csv("curvepts01_knotins.csv")
curve.save_ctrlpts_to_csv("ctrlpts01_knotins.csv")

# Good to have something here to put a breakpoint
pass
