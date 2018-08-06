#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

from geomdl.shapes import curve2d
from geomdl.visualization import VisMPL


# Generate a NURBS full circle from 9 control points
circle = curve2d.full_circle(radius=5.0)
circle.sample_size = 50

# Render the circle and the control points polygon
vis_config = VisMPL.VisConfig(ctrlpts=True, figure_size=[8, 8])
vis_comp = VisMPL.VisCurve2D(config=vis_config)
circle.vis = vis_comp
circle.render()

# Good to have something here to put a breakpoint
pass
