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

# Create a cylindrical surface
cylinder = surface.cylinder(radius=5.0, height=22.5)

# Export evaluated points as a .vtk file
exchange_vtk.export_polydata(cylinder, "cylindrical_surface_evalpts.vtk", tessellate=True)

# Export control points as a .vtk file (optionally tessellated as quads)
exchange_vtk.export_polydata(cylinder, "cylindrical_surface_ctrlpts.vtk", point_type="ctrlpts", tessellate=False)

# Good to have something here to put a breakpoint
pass
