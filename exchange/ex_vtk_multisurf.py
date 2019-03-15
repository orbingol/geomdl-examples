#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019

    Exporting multiple NURBS surfaces in VTK Polydata format
"""

from geomdl.shapes import surface
from geomdl import operations
from geomdl import multi
from geomdl import exchange_vtk

# Create a cylindrical surface
cylinder = surface.cylinder(radius=5.0, height=22.5)

# Decompose to generate multiple surfaces
cylinder_decomposed = operations.decompose_surface(cylinder)

# Add decomposed surfaces to a surface container
surf_container = multi.SurfaceContainer(cylinder_decomposed)

# Export evaluated points as a .vtk file
exchange_vtk.export_polydata(surf_container, "cylindrical_surface_decomposed_evalpts.vtk", tessellate=True)

# Good to have something here to put a breakpoint
pass
