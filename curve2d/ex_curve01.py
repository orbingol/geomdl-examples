#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange

from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 4
curve.ctrlpts = exchange.import_txt("ex_curve01.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve2D()
curve.vis = vis_comp
curve.render()

from geomdl import operations
c = operations.decompose_curve(curve)
from geomdl import helpers
cps = helpers.degree_elevation(c[0].degree, c[0].ctrlpts)

c[0].vis = VisMPL.VisCurve2D(VisMPL.VisConfig(legend=False))
# c[0].render()
from copy import deepcopy
ce = deepcopy(c[0])
ce.degree = curve.degree + 1
ce.ctrlpts = cps
ce.knotvector = utilities.generate_knot_vector(ce.degree, ce.ctrlpts_size)
# ce.render()

# Insert a knot
u = 0.2
curve.insert_knot(u)

# Plot the control point polygon and the evaluated curve after knot insertion
# curve.render()

# Good to have something here to put a breakpoint
pass
