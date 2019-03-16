#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl import knotvector
from geomdl import operations
from geomdl import tessellate
from geomdl.visualization import VisVTK as vis
from geomdl.shapes import curve2d


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

########################
# GENERATE TRIM CURVES #
########################

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 1

# Set control points
curve.ctrlpts = [[1.1, 1.1], [0.24, 1.1], [0.24, 1.1], [0.24, 0.49], [0.24, 0.49], [1.1, 0.49], [1.1, 0.49], [1.1, 1.1]]

# Auto-generate knot vector
curve.knotvector = knotvector.generate(curve.degree, curve.ctrlpts_size)

# Translate original curve to generate 1st trim curve
trim_curve1 = operations.translate(curve, (0.25, 0.25))

# Translate original curve to generate 2nd trim curve
trim_curve2 = operations.translate(curve, (-0.75, -0.75))

# Generate a NURBS full circle from 9 control points
circle = curve2d.full_circle(radius=0.15)

# Translate circle
operations.translate(circle, (0.5, 0.5), inplace=True)

# Set evaluation deltas
trim_curve1.delta = 0.01
trim_curve2.delta = 0.01
circle.delta = 0.01

# List of trim curves
trim_curves = [trim_curve1, trim_curve2, circle]

####################
# GENERATE SURFACE #
####################

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("../ex_surface01.cpt", two_dimensional=True))

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set evaluation delta
surf.delta = 0.015

# Set surface tessellation component
surf.tessellator = tessellate.TrimTessellate()

# Set trim curves
surf.trims = trim_curves

# Set visualization component
visconf = vis.VisConfig(ctrlpts=False, legend=False, trims=False)
surf.vis = vis.VisSurface(config=visconf)

# Visualize surface
surf.render()

# Save as Wavefront OBJ file
# exchange.export_obj(surf, "trim_multi.obj")

# Good to have something here to put a breakpoint
pass
