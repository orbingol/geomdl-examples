#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Exporting a NURBS surface as .stl file
"""

from geomdl.shapes import surface
from geomdl import exchange

cylinder = surface.cylinder(radius=5.0, height=22.5)

# Export the surface as a .stl file
exchange.export_stl(cylinder, "cylindrical_surface.stl")

# Good to have something here to put a breakpoint
pass
