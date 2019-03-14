#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019

    Exporting a NURBS surface in VTK Polydata format
"""

from geomdl.shapes import surface
from geomdl import exchange_vtk

cylinder = surface.cylinder(radius=5.0, height=22.5)

# Export the surface as a .obj file
exchange_vtk.export_polydata(cylinder, "cylindrical_surface.vtk")

# Good to have something here to put a breakpoint
pass
