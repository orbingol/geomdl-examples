#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

from geomdl.shapes import curve2d
from geomdl import operations
from geomdl import multi
from geomdl.visualization import VisMPL


# Generate a NURBS full circle from 7 control points
circle = curve2d.full_circle2(radius=5.0)
circle.sample_size = 75

# Render the circle and the control points polygon
vis_config = VisMPL.VisConfig(ctrlpts=True, figure_size=[9, 8])
vis_comp = VisMPL.VisCurve2D(config=vis_config)
circle.vis = vis_comp
circle.render()

# Decompose the circle into Bezier curve segments
segments = operations.decompose_curve(circle)
bezier_segments = multi.CurveContainer(segments)

# Set sample size (delta)
bezier_segments.sample_size = 25

# Render the Bezier curve segments and their control points polygons
vis_config = VisMPL.VisConfig(ctrlpts=True, figure_size=[9, 8])
vis_comp = VisMPL.VisCurve2D(config=vis_config)
bezier_segments.vis = vis_comp
bezier_segments.render()

# Good to have something here to put a breakpoint
pass
