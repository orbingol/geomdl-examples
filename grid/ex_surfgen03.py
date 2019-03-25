#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under the MIT License
    Developed by Onur Rauf Bingol (c) 2018

    This example illustrates the following operations:

    * Generating a control points grid
    * Generating a B-Spline surface and using the generated grid as its control points input
    * Plotting the surface using Matplotlib
    * Exporting the surface as a .stl file
"""


from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities
from geomdl.visualization import VisMPL as vis
from geomdl import exchange

# Generate a control points grid
surfgrid = CPGen.Grid(100, 100)

# This will generate a 8x8 grid
surfgrid.generate(8, 8)

# Generate 1 bump at the center of the grid
surfgrid.bumps(num_bumps=1, bump_height=20, base_extent=4, base_adjust=-1)

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Get the control points from the generated grid
surf.ctrlpts2d = surfgrid.grid

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# Set sample size of the surface
surf.sample_size = 50

# Generate the visualization component and its configuration
vis_config = vis.VisConfig(ctrlpts=True, legend=False)
vis_comp = vis.VisSurface(vis_config)

# Set visualization component of the surface
surf.vis = vis_comp

# Plot the surface
surf.render()

# Export the surface as a .stl file
exchange.export_stl(surf, "bump_smoother_1pt-padding.stl")

# Good to have something here to put a breakpoint
pass
