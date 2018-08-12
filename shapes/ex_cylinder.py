#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
from geomdl.shapes import surface
from geomdl.visualization import VisMPL


# Generate a cylindrical surface using the shapes component
cylinder = surface.cylinder(radius=5.0, height=22.5)
cylinder.sample_size = 20

# Render the surface
vis_config = VisMPL.VisConfig(ctrlpts=True)
vis_comp = VisMPL.VisSurface(config=vis_config)
cylinder.vis = vis_comp
cylinder.render()

# Good to have something here to put a breakpoint
pass
