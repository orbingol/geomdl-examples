#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities
from geomdl import construct
from geomdl import operations
from geomdl.visualization import VisMPL as vis


# Generate control points grid for Surface #1
sg01 = CPGen.Grid(15, 10, z_value=0.0)
sg01.generate(8, 8)

# Create a BSpline surface instance
surf01 = BSpline.Surface()

# Set degrees
surf01.degree_u = 1
surf01.degree_v = 1

# Get the control points from the generated grid
surf01.ctrlpts2d = sg01.grid

# Set knot vectors
surf01.knotvector_u = utilities.generate_knot_vector(surf01.degree_u, surf01.ctrlpts_size_u)
surf01.knotvector_v = utilities.generate_knot_vector(surf01.degree_v, surf01.ctrlpts_size_v)

# Generate control points grid for Surface #2
sg02 = CPGen.Grid(15, 10, z_value=1.0)
sg02.generate(8, 8)

# Create a BSpline surface instance
surf02 = BSpline.Surface()

# Set degrees
surf02.degree_u = 1
surf02.degree_v = 1

# Get the control points from the generated grid
surf02.ctrlpts2d = sg02.grid

# Set knot vectors
surf02.knotvector_u = utilities.generate_knot_vector(surf02.degree_u, surf02.ctrlpts_size_u)
surf02.knotvector_v = utilities.generate_knot_vector(surf02.degree_v, surf02.ctrlpts_size_v)

# Generate control points grid for Surface #3
sg03 = CPGen.Grid(15, 10, z_value=2.0)
sg03.generate(8, 8)

# Create a BSpline surface instance
surf03 = BSpline.Surface()

# Set degrees
surf03.degree_u = 1
surf03.degree_v = 1

# Get the control points from the generated grid
surf03.ctrlpts2d = sg03.grid

# Set knot vectors
surf03.knotvector_u = utilities.generate_knot_vector(surf03.degree_u, surf03.ctrlpts_size_u)
surf03.knotvector_v = utilities.generate_knot_vector(surf03.degree_v, surf03.ctrlpts_size_v)

# Construct the parametric volume with a uniform knot vector
pvolume = construct.construct_volume('w', surf01, surf02, surf03, degree=1)

# Visualize volume
pvolume.vis = vis.VisVolume(vis.VisConfig(ctrlpts=True, evalpts=False))
pvolume.render()

# Remove knots
pvolume.remove_knot(w=0.5)

# Visualize volume after knot removal
pvolume.render()

# Good to have something here to put a breakpoint
pass
